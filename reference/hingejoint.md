## HingeJoint

Derived from [Joint](reference/joint.md#joint).

```
HingeJoint {
  field       MFNode  device   [ ] # RotationalMotor, PositionSensor and Brake
  hiddenField SFFloat position 0   # (rad) initial position
}
```

### Description

The [HingeJoint](reference/hingejoint.md#hingejoint) node can be used to model a
hinge, i.e. a joint allowing only a rotational motion around a given axis (1
degree of freedom). It inherits [Joint](reference/joint.md#joint)'s
`jointParameters` field. This field can be filled with a
[HingeJointParameters](reference/hingejointparameters.md#hingejointparameters)
only. If empty,
[HingeJointParameters](reference/hingejointparameters.md#hingejointparameters)
default values apply.

### Field Summary

- `device`: This field optionally specifies a
[RotationalMotor](reference/rotationalmotor.md#rotationalmotor), an angular
[PositionSensor](reference/positionsensor.md#positionsensor) and/or a
[Brake](reference/brake.md#brake) device. If no motor is specified, the joint is
passive joint.
- `position`: see [joint's hidden position field](reference/joint.md#joint-s
-hidden-position-fields).

