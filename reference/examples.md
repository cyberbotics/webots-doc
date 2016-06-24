## Examples

Webots comes with several examples of physics plugin. When opening an example,
the code of the physics plugin should appear in Webots text editor. If it does
not appear automatically, then you can always use the menu: `Tools / Edit
Physics Plugin`.

A simple example is the "WEBOTS\_HOME/projects/samples/howto/worlds/physics.wbt"
world. In this example, the plugin is used to add forces to make the robot fly,
to communicate with the Webots model, to detect objects using a `Ray` object, to
display this object using OpenGL and to define a frictionless collision between
the robot and the floor.

The "WEBOTS\_HOME/projects/samples/howto/worlds/contact\_points.wbt" example
shows how to detect collision of an arbitrary object with the floor, draw the
collision contact points in the 3D window, set up contact joints to define the
collison behavior, and determines the forces and torques involved in the
collision. This example can be helpful if you need a detailed feedback about the
contact points and forces involved in the locomotion of a legged robot.

The "WEBOTS\_HOME/projects/samples/demos/worlds/blimp\_lis.wbt" shows how to
suppress gravity, and apply a thrust force (propeller) for a blimp model.

The "WEBOTS\_HOME/projects/samples/demos/worlds/salamander.wbt" shows how to
simulate Archimedes'buoyant force and hydrodynamic drag forces.
