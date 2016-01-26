## Modeling

### My robot/simulation explodes, what should I do?

The explosion is usually caused by inappropriate values passed to the physics
engine (ODE). There are many things you can be try to improve the stability of
the simulation (adapted from ODE's User Guide):

### How to make replicable/deterministic simulations?

In order for a Webots simulation to be replicable, the following conditions must
be fulfilled:

If the four above conditions are met, Webots simulations become replicable. This
means that after the same number of steps two simulations will have exactly the
same internal state. Hence if both simulation are saved using the `Save as...`
button, the resulting files will be identical. This is true independently of the
simulation mode used to execute the simulation: `Step`, `Real-Time`, `Run` or
`Fast`. This is also true whether or not sensor noise is used (see below).

### How to remove the noise from the simulation?

There are two sources of noise in Webots: the *sensor/actuator noise* and the
*physics engine noise*. The amount of sensor/actuator noise can be changed (or
removed) by the user (see below). The physics engine's noise cannot be changed
because it is necessary for the realism of the simulation. To completely remove
the sensor/actuator noise the following field values must be reset:

### How can I create a passive joint?

First of all, any joint, passive or active, must be created by adding a
`Joint`-derived node (depending on the constraint type requested) in the Scene
Tree. A `Joint` is passive if its device is null (or at least not a
`Motor`-derived node. Alternatively, it is also possible to make a `Motor`
become passive during the simulation; this can be done like this:
`wb_motor_set_motor_force(motor, 0.0);` The effect is similar to turning off the
power of a real motor.

### Is it possible fix/immobilize one part of a robot?

To immobilize one part of the robot, you need to fix the part to the static
environment. This must be done with a *physics plugin* (Webots PRO required).
You can add a physics plugin with the menu item: `Wizards > New Physics Plugin`.
In the plugin code, you must simply add an ODE *fixed joint* between the
*dBodyID* of the robot part and the static environment. This can be implemented
like this: `#include ltode/ode.hgt #include ltplugins/physics.hgt  void
webots_physics_init() {  // get body of the robot part dBodyID body =
dWebotsGetBodyFromDEF("MY_ROBOT_PART");  // get the matching world dWorldID
world = dBodyGetWorld(body);  // the joint group ID is 0 to allocate the joint
normally dJointID joint = dJointCreateFixed(world, 0);  // attach robot part to
the static environment: 0 dJointAttach(joint, body, 0);  // fix now: remember
current position and rotation dJointSetFixed(joint); }  void
webots_physics_step() { // nothing to do }  void webots_physics_cleanup() { //
nothing to do }` You will find the description of Webots physics plugin API in
your `Reference Manual` or on `this page`. You will find the description about
the ODE functions on `this page`.

### Should I specify the "mass" or the "density" in the Physics nodes?

It is more accurate to specify the mass if it is known. If you are modeling a
real robot it is sometimes possible to find the mass values in the robot's
specifications. If you specify the densities, Webots will use the volume of each
`boundingObject` multiplied by the density of the corresponding `Physics` node
to compute each mass. This may be less accurate because `boundingObject`s are
often rough approximations.

### How to get a realisitc and efficient rendering?

The quality of the rendering depends on the `Shapes` resolution, on the setup of
the `Materials` and on the setup of the `Lights`.

The bigger the number of vertices is, the slower the simulation is (except
obviously in `fast` mode). A tradeoff has to be found between these two
components. To be efficient, `Shapes` should have a reasonable resolution. If a
rule should be given, a `Shape` shouldn't exceed 1000 vertices. Exporting a
`Shape` from a CAD software generates often meshes having a huge resolution.
Reducing them to low poly meshes is recommended.

The rendering is also closely related to the `Materials`. To set a `Material`
without texture, set only its `Appearance` node. Then you can play with the
`diffuseColor` field to set its color (avoid to use pure colors, balancing the
RGB components give better results). To set a `Material` with texture, set only
its `ImageTexture` node. Eventually, the `specularColor` field can be set to a
gray value to set a reflection on the object. The other fields (especially the
`ambientIntensity` and the `emissiveColor` fields) shouldn't be modified except
in specific situations.

The `color` field of the `ElevationGrid` shouldn't be use for a realistic
rendering because it is not affected by the ambient light with the same way as
the other `Shapes`.

Here is a methodology to set up the lights:

