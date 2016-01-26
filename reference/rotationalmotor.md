## RotationalMotor

Derived from `Motor`.


```
RotationalMotor {
  field SFString name         "rotational motor" # for wb_robot_get_device()
  field SFFloat  maxTorque   10                  # max torque (Nm) : [0, inf)
}
```

### Description

A `RotationalMotor` node can be used to power either a `HingeJoint` or a
`Hinge2Joint` to produce a rotational motion around the choosen axis.

### Field Summary

