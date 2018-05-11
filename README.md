# KLearn

## Introduction

KLearn is a toolbox for machine learning & data mining(developing).

## Setup

> python setup.py install<br>
> pip install numpy,matplotlib

or

> pip install klearn

notes: setup with pip may not install the latest version!

## Sensor

### use

```python
from klearn.sensor import Sensor

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
from klearn.knn import KNN

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
from klearn.kdtree import KDTree

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

## Naive Bayes

### use

```python
from klearn.bayes import Bayes

bayes = Bayes(x, tags, test_x, show=True)
"""
:param show: whether show probabilities in training(default False)
"""
tag = bayes.get_result()
```

### exapmle 1

```python
n = 200
dimensions = 5
x = np.random.randint(0, 4, size=(dimensions, n))
y = np.random.randint(0, 3, size=(1, n))
x_test = np.random.randint(0, 4, size=(1, dimensions))
bayes = Bayes(x, y[0], x_test[0])
```

### example 2

```python
x = [[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
    ['S', 'M', 'M', 'S', 'S', 'S', 'M', 'M', 'L', 'L', 'L', 'M', 'M', 'L', 'L']]
y = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
test_x = [2, 'S']
bayes = Bayes(x, y, test_x, show=True)
print bayes.get_result()
```

output in console:

>prior probabilities:
>P(Y=1)=0.6
>P(Y=-1)=0.4
>
>conditional_probabilities:
>P(X(0)=1|Y=1)=0.222222222222    P(X(0)=2|Y=1)=0.333333333333    P(X(0)=3|Y=1)=0.444444444444    
>P(X(1)=S|Y=1)=0.111111111111    P(X(1)=M|Y=1)=0.444444444444    P(X(1)=L|Y=1)=0.444444444444    
>P(X(0)=1|Y=-1)=0.5  P(X(0)=2|Y=-1)=0.333333333333   P(X(0)=3|Y=-1)=0.166666666667   
>P(X(1)=S|Y=-1)=0.5  P(X(1)=M|Y=-1)=0.333333333333   P(X(1)=L|Y=-1)=0.166666666667   
>
>posterior_probabilities:
>P(Y=1)P(X(0)=2|Y=1)P(X(1)=S|Y=1)=0.0222222222222
>P(Y=-1)P(X(0)=2|Y=-1)P(X(1)=S|Y=-1)=0.0666666666667
>
>-1
