## Hinge2Joint

Derived from [HingeJoint](reference/hingejoint.md#hingejoint).

```
Hinge2Joint {
  field SFNode jointParameters2 NULL # JointParameters for second axis
  field MFNode device2 [ ] # RotationalMotor, PositionSensor and Brake
  hiddenField SFFloat position2  0 # initial position with respect to the second hinge (rad)
}
```

### Description

The [Hinge2Joint](reference/hinge2joint.md#hinge2joint) node can be used to
model a hinge2 joint, i.e. a joint allowing only rotational motions around two
intersecting axes (2 degrees of freedom). These axes cross at the `anchor` point
and need not to be perpendicular. The suspension fields defined in a
[HingeJointParameters](reference/hingejointparameters.md#hingejointparameters)
node allow for spring and damping effects along the suspension axis.

Note that a universal joint boils down to a hinge2 joint with orthogonal axes
and (default) zero suspension.

Typically, [Hinge2Joint](reference/hinge2joint.md#hinge2joint) can be used to
model a steering wheel with suspension for a car, a shoulder or a hip for a
humanoid robot.

> **note**: A [Hinge2Joint](reference/hinge2joint.md#hinge2joint) will connect only
[Solid](reference/solid.md#solid)s having a
[Physics](reference/physics.md#physics) node. In other words, this joint cannot
be statically based.

### Field Summary

- `jointParameters2`: This field optionally specifies a
[HingeJointParameters](reference/hingejointparameters.md#hingejointparameters)
node It contains, among others, the joint position, the axis position expressed
in relative coordinates, the stop positions and suspension parameters. If the
`jointParameters` field is left empty, default values of the
HingeJointParameters node apply.
- `device2`: This field optionally specifies a
[RotationalMotor](reference/rotationalmotor.md#rotationalmotor), an angular
[PositionSensor](reference/positionsensor.md#positionsensor) and/or a
[Brake](reference/brake.md#brake) device attached to the second axis. If no
motor is specified, this part of the joint is passive.
- `position2`: see [joint's hidden position
field](reference/rotationalmotor.md#rotationalmotor).

