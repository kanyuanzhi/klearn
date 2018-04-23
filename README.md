# kan_ML

## setup

> python setup.py install
> pip install numpy,matplotlib

## Sensor

### use

```python
import kan_ml.sensor as kmls

sensor = kmls.Sensor(x,y,eta,epoch,(boolen)draw_flag)
"""
:param eta: learning rate
:param epoch: maximum number of cycles
:param draw_flag: whether draw a graph in 2D
"""
[w,b] = sensor.get_paras
```
