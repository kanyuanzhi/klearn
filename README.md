# kan_ML

## setup

> python setup.py install<br>
> pip install numpy,matplotlib

## Sensor

### use

```python
import kan_ml.sensor as kmls

sensor = kmls.Sensor(x, y, eta, epoch, (boolen)draw_flag)
"""
:param eta: learning rate
:param epoch: maximum number of cycles
:param draw_flag: whether draw a graph in 2D (default True)
"""
[w,b] = sensor.get_paras()
```

### example
```python
x = np.array([(3, 4, 1), (3, 3, 1)]).T
y = np.array([(1, 1, -1)]).T
sensor = Sensor(x, y, 0.3, 20, True)
[w, b] = sensor.get_paras()
```

## KNN

### use

```python
import kan_ml.KNN as kmls

knn = KNN(x, tags, test_point, k, (boolen)draw_flag)
"""
:param x: training set
:param tags: tags of training set
:param test_point: point to be classified
:param draw_flag: whether draw a graph in 2D or 3D(default True)
"""
tag = knn.get_result()
```

### example
```python
n = 1000
x = np.random.randint(-100, 100, size=(3, n))
y = np.random.randint(0, 3, size=(1, n))
test_point = [3, 4, 100]
knn = KNN(x.T, y[0], test_point, 5)
tag = knn.get_result()
```
![image](https://github.com/kanyuanzhi/kan_ML/raw/master/docs/images/knn_3d.png)
