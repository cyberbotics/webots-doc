## HingeJoint

Derived from `Joint`.


```
HingeJoint {
  field       MFNode  device   [ ] # RotationalMotor, PositionSensor and Brake
  hiddenField SFFloat position 0   # (rad) initial position
}
```

### Description

The `HingeJoint` node can be used to model a hinge, i.e. a joint allowing only a
rotational motion around a given axis (1 degree of freedom). It inherits
`Joint`'s `jointParameters` field. This field can be filled with a
`HingeJointParameters` only. If empty,  `HingeJointParameters` default values
apply.

### Field Summary

- `device`: This field optionally specifies a `RotationalMotor`, an angular `PositionSensor` and/or a `Brake` device. If no motor is specified, the joint is passive joint.
- `position`: see `joint's hidden position field`.

