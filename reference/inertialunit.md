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

### InertialUnit Functions

