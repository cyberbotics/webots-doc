## Brake

Derived from [Device](device.md).

```
Brake {
}
```

### Description

A [Brake](#brake) node can be used in a mechanical simulation in order to change the friction of a joint.
The [Brake](#brake) node can be inserted in the `device` field of a [HingeJoint](hingejoint.md), a [Hinge2Joint](hinge2joint.md), a [SliderJoint](sliderjoint.md), or a [Track](track.md).

### Brake Functions

**Name**

**wb\_brake\_set\_damping\_constant**, **wb\_brake\_get\_type** - *set the damping constant coefficient of the joint and get the type of brake*

{[C++](cpp-api.md#cpp_brake)}, {[Java](java-api.md#java_brake)}, {[Python](python-api.md#python_brake)}, {[Matlab](matlab-api.md#matlab_brake)}, {[ROS](ros-api.md)}

```c
#include <webots/brake.h>

void wb_brake_set_damping_constant(WbDeviceTag tag, double damping_constant);
int wb_brake_get_type(WbDeviceTag tag);
```

**Description**

The `wb_brake_set_damping_constant` function sets the value of the dampingConstant coefficient (Ns/m or Nms) of the joint.
If any dampingConstant is already set using [JointParameters](jointparameters.md) the resulting dampingConstant coefficient is the sum of the one in the [JointParameters](jointparameters.md) and the one set using the `wb_brake_set_damping_constant` function.

The `wb_brake_get_type` function returns the type of the brake.
It will return `WB_ANGULAR` if the sensor is associated with a [HingeJoint](hingejoint.md) or a [Hinge2Joint](hinge2joint.md) node, and `WB_LINEAR` if it is associated with a [SliderJoint](sliderjoint.md) or a [Track](track.md) node.

---

**Name**

**wb\_brake\_get\_motor**, **wb\_brake\_get\_position\_sensor** - *get associated devices*

{[C++](cpp-api.md#cpp_brake)}, {[Java](java-api.md#java_brake)}, {[Python](python-api.md#python_brake)}, {[Matlab](matlab-api.md#matlab_brake)}, {[ROS](ros-api.md)}

```c
#include <webots/brake.h>

WbDeviceTag wb_brake_get_motor(WbDeviceTag tag);
WbDeviceTag wb_brake_get_position_sensor(WbDeviceTag tag);
```

**Description**

The `wb_brake_get_motor` and `wb_brake_get_position_sensor` functions return the [Motor](motor.md) and [PositionSensor](positionsensor.md) instances defined in the same [Joint](joint.md) or [Track](track.md) `device` field.
If none is defined they return 0.
