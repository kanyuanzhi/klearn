import numpy as np
import matplotlib.pyplot as plt
from math import pow


class KNN:
    def __init__(self, points, tags, test_point, k=5):
        self.points = points
        self.tags = tags
        self.test_point = test_point
        self.k = k

    def __train(self):
        # distance = []
        distance = {}
        for i in range(len(self.points)):
            distance[i] = self.__distance(self.test_point, self.points[i])
            # distance.append({'point': i, 'd': self.__distance(self.test_point, self.points[i]))
        sorted(distance.items(), key=lambda item: item[1])
        k_distance = distance[0:k]
        k_tags = [self.tags[i] for i in ]

        pass

    def __distance(point_a, point_b):
        """
        Euclidean distance
        """
        delta = [pow(point_a[i] - point_b[i], 2) for i in range(len(point_a))]
        return pow(sum(delta), 0.5)


if __name__ == "__main__":
    n = 20
    x = np.random.randint(-10, 10, size=(2, n))
    y = np.random.randint(0, 2, size=(1, n))
    x0 = []
    x1 = []
    for i in range(len(y[0])):
        if y[0][i] == 0:
            x0.append(x.T[i])
        else:
            x1.append(x.T[i])
    x0 = np.array(x0).T
    x1 = np.array(x1).T
    print x0
    print x1
    plt.scatter(x0[0], x0[1], c='red')
    plt.scatter(x1[0], x1[1], c='blue')
    plt.show()
    print x
    print y
