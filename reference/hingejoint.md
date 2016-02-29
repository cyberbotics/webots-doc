## HingeJoint

Derived from [Joint](#joint).

```
HingeJoint {
  field       MFNode  device   [ ] # RotationalMotor, PositionSensor and Brake
  hiddenField SFFloat position 0   # (rad) initial position
}
```

### Description

The [HingeJoint](#hingejoint) node can be used to model a hinge, i.e. a joint
allowing only a rotational motion around a given axis (1 degree of freedom). It
inherits [Joint](#joint)'s `jointParameters` field. This field can be filled
with a [HingeJointParameters](#hingejointparameters) only. If empty,
[HingeJointParameters](#hingejointparameters) default values apply.

### Field Summary

- `device`: This field optionally specifies a [RotationalMotor](#rotationalmotor),
an angular [PositionSensor](#positionsensor) and/or a [Brake](#brake) device. If
no motor is specified, the joint is passive joint.
- `position`: see [joint's hidden position
field](#joint-s-hidden-position-fields).

