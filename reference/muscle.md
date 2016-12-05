## Muscle

```
Muscle {
  field SFDouble maxRadius   0.2
  field MFColor  colors      []            # idle (0), contracting (1), and relaxing(2) state colors
  field SFBool   castShadows TRUE
  field SFBool   visible     TRUE
}
```

### Description

A [Muscle](#muscle) node can be used to graphically display the contraction of an artificial muscle implemented using [Joint](joint.md) and [Motor](motor.md) nodes.
The artificial muscle is represented using a spheroid where the symmetry axis is the vector between the joint's parent [Solid](solid.md) node and the `endPoint` [Solid](solid.md) node.
The other two axes have the same length computed based on the symmetry axis length so that the volume remains constant during stretching.
In order to define the spheroid's volume, the `minPosition` and `maxPosition` limits of the parent [Motor](motor.md) node have to be defined.

Note that the [Muscle](#muscle) node cannot be used in case of a [Motor](motor.md) device included in a [Hinge2Joint](hinge2joint.md) or [Track](track.md) node.

### Field Summary

- The `maxRadius` field specifies the length of the two equally sized axes of the graphical spheroid when the distance between the joint's parent [Solid](solid.md) and the `endPoint` [Solid](solid.md) nodes is minimal.
This value is used to recompute the shape of the muscle when the joint moves in order to keep the spheroid volume constant.

- The `colors` field specifies the color of the spheroid at the three different muscle states: idle (item 0), negative movement (item 1), and positive movement (item 2).
Depending on the axis setup of the joint setup, the negative movement could correspond to the muscle contraction or the muscle relaxation.
The displayed color results by mixing the idle color and the current state color with a percentage depending on the force applied by the motor:
```
color = idle_color * (1 - percentage) + other_color * percentage
```
where ``other_color`` is contracting or relaxing color.
Only three colors are used, so if more items are specified then they will be ignored.
If only two colors are defined, then same color (item 1) is used when the muscle is contracting or relaxing.
If only one color is defined, then the specified color is be used for all the muscle states.
If `colors` field is empty, the default color (pure red) is used for all the muscle states.

- The `castShadows` field allows the user to turn on (TRUE) or off (FALSE) shadows
casted by the muscle spheroid mesh.

- The `visible` field is used to show (TRUE) or hide (FALSE) the muscle in the 3D scene.
