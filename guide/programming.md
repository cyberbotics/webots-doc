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

