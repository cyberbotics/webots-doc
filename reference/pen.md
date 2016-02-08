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

- `inkColor`: define the color of the pen's ink. This field can be changed from
the pen API, using the `wb_pen_set_ink_color()` function.
- `inkDensity`: define the density of the color of the ink. The value should be in
the range [0,1]. This field can also be changed from the pen API, using the
`wb_pen_set_ink_color()` function.
- `leadSize`: define the width of the "tip" of the pen. This allows the robot to
write a wider or narrower track.
- `maxDistance`: define the maximal distance between the `Pen` device and a
paintable object and allows to simulate write-on-contact behaviors. A value
smaller or equal 0 represents an unlimited painting range.
- `write`: this boolean field allows the robot to enable or disable writing with
the pen. It is also switchable from the pen API, using the `wb_pen_write()`
function.

### Pen Functions

#### Description

`wb_pen_write()` allows the user to switch a pen device on or off to disable or
enable writing. If the `write` parameter is *true*, the specified `tag` device
will write; if `write` is *false*, it won't.

#### Description

`wb_pen_set_ink_color()` changes the current ink color of the specified `tag`
device. The `color` is a 32 bit integer value which defines the new color of the
ink in the 0xRRGGBB hexadecimal format (i.e., 0x000000 is black, 0xFF0000 is
red, 0x00FF00 is green, 0x0000FF is blue, 0xFFA500 is orange, 0x808080 is grey
0xFFFFFF is white, etc.). The `density` parameter defines the ink density, with
0 meaning transparent ink and 1 meaning completely opaque ink.

#### Example


```
wb_pen_set_ink_color(pen,0xF01010,0.9);
```

The above statement will change the ink color of the indicated pen to some red
color.

