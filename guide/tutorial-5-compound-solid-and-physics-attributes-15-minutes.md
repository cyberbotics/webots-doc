## Tutorial 5: Compound Solid and Physics Attributes (15 minutes)

The aim of this chapter is to explore in more detail the physics simulation by
creating a solid with several bounding objects: a dumbbell made of two spheres
and one cylinder. The expected result is depicted in .


%figure "Expected result at the end of the tutorial about compound solids."
![Expected result at the end of the tutorial about compound solids.](png/tutorial_dumbbell.png)
%end

### New simulation

### Compound Solid

It is possible to build Solid nodes more complex than what we have seen before
by aggregating Shape nodes. In fact, both the physical and the graphical
properties of a Solid can be made of several Shape nodes. Moreover each Shape
node can be placed in a Transform node in order to change its relative position
and orientation. Group nodes can also be used to group several subnodes.

We want to implement a dumbbell made of a handle (Cylinder) and of two weights
(Sphere) located at each end of the handle. The  depicts the Solid nodes and its
subnodes required to implement the dumbbell.


%figure "Representation of the subnodes of a compound solid made of
    several transformed geometries."
![Representation of the subnodes of a compound solid made of
    several transformed geometries.](pdf/tutorial_compound_solid.pdf.png)
%end

### Physics Attributes

The aim of this subsection is to learn how to set some simple physics properties
for a Solid node. The Physics node contains fields related to the physics of the
current rigid body (Solid).

### The Rotation Field

### How to choose bounding Objects?

As said before, minimizing the number of bounding objects increases the
simulation speed. However choosing the bounding objects primitives carefully is
also crucial to increase the simulation speed.

Using a combination of Sphere, Box, Capsule and Cylinder nodes for defining
objects is very efficient. Generally speaking, the efficiency of these
primitives can be sorted like this: Sphere > Box > Capsule > Cylinder. Where the
Sphere is the most efficient. But this can be neglected for a common usage.

The IndexdedFaceSet geometry primitive can also be used in a bounding object.
But this primitive is less efficient than the other primitives listed above.
Moreover its behavior is sometimes buggy. For this reasons, we don't recommend
using the IndexdedFaceSet when another solution using a combination of the other
primitives is possible.

Grounds can be defined using the Plane or the ElevationGrid primitives. The
Plane node is much more efficient than the ElevationGrid node, but it can only
be used to model a flat terrain while the ElevationGrid can be used to model an
uneven terrain.

### Contacts

We want now to modify the friction model between the dumbbell and the other
solids of the environment.

### basicTimeStep, ERP and CFM

The most critical parameters for a physics simulation are stored in the
`basicTimeStep`, `ERP` and `CFM` fields of the WorldInfo node.

The `basicTimeStep` field determines the duration (in [ms]) of a physics step.
The bigger this value is, the quicker the simulation is, the less precise the
simulation is. We recommend values between *8* and *16* for a regular use of
Webots.

It's more difficult to explain the behavior of the `ERP` and `CFM` fields. These
values are directly used by the physics engine to determine how the constraints
are solved. The default values are well defined  for a regular use of Webots. We
recommend to read the `Reference Manual` and the documentation of [ODE](http
://ode-wiki.org/wiki/index.php?title=Manual) (physics engine used in Webots) to
understand completely their purpose.

### Minor physics Parameters

There are also other physics parameters which are less useful in a regular use
of Webots. A complete description of these parameters can be found in the
`Reference Manual`. Remark simply that the Physics, WorldInfo and
ContactProperties nodes contains other fields.

### Conclusion

You are now able to build a wide range of solids including those being composed
of several rigid bodies. You know that a Geometry node can be moved and rotated
if it is included in a Transform node. You are aware about all the physics
parameters allowing you to design robust simulations. The next step will be to
create your own robot.

You can test your skills by creating common objects such as a table.

