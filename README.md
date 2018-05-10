# kan_ML

## setup

> python setup.py install<br>
> pip install numpy,matplotlib

## Sensor

### use

```python
from kan_ml.sensor import Sensor

sensor = Sensor(x, y, eta, epoch, draw=True)
"""
:param eta: learning rate
:param epoch: maximum number of cycles
:param draw: whether draw a graph in 2D (default False)
"""
[w,b] = sensor.get_paras()
```

### example
```python
x = np.array([(3, 4, 1), (3, 3, 1)]).T
y = np.array([(1, 1, -1)]).T
sensor = Sensor(x, y, 0.3, 20, draw=True)
[w, b] = sensor.get_paras()
```
![image](https://github.com/kanyuanzhi/kan_ML/raw/master/docs/images/sensor.png)

## KNN

### use

```python
from kan_ml.knn import KNN

knn = KNN(x, tags, test_point, k, draw=True)
"""
:param x: training set
:param tags: tags of training set
:param test_point: point to be classified
:param k: k value in knn
:param draw: whether draw a graph in 2D or 3D(default False)
"""
tag = knn.get_result()
```

### example
```python
n = 1000
x = np.random.randint(-100, 100, size=(3, n))
y = np.random.randint(0, 3, size=(1, n))
test_point = [3, 4, 100]
knn = KNN(x.T, y[0], test_point, 5, draw=True)
tag = knn.get_result()
```
![image](https://github.com/kanyuanzhi/kan_ML/raw/master/docs/images/knn_3d.png)

### kdTree

The toolbox also provide kdTree to store data in knn:

#### use independently

```python
from kan_ml.kdtree import KDTree

kdtree = KDTree(x)
kdtree.scan_tree()
```

#### use in knn

```python
knn = KNN(x, tags, test_point, k, kdtree=True)
"""
:param kdtree: whether use kdtree to store and train your data(default False)
"""
```