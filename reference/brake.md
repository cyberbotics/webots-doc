## Brake

Derived from [Device](device.md).

```
Brake {
}
```

### Description

A [Brake](#brake) node can be used in a mechanical simulation in order to change
the friction of a joint. The [Brake](#brake) node can be inserted in the
`device` field of a [HingeJoint](hingejoint.md), a
[Hinge2Joint](hinge2joint.md), a [SliderJoint](sliderjoint.md), or a
[Track](track.md).

### Brake Functions

<a name="wb_brake_set_damping_constant">**Name**</a>

**wb\_brake\_set\_damping\_constant**, **wb\_brake\_get\_type** - *set the damping constant coefficient of the joint and get the type of brake*

{[C++](cpp-api.md#cpp_brake)}, {[Java](java-api.md#java_brake)}, {[Python](python-api.md#python_brake)}, {[Matlab](matlab-api.md#matlab_brake)}

``` c
#include <webots/brake.h>

void wb_brake_set_damping_constant(WbDeviceTag tag, double damping_constant)
int wb_brake_get_type(WbDeviceTag tag)
```

**Description**

`wb_brake_set_damping_constant()` sets the value of the dampingConstant
coefficient (Ns/m or Nms) of the joint. If any dampingConstant is already set
using [JointParameters](jointparameters.md) the resulting dampingConstant
coefficient is the sum of the one in the [JointParameters](jointparameters.md)
and the one set using the `wb_brake_set_damping_constant()` function.

`wb_brake_get_type()` returns the type of the brake. It will return `WB_ANGULAR`
if the sensor is associated with a [HingeJoint](hingejoint.md) or a
[Hinge2Joint](hinge2joint.md) node, and `WB_LINEAR` if it is associated with a
[SliderJoint](sliderjoint.md) or a [Track](track.md) node.

