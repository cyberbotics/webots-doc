## RotationalMotor

Derived from [Motor](#motor).

```
RotationalMotor {
  field SFString name         "rotational motor" # for wb_robot_get_device()
  field SFFloat  maxTorque   10                  # max torque (Nm) : [0, inf)
}
```

### Description

A [RotationalMotor](#rotationalmotor) node can be used to power either a
[HingeJoint](#hingejoint) or a [Hinge2Joint](#hinge2joint) to produce a
rotational motion around the choosen axis.

### Field Summary

- The `name` field specifies the name identifier of the motor device. This the
name to which `wb_robot_get_device()` can refer. It defaults to `"rotational
motor"`.
- The `maxTorque` field specifies both the upper limit and the default value for
the motor *available torque*. The *available torque* is the torque that is
available to the motor to perform the requested motions. The
`wb_motor_set_available_torque()` function can be used to change the *available
torque* at run-time. The value of `maxTorque` should always be zero or positive
(the default is 10). A small `maxTorque` value may result in a motor being
unable to move to the target position because of its weight or other external
forces.

