# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from random import choice


def sign(a):
    a[a >= 0] = 1
    a[a < 0] = -1
    return a


class Sensor:
    def __init__(self, x, y, eta=0.3, epoch=20, **args):
        """
        初始化
        :param x:
        :param y:
        :param eta: 学习速率
        :param epoch: 最大循环次数
        """
        self.x = x
        self.y = y
        self.eta = eta
        self.epoch = epoch
        self.count = 1

        self.x_rows = x.shape[0]
        self.x_cols = x.shape[1]

        self.y_rows = y.shape[0]
        self.y_cols = y.shape[1]

        self.w = np.random.rand(self.x_cols, self.y_cols)
        self.b = np.random.rand()
        self.w_list = [self.w]
        self.b_list = [self.b]

        self.__train()
        self.__to_string()

        if 'draw' in args:
            draw_flag = args['draw']
        else:
            draw_flag = False

        if draw_flag:
            if self.x_cols <= 2:
                self.__draw()
            else:
                print "can not draw in 2D graph!"

    def __train(self):
        a = sign(np.dot(self.x, self.w) + self.b)
        # loss = np.sum(self.y * (np.dot(self.x, self.w) + self.b)) * (-1)
        # print "loss:", loss
        delta = a * self.y
        wrong_point_index = []
        wrong_x = []
        wrong_y = []
        for i in range(self.y_rows):
            if delta[i][0] < 0:
                wrong_point_index.append(i)
                wrong_x.append(self.x[i])
                wrong_y.append(self.y[i])
        if len(wrong_point_index) > 0:
            loss = np.sum(
                np.array(wrong_y) * (np.dot(np.array(wrong_x), self.w) + self.b)) * (-1)  # 损失函数
        else:
            loss = 0
        # print loss

        while len(wrong_point_index) > 0 and self.count < self.epoch:
            select_index = choice(wrong_point_index)  # 随机梯度
            dw = self.eta * \
                np.array([self.x[select_index]]).T * self.y[select_index][0]
            db = self.eta * self.y[select_index][0]
            self.w = self.w + dw
            self.b = self.b + db
            self.w_list.append(self.w)
            self.b_list.append(self.b)

            a = sign(np.dot(self.x, self.w) + self.b)
            delta = a * self.y
            wrong_point_index = []
            wrong_x = []
            wrong_y = []
            for i in range(self.y_rows):
                if delta[i][0] < 0:
                    wrong_point_index.append(i)
                    wrong_x.append(self.x[i])
                    wrong_y.append(self.y[i])
            if len(wrong_point_index) > 0:
                loss = np.sum(
                    np.array(wrong_y) * (np.dot(np.array(wrong_x), self.w) + self.b)) * (-1)
            else:
                loss = 0
            # print loss
            self.count = self.count + 1

    def __draw(self):
        x1 = []
        x2 = []
        for point in self.x:
            x1.append(point[0])
            x2.append(point[1])
        plt.scatter(x1, x2)
        x = np.linspace(-10, 10)
        for i in range(len(self.w_list)):
            y = (self.w_list[i][0] * x + self.b_list[i]) / (-self.w_list[i][1])
            plt.plot(x, y, label=i)
        plt.legend()
        plt.show()

    def __to_string(self):
        print "w:", self.w
        print "b:", self.b
        print "epoch:", self.count

    def get_paras(self):
        return [self.w, self.b]


if __name__ == "__main__":
    x = np.array([(3, 4, 1), (3, 3, 1)]).T
    y = np.array([(1, 1, -1)]).T
    print x
    print y
    sensor = Sensor(x, y, 0.3, 20, draw=True)
    [w, b] = sensor.get_paras()
    print sign(np.dot(x, w) + b)
