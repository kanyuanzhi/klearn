import numpy as np
import matplotlib.pyplot as plt


class KNN:
    def __init__(self, points, k=5):
        self.points = points
        self.k = k


if __name__ == "__main__":
    x = np.random.randint(-10, 10, size=(2, 10))
    plt.scatter(x[0], x[1])
    plt.show()
    print x
