## Joint

```
Joint {
  field SFNode jointParameters NULL # a joint parameters node
  field SFNode endPoint        NULL # Solid or SolidReference
}
```

### Description

The [Joint](reference/joint.md#joint) node is an abstract node (not
instantiated) whose derived classes model various types of mechanical joints:
hinge ([HingeJoint](reference/hingejoint.md#hingejoint)), slider
([SliderJoint](reference/sliderjoint.md#sliderjoint)), ball joint
([BallJoint](reference/balljoint.md#balljoint)), hinge2
([Hinge2Joint](reference/hinge2joint.md#hinge2joint)). Apart from the ball
joint, joints can be motorized and endowed with
[PositionSensor](reference/positionsensor.md#positionsensor) nodes.

The [Joint](reference/joint.md#joint) node creates a link between its
[Solid](reference/solid.md#solid) parent and the
[Solid](reference/solid.md#solid) placed into its ` endPoint` field. Using a
[SolidReference](reference/solidreference.md#solidreference) inside `endPoint`
enables you to close mechanical loops within a [Robot](reference/robot.md#robot)
or a passive mechanical system.

### Field Summary

- `jointParameters`: this field optionally specifies a
[JointParameters](reference/jointparameters.md#jointparameters) node or one of
its derived classes. These nodes contain common joint parameters such as
position, stops, anchor or axis if existing. This field must be filled with an
[HingeJointParameters](reference/hingejointparameters.md#hingejointparameters)
node for an [HingeJoint](reference/hingejoint.md#hingejoint) or an
[Hinge2Joint](reference/hinge2joint.md#hinge2joint), with a
[JointParameters](reference/jointparameters.md#jointparameters) node for a
[SliderJoint](reference/sliderjoint.md#sliderjoint) (anchor-less) and with a
[BallJointParameters](reference/balljointparameters.md#balljointparameters) node
for a [BallJoint](reference/balljoint.md#balljoint).

    For an [Hinge2Joint](reference/hinge2joint.md#hinge2joint), the
    `jointParameters` field is related to the first rotation axis while an
    additional field called `jointParameters2` refers to the second rotation axis.

    3D-vector parameters (e.g `axis, anchor`) are always expressed in relative
    coordinates with respect to the closest upper
    [Solid](reference/solid.md#solid)'s frame using the meter as unit. If the
    `jointParameters` field is not specified, parameters are set with the default
    values defined in the corresponding parameter node.

- `endPoint`: this field specifies which [Solid](reference/solid.md#solid) will be
subjected to the joint constraints. It must be either a
[Solid](reference/solid.md#solid) child, or a reference to an existing
[Solid](reference/solid.md#solid), i.e. a
[SolidReference](reference/solidreference.md#solidreference). Alternatively, a
[Slot](reference/slot.md#slot) node can be inserted in the `endPoint` field, but
this [Slot](reference/slot.md#slot) should be connected to another
[Slot](reference/slot.md#slot) whose `endPoint` is either a
[Solid](reference/solid.md#solid) or a
[SolidReference](reference/solidreference.md#solidreference).

### Joint's hidden position fields

If the `jointParameters` is set to NULL, joint positions are then not visible
from the Scene Tree. In this case Webots keeps track of the initial positions of
[Joint](reference/joint.md#joint) nodes (except for the
[BallJoint](reference/balljoint.md#balljoint)) by means of hidden position
fields. These fields, which are not visible from the Scene Tree, are used to
store inside the world file the current joint positions when the simulation is
saved. As a result joint positions are restored when reloading the simulation
just the same way they would be if
[JointParameters](reference/jointparameters.md#jointparameters) nodes were used.

For [HingeJoint](reference/hingejoint.md#hingejoint) and
[SliderJoint](reference/sliderjoint.md#sliderjoint) nodes containing no
[JointParameters](reference/jointparameters.md#jointparameters), Webots uses the
hidden field named `position`. For a
[Hinge2Joint](reference/hingejoint.md#hingejoint) node, an additional hidden
field named `position2` is used to store the joint position with respect the the
second hinge.

