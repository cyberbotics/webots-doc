## SliderJoint

Derived from [Joint](#joint).

```
SliderJoint {
  field       MFNode  device   [ ]        # linear motor or linear position sensor
  hiddenField SFFloat position 0          # initial position (m)
}
```

### Description

The [SliderJoint](#sliderjoint) node can be used to model a slider, i.e. a joint
allowing only a translation motion along a given axis (1 degree of freedom). It
inherits [Joint](#joint)'s `jointParameters` field. This field can be filled
with a [JointParameters](#jointparameters) only. If empty,
[JointParameters](#jointparameters) default values apply.

### Field Summary

- `device`: This field optionally specifies a [LinearMotor](#linearmotor), a
linear [PositionSensor](#positionsensor) and/or a [Brake](#brake) device. If no
motor is specified, the joint is passive joint.
- `position`: see [joint's hidden position
field](#joint-s-hidden-position-fields).

