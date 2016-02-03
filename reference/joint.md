## Joint


```
Joint {
  field SFNode jointParameters NULL # a joint parameters node
  field SFNode endPoint        NULL # Solid or SolidReference
}
```

### Description

The `Joint` node is an abstract node (not instantiated) whose derived classes
model various types of mechanical joints: hinge (`HingeJoint`), slider
(`SliderJoint`), ball joint (`BallJoint`), hinge2 (`Hinge2Joint`). Apart from
the ball joint, joints can be motorized and endowed with `PositionSensor` nodes.

The `Joint` node creates a link between its `Solid` parent and the `Solid`
placed into its ` endPoint` field. Using a `SolidReference` inside `endPoint`
enables you to close mechanical loops within a `Robot` or a passive mechanical
system.

### Field Summary

- `jointParameters`: this field optionally specifies a `JointParameters` node or one of its derived classes. These nodes contain common joint parameters such as position, stops, anchor or axis if existing. This field must be filled with an `HingeJointParameters` node for an `HingeJoint` or an `Hinge2Joint`, with a `JointParameters` node for a `SliderJoint` (anchor-less) and with a `BallJointParameters` node for a `BallJoint`.For an `Hinge2Joint`, the `jointParameters` field is related to the first rotation axis while an additional field called `jointParameters2` refers to the second rotation axis.3D-vector parameters (e.g `axis, anchor`) are always expressed in relative coordinates with respect to the closest upper `Solid`'s frame using the meter as unit. If the `jointParameters` field is not specified, parameters are set with the default values defined in the corresponding parameter node.
- `endPoint`: this field specifies which `Solid` will be subjected to the joint constraints. It must be either a `Solid` child, or a reference to an existing `Solid`, i.e. a `SolidReference`. Alternatively, a `Slot` node can be inserted in the `endPoint` field, but this `Slot` should be connected to another `Slot` whose `endPoint` is either a `Solid` or a `SolidReference`.

### Joint's hidden position fields

If the `jointParameters` is set to NULL, joint positions are then not visible
from the Scene Tree. In this case Webots keeps track of the initial positions of
`Joint` nodes (except for the `BallJoint`) by means of hidden position fields.
These fields, which are not visible from the Scene Tree, are used to store
inside the world file the current joint positions when the simulation is saved.
As a result joint positions are restored when reloading the simulation just the
same way they would be if `JointParameters` nodes were used.

For `HingeJoint` and `SliderJoint` nodes containing no `JointParameters`, Webots
uses the hidden field named `position`. For a `Hinge2Joint` node, an additional
hidden field named `position2` is used to store the joint position with respect
the the second hinge.

