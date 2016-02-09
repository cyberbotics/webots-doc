## Brake

Derived from `Device`.

```
Brake {
}
```

### Description

A `Brake` node can be used in a mechanical simulation in order to change the
friction of a joint. The `Brake` node can be inserted in the `device` field of a
`HingeJoint`, a `Hinge2Joint`, a `SliderJoint`, or a `Track`.

### Brake Functions

#### Description

`wb_brake_set_damping_constant()` sets the value of the dampingConstant
coefficient (Ns/m or Nms) of the joint. If any dampingConstant is already set
using `JointParameters` the resulting dampingConstant coefficient is the sum of
the one in the `JointParameters` and the one set using the
`wb_brake_set_damping_constant()` function.

`wb_brake_get_type()` returns the type of the brake. It will return `WB_ANGULAR`
if the sensor is associated with a `HingeJoint` or a `Hinge2Joint` node, and
`WB_LINEAR` if it is associated with a `SliderJoint` or a `Track` node.

