## Accelerometer

Derived from [Device](device.md).

```
Accelerometer {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute x-axis
  SFBool     yAxis          TRUE  # compute y-axis
  SFBool     zAxis          TRUE  # compute z-axis
  SFFloat    resolution     -1
}
```

### Description

The [Accelerometer](#accelerometer) node can be used to model accelerometer
devices such as those commonly found in mobile electronics, robots and game
input devices. The [Accelerometer](#accelerometer) node measures acceleration
and gravity induced reaction forces over 1, 2 or 3 axes. It can be used for
example to detect fall, the up/down direction, etc.

### Field Summary

- `lookupTable`: This field optionally specifies a lookup table that can be used
for mapping the raw acceleration values [m/s^2] to device specific output
values. With the lookup table it is also possible to add noise and to define the
min and max output values. By default the lookup table is empty and therefore
the raw acceleration values are returned (no mapping).
- `xAxis, yAxis, zAxis`: Each of these boolean fields enables or disables
computation for the specified axis. If one of these fields is set to FALSE, then
the corresponding vector element will not be computed and will return *NaN* (Not
a Number). For example, if  `zAxis ` is FALSE, then
`wb_accelerometer_get_values()[2]` will always return *NaN*. The default is that
all three axes are enabled (TRUE). Modifying these fields makes it possible to
choose between a single, dual or three-axis accelerometer and to specify which
axes will be used.
- `resolution`: This field allows to define the resolution of the sensor, the
resolution is the smallest change that it is able to measure. For example, if
`resolution` is 0.2 instead of returning 1.767 the sensor will return 1.8.
Setting this field to -1 (default) means that the sensor has an 'infinite'
resolution (it can measure any infinitesimal change). This field accepts any
value in the interval (0.0, inf).

### Accelerometer Functions

**Name**

**wb\_accelerometer\_enable**, **wb\_accelerometer\_disable**, **wb\_accelerometer\_get\_sampling\_period**, **wb\_accelerometer\_get\_values** - *enable, disable and read the output of the accelerometer*

{[C++](cpp-api.md#cpp_accelerometer)}, {[Java](java-api.md#java_accelerometer)}, {[Python](python-api.md#python_accelerometer)}, {[Matlab](matlab-api.md#matlab_accelerometer)}, {[ROS](ros-api.md)}

``` c
#include <webots/accelerometer.h>

void wb_accelerometer_enable(WbDeviceTag tag, int ms)
void wb_accelerometer_disable(WbDeviceTag tag)
int wb_accelerometer_get_sampling_period(WbDeviceTag tag)
const double *wb_accelerometer_get_values(WbDeviceTag tag)
```

**Description**

The `wb_accelerometer_enable()` function allows the user to enable the
acceleration measurement each `ms` milliseconds.
The provided `ms` argument specifies the sensor's sampling period.
Note that the first measurement will be available only after the sampling period has expired.

The `wb_accelerometer_disable()` function turns the accelerometer off, saving
computation time.

The `wb_accelerometer_get_sampling_period()` function returns the period given
into the `wb_accelerometer_enable()` function, or 0 if the device is disabled.

The `wb_accelerometer_get_values()` function returns the current values measured
by the [Accelerometer](#accelerometer). These values are returned as a
3D-vector, therefore only the indices 0, 1, and 2 are valid for accessing the
vector. Each element of the vector represents the acceleration along the
corresponding axis of the [Accelerometer](#accelerometer) node, expressed in
meters per second squared [m/s^2]. The first element corresponds to the x-axis,
the second element to the y-axis, etc. An [Accelerometer](#accelerometer) at
rest with earth's gravity will indicate 1 g (9.81 m/s^2) along the vertical
axis. Note that the gravity can be specified in the `gravity` field in the
[WorldInfo](worldinfo.md) node. To obtain the acceleration due to motion alone,
this offset must be subtracted. The device's output will be zero during free
fall when no offset is substracted.

> **note** [C, C++]:
The returned vector is a pointer to the internal values managed by the
[Accelerometer](#accelerometer) node, therefore it is illegal to free this
pointer. Furthermore, note that the pointed values are only valid until the next
call to `wb_robot_step()` or `Robot::step()`. If these values are needed for a
longer period they must be copied.

<!-- -->

> **note** [Python]:
`getValues()` returns the 3D-vector as a list containing three floats.
