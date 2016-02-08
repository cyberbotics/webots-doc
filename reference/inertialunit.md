## InertialUnit

Derived from `Device`.


```
InertialUnit {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute roll
  SFBool     zAxis          TRUE  # compute pitch
  SFBool     yAxis          TRUE  # compute yaw
  SFFloat    resolution     -1
}
```

### Description

The `InertialUnit` node simulates an *Inertial Measurement Unit* (IMU). The
`InertialUnit` computes and returns its *roll*, *pitch* and *yaw* angles with
respect to a global coordinate system defined in the `WorldInfo` node. If you
would like to measure an acceleration or an angular velocity, please use the
`Accelerometer` or `Gyro` node instead. The `InertialUnit` node must be placed
on the `Robot` so that its *x*-axis points in the direction of the `Robot`'s
forward motion (longitudinal axis). The positive *z*-axis must point towards the
`Robot`'s right side, e.g., right arm, right wing (lateral axis). The positive
*y*-axis must point to the `Robot`'s up/top direction. If the `InertialUnit` has
this orientation, then the *roll*, *pitch* and *yaw* angles correspond to the
usual automotive, aeronautics or spatial meaning.  More precisely, the
`InertialUnit` measures the Tait-Bryan angles along *x*-axis (roll), *z*-axis
(pitch) and *y*-axis (yaw). This convention is commonly referred to as the
*x-z-y* extrinsic sequence; it corresponds to the composition of elemental
rotations denoted by YZX. The reference frame is made of the unit vector giving
the north direction, the opposite of the normalized gravity vector and their
cross-product (see `WorldInfo` to customize this frame).

### Field Summary

- `lookupTable`: This field optionally specifies a lookup table that can be used
for changing the angle values [rad] into device specific output values, or for
changing the units to degrees for example. With the lookup table it is also
possible to define the min and max output values and to add noise to the output
values. By default the lookup table is empty and therefore the returned angle
values are expressed in radians and no noise is added.
- `xAxis, yAxis, zAxis`: Each of these boolean fields specifies if the computation
should be enabled or disabled for the specified axis. The `xAxis` field defines
whether the *roll* angle should be computed. The `yAxis` field defines whether
the *yaw* angle should be computed. The `zAxis` field defines whether the
*pitch* angle should be computed. If one of these fields is set to FALSE, then
the corresponding angle element will not be computed and it will return *NaN*
(Not a Number). For example if `zAxis` is FALSE, then
`wb_inertial_unit_get_values()[2]` returns *NaN*. The default is that all three
axes are enabled (TRUE).


%figure "Roll, pitch and yaw angles in Webots' Inertial Unit"
![Roll, pitch and yaw angles in Webots' Inertial Unit](png/roll_pitch_yaw.png)
%end


- `resolution`: This field allows to define the resolution of the sensor, the
resolution is the smallest change that it is able to measure. Setting this field
to -1 (default) means that the sensor has an 'infinite' resolution (it can
measure any infinitesimal change). This field accepts any value in the interval
(0.0, inf).

### InertialUnit Functions

#### Description

The `wb_inertial_unit_enable()` function turns on the angle measurement each
`ms` milliseconds.

The `wb_inertial_unit_disable()` function turns off the `InertialUnit` device.

The `wb_inertial_unit_get_sampling_period()` function returns the period given
into the `wb_inertial_unit_enable()` function, or 0 if the device is disabled.

The `wb_inertial_unit_get_roll_pitch_yaw()` function returns the current *roll*,
*pitch* and *yaw* angles of the `InertialUnit`. The values are returned as an
array of 3 components therefore only the indices 0, 1, and 2 are valid for
accessing the returned array. Note that the indices 0, 1 and 2 return the
*roll*, *pitch* and *yaw* angles respectively.

The *roll* angle indicates the unit's rotation angle about its *x*-axis, in the
interval [-π,π]. The *roll* angle is zero when the `InertialUnit` is
horizontal, i.e., when its *y*-axis has the opposite direction of the gravity
(`WorldInfo` defines the `gravity` vector).

The *pitch* angle indicates the unit's rotation angle about is *z*-axis, in the
interval [-π/2,π/2]. The *pitch* angle is zero when the `InertialUnit` is
horizontal, i.e., when its *y*-axis has the opposite direction of the gravity.
If the `InertialUnit` is placed on the `Robot` with a standard orientation, then
the *pitch* angle is negative when the `Robot` is going down, and positive when
the robot is going up.

The *yaw* angle indicates the unit orientation, in the interval [-π,π], with
respect to `WorldInfo`.`northDirection`. The *yaw* angle is zero when the
`InertialUnit`'s *x*-axis is aligned with the north direction, it is π/2 when
the unit is heading east, and -π/2 when the unit is oriented towards the west.
The *yaw* angle can be used as a compass.

