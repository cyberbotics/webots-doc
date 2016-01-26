## LinearMotor

Derived from `Motor`.


```
LinearMotor {
  field SFString name       "linear motor" # used by wb_robot_get_device()
  field SFFloat  maxForce   10             # max force (N) : [0, inf)
}
```

### Description

A `LinearMotor` node can be used to power a `SliderJoint` and a `Track`.

### Field Summary

