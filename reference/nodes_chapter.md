# Nodes and API Functions

## Accelerometer

Derived from `Device`.


```
Accelerometer {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute x-axis
  SFBool     yAxis          TRUE  # compute y-axis
  SFBool     zAxis          TRUE  # compute z-axis
  SFFloat    resolution     -1
}
```

### Description

The `Accelerometer` node can be used to model accelerometer devices such as
those commonly found in mobile electronics, robots and game input devices. The
`Accelerometer` node measures acceleration and gravity induced reaction forces
over 1, 2 or 3 axes. It can be used for example to detect fall, the up/down
direction, etc.

### Field Summary

### Accelerometer Functions

## Appearance


```
Appearance {
  SFNode   material           NULL
  SFNode   texture            NULL
  SFNode   textureTransform   NULL
}
```

### Description

The `Appearance` node specifies the visual properties of a geometric node. The
value for each of the fields in this node may be NULL. However, if the field is
non-NULL, it shall contain one node of the appropriate type.

### Field Summary

## Background


```
Background {
  MFString backUrl   []
  MFString bottomUrl []
  MFString frontUrl  []
  MFString leftUrl   []
  MFString rightUrl  []
  MFString topUrl    []
  MFColor  skyColor  [ 0 0 0 ] # [0,1]
}
```

The `Background` node defines the background used for rendering the 3D world.
The `skyColor` field defines the red, green and blue components of this color.
Only the three first float values of the `skyColor` field are used.

The `backUrl`, `bottomUrl`, `frontUrl`, `leftUrl`, `rightUrl`, and `topUrl`
fields specify a set of images that define a background panorama, between the
ground/sky backdrop and the world's geometry. The panorama consists of six
images, each of which is mapped onto the faces of an infinitely large cube
centered in the local coordinate system. The images are applied individually to
each face of the cube; the entire image goes on each face. On the front, back,
right, and left faces of the cube, when viewed from the inside with the Y-axis
up, the texture is mapped onto each face with the same orientation as the if
image was displayed normally in 2D. On the top face of the cube, when viewed
from the inside looking up along the +Y axis with the +Z axis as the view up
direction, the texture is mapped onto the face with the same orientation as the
if image was displayed normally in 2D. On the bottom face of the box, when
viewed from the inside down the -Y axis with the -Z axis as the view up
direction, the texture is mapped onto the face with the same orientation as the
if image was displayed normally in 2D.

## BallJoint

Derived from `Joint`.


```
BallJoint {
}
```

### Description

The `BallJoint` node can be used to model a ball joint. A ball joint, also
called ball-and-socket, prevents translation motion while allowing rotation
around its anchor (3 degrees of freedom). It supports spring and damping
parameters which can be used to simulate the elastic deformation of ropes and
flexible beams.

It inherits `Joint`'s `jointParameters` field. This field can be filled with a
`BallJointParameters` node only. If empty, `BallJointParameters` default values
apply.

## BallJointParameters


```
BallJointParameters {
  field SFVec3f anchor 0 0 0      # point at which the bodies are connected (m)
  field SFFloat springConstant  0 # uniform rotational spring constant (Nm)
  field SFFloat dampingConstant 0 # uniform rotational damping constant (Nms) 
}
```

### Description

The `BallJointJointParameters` node can be used to specify the parameters of a
ball joint. It contains the anchor position, i.e. the coordinates of the point
where bodies under a ball joint constraints are kept attached. It can be used in
the jointParameters field of `BallJoint` only.

### Field Summary

## Box


```
Box {
  SFVec3f   size   2 2 2   # (-inf,inf)
}
```

### Description

The `Box` node specifies a rectangular parallelepiped box centered at (0,0,0) in
the local coordinate system and aligned with the local coordinate axes. By
default, the box measures 2 meters in each dimension, from -1 to +1.

The `size` field specifies the extents of the box along the *x*-, *y*-, and
*z*-axes respectively. See . Three positive values display the outside faces
while three negative values display the inside faces.

![Box node](png/box.png)
**Box node**

Textures are applied individually to each face of the box. On the front (+*z*),
back (-*z*), right (+*x*), and left (-*x*) faces of the box, when viewed from
the outside with the +*y*-axis up, the texture is mapped onto each face with the
same orientation as if the image were displayed normally in 2D. On the top face
of the box (+*y*), when viewed from above and looking down the *y*-axis toward
the origin with the -*z*-axis as the view up direction, the texture is mapped
onto the face with the same orientation as if the image were displayed normally
in 2D. On the bottom face of the box (-*y*), when viewed from below looking up
the *y*-axis toward the origin with the +Z-axis as the view up direction, the
texture is mapped onto the face with the same orientation as if the image were
displayed normally in 2D. `TextureTransform` affects the texture coordinates of
the Box.

## Brake

Derived from `Device`.


```
Brake {
}
```

### Description

A `Brake` node can be used in a mechanical simulation in order to change the
friction of a joint. The `Brake` node can be inserted in the `device` field of a
`HingeJoint`, a `Hinge2Joint`, a `SliderJoint`, or a `Track`.

### Brake Functions

## Camera

Derived from `Device`.


```
Camera {
  SFFloat    fieldOfView      0.7854
  SFInt32    width            64
  SFInt32    height           64
  SFString   type             "color"
  SFBool     spherical        FALSE
  SFFloat    near             0.01
  SFFloat    maxRange         1.0
  SFBool     antiAliasing     FALSE
  SFFloat    motionBlur       0.0
  SFFloat    colorNoise       0.0
  SFFloat    rangeNoise       0.0
  SFFloat    rangeResolution -1.0
  SFNode     lensDistortion   NULL
  SFNode     focus            NULL
  SFNode     zoom             NULL
  SFString   compositor       ""
}
```

### Description

The `Camera` node is used to model a robot's on-board camera or a range-finder.
The resulted image can be displayed on the 3D window. Depending on its setup,
the Camera node can model a linear camera, a lidar device, a Microsoft Kinect or
even a biological eye which is spherically distorted.

### Field Summary

### Camera Type

The camera type can be setup by the `type` field described above.

#### Color

The color camera allows to get color information from the OpenGL context of the
camera. This information can be get by the `wb_camera_get_image` function, while
the red, green and blue channels (RGB) can be extracted from the resulted image
by the `wb_camera_image_get_*`-like functions.

Internally when the camera is refreshed, an OpenGL context is created, and the
color or depth information is copied into the buffer which can be get throught
the `wb_camera_get_image` or the `wb_camera_get_range_image` functions. The
format of these buffers are respectively BGRA (32 bits) and float (16 bits). We
recommend to use the `wb_camera_image_get_*`-like functions to access the buffer
because the internal format could change.

#### Range-Finder

The range-finder camera allows to get depth information (in meters) from the
OpenGL context of the camera. This information is obtained through the
`wb_camera_get_range_image` function, while depth information can be extracted
from the returned image by using the `wb_camera_range_image_get_depth` function.

Internally when the camera is refreshed, an OpenGL context is created, and the
z-buffer is copied into a buffer of `float`. As the z-buffer contains scaled and
logarithmic values, an algorithm linearizes the buffer to metric values between
`near` and `maxRange`. This is the buffer which is accessible by the
`wb_camera_get_range_image` function.

Range-finder cannot see transparent objects. An object can be semi-transparent
either if its texture has an alpha channel, or if its `Material`.`transparency`
field is not equal to 1.

### Frustum

The frustum is the truncated pyramid defining what is visible from the camera.
Any 3D shape completely outside this frustum won't be rendered. Hence, shapes
located too close to the camera (standing between the camera and the near plane)
won't appear. It can be displayed with magenta lines by enabling the
`View|Optional Rendering|Show Camera Frustums` menu item. The `near` field
defines the position of the near clipping plane (x, y, -near). The `fieldOfView`
field defines the horizontal angle of the frustum. The `fieldOfView`, `width`
and `height` fields define the vertical angle of the frustum according to the
above formula.

Generally speaking there is no far clipping plane while this is common in other
OpenGL programs. In Webots, a camera can see as far as needed. Nevertheless, a
far clipping plane is artificially added in the case of range-finder cameras
(i.e. the resulted values are bounded by the `maxRange` field).

In the case of the spherical cameras, the frustum is quite different and
difficult to represent. In comparison with the frustum description above, the
near and the far planes are transformed to be sphere parts having their center
at the camera position, and the `fieldOfView` can be greater than Pi.

### Noise

It is possible to add quickly a white noise on the cameras by using the
`colorNoise` and the `rangeNoise` fields (applied respectively on the color
cameras and on the range-finder cameras). A value of `0.0` corresponds to an
image without noise. For each channel of the image and at each camera refresh, a
gaussian noise is computed and added to the channel. This gaussian noise has a
standard deviation corresponding to the noise field times the channel range. The
channel range is 256 for a color camera and `maxRange` for a range-finder
camera.

### Spherical projection

OpenGL is designed to have only planar projections. However spherical
projections are very useful for simulating a lidar, a camera pointing on a
curved mirror or a biological eye. Therefore we implemented a camera mode
rendering spherical projections. It can be enabled simply by switching on the
corresponding `spherical` field described above.

Internally, depending on the field of view, a spherical camera is implemented by
using between 1 to 6 OpenGL cameras oriented towards the faces of a cube (the
activated cameras are displayed by magenta squares when the `View|Optional
Rendering|Show Camera Frustums` menu item is enabled). Moreover an algorithm
computing the spherical projection is applied on the result of the subcameras.

So this mode is costly in terms of performance! Reducing the resolution of the
cameras and using a `fieldOfView` which minimizes the number of activated
cameras helps a lot to improve the performances if needed.

When the camera is spherical, the image returned by the `wb_camera_get_image` or
the `wb_camera_get_range_image` functions is a 2-dimensional array (s,t) in
spherical coordinates.

Let `hFov` be the horizontal field of view, and let `theta` be the angle in
radian between the `(0, 0, -z)` relative coordinate and the relative coordinate
of the target position along the `xz` plane relative to the camera, then `s=0`
corresponds to a `theta` angle of `-hFov/2`, `s=(width-1)/2` corresponds to a
`theta` angle of 0, and `s=width-1` corresponds to a `theta` angle of `hFov/2`.

Similarly, let `vFov` be the vertical field of view (defined just above), and
`phi` the angle in radian between the `(0, 0, -z)` relative coordinate and the
relative coordinate of the target position along the `xy` plane relative to the
camera, `t=0` corresponds to a `phi` angle of `-vFov/2`, `t=(height-1)/2`
corresponds to a `phi` angle of 0, and `t=height-1` corresponds to a `phi` angle
of `vFov/2`).

### Overlay Image

![Camera overlay image](png/camera_overlay.png)
**Camera overlay image**

The camera image is shown by default on top of the 3D window with a magenta
border, see . The user can move this camera image at the desired position using
the mouse drag and drop and resize it by clicking on the icon at the bottom
right corner. Additionally a close button is available on the top right corner
to hide the image. Once the robot is selected, it is also possible to show or
hide the overlay images from the `Camera Devices` item in `Robot` menu.

It is also possible to show the camera image in an external window by double-
clicking on it. After doing it, the overlay disappears and the new window pops
up. Then, after closing the window, the overlay will be automatically restored.

### Camera Functions

## CameraFocus


```
CameraFocus {
  SFFloat  focalDistance     0  # Distance to the object we are focusing on (m)
  SFFloat  focalLength       0  # Focal length of the lens (m)
  SFFloat  maxFocalDistance  0  # (m)
  SFFloat  minFocalDistance  0  # (m)
}
```

### Description

The `CameraFocus` node allows the user to define a controllable focus for a
`Camera` device. The `CameraFocus` node should be set in the `focus` field of a
`Camera` node. The focal distance can be adjusted from the controller program
using the `wb_camera_set_focal_distance()` function.

### Field Summary

## CameraLensDistortion


```
CameraLensDistortion {
  SFVec2f  center                  0.5 0.5
  SFVec2f  radialCoefficients      0 0
  SFVec2f  tangentialCoefficients  0 0
}
```

### Description

The `CameraLensDistortion` node allows the user to simulate the camera image
distortion due to the camera lens. A Brown's distortion model with two
coefficients both for the radial and tangential distortions is used to simulate
image distortion.

### Field Summary

## CameraZoom


```
CameraZoom {
  SFFloat     maxFieldOfView 1.5 # (rad)
  SFFloat     minFieldOfView 0.5 # (rad)
}
```

### Description

The `CameraZoom` node allows the user to define a controllable zoom for a
`Camera` device. The `CameraZoom` node should be set in the `zoom` field of a
`Camera` node. The zoom level can be adjusted from the controller program using
the `wb_camera_set_fov()` function.

### Field Summary

## Capsule


```
Capsule {
  SFBool    bottom        TRUE
  SFFloat   height        2     # (-inf,inf)
  SFFloat   radius        1     # (-inf,inf)
  SFBool    side          TRUE
  SFBool    top           TRUE
  SFInt32   subdivision   12    # (2,inf)
}
```

### Description

A `Capsule` node is like a `Cylinder` node except it has half-sphere caps at its
ends. The capsule's height, not counting the caps, is given by the `height`
field. The radius of the caps, and of the cylinder itself, is given by the
`radius` field. Capsules are aligned along the local y-axis.

The capsule can be used either as a graphical or collision detection primitive
(when placed in a `boundingObject`). The capsule is a particularly fast and
accurate collision detection primitive.

A capsule has three optional parts: the `side`, the `top` and the `bottom`. Each
part has an associated boolean field that indicates whether the part should be
drawn or not. For collision detection, all parts are considered to be present,
regardless of the value of these boolean fields.

If both `height` and `radius` are positive, the outside faces of the capsule are
displayed while if they are negative, the inside faces are displayed. The values
of `height` and `radius` must both be greater than zero when the capsule is used
for collision detection.

The `subdivision` field defines the number of triangles that must be used to
represent the capsule and so its resolution. More precisely, it corresponds to
the number of faces that compose the capsule's side. This field has no effect on
collision detection.

![The Capsule node](png/capsule.png)
**The Capsule node**

When a texture is mapped to a capsule, the texture map is vertically divided in
three equally sized parts (e.g., like the German flag). The top part is mapped
to the capsule's top. The middle part is mapped to the capsule's side (body).
The bottom part is mapped to the capsule's bottom. On each part, the texture
wraps counterclockwise (seen from above) starting from the intersection with the
*y*- and negative *z*-plane.

## Charger

Derived from `Solid`.


```
Charger {
  MFFloat   battery        []
  SFFloat   radius         0.04    # (0,inf)
  SFColor   emissiveColor  0 1 0   # [0,1]
  SFBool    gradual        TRUE
}
```

### Description

The `Charger` node is used to model a special kind of battery charger for the
robots. A robot has to get close to a charger in order to recharge itself. A
charger is not like a standard battery charger connected to a constant power
supply. Instead, it is a battery itself: it accumulates energy with time. It
could be compared to a solar power panel charging a battery. When the robot
comes to get energy, it can't get more than the charger has presently
accumulated.

The appearance of the `Charger` node can be altered by its current energy. When
the `Charger` node is full, the resulted color corresponds to its
`emissiveColor` field, while when the `Charger` node is empty, its resulted
color corresponds to its original one. Intermediate colors depend on the
`gradual` field. Only the first child of the `Charger` node is affected by this
alteration. The resulted color is applied only on the first child of the
`Charger` node. If the first child is a `Shape` node, the `emissiveColor` field
of its `Material` node is altered. If the first child is a `Light` node, its
`color` field is altered. Otherwise, if the first child is a `Group` node, a
recursive search is applied on this node and every `Light`, `Shape` and `Group`
nodes are altered according to the two previous rules.

### Field Summary

The fields specific to the `Charger` node are:

## Color


```
Color {
  MFColor   color   []   # [0,1]
}
```

This node defines a set of RGB colors to be used in the fields of another node.

`Color` nodes are only used to specify multiple colors for a single geometric
shape, such as colors for the faces or vertices of an `ElevationGrid`. A
`Material` node is used to specify the overall material parameters of a
geometric node. If both a `Material` node and a `Color` node are specified for a
geometric shape, the colors shall replace the diffuse component of the material.

RGB or RGBA textures take precedence over colors; specifying both an RGB or RGBA
texture and a Color node for a geometric shape will result in the Color node
being ignored.

## Compass

Derived from `Device`.


```
Compass {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute x-axis
  SFBool     yAxis          TRUE  # compute y-axis
  SFBool     zAxis          TRUE  # compute z-axis
  SFFloat    resolution     -1
}
```

### Description

A `Compass` node can be used to model a 1, 2 or 3-axis digital compass (magnetic
sensor). The `Compass` node returns a vector that indicates the direction of the
*virtual north*. The *virtual north* is specified by the `northDirection` field
in the `WorldInfo` node.

### Field Summary

### Compass Functions

## Cone


```
Cone {
  SFFloat   bottomRadius   1   # (-inf,inf)
  SFFloat   height         2   # (-inf,inf)
  SFBool    side           TRUE
  SFBool    bottom         TRUE
  SFInt32   subdivision    12  # (3,inf)
}
```

The `Cone` node specifies a cone which is centered in the local coordinate
system and whose central axis is aligned with the local *y*-axis. The
`bottomRadius` field specifies the radius of the cone's base, and the `height`
field specifies the height of the cone from the center of the base to the apex.
By default, the cone has a radius of 1 meter at the bottom and a height of 2
meters, with its apex at y = height/2 and its bottom at y = -height/2.  See .

If both `bottomRadius` and `height` are positive, the outside faces of the cone
are displayed while if they are negative, the inside faces are displayed.

The `side` field specifies whether the sides of the cone are created, and the
`bottom` field specifies whether the bottom cap of the cone is created. A value
of `TRUE` specifies that this part of the cone exists, while a value of `FALSE`
specifies that this part does not exist.

The `subdivision` field defines the number of polygons used to represent the
cone and so its resolution. More precisely, it corresponds to the number of
lines used to represent the bottom of the cone.

![The Cone node](png/cone.png)
**The Cone node**

When a texture is applied to the sides of the cone, the texture wraps
counterclockwise (from above) starting at the back of the cone. The texture has
a vertical seam at the back in the *yz* plane, from the apex (0, `height`/2, 0)
to the point (0, 0, -r). For the bottom cap, a circle is cut out of the unit
texture square centered at (0, -`height`/2, 0) with dimensions (2 *
`bottomRadius`) by (2 * `bottomRadius`). The bottom cap texture appears right
side up when the top of the cone is rotated towards the -Z axis.
`TextureTransform` affects the texture coordinates of the Cone.

`Cone` geometries cannot be used as primitives for collision detection in
bounding objects.

## Connector

Derived from `Device`.


```
Connector {
  SFString   type                "symmetric"
  SFBool     isLocked            FALSE
  SFBool     autoLock            FALSE
  SFBool     unilateralLock      TRUE
  SFBool     unilateralUnlock    TRUE
  SFFloat    distanceTolerance   0.01  # [0,inf)
  SFFloat    axisTolerance       0.2   # [0,pi)
  SFFloat    rotationTolerance   0.2   # [0,pi)
  SFInt32    numberOfRotations   4
  SFBool     snap                TRUE
  SFFloat    tensileStrength     -1
  SFFloat    shearStrength       -1
}
```

### Description

`Connector` nodes are used to simulate mechanical docking systems, or any other
type of device, that can dynamically create a physical link (or *connection*)
with another device of the same type.

`Connector` nodes can only connect to other `Connector` nodes. At any time, each
connection involves exactly two `Connector` nodes (peer to peer). The physical
connection between two `Connector` nodes can be created and destroyed at run
time by the robot's controller. The primary idea of `Connector` nodes is to
enable the dynamic reconfiguration of modular robots, but more generally,
`Connector` nodes can be used in any situation where robots need to be attached
to other robots.

`Connector` nodes were designed to simulate various types of docking hardware:

Connectors can be classified into two types, independent of the actual hardware
system:

*Symmetric connectors*, where the two connecting faces are mechanically (and
electrically) equivalent. In such cases both connectors are active.

*Asymmetric connectors*, where the two connecting interfaces are mechanically
different. In asymmetric systems there is usually one active and one passive
connector.

The detection of the presence of a peer `Connector` is based on simple distance
and angle measurements, and therefore the `Connector` nodes are a
computationally inexpensive way of simulating docking mechanisms.

### Field Summary

### Connector Axis System

A `Connector`'s axis system is displayed by Webots when the corresponding robot
is selected or when *Display Axes* is checked in Webots *Preferences*. The
*z*-axis is drawn as a 5 cm blue line, the y-axis (a potential docking rotation)
is drawn as a 5 cm red line, and each additional potential docking rotation is
displayed as a 4 cm black line. The bounding objects and graphical objects of a
`Connector` should normally be designed such that the docking surface
corresponds exactly to *xy*-plane of the local coordinate system. Furthermore,
the `Connector`'s z-axis should be perpendicular to the docking surface and
point outward from the robot body. Finally, the bounding objects should allow
the superposition of the origin of the coordinate systems. If these design
criteria are not met, the `Connector` nodes will not work properly and may be
unable to connect.

![Connector axis system](png/connector_axes.png)
**Connector axis system**

### Connector Functions

## ContactProperties


```
ContactProperties {
  SFString   material1           "default"
  SFString   material2           "default"
  MFFloat    coulombFriction     1          # [0,inf)
  SFVec2f    frictionRotation    0 0
  SFFloat    bounce              0.5        # [0,1]
  SFFloat    bounceVelocity      0.01       # (m/s)
  MFFloat    forceDependentSlip  0
  SFFloat    softERP             0.2
  SFFloat    softCFM             0.001
}
```

### Description

`ContactProperties` nodes define the contact properties to use in case of
contact between `Solid` nodes (or any node derived from `Solid`).
`ContactProperties` nodes are placed in the `contactProperties` field of the
`WorldInfo` node. Each `ContactProperties` node specifies the name of two
*materials* for which these `ContactProperties` are valid.

When two `Solid` nodes collide, a matching `ContactProperties` node is searched
in the `WorldInfo`.`contactProperties` field. A `ContactProperties` node will
match if its `material1` and `material2` fields correspond (in any order) to the
the `contactMaterial` fields of the two colliding `Solid`s. The values of the
first matching `ContactProperties` are applied to the contact. If no matching
node is found, default values are used. The default values are the same as those
indicated above.

### Field Summary

## Coordinate


```
Coordinate {
  MFVec3f   point   []   # (-inf,inf)
}
```

This node defines a set of 3D coordinates to be used in the `coord` field of
vertex-based `Geometry` nodes including `IndexedFaceSet` and `IndexedLineSet`.

## Cylinder


```
Cylinder {
  SFBool    bottom        TRUE
  SFFloat   height        2     # (-inf,inf)
  SFFloat   radius        1     # (-inf,inf)
  SFBool    side          TRUE
  SFBool    top           TRUE
  SFInt32   subdivision   12    # (2,inf)
}
```

### Description

The `Cylinder` node specifies a cylinder centered at (0,0,0) in the local
coordinate system and with a central axis oriented along the local *y*-axis. By
default, the cylinder spans -1 to +1 in all three dimensions. The `radius` field
specifies the radius of the cylinder and the `height` field specifies the height
of the cylinder along the central axis. See .

If both `height` and `radius` are positive, the outside faces of the cylinder
are displayed while if they are negative, the inside faces are displayed.

The cylinder has three parts: the side, the top (y = +`height`/2) and the bottom
(y = -`height+`/2). Each part has an associated `SFBool` field that indicates
whether the part exists (`TRUE`) or does not exist (`FALSE`). Parts which do not
exist are not rendered. However, all parts are used for collision detection,
regardless of their associated `SFBool` field.

The `subdivision` field defines the number of polygons used to represent the
cylinder and so its resolution. More precisely, it corresponds to the number of
lines used to represent the bottom or the top of the cylinder.

![The Cylinder node](png/cylinder.png)
**The Cylinder node**

When a texture is applied to a cylinder, it is applied differently to the sides,
top, and bottom. On the sides, the texture wraps counterclockwise (from above)
starting at the back of the cylinder. The texture has a vertical seam at the
back, intersecting the yz plane. For the top and bottom caps, a circle is cut
out of the unit texture squares centered at (0, +/- `height`, 0) with dimensions
2*`radius`  by 2*`radius`. The top texture appears right side up when the top of
the cylinder is tilted toward the +*z* axis, and the bottom texture appears
right side up when the top of the cylinder is tilted toward the -*z* axis.
`TextureTransform` affects the texture coordinates of the Cylinder.

## Damping


```
Damping {
    SFFloat   linear        0.2     # [0,1]
    SFFloat   angular       0.2     # [0,1]
}
```

### Description

A `Damping` node can be used to slow down a body (a `Solid` node with
`Physics`). The speed of each body is reduced by the specified amount (between
0.0 and 1.0) every second. A value of 0.0 means "no slowing down" and value of
1.0 means a "complete stop", a value of 0.1 means that the speed should be
decreased by 10 percent every second. Note that the behavior of this value on
the solid speeds is nonlinear: a linear damping of 0.99 is far to affect the
solids speeds as a linear damping of 1.0. A damped body will possibly come to
rest and become disabled depending on the values specified in `WorldInfo`.
Damping does not add any force in the simulation, it directly affects the
velocity of the body. The damping effect is applied after all forces have been
applied to the bodies. Damping can be used to reduce simulation instability.

The `linear` field indicates the amount of damping that must be applied to the
body's linear motion. The `angular` field indicates the amount of damping that
must be applied to the body's angular motion. The linear damping can be used,
e.g., to slow down a vehicule by simulating air or water friction. The angular
damping can be used, e.g., to slow down the rotation of a rolling ball or the
spin of a coin. Note that the damping is applied regardless of the shape of the
object, so damping cannot be used to model complex fluid dynamics (use
`ImmersionProperties` and `Fluid` nodes instead).

A `Damping` node can be specified in the `defaultDamping` field of the
`WorldInfo` node; in this case it defines the default damping parameters that
must be applied to every body in the simulation. A `Damping` node can be
specified in the `damping` field of a `Physics` node; in this case it defines
the damping parameters that must be applied to the `Solid` that contains the
`Physics` node. The damping specified in a `Physics` node overrides the default
damping.

## Device

Abstract node, derived from `Solid`.


```
Device {
}
```

### Description

This abstract node (not instanciable) represents a robot device (actuator and/or
sensor).

### Device Functions

## DifferentialWheels

Derived from `Robot`.


```
DifferentialWheels {
  SFFloat   motorConsumption    0      # [0,inf)
  SFFloat   axleLength          0.1    # (0,inf)
  SFFloat   wheelRadius         0.01   # (0,inf)
  SFFloat   maxSpeed            10     # (0,inf)
  SFFloat   maxAcceleration     10     
  SFFloat   speedUnit           1
  SFFloat   slipNoise           0.1    # [0,inf)
  SFFloat   encoderNoise        -1
  SFFloat   encoderResolution   -1
  SFFloat   maxForce            0.3    # (0,inf)
}
```

### Description

The `DifferentialWheels` node can be used as base node to build robots with two
wheels and differential steering. Any other type of robot (legged, humanoid,
vehicle, etc.) needs to use `Robot` as base node.

A `DifferentialWheels` robot will automatically take control of its wheels if
they are placed in the `children` field. The wheels must be `Solid` nodes, and
they must be named "right wheel" and "left wheel". If the wheel objects are
found, Webots will automatically make them rotate at the speed specified by the
`wb_differential_wheels_set_speed()` function.

The origin of the robot coordinate system is the projection on the ground plane
of the middle of the wheels' axle. The *x* axis is the axis of the wheel axle,
*y* is the vertical axis and *z* is the axis pointing towards the rear of the
robot (the front of the robot has negative *z* coordinates).

### Field Summary

### Simulation Modes

The `DifferentialWheels`'s motion can be computed by different algorithms:
"physics" or "kinematics" depending on the structure of the world.

#### Physics mode

A `DifferentialWheels` is simulated in "physics" mode if it contains `Physics`
nodes in its body and wheels. In this mode, the simulation is carried out by the
ODE physics engine, and the robot's motion is caused by the friction forces
generated by the contact of the wheels with the floor. The wheels can have any
arbitrary shape (usually a cylinder), but their contact with the floor is
necessary for the robot's motion. In "physics" mode the inertia, weight, etc. of
the robot and wheels is simulated, so for example the robot will fall if you
drop it. The friction is simulated with the Coulomb friction model, so a
`DifferentialWheels` robot would slip on a wall with some friction coefficient
that you can tune in the `Physics` nodes. The "physics" mode is the most
realistic but also the slowest simulation mode.

#### Kinematics mode

When a `DifferentialWheels` does not have `Physics` nodes then it is simulated
in "kinematics" mode. In the "kinematics" mode the robot's motion is calculated
according to 2D kinematics algorithms and the collision detection is calculated
with 3D algorithms. Friction is not simulated, so a `DifferentialWheels` does
not actually require the contact of the wheels with the floor to move. Instead,
its motion is controlled by a 2D kinematics algorithm using the  `axleLength,
wheelRadius` and `maxAcceleration` fields. Because friction is not simulated the
`DifferentialWheels` will not slide on a wall or on another robot. The
simulation will rather look as if obstacles (walls, robots, etc.) are very rough
or harsh. However the robots can normally avoid to become blocked by changing
direction, rotating the wheels backwards, etc. Unlike the "physics" mode, in the
"kinematics" mode the gravity and other forces are not simulated therefore a
`DifferentialWheels` robot will keep its initial elevation throughout the
simulation.

### DifferentialWheels Functions

## DirectionalLight

Derived from `Light`.


```
DirectionalLight {
  SFVec3f   direction   0 0 -1   # (-inf,inf)
}
```

### Description

The `DirectionalLight` node defines a directional light source that illuminates
along rays parallel to a given 3-dimensional vector. Unlike `PointLight`, rays
cast by `DirectionalLight` nodes do not attenuate with distance.

### Field Summary

## Display

Derived from `Device`.


```
Display {
  SFInt32    width          64
  SFInt32    height         64
}
```

### Description

The `Display` node allows to handle a 2D pixel array using simple API functions,
and render it into a 2D overlay on the 3D view, into a 2D texture of any `Shape`
node, or both. It can model an embedded screen or it can display any graphical
information such as graphs, text, robot trajectory, filtered camera images and
so on.

If the first child of the `Display` node is or contains (recursive search if the
first node is a `Group`) a `Shape` node having a `ImageTexture`, then the
internal texture of the(se) `ImageTexture` node(s) is replaced by the texture of
the `Display`.

### Field Summary

### Coordinates system

Internally, the `Display` image is stored in a 2D pixel array. The RGBA value
(4x8 bits) of a pixel is dislayed in the status bar (the bar at the bottom of
the console window) when the mouse hovers over the pixel in the `Display`. The
2D array has a fixed size defined by the `width` and `height` fields. The (0,0)
coordinate corresponds to the top left pixel, while the (`width`-1,`height`-1)
coordinate corresponds to the bottom right pixel.

### Command stack

Each function call of the `Display` device API (except for
`wb_display_get_width()` and `wb_display_get_height()`) is storing a specific
command into an internal stack. This command stack is sent to Webots during the
next call of the `wb_robot_step()` function, using a FIFO scheme (First In,
First Out), so that commands are executed in the same order as the corresponding
function calls.

### Context

The `Display` device has among other things two kinds of functions; the
contextual ones which allow to set the current state of the display, and the
drawing ones which allow to draw specific primitives. The behavior of the
drawing functions depends on the display context. For example, in order to draw
two red lines, the `wb_display_set_color` contextual function must be called for
setting the display's internal color to red before calling twice the
`wb_display_draw_line` drawing function to draw the two lines.

### Overlay Image

![Display overlay image](png/display_overlay.png)
**Display overlay image**

The display image is shown by default on top of the 3D window with a cyan
border, see . The user can move this display image at the desired position using
the mouse drag and drop and resize it by clicking on the icon at the bottom
right corner. Additionally a close button is available on the top right corner
to hide the image. Once the robot is selected, it is also possible to show or
hide the overlay image from the `Display Devices` item in `Robot` menu.

It is also possible to show the display image in an external window by double-
clicking on it. After doing it, the overlay disappears and the new window pops
up. Then, after closing the window, the overlay will be automatically restored.

### Display Functions

## DistanceSensor

Derived from `Device`.


```
DistanceSensor {
  MFVec3f    lookupTable     [ 0 0 0, 0.1 1000 0 ]
  SFString   type            "generic"
  SFInt32    numberOfRays    1        # [1,inf)
  SFFloat    aperture        1.5708   # [0,2pi]
  SFFloat    gaussianWidth   1
  SFFloat    resolution     -1
}
```

### Description

The `DistanceSensor` node can be used to model a generic sensor, an infra-red
sensor, a sonar sensor, or a laser range-finder. This device simulation is
performed by detecting the collisions between one or several sensor rays and
objects in the environment. In case of generic, sonar and laser type the
collision occurs with the bounding objects of `Solid` nodes, whereas infra-red
rays collision detection uses the `Solid` nodes themselves.

The rays of the `DistanceSensor` nodes can be displayed by checking the menu
`View > Optional Rendering > Show Distance Sensor Rays`. The red/green
transition on the rays indicates the points of intersection with the bounding
objects.

### Field Summary

### DistanceSensor types

This table summarizes the difference between the three types of DistanceSensor.

Two different methods are used for calculating the distance from an object.
*Average* method computes the average of the distances measured by all the rays,
whereas *Nearest* method uses the shortest distance measured by any of the rays.

### Infra-Red Sensors

In the case of an "infra-red" sensor, the value returned by the lookup table is
modified by a reflection factor depending on the color properties of the object
hit by the sensor ray. The reflection factor is computed as follows: *f = 0.2 +
0.8 * red_level* where *red_level* is the level of red color of the object hit
by the sensor ray. This level is evaluated combining the `diffuseColor` and
`transparency` values of the object, the pixel value of the image texture and
the paint color applied on the object with the `Pen` device. Then, the distance
value computed by the simulator is divided by the reflection factor before the
lookup table is used to compute the output value.

### Sonar Sensors

In the case of a "sonar" sensor, the return value will be the last value entered
in the lookup table, i.e. the value corresponding to sonar sensor's range, if
the angle of incidence is greater than 22.5 degrees (pi/8 radians). In other
words, sonar rays which lie outside the reflexion cone of aperture 45 degrees
never return and thus are lost for distance computation (see ).

![Sonar sensor](pdf/sonar_reflection.pdf)
**Sonar sensor**

### Line Following Behavior

Some support for `DistanceSensor` nodes used for reading the red color level of
a textured floor is implemented. This is useful to simulate line following
behaviors. This feature is demonstrated in the "rover.wbt" example (see in the
"projects/robots/mindstorms/worlds" directory of Webots). The ground texture
must be placed in a `Plane`.

### DistanceSensor Functions

## ElevationGrid


```
ElevationGrid {
  SFNode    color            NULL
  MFFloat   height           []     # (-inf,inf)
  SFBool    colorPerVertex   TRUE
  SFInt32   xDimension       0      # [0,inf)
  SFFloat   xSpacing         1      # (0,inf)
  SFInt32   zDimension       0      # [0,inf)
  SFFloat   zSpacing         1      # (0,inf)
  SFFloat   thickness        1      # [0,inf)
}
```

### Description

The `ElevationGrid` node specifies a uniform rectangular grid of varying height
in the *y=0* plane of the local coordinate system. The geometry is described by
a scalar array of height values that specify the height of the surface above
each point of the grid. The `ElevationGrid` node is the most appropriate to
model an uneven terrain.

### Field Summary

The `xDimension` and `zDimension` fields indicate the number of points in the
grid height array in the *x* and *z* directions. Both `xDimension` and
`zDimension` shall be greater than or equal to zero. If either the `xDimension`
or the `zDimension` is less than two, the `ElevationGrid` contains no
quadrilaterals. The vertex locations for the quadrilaterals are defined by the
`height` field and the `xSpacing` and `zSpacing` fields:

![ElevationGrid node](png/elevation_grid.png)
**ElevationGrid node**

Thus, the vertex corresponding to the point P[i,j] on the grid is placed at:


```
P[i,j].x = xSpacing * i
P[i,j].y = height[ i + j * xDimension]
P[i,j].z = zSpacing * j

where 0 lt= i lt xDimension and 0 lt= j lt zDimension,
and P[0,0] is height[0] units above/below the origin of the local
coordinate system
```

The `color` field specifies per-vertex or per-quadrilateral colors for the
`ElevationGrid` node depending on the value of `colorPerVertex`. If the `color`
field is NULL, the `ElevationGrid` node is rendered with the overall attributes
of the `Shape` node enclosing the `ElevationGrid` node. If only two colors are
supplied, these two colors are used alternatively to display a checkerboard
structure.

The `colorPerVertex` field determines whether colors specified in the color
field are applied to each vertex or each quadrilateral of the `ElevationGrid`
node. If `colorPerVertex` is `FALSE` and the `color` field is not NULL, the
`color` field shall specify a `Color` node containing at least (`xDimension`-1)
x (`zDimension`-1) colors.

If `colorPerVertex` is `TRUE` and the `color` field is not NULL, the `color`
field shall specify a `Color` node containing at least `xDimension` x
`zDimension` colors, one for each vertex.

The `thickness` field specifies the thickness of the bounding box which is added
below the lowest point of the `height` field, to prevent objects from falling
through very thin `ElevationGrid`s.

### Texture Mapping

The default texture mapping produces a texture that is upside down when viewed
from the positive *y*-axis. To orient the texture with a more intuitive mapping,
use a `TextureTransform` node to reverse the texture coordinate, like this:


```
Shape { 
  appearance Appearance { 
    textureTransform TextureTransform {
      scale 1 -1
    } 
  } 
  geometry ElevationGrid {
    ...
  } 
}
```

This will produce a compact `ElevationGrid` with texture mapping that aligns
with the natural orientation of the image.

## Emitter

Derived from `Device`.


```
Emitter {
  SFString   type         "radio"  # or "serial" or "infra-red"
  SFFloat    range        -1       # -1 or positive
  SFFloat    maxRange     -1       # -1 or positive
  SFFloat    aperture     -1       # -1 or between 0 and 2*pi
  SFInt32    channel      0
  SFInt32    baudRate     -1       # -1 or positive
  SFInt32    byteSize     8        # 8 or more
  SFInt32    bufferSize   -1       # -1 or positive
}
```

### Description

The `Emitter` node is used to model radio, serial or infra-red emitters. An
`Emitter` node must be added to the children of a robot or a supervisor. Please
note that an emitter can send data but it cannot receive data. In order to
simulate a unidirectional communication between two robots, one robot must have
an `Emitter` while the other robot must have a `Receiver`. To simulate a
bidirectional communication between two robots, each robot needs to have both an
`Emitter` and a `Receiver`. Note that messages are never transmitted from one
robot to itself.

### Field Summary

### Emitter Functions

And here an example on how to send binary data with the C API:

## Fluid

Derived from `Transform`.


```
Fluid {
  SFString  description     ""
  field     SFString         name           "fluid"   # used in ImmersionProperties
  field     SFString         model           ""       # generic name of the fluid (eg: "sea")
  field     SFString         description     ""       # a short (1 line) of description of the fluid
  field     SFFloat          density         1000     # (kg/m^3) fluid density
  field     SFFloat          viscosity       0.001    # (kg/(ms)) fluid's dynamic viscosity
  field     SFVec3f          streamVelocity  0 0 0    # (m/s) linear fluid velocity
  SFNode    boundingObject   NULL
  SFBool    locked           FALSE
}
```

### Description

A `Fluid` node represents a possibly unbounded fluid volume with physical
properties such as density and stream velocity. A `Solid` node which is
partially or fully immersed in some `Fluid`'s `boundingObject` will be subject
to the static force (Archimedes'thrust) and the dynamic force (drag force)
exerted by the `Fluid` provided it has a `Physics` node, a `boundingObject` and
that its field `immersionProperties` contains an `ImmersionProperties` node
referring to the given `Fluid`.

In the 3D window, `Fluid` nodes can be manipulated (dragged, lifted, rotated,
etc) using the mouse.

### Fluid Fields

Note that in the `Fluid` node, the `scale` field inherited from the `Transform`
must always remain uniform, i.e., of the form `x x x` where `x` is any positive
real number. This ensures that all primitive geometries will remain suitable for
ODE immersion detection. Whenever a scale coordinate is changed, the two other
ones are automatically changed to this new value. If a scale coordinate is
assigned a non-positive value, it is automatically changed to 1.

## Fog


```
Fog {
  SFColor    color             1 1 1    # [0,1]
  SFString   fogType           "LINEAR"
  SFFloat    visibilityRange   0        # [0,inf)
}
```

The `Fog` node provides a way to simulate atmospheric effects by blending
objects with the color specified by the `color` field based on the distances of
the various objects from the camera. The distances are calculated in the
coordinate space of the `Fog` node. The `visibilityRange` specifies the distance
in meters (in the local coordinate system) at which objects are totally obscured
by the fog. Objects located beyond the `visibilityRange` of the camera are drawn
with a constant specified by the `color` field. Objects very close to the viewer
are blended very little with the fog `color`. A `visibilityRange` of 0.0
disables the `Fog` node.

The `fogType` field controls how much of the fog color is blended with the
object as a function of distance. If `fogType` is "LINEAR", the amount of
blending is a linear function of the distance, resulting in a depth cueing
effect. If `fogType` is "EXPONENTIAL", an exponential increase in blending is
used, resulting in a more natural fog appearance. If `fogType` is
"EXPONENTIAL2", a square exponential increase in blending is used, resulting in
an even more natural fog appearance (see the OpenGL documentation for more
details about fog rendering).

## GPS

Derived from `Device`.


```
GPS {
  SFString   type              "satellite"
  SFFloat    accuracy          0
  SFFloat    noiseCorrelation  0
  SFFloat    resolution       -1
}
```

### Description

The `GPS` node is used to model a Global Positioning Sensor (GPS) which can
obtain information about its absolute position from the controller program.

### Field Summary

### GPS Functions

## Group


```
Group {
  MFNode   children   []
}
```

Direct derived nodes: `Transform`.

A `Group` node contains `children` nodes without introducing a new
transformation. It is equivalent to a `Transform` node containing an identity
transform.

A `Group` node may not contain subsequent `Solid`, device or robot nodes.

## Gyro

Derived from `Device`.


```
Gyro {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute x-axis
  SFBool     yAxis          TRUE  # compute y-axis
  SFBool     zAxis          TRUE  # compute z-axis
  SFFloat    resolution     -1
}
```

### Description

The `Gyro` node is used to model 1, 2 and 3-axis angular velocity sensors
(gyroscope). The angular velocity is measured in radians per second [rad/s].

### Field Summary

### Gyro Functions

## HingeJoint

Derived from `Joint`.


```
HingeJoint {
  field       MFNode  device   [ ] # RotationalMotor, PositionSensor and Brake
  hiddenField SFFloat position 0   # (rad) initial position
}
```

### Description

The `HingeJoint` node can be used to model a hinge, i.e. a joint allowing only a
rotational motion around a given axis (1 degree of freedom). It inherits
`Joint`'s `jointParameters` field. This field can be filled with a
`HingeJointParameters` only. If empty,  `HingeJointParameters` default values
apply.

### Field Summary

## HingeJointParameters

Derived from `JointParameters`.


```
HingeJointParameters {
  field SFVec3f anchor                    0 0 0 # for the rotation axis (m)
  # the following field have different default values than the parent class
  field SFVec3f axis                      1 0 0 # rotation axis
  field SFFloat suspensionSpringConstant  0     # linear spring constant along the suspension axis (Ns/m)
  field SFFloat suspensionDampingConstant 0     # linear damping constant along the suspension axis (Ns/m)
  field SFVec3f suspensionAxis            1 0 0 # direction of the suspension axis
}

```

### Description

The `HingeJointParameters` node can be used to specify the hinge rotation axis
and various joint parameters (e.g., angular position, stop angles, spring and
damping constants etc.) related to this rotation axis.

### Field Summary

The `suspensionSpringConstant` and `suspensionDampingConstant` fields can be
used to add a linear spring and/or damping behavior *along* the axis defined in
`suspensionAxis`. These fields are described in more detail in
`JointParameters`'s Springs and Dampers" section.

## Hinge2Joint

Derived from `HingeJoint`.


```
Hinge2Joint {
  field SFNode jointParameters2 NULL # JointParameters for second axis
  field MFNode device2 [ ] # RotationalMotor, PositionSensor and Brake
  hiddenField SFFloat position2  0 # initial position with respect to the second hinge (rad)
}
```

### Description

The `Hinge2Joint` node can be used to model a hinge2 joint, i.e. a joint
allowing only rotational motions around two intersecting axes (2 degrees of
freedom). These axes cross at the `anchor` point and need not to be
perpendicular. The suspension fields defined in a `HingeJointParameters` node
allow for spring and damping effects along the suspension axis.

Note that a universal joint boils down to a hinge2 joint with orthogonal axes
and (default) zero suspension.

Typically, `Hinge2Joint` can be used to model a steering wheel with suspension
for a car, a shoulder or a hip for a humanoid robot.

### Field Summary

## ImageTexture


```
ImageTexture {
  MFString   url       []
  SFBool     repeatS   TRUE
  SFBool     repeatT   TRUE
  SFBool     filtering TRUE
}
```

### Description

The `ImageTexture` node defines a texture map by specifying an image file and
general parameters for mapping to geometry. Texture maps are defined in a 2D
coordinate system *(s,t)* that ranges from 0.0 to 1.0 in both directions. The
bottom edge of the image corresponds to the *s*-axis of the texture map, and
left edge of the image corresponds to the *t*-axis of the texture map. The
lower-left pixel of the image corresponds to *s=0, t=0*, and the top-right pixel
of the image corresponds to *s=1, t=1*. These relationships are depicted below.

![Texture map coordinate system](png/image_texture.png)
**Texture map coordinate system**

The texture is read from the file specified by the `url` field. The file should
be specified with a relative path (cf. ). Absolute paths work as well, but they
are not recommended because they are not portable across different systems.
Ideally, the texture file should lie next to the world file, possibly inside a
"textures" subfolder. Supported image formats include both JPEG and PNG. The
rendering of the PNG alpha transparency is supported. It is slightly more
efficient to use textures with power of 2 resolution (e.g. 8x8, 2048x64, etc.).
Otherwise an internal upscaling is performed.

A PNG image may contain an alpha channel. If such an alpha channel exists, the
texture becomes semi-transparent. This is useful to render for example a scissor
cut texture. Semi-transparent objects are sorted according to their center (the
local position of the parent Transform) and are rendered in the same rendering
queue as the objects having a transparent material (see the `transparency` field
of the `Material` node). Semi-transparent objects cannot receive and cannot cast
shadows.

If the image contains an alpha channel no texture filtering is performed,
otherwise both a trilinear interpolation and an anisotropic texture filtering is
applied (the texture is subsampled according to the distance and the angle
between the textured polygon and the camera).

The `repeatS` and `repeatT` fields specify how the texture wraps in the *s* and
*t* directions. If `repeatS` is `TRUE` (the default), the texture map is
repeated outside the [0.0,1.0] texture coordinate range in the *s* direction so
that it fills the shape. If `repeatS` is `FALSE`, the texture coordinates are
clamped in the *s* direction to lie within the [0.0,1.0] range. The `repeatT`
field is analogous to the `repeatS` field.

The `filtering` field defines whether the texture will be displayed using a
texture filtering or not. No filtering corresponds to a simple nearest-neighbor
pixel interpolation filtering method. Filtering corresponds to both an
anisotropic filtering method (using mipmapping) which chooses the smallest
mipmap according to the texture orientation and to the texture distance, and a
trilinear filtering method which smooths the texture. Using filtering doesn't
affect significantly the run-time performance, however it may increase slightly
the initialization time because of the generation of the mipmaps.

### Search rule of the texture path

The texture path is searched from the corresponding `url` element according to
the following rule:


```

i = current_url_index
generic_textures_path = "$WEBOTS_MODULES_PATH/projects/default/worlds"
if is_absolute(url[i]) then
  if is_existing(url[i])
    return url[i]
  else
    return Error
else
  if defined_in_a_PROTO(current_node) and is_existing(PROTO_path + url[i])
    return PROTO_path + url[i]
  else if is_existing(world_path + url[i])
    return world_path + url[i]
  else if is_existing(generic_textures_path + url[i])
    return generic_textures_path + url[i]
  endif
endif
return Error
  
```

## ImmersionProperties


```
ImmersionProperties {
  field SFString   fluidName       ""
  field SFString   referenceArea   "immersed area"
  field SFVec3f    dragForceCoefficients  0 0 0 # dimensionless coefficient ranging in [0, infinity)
  field SFVec3f    dragTorqueCoefficients  0 0 0 # dimensionless coefficients ranging in [0, infinity)
  field SFFloat    viscousResistanceForceCoefficient  0 # (Ns/m) ranges in [0, infinity)
  field SFFloat    viscousResistanceTorqueCoefficient  0 # (Nm/s ) ranges in [0, infinity)
}
```

### Description

An `ImmersionProperties` node is used inside the `immersionProperties` field of
a `Solid` node to specify its dynamical interactions with one or more `Fluid`
nodes.

### ImmersionProperties Fields

## IndexedFaceSet


```
IndexedFaceSet {
  SFNode    coord           NULL
  SFNode    texCoord        NULL
  SFBool    solid           TRUE  # ignored and regarded as TRUE
  SFBool    ccw             TRUE
  SFBool    convex          TRUE
  MFInt32   coordIndex      []    # [-1,inf)
  MFInt32   texCoordIndex   []    # [-1,inf)
  SFFloat   creaseAngle     0     # [0,inf)
}
```

### Description

The `IndexedFaceSet` node represents a 3D shape formed by constructing faces
(polygons) from vertices listed in the `coord` field. The `IndexedFaceSet` node
can be used either as a graphical or as a collision detection primitive (in a
boundingObject). `IndexedFaceSet` nodes can be easily imported from 3D modeling
programs after a triangle mesh conversion.

### Field Summary

The `coord` field contains a `Coordinate` node that defines the 3D vertices
referenced by the `coordIndex` field. `IndexedFaceSet` uses the indices in its
`coordIndex` field to specify the polygonal faces by indexing into the
coordinates in the `Coordinate` node. An index of "-1" indicates that the
current face has ended and the next one begins. The last face may be (but does
not have to be) followed by a "-1" index. If the greatest index in the
`coordIndex` field is N, the `Coordinate` node shall contain N+1 coordinates
(indexed as 0 to N). Each face of the `IndexedFaceSet` shall have:

Otherwise, the results are undefined.

When used for collision detection (boundingObject), each face of the
`IndexedFaceSet` must contain exactly three vertices, hence defining a triangle
mesh (or trimesh).

If the `texCoord` field is not NULL, then it must contain a `TextureCoordinate`
node. The texture coordinates in that node are applied to the vertices of the
`IndexedFaceSet` as follows:

If the `texCoordIndex` field is not empty, then it is used to choose texture
coordinates for each vertex of the `IndexedFaceSet` in exactly the same manner
that the `coordIndex` field is used to choose coordinates for each vertex from
the `Coordinate` node. The `texCoordIndex` field must contain at least as many
indices as the `coordIndex` field, and must contain end-of-face markers (-1) in
exactly the same places as the `coordIndex` field. If the greatest index in the
`texCoordIndex` field is N, then there must be N+1 texture coordinates in the
`TextureCoordinate` node.

The `creaseAngle` field, affects how default normals are generated. For example,
when an `IndexedFaceSet` has to generate default normals, it uses the
`creaseAngle` field to determine which edges should be smoothly shaded and which
ones should have a sharp crease. The crease angle is the positive angle between
surface normals on adjacent polygons. For example, a crease angle of .5 radians
means that an edge between two adjacent polygonal faces will be smooth shaded if
the normals to the two faces form an angle that is less than .5 radians (about
30 degrees). Otherwise, it will be faceted. Crease angles must be greater than
or equal to 0.0.

### Example


```
IndexedFaceSet {
  coord Coordinate {
    point [ 1 0 -1, -1 0 -1, -1 0 1, 1 0 1, 0 2 0 ]
  }
  coordIndex [ 0 4 3 -1   # face A, right
               1 4 0 -1   # face B, back
               2 4 1 -1   # face C, left
               3 4 2 -1   # face D, front
               0 3 2  1 ] # face E, bottom
}
```

![A simple IndexedFaceSet example](png/indexed_face_set.png)
**A simple IndexedFaceSet example**

## IndexedLineSet


```
IndexedLineSet {
  SFNode    coord        NULL
  MFInt32   coordIndex   []    # [-1,inf)
}
```

The `IndexedLineSet` node represents a 3D geometry formed by constructing
polylines from 3D vertices specified in the `coord` field. `IndexedLineSet` uses
the indices in its `coordIndex` field to specify the polylines by connecting
vertices from the `coord` field. An index of "-1" indicates that the current
polyline has ended and the next one begins. The last polyline may be (but does
not have to be) followed by a "-1". `IndexedLineSet` is specified in the local
coordinate system and is affected by the transformations of its ancestors.

The `coord` field specifies the 3D vertices of the line set and contains a
`Coordinate` node.

`IndexedLineSet`s are not lit, are not texture-mapped and they do not cast or
receive shadows. `IndexedLineSet`s cannot be use for collision detection
(boundingObject).

## InertialUnit

Derived from `Device`.


```
InertialUnit {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute roll
  SFBool     zAxis          TRUE  # compute pitch
  SFBool     yAxis          TRUE  # compute yaw
  SFFloat    resolution     -1
}
```

### Description

The `InertialUnit` node simulates an *Inertial Measurement Unit* (IMU). The
`InertialUnit` computes and returns its *roll*, *pitch* and *yaw* angles with
respect to a global coordinate system defined in the `WorldInfo` node. If you
would like to measure an acceleration or an angular velocity, please use the
`Accelerometer` or `Gyro` node instead. The `InertialUnit` node must be placed
on the `Robot` so that its *x*-axis points in the direction of the `Robot`'s
forward motion (longitudinal axis). The positive *z*-axis must point towards the
`Robot`'s right side, e.g., right arm, right wing (lateral axis). The positive
*y*-axis must point to the `Robot`'s up/top direction. If the `InertialUnit` has
this orientation, then the *roll*, *pitch* and *yaw* angles correspond to the
usual automotive, aeronautics or spatial meaning.  More precisely, the
`InertialUnit` measures the Tait-Bryan angles along *x*-axis (roll), *z*-axis
(pitch) and *y*-axis (yaw). This convention is commonly referred to as the
*x-z-y* extrinsic sequence; it corresponds to the composition of elemental
rotations denoted by YZX. The reference frame is made of the unit vector giving
the north direction, the opposite of the normalized gravity vector and their
cross-product (see `WorldInfo` to customize this frame).

### Field Summary

### InertialUnit Functions

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

## JointParameters


```
JointParameters {
  field SFFloat position        0 # current position (m or rad)
  field SFVec3f axis        0 0 1 # displacement axis (m)
  field SFFloat minStop         0 # low stop position (m or rad)
  field SFFloat maxStop         0 # high stop position (m or rad)
  field SFFloat springConstant  0 # spring constant (N/m or Nm)
  field SFFloat dampingConstant 0 # damping constant (Ns/m or Nms) 
  field SFFloat staticFriction  0 # friction constant (Ns/m or Nms)
}

```

### Description

The `JointParameters` node is a concrete base node used to specify various joint
parameters related to an axis along which, or around which, the motion is
allowed. As an instantiated node it can be used within the jointParameters field
of `SliderJoint` or within the jointParameters2 field of `Hinge2Joint`. Unlike
the other joint parameters node, it has no anchor.

### Field Summary

### Units

Rotational joint units (`HingeJoint`, `Hinge2Joint`) are expressed in *radians*
while linear joint units (`SliderJoint`) are expressed in *meters*. See :

### Initial Transformation and Position

![HingeJoint](pdf/hinge_joint.pdf)
**HingeJoint**

![SliderJoint](pdf/slider_joint.pdf)
**SliderJoint**

The `position` field is a scalar representing an angle (in radians) or a
distance (in meters) computed with respect to the initial `translation` and
`rotation` of the `Joint`'s `Solid` child. If its value is zero, then the
`Joint`'s child is *by definition* set with its initial `translation` and
`rotation`. For a joint with one or two rotational degrees of freedom (e.g.,
`HingeJoint`, `Hinge2Joint`), the `position` field value is the rotation angle
around one the joint axes that was applied to the `Joint`'s child initially in
zero position. For a slider joint, `position` is the translation length along
the sliding axis that was applied to the `Joint`'s child initially in zero
position.

For example if we have a `HingeJoint` and a `position` field value of 1.5708,
this means that this `HingeJoint` is 90 degrees from its initial rotation with
respect to the hinge rotation axis. The values passed to the
`wb_motor_set_position()` function are specified with respect to the zero
position. The values of the `minStop` and `maxStop` fields are also defined with
respect to the zero position.

### Joint Limits

The `minStop` and `maxStop` fields define the *hard limits* of the joint. Hard
limits represent physical (or mechanical) bounds that cannot be overrun by any
force; they are defined with respect to the joint `position`. Hard limits can be
used, for example, to simulate both end caps of a hydraulic or pneumatic piston
or to restrict the range of rotation of a hinge. When used for a rotational
motion the value of `minStop` must be in the range [-pi, 0] and `maxStop` must
be in the range [0, pi]. When both `minStop` and `maxStop` are zero (the
default), the hard limits are deactivated. The joint hard limits use ODE joint
stops (for more information see the ODE documentation on `dParamLoStop` and
`dParamHiStop`).

Finally, note that when both soft (`minPosition` and `maxPosition`, see the
`Motor`'s "Motor Limits" section) and hard limits (`minStop` and `maxStop`) are
activated, the range of the soft limits must be included in the range of the
hard limits, such that `minStop lt= minValue` and `maxStopgt= maxValue`.

### Springs and Dampers

The `springConstant` field specifies the value of the spring constant (or spring
stiffness), usually denoted as `K`. The `springConstant` must be positive or
zero. If the `springConstant` is zero (the default), no spring torque/force will
be applied to the joint. If the `springConstant` is greater than zero, then a
spring force will be computed and applied to the joint in addition to the other
forces (i.e., motor force, damping force). The spring force is calculated
according to Hooke's law: `F = -Kx`, where `K` is the `springConstant` and `x`
is the current joint position as represented by the `position` field. Therefore,
the spring force is computed so as to be proportional to the current joint
position, and to move the joint back to its initial position. When designing a
robot model that uses springs, it is important to remember that the spring's
resting position for each joint will correspond to the initial position of the
joint. The only expection arise when the closest upper `Solid` of the `Joint` is
passive, i.e. the `physics` field is not defined. In this case the spring force
direction is inverted.

The `dampingConstant` field specifies the value of the joint damping constant.
The value of `dampingConstant` must be positive or zero. If `dampingConstant` is
zero (the default), no damping torque/force will be added to the joint. If
`dampingConstant` is greater than zero, a damping torque/force will be applied
to the joint in addition to the other forces (i.e., motor force, spring force).
This damping torque/force is proportional to the effective joint velocity: `F =
-Bv`, where `B` is the damping constant, and `v = dx/dt` is the effective joint
velocity computed by the physics simulator.

![Mechanical Diagram of a Slider Joint](pdf/slider_joint_mechanics.pdf)
**Mechanical Diagram of a Slider Joint**

As you can see in (see  ), a `Joint` creates a joint between two masses `m` and
`m`. The mass `m` is defined by the `Physics` node in the closest upper `Solid`
of the `Joint`. The mass `m` is defined by the `Physics` node of the `Solid`
placed into the `endPoint` of the `Joint`. The value `x` corresponds to the
anchor position of the `Joint` defined in the `anchor` field of a
`JointParameters` node. The position `x` corresponds to the current position of
the `Joint` defined in the `position` field of a `JointParameters` node.

## LED

Derived from `Device`.


```
LED {
  MFColor   color   [ 1 0 0 ]  # [0,1]
  SFBool    gradual FALSE      # for gradual color display and RBG LEDs
}
```

### Description

The `LED` node is used to model a light emitting diode (LED). The light produced
by an LED can be used for debugging or informational purposes. The resulted
color is applied only on the first child of the `LED` node. If the first child
is a `Shape` node, the `emissiveColor` field of its `Material` node is altered.
If the first child is a `Light` node, its `color` field is altered. Otherwise,
if the first child is a `Group` node, a recursive search is applied on this node
in order to find which color field must be modified, so every `Light`, `Shape`
and `Group` node is altered according to the previous rules.

### Field Summary

### LED Functions

## Light


```
Light {
  SFFloat   ambientIntensity   0        # [0,1]
  SFColor   color              1 1 1    # [0,1]
  SFFloat   intensity          1        # [0,1]
  SFBool    on                 TRUE
  SFBool    castShadows        FALSE
}
```

Direct derived nodes: `PointLight`, `SpotLight`, `DirectionalLight`.

### Description

The `Light` node is abstract: only derived nodes can be instantiated. Lights
have two purposes in Webots: (1) the are used to graphically illuminate objects
and (2) they determine the quantity of light perceived by `LightSensor` nodes.
Except for `castShadows`, every field of a `Light` node affects the light
measurements made by `LightSensor` nodes.

### Field Summary

## LightSensor

Derived from `Device`.


```
LightSensor {
  MFVec3f     lookupTable   [ 0 0 0, 1 1000 0 ]
  SFColor     colorFilter   1 1 1    # [0,1]
  SFBool      occlusion     FALSE
  SFFloat     resolution    -1
}
```

### Description

`LightSensor` nodes are used to model photo-transistors, photo-diodes or any
type of device that measures the irradiance of light in a given direction.
*Irradiance* represents the radiant power incident on a surface in Watts per
square meter (W/m^2), and is sometimes called *intensity*. The simulated
irradiance is computed by adding the irradiance contributed by every light
source (`DirectionalLight`, `SpotLight` and `PointLight`) in the world. Then the
total irradiance is multiplied by a color filter and fed into a lookup table
that returns the corresponding user-defined value.

The irradiance contribution of each light source is divided into *direct* and
*ambient* contributions. The direct contribution depends on the `position` and
the `orientation` of the sensor, the `location` and the `direction` of the light
sources and (optionally) on the possible occlusion of the light sources. The
ambient contribution ignores the possible occlusions, and it is not affected by
the `orientation` of the sensor nor by the `direction` of a light source. The
direct and ambient contributions of `PointLight`s and `SpotLight`s are
attenuated according to the distance between the sensor and the light, according
to specified attenuation coefficients. The light radiated by a
`DirectionalLight` is not attenuated. See also `DirectionalLight`, `SpotLight`
and `PointLight` node descriptions.

Note that the Webots lighting model does not take reflected light nor object
colors into account.

### Field Summary

Before being interpolated by the `lookupTable`, the total irradiance `E` [W/m^2]
seen by a sensor is computed according to the equation shown in :

![Light sensor irradiance formula](pdf/light_intensity.pdf)
**Light sensor irradiance formula**

The `F` vector corresponds to the sensor's `colorFilter` field, `n` is the total
number of lights in the simulation, `on[i]` corresponds to the `on` field of
light `i` (TRUE=1, FALSE=0), the `C[i]` vector is the `color` field of light
`i`, and `I` is the `ambientIntensity` field of light `i`.  The value `att[i]`
is the attenuation of light `i`, and is calculated as shown in .

![Light attenuation](pdf/light_attenuation.pdf)
**Light attenuation**

Variables `a` and `a` correspond to the `attenuation` field of light `i`, and
`d` is the distance between the sensor and the light. There is no attenuation
for `DirectionalLight`s. `I` is the direct irradiance contributed by light `i`,
and is calculated as shown in .

![Direct irradiance](pdf/direct_light.pdf)
**Direct irradiance**

Finally, `spot[i]` is a factor used only in case of a `SpotLight`, and that
depends on its `cutOffAngle` and `beamWidth` fields, and is calculated as shown
in , where the `alpha` angle corresponds to the angle between `-L` and the
`direction` vector of the `SpotLight`.

![SpotLight factor](pdf/spot_light.pdf)
**SpotLight factor**

The value `I[i]` corresponds to the *intensity* field of light `i`, and `N` is
the normal axis (*x*-axis) of the sensor (see ). In the case of a `PointLight`,
`L` is the sensor-to-light-source vector. In the case of a `DirectionalLight`,
`L` corresponds to the negative of the light's `direction` field. The *
operation is a modified dot product: if dot lt 0, then 0, otherwise, dot
product. Hence, each light source contributes to the irradiance of a sensor
according to the cosine of the angle between the `N` and the `L` vectors, as
shown in the figure. The contribution is zero if the light source is located
behind the sensor. This is derived from the physical fact that a photo-sensitive
device is usually built as a surface of semiconductor material and therefore,
the closer the angle of incidence is to perpendicular, the more photons will
actually hit the surface and excite the device. When a light source is parallel
to (or behind) the semiconductor surface, no photons actually reach the surface.

![The irradiance (E) depends on the angle (phi) between the ](pdf/light_sensor.pdf)
**The irradiance (E) depends on the angle (phi) between the **

The "occlusion" condition is true if the light source is hidden by one or more
obstacles. More precisely, "occlusion" is true if (1) the `occlusion` field of
the sensor is set to TRUE and (2) there is an obstacle in the line of sight
between the sensor and the light source. Note that `DirectionalLight` nodes
don't have *location* fields; in this case Webots checks for obstacles between
the sensor and an imaginary point located 1000m away in the direction opposite
to the one indicated by the `direction` field of this `DirectionalLight`.

Like any other type of collision detection in Webots, the `LightSensor`
occlusion detection is based on the `boundingObjects` of `Solid` nodes (or
derived nodes). Therefore, even if it has a visible geometric structure, a
`Solid` node cannot produce any occlusion if its `boundingObject` is not
specified.

### LightSensor Functions

## LinearMotor

Derived from `Motor`.


```
LinearMotor {
  field SFString name       "linear motor" # used by wb_robot_get_device()
  field SFFloat  maxForce   10             # max force (N) : [0, inf)
}
```

### Description

A `LinearMotor` node can be used to power a `SliderJoint` and a `Track`.

### Field Summary

## Material


```
Material {
  SFFloat   ambientIntensity   0.2          # [0,1]
  SFColor   diffuseColor       0.8 0.8 0.8  # [0,1]
  SFColor   emissiveColor      0 0 0        # [0,1]
  SFFloat   shininess          0.2          # [0,1]
  SFColor   specularColor      0 0 0        # [0,1]
  SFFloat   transparency       0            # [0,1]
}
```

### Description

The `Material` node specifies surface material properties for associated
geometry nodes and is used by the VRML97 lighting equations during rendering.
The fields in the `Material` node determine how light reflects off an object to
create color.

### Field Summary

## Motor

Derived from `Device`.


```
Motor {
  SFFloat maxVelocity  10 # (m/s or rad/s): (0,inf)
  SFVec3f controlPID   10 0 0 # PID gains: (0,inf), [0, inf), [0, inf)
  SFFloat acceleration -1 # (m/s^2 or rad/s^2): -1 or (0,inf)
  SFFloat minPosition  0  # (m or rad): (-inf,inf) or [-pi, pi]
  SFFloat maxPosition  0  # (m or rad): (-inf,inf) or [-pi, pi]
}
```

### Description

A `Motor` node is an abstract node (not instantiated) whose derived classes can
be used in a mechanical simulation to power a joint hence producing a motion
along, or around, one of its axes.

A `RotationalMotor` can power a `HingeJoint` (resp. a `Hinge2Joint`) when set
inside the `device` (resp. `device` or `device2`) field of these nodes. It
produces then a rotational motion around the choosen axis. Likewise, a
`LinearMotor` can power a `SliderJoint`, producing a sliding motion along its
axis.

### Field Summary

### Units

By *motor position*, we mean joint position as defined in `JointParameters`.
Rotational motors units are expressed in *radians* while linear motors units are
expressed in *meters*. See :

### Initial Transformation and Position

The `minPosition` and `maxPosition` are defined with respect to joint's zero
position (see description of the `position` field in `JointParameters`).

![Linear Motor](pdf/linear_motor.pdf)
**Linear Motor**

![Rotational Motor](pdf/rotational_motor.pdf)
**Rotational Motor**

### Position Control

The standard way of operating a `Motor` is to control the position directly
(*position control*). The user specifies a target position using the
`wb_motor_set_position()` function, then the P-controller takes into account the
desired velocity, acceleration and motor force in order to move the motor to the
target position. See .

In Webots, position control is carried out in three stages, as depicted in . The
first stage is performed by the user-specified controller (1) that decides which
position, velocity, acceleration and motor force must be used. The second stage
is performed by the motor P-controller (2) that computes the current velocity of
the motor `V`. Finally, the third stage (3) is carried out by the physics
simulator (ODE joint motors).

![Motor control](pdf/motor_control.pdf)
**Motor control**

At each simulation step, the PID-controller (2) recomputes the current velocity
*Vc* according to following algorithm: `error = Pt - Pc; error_integral += error
* ts; error_derivative = (previous_error - error) / ts; Vc = P * error + D *
error_derivative + I * error_integral ; if (abs(Vc) > Vd) Vc = sign(Vc) * Vd; if
(A != -1) { a = (Vc - Vp) / ts; if (abs(a) > A) a = sign(a) * A; Vc = Vp + a *
ts; }` where  `V` is the current motor velocity in rad/s or m/s, `P, I` and `D`
are the PID-control gains specified in the `controlPID` field, or set with
`wb_motor_set_control_pid()`, `P` is the *target position* of the motor set by
the function `wb_motor_set_position()`, `P` is the current motor position as
reflected by the `position` field, `V` is the desired velocity as specified by
the `maxVelocity` field (default) or set with `wb_motor_set_velocity()`, `a` is
the acceleration required to reach *Vc* in one time step, `V` is the motor
velocity of the previous time step, `t` is the duration of the simulation time
step as specified by the `basicTimeStep` field of the `WorldInfo` node
(converted in seconds), and `A` is the acceleration of the motor as specified by
the `acceleration` field (default) or set with `wb_motor_set_acceleration()`.

### Velocity Control

The motors can also be used with *velocity control* instead of *position
control*. This is obtained with two function calls: first the
`wb_motor_set_position()` function must be called with `INFINITY` as a position
parameter, then the desired velocity, which may be positive or negative, must be
specified by calling the `wb_motor_set_velocity()` function. This will initiate
a continuous motor motion at the desired speed, while taking into account the
specified acceleration and motor force. Example: `wb_motor_set_position(motor,
INFINITY); wb_motor_set_velocity(motor, 6.28);  // 1 rotation per second`
`INFINITY` is a C macro corresponding to the IEEE 754 floating point standard.
It is implemented in the C99 specifications as well as in C++. In Java, this
value is defined as `Double.POSITIVE_INFINITY`. In Python, you should use
`float('inf')`. Finally, in Matlab you should use the `inf` constant.

### Force and Torque Control

The position (resp. velocity) control described above are performed by the
Webots PID-controller and ODE's joint motor implementation (see ODE
documentation). As an alternative, Webots does also allow the user to directly
specify the amount of force (resp. torque) that must be applied by a `Motor`.
This is achieved with the `wb_motor_set_force()` (resp. `wb_motor_set_torque()`)
function which specifies the desired amount of forces (resp. torques) and
switches off the PID-controller and motor force (resp. motor torque). A
subsequent call to `wb_motor_set_position()` restores the original *position
control*. Some care must be taken when using *force control*. Indeed the force
(resp. torque) specified with `wb_motor_set_force()` (resp.
`wb_motor_set_torque()`) is applied to the `Motor` continuously. Hence the
`Motor` will infinitely accelerate its rotational or linear motion and
eventually *explode* unless a functional force control (resp. torque control)
algorithm is used.

### Motor Limits

The `minPosition` and `maxPosition` fields define the *soft limits* of the
motor. Motor zero position and joint zero position coincide (see description of
the `position` field in `JointParameters`). Soft limits specify the *software*
boundaries beyond which the PID-controller will not attempt to move. If the
controller calls `wb_motor_set_position()` with a target position that exceeds
the soft limits, the desired target position will be clipped in order to fit
into the soft limit range. Valid limits values depends on the motor position,
i.e. `minPosition` must always be less than or equal to the motor position and
`maxPosition` must always be greater than or equal to the motor position. When
both `minPosition` and `maxPosition` are zero (the default), the soft limits are
deactivated. Note that the soft limits can be overstepped when an external force
which exceeds the motor force is applied to the motor. For example, it is
possible that the weight of a robot exceeds the motor force that is required to
hold it up.

Finally, note that when both soft (`minPosition` and `maxPosition`) and hard
limits (`minStop` and `maxStop`, see `JointParameters`) are activated, the range
of the soft limits must be included in the range of the hard limits, such that
`minStop lt= minValue` and `maxStopgt= maxValue`. Moreover a simulation
instability can appear if `position` is exactly equal to one of the bounds
defined by the `minStop` and `maxStop` fields at the simulation startup.
Warnings are displayed if theses rules are not respected.

### Motor Functions

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

## Physics


```
Physics {
  SFFloat     density             1000      # (kg/m^3) -1 or > 0
  SFFloat     mass                -1        # (kg) -1 or > 0
  SFVec3f     centerOfMass        0 0 0     # (-inf,inf)
  MFVec3f     inertiaMatrix       []        # empty or 2 values
  SFNode      damping             NULL      # optional damping node
}
```

### Description

The `Physics` node allows to specify parameters for the physics simulation
engine. `Physics` nodes are used in most Webots worlds with the exception of
some purely kinematics-based simulations. The `Physics` node specifies the mass,
the center of gravity and the mass distribution, thus allowing the physics
engine to create a *body* and compute realistic forces.

A `Physics` node can be placed in a `Solid` node (or any node derived from
`Solid`). The presence or absence of a `Physics` node in the `physics` field of
a `Solid` defines whether the `Solid` will have a *physics* or a *kinematic*
behavior.

### Field Summary

### How to use Physics nodes?

If it contains a `Physics` node, a `Solid` object will be simulated in *physics*
mode. The *physics* simulation mode takes into account the simulation of the
forces that act on the bodies and the properties of these bodies, e.g., mass and
moment of inertia. On the contrary, if its `physics` field is NULL, then the
`Solid` will be simulated in *kinematics* mode. The *kinematics* mode simulates
the objects motions without considering the forces that cause the motion. For
example in *kinematics* mode an object can reach the desired speed immediately
while in *physics* mode the inertial resistance will cause this object to
accelerate progressively. It is usually not necessary to specify all the
`Physics` nodes in a Webots world. Whether to use or not a `Physics` node in a
particular case depends on what aspect of the real world your want to model in
your simulation.

#### In passive objects

If a passive object should never move during a simulation then you should leave
its `physics` field empty. In this case no contact force will be simulated on
this object and hence it will never move. This is perfect for modeling walls or
the floor. Furthermore the floor should always be designed without `Physics`
node anyway, because otherwise it would fall under the action of gravity.

On the contrary, if a passive object needs to be pushed, kicked, dropped, etc.
then it should have a `Physics` node. So for example, if you want to design a
soccer game where the ball needs to be kicked and roll, then you will need to
add a `Physics` node to the ball. Similarly, in a box pushing or stacking
simulation, you will need to specify the `Physics` nodes for the boxes so that
the friction and gravity forces are applied to these objects.

#### In robots

Articulated robot, humanoids, vehicles and so on, are built as hierarchies of
`Solid` nodes (or subclasses of `Solid`). The contact and friction forces
generated by legs or wheels are usually a central aspect of the simulation of
robot locomotion. Similarly, the contact and friction forces of a grasping
robotic hand or gripper is crucial for the simulation of such devices. Therefore
the mechanical body parts of robots (eg., legs, wheels, arms, hands, etc) need
in general to have `Physics` nodes.

#### Implicit solid merging and joints

By `Solid` *child* of a given `Solid` node, we mean either a node directly
placed into the children list or a `Solid` node located into the `endPoint`
field of a `Joint` placed in the children list. We extend this definition to
nested `Group`s starting from the `Solid` children list and containing `Joint`s
or `Solid`s.

If a `Solid` child in the above sense is not related to its `Solid` parent by a
joint while both have a `Physics` node, they are *merged at the physics engine
level*: ODE will be given only one body to represent both parent and child. This
process is recursive and stops at the highest ancestor which have a joint
pointing to an upper `Solid` or just before the highest ancestor without
`Physics` node. This way modelling a rigid assembly of `Solid`s won't hurt
physics simulation speed even if it aggregates numerous components.

When designing the robot tree structure, there is one important rule to remember
about the `Physics` nodes: *If a Solid node has a parent and a child with a
Physics node then it must also have a Physics node* (1). A consequence of this
rule is that, in a robot tree structure, only leaf nodes and nodes included in
the *static basis* (see first `note` above) can have a NULL `physics` field. In
addition top nodes (`Robot`, `DifferentialWheels` or `Supervisor`) do usually
have `Physics` because this is required to allow any of their children to use
the *physics* simulation.

Note that each `Physics` node adds a significant complexity to the world: as a
consequence the simulation speed decreases. Therefore the number of `Physics`
nodes should be kept as low as possible. Fortunately, even with a complex
wheeled or articulated robot some of the `physics` fields can remain empty
(NULL). This is better explained with an example. Let's assume that you want to
design an articulated robot with two legs. Your robot model may look like this
(very simplified): `Robot { ... children [ DEF LEG1_HINGE HingeJoint  { ...
endPoint DEF LEG1 Solid { physics Physics { } } } DEF LEG2_HINGE HingeJoint {
... endPoint DEF LEG2 Solid { physics Physics { } } } ] physics Physics { } }`
The legs need `Physics` nodes because the forces generated by their contact with
the floor will allow the robot to move. If you would leave the legs without
`Physics`, then no contact forces would be generated and therefore the robot
would not move. Now, according to rule (1), because the legs have `Physics`
nodes, their parent (the `Robot` node) must also have a `Physics` node. If the
`Physics` node of the `Robot` was missing, the simulation would not work, the
legs would fall off, etc.

Now suppose you would like to add a `Camera` to this robot. Let's also assume
that the physical properties of this camera are not relevant for this
simulation, say, because the mass of the camera is quite small and because we
want to ignore potential collisions of the camera with other objects. In this
case, you should leave the `physics` field of the camera empty. So the model
with the camera would look like this: `Robot { ... children [ DEF CAM Camera {
... } DEF LEG1_HINGE HingeJoint  { ... endPoint DEF LEG1 Solid { ... physics
Physics { } } } DEF LEG2_HINGE HingeJoint { ... endPoint DEF LEG2 Solid {
physics Physics { } } } ] physics Physics { } }` Now suppose that the camera
needs to be motorized, e.g., it should rotate horizontally. Then the camera must
simply be placed in the `endPoint` field of `HingeJoint` node that controls its
horizontal position. This time again, the physical properties of the camera
motor are apparently unimportant. If we assume that the mass of the camera motor
is small and that its inertia is not relevant, then the camera `Physics` node
can also be omitted: `Robot { ... children [ DEF CAMERA_HINGE HingeJoint { ...
device DEF CAM_MOTOR RotationalMotor { ... } endPoint DEF CAM Camera { ... } }
DEF LEG1_HINGE HingeJoint  { ... endPoint DEF LEG1 Solid { ... physics Physics {
} } } DEF LEG2_HINGE HingeJoint { ... endPoint DEF LEG2 Solid { physics Physics
{ } } } ] physics Physics { } }`

#### Devices


Most device nodes work without `Physics` node. But a `Physics` node can
optionally be used if one wishes to simulate the weight and inertia of the
device. So it is usually recommended to leave the `physics` field of a device
empty, unless it represents a significant mass or volume in the simulated robot.
This is true for these devices: `Accelerometer`, `Camera`, `Compass`,
`DistanceSensor`, `Emitter`, `GPS`, `LED`, `LightSensor`, `Pen`, and `Receiver`.

## Plane


```
Plane {
  SFVec2f     size        1 1     # (-inf,inf)
}
```

### Description

The `Plane` node defines a plane in 3D-space. The plane's normal vector is the
*y*-axis of the local coordinate system. The plane can be used as graphical
object or as collision detection object.

When a plane is used as graphical object, the `size` field specifies the
dimensions of the graphical representation. Just like the other graphical
primitives, it is possible to apply a `Material` (e.g., a texture) to a plane.

When a plane is used as collision detection object (in a `boundingObject`) then
the `size` field is ignored and the plane is considered to be infinite. The
`Plane` node is the ideal primitive to simulate, e.g., the floor or infinitely
high walls. Unlike the other collision detection primitives, the `Plane` can
only be used in static objects (a static object is an object without a `Physics`
node). Note that Webots ignores collision between planes, so planes can safely
cut each other. Note that a `Plane` node is in fact not really a plane: it's a
half-space. Anything that is moving inside the half-space will be ejected out of
it. This means that planes are only planes from the perspective of one side. If
you want your plane to be reversed, rotate it by pi using a `Transform` node.

## PointLight

Derived from `Light`.


```
PointLight {
  SFVec3f   attenuation   1 0 0    # [0,inf)
  SFVec3f   location      0 0 0    # (-inf,inf)
  SFFloat   radius        100      # [0,inf)
}
```

### Description

The `PointLight` node specifies a point light source at a 3D location in the
local coordinate system. A point light source emits light equally in all
directions. It is possible to put a `PointLight` on board a mobile robot to have
the light move with the robot.

A `PointLight` node's illumination drops off with distance as specified by three
`attenuation` coefficients. The final attenuation factor is calculated as
follows: *att = 1/(attenuation[0] + attenuation[1] * r + attenuation[2] * r^2)*,
where *r* is the distance from the light to the surface being illuminated. The
default is no attenuation. When `PointLight` nodes are used together with
`LightSensor`, it is recommended to change the default attenuation to a more
realistic [*0 0 4*pi*] in order to more accurately model physical reality.
Indeed, if a point source radiates light uniformly in all directions and there
is no absorption, then the irradiance drops off in proportion to the square of
the distance from the surface.

Contrary to the VRML specifications, the `attenuation` and the
`ambientIntensity` fields cannot be set simultaneously.

## PositionSensor

Derived from `Device`.


```
PositionSensor {
  SFFloat resolution  -1
}
```

### Description

A `PositionSensor` node can be used in a mechanical simulation to monitor a
joint position. The position sensor can be inserted in the `device` field of a
`HingeJoint`, a `Hinge2Joint`, a `SliderJoint`, or a `Track`. Depending on the
`Joint` type, it will measure the angular position in radians or the linear
position in meters.

### Field Summary

### PositionSensor Functions

## Propeller


```
Propeller {
  field SFVec3f shaftAxis       1 0 0 # (m)
  field SFVec3f centerOfThrust  0 0 0 # (m)
  field SFVec2f thrustConstants 1 0   # Ns^2/rad : (-inf, inf), Ns^2/(m*rad) : (-inf, inf)
  field SFVec2f torqueConstants 1 0   # Nms^2/rad : (-inf, inf), Ns^2/rad : (-inf, inf)
  field SFNode device NULL            # RotationalMotor
  field SFNode fastHelix NULL         # Solid node containing a graphical representation for rotation speed gt 24 pi rad/s (720 rpm)
  field SFNode slowHelix NULL         # Solid node containing a graphical representation for rotation speed lt= 24 pi rad/s
}
```

### Description

![Propeller](pdf/propeller.pdf)
**Propeller**

The `Propeller` node can be used to model a marine or an aircraft propeller.
When its `device` field is set with a `RotationalMotor`, the propeller turns the
motor angular velocity into a thrust and a (resistant) torque. The resultant
thrust is the product of a real number T by the unit length shaft axis vector
defined in the `shaftAxis` field, with T given by the formula  `T = t1 * |omega|
* omega - t2 * |omega| * V`  and where t1 and t2 are the constants specified in
the `thrustConstants` field, omega is the motor angular velocity and V is the
component of the linear velocity of the center of thrust along the shaft axis.
The thrust is applied at the point specified within the `centerOfThrust` field.
The resultant torque is the product of a real number Q by the unit length shaft
axis vector, with Q given by the formula  `Q = q1 * |omega| * omega - q2 *
|omega| * V` and where q1 and q2 are the constants specified in the
`torqueConstants` field.

The above formulae are based on "Guidance and Control of Ocean Vehicles" from
Thor I. Fossen and "Helicopter Performance, Stability, and Control" from Raymond
W. Prouty.

The example "propeller.wbt" located in the "projects/samples/devices/worlds"
directory of Webots shows three different helicopters modeled with `Propeller`
nodes.

### Field Summary

## Receiver

Derived from `Device`.


```
Receiver {
  SFString  type                "radio"  # or "serial" or "infra-red"
  SFFloat   aperture            -1       # -1 or [0,2pi]
  SFInt32   channel             0        # [-1,inf)
  SFInt32   baudRate            -1       # -1 or [0,inf)
  SFInt32   byteSize            8        # [8,inf)
  SFInt32   bufferSize          -1       # -1 or [0,inf)
  SFFloat   signalStrengthNoise 0        # [0,inf)
  SFFloat   directionNoise      0        # [0,inf)
}
```

### Description

The `Receiver` node is used to model radio, serial or infra-red receivers. A
`Receiver` node must be added to the children of a robot or supervisor. Please
note that a `Receiver` can receive data but it cannot send it. In order to
achieve bidirectional communication, a robot needs to have both an `Emitter` and
a `Receiver` on board.

### Field Summary

### Receiver Functions

## Robot

Derived from `Solid`.


```
Robot {
  SFString   controller        "void"
  SFString   controllerArgs    ""
  SFString   data              ""
  SFBool     synchronization   TRUE
  MFFloat    battery           []
  SFFloat    cpuConsumption    0   # [0,inf)
  SFBool     selfCollision     FALSE
  SFBool     showRobotWindow   FALSE
  SFString   robotWindow       ""
  SFString   remoteControl     ""
}
```

Direct derived nodes: `DifferentialWheels`, `Supervisor`.

### Description

The `Robot` node can be used as basis for building a robot, e.g., an articulated
robot, a humanoid robot, a wheeled robot... If you want to build a two-wheels
robot with differential-drive you should also consider the `DifferentialWheels`
node. If you would like to build a robot with supervisor capabilities use the
`Supervisor` node instead (Webots PRO license required).

### Field Summary

### Synchronous versus Asynchronous controllers

The `synchronization` field specifies if a robot controller must be synchronized
with the simulator or not.

If `synchronization` is `TRUE` (the default), the simulator will wait for the
controller's `wb_robot_step()` whenever necessary to keep the simulation and the
controller synchronized. So for example if the simulation step
(`WorldInfo.basicTimeStep`) is 16 ms and the control step (`wb_robot_step()`) is
64 ms, then Webots will always execute precisely 4 simulation steps during one
control step. After the 4th simulation step, Webots will wait for the
controller's next control step (call to `wb_robot_step(64)`).

If `synchronization` is `FALSE`, the simulator will run as fast a possible
without waiting for the control step. So for example, with the same simulation
step (16 ms) and control step (64 ms) as before, if the simulator has finished
the 4th simulation step but the controller has not yet reached the call to
`wb_robot_step(64)`, then Webots will not wait; instead it will continue the
simulation using the latest actuation commands. Hence, if `synchronization` is
`FALSE`, the number of simulation steps that are executed during a control step
may vary; this will depend on the current simulator and controller speeds and on
the current CPU load, and hence the outcome of the simulation may also vary.
Note that if the number of simulation steps per control step varies, this will
appear as a variations of the "speed of the physics" in the controller's point
of view, and this will appear as a variation of the robot's reaction speed in
the user's point of view.

So generally the `synchronization` field should be set to `TRUE` when robust
control is required. For example if a motion (or ".motion file") was designed in
synchronous mode then it may appear completely different in asynchronous mode.
The asynchronous mode is currently used only for the robot competitions, because
in this case it is necessary to limit the CPU time allocated to each
participating controller. Note that it is also possible to combine synchronous
and asynchronous controllers, e.g., for the robot competitions generally the
`Supervisor` controller is synchronous while the contestants controllers are
asynchronous. Asynchronous controllers may also be recommended for networked
simulations involving several robots distributed over a computer network with an
unpredictable delay (like the Internet).

### Robot Functions

## RotationalMotor

Derived from `Motor`.


```
RotationalMotor {
  field SFString name         "rotational motor" # for wb_robot_get_device()
  field SFFloat  maxTorque   10                  # max torque (Nm) : [0, inf)
}
```

### Description

A `RotationalMotor` node can be used to power either a `HingeJoint` or a
`Hinge2Joint` to produce a rotational motion around the choosen axis.

### Field Summary

## Servo

Derived from `Device`.


```
Servo {
  SFString   type             "rotational"
  SFFloat    maxVelocity      10      # (0,inf)
  SFFloat    maxForce         10      # [0,inf)
  SFFloat    controlP         10      # (0,inf)
  SFFloat    acceleration     -1      # -1 or (0,inf)
  SFFloat    position         0
  SFFloat    minPosition      0       # (-inf,0]
  SFFloat    maxPosition      0       # [0,inf)
  SFFloat    minStop          0       # [-pi,0]
  SFFloat    maxStop          0       # [0,pi]
  SFFloat    springConstant   0       # [0,inf)
  SFFloat    dampingConstant  0       # [0,inf)
  SFFloat    staticFriction   0       # [0,inf)
}
```

### Description

A `Servo` node is used to add a joint (1 degree of freedom (DOF)) in a
mechanical simulation. The joint can be active or passive; it is placed between
the parent and children nodes (".wbt" hierarchy) of the `Servo` and therefore it
allows the children to move with respect to the parent. The `Servo` can be of
type "rotational" or "linear". A "rotational" `Servo` is used to simulate a
rotating motion, like an electric motor or a hinge. A "linear" `Servo` is used
to simulate a sliding motion, like a linear motor, a piston, a
hydraulic/pneumatic cylinder, a spring, or a damper.

### Field Summary

### Units

Rotational servos units are expressed in *radians* while linear servos units are
expressed in *meters*. See :

### Initial Transformation and Position

The `Servo` node inherits the `translation` and `rotation` fields from the
`Transform` node. These two fields represent the initial coordinate system
transformation between the `Servo` parent and children.

In a "rotational" `Servo`, these fields have the following meaning: The
`translation` field specifies the translation of the axis of rotation. The
`rotation` field specifies the orientation of the axis of rotation. See .

![Rotational servo](pdf/rotational_servo.pdf)
**Rotational servo**

In a "linear" `Servo`, these fields have the following meaning: The
`translation` field specifies the translation of the sliding axis. The
`rotation` field specifies the direction of the sliding axis. See .

![Linear servo](pdf/linear_servo.pdf)
**Linear servo**

The `position` field represents the current angle difference (in radians) or the
current distance (in meters) with respect to the initial `translation` and
`rotation` of the `Servo`. If `position` field is zero then the `Servo` is at
its initial `translation` and `rotation`. For example if we have a "rotational"
`Servo` and the value of the `position` field is 1.5708, this means that this
`Servo` is 90 degrees from its initial rotation. The values passed to the
`wb_servo_set_position()` function are specified with respect to the position
zero. The values of the `minPosition`, `maxPosition`, `minStop` and `maxStop`
fields are also defined with respect to the position zero.

### Position Control

The standard way of operating a `Servo` is to control the position directly
(*position control*). The user specifies a target position using the
`wb_servo_set_position()` function, then the P-controller takes into account the
desired velocity, acceleration and motor force in order to move the servo to the
target position. See .

In Webots, position control is carried out in three stages, as depicted in . The
first stage is performed by the user-specified controller (1) that decides which
position, velocity, acceleration and motor force must be used. The second stage
is performed by the servo P-controller (2) that computes the current velocity of
the servo `V`. Finally, the third stage (3) is carried out by the physics
simulator (ODE joint motors).

![Servo control](pdf/servo_control.pdf)
**Servo control**

At each simulation step, the P-controller (2) recomputes the current velocity
*Vc* according to the following algorithm: `Vc = P * (Pt - Pc); if (abs(Vc) >
Vd) Vc = sign(Vc) * Vd; if (A != -1) { a = (Vc - Vp) / ts; if (abs(a) > A) a =
sign(a) * A; Vc = Vp + a * ts; }` where  `V` is the current servo velocity in
rad/s or m/s, `P` is the P-control parameter specified in `controlP` field or
set with `wb_servo_set_control_p()`, `P` is the *target position* of the servo
set by the function `wb_servo_set_position()`, `P` is the current servo position
as reflected by the `position` field, `V` is the desired velocity as specified
by the `maxVelocity` field (default) or set with `wb_servo_set_velocity()`, `a`
is the acceleration required to reach *Vc* in one time step, `V` is the motor
velocity of the previous time step, `t` is the duration of the simulation time
step as specified by the `basicTimeStep` field of the `WorldInfo` node
(converted in seconds), and `A` is the acceleration of the servo motor as
specified by the `acceleration` field (default) or set with
`wb_servo_set_acceleration()`.

### Velocity Control

The servos can also be used with *velocity control* instead of *position
control*. This is obtained with two function calls: first the
`wb_servo_set_position()` function must be called with `INFINITY` as a position
parameter, then the desired velocity, which may be positive or negative, must be
specified by calling the `wb_servo_set_velocity()` function. This will initiate
a continuous servo motion at the desired speed, while taking into account the
specified acceleration and motor force. Example: `wb_servo_set_position(servo,
INFINITY); wb_servo_set_velocity(servo, 6.28);  // 1 rotation per second`
`INFINITY` is a C macro corresponding to the IEEE 754 floating point standard.
It is implemented in the C99 specifications as well as in C++. In Java, this
value is defined as `Double.POSITIVE_INFINITY`. In Python, you should use
`float('inf')`. Finally, in Matlab you should use the `inf` constant.

### Force Control

The position/velocity control described above are performed by the Webots
P-controller and ODE's joint motor implementation (see ODE documentation). As an
alternative, Webots does also allow the user to directly specify the amount of
torque/force that must be applied by a `Servo`. This is achieved with the
`wb_servo_set_force()` function which specifies the desired amount of
torque/forces and switches off the P-controller and motor force. A subsequent
call to `wb_servo_set_position()` restores the original *position control*. Some
care must be taken when using *force control*. Indeed the torque/force specified
with `wb_servo_set_force()` is applied to the `Servo` continuously. Hence the
`Servo` will infinitely accelerate its rotational or linear motion and
eventually *explode* unless a functional force control algorithm is used.

### Servo Limits

The `position` field is a scalar value that represents the current servo
"rotational" or "linear" position. For a rotational servo, `position` represents
the difference (in radians) between the initial and the current angle of its
rotation field. For a linear servo, `position` represents the distance (in
meters) between the servo's initial and current translation (`translation`
field).

The `minPosition` and `maxPosition` fields define the *soft limits* of the
servo. Soft limits specify the *software* boundaries beyond which the
P-controller will not attempt to move. If the controller calls
`wb_servo_set_position()` with a target position that exceeds the soft limits,
the desired target position will be clipped in order to fit into the soft limit
range. Since the initial position of the servo is always zero, `minPosition`
must always be negative or zero, and `maxPosition` must always be positive or
zero. When both `minPosition` and `maxPosition` are zero (the default), the soft
limits are deactivated. Note that the soft limits can be overstepped when an
external force which exceeds the motor force is applied to the servo. For
example, it is possible that the weight of a robot exceeds the motor force that
is required to hold it up.

The `minStop` and `maxStop` fields define the *hard limits* of the servo. Hard
limits represent physical (or mechanical) bounds that cannot be overrun by any
force. Hard limits can be used, for example, to simulate both end caps of a
hydraulic or pneumatic piston or to restrict the range of rotation of a hinge.
The value of `minStop` must be in the range [-pi, 0] and `maxStop` must be in
the range [0, pi]. When both `minStop` and `maxStop` are zero (the default), the
hard limits are deactivated. The servo hard limits use ODE joint stops (for more
information see the ODE documentation on `dParamLoStop` and `dParamHiStop`).

Finally, note that when both soft and hard limits are activated, the range of
the soft limits must be included in the range of the hard limits, such that
`minStop lt= minValue` and `maxStopgt= maxValue`.

### Springs and Dampers

The `springConstant` field specifies the value of the spring constant (or spring
stiffness), usually denoted as `K`. The `springConstant` must be positive or
zero. If the `springConstant` is zero (the default), no spring torque/force will
be applied to the servo. If the `springConstant` is greater than zero, then a
spring force will be computed and applied to the servo in addition to the other
forces (i.e., motor force, damping force). The spring force is calculated
according to Hooke's law: `F = -Kx`, where `K` is the `springConstant` and `x`
is the current servo position as represented by the `position` field. Therefore,
the spring force is computed so as to be proportional to the current servo
position, and to move the servo back to its initial position. When designing a
robot model that uses springs, it is important to remember that the spring's
resting position for each servo will correspond to the initial position of the
servo.

The `dampingConstant` field specifies the value of the servo damping constant.
The value of `dampingConstant` must be positive or zero. If `dampingConstant` is
zero (the default), no damping torque/force will be added to the servo. If
`dampingConstant` is greater than zero, a damping torque/force will be applied
to the servo in addition to the other forces (i.e., motor force, spring force).
This damping torque/force is proportional to the effective servo velocity: `F =
-Bv`, where `B` is the damping constant, and `v = dx/dt` is the effective servo
velocity computed by the physics simulator.

![Mechanical Diagram of a Servo](pdf/servo_mechanics.pdf)
**Mechanical Diagram of a Servo**

As you can see in (see  ), a `Servo` creates a joint between two masses `m` and
`m`. `m` is defined by the `Physics` node in the parent of the `Servo`. The mass
`m` is defined by the `Physics` node of the `Servo`. The value `x` corresponds
to the initial translation of the `Servo` defined by the `translation` field.
The position `x` corresponds to the current position of the `Servo` defined by
the `position` field.

### Servo Forces

Altogether, three different forces can be applied to a `Servo`: the motor force,
the spring force and the damping force. These three forces are applied in
parallel and can be switched on and off independently (by default only the motor
force is on). For example, to turn off the motor force and obtain a passive
`Servo`, you can set the `maxForce` field to zero.

To obtain a spring amp damper element, you can set `maxForce` to zero and
`springConstant` and `dampingConstant` to non-zero values. A pure spring is
obtained when both `maxForce` and `dampingConstant` but not `springConstant` are
set to zero. However in this case the spring may oscillate forever because
Webots will not simulate the air friction. So it is usually wise to associate
some damping to every spring.

### Friction

The friction applied on the `Servo` to slow down its velocity is computed as the
maximum between the `maxForce` and the `staticFriction` values. The static
friction is particularily useful to add a friction for a passive `Servo`.

### Serial Servos

Each instance of a `Servo` simulates a mechanical system with optional motor,
spring and damping elements, mounted in parallel. Sometimes it is necessary to
have such elements mounted serially. With Webot, serially mounted elements must
be modeled by having `Servo` nodes used as children of other `Servo` nodes. For
example if you wish to have a system where a motor controls the resting position
of a spring, then you will need two `Servo` nodes, as depicted in . In this
example, the parent `Servo` will have a motor force (maxForce gt 0) and the
child `Servo` will have spring and damping forces (`springConstant` gt 0 and
`dampingConstant` gt 0).

![Example of serial connection of two Servo nodes](pdf/servo_serial.pdf)
**Example of serial connection of two Servo nodes**

This is equivalent to this ".wbt" code, where, as you can notice, *Servo2* is a
child of *Servo1*:


```
DEF Servo1 Servo {
  ...
  children [
    DEF Servo2 Servo {
      ...
      children [
        ...
      ]
      boundingObject ...
      physics Physics {
        mass {m2}
      }
      maxForce 0
      springConstant {K}
      dampingConstant {B}
    }
  ]
  boundingObject ...
  physics Physics {
    mass {m1}
  }
  maxForce {M}
  springConstant 0
  dampingConstant 0
}
```

Note that it is necessary to specify the `Physics` and the `boundingObject` of
*Servo1*. This adds the extra body `m` in the simulation, between the motor and
the spring and damper.

### Simulating Overlayed Joint Axes

Sometimes it is necessary to simulate a joint with two or three independent but
overlayed rotation axes (e.g., a shoulder joint with a *pitch* axis and a *roll*
axis). As usually with Webots, each axis must be implemented as a separate
`Servo` node. So for two axes you need two `Servo` nodes, for three axes you
need three `Servo` nodes, etc.

With overlayed axes (or very close axes) the mass and the shape of the body
located between these axes is often unknown or negligible. However, Webots
requires all the intermediate `boundingObject` and `physics` fields to be
defined. So the trick is to use dummy values for these fields. Usually the dummy
`boundingObject` can be specified as a `Sphere` with a radius of 1 millimeter. A
`Sphere` is the preferred choice because this is the cheapest shape for the
collision detection. And the `physics` field can use a `Physics` node with
default values.

This is better explained with an example. Let's assume that we want to build a
pan/tilt robot head. For this we need two independent (and perpendicular)
rotation axes: *pan* and *tilt*. Now let's assume that these axes cross each
other but we don't know anything about the shape and the mass of the body that
links the two axes. Then this can be modeled like this:


```
DEF PAN Servo {
  ...
  children [
    DEF TILT Servo {
      translation 0 0 0  # overlayed
      children [
        DEF HEAD_TRANS Transform {
          # head shape
        }
        # head devices
      ]
      boundingObject USE HEAD_TRANS
      physics Physics {
      }
    }
  ]
  boundingObject DEF DUMMY_BO Sphere {
    radius 0.001
  }
  physics DEF DUMMY_PHYSICS Physics {
  }
}
```

Please note the dummy `Physics` and the 1 millimeter `Sphere` as dummy
`boundingObject`.

### Servo Functions

## Shape


```
Shape {
  SFNode   appearance   NULL
  SFNode   geometry     NULL
}
```

The `Shape` node has two fields, `appearance` and `geometry`, which are used to
create rendered objects in the world. The `appearance` field contains an
`Appearance` node that specifies the visual attributes (e.g., material and
texture) to be applied to the geometry. The `geometry` field contains a
`Geometry` node: `Box`, `Capsule`, `Cone`, `Cylinder`, `ElevationGrid`,
`IndexedFaceSet`, `IndexedLineSet`, `Plane` or `Sphere`. The specified
`Geometry` node is rendered with the specified appearance nodes applied.

## SliderJoint

Derived from `Joint`.


```
SliderJoint {
  field       MFNode  device   [ ]        # linear motor or linear position sensor
  hiddenField SFFloat position 0          # initial position (m)
}
```

### Description

The `SliderJoint` node can be used to model a slider, i.e. a joint allowing only
a translation motion along a given axis (1 degree of freedom). It inherits
`Joint`'s `jointParameters` field. This field can be filled with a
`JointParameters` only. If empty,  `JointParameters` default values apply.

### Field Summary

## Slot


```
Slot {
  field     SFString type      ""
  vrmlField SFNode   endPoint  NULL
}
```

### Description

`Slot` nodes always works with pairs, only a second `Slot` can be added in the
`endPoint` field of a `Slot` before to be able to add any node in the `endPoint`
field of the second `Slot`. Furthermore, the second `Slot` can be added only if
it has the same `type` as the first one.  The `Slot` node is particularly
usefull with PROTOs, it allows the user to constrain the type of nodes that can
be added in an extension field of the PROTO. Imagine for example that you have
an armed robot in which you can plug different kinds of hands. In order to do so
you will put the hand as an extension field of your robot, you will then be able
to add all the different PROTOs of hand that you have made. But nothing prevent
you to add a PROTO of table in the hand extension field. The `Slot` is made for
preventing this kind of problems. By encapsulating your extension field in a
`Slot` and using the `Slot` node as base node for all your hands PROTOs and
defining the same `type` for the field `Slot` and the PROTO `Slot`, only hands
can be inserted in the extension field. This is illustrated in the `example`
section.

### Field Summary

### Example

If you want to write a proto of a robot called `MyRobot` that accepts only hands
in its field `handExtension`, you have to set the field `handExtension` to be
the `endPoint` of a `Slot`.


```
PROTO MyRobot [
  field SFNode handExtension NULL
]
Robot {
  children [
    Slot {
      type "robotHand"
      endPoint IS handExtension
    }
    ...
  ]
}
```

Then any PROTO of a hand needs to use the `Slot` as base node and the `type` of
this `Slot` should match the one in `MyRobot`.


```
PROTO RobotHand [
]
{
  Slot {
    type "robotHand"
    endPoint Solid {
      ...
    }
  }
}
```

## Solid

Derived from `Transform`.


```
Solid {
  SFString   name               "solid"
  SFString   model              ""
  SFString   description        ""
  SFString   contactMaterial    "default"
  MFNode     immersionProperties []
  SFNode     boundingObject   NULL
  SFNode     physics          NULL
  SFBool     locked           FALSE
  SFFloat    translationStep  0.01        # m
  SFFloat    rotationStep     0.261799387 # pi/12 rad 
  # hidden fields
  hiddenField SFVec3f linearVelocity 0 0 0 # initial linear velocity
  hiddenField SFVec3f angularVelocity 0 0 0 # initial angular velocity
}
```

Direct derived nodes: `Accelerometer`, `Camera`, `Charger`, `Compass`,
`Connector`, `Display`, `DistanceSensor`, `Emitter`, `GPS`, `Gyro`,
`InertialUnit`, `LED`, `LightSensor`, `Pen`, `Receiver`, `Robot`, `Servo`,
`TouchSensor`.

### Description

A `Solid` node represents an object with physical properties such as dimensions,
a contact material and optionally a mass. The `Solid` class is the base class
for collision-detected objects. Robots and device classes are subclasses of the
`Solid` class. In the 3D window, `Solid` nodes can be manipulated (dragged,
lifted, rotated, etc) using the mouse.

### Solid Fields

Note that in the `Solid` node, the `scale` field inherited from the `Transform`
must always remain uniform, i.e., of the form `x x x` where `x` is any positive
real number. This ensures that all primitive geometries will remain suitable for
ODE collision detection. Whenever a scale coordinate is changed, the two other
ones are automatically changed to this new value. If a scale coordinate is
assigned a non-positive value, it is automatically changed to 1.

### How to use the boundingObject field?

`boundingObject`s are used to define the bounds of a `Solid` as geometrical
primitive. Each `boundingObject` can hold one or several geometrical primitives,
such as `Box`, `Capsule`, `Cylinder`, etc. These primitives should normally be
chosen such as to represent the approximate bounds of the `Solid`. In the usual
case, the graphical representation of a robot is composed of many complex
shapes, e.g., `IndexedFaceSet`s, placed in the `children` field of the `Solid`
nodes. However this graphical representation is usually too complex to be used
directly for detecting collisions. If there are too many faces the simulation
becomes slow and error-prone. For that reason, it is useful to be able to
approximate the graphical representation by simpler primitives, e.g., one or
more `Box` or `Capsule`s, etc. This is the purpose of the `boundingObject`
field.

Various combinations of primitives can be used in a `boundingObject`: it can
contain either:

The `boundingObject`, together with the `Physics` node, are used to compute the
inertia matrix of the `Solid`. Such a computation assumes a uniform mass
distribution in the primitives composing the `boundingObject`. Note that the
center of mass of the `Solid` does not depend on its `boundingObject`. The
center of mass of is specified by the `centerOfMass` field of the `Physics` node
(in coordinates relative to the center of the `Solid`).

## SolidReference


```
SolidReference {
  field  SFString  solidName  "" # name of an existing solid or ltstatic environmentgt
}
```

### Description

A `SolidReference` can be used inside the `endPoint` field of a `Joint` node to
refer either to an existing `Solid` or to the static environment. Mechanical
loops can be closed this way. The only constraint when referring to a `Solid` is
that both `Solid` and `Joint` must be descendants of a common upper `Solid`.

### Field Summary

## Sphere


```
Sphere { 
  SFFloat   radius        1   # (-inf,inf)
  SFInt32   subdivision   1   # [0,5] or 10
}
```

The `Sphere` node specifies a sphere centered at (0,0,0) in the local coordinate
system. The `radius` field specifies the radius of the sphere (see ).

If `radius` is positive, the outside faces of the sphere are displayed while if
it is negative, the inside faces are displayed.

![Sphere node](png/sphere.png)
**Sphere node**

The `subdivision` field controls the number of faces of the rendered sphere.
Spheres are rendered as icosahedrons with 20 faces when the subdivision field is
set to 0. If the subdivision field is 1 (default value), then each face is
subdivided into 4 faces, making 80 faces. With a subdivision field set to 2, 320
faces will be rendered, making the sphere very smooth. A maximum value of 5
(corresponding to 20480 faces) is allowed for this subdivision field to avoid a
very long rendering process. A value of 10 will turn the sphere appearance into
a black and white soccer ball.

When a texture is applied to a sphere, the texture covers the entire surface,
wrapping counterclockwise from the back of the sphere. The texture has a seam at
the back where the *yz*-plane intersects the sphere. `TextureTransform` affects
the texture coordinates of the Sphere.

## SpotLight

Derived from `Light`.


```
SpotLight { 
  SFFloat ambientIntensity  0        # [0,1]
  SFVec3f attenuation       1 0 0    # [0,inf)
  SFFloat beamWidth         1.570796 # [0,pi/2)
  SFColor color             1 1 1    # [0,1]
  SFFloat cutOffAngle       0.785398 # [0,pi/2)
  SFVec3f direction         0 0 -1   # (-inf,inf)
  SFFloat intensity         1        # [0,1]
  SFVec3f location          0 0 10   # (-inf,inf)
  SFBool  on                TRUE
  SFFloat radius            100      # [0,inf)
  SFBool  castShadows       FALSE
}
```

### Description

The `SpotLight` node defines a light source that emits light from a specific
point along a specific direction vector and constrained within a solid angle.
Spotlights may illuminate `Geometry` nodes that respond to light sources and
intersect the solid angle. Spotlights are specified in their local coordinate
system and are affected by parent transformations.

The `location` field specifies a translation offset of the center point of the
light source from the light's local coordinate system origin. This point is the
apex of the solid angle which bounds light emission from the given light source.
The `direction` field specifies the direction vector of the light's central axis
defined in its own local coordinate system. The `on` field specifies whether the
light source emits light--if TRUE, then the light source is emitting light and
may illuminate geometry in the scene, if FALSE it does not emit light and does
not illuminate any geometry. The `radius` field specifies the radial extent of
the solid angle and the maximum distance from `location` that may be illuminated
by the light source - the light source does not emit light outside this radius.
The `radius` must be >= 0.0.

The `cutOffAngle` field specifies the outer bound of the solid angle. The light
source does not emit light outside of this solid angle. The `beamWidth` field
specifies an inner solid angle in which the light source emits light at uniform
full intensity. The light source's emission intensity drops off from the inner
solid angle (`beamWidth`) to the outer solid angle (`cutOffAngle`). The drop off
function from the inner angle to the outer angle is a cosine raised to a power
function:


```

    intensity(angle) = intensity * (cosine(angle) ** exponent)

    where exponent = 0.5*log(0.5)/log(cos(beamWidth)),
          intensity is the SpotLight's field value,
          intensity(angle) is the light intensity at an arbitrary
              angle from the direction vector,
          and angle ranges from 0.0 at central axis to cutOffAngle.
  
```

If `beamWidth` > `cutOffAngle`, then `beamWidth` is assumed to be equal to
`cutOffAngle` and the light source emits full intensity within the entire solid
angle defined by `cutOffAngle`. Both `beamWidth` and `cutOffAngle` must be
greater than 0.0 and less than or equal to pi/2. See figure below for an
illustration of the SpotLight's field semantics (note: this example uses the
default attenuation).

The light's illumination falls off with distance as specified by three
`attenuation` coefficients. The attenuation factor is
`1/(attenuation[0]+attenuation[1]*r+attenuation[2]*r^2)`, where `r` is the
distance of the light to the surface being illuminated. The default is no
attenuation. An `attenuation` value of `0` `0` `0` is identical to `1` `0` `0`.
Attenuation values must be >= 0.0.

Contrary to the VRML specifications, the `attenuation` and the
`ambientIntensity` fields cannot be set simultaneously.

![Spot light](png/spot_light.png)
**Spot light**

## Supervisor

Derived from `Robot`.


```
Supervisor {
  # no additional fields
}
```

### Description

A `Supervisor` is a special kind of `Robot` which is specially designed to
control the simulation. A `Supervisor` has access to extra functions that are
not available to a regular `Robot`. If a `Supervisor` contains devices then the
`Supervisor` controller can use them. Webots PRO is required to use the
`Supervisor` node.

### Supervisor Functions

As for a regular `Robot` controller, the `wb_robot_init()`, `wb_robot_step()`,
etc. functions must be used in a `Supervisor` controller.

## TextureCoordinate


```
TextureCoordinate {
  MFVec2f   point   []   # (-inf,inf)
}
```

The `TextureCoordinate` node specifies a set of 2D texture coordinates used by
vertex-based `Geometry` nodes (e.g., `IndexedFaceSet`) to map textures to
vertices. Textures are two-dimensional color functions that, given a coordinate
pair *(s,t)*, return a color value *color(s,t)*. Texture map values
(`ImageTexture`) range from 0.0 to 1.0 along the s and t axes. Texture
coordinates identify a location (and thus a color value) in the texture map. The
horizontal coordinate *s* is specified first, followed by the vertical
coordinate *t*.

## TextureTransform


```
TextureTransform {
  SFVec2f   center        0 0   # (-inf,inf)
  SFFloat   rotation      0     # (-inf,inf)
  SFVec2f   scale         1 1   # (-inf,inf)
  SFVec2f   translation   0 0   # (-inf,inf)
}
```

The `TextureTransform` node defines a 2D transformation that is applied to
texture coordinates. This node affects the way textures are applied to the
surface of a `Geometry`. The transformation consists of (in order):

These parameters support changes in the size, orientation, and position of
textures on shapes. Note that these operations appear reversed when viewed on
the surface of a geometric node. For example, a `scale` value of (2 2) will
scale the texture coordinates, with the net effect of shrinking the texture size
by a factor of 2 (texture coordinates are twice as large and thus cause the
texture to repeat). A `translation` of (0.5 0.0) translates the texture
coordinates +0.5 units along the *s* axis, with the net effect of translating
the texture -0.5 along the *s* axis on the geometry's surface. A `rotation` of
pi/2 of the texture coordinates results in a -pi/2 rotation of the texture on
the geometric node.

The `center` field specifies a translation offset in texture coordinate space
about which the `rotation` and `scale` fields are applied. The `scale` field
specifies a scaling factor in *s* and *t* of the texture coordinates about the
center point. The `rotation` field specifies a rotation in radians of the
texture coordinates about the center point after the scaling operation has been
applied. A positive rotation value makes the texture coordinates rotate
counterclockwise about the center, thereby rotating the appearance of the
texture clockwise. The `translation` field specifies a translation of the
texture coordinates.

Given a point **T** with texture coordinates `(s,t)` and a `TextureTransform`
node, **T** is transformed into the point **T'**`=(s',t')` by the three
intermediate transformations described above. Let `C` be the translation mapping
`(0,0)` to the point `(C`, `T` be the translation of vector `(T`, `R` the
rotation with center `(0,0)` and angle theta, and `S` a scaling with scaling
factors `S`. In matrix notation, the corresponding `TextureTransform` reads as

![Texture transformation in matrix notation](pdf/texture_transform.pdf)
**Texture transformation in matrix notation**

where `C` denotes the matrix inverse of `C`.

Note that `TextureTransform` nodes cannot combine or accumulate.

## TouchSensor

Derived from `Device`.


```
TouchSensor {
  SFString   type          "bumper" 
  MFVec3f    lookupTable   [ 0 0 0, 5000 50000 0 ]
  SFFloat    resolution    -1
}
```

### Description

A `TouchSensor` node is used to model a bumper or a force sensor. The
`TouchSensor` comes in three different types. The "bumper" type simply detects
collisions and returns a boolean status. The "force" type measures the force
exerted on the sensor's body on one axis (*z*-axis). The "force-3d" type
measures the 3d force vector exerted by external object on the sensor's body.

Examples of using the `TouchSensor` are provided by the "hoap2_sumo.wbt" and
"hoap2_walk.wbt" worlds (located in the "projects/robots/hoap2/worlds" directory
of Webots) and by the "force_sensor.wbt" and "bumper.wbt" worlds (located in the
"projects/samples/devices/worlds" directory of Webots).

### Field Summary

### Description

#### "bumper" Sensors

A "bumper" `TouchSensor` returns a boolean value that indicates whether or not
there is a collision with another object. More precisely, it returns 1.0 if a
collision is detected and 0.0 otherwise. A collision is detected when the
`boundingObject` of the `TouchSensor` intersects the `boundingObject` of any
other `Solid` object. The `lookupTable` field of a "bumper" sensor is ignored.
The `Physics` node of a "bumper" sensor is not required.

#### "force" Sensors

A "force" `TouchSensor` computes the (scalar) amount of force currently exerted
on the sensor's body along the *z*-axis. The sensor uses this equation:
`r=|f|*cos(alpha)`, where *r* is the return value, `f` is the cumulative force
currently exerted on the sensor's body, and `alpha` is the angle between `f` and
the sensor's *z*-axis. So the "force" sensor returns the projection of the force
on its *z*-axis; a force perpendicular to the *z*-axis yields zero. For this
reason, a "force" sensor must be oriented such that its positive *z*-axis points
outside of the robot, in the direction where the force needs to me measured. For
example if the `TouchSensor` is used as foot sensor then the *z*-axis should be
oriented downwards. The scalar force value must be read using the
`wb_touch_sensor_get_value()` function.

#### "force-3d" Sensors

A "force-3d" `TouchSensor` returns a 3d-vector that represents the cumulative
force currently applied to its body. This 3d-vector is expressed in the
coordinate system of the `TouchSensor`. The length of the vector reflects the
magnitude of the force. The force vector must be read using the
`wb_touch_sensor_get_values()` function.

#### Lookup Table

A "force" and "force-3d" sensors can optionally specify a `lookupTable` to
simulate the possible non-linearity (and saturation) of the real device. The
`lookupTable` allows the user to map the simulated force measured in Newtons (N)
to an output value that will be returned by the `wb_touch_sensor_get_value()`
function. The value returned by the force sensor is first computed by the ODE
physics engine, then interpolated using the `lookupTable`, and finally noise is
added (if specified in the lookupTable). Each line of the `lookupTable` contains
three numbers: (1) an input force in Newtons, (2) the corresponding output
value, and (3) a noise level between 0.0 and 1.0 (see `DistanceSensor` for more
info). Note that the default `lookupTable` of the `TouchSensor` node is: `[   0
0 0 5000 50000 0 ]`and hence it maps forces between 0 and 5000 Newtons to output
values between 0 and 50000, the output unit being 0.1 Newton. You should empty
the `lookupTable` to have Newtons as output units.

#### Collision detection

`TouchSensor`s detect collisions based on the 3D geometry of its
`boundingObject`. So the `boundingObject` must be specified for every type of
`TouchSensor`. Because the actual 3D intersection of the sensors
`boundingObject`s with other `boundingObject`s is used in the calculation, it is
very important that the sensors' `boundingObject`s are correctly positioned;
they should be able to collide with other objects, otherwise they would be
ineffective. For that reason, the `boundingObject`s of `TouchSensor`s should
always extend beyond the other `boundingObject`s of the robot in the area where
the collision is expected.

For example, let's assume that you want to add a `TouchSensor` under the foot of
a humanoid robot. In this case, it is critical that the `boundingObject` of this
sensor (and not any other `boundingObject` of the robot) makes the actual
contact with the floor. Therefore, it is necessary that the sensor's
`boundingObject` extend below any other `boundingObject` of the robot (e.g.,
foot, ankle, etc.).

#### Coordinate System

It is easy to check the orientation of the coordinate system of a `TouchSensor`:
if you select the `TouchSensor` object in the Scene Tree, then only the bounding
object of this `TouchSensor` should be shown in the 3D window. If you zoom in on
this bounding object, you should see the red/green/blue depiction of the
`TouchSensor`'s coordinate system (the color coding is: *x/y/z* =
red/green/blue). For a "force" sensor, the blue (*z*) component should point in
the direction where the collision is expected.

#### Accuracy

The force measured by the ODE physics engine is only a rough approximation of a
real physical force. This approximation usually improves as the `basicTimeStep`
(`WorldInfo` node) decreases.

### TouchSensor Functions

## Track

Derived from `Solid`.


```
Track {
  MFNode     device            []
  SFVec3f    textureAnimation  0 0
  SFNode     animatedGeometry  NULL
  SFInt32    geometriesCount   10
}
```

The `Track` node defines a track object that could be used to model tracks for
conveyor belts or tank robots.

Note that this works only in *physics-based* simulation. Therefore, the
`physics` and `boundingObject` fields of the `Track` node and related `Solid`
nodes must be defined to work properly.

The `device` field optionally specifies a `LinearMotor`, a linear
`PositionSensor` and a `Brake` device. The motor allows to control the motion of
the track, and if not specified the track will behave like a fixed joint.
Position, velocity or force control can be used but force feedback functions are
not available.

The track system doesn't have any default wheel, but it is possible to insert a
`TrackWheel` node in the `children` field to define an object that will
automatically rotate based on its `radius` value and the `Track` motor speed.

Other than the motion, it is also possible to define an animation to show
graphically the movement of the track. Two different types of animation are
available: texture animation and geometries animation.

### Texture Animation

The texture animation is the simplest option and consists in scrolling the
texture object in the direction defined in the `textureAnimation` field. This
scroll value is combined with the belt velocity in order to update the position
of texture at each time step. If the value is *[0 0]* the texture will not move.
Only the first child of the `Track` is taken into consideration for texture
animation, and it has to be a `Shape`, a `Group` node or a `Group` descendant
having a `Shape` node as its first child.

### Geometries Animation

The geometries animation consists of a set of pure graphical `Shape` objects
without physics properties moving along a defined belt path.

The `animatedGeometry` field contains the specification of the appearance and
geometry of the animated objects.

The `geometriesCount` field specifies the number of animated objects that will
move along the belt path.

The belt path along which the animated geometries will move is shaped to the
`TrackWheel` nodes contained in the `children` field. Each wheel contains the
information about its center position, its radius and if it is inside or outside
the belt. By convention the wheels are all aligned along the z-axis of the
`Track` node and have to be defined in clockwise order starting from the one
having the smallest x-axis value. The following code fragment shows the belt
path definition for the convex track example shown in :


```
children [
  TrackWheel {
   position -0.4 0.4
    radius 0.2
    inner TRUE
  }
  TrackWheel {
    position 0.4 0.4
    radius 0.2
    inner TRUE
  }
  TrackWheel {
    position 0.2 0.12
    radius 0.1
    inner TRUE
  }
  TrackWheel {
    position 0 0.12
    radius 0.1
    inner TRUE
  }
  TrackWheel {
    position -0.2 0.12
    radius 0.1
    inner TRUE
  }
]
   
```

![Convex track's belt shape example](png/track_belt_convex.png)
**Convex track's belt shape example**

Then for a concave track belt shape like the one shown in the following
`TrackWheel` nodes have to be defined:


```
children [
  TrackWheel {
    position -0.4 0.0
    radius 0.2
    inner TRUE
  }
  TrackWheel {
    position -0.0 0.14
    radius 0.1
    inner FALSE
  }
  TrackWheel {
    position 0.4 0.0
    radius 0.2
    inner TRUE
  }
]
   
```

![Concave track's belt shape example](png/track_belt_concave.png)
**Concave track's belt shape example**

## TrackWheel

Derived from `Group`.


```
TrackWheel {
  SFVec2f    position          0 0
  SFFloat    radius            0.1
  SFBool     inner             TRUE
}
```

### Description

The `TrackWheel` node defines a wheel of a track system defined by a `Track`
node. The shape defined inside the `children` field of the `TrackWheel` node is
automatically rotated along the z-axis based on the speed of the parent `Track`
node. Additionally this node it is used by the parent `Track` node to compute
the track belt path used for geometries animation.

`TrackWheel` node can only be inserted in the `children` field of a `Track`
node.

### Field Summary

## Transform

Derived from `Group`.


```
Transform {
  SFVec3f      translation   0 0 0     # 3D vector
  SFRotation   rotation      0 1 0 0   # 3D unit vector,angle (rad)
  SFVec3f      scale         1 1 1     # 3 real scaling factors
}
```

Direct derived nodes: `Solid`.

### Description

The `Transform` node is a grouping node that defines a coordinate system for its
children that is relative to the coordinate systems of its parent.

### Field Summary

## Viewpoint


```
Viewpoint {
  SFFloat      fieldOfView    0.785398  # (0,pi)
  SFRotation   orientation    0 0 1 0   # 3D unit vector, angle (rad)
  SFVec3f      position       0 0 0     # 3D vector
  SFString     description    ""
  SFFloat      near           0.05      # [0,inf)
  SFString     follow         ""
}
```

The `Viewpoint` node defines a specific location in the local coordinate system
from which the user may view the scene.

The `position` and `orientation` fields of the `Viewpoint` node specify absolute
locations in the coordinate system. In the default position and orientation, the
viewer is on the *z*-axis, looking down the *-z*-axis toward the origin with
*+x* to the right and *+y* straight up.

Navigating in the 3D view by dragging the mouse pointer dynamically changes the
`position` and the `orientation` fields of the `Viewpoint` node.

The `fieldOfView` field specifies the viewing angle in radians. A small field of
view roughly corresponds to a telephoto lens; a large field of view roughly
corresponds to a wide-angle lens.

The `near` field defines the distance from the camera to the near clipping
plane. This plane is parallel to the projection plane for the 3D display in the
main window. The near field determines the precision of the OpenGL depth buffer.
A too small value may cause depth fighting between overlaid polygons, resulting
in random polygon overlaps. The far clipping plane is parallel to the near
clipping plane and is defined at an infinite distance from the camera. The far
clipping plane distance cannot be modified.

The `near` and the `fieldOfView` fields define together the viewing frustum. Any
3D shape outside this frustum won't be rendered. Hence, shapes too close
(standing between the camera and the near plane) won't appear.

The `follow` field can be used to specify the name of a robot (or other object)
that the viewpoint needs to follow during the simulation. If the string is
empty, or if it does not correspond to any object, then the viewpoint will
remain fixed. The `follow` field is modified by the `View > Follow Object` menu
item.

## WorldInfo


```
WorldInfo {
  SFString   title                          ""
  MFString   info                           []
  SFVec3f    gravity                        0 -9.81 0
  SFFloat    CFM                            0.00001  # [0,inf)
  SFFloat    ERP                            0.2      # [0,1]
  SFString   physics                        ""
  SFFloat    basicTimeStep                  32       # in ms
  SFFloat    FPS                            60
  SFInt32    optimalThreadCount             1        # maximum number of threads assigned to physics computation
  SFFloat    physicsDisableTime             1        # time after which the objects are disabled if they are idle
  SFFloat    physicsDisableLinearThreshold  0.01     # threshold determining if an object is idle or not
  SFFloat    physicsDisableAngularThreshold 0.01     # threshold determining if an object is idle or not
  SFNode     defaultDamping                 NULL     # default damping parameters
  SFFloat    inkEvaporation                 0        # make ground textures evaporate
  SFVec3f    northDirection                 1 0 0    # for compass and InertialUnit
  SFFloat    lineScale                      0.1      # control the length of every arbitrary-sized lines
  MFNode     contactProperties              []       # see ContactProperties node
}
```

The `WorldInfo` node provides general information on the simulated world:

