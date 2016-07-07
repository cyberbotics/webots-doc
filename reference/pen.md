## Pen

Derived from [Device](device.md).

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

The [Pen](#pen) node models a pen attached to a mobile robot, typically used to
show the trajectory of the robot. The paint direction of the [Pen](solid.md)
device coincides with the *-y*-axis of the node. So, it can be adjusted by
modifying the rotation and translation fields of the [Solid](solid.md) node. By
setting the `maxDistance` field is possible to define the range of the
[Pen](#pen) and paint only on objects close to the device. For example with a
small value of `maxDistance` you can simulate the real behaviour of a pen or
pencil that writes only on physical contact. If `maxDistance` is set to 0
(default value), the range will be unlimited.

In order to be paintable, an object should be made up of a [Solid](solid.md)
node containing a [Shape](shape.md) with a valid `Geometry`. Even if a
[ImageTexture](imagetexture.md) is already defined, the painture is applied over
the texture without modifying it.

The precision of the painting action mainly depends on the `subdivision` field
of the `Geometry` node. A high `subdivision` value increases the number of
polygons used to represent the geometry and thus allows a more precise texture
mapping, but it will also slow down the rendering of the scene. On the other
hand, with a poor texture mapping, the painted area could be shown at a
different position than the expected one. In case of
[IndexedFaceSet](indexedfaceset.md), the precision can be improved by defining a
texture mapping and setting the `texCoord` and `texCoordIndex` fields. In fact,
if no texture mapping or an invalid one is given, the system will use a default
general mapping.

An example of a textured floor used with a robot equipped with a pen is given in
the "pen.wbt" example world (located in the "projects/samples/devices/worlds"
directory of Webots).

> **note**:
The `inkEvaporation` field of the [WorldInfo](worldinfo.md) node controls how
fast the ink evaporates (disappears).

<!-- -->

> **note**:
The drawings performed by a pen can be seen by infra-red distance sensors.
Hence, it is possible to implement a robotics experiment where a robot draws a
line on the floor with a pen and a second robot performs a line following
behavior with the line drawn by the first robot.

### Field Summary

- `inkColor`: define the color of the pen's ink. This field can be changed from
the pen API, using the `wb_pen_set_ink_color()` function.

- `inkDensity`: define the density of the color of the ink. The value should be in
the range [0,1]. This field can also be changed from the pen API, using the
`wb_pen_set_ink_color()` function.

- `leadSize`: define the width of the "tip" of the pen. This allows the robot to
write a wider or narrower track.

- `maxDistance`: define the maximal distance between the [Pen](#pen) device and a
paintable object and allows to simulate write-on-contact behaviors. A value
smaller or equal 0 represents an unlimited painting range.

- `write`: this boolean field allows the robot to enable or disable writing with
the pen. It is also switchable from the pen API, using the `wb_pen_write()`
function.

### Pen Functions

**Name**

**wb\_pen\_write** - *enable or disable pen writing*

{[C++](cpp-api.md#cpp_pen)}, {[Java](java-api.md#java_pen)}, {[Python](python-api.md#python_pen)}, {[Matlab](matlab-api.md#matlab_pen)}, {[ROS](ros-api.md)}

```c
#include <webots/pen.h>

void wb_pen_write(WbDeviceTag tag, bool write);
```

**Description**

`wb_pen_write()` allows the user to switch a pen device on or off to disable or
enable writing. If the `write` parameter is *true*, the specified `tag` device
will write; if `write` is *false*, it won't.

---

**Name**

**wb\_pen\_set\_ink\_color** - *change the color of a pen's ink*

{[C++](cpp-api.md#cpp_pen)}, {[Java](java-api.md#java_pen)}, {[Python](python-api.md#python_pen)}, {[Matlab](matlab-api.md#matlab_pen)}, {[ROS](ros-api.md)}

```c
#include <webots/pen.h>

void wb_pen_set_ink_color(WbDeviceTag tag, int color, double density);
```

**Description**

`wb_pen_set_ink_color()` changes the current ink color of the specified `tag`
device. The `color` is a 32 bit integer value which defines the new color of the
ink in the 0xRRGGBB hexadecimal format (i.e., 0x000000 is black, 0xFF0000 is
red, 0x00FF00 is green, 0x0000FF is blue, 0xFFA500 is orange, 0x808080 is gray
0xFFFFFF is white, etc.). The `density` parameter defines the ink density, with
0 meaning transparent ink and 1 meaning completely opaque ink.

**Example**

```c
wb_pen_set_ink_color(pen,0xF01010,0.9);
```

The above statement will change the ink color of the indicated pen to some red
color.

> **note** [Matlab]:
In the Matlab version of `wb_pen_set_ink_color()`, the `color` argument must be
a vector containing the three RGB components: `[RED GREEN BLUE]`. Each component
must be a value between 0.0 and 1.0. For example the vector `[1 0 1]` represents
the magenta color.
