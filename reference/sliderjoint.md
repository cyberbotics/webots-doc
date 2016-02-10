## SliderJoint

Derived from [Joint](reference/joint.md#joint).

```
SliderJoint {
  field       MFNode  device   [ ]        # linear motor or linear position sensor
  hiddenField SFFloat position 0          # initial position (m)
}
```

### Description

The [SliderJoint](reference/sliderjoint.md#sliderjoint) node can be used to
model a slider, i.e. a joint allowing only a translation motion along a given
axis (1 degree of freedom). It inherits [Joint](reference/joint.md#joint)'s
`jointParameters` field. This field can be filled with a
[JointParameters](reference/jointparameters.md#jointparameters) only. If empty,
[JointParameters](reference/jointparameters.md#jointparameters) default values
apply.

### Field Summary

- `device`: This field optionally specifies a
[LinearMotor](reference/linearmotor.md#linearmotor), a linear
[PositionSensor](reference/positionsensor.md#positionsensor) and/or a
[Brake](reference/brake.md#brake) device. If no motor is specified, the joint is
passive joint.
- `position`: see [joint's hidden position field](reference/joint.md#joint-s
-hidden-position-fields).

