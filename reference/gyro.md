## Gyro

Derived from [Device](device.md).

```
Gyro {
  MFVec3f lookupTable [ ]  # interpolation
  SFBool  xAxis       TRUE # compute x-axis
  SFBool  yAxis       TRUE # compute y-axis
  SFBool  zAxis       TRUE # compute z-axis
  SFFloat resolution  -1
}
```

### Description

The [Gyro](#gyro) node is used to model 1, 2 and 3-axis angular velocity sensors (gyroscope).
The angular velocity is measured in radians per second [rad/s].

### Field Summary

- `lookupTable`: This field optionally specifies a lookup table that can be used
for mapping the raw angular velocity values [rad/s] to device specific output
values. With the lookup table it is also possible to add noise and to define the
min and max output values. By default the lookup table is empty and therefore
the raw values are returned (no mapping).

- `xAxis, yAxis, zAxis`: Each of these boolean fields specifies if the computation
should be enabled or disabled for the specified axis. If one of these fields is
set to FALSE, then the corresponding vector element will not be computed and it
will return *NaN* (Not a Number) For example if `zAxis` is FALSE, then
the second element of the array returned by the `wb_gyro_get_values` function returns *NaN*.
The default is that all three axes are enabled (TRUE).

- `resolution`: This field allows to define the resolution of the sensor, the
resolution is the smallest change that it is able to measure. Setting this field
to -1 (default) means that the sensor has an 'infinite' resolution (it can
measure any infinitesimal change). This field accepts any value in the interval
(0.0, inf).

### Gyro Functions

**Name**

**wb\_gyro\_enable**, **wb\_gyro\_disable**, **wb\_gyro\_get\_sampling\_period**, **wb\_gyro\_get\_values** - *enable, disable and read the output values of the gyro device*

{[C++](cpp-api.md#cpp_gyro)}, {[Java](java-api.md#java_gyro)}, {[Python](python-api.md#python_gyro)}, {[Matlab](matlab-api.md#matlab_gyro)}, {[ROS](ros-api.md)}

```c
#include <webots/gyro.h>

void wb_gyro_enable(WbDeviceTag tag, int sampling_period);
void wb_gyro_disable(WbDeviceTag tag);
int wb_gyro_get_sampling_period(WbDeviceTag tag);
const double *wb_gyro_get_values(WbDeviceTag tag);
```

**Description**

The `wb_gyro_enable` function turns on the angular velocity measurements.
The `sampling_period` argument specifies the sampling period of the sensor and is expressed in milliseconds.
Note that the first measurement will be available only after the first sampling period elapsed.

The `wb_gyro_disable` function turns off the [Gyro](#gyro) device.

The `wb_gyro_get_sampling_period` function returns the period given into the `wb_gyro_enable` function, or 0 if the device is disabled.

The `wb_gyro_get_values` function returns the current measurement of the [Gyro](#gyro) device.
The values are returned as a 3D-vector therefore only the indices 0, 1, and 2 are valid for accessing the vector.
Each vector element represents the angular velocity about one of the axes of the [Gyro](#gyro) node, expressed in radians per second [rad/s].
The first element corresponds to the angular velocity about the *x*-axis, the second element to the *y*-axis, etc.

> **Note** [C, C++]: The returned vector is a pointer to the internal values managed by the [Gyro](#gyro) node, therefore it is illegal to free this pointer.
Furthermore, note that the pointed values are only valid until the next call to the `wb_robot_step` or `Robot::step` functions.
If these values are needed for a longer period they must be copied.

<!-- -->

> **Note** [Python]: The `getValues` function returns the vector as a list containing three floats.
