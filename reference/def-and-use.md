## DEF and USE

A node which is named using the DEF keyword can be referenced later by its name
in the same file with USE statements. The DEF and USE keywords can be used to
reduce redundancy in ".wbt" and ".proto" files. DEF name are limited in scope to
a single ".wbt" or ".proto" file. If multiple nodes are given the same DEF name,
each USE statement refers to the closest node with the given DEF name preceding
it in the ".wbt" or ".proto" file.

```
[DEF defName] nodeName { nodeBody }
```

```
USE defName
```

> **note**: Although it is permitted to name any node using the DEF keyword, USE statements
are not allowed for `Solid`, `Joint`, `JointParameters`, and
`BallJointParameters` nodes and their derived nodes. Indeed, the ability for
identical solids or joints to occupy the same position is useless, if not
hazardous, in a physics simulation. To safely duplicate one of these nodes, you
can design a `PROTO` model for this node and then add different PROTO instances
to your world.

