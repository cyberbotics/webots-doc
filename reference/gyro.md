## Gyro

Derived from `Device`.

```
Gyro {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute x-axis
  SFBool     yAxis          TRUE  # compute y-axis
  SFBool     zAxis          TRUE  # compute z-axis
  SFFloat    resolution     -1
}
```

### Description

The `Gyro` node is used to model 1, 2 and 3-axis angular velocity sensors
(gyroscope). The angular velocity is measured in radians per second [rad/s].

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
`wb_gyro_get_values()[2]` returns *NaN*. The default is that all three axes are
enabled (TRUE).
- `resolution`: This field allows to define the resolution of the sensor, the
resolution is the smallest change that it is able to measure. Setting this field
to -1 (default) means that the sensor has an 'infinite' resolution (it can
measure any infinitesimal change). This field accepts any value in the interval
(0.0, inf).

### Gyro Functions

#### Description

The `wb_gyro_enable()` function turns on the angular velocity measurement each
`ms` milliseconds.

The `wb_gyro_disable()` function turns off the `Gyro` device.

The `wb_gyro_get_sampling_period()` function returns the period given into the
`wb_gyro_enable()` function, or 0 if the device is disabled.

The `wb_gyro_get_values()` function returns the current measurement of the
`Gyro` device. The values are returned as a 3D-vector therefore only the indices
0, 1, and 2 are valid for accessing the vector. Each vector element represents
the angular velocity about one of the axes of the `Gyro` node, expressed in
radians per second [rad/s]. The first element corresponds to the angular
velocity about the *x*-axis, the second element to the *y*-axis, etc.

> **note**: The returned vector is a pointer to the internal values managed by the `Gyro`
node, therefore it is illegal to free this pointer. Furthermore, note that the
pointed values are only valid until the next call to `wb_robot_step()` or
`Robot::step()`. If these values are needed for a longer period they must be
copied.

> **note**: `getValues()` returns the vector as a list containing three floats.

