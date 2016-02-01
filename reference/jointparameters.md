## JointParameters


```
JointParameters {
  field SFFloat position        0 # current position (m or rad)
  field SFVec3f axis        0 0 1 # displacement axis (m)
  field SFFloat minStop         0 # low stop position (m or rad)
  field SFFloat maxStop         0 # high stop position (m or rad)
  field SFFloat springConstant  0 # spring constant (N/m or Nm)
  field SFFloat dampingConstant 0 # damping constant (Ns/m or Nms) 
  field SFFloat staticFriction  0 # friction constant (Ns/m or Nms)
}

```

### Description

The `JointParameters` node is a concrete base node used to specify various joint
parameters related to an axis along which, or around which, the motion is
allowed. As an instantiated node it can be used within the jointParameters field
of `SliderJoint` or within the jointParameters2 field of `Hinge2Joint`. Unlike
the other joint parameters node, it has no anchor.

### Field Summary

### Units

Rotational joint units (`HingeJoint`, `Hinge2Joint`) are expressed in *radians*
while linear joint units (`SliderJoint`) are expressed in *meters*. See :

 | Rotational | Linear
--- | --- | ---
Position | rad (radians) | m (meters)

### Initial Transformation and Position

![HingeJoint](pdf/hinge_joint.pdf)

**HingeJoint**

![SliderJoint](pdf/slider_joint.pdf)

**SliderJoint**

The `position` field is a scalar representing an angle (in radians) or a
distance (in meters) computed with respect to the initial `translation` and
`rotation` of the `Joint`'s `Solid` child. If its value is zero, then the
`Joint`'s child is *by definition* set with its initial `translation` and
`rotation`. For a joint with one or two rotational degrees of freedom (e.g.,
`HingeJoint`, `Hinge2Joint`), the `position` field value is the rotation angle
around one the joint axes that was applied to the `Joint`'s child initially in
zero position. For a slider joint, `position` is the translation length along
the sliding axis that was applied to the `Joint`'s child initially in zero
position.

For example if we have a `HingeJoint` and a `position` field value of 1.5708,
this means that this `HingeJoint` is 90 degrees from its initial rotation with
respect to the hinge rotation axis. The values passed to the
`wb_motor_set_position()` function are specified with respect to the zero
position. The values of the `minStop` and `maxStop` fields are also defined with
respect to the zero position.

### Joint Limits

The `minStop` and `maxStop` fields define the *hard limits* of the joint. Hard
limits represent physical (or mechanical) bounds that cannot be overrun by any
force; they are defined with respect to the joint `position`. Hard limits can be
used, for example, to simulate both end caps of a hydraulic or pneumatic piston
or to restrict the range of rotation of a hinge. When used for a rotational
motion the value of `minStop` must be in the range [-pi, 0] and `maxStop` must
be in the range [0, pi]. When both `minStop` and `maxStop` are zero (the
default), the hard limits are deactivated. The joint hard limits use ODE joint
stops (for more information see the ODE documentation on `dParamLoStop` and
`dParamHiStop`).

Finally, note that when both soft (`minPosition` and `maxPosition`, see the
`Motor`'s "Motor Limits" section) and hard limits (`minStop` and `maxStop`) are
activated, the range of the soft limits must be included in the range of the
hard limits, such that `minStop lt= minValue` and `maxStopgt= maxValue`.

### Springs and Dampers

The `springConstant` field specifies the value of the spring constant (or spring
stiffness), usually denoted as `K`. The `springConstant` must be positive or
zero. If the `springConstant` is zero (the default), no spring torque/force will
be applied to the joint. If the `springConstant` is greater than zero, then a
spring force will be computed and applied to the joint in addition to the other
forces (i.e., motor force, damping force). The spring force is calculated
according to Hooke's law: `F = -Kx`, where `K` is the `springConstant` and `x`
is the current joint position as represented by the `position` field. Therefore,
the spring force is computed so as to be proportional to the current joint
position, and to move the joint back to its initial position. When designing a
robot model that uses springs, it is important to remember that the spring's
resting position for each joint will correspond to the initial position of the
joint. The only expection arise when the closest upper `Solid` of the `Joint` is
passive, i.e. the `physics` field is not defined. In this case the spring force
direction is inverted.

The `dampingConstant` field specifies the value of the joint damping constant.
The value of `dampingConstant` must be positive or zero. If `dampingConstant` is
zero (the default), no damping torque/force will be added to the joint. If
`dampingConstant` is greater than zero, a damping torque/force will be applied
to the joint in addition to the other forces (i.e., motor force, spring force).
This damping torque/force is proportional to the effective joint velocity: `F =
-Bv`, where `B` is the damping constant, and `v = dx/dt` is the effective joint
velocity computed by the physics simulator.

![Mechanical Diagram of a Slider Joint](pdf/slider_joint_mechanics.pdf)

**Mechanical Diagram of a Slider Joint**

As you can see in (see  ), a `Joint` creates a joint between two masses `m` and
`m`. The mass `m` is defined by the `Physics` node in the closest upper `Solid`
of the `Joint`. The mass `m` is defined by the `Physics` node of the `Solid`
placed into the `endPoint` of the `Joint`. The value `x` corresponds to the
anchor position of the `Joint` defined in the `anchor` field of a
`JointParameters` node. The position `x` corresponds to the current position of
the `Joint` defined in the `position` field of a `JointParameters` node.

