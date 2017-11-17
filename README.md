# lidar filters

Tested with python2.7 and python3.6

## Range filter
The range filter crops all the values that are below range_min (resp. above range_max), 
and replaces them with the range_min value (resp. range_max)

## Temporal median filter
The temporal median filter returns the median of the current and the previous D scans:

`y_i(t)= median(x_i(t), x_i(t−1), ..., x_i(t−D))`

where x and y are input and output length-N scans and i ranges from 0 to N-1. The number 
of previous scans D is a parameter that should be given when creating a new temporal 
median filter. Note that, although the update method will receive a single scan, the 
returned array depends on the values of previous scans. Note also that the for the 
first D scans, the filter is expected to return the median of all the scans so far.

## Build and Install

``` $ python setup.py build install ```

## Usage

```python

#RangeFilter
import lidar_filter.range_filter as rf

rfilter = rf.RangeFilter(-75, 75)
rfilter.update(np.array([100, -100, 50, -50, 0]))

#TemporalMedianFilter
import lidar_filter.temporal_median as tm

tmed = tm.TemporalMedianFilter(3)
test_list = [
    [0.0, 1.0, 2.0, 1.0, 3.0],
    [1.0, 5.0, 7.0, 1.0, 3.0],
    [2.0, 3.0, 4.0, 1.0, 0.0], 
    [3.0, 3.0, 3.0, 1.0, 3.0],
    [10.0, 2.0, 4.0, 0.0, 0.0]
]

for i, out in test_list:
    print(tmed.update(np.array(i)))

```

## Unittests

From project directory run

```$ python -m unittest discover tests```
