## Modeling

### My robot/simulation explodes, what should I do?

The explosion is usually caused by inappropriate values passed to the physics
engine (ODE). There are many things you can be try to improve the stability of
the simulation (adapted from ODE's User Guide):

1. Reduce the value of `WorldInfo.basicTimeStep`. This will also make the
simulation slower, so a tradeoff has to be found. Note that the value of the
control step (`wb_robot_step(TIME_STEP)`) may have to be adapted to avoid
warnings.
2. Reduce the value of the `JointParameters.springConstant` and
`JointParameters.dampingConstant` fields or avoid using springs and dampers at
all.
3. Avoid large mass ratios. A `Joint` that connects a large and a small mass
(`Physics.mass`) together will have a hard time to keep its error low. For
example, using a `Joint` to connect a hand and a hair may be unstable if the
hand/hair mass ratio is large.
4. Increase the value of `WorldInfo.CFM`. This will make the system
numerically more robust and less susceptible to stability problems. This will also
make the system look more *spongy* so a tradeoff has to be found.
5. Avoid making robots (or other objects) move faster than reasonably for the time
step (`WorldInfo.basicTimeStep`). Since contact forces are computed and applied
only at every time step, too fast moving bodies can penetrate each other in
unrealistic ways.
6. Avoid building mechanical loops by using `Connector` nodes. The mechanical loops
may cause constraints to fight each other and generate strange forces in the
system that can swamp the normal forces. For example, an affected body might fly
around as though it has life on its own, with complete disregard for gravity.

### How to make replicable/deterministic simulations?

In order for a Webots simulation results to be reproducible, the following conditions must
be fulfilled:

1. Each simulation must be restarted either by pushing the `Revert` button, or by
using the `wb_supervisor_simulation_revert()` function, or by restarting Webots.
Any other method for resetting the simulation will not reset the physics
(velocity, inertia, etc.) and other simulation data, hence the simulation state
will be reset only partly. The random seeds used by Webots internally are reset
for each simulation restarted with one of the above methods.
2. The `synchronization` flag of every robot and supervisor must be TRUE. Otherwise
the number of physics steps per control step may vary with the current CPU load
and hence the robot's behavior may also vary.
3. The controllers (and physics plugin) code must also be deterministic. In
particular that code must not use a pseudo random generator initialized with an
non-deterministic seed such as the system time. For example this is not suitable
for replicable experiments: `srand(time(NULL))`. Note that uninitialized
variables may also be a source of undeterministc behavior.
4. Each simulation must be executed with the same version of the Webots software
and on the same OS platform. Different OS platforms and different Webots
versions may result small numerical differences.
5. ODE must run in single thread mode.
The number of threads used by ODE to compute the physic can be changed globally in the [preferences](preferences.md) or using the `WorldInfo.basicTimeStep` field.

If the five above conditions are met, Webots simulations become replicable. This
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

1. In the `lookupTable`s: the third column of each `lookupTable` in the .wbt and
.proto files must be reset to 0
2. In the `GPS` nodes: the `resolution` field must be reset to 0
3. In the `Camera` nodes: the `colorNoise` and the `rangeNoise` fields must be
reset to 0
4. In the `DifferentialWheels` nodes: the value of `slipNoise` must be reset to 0
and the value of `encoderNoise` must be reset to -1

### How can I create a passive joint?

First of all, any joint, passive or active, must be created by adding a
`Joint`-derived node (depending on the constraint type requested) in the Scene
Tree. A `Joint` is passive if its device is null (or at least not a
`Motor`-derived node. Alternatively, it is also possible to make a `Motor`
become passive during the simulation; this can be done like this:

```c
wb_motor_set_motor_force(motor, 0.0);
```

The effect is similar to turning off the power of a real motor.

### Is it possible fix/immobilize one part of a robot?

To immobilize one part of the robot, you need to fix the part to the static
environment. This must be done with a *physics plugin* (Webots PRO required).
You can add a physics plugin with the menu item: `Wizards / New Physics Plugin`.
In the plugin code, you must simply add an ODE *fixed joint* between the
*dBodyID* of the robot part and the static environment. This can be implemented
like this:

```c
#include <ode/ode.h>
#include <plugins/physics.h>

void webots_physics_init() {

  // get body of the robot part
  dBodyID body = dWebotsGetBodyFromDEF("MY_ROBOT_PART");

  // get the matching world
  dWorldID world = dBodyGetWorld(body);

  // the joint group ID is 0 to allocate the joint normally
  dJointID joint = dJointCreateFixed(world, 0);

  // attach robot part to the static environment: 0
  dJointAttach(joint, body, 0);

  // fix now: remember current position and rotation
  dJointSetFixed(joint);
}

void webots_physics_step() {
  // nothing to do
}

void webots_physics_cleanup() {
  // nothing to do
}
```

You will find the description of Webots physics plugin API in your `Reference
Manual` or on [this
page](http://www.cyberbotics.com/reference/physics-plugin.php). You will find
the description about the ODE functions on [this
page](http://ode-wiki.org/wiki/index.php?title=Manual).

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
RGB components gives better results). To set a `Material` with texture, set only
its `ImageTexture` node. Eventually, the `specularColor` field can be set to a
gray value to set a reflection on the object. The other fields (especially the
`ambientIntensity` and the `emissiveColor` fields) shouldn't be modified except
in specific situations.

The `color` field of the `ElevationGrid` shouldn't be used for a realistic
rendering because it is not affected by the ambient light with the same way as
the other `Shapes`.

Here is a methodology to set up the lights:

1. Place the lights at the desired places. Often, a single directional light
pointing down is sufficient.
2. Set both their `ambientIntensity` and their `intensity` fields to 0.
3. Increase the `ambientIntensity` of the main light. The result will be the
appearance of the objects when they are in shadows.
4. Switch on the shadows if required. The shadows are particularily costly, and are
strongly related to the `Shapes` resolution.
5. Increase the `intensity` of each lamp.
