## Pen

Derived from `Device`.


```
Pen {
  SFColor   inkColor     0 0 0   # [0,1]
  SFFloat   inkDensity   0.5     # [0,1]
  SFFloat   leadSize     0.002
  SFFloat   maxDistance  0.0     # >= 0.0
  SFBool    write        TRUE
}
```

### Description

The `Pen` node models a pen attached to a mobile robot, typically used to show
the trajectory of the robot. The paint direction of the `Pen` device coincides
with the *-y*-axis of the node. So, it can be adjusted by modifying the rotation
and translation fields of the `Solid` node. By setting the `maxDistance` field
is possible to define the range of the `Pen` and paint only on objects close to
the device. For example with a small value of `maxDistance` you can simulate the
real behaviour of a pen or pencil that writes only on physical contact. If
`maxDistance` is set to 0 (default value), the range will be unlimited.

In order to be paintable, an object should be made up of a `Solid` node
containing a `Shape` with a valid `Geometry`. Even if a `ImageTexture` is
already defined, the painture is applied over the texture without modifying it.

The precision of the painting action mainly depends on the `subdivision` field
of the `Geometry` node. A high `subdivision` value increases the number of
polygons used to represent the geometry and thus allows a more precise texture
mapping, but it will also slow down the rendering of the scene. On the other
hand, with a poor texture mapping, the painted area could be shown at a
different position than the expected one. In case of `IndexedFaceSet`, the
precision can be improved by defining a texture mapping and setting the
`texCoord` and `texCoordIndex` fields. In fact, if no texture mapping or an
invalid one is given, the system will use a default general mapping.

An example of a textured floor used with a robot equipped with a pen is given in
the "pen.wbt" example world (located in the "projects/samples/devices/worlds"
directory of Webots).

### Field Summary

### Pen Functions

