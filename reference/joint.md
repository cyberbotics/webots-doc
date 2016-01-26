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

