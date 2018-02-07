## Geometries

This section shows the geometric primitives available in Webots.
The world files for these examples are located in the "sample/geometries/worlds" directory.

In this directory, you will find the following world files :

### box.wbt, capsule.wbt, cone.wbt, convex\_polygon.wbt, cylinder.wbt, non\_convex\_polygon.wbt, polyhedra.wbt, sphere.wbt

**Keywords**: Box, Capsule, Cone, Cylinder, Sphere, IndexedFaceSet, basic 3D primitives

These examples shows how to use the basic geometric primitives of Webots in order to display untextured and colored 3D shapes in the 3D window.
No physics is running in this example.
Basically:

- `box.wbt` demonstrates how to use the `Box` primitive to display a red box.
- `capsule.wbt`: demonstrates how to use the `Capsule` primitive to display a red capsule.
- `cone.wbt`: demonstrates how to use the `Cone` primitive to display a red cone.
- `convex_polygon.wbt`: demonstrates how to use the `IndexedFaceSet` primitive to display a convex polygon.
- `cylinder.wbt`: demonstrates how to use the `Cylinder` primitive to display a red cylinder.
- `polyhedra.wbt`: demonstrates how to use the `IndexedFaceSet` primitive to display a red polyhedra.
- `sphere.wbt`: demonstrates how to use the `Sphere` primitive to display a red sphere.

### extended\_solids.wbt

**Keywords**: Extended solids, torus, rounded box, pipe

![extended_solids.png](images/extended_solids.png) This example demonstrates the use of several extended primitives.
These primitives are based on the basic Geometry nodes, and are defined as PROTO.
Physics is running in this example.

### extrusion.wbt

**Keywords**: Extrusion

![extrusion.png](images/extrusion.png) This example demonstrates the use of the `Extrusion` PROTO.
The `Extrusion` PROTO allows to define a 2D section shape, and to extrude it along a path.
In this example, the section is a triangle extruded along a spiral path.

### floating\_geometries.wbt

**Keywords**: Fluid simulation

![floating_geometries.png](images/floating_geometries.png) This example demonstrates the interactions between basic physics primitives and fluids.
Three geometries are `Fluid` (two flowing fluids and a static pool).
Therefore the other small objects are affected by the fluids viscosity and forces based on the Archimedes' principle.

### high\_resolution\_indexedfaceset.wbt

**Keywords**: IndexedFaceSet, High resolution mesh

![high_resolution_indexedfaceset.png](images/high_resolution_indexedfaceset.png) This example demonstrates the display of a high resolution mesh.
This mesh is a textured high resolution version of the [monkey head of Blender](https://en.wikipedia.org/wiki/Blender_(software)#Suzanne).

### muscle.wbt

**Keywords**: Muscle

![muscle.png](images/muscle.png) This example demonstrates how to use the `Muscle` node.
The `Muscle` nodes helps

Two scenarios are shown:

1. Two muscles are applied on a `HingeJoint`.
Depending on the HingeJoint position, one muscle makes contract, and the other is released.
2. A muscle is applied on a `SliderJoint`.

### physics\_primitives.wbt

**Keywords**: Collisions, physics primitives

![physics_primitives.png](images/physics_primitives.png) This example demonstrates the possible collisions between the basic physics primitives.
Three identical set of primitives composed of a `Box`, a `Capsule`, a `Cylinder`, a `Sphere` and an `IndexedFaceSet` falls over three grounds, respectively, a `Box`, a `Plane` and an `ElevationGrid`.

### textured\_boxes.wbt

**Keywords**: TexturedBox, texture mapping

![textured_box.png](images/textured_box.png) This examples shows the possible UV mappings for the `TexturedBox` PROTO.

### textured\_proto\_shapes.wbt

**Keywords**: TexturedBoxShape, texture mapping

![textured_box_shapes.png](images/textured_box_shapes.png) This examples shows the differences between the `TexturedBoxShape` and `TexturedBoxShape` PROTOs.

### textured\_shapes.wbt

TODO.

### webots\_box.wbt

TODO.
