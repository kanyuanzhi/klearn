# coding=utf-8
import numpy as np


class KDTree(object):
    def __init__(self, points):
        points_to_dictionary = []
        for i in range(len(points)):
            points_to_dictionary.append({'index': i, 'coordinate': points[i]})

        self.dimensions = np.shape(points)[1]  # 维度

        self.root = self.__create(points_to_dictionary, 0)
        # self.scan_tree()

    @staticmethod
    def __midian(a, j):
        """
        求中位数
        :param a:
        :param j: 按第j个维度
        :return:
        """
        length = len(a)
        a.sort(key=lambda x: (x['coordinate'][j]))
        middle = length / 2
        return a[middle]

    def __create(self, a, j):
        """
        递归生成kd树
        :param a: 待划分数据集
        :param j: 选择划分维度
        :return:
        """
        if len(a) == 1:
            a[0]['dimension'] = j
            return Node(a[0])
        else:
            middle_a = self.__midian(a, j)
            middle_index = len(a) / 2
            middle_a['dimension'] = j
            root_node = Node(middle_a)

            left_a = a[:middle_index]
            right_a = a[middle_index + 1:]

            left_node = self.__create(left_a, (j + 1) % self.dimensions)
            left_node.location = 'left'
            root_node.left = left_node
            left_node.parent = root_node

            if len(a) > 2:  # or len(right_a)>0，此处由于偶数长度序列取中位数时取的是中间两个数中右侧的一个，导致右序列可能为空
                right_node = self.__create(right_a, (j + 1) % self.dimensions)
                right_node.location = 'right'
                root_node.right = right_node
                right_node.parent = root_node

            return root_node

    def scan_tree(self):
        queue = []
        queue.append(self.root)
        cur_dimension = 0
        count = 1
        print count, "layer"
        while queue:
            current = queue.pop(0)
            if current.value['dimension'] != cur_dimension:
                count = count + 1
                cur_dimension = current.value['dimension']
                print '\t'
                print count, "layers"
            print current.value['coordinate']
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)


class Node(object):
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.location = None
        self.visited = False  # 回溯时判断是否访问过
