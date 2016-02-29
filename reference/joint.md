## Joint

```
Joint {
  field SFNode jointParameters NULL # a joint parameters node
  field SFNode endPoint        NULL # Solid or SolidReference
}
```

### Description

The [Joint](#joint) node is an abstract node (not instantiated) whose derived
classes model various types of mechanical joints: hinge
([HingeJoint](#hingejoint)), slider ([SliderJoint](#sliderjoint)), ball joint
([BallJoint](#balljoint)), hinge2 ([Hinge2Joint](#hinge2joint)). Apart from the
ball joint, joints can be motorized and endowed with
[PositionSensor](#positionsensor) nodes.

The [Joint](#joint) node creates a link between its [Solid](#solid) parent and
the [Solid](#solid) placed into its ` endPoint` field. Using a
[SolidReference](#solidreference) inside `endPoint` enables you to close
mechanical loops within a [Robot](#robot) or a passive mechanical system.

### Field Summary

- `jointParameters`: this field optionally specifies a
[JointParameters](#jointparameters) node or one of its derived classes. These
nodes contain common joint parameters such as position, stops, anchor or axis if
existing. This field must be filled with an
[HingeJointParameters](#hingejointparameters) node for an
[HingeJoint](#hingejoint) or an [Hinge2Joint](#hinge2joint), with a
[JointParameters](#jointparameters) node for a [SliderJoint](#sliderjoint)
(anchor-less) and with a [BallJointParameters](#balljointparameters) node for a
[BallJoint](#balljoint).

    For an [Hinge2Joint](#hinge2joint), the `jointParameters` field is related to
    the first rotation axis while an additional field called `jointParameters2`
    refers to the second rotation axis.

    3D-vector parameters (e.g `axis, anchor`) are always expressed in relative
    coordinates with respect to the closest upper [Solid](#solid)'s frame using the
    meter as unit. If the  `jointParameters` field is not specified, parameters are
    set with the default values defined in the corresponding parameter node.

- `endPoint`: this field specifies which [Solid](#solid) will be subjected to the
joint constraints. It must be either a [Solid](#solid) child, or a reference to
an existing [Solid](#solid), i.e. a [SolidReference](#solidreference).
Alternatively, a [Slot](#slot) node can be inserted in the `endPoint` field, but
this [Slot](#slot) should be connected to another [Slot](#slot) whose `endPoint`
is either a [Solid](#solid) or a [SolidReference](#solidreference).

### Joint's hidden position fields

If the `jointParameters` is set to NULL, joint positions are then not visible
from the Scene Tree. In this case Webots keeps track of the initial positions of
[Joint](#joint) nodes (except for the [BallJoint](#balljoint)) by means of
hidden position fields. These fields, which are not visible from the Scene Tree,
are used to store inside the world file the current joint positions when the
simulation is saved. As a result joint positions are restored when reloading the
simulation just the same way they would be if
[JointParameters](#jointparameters) nodes were used.

For [HingeJoint](#hingejoint) and [SliderJoint](#sliderjoint) nodes containing
no [JointParameters](#jointparameters), Webots uses the hidden field named
`position`. For a [Hinge2Joint](#hingejoint) node, an additional hidden field
named `position2` is used to store the joint position with respect the the
second hinge.

