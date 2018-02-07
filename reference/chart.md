## Chart

The Webots Node Chart outlines all the nodes available to build Webots worlds.

In the chart, an arrow between two nodes represents an inheritance relationship.
The inheritance relationship indicates that a derived node (at the arrow tail) inherits all the fields and API functions of a base node (at the arrow head).
For example, the [Supervisor](supervisor.md) node inherits from the [Robot](robot.md) node, and therefore all the fields and functions available in the [Robot](robot.md) node are also available in the [Supervisor](supervisor.md) node.

Boxes depicted with a dashed line ([Light](light.md), `Device` and `Geometry`) represent *abstract* nodes, that is, nodes that cannot be instantiated (either using the SceneTree or in a ".wbt" file).
Abstract nodes are used to group common fields and functions that are shared by derived nodes.

A box with round corners represents a `Geometry` node; that is, a node that will be graphically depicted when placed in the `geometry` field of a [Shape](shape.md) node.

A box with a gray background indicates a node that can be used directly (or composed using [Group](group.md) and [Transform](transform.md) nodes) to build a *boundingObject* used to detect collisions between [Solid](solid.md) objects.
Note that not all geometry nodes can be used as boundingObjects, and that although [Group](group.md) and [Transform](transform.md) can be used, not every combination of these will work correctly.

%figure "Webots Nodes Chart"

![node_hierarchy.png](images/node_hierarchy.png)

%end
