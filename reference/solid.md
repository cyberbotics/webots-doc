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

