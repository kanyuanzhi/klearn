# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from math import pow
from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D


class KNN():
    def __init__(self, points, tags, test_point, k=5, draw_flag=True):
        """
        初始化
        :param points: 训练集
        :param tags: 训练集对应标签
        :param test_point: 待分类点
        :param k: k值
        :param draw_flag: 是否绘制2D或3D图形
        """
        self.points = points
        self.tags = tags
        self.test_point = test_point
        if k > len(points):
            self.k = len(points)
        elif k < 1:
            print "k must be bigger than 0!"
        else:
            self.k = k
        self.result = self.__train()

        dimensions = np.shape(points)[1]  # 维度

        if draw_flag:
            if dimensions == 2 or dimensions == 3:
                self.__draw(dimensions)
            else:
                print "can only draw a graph in 2D or 3D!"

    def __train(self):
        # distance = []
        distance = {}
        for i in range(len(self.points)):
            distance[i] = self.__distance(self.test_point, self.points[i])
        distance_list = sorted(distance.items(), key=lambda item: item[1])
        # print distance_list
        # print distance_list[3]
        k_distance = distance_list[0:self.k]
        # print k_distance
        k_tags = [self.tags[kd[0]] for kd in k_distance]
        tag_count = {}  # 每个标签有多少个
        for kt in k_tags:
            if kt in tag_count:
                tag_count[kt] = tag_count[kt] + 1
            else:
                tag_count[kt] = 1
        tag_count_list = sorted(
            tag_count.items(), key=lambda item: item[1], reverse=True)
        # print tag_count_list
        result = tag_count_list[0][0]
        return result

    def __draw(self, dimensions):
        """
        绘图
        :param dimensions: 数据维度
        :return:
        """
        col_gen = cycle('bgrcmk')
        all_tag_count = {}  # 每个标签有多少个
        tag = []  # 标签类别
        xs = []  # 将训练集按标签划分
        for i in range(len(self.tags)):
            if self.tags[i] in all_tag_count:
                all_tag_count[self.tags[i]] = all_tag_count[self.tags[i]] + 1
                xs[tag.index(self.tags[i])].append(self.points[i])
            else:
                all_tag_count[self.tags[i]] = 1
                tag.append(self.tags[i])
                xs.append([self.points[i]])

        if dimensions == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            for i in range(len(xs)):
                item_matrix = np.array(xs[i]).T
                ax.scatter(item_matrix[0], item_matrix[1],
                           c=col_gen.next(), marker='.', label=tag[i])
            ax.scatter(self.test_point[0],
                       self.test_point[1], c='black', marker='*', label='test_point')
            plt.legend()
            plt.show()
        if dimensions == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            for i in range(len(xs)):
                item_matrix = np.array(xs[i]).T
                ax.scatter(item_matrix[0], item_matrix[1], item_matrix[2], c=col_gen.next(
                ), marker='.', label=tag[i])
            ax.scatter(self.test_point[0], self.test_point[1],
                       self.test_point[2], c='black', marker='*', label='test_point')
            plt.legend()
            plt.show()

    def __distance(self, point_a, point_b):
        """
        Euclidean distance
        """
        delta = [pow(point_a[i] - point_b[i], 2) for i in range(len(point_a))]
        return pow(sum(delta), 0.5)

    def get_result(self):
        return self.result


class KDTree():
    def __init__(self, value, left, right, parent):
        self.value = arg
        self.left = left
        self.right = right
        self.parent = parent


if __name__ == "__main__":
    n = 1000
    # np.random.seed(10)
    x = np.random.randint(-100, 100, size=(3, n))
    y = np.random.randint(0, 3, size=(1, n))
    print x
    print y
    test_point = [3, 4, 100]
    knn = KNN(x.T, y[0], test_point, 5)
    tag = knn.get_result()
    print tag
