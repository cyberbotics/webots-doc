# Physics Plugin

## Introduction of the physics plugins

This chapter describes Webots capability to add a physics plugin to a
simulation. A physics plugin is a user-implemented shared library which is
loaded by Webots at run-time, and which gives access to the low-level API of the
`ODE` physics engine. A physics plugin can be used, for example, to gather
information about the simulated bodies (position, orientation, linear or angular
velocity, etc.), to add forces and torques, to add extra joints, e.g., "ball amp
socket" or "universal joints" to a simulation. For example with a physics plugin
it is possible to design an aerodynamics model for a flying robot, a
hydrodynamics model for a swimming robot, etc. Moreover, with a physics plugin
you can implement your own collision detection system and define non-uniform
friction parameters on some surfaces. Note that physics plugins can be
programmed only in C or C++. Webots PRO is necessary to program physics plugins.

## Plugin Setup

You can add a new plugin, or edit the existing plugin, by using the menu `Tools
> Edit Physics Plugin`. After a physics plugin was created it must be associated
with the current ".wbt" file. This can be done in the Scene Tree: the
`WorldInfo` node has a field called `physics` which indicates the name of the
physics plugin associated with the current world. Select the `WorldInfo.physics`
field, then hit the `Select...` button. A dialog pops-up and lets you choose one
of the plugins available in the current project. Choose a plugin in the dialog
and then save the ".wbt" file.

Note that the `WorldInfo.physics` string specifies the name of the plugin source
and binary files without extension. The extension will be added by Webots
depending on the platform: it will be ".so" (Linux), ".dll" (Windows) or
".dylib" (Mac OS X) for the binary file. For example, this `WorldInfo` node:


```
WorldInfo {
  ...
  physics "my_physics"
  ...
}
```

specifies that the plugin binary file is expected to be at the location
"my_project/plugins/physics/my_physics/my_physics[.dll|.dylib|.so]" (actual
extension depending on the platform) and that the plugin source file should be
located in "my_project/plugins/physics/my_physics/my_physics[.c|.cpp]". If
Webots does not find the file there, it will also look in the
"WEBOTS_HOME/resources/projects/plugins" and
"WEBOTS_MODULES_PATH/projects/default/plugins" directories.

## Callback Functions

The plugin code must contain user-implemented functions that will be called by
Webots during the simulation. These user-implemented functions and their
interfaces are described in this section. The implementation of the
`webots_physics_step()` and `webots_physics_cleanup()` functions is mandatory.
The implementation of the other callback functions is optional.

Since Webots 7.2.0, the ODE physics library used in Webots is multi-threaded.
This allows Webots to run some physics simulation much faster than before on
multi-core CPUs. However, it also implies that programming a physics plug-in is
slightly more complicated as the `webots_physics_collide()` callback function
may be called from different threads. Hence, it should be re-entrant and every
call to an ODE API function modifying the current world (contacts, bodies,
geoms) should be mutex protected within this callback function. We recommend
using POSIX mutexes as exemplified here:


```
static pthread_mutex_t mutex;

void webots_physics_init() {
  pthread_mutex_init(ampmutex, NULL);
  ...
}

int webots_physics_collide(dGeomID g1, dGeomID g2) {
...
    dJointGroupID contact_joint_group = dWebotsGetContactJointGroup();
    pthread_mutex_lock(ampmutex);
    dJointAttach(dJointCreateContact(world,
                                     contact_joint_group,
                                     ampcontact[i]),
                                     robot_body,
                                     NULL);
    pthread_mutex_unlock(ampmutex);
...
}

void webots_physics_cleanup() {
  ...
  pthread_mutex_destroy(ampmutex);
}
```

### void webots_physics_init(dWorldID, dSpaceID, dJointGroupID)

This function is called upon initialization of the world. Its arguments are
obsolete and should not be used. This function is a good place to call the
`dWebotsGetBodyFromDEF()` and `dWebotsGetGeomFromDEF()` functions (see below for
details) to get pointers to the objects for which you want to control the
physics. Before calling this function, Webots sets the current directory to
where the plugin's ".dll", ".so" or ".dylib" was found. This is useful for
reading config files or writing log files in this directory.

The obsolete arguments can be retrieved as follows:


```
void webots_physics_init(dWorldID, dSpaceID, dJointGroupID) {
  // get body of the robot part
  dBodyID body = dWebotsGetBodyFromDEF("MY_ROBOT_PART");
  dGeomID geom = dWebotsGetGeomFromDEF("MY_ROBOT_PART");

  // get the matching world
  dWorldID world = dBodyGetWorld(body);

  // get the matching space
  dSpaceID space = dGeomGetSpace(geom);
}
```

This function is also the preferred place to initialize/reinitialize the random
number generator (via `srand()`). Reinitializing the generator with a constant
seed allows Webots to run reproducible (deterministic) simulations. If you don't
need deterministic behavior you should initialize srand() with the current time:
`srand(time(NULL)`). Webots itself does not invoke `srand()`; however, it uses
`rand()`, for example to add noise to sensor measurements. In order to have
reproducible simulations, it is also required that all controllers run in
*synchronous* mode. That means that the `synchronization` field of every
`Robot`, `DifferentialWheels` or `Supervisor` must be set to TRUE. Finally, note
that ODE uses its own random number generator that you might also want to
reinitialize separately via the `dRandSetSeed()` function.

### int webots_physics_collide(dGeomID, dGeomID)

This function is called whenever a collision occurs between two geoms. It may be
called several times (or not at all) during a single simulation step, depending
on the number of collisions. Generally, you should test whether the two
colliding geoms passed as arguments correspond to objects for which you want to
control the collision. If you don't wish to handle a particular collision you
should return 0 to inform Webots that the default collision handling code must
be used.

Otherwise you should use ODE's `dCollide()` function to find the contact points
between the colliding objects and then you can create contact joints using ODE's
`dJointCreateContact()` function. Normally the contact joints should be created
within the contact joint group given by the `dWebotsGetContactJointGroup()`
function. Note that this contact joint group is automatically emptied after each
simulation step, see `here`. Then the contact joints should be attached to the
corresponding bodies in order to prevent them from inter-penetrating. Finally,
the `webots_physics_collide()` function should return either 1 or 2 to inform
Webots that this collision was handled. If the value 2 is returned, Webots will
moreover notify graphically that a collision occurred by changing the color of
the corresponding boundingObject Geometry in the 3D view.

Since Webots 7.2.0, a multi-threaded version of ODE is used. Therefore, this
function may be called from different threads. You should ensure it is re-
entrant and that every ODE function call modifying the ODE world is protected by
mutexes as explained earlier.

### void webots_physics_step()

This function is called before every physics simulation step (call to the ODE
`dWorldStep()` function). For example it can contain code to read the position
and orientation of bodies or add forces and torques to bodies.

### void webots_physics_step_end()

This function is called right after every physics simulation step (call to the
ODE `dWorldStep()` function). It can be used to read values out of
`dJointFeedback` structures. ODE's `dJointFeedback` structures are used to know
how much torque and force is added by a specific joint to the joined bodies (see
ODE User Guide for more information). For example, if the plugin has registered
`dJointFeedback` structures (using ODE's function `dJointSetFeedback()`), then
the structures will be filled during `dWorldStep()` and the result can be read
straight afterwards in `webots_physics_step_end()`.

### void webots_physics_cleanup()

This function is the counterpart to the `webots_physics_init()` function. It is
called once, when the world is destroyed, and can be used to perform cleanup
operations, such as closing files and freeing the objects that have been created
in the plugin.

### void webots_physics_draw(int pass, const char *view)

This function is used to add user-specified OpenGL graphics to the 3D view
and/or to the cameras. For example, this can be used to draw robots
trajectories, force vectors, etc. The function should normally contain OpenGL
function calls. This function is called 2 times (2 passes): one right before and
one right after the regular OpenGL rendering. The first pass may be useful for
drawing solid objects visible through transparent or semi-transparent objects in
the world, but generally only the second is used. The `pass` argument allows to
distinguish these 2 passes (`pass` = 0 for the pass before the OpenGL rendering,
`pass`  = 1 for the pass after the OpenGL rendering) The `view` argument allows
to determine if the function is called when rendering the 3D view (`view` ==
NULL) or when rendering a robot camera (`view` == Robot::name). Here is an
implementation example:


```
void webots_physics_draw(int pass, const char *view) {
  if (pass == 1 ampamp view == NULL) {
    /* This code is reached only during the second pass of the 3D view */

    /* modify OpenGL context */
    glDisable(GL_DEPTH_TEST);
    glDisable(GL_LIGHTING);
    glLineWidth(2.0);

    /* draw 1 meter yellow line */
    glBegin(GL_LINES);
    glColor3f(1, 1, 0);
    glVertex3f(0, 0, 0);
    glVertex3f(0, 1, 0);
    glEnd();
  }
```

The above example will draw a meter high yellow line in the center of the world.
Note that Webots loads the *world* (global) coordinates matrix right before
calling this function. Therefore the arguments passed to `glVertex()` are
expected to be specified in *world* coordinates. Note that the default OpenGL
states should be restored before leaving this function otherwise the rendering
in Webots 3D view may be altered.

## Utility Functions

This section describes utility functions that are available to the physics
plugin. They are not callback functions, but functions that you can call from
your callback functions.

### dWebotsGetBodyFromDEF()

This function looks for a `Solid` node with the specified name and returns the
corresponding dBodyID. The returned dBodyID is an ODE object that represent a
rigid body with properties such as mass, velocity, inertia, etc. The dBodyID
object can then be used with all the available ODE `dBody*()` functions (see ODE
documentation). For example it is possible to add a force to the body with
`dBodyAddForce()`, etc. The prototype of this function is:


```
dBodyID dWebotsGetBodyFromDEF(const char *DEF);
```

where DEF is the DEF name of the requested `Solid` node.

It is possible to use dots (.) as scoping operator in the DEF parameter. Dots
can be used when looking for a specific node path in the node hierarchy. For
example: `dBodyID head_pitch_body =
dWebotsGetBodyFromDEF("BLUE_PLAYER_1.HeadYaw.HeadPitch");` means that we are
searching for a `Solid` node named "HeadPitch" inside a node named "HeadYaw",
inside a node named "BLUE_PLAYER_1". Note that each dot (.) can be substituted
by any number of named or unnamed nodes, so in other words it is not necessary
to fully specify the path.

This function returns NULL if there is no `Solid` (or derived) node with the
specified DEF name. It will also return NULL if the `physics` field of the
`Solid` node is undefined (NULL) or if the `Solid` have been *merged* with an
ancestor. Solid merging happens between rigidly linked solids with non NULL
`physics` fields, see `Physics`'s "Implicit solid merging and joints" for more
details. This function searches the Scene Tree recursively, therefore it is
recommended to store the result rather than calling it at each step. It is
highly recommended to test for NULL returned values, because passing a NULL
dBodyID to an ODE function is illegal and will crash the plugin and Webots.

### dWebotsGetGeomFromDEF()

This function looks for a `Solid` node with the specified name and returns the
corresponding dGeomID. A dGeomID is an ODE object that represents a geometrical
shape such as a sphere, a cylinder, a box, etc., or a coordinate system
transformation. The dGeomID returned by Webots corresponds to the boundingObject
of the `Solid`. The dGeomID object can then be used with all the available ODE
`dGeom*()` functions (see ODE documentation). The prototype of this function is:


```
dGeomID dWebotsGetGeomFromDEF(const char *DEF);
```

where DEF is the DEF name of the requested `Solid` node.

It is possible to use dots (.) as scoping operator in the DEF parameter, see
above. This function returns NULL if there is no `Solid` (or derived) node with
the specified DEF name. It will also return NULL if the `boundingObject` field
of the `Solid` node is undefined (NULL). This function searches the Scene Tree
recursively therefore it is recommended to store the result rather than calling
it at each step. It is highly recommended to test for NULL returned values,
because passing a NULL dGeomID to an ODE function is illegal and will crash the
plugin and Webots.

Using the returned dGeomID, it is also possible to obtain the corresponding
dBodyID object using ODE's `dGeomGetBody()` function. This is an alternative to
calling the `dWebotsGetGeomFromDEF()` function described above.

Note that this function returns only the top level dGeomID of the
boundingObject, but the boundingObject can be made of a whole hierarchy of
dGeomIDs. Therefore it is risky to make assumptions about the type of the
returned dGeomID. It is safer to use ODE functions to query the actual type. For
example this function may return a "transform geom" (dGeomTransformClass) or a
"space geom" (dSimpleSpaceClass) if this is required to represent the structure
of the boundingObject.

### dWebotsGetContactJointGroup()

This function allows you to retrieve the contact joint group where to create the
contacts. It is typically called inside the `webots_physics_collide()` function.
Remark that this group may change during the time and should be retrieved at
each `webots_physics_collide()` call.

### dGeomSetDynamicFlag(dGeomID geom)

This function switches on the dynamic flag of a given ODE geometry (given by the
`geom` argument).

By default the ODE geometries linked with an ODE body are dynamic, meaning that
they can pass from one to another cluster in the case of the multi-threaded
version of ODE. On the other hand, an ODE geometry without any ODE body is
static, meaning it is available in every cluster.

There are some cases where one wants to have a dynamic ODE geometry even if it
is not linked with an ODE body. This is the puropose of this function. Typically
the ODE rays (which don't have bodies) are more efficient if defined as dynamic
geometries.

### dWebotsSend() and dWebotsReceive()

It is often useful to communicate information between your physics plugin and
your robot (or Supervisor) controllers. This is especially useful if your
physics plugin implements some sensors (like accelerometers, force feedback
sensors, etc.) and needs to send the sensor measurement to the robot controller.
It is also useful if your physics plugin implements some actuators (like an
Akermann drive model), and needs to receive motor commands from a robot
controller.

The physics plugin API provides the `dWebotsSend()` function to send messages to
robot controllers and the `dWebotsReceive()` function to receive messages from
robot controllers. In order to receive messages from the physics plugin, a robot
has to contain a `Receiver` node set to an appropriate channel (see Reference
Manual) and with a `baudRate` set to -1 (for infinite communication speed).
Messages are sent from the physics plugin using the `dWebotsSend()` function,
and received through the receiver API as if they were sent by an `Emitter` node
with an infinite range and baud rate. Similarly, in order to send messages to
the physics plugin, a robot has to contain an `Emitter` node set to `channel` 0
(as the physics plugin only receives data sent on this channel). The `range` and
`baudRate` fields of the `Emitter` node should be set to -1 (infinite). Messages
are sent to the physics plugin using the standard `Emitter` API functions. They
are received by the physics plugin through the `dWebotsReceive()` function.


```
void dWebotsSend(int channel,const void *buffer,int size);
void *dWebotsReceive(int *size);
```

The `dWebotsSend()` function sends `size` bytes of data contained in `buffer`
over the specified communication `channel`.

The `dWebotsReceive()` function receives any data sent on channel 0. If no data
was sent, it returns NULL; otherwise it returns a pointer to a buffer containing
the received data. If `size` is non-NULL, it is set to the number of bytes of
data available in the returned buffer. If multiple messages are sent to the
physics plugin at the same time step, then they will be concatenated.

### dWebotsGetTime()

This function returns the current simulation time in milliseconds [ms] as a
double precision floating point value. This corresponds to the time displayed in
the bottom right corner of the main Webots window.


```
double dWebotsGetTime(void);
```

### dWebotsConsolePrintf()

This function prints a line of formatted text to the Webots console. The format
argument is the same as the standard C `printf()` function, i.e., the format
string may contain format characters defining conversion specifiers, and
optional extra arguments should match these conversion specifiers. A prefix and
a '\n' (new line) character will automatically be added to each line. A '\f'
(form feed) character can optionally be used for clearing up the console.


```
void dWebotsConsolePrintf(const char *format, ...);
```

## Structure of ODE objects

This table shows how common ".wbt" constructs are mapped to ODE objects. This
information shall be useful for implementing physics plugins.

## Compiling the Physics Plugin

When a plugin is created using the menu `Wizard > New Physics Plugin`, Webots
will automatically add a suitable ".c" or ".cpp" source file and a Makefile to
the plugin's directory. Your plugin can be compiled with Webots text editor or
manually by using `gcc` and `make` commands in a terminal. On Windows, you can
also use Visual C++ to compile the plugin. In this case, please note that the
plugin should be dynamically linked to the ODE library. The Webots "lib"
directory contains the gcc ("libode.a") and Visual C++ ("ode.lib") import
libraries. Under Linux, you don't need to link the shared library with anything.

## Examples

Webots comes with several examples of physics plugin. When opening an example,
the code of the physics plugin should appear in Webots text editor. If it does
not appear automatically, then you can always use the menu: `Tools > Edit
Physics Plugin`.

A simple example is the "WEBOTS_HOME/projects/samples/howto/worlds/physics.wbt"
world. In this example, the plugin is used to add forces to make the robot fly,
to communicate with the Webots model, to detect objects using a `Ray` object, to
display this object using OpenGL and to define a frictionless collision between
the robot and the floor.

The "WEBOTS_HOME/projects/samples/howto/worlds/contact_points.wbt" example shows
how to detect collision of an arbitrary object with the floor, draw the
collision contact points in the 3D window, set up contact joints to define the
collison behavior, and determines the forces and torques involved in the
collision. This example can be helpful if you need a detailed feedback about the
contact points and forces involved in the locomotion of a legged robot.

The "WEBOTS_HOME/projects/samples/demos/worlds/blimp_lis.wbt" shows how to
suppress gravity, and apply a thrust force (propeller) for a blimp model.

The "WEBOTS_HOME/projects/samples/demos/worlds/salamander.wbt" shows how to
simulate Archimedes'buoyant force and hydrodynamic drag forces.

## ODE improvments

In order to extend ODE possibilities and correct some bugs, the version of ODE
bundled with Webots was improved. New functions were added and some existing
functions were modified.

### Hinge joint

It is possible to set and get the suspension axis thanks to the following two
functions:


```

void dJointSetHingeSuspensionAxis (dJointID, dReal x, dReal y, dReal z);
void dJointGetHingeSuspensionAxis (dJointID, dVector3 result);
    
```

Furthermore, the `dJointSetHingeParam()` and `dJointGetHingeParam()` functions
support `dParamSuspensionERP` and `dParamSuspensionCFM` parameters.

### Hinge 2 joint

By default in ODE, the suspension is along one of the axes of the joint, in the
ODE version of Webots, the suspension has been improved in order to use any
arbitrary axis. It is possible to set and get this axis thanks to the following
two functions:


```

void dJointSetHinge2SuspensionAxis (dJointID, dReal x, dReal y, dReal z);
void dJointGetHinge2SuspensionAxis (dJointID, dVector3 result);
    
```

## Troubleshooting

Unlike the controller code, the physics plugin code is executed in the same
process and memory space as the Webots application. Therefore, a segmentation
fault in the physics plugin code will cause the termination of the Webots
application. Webots termination is often misinterpreted by users who believe
that Webots is unstable, while the error is actually in the user's plugin code.
For that reason, it is important to precisely locate the crash before reporting
a bug to Cyberbotics Ltd.

The following are some debugging hints that should help you find the exact
location of a crash using `gdb` (the GNU Debugger). The first step is to
recompile the physics plugin with the *-g* flag, in order to add debugging
information to the compiled plugin. This can be achieved by adding this line to
the plugin's "Makefile":


```
CFLAGS=-g
```

Then you must rebuild the plugin using Webots Text Editor or using these
commands in a terminal:


```
$ make clean
$ make
```

Make sure that the *-g* flag appears in the compilation line. Once you have
rebuilt the plugin, you can quit Webots, and restart it using `gdb` in a
terminal, like this:


```
$ cd /usr/local/webots
$ export LD_LIBRARY_PATH=/usr/local/webots/lib:$LD_LIBRARY_PATH
$ gdb ./webots-bin
(gdb) run
```

Note that the above path corresponds to a default Webots installation on Linux:
the actual path might be different depending on your specific system or
installation. The LD_LIBRARY_PATH environment variable indicates where to find
the shared libraries that will be required by Webots.

When Webots window appears, run the simulation until it crashes, or make it
crash by some manipulations if necessary. If the plugin crahes due to a
segmentation fault, `gdb` should print an error message similar to this:


```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1208154400 (LWP 30524)]
0x001f5c7e in webots_physics_init (w=0xa6f8060, s=0xa6f80e0, j=0xa6f5c00)
at my_physics.c:50
50            float pos = position[0] + position[1] + position[2];
...
```

This indicates precisely the file name and line number where the problem
occurred. If the indicated file name corresponds to one of the plugin source
files, then the error is located in the plugin code. You can examine the call
stack more precisely by using the `where` or the `bt` command of `gdb`. For
example:


```
(gdb) where
#0  0x001f5c7e in webots_physics_init (w=0xa6f8060, s=0xa6f80e0, j=0xa6f5c00)
at my_physics.c:50
#1  0x081a96b3 in A_PhysicsPlugin::init ()
#2  0x081e304b in A_World::preprocess ()
#3  0x081db3a6 in A_View::render ()
#4  0x081db3f3 in A_View::onPaint ()
#5  0x084de679 in wxEvtHandler::ProcessEventIfMatches ()
#6  0x084de8be in wxEventHashTable::HandleEvent ()
#7  0x084def90 in wxEvtHandler::ProcessEvent ()
#8  0x084ea393 in wxGLContext::SetCurrent ()
...
```

In this example you see that the error is located in the plugin's
`webots_physics_init()` function. If the error is reported in an unknown
function (and if the line number and file name are not displayed), then the
crash may have occurred in Webots, or possibly in a library used by your plugin.

## Execution Scheme

The following diagram illustrates the sequence of execution of the plugin
callback functions. In addition, the principal interactions of Webots with the
ODE functions are indicated.

![Physics Plugin Execution Scheme](pdf/physics_execution_scheme.pdf)
**Physics Plugin Execution Scheme**

