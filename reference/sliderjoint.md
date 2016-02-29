## SliderJoint

Derived from [Joint](joint.md#joint).

```
SliderJoint {
  field       MFNode  device   [ ]        # linear motor or linear position sensor
  hiddenField SFFloat position 0          # initial position (m)
}
```

### Description

The [SliderJoint](sliderjoint.md#sliderjoint) node can be used to model a
slider, i.e. a joint allowing only a translation motion along a given axis (1
degree of freedom). It inherits [Joint](joint.md#joint)'s `jointParameters`
field. This field can be filled with a
[JointParameters](jointparameters.md#jointparameters) only. If empty,
[JointParameters](jointparameters.md#jointparameters) default values apply.

### Field Summary

- `device`: This field optionally specifies a
[LinearMotor](linearmotor.md#linearmotor), a linear
[PositionSensor](positionsensor.md#positionsensor) and/or a
[Brake](brake.md#brake) device. If no motor is specified, the joint is passive
joint.
- `position`: see [joint's hidden position
field](joint.md#joint-s-hidden-position-fields).

