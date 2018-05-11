# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from math import pow
from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D
from kdtree import KDTree
import time


class KNN(object):
    def __init__(self, points, tags, test_point, k=5, **args):
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
        self.dimensions = np.shape(points)[1]  # 维度
        self.k_points = []  # k个与test_point最近的点
        if k > len(points):
            self.k = len(points)
        elif k < 1:
            print "k must be bigger than 0!"
            return
        else:
            self.k = k

        if 'draw' in args:
            draw_flag = args['draw']
        else:
            draw_flag = False

        if 'kdtree' in args:
            kdtree_flag = args['kdtree']
        else:
            kdtree_flag = False

        if kdtree_flag:
            self.result = self.__train_by_kdtree()
        else:
            self.result = self.__train()

        if draw_flag:
            if self.dimensions == 2 or self.dimensions == 3:
                self.__draw(self.dimensions)
            else:
                print "can only draw a graph in 2D or 3D!"

    def __train(self):
        # distance = []
        distance = {}
        for i in range(len(self.points)):
            distance[i] = KNN.__distance(self.test_point, self.points[i])
        distance_list = sorted(distance.items(), key=lambda item: item[1])
        # print distance_list
        # print distance_list[3]
        k_distance = distance_list[0:self.k]

        self.k_point = []
        for k in k_distance:
            self.k_points.append(self.points[k[0]])

        k_tags = [self.tags[kd[0]] for kd in k_distance]  # 前k个点的标签是多少
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

    def __train_by_kdtree(self):
        candidate_point = []
        kdtree = KDTree(self.points)
        # kdtree.scan_tree()

        current_node = self.find_leaf(kdtree.root, self.test_point)
        # close_in_distance = KNN.__distance(close_in_node.value['coordinate'], self.test_point)
        # candidate_point.append({'node': close_in_node, 'distance': close_in_distance})
        while True:
            """
            算法描述：

            如果candidate_point长度不等于k，则判断current_node是否访问过：
            若访问过，则一直爬到其未被访问过的父节点，
                若爬到父节点为根节点，若访问过，结束，若没有访问过，比较candidate_point的最大距离是否大于test_point到current_node切分线
                的垂直距离，若大于，进入另一侧，找到叶节点，重复，若不大于，结束，
                若不是父节点，重复；
            若没有访问过，则将current_node加入候选序列，然后比较candidate_point的最大距离是否大于test_point到current_node切分线的垂直距离，若大于，
            进入current另一侧找到叶节点，重复，若不大于，则一直爬到其未被访问过的父节点，若爬到父节点为根节点，若访问过，结束，若没有访问过，
            比较candidate_point的最大距离是否大于test_point到current_node切分线的垂直距离，若大于，进入另一侧，找到叶节点，重复，
            若不大于，结束；

            如果candidate_point长度等于k，则判断current_node是否访问过：
            若访问过，则一直爬到其未被访问过的父节点，
                若爬到父节点为根节点，若访问过，结束，若没有访问过，比较candidate_point的最大距离是否大于test_point到current_node切分线
                的垂直距离，若大于，进入另一侧，找到叶节点，重复，若不大于，结束，
                若不是父节点，重复；
            若没有访问过，则比较distance(current_node,test_node)是否大于candidate_point中最大距离，若小于，则替换掉candidate_point中的最大距离，
            然后比较candidate_point的最大距离是否大于test_point到current_node切分线的垂直距离，若大于，则进入另一侧找到叶节点，重复，
            若不大于，则一直爬到其为被访问过的父节点，若该父节点为根节点，若访问过，结束，若没有访问过，比较candidate_point的最大距离
            是否大于test_point到current_node切分线的垂直距离，若大于，进入另一侧，找到叶节点，重复，若不大于，结束；
            """
            while current_node.visited:
                if current_node.parent is None:
                    break
                previous_node = current_node
                current_node = current_node.parent

            if current_node.parent is None:
                if current_node.visited:
                    break

            if len(candidate_point) != self.k:
                current_distance = KNN.__distance(
                    current_node.value['coordinate'], self.test_point)
                current_node.visited = True
                candidate_point.append(
                    {'node': current_node, 'distance': current_distance})
                if current_node.left is None:
                    continue
            else:
                current_distance = KNN.__distance(
                    current_node.value['coordinate'], self.test_point)
                candidate_point.sort(key=lambda x: x['distance'])
                if current_distance < candidate_point[self.k - 1]['distance']:
                    current_node.visited = True
                    candidate_point.pop()
                    candidate_point.append(
                        {'node': current_node, 'distance': current_distance})
                else:
                    current_node.visited = True
                if current_node.left is None:
                    continue

            # if current_node.left is not None:会执行以下部分
            if self.intersect_check(candidate_point, current_node):
                location = previous_node.location
                if location == 'left':
                    if current_node.right is None:
                        continue
                    else:
                        current_node = self.find_leaf(
                            current_node.right, self.test_point)
                        continue
                if location == 'right':
                    if current_node.left is None:
                        continue
                    else:
                        current_node = self.find_leaf(
                            current_node.left, self.test_point)
            else:
                continue

        self.k_point = []
        for cd in candidate_point:
            self.k_points.append(cd['node'].value['coordinate'])

        k_tags = [self.tags[cd['node'].value['index']]
                  for cd in candidate_point]  # 前k个点的标签是多少
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

    def intersect_check(self, candidate_point, current_node):
        candidate_point.sort(key=lambda x: (x['distance']))
        d = current_node.value['dimension']
        if candidate_point[len(candidate_point) - 1]['distance'] >= np.abs(
                self.test_point[d] - current_node.value['coordinate'][d]):
            return True
        else:
            return False

    def find_leaf(self, current_node, test_node):
        d = current_node.value['dimension']
        while True:
            if current_node.left is not None:
                if test_node[d % self.dimensions] <= current_node.value['coordinate'][d % self.dimensions]:
                    current_node = current_node.left
                else:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node = current_node.left
                        return current_node
                d = d + 1
            else:
                return current_node

    @staticmethod
    def root_check(node):
        if node.parent is None:
            return True
        else:
            return False

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

    @staticmethod
    def __distance(point_a, point_b):
        """
        Euclidean distance
        """
        delta = [pow(point_a[i] - point_b[i], 2) for i in range(len(point_a))]
        return pow(sum(delta), 0.5)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    n = 50000
    # np.random.seed(100)
    x = np.random.randint(0, 500, size=(8, n))
    y = np.random.randint(0, 3, size=(1, n))
    # print x.T
    # print y
    test_point = [3, 4, 50, 409, 323, 534, 654, 21]
    knn = KNN(x.T, y[0], test_point, 20, draw=True, kdtree=False)
    knn1 = KNN(x.T, y[0], test_point, 20, draw=True, kdtree=True)
    print knn.get_result(), knn1.get_result()
    # tag = knn.get_result()
    # print "predicted tag:", tag
    # xx = np.array([(2, 5, 9, 4, 8, 7), (3, 4, 6, 7, 1, 2)])
    # yy = np.random.randint(0, 2, size=(1, 6))
    # test_pointt = [4, 3]
    # knn = KNN(xx.T, yy[0], test_pointt, 5, False)
    # tag = knn.get_result()
    # ktree = KDTree(xx.T)
