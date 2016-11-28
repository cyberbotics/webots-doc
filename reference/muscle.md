## Muscle

```
Muscle {
  field SFDouble maxRadius 0.2           # maximum length of the
  field MFColor  colors    []            # idle (0), contracting (1), and relaxing(2) state colors
  field SFBool   visible   TRUE
}
```

### Description

A [Muscle](#muscle) node can be used to graphically display the contraction of an artificial muscle implemented using [SliderJoint](sliderjoint.md) and [LinearMotor](linearmotor.md) nodes.
The artificial muscle is represented using a spheroid where the symmetry axis is the vector between the joint's parent [Solid](solid.md) and the `endPoint` [Solid](solid.md) nodes.
The other two axes have the same length that is computed based on the symmetry axis length so that the volume remains constant.

Note that this node cannot be used in case of a [LinearMotor](linearmotor.md) device included in a [Track](track.md) node.

### Field Summary

- The `maxRadius` field specifies the length of the two equally sized axes of the graphical ellipsoid when the distance between the joint's parent [Solid](solid.md) and the `endPoint` [Solid](solid.md) nodes is minimal.
This value is used to recompute the shape of the muscle when the joint moves in order to keep the ellipsoid volume constant.

- The `colors` field specifies the color of the muscle mesh at the three different muscle states: idle (item 0), contracting (item 1), and relaxing (item 2).
Only three colors are used, so if more items are specified then they will be ignored.
If only two colors are defines, then the idle color (item 0) will also be used when the muscle is relaxing.
If only one color is defined, then the specified color will be used for all the muscle states.
If `colors` field is empty, the default color (pure red) is used.

- The `visible` field is used to show (TRUE) or hide (FALSE) the graphical mesh in the 3D scene.
