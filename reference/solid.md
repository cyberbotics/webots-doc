## Solid

Derived from [Transform](transform.md).

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

Direct derived nodes: [Accelerometer](accelerometer.md), [Camera](camera.md),
[Charger](charger.md), [Compass](compass.md), [Connector](connector.md),
[Display](display.md), [DistanceSensor](distancesensor.md),
[Emitter](emitter.md), [GPS](gps.md), [Gyro](gyro.md),
[InertialUnit](inertialunit.md), [LED](led.md), [Lidar](lidar.md),
[LightSensor](lightsensor.md), [Pen](pen.md), [RangeFinder](rangefinder.md),
[Receiver](receiver.md), [Robot](robot.md), [Servo](servo.md),
[TouchSensor](touchsensor.md).

### Description

A [Solid](#solid) node represents an object with physical properties such as
dimensions, a contact material and optionally a mass. The [Solid](#solid) class
is the base class for collision-detected objects. Robots and device classes are
subclasses of the [Solid](#solid) class. In the 3D window, [Solid](#solid) nodes
can be manipulated (dragged, lifted, rotated, etc) using the mouse.

### Solid Fields

Note that in the [Solid](#solid) node, the `scale` field inherited from the
[Transform](transform.md) must always remain uniform, i.e., of the form `x x x`
where `x` is any positive real number. This ensures that all primitive
geometries will remain suitable for ODE collision detection. Whenever a scale
coordinate is changed, the two other ones are automatically changed to this new
value. If a scale coordinate is assigned a non-positive value, it is
automatically changed to 1.

- `name`: name of the solid. In derived device classes this corresponds to the
device name argument used by `wb_robot_get_device()`. Note that the name cannot
contain the colon character '`:`'.
- `model`: generic name of the solid (e.g., "chair").
- `description`: short description (1 line) of the solid.
- `contactMaterial`: name of the contact material. When the `boundingObject`s of
[Solid](#solid) nodes intersect, the `contactMaterial` is used to define which
[ContactProperties](contactproperties.md) must be applied at the contact points.
- `immersionProperties`: list of [ immersionProperties](immersionproperties.md)
nodes. It is used to specify dynamic interactions of the [Solid](#solid) node
with one or more [Fluid](fluid.md) nodes.
- `boundingObject`: the bounding object specifies the geometrical primitives used
for collision detection. If the `boundingObject` field is NULL, then no
collision detection is performed and that object can pass through any other
object, e.g., the floor, obstacles and other robots. Note that if the
`boundingObject` field is NULL then the `physics` field (see below) must also be
NULL. You will find more explanations about the `boundingObject` field below.
- `physics`: this field can optionally contain a [Physics](physics.md) node that
is used to model the physical properties of this [Solid](#solid). A
[Physics](physics.md) node should be added when effects such as gravity,
inertia, frictional and contact forces need to be simulated. If the `physics`
field is NULL then Webots simulates this object in *kinematics* mode. Note that
if this field is not NULL then the `boundingObject` field must be specified.
Please find more info in the description of the [Physics](physics.md) node.
- `locked`: if `TRUE`, the solid object cannot be moved using the mouse. This is
useful to prevent moving an object by mistake.
- `translationStep` and `rotationStep`: these fields specify the minimum step size
that will be used by the translate and rotate handles appearing in the 3D window
when selecting a top solid. Continuous increment is obtained by setting the step
value to -1.
- `linearVelocity` and `angularVelocity`: these fields, which aren't visible from
the Scene Tree, are used by Webots when saving a world file to store the initial
linear and angular velocities of a [Solid](#solid) with a non-NULL
[Physics](physics.md) node. If the [Solid](#solid) node is merged into a solid
assembly (see [implicit solid
merging](physics.md#implicit-solid-merging-and-joints)), then these fields will
be effective only for the [Solid](#solid) at the top of the assembly. Hidden
velocity fields allow you to save and restore the dynamics of your simulation or
to define initial velocities for every physical objects in the scene.

### How to use the boundingObject field?

`boundingObject`s are used to define the bounds of a [Solid](#solid) as
geometrical primitive. Each `boundingObject` can hold one or several geometrical
primitives, such as [Box](box.md), [Capsule](capsule.md),
[Cylinder](cylinder.md), etc. These primitives should normally be chosen such as
to represent the approximate bounds of the [Solid](#solid). In the usual case,
the graphical representation of a robot is composed of many complex shapes,
e.g., [IndexedFaceSet](indexedfaceset.md)s, placed in the `children` field of
the [Solid](#solid) nodes. However this graphical representation is usually too
complex to be used directly for detecting collisions. If there are too many
faces the simulation becomes slow and error-prone. For that reason, it is useful
to be able to approximate the graphical representation by simpler primitives,
e.g., one or more [Box](box.md) or [Capsule](capsule.md)s, etc. This is the
purpose of the `boundingObject` field.

Various combinations of primitives can be used in a `boundingObject`: it can
contain either:

1. A [Box](box.md) node,
2. A [Capsule](capsule.md) node,
3. A [Cylinder](cylinder.md) node,
4. An [ElevationGrid](elevationgrid.md) node,
5. An [IndexedFaceSet](indexedfaceset.md) node,
6. A [Plane](plane.md) node,
7. A [Sphere](sphere.md) node,
8. A [Shape](shape.md) node with one of the above nodes in its `geometry` field,
9. A [Transform](transform.md) node with one of the above nodes in its `children`
field, or
10. A [Group](group.md) node with several `children`, each being one of the above.

The `boundingObject`, together with the [Physics](physics.md) node, are used to
compute the inertia matrix of the [Solid](#solid). Such a computation assumes a
uniform mass distribution in the primitives composing the `boundingObject`. Note
that the center of mass of the [Solid](#solid) does not depend on its
`boundingObject`. The center of mass of is specified by the `centerOfMass` field
of the [Physics](physics.md) node (in coordinates relative to the center of the
[Solid](#solid)).

