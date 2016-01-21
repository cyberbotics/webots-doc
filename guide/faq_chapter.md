# Webots FAQ

This chapter is a selection of frequently asked questions found on the `Webots
forum`. You may find additional information directly in the group. Other useful
sources of information about Webots include: `Webots Reference Manual` and
`Cyberbotics' Robot Curriculum`.

## General FAQ

### What are the differences between Webots PRO, Webots EDU and other Webots modules?

Webots PRO provides a fully featured version of Webots intended for robotics
research. Webots EDU provides a special version of Webots well suited for
education. Webots modules are components tailored for specific uses of Webots,
they include different models of robots, objects, environments, programming
interfaces, libraries, etc. Users can purchase only the modules they need
separately. The differences between Webots modules are explained `here`.

### How can I report a bug in Webots?

If you can still start Webots, please report the bug by using Webots menu: `Help
> Bug report...`.

If Webots cannot start any more, please report the bug there:
`http://www.cyberbotics.com/bug`. Please include a precise description of the
problem, the sequence of actions necessary to reproduce the problem. Do also
attach the world file and the controller programs necessary to reproduce it.

Before reporting a bug, please make sure that the problem is actually caused by
Webots and not by your controller program. For example, a crash of the
controller process usually indicates a bug in the controller code, not in
Webots. This situation can be identified with these two symptoms:

### Is it possible to use Visual C++ to compile my controllers?

Yes. However, you will need to create your own project with all the necessary
options. You will find more detailed instructions on how to do that in . To
create the import libraries (the "*.lib" files in Visual C++) from the "*.dll"
files of the lib directory of Webots, please follow the instructions provided
with the documentation of your compiler.

## Programming

### How can I get the 3D position of a robot/object?

There are different functions depending whether this information must be
accessed in the controller, in the Supervisor or in the physics plugin. Note
that Webots PRO is required for using `Supervisor` and the physics plugin
functions. All the functions described below will return the 3D position in
meters and expressed in the global (world) coordinate system.

Clearly, the position of a robot can also be approximated by using *odometry* or
*SLAM* techniques. This is usually more realistic because most robots don't have
a GPS and therefore have no mean of precisely determining their position. You
will find more info about *odometry* and *SLAM* techniques in  `Cyberbotics'
Robot Curriculum`.

#### In controller code:

To get the position of a robot in the robot's controller code: add a `GPS` node
to the robot, then use `wb_robot_get_device(), wb_gps_enable()` and
`wb_gps_get_values()` functions. Note that the `GPS`'s resolution field must be
0 (the default), otherwise the results will be noisy. You will find more info
about the `GPS` node and functions in `Reference Manual`. Note that the `GPS`
can also be placed on a robot's part (arm, foot, etc.) to get the world/global
coordinates of that particular part.

#### In Supervisor code:

A simulation example that shows both the `GPS` and the `Supervisor` techniques
is included in the Webots installation, you just need to open this world:
"WEBOTS_MODULES_PATH/projects/samples/devices/worlds/gps.wbt".

#### In physics plugin code:

In the physics plugin you can use ODE's `dBodyGetPosition()` function. Note that
this function returns the position of the center of mass of the body: this may
be different from the center of the `Solid`. Please find a description of ODE
functions `here`.

### How can I get the linear/angular speed/velocity of a robot/object?

Webots provides several functions to get the 3D position of a robot or an object
(see above): by taking the first derivative of the position you can determine
the velocity. There are also some functions (see below) that can be used to get
the velocity directly:

#### In controller code:

To get the angular velocity of a robot (or robot part) in the robot's controller
code: add a `Gyro` node to the robot (or robot part), then use
`wb_robot_get_device(), wb_gyro_enable()` and `wb_gyro_get_values()` functions.
You will find more information about the `Gyro` node and functions in the
`Reference Manual`.

#### Using a Supervisor:

Using the `wb_supervisor_node_get_velocity()` function it is possible to
retrieve both the linear and angular velocity of any `Solid` node. You will find
more information about this function in the `Reference Manual`.

#### In physics plugin code:

In the physics plugin you can use ODE's `dBodyGetLinearVel()` and
`dBodyAngularVel()` functions. These functions return the linear velocity in
meters per second, respectively the angular velocity in radians per second.
Please find a description of ODE functions here: `here`.

### How can I reset my robot?

Please see .

### What does this mean: "Could not find controller {...} Loading void controller instead." ?

This message means that Webots could neither find an executable file (e.g.
.exe), nor an interpreted language file (e.g. .class, .py, .m) to run as
controller program for a robot. In fact, Webots needs each controller file to be
stored at specific location in order to be able to executed it. The requested
location is in the "controllers" subdirectory of the current Webots project
directory, e.g. "my_project". Inside the "controllers" directory, each
controller project must be stored in its own directory which must be named
precisely like the `controller` field of the Robot. Inside that directory, the
executable/interpretable file must also be named after the `controller` field of
the Robot (plus a possible extension). For example if the controller field of
the robot looks like this, in the Scene Tree: `Robot { controller
"my_controller" }` then the executable/interpretable file will be searched at
the following paths: `my_project/controllers/my_controller/my_controller.exe
(Windows only) my_project/controllers/my_controller/my_controller (Linux/Mac
only) my_project/controllers/my_controller/my_controller.class
my_project/controllers/my_controller/my_controller.py
my_project/controllers/my_controller/my_controller.m` If Webots does not find
any file at the above specified paths, then the error message in question is
shown. So this problem often happens when you:

### What does this mean: "Warning: invalid WbDeviceTag in API function call" ?

A `WbDeviceTag` is an abstract reference (or handle) used to identify a
simulated device in Webots. Any `WbDeviceTag` must be obtained from the
`wb_robot_get_device()` function. Then, it is used to specify a device in
various Webots function calls. Webots issues this warning when the `WbDeviceTag`
passed to a Webots function appears not to correspond to a known device. This
can happen mainly for three reasons:

### Is it possible to apply a (user specified) force to a robot?

Yes. You need to use a *physics plugin* to apply user specified forces (or
torques). Note that Webots PRO is required to create a physics plugin. Then you
can add the physics plugin with the menu item: `Wizards` > `New Physics Plugin`.
After having added the plugin you must compile it using Webots editor. Then you
must associate the plugin with your simulation world. This can be done by
editing the `WorldInfo.physics` field in the Scene Tree. Then you must modify
the plugin code such as to add the force. Here is an example: `#include
ltode/ode.hgt #include ltplugins/physics.hgt  dBodyID body = NULL;  void
webots_physics_init() { // find the body on which you want to apply a force body
= dWebotsGetBodyFromDEF("MY_ROBOT"); ... }  void webots_physics_step() { ...
dVector3 f; f[0] = ... f[1] = ... f[2] = ... ... // at every time step, add a
force to the body dBodyAddForce(body, f[0], f[1], f[2]); ... }` There is more
info on the plugin functions in the `Reference Manual` in the chapter about
Physics Plugins. Additional information about the ODE functions can be found
`here`. You may also want to study this example distributed with Webots:
`WEBOTS_MODULES_PATH/projects/samples/demos/worlds/salamander.wbt` In this
example, the physics plugin adds user computed forces to the robot body in order
to simulate Archimedes and hydrodynamic drag forces.

### How can I draw in the 3D window?

There are different techniques depending on what you want to draw:

### What does this mean: "The time step used by controller {...} is not a multiple of WorldInfo.basicTimeStep!"?

Webots allows to specify the *control step* and the *simulation step*
independently. The control step is the argument passed to the `wb_robot_step()`
function, it specifies the duration of a step of control of the robot. The
*simulation step* is the value specified in `WorldInfo.basicTimeStep` field, it
specifies the duration of a step of integration of the physics simulation, in
other words: how often the objects motion must be recomputed. The execution of a
simulation step is an atomic operation: it cannot be interrupted. Hence a sensor
measurement or a motor actuation must take place between two simulation steps.
For that reason the control step specified with each `wb_robot_step()` must be a
multiple of the simulation step. If it is not the case you get this error
message. So, for example if the `WorldInfo.basicTimeStep` is 16 (ms), then the
control step argument passed to `wb_robot_step()` can be 16, 32, 48, 64, 80,
128, 1024, etc.

### How can I detect collisions?

Webots does automatically detect collisions and apply the contact forces
whenever necessary. The collision detection mechanism is based on the shapes
specified in the `boundingObject`s. Now if you want to programmatically detect
collision, there are several methods:

### Why does my camera window stay black?

The content of the camera windows will appear only after all the following steps
have been completed:

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

## Speed/Performance

### Why is Webots slow on my computer?

You should verify your graphics driver installation. Please find instructions
here .

If you are using a laptop computer, please check the power options and make sure
you are using the high performance power plan.

On Ubuntu (or other Linux) we do also recommend to deactivate *compiz* (`System
> Preferences > Appearance > Visual Effects = None`). Depending on the graphics
hardware, there may be a huge performance drop of the rendering system (up to
10x) when *compiz* is on.

### How can I change the speed of the simulation?

There are several ways to increase the simulation speed:

