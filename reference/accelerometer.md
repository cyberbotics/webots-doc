## Accelerometer

Derived from `Device`.

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

The `Accelerometer` node can be used to model accelerometer devices such as
those commonly found in mobile electronics, robots and game input devices. The
`Accelerometer` node measures acceleration and gravity induced reaction forces
over 1, 2 or 3 axes. It can be used for example to detect fall, the up/down
direction, etc.

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

#### Description

The `wb_accelerometer_enable()` function allows the user to enable the
acceleration measurement each `ms` milliseconds.

The `wb_accelerometer_disable()` function turns the accelerometer off, saving
computation time.

The `wb_accelerometer_get_sampling_period()` function returns the period given
into the `wb_accelerometer_enable()` function, or 0 if the device is disabled.

The `wb_accelerometer_get_values()` function returns the current values measured
by the `Accelerometer`. These values are returned as a 3D-vector, therefore only
the indices 0, 1, and 2 are valid for accessing the vector. Each element of the
vector represents the acceleration along the corresponding axis of the
`Accelerometer` node, expressed in meters per second squared [m/s^2]. The first
element corresponds to the x-axis, the second element to the y-axis, etc. An
`Accelerometer` at rest with earth's gravity will indicate 1 g (9.81 m/s^2)
along the vertical axis. Note that the gravity can be specified in the `gravity`
field in the `WorldInfo` node. To obtain the acceleration due to motion alone,
this offset must be subtracted. The device's output will be zero during free
fall when no offset is substracted.

