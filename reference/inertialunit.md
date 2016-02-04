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

- `lookupTable`: This field optionally specifies a lookup table that can be used for changing the angle values [rad] into device specific output values, or for changing the units to degrees for example. With the lookup table it is also possible to define the min and max output values and to add noise to the output values. By default the lookup table is empty and therefore the returned angle values are expressed in radians and no noise is added.
- `xAxis, yAxis, zAxis`: Each of these boolean fields specifies if the computation should be enabled or disabled for the specified axis. The `xAxis` field defines whether the *roll* angle should be computed. The `yAxis` field defines whether the *yaw* angle should be computed. The `zAxis` field defines whether the *pitch* angle should be computed. If one of these fields is set to FALSE, then the corresponding angle element will not be computed and it will return *NaN* (Not a Number). For example if `zAxis` is FALSE, then `wb_inertial_unit_get_values()[2]` returns *NaN*. The default is that all three axes are enabled (TRUE).


%figure "Roll, pitch and yaw angles in Webots' Inertial Unit"
![Roll, pitch and yaw angles in Webots' Inertial Unit](png/roll_pitch_yaw.png)
%end


- `resolution`: This field allows to define the resolution of the sensor, the resolution is the smallest change that it is able to measure. Setting this field to -1 (default) means that the sensor has an 'infinite' resolution (it can measure any infinitesimal change). This field accepts any value in the interval (0.0, inf).

### InertialUnit Functions

