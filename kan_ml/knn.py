# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from math import pow
from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D
from kdtree import KDTree


class KNN(object):
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

        self.dimensions = np.shape(points)[1]  # 维度

        self.__train_by_kdtree()

        if draw_flag:
            if self.dimensions == 2 or self.dimensions == 3:
                self.__draw(self.dimensions)
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
        tag_count_list = sorted(tag_count.items(), key=lambda item: item[1], reverse=True)
        # print tag_count_list
        result = tag_count_list[0][0]
        return result

    def __train_by_kdtree(self):
        candidate_point = []
        kdtree = KDTree(self.points)
        current_node = kdtree.root
        # while root_check(current_node) and len
        # j = 0
        # while True:
        #     if current_node.left is not None:
        #         if self.test_point[j % self.dimensions] <= current_node.value['coordinate'][j % self.dimensions]:
        #             current_node = current_node.left
        #         else:
        #             if current_node.right is not None:
        #                 current_node = current_node.right
        #             else:
        #                 current_node = current_node.left
        #                 break
        #     else:
        #         break
        #     j = j + 1

        close_in_node = current_node
        close_in_distance = self.__distance(
            close_in_node.value['coordinate'], self.test_point)
        print close_in_node.value
        print close_in_distance
        # while current_node.parent is not None:

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


if __name__ == "__main__":
    n = 500
    np.random.seed(10)
    x = np.random.randint(0, 200, size=(3, n))
    y = np.random.randint(0, 3, size=(1, n))
    # print x.T
    # print y
    test_point = [3, 4, 50]
    # knn = KNN(x.T, y[0], test_point, 5, False)
    # tag = knn.get_result()
    # print "predicted tag:", tag
    xx = np.array([(2, 5, 9, 4, 8, 7), (3, 4, 6, 7, 1, 2)])
    yy = np.random.randint(0, 2, size=(1, 6))
    test_pointt = [4, 3]
    knn = KNN(xx.T, yy[0], test_pointt, 5, True)
    tag = knn.get_result()
    # ktree = KDTree(xx.T)
