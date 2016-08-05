## Viewpoint

```
Viewpoint {
  SFFloat      fieldOfView        0.785398  # (0,pi)
  SFRotation   orientation        0 0 1 0   # 3D unit vector, angle (rad)
  SFVec3f      position           0 0 0     # 3D vector
  SFString     description        ""
  SFFloat      near               0.05      # [0,inf)
  SFString     follow             ""
  SFBool       followOrientation  FALSE
}
```

The [Viewpoint](#viewpoint) node defines a specific location in the local
coordinate system from which the user may view the scene.

The `position` and `orientation` fields of the [Viewpoint](#viewpoint) node
specify absolute locations in the coordinate system. In the default position and
orientation, the viewer is on the *z*-axis, looking down the *-z*-axis toward
the origin with *+x* to the right and *+y* straight up.

Navigating in the 3D view by dragging the mouse pointer dynamically changes the
`position` and the `orientation` fields of the [Viewpoint](#viewpoint) node.

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
that the viewpoint will follow in translation (traveling movement) during the simulation. If the string is
empty, or if it does not correspond to any object, then the viewpoint will
remain fixed. The `follow` field is automatically updated when setting the solid
to be followed from the `View / Follow Object` menu item. If multiple solid
instances with the same name exist, the instance to be followed is identified by
adding the instance number to the `follow` field value using the format
"`<name>:<number>`".

The `followOrientation` field can be used to make the viewpoint follow also the orientation of an object (in addition to its position). If `followOrientation` is true, the viewpoint is rigidly attached to the followed object, like an embedded camera onboard a robot. The `follow` field should be set with a valid object name otherwise the `followOrientation` field has no effect.
