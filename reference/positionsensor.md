## PositionSensor

Derived from `Device`.


```
PositionSensor {
  SFFloat resolution  -1
}
```

### Description

A `PositionSensor` node can be used in a mechanical simulation to monitor a
joint position. The position sensor can be inserted in the `device` field of a
`HingeJoint`, a `Hinge2Joint`, a `SliderJoint`, or a `Track`. Depending on the
`Joint` type, it will measure the angular position in radians or the linear
position in meters.

### Field Summary

### PositionSensor Functions

