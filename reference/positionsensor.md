## PositionSensor

Derived from [Device](reference/device.md#device).

```
PositionSensor {
  SFFloat resolution  -1
}
```

### Description

A [PositionSensor](reference/positionsensor.md#positionsensor) node can be used
in a mechanical simulation to monitor a joint position. The position sensor can
be inserted in the `device` field of a
[HingeJoint](reference/hingejoint.md#hingejoint), a
[Hinge2Joint](reference/hinge2joint.md#hinge2joint), a
[SliderJoint](reference/sliderjoint.md#sliderjoint), or a
[Track](reference/track.md#track). Depending on the
[Joint](reference/joint.md#joint) type, it will measure the angular position in
radians or the linear position in meters.

### Field Summary

- `resolution`: This field allows to define the resolution of the sensor, the
resolution is the smallest change that it is able to measure. Setting this field
to -1 (default) means that the sensor has an 'infinite' resolution (it can
measure any infinitesimal change). This field accepts any value in the interval
(0.0, inf).

### PositionSensor Functions

#### Name

**wb\_position\_sensor\_enable**, **wb\_position\_sensor\_disable**, **wb\_position\_sensor\_get\_sampling\_period**, **wb\_position\_sensor\_get\_value**, **wb\_position\_sensor\_get\_type** - *enable, disable and read position sensor measurement*

{[C++](reference/cpp-api.md)}, {[Java](reference/java-api.md)}, {[Python](reference/python-api.md)}, {[Matlab](reference/matlab-api.md)}

``` c
#include <webots/position_sensor.h>

void wb_position_sensor_enable(WbDeviceTag tag, int ms)
void wb_position_sensor_disable(WbDeviceTag tag)
int wb_position_sensor_get_sampling_period(WbDeviceTag tag)
double wb_position_sensor_get_value(WbDeviceTag tag)
int wb_position_sensor_get_type(WbDeviceTag tag)
```

#### Description

`wb_position_sensor_enable()` enables a measurement of the joint position each
`ms` milliseconds.

`wb_position_sensor_disable()` turns off the position sensor to save CPU time.

The `wb_position_sensor_get_sampling_period()` function returns the period given
into the `wb_position_sensor_enable()` function, or 0 if the device is disabled.

`wb_position_sensor_get_value()` returns the most recent value measured by the
specified position sensor. Depending on the type, it will return a value in
radians (angular position sensor) or in meters (linear position sensor).

`wb_position_sensor_get_type()` returns the type of the position sensor. It will
return `WB_ANGULAR` if the sensor is associated with a
[HingeJoint](reference/hingejoint.md#hingejoint) or a
[Hinge2Joint](reference/hinge2joint.md#hinge2joint) node, and `WB_LINEAR` if it
is associated with a [SliderJoint](reference/sliderjoint.md#sliderjoint) or a
[Track](reference/track.md#track) node.

