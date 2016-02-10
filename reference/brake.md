## Brake

Derived from [Device](reference/device.md#device).

```
Brake {
}
```

### Description

A [Brake](reference/brake.md#brake) node can be used in a mechanical simulation
in order to change the friction of a joint. The
[Brake](reference/brake.md#brake) node can be inserted in the `device` field of
a [HingeJoint](reference/hingejoint.md#hingejoint), a
[Hinge2Joint](reference/hinge2joint.md#hinge2joint), a
[SliderJoint](reference/sliderjoint.md#sliderjoint), or a
[Track](reference/track.md#track).

### Brake Functions

#### Name

**wb\_brake\_set\_damping\_constant**, **wb\_brake\_get\_type** - *set the damping constant coefficient of the joint and get the type of brake*

``` c
#include <webots/brake.h>

void wb_brake_set_damping_constant(WbDeviceTag tag, double damping_constant)
int wb_brake_get_type(WbDeviceTag tag)
```

#### Description

`wb_brake_set_damping_constant()` sets the value of the dampingConstant
coefficient (Ns/m or Nms) of the joint. If any dampingConstant is already set
using [JointParameters](reference/jointparameters.md#jointparameters) the
resulting dampingConstant coefficient is the sum of the one in the
[JointParameters](reference/jointparameters.md#jointparameters) and the one set
using the `wb_brake_set_damping_constant()` function.

`wb_brake_get_type()` returns the type of the brake. It will return `WB_ANGULAR`
if the sensor is associated with a
[HingeJoint](reference/hingejoint.md#hingejoint) or a
[Hinge2Joint](reference/hinge2joint.md#hinge2joint) node, and `WB_LINEAR` if it
is associated with a [SliderJoint](reference/sliderjoint.md#sliderjoint) or a
[Track](reference/track.md#track) node.

