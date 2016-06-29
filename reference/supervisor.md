## Supervisor

Derived from [Robot](robot.md).

```
Supervisor {
  # no additional fields
}
```

### Description

A [Supervisor](#supervisor) is a special kind of [Robot](robot.md) which is
specially designed to control the simulation. A [Supervisor](#supervisor) has
access to extra functions that are not available to a regular [Robot](robot.md).
If a [Supervisor](#supervisor) contains devices then the
[Supervisor](#supervisor) controller can use them. Webots PRO is required to use
the [Supervisor](#supervisor) node.

> **note**:
Note that in some special cases the [Supervisor](#supervisor) functions might
return wrong values and it might not be possible to retrieve fields and nodes.
This occurs when closing a world and quitting its controllers, i.e. reverting
the current world, opening a new world, or closing Webots. In this case the
output will be a NULL pointer or a default value. For functions returning a
string, an empty string is returned instead of a NULL pointer.

<!-- -->

> **note** [C++, Java, Python]:
It is a good practice to check for a NULL pointer after calling a
[Supervisor](#supervisor) function.

### Supervisor Functions

As for a regular [Robot](robot.md) controller, the `wb_robot_init()`,
`wb_robot_step()`, etc. functions must be used in a [Supervisor](#supervisor)
controller.

**Name**

**wb\_supervisor\_export\_image** - *save the current 3D image of the simulator into a JPEG file, suitable for
    building a webcam system*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_export_image(const char *filename, int quality)
```

**Description**

The `wb_supervisor_export_image()` function saves the current image of Webots
main window into a JPEG file as specified by the `filename` parameter. If the
target file exists, it will be silently overwritten. The `quality` parameter
defines the JPEG quality (in the range 1 - 100). The `filename` parameter should
specify a valid (absolute or relative) file name, e.g., "snapshot.jpg" or
"/var/www/html/images/snapshot.jpg". In fact, a temporary file is first saved,
and then renamed to the requested `filename`. This avoids having a temporary
unfinished (and hence corrupted) file for webcam applications.

**Example**

The "projects/samples/howto/worlds/supervisor.wbt" world provides an example on
how to use the `wb_supervisor_export_image()` function. In this example, the
[Supervisor](#supervisor) controller takes a snapshot image each time a goal is
scored.

---

**Name**

**wb\_supervisor\_node\_get\_from\_def**, **wb\_supervisor\_node\_get\_from\_id**, **wb\_supervisor\_node\_get\_id**, **wb\_supervisor\_node\_get\_parent\_node**, **wb\_supervisor\_node\_get\_root**, **wb\_supervisor\_node\_get\_self** - *get a handle to a node in the world*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

WbNodeRef wb_supervisor_node_get_from_def(const char *def)
WbNodeRef wb_supervisor_node_get_from_id(int id)
int wb_supervisor_node_get_id(WbNodeRef node)
WbNodeRef wb_supervisor_node_get_parent_node(WbNodeRef node)
WbNodeRef wb_supervisor_node_get_root()
WbNodeRef wb_supervisor_node_get_self()
```

**Description**

The `wb_supervisor_node_get_from_def()` function retrieves a handle to a node in
the world from its DEF name. The return value can be used for subsequent calls
to functions which require a `WbNodeRef` parameter. If the requested node does
not exist in the current world file or is an internal node of a PROTO, the
function returns NULL, otherwise, it returns a non-NULL handle.

It is possible to use dots (.) as scoping operator in the DEF parameter. Dots
can be used when looking for a specific node path in the node hierarchy. For
example:

```
WbNodeRef node = wb_supervisor_node_get_from_def("ROBOT.JOINT.SOLID");
```

means that we are searching for a node named "SOLID" inside a node named
"JOINT", inside a node named "ROBOT".

Similarily, the `wb_supervisor_node_get_from_id()` function retrieves a handle
to a node, but from its unique identifier (the `id` parameter). The function
returns NULL if the given identifier doesn't match with any node of the current
world. It is recommended to use this function only when knowing formerly the
identifier (rather than looping on this function to retrieve all the nodes of a
world). For example, when exporting an X3D file, its XML nodes are containing an
`id` attribute which matches with the unique identifier described here.

The `wb_supervisor_node_get_id()` retrieves the unique identifier of the node
given in parameter.

The `wb_supervisor_node_get_parent_node()` function retrieves the reference to
the direct parent node of the node given in parameter.

The `wb_supervisor_node_get_root()` function returns a handle to the root node
which is actually a [Group](group.md) node containing all the nodes visible at
the top level in the scene tree window of Webots. Like any [Group](group.md)
node, the root node has a MFNode field called "children" which can be parsed to
read each node in the scene tree. An example of such a usage is provided in the
"supervisor.wbt" sample worlds (located in the "projects/samples/devices/worlds"
directory of Webots.

The `wb_supervisor_node_get_self()` function returns a handle to the
[Supervisor](#supervisor) node itself on which the controller is run. This is a
utility function that simplifies the task of retrieving the base node without
having to define a DEF name for it.

---

**Name**

**wb\_supervisor\_node\_get\_type**, **wb\_supervisor\_node\_get\_type\_name**, **wb\_supervisor\_node\_get\_base\_type\_name** - *get information on a specified node*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

WbNodeType wb_supervisor_node_get_type(WbNodeRef node)
const char *wb_supervisor_node_get_type_name(WbNodeRef node)
const char *wb_supervisor_node_get_base_type_name(WbNodeRef node)
```

**Description**

The `wb_supervisor_node_get_type()` function returns a symbolic value
corresponding the type of the node specified as an argument. If the argument is
NULL, it returns WB\_NODE\_NO\_NODE. A list of all node types is provided in the
"webots/nodes.h" include file. Node types include
WB\_NODE\_DIFFERENTIAL\_WHEELS, WB\_NODE\_APPEARANCE, WB\_NODE\_LIGHT\_SENSOR,
etc.

The `wb_supervisor_node_get_type_name()` function returns a text string
corresponding to the name of the node. If the argument node is a PROTO node,
this function returns the PROTO name, like "E-puck", "RectangleArena", "Door",
etc. Otherwise if the argument node is not a PROTO node the returned value is
the same as the output of `wb_supervisor_node_get_base_type_name` function, i.e.
"DifferentialWheels", "Appearance", "LightSensor", etc. If the argument is NULL,
the function returns NULL.

The `wb_supervisor_node_get_base_type_name()` function returns a text string
corresponding to the base type name of the node, like "DifferentialWheels",
"Appearance", "LightSensor", etc. If the argument is NULL, the function returns
NULL.

> **note** [C++, Java, Python]:
In the oriented-object APIs, the WB\_NODE\_* constants are available as static
integers of the `Node` class (for example, Node::DIFFERENTIAL\_WHEELS). These
integers can be directly compared with the output of the `Node::getType()`

---

**Name**

**wb\_supervisor\_node\_remove** - *Remove a specified node*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_node_remove(WbNodeRef node)
```

**Description**

The `wb_supervisor_node_remove()` function removes the node specified as an
argument from the Webots scene tree.

---

**Name**

**wb\_supervisor\_node\_get\_field** - *get a field reference from a node*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

WbFieldRef wb_supervisor_node_get_field(WbNodeRef node, const char *field_name)
```

**Description**

The `wb_supervisor_node_get_field()` function retrieves a handler to a node
field. The field is specified by its name in `field_name` and the `node` it
belongs to. It can be a single field (SF) or a multiple field (MF). If no such
field name exists for the specified node or the field is an internal field of a
PROTO, the return value is NULL. Otherwise, it returns a handler to a field.

> **note**:
The `wb_supervisor_node_get_field()` function will return a valid field handler
if the field corresponding to the field name is an hidden field.

---

**Name**

**wb\_supervisor\_node\_get\_position**, **wb\_supervisor\_node\_get\_orientation** - *get the global (world) position/orientation of a node*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

const double *wb_supervisor_node_get_position(WbNodeRef node)
const double *wb_supervisor_node_get_orientation(WbNodeRef node)
```

**Description**

The `wb_supervisor_node_get_position()` function returns the position of a node
expressed in the global (world) coordinate system. The `node` argument must be a
[Transform](transform.md) node (or a derived node), otherwise the function will
print a warning message and return 3 `NaN` (Not a Number) values. This function
returns a vector containing exactly 3 values.

The `wb_supervisor_node_get_orientation()` function returns a matrix that
represents the rotation of the node in the global (world) coordinate system. The
`node` argument must be a [Transform](transform.md) node (or a derived node),
otherwise the function will print a warning message and return 9 `NaN` (Not a
Number) values. This function returns a matrix containing exactly 9 values that
shall be interpreted as a 3 x 3 orthogonal rotation matrix:

```
[ R[0] R[1] R[2] ]
[ R[3] R[4] R[5] ]
[ R[6] R[7] R[8] ]
```

Each column of the matrix represents where each of the three main axes (*x*, *y*
and *z*) is pointing in the node's coordinate system. The columns (and the rows)
of the matrix are pairwise orthogonal unit vectors (i.e., they form an
orthonormal basis). Because the matrix is orthogonal, its transpose is also its
inverse. So by transposing the matrix you can get the inverse rotation. Please
find more info [here](http://en.wikipedia.org/wiki/Rotation_representation).

By multiplying the rotation matrix on the right with a vector and then adding
the position vector you can express the coordinates of a point in the global
(world) coordinate system knowing its coordinates in a local (node) coordinate
system. For example:

```
p' = R * p + T
```

where *p* is a point whose coordinates are given with respect to the local
coordinate system of a node, *R* the rotation matrix returned by
`wb_supervisor_node_get_orientation(node)`, *T* is the position returned by
`wb_supervisor_node_get_position(node)` and *p'* represents the same point but
this time with coordinates expressed in the global (world) coordinate system.

The "WEBOTS\_HOME/projects/robots/ipr/worlds/ipr\_cube.wbt" project shows how to
use these functions to do this.

> **note**:
The returned pointers are valid during one time step only as memory will be
deallocated at the next time step.

---

**Name**

**wb\_supervisor\_node\_get\_center\_of\_mass** - *get the global position of a solid's center of mass*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

const double *wb_supervisor_node_get_center_of_mass(WbNodeRef node)
```

**Description**

The `wb_supervisor_node_get_center_of_mass()` function returns the position of
the center of mass of a Solid node expressed in the global (world) coordinate
system. The `node` argument must be a [Solid](solid.md) node (or a derived
node), otherwise the function will print a warning message and return 3 `NaN`
(Not a Number) values. This function returns a vector containing exactly 3
values. If the `node` argument has a `NULL` `physics` node, the return value is
always the zero vector.

The "WEBOTS\_HOME/projects/samples/.wbt" project shows how to use this function.

> **note**:
The returned pointer is valid during one time step only as memory will be
deallocated at the next time step.

---

**Name**

**wb\_supervisor\_node\_get\_contact\_point** - *get the contact point with given index in the contact point list of the given solid.*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

const double *wb_supervisor_node_get_contact_point(WbNodeRef node, int index)
```

**Description**

The `wb_supervisor_node_get_contact_point()` function returns the contact point
with given index in the contact point list of the given `Solid`. The function
`wb_supervisor_node_get_number_of_contact_points()` allows you to retrieve the
length of this list. Contact points are expressed in the global (world)
coordinate system. If the index is less than the number of contact points, then
the x (resp. y, z) coordinate of the *index*th contact point is the element
number *0* (resp. *1, 2*) in the returned array. Otherwise the function returns
a `NaN` (Not a Number) value for each of these numbers. The `node` argument must
be a [Solid](solid.md) node (or a derived node), which moreover has no `Solid`
parent, otherwise the function will print a warning message and return `NaN`
values on the first 3 array components.

The "WEBOTS\_HOME/projects/samples/howto/worlds/cylinder\_stack.wbt" project
shows how to use this function.

> **note**:
The returned pointer is valid during one time step only as memory will be
deallocated at the next time step.

---

**Name**

**wb\_supervisor\_node\_get\_number\_of\_contact\_points** - *get the number of contact points of the given solid*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

const double *wb_supervisor_node_get_number_of_contact_points(WbNodeRef node)
```

**Description**

The `wb_supervisor_node_get_number_of_contact_points()` function returns the
number of contact points of the given `Solid`. The `node` argument must be a
[Solid](solid.md) node (or a derived node), which moreover has no `Solid`
parent, otherwise the function will print a warning message and return `-1`.

The "WEBOTS\_HOME/projects/samples/howto/worlds/cylinder\_stack.wbt" project
shows how to use this function.

---

**Name**

**wb\_supervisor\_node\_get\_static\_balance** - *return the boolean value of the static balance test based on the support polygon of a solid*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

bool wb_supervisor_node_get_static_balance(WbNodeRef node)
```

**Description**

The `wb_supervisor_node_get_static_balance()` function returns the boolean value
of the static balance test based on the support polygon of a solid. The `node`
argument must be a [Solid](solid.md) node (or a derived node), which moreover
has no `Solid` parent. Otherwise the function will print a warning message and
return `false`. The support polygon of a solid is the convex hull of the solid's
contact points projected onto a plane that is orthognal to the gravity
direction. The test consists in checking whether the projection of the center of
mass onto this plane lies inside or outside the support polygon.

---

**Name**

**wb\_supervisor\_node\_get\_velocity**, **wb\_supervisor\_node\_set\_velocity** - *get/set the angular and linear velocities of a Solid node.*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

const double *wb_supervisor_node_get_velocity(WbNodeRef node)
void wb_supervisor_node_set_velocity(WbNodeRef node, const double velocity[6])
```

**Description**

The `wb_supervisor_node_get_velocity()` function returns the velocity (both
linear and angular) of a node. The `node` argument must be a [Solid](solid.md)
node (or a derived node), otherwise the function will print a warning message
and return 6 `NaN` (Not a Number) values. This function returns a vector
containing exactly 6 values. The first three are respectively the linear
velocities in the x, y and z direction. The last three are respectively the
angular velocities around the x, y and z axes.

The `wb_supervisor_node_set_velocity()` function set the velocity (both linear
and angular) of a node. The `node` argument must be a [Solid](solid.md) node (or
a derived node), otherwise the function will print a warning message and have no
effect. The `velocity` argument must be a vector containing exactly 6 values.
The first three are respectively the linear velocities in the x, y and z
direction. The last three are respectively the angular velocities around the x,
y and z axes.

---

**Name**

**wb\_supervisor\_node\_reset\_physics** - *stops the inertia of the given solid*

{[C++](cpp-api.md#cpp_node)}, {[Java](java-api.md#java_node)}, {[Python](python-api.md#python_node)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_node_reset_physics(WbNodeRef node)
```

**Description**

The `wb_supervisor_node_reset_physics()` function stops the inertia of the given
solid. If the specified node is physics-enables, i.e. it contains a
[Physics](physics.md) node, then the linear and angular velocities of the
corresonding body are reset to 0, hence the inertia is also zeroed. The `node`
argument must be a [Solid](solid.md) node (or a derived node). This function
could be useful for resetting the physics of a solid after changing its
translation or rotation. To stop the inertia of all available solids please
refer to [this section](#wb_supervisor_simulation_reset_physics).

---

**Name**

**wb\_supervisor\_set\_label** - *overlay a text label on the 3D scene*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_set_label(int id, const char *text, double x, double y, double size, int color, double transparency)
```

**Description**

The `wb_supervisor_set_label()` function displays a text label overlaying the 3D
scene in Webots' main window. The `id` parameter is an identifier for the label;
you can choose any value in the range 0 to 65534. The same value may be used
later if you want to change that label, or update the text. Id value 65535 is
reserved for automatic video caption. The `text` parameter is a text string
which should contain only displayable characters in the range 32-127. The `x`
and `y` parameters are the coordinates of the upper left corner of the text,
relative to the upper left corner of the 3D window. These floating point values
are expressed in percent of the 3D window width and height, hence, they should
lie in the range 0-1. The `size` parameter defines the size of the font to be
used. It is expressed in the same unit as the `y` parameter. Finally, the
`color` parameter defines the color of the label. It is expressed as a 3 bytes
RGB integer, the most significant byte (leftmost byte in hexadecimal
representation) represents the red component, the second most significant byte
represents the green component and the third byte represents the blue component.
The `transparency` parameter defines the transparency of the label. A
transparency level of 0 means no transparency, while a transparency level of 1
means total transparency (the text will be invisible). Intermediate values
correspond to semi-transparent levels.

**Example**

-

        wb_supervisor_set_label(0,"hello world",0,0,0.1,0xff0000,0);

will display the label "hello world" in red at the upper left corner of the 3D
window.

-

        wb_supervisor_set_label(1,"hello Webots",0,0.1,0.1,0x00ff00,0.5);

will display the label "hello Webots" in semi-transparent green, just below.

-

        supervisor_set_label(0,"hello universe",0,0,0.1,0xffff00,0);

will change the label "hello world" defined earlier into "hello universe", using
a yellow color for the new text.

> **note** [Matlab]:
In the Matlab version of `wb_supervisor_set_label()` the `color` argument must
be a vector containing the three RGB components: `[RED GREEN BLUE]`. Each
component must be a value between 0.0 and 1.0. For example the vector `[1 0 1]`
represents the magenta color.

---

**Name**

**wb\_supervisor\_simulation\_quit** - *terminate the simulator and controller processes*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_simulation_quit(int status)
```

**Description**

The `wb_supervisor_simulator_quit()` function quits Webots, as if one was using
the menu `File / Quit Webots`. This function makes it easier to invoke a Webots
simulation from a script because it allows to terminate the simulation
automatically, without human intervention. As a result of quitting the simulator
process, all controller processes, including the calling supervisor controller,
will terminate. The `wb_supervisor_simulator_quit()` sends a request to quit the
simulator and immediately returns to the controller process, it does not wait
for the effective termination of the simulator. After the call to
`wb_supervisor_simulator_quit()`, the controller should call the
`wb_robot_cleanup()` function and then exit. The POSIX exit status returned by
Webots can be defined by the status `status` parameter. Some typical values for
this are the `EXIT_SUCCESS` or `EXIT_FAILURE` macros defined into the "stdlib.h"
file. Here is a C example:

```c
#include <webots/robot.h>
#include <webots/supervisor.h>
#include <stdlib.h>

#define TIME_STEP 32

int main(int argc, char *argv[]) {
  wb_robot_init();
  ...
  while (! finished) {
    // your controller code here
    ...
    if (wb_robot_step(TIME_STEP) == -1)
      break;
  }
  saveExperimentsData();
  wb_supervisor_simulation_quit(EXIT_SUCCESS); // ask Webots to terminate
  wb_robot_cleanup(); // cleanup resources
  return 0;
}
```

In object-oriented languages, there is no `wb_robot_cleanup()` function, in this
case the controller should call its destructor. Here is a C++ example:

```c
#include <webots/Robot.hpp>
#include <webots/Supervisor.hpp>
#include <cstdlib>

#define TIME_STEP 32

using namespace webots;

int main(int argc, char *argv[]) {
  Supervisor *controller = new Supervisor();

  ...
  while (! finished) {
    // your controller code here
    ...
    if (controller->step(TIME_STEP) == -1)
      break;
  }
  controller->simulationQuit(EXIT_SUCCESS);  // ask Webots to terminate

  delete controller; // cleanup resources
  return 0;
}
```

---

**Name**

**wb\_supervisor\_simulation\_revert** - *reload the current world*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_simulation_revert()
```

**Description**

The `wb_supervisor_simulator_revert()` function sends a request to the simulator
process, asking it to reload the current world immediately. As a result of
reloading the current world, the supervisor process and all the robot processes
are terminated and restarted. You may wish to save some data in a file from your
supervisor program in order to reload it when the supervisor controller
restarts.

---

**Name**

**wb\_supervisor\_simulation\_get\_mode**, **wb\_supervisor\_simulation\_set\_mode** - *get and set the simulation mode*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

int wb_supervisor_simulation_get_mode()
void wb_supervisor_simulation_set_mode(int mode)
```

**Description**

The `wb_supervisor_simulation_get_mode()` function returns an integer matching
with the current simulation mode, i.e., if the simulation is currently paused,
is running in real-time, or in fast mode with or without the graphical
renderings. The macros described in the [table](#simulation-modes) are matching
with the return value of this function. The value returned by this function is
updated during the previous function call of the `wb_robot_init()` or of the
`wb_robot_step()` functions.

The `wb_supervisor_simulation_set_mode()` function allows to set the simulation
mode. Note that if the `WB_SUPERVISOR_SIMULATION_MODE_PAUSE` is set by the
current supervisor, then calling the `wb_robot_step(time_step)` function with a
`time_step` argument different from 0 is prohibited. Calling `wb_robot_step(0)`
could be useful to send information to Webots when it is paused (such as
modifying, moving, adding or deleting objects). The simulation can then go on by
calling for example
`wb_supervisor_simulation_set_mode(WB_SUPERVISOR_SIMULATION_MODE_RUN)`.

The current simulation mode can also be modified by the Webots user, when he's
clicking on the corresponding buttons in the user interface.

%figure "Simulation modes"

| Mode                                         | Description                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------- |
| WB\_SUPERVISOR\_SIMULATION\_MODE\_PAUSE      | The simulation is paused.                                                       |
| WB\_SUPERVISOR\_SIMULATION\_MODE\_REAL\_TIME | The simulation is running as close as possible to the real-time.                |
| WB\_SUPERVISOR\_SIMULATION\_MODE\_RUN        | The simulation is running as fast as possible with the graphical renderings.    |
| WB\_SUPERVISOR\_SIMULATION\_MODE\_FAST       | The simulation is running as fast as possible without the graphical renderings. |

%end

---

**Name**

**wb\_supervisor\_load\_world**, **wb\_supervisor\_save\_world** - *Load or save the current world.*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_load_world(const char *filename)
bool wb_supervisor_save_world(const char *filename)
```

**Description**

The `wb_supervisor_load_world()` function sends a request to the simulator
process, asking it to stop the current simulation and load the world given in
argument immediately. As a result of changing the current world, the supervisor
process and all the robot processes are terminated and the new one are restarted
with the new world. You may wish to save some data in a file from your
supervisor program in order to reload it from the new world.

The `wb_supervisor_save_world()` function saves the current world. The
`filename` parameter defines the path to the target world file. It should end
with the `.wbt` extension. It can be defined either as an absolute path, or as a
path relative to the current supervisor controller. If NULL, the current world
path is used instead (e.g., a simple save operation). The boolean return value
indicates the success of the save operation. Be aware that this function can
overwrite silently existing files, so that the corresponding data may be lost.

> **note** [C++, Java, Python, Matlab]:
In the other APIs, the `Robot.saveWorld()` function can be called without
argument. In this case, a simple save operation is performed.

---

**Name**

**wb\_supervisor\_simulation\_reset\_physics** - *stop the inertia of all solids in the world and reset the random number generator*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_simulation_reset_physics()
```

**Description**

The `wb_supervisor_simulation_reset_physics()` function sends a request to the
simulator process, asking it to stop the movement of all physics-enabled solids
in the world. It means that for any [Solid](solid.md) node containing a
[Physics](physics.md) node, the linear and angular velocities of the
corresponding body are reset to 0, hence the inertia is also zeroed. This is
actually implemented by calling the ODE `dBodySetLinearVel()` and
`dBodySetAngularVel()` functions for all bodies with a zero velocity parameter.
This function is especially useful for resetting a robot to its initial position
and inertia. To stop the inertia of a single [Solid](solid.md) node please refer
to [this section](#wb_supervisor_node_reset_physics).

Furthermore, this function resets the seed of the random number generator used
in Webots, so that noise-based simulations can be be reproduced identically
after calling this function.

---

**Name**

**wb\_supervisor\_movie\_start\_recording**, **wb\_supervisor\_movie\_stop\_recording**, **wb\_supervisor\_movie\_is\_ready**, **wb\_supervisor\_movie\_failed** - *export the current simulation into a movie file*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_movie_start_recording(const char *filename, int width, int height, int codec, int quality, int acceleration, bool caption)
void wb_supervisor_movie_stop_recording()
bool wb_supervisor_movie_is_ready()
bool wb_supervisor_movie_failed()
```

**Description**

The `wb_supervisor_movie_start_recording()` function starts saving the current
simulation into a movie file. The movie creation process will complete after the
`wb_supervisor_movie_stop_recording()` function is called. The movie is saved in
the file defined by the `filename` parameter. If the `filename` doesn't end with
a ".mp4" extension, the file extension is completed automatically. If the target
file exists, it will be silently overwritten. The `codec` parameter specify the
codec used when creating the movie. Currently only MPEG-4/AVC encoding is
available and the `codec` value is ignored. The `quality` corresponds to the
movie compression factor that affects the movie quality and file size. It should
be a value between 1 and 100. Beware, that choosing a too small value may cause
the video encoding program to fail because of a too low bitrate. The movie frame
rate is automatically computed based on the `basicTimeStep` value of the
simulation in order to produce a real-time movie. The `acceleration` specifies
the acceleration factor of the created movie with respect to the real simulation
time. Default value is 1, i.e. no acceleration. If `caption` parameters is set
to true, a default caption is printed on the top right corner of the movie
showing the current `acceleration` value.

The `wb_supervisor_movie_is_ready()` function returns `TRUE` if the application
is ready to start recording a movie, i.e. if another recording process is not
already running. So it could be used to check if the encoding process is
completed and the file has been created. Note that if the recording process
failed, this function will return `TRUE`. In order to detect a failure the
`wb_supervisor_movie_failed()` function has to be called.

The `wb_supervisor_movie_failed()` function returns `TRUE` if the recording
process failed. After starting a new recording process the returned value is
reset to `FALSE`.

---

**Name**

**wb\_supervisor\_animation\_start\_recording**, **wb\_supervisor\_animation\_stop\_recording** - *export the current simulation into an animation file*

{[C++](cpp-api.md#cpp_supervisor)}, {[Java](java-api.md#java_supervisor)}, {[Python](python-api.md#python_supervisor)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

bool wb_supervisor_animation_start_recording(const char *filename)
bool wb_supervisor_animation_stop_recording()
```

**Description**

The `wb_supervisor_animation_start_recording()` function starts saving the
current simulation into an animation file. The animation creation process will
complete after the `wb_supervisor_animation_stop_recording()` function is
called. Only one animation can be created at the same time. The animation is
saved in the file defined by the `filename` parameter. If the target file
exists, it will be silently overwritten. The `filename` should ends with the
".html" extension. The animation frame rate is automatically computed based on
the `basicTimeStep` value of the simulation in order to produce a real-time
animation.

Both `wb_supervisor_animation_start_recording()` and
`wb_supervisor_animation_stop_recording()` functions are returning a boolean
indicating their success.

---

**Name**

**wb\_supervisor\_field\_get\_type**, **wb\_supervisor\_field\_get\_type\_name**, **wb\_supervisor\_field\_get\_count** - *get a handler and more information on a field in a node*

{[C++](cpp-api.md#cpp_field)}, {[Java](java-api.md#java_field)}, {[Python](python-api.md#python_field)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

WbFieldType wb_supervisor_field_get_type(WbFieldRef field)
const char *wb_supervisor_field_get_type_name(WbFieldRef field)
int wb_supervisor_field_get_count(WbFieldRef field)
```

**Description**

The `wb_supervisor_field_get_type()` returns the data type of a field found
previously from the `wb_supervisor_node_get_field()` function, as a symbolic
value. If the argument is NULL, the function returns 0. Field types are defined
in "webots/supervisor.h" and include for example: `WB_SF_FLOAT`, `WB_MF_NODE`,
`WB_SF_STRING`, etc.

The `wb_supervisor_field_get_type_name()` returns a text string corresponding to
the data type of a field found previously from the
`wb_supervisor_node_get_field()` function. Field type names are defined in the
VRML'97 specifications and include for example: `"SFFloat"`, `"MFNode"`,
`"SFString"`, etc. If the argument is NULL, the function returns NULL.

The `wb_supervisor_field_get_count()` returns the number of items of a multiple
field (MF) passed as an argument to this function. If a single field (SF) or
NULL is passed as an argument to this function, it returns -1. Hence, this
function can also be used to test if a field is MF (like `WB_MF_INT32`) or SF
(like `WB_SF_BOOL`).

> **note** [C++, Java, Python]:
In the oriented-object APIs, the WB\_*F\_* constants are available as static
integers of the `Field` class (for example, Field::SF\_BOOL). These integers can
be directly compared with the output of the `Field::getType()`

---

**Name**

**wb\_supervisor\_field\_get\_sf\_bool**, **wb\_supervisor\_field\_get\_sf\_int32**, **wb\_supervisor\_field\_get\_sf\_float**, **wb\_supervisor\_field\_get\_sf\_vec2f**, **wb\_supervisor\_field\_get\_sf\_vec3f**, **wb\_supervisor\_field\_get\_sf\_rotation**, **wb\_supervisor\_field\_get\_sf\_color**, **wb\_supervisor\_field\_get\_sf\_string**, **wb\_supervisor\_field\_get\_sf\_node**, **wb\_supervisor\_field\_get\_mf\_bool**, **wb\_supervisor\_field\_get\_mf\_int32**, **wb\_supervisor\_field\_get\_mf\_float**, **wb\_supervisor\_field\_get\_mf\_vec2f**, **wb\_supervisor\_field\_get\_mf\_vec3f**, **wb\_supervisor\_field\_get\_mf\_rotation**, **wb\_supervisor\_field\_get\_mf\_color**, **wb\_supervisor\_field\_get\_mf\_string**, **wb\_supervisor\_field\_get\_mf\_node** - *get the value of a field*

{[C++](cpp-api.md#cpp_field)}, {[Java](java-api.md#java_field)}, {[Python](python-api.md#python_field)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

bool wb_supervisor_field_get_sf_bool(WbFieldRef field)
int wb_supervisor_field_get_sf_int32(WbFieldRef field)
double wb_supervisor_field_get_sf_float(WbFieldRef field)
const double *wb_supervisor_field_get_sf_vec2f(WbFieldRef sf_field)
const double *wb_supervisor_field_get_sf_vec3f(WbFieldRef field)
const double *wb_supervisor_field_get_sf_rotation(WbFieldRef field)
const double *wb_supervisor_field_get_sf_color(WbFieldRef field)
const char *wb_supervisor_field_get_sf_string(WbFieldRef field)
WbNodeRef wb_supervisor_field_get_sf_node(WbFieldRef field)
bool wb_supervisor_field_get_mf_bool(WbFieldRef field, int index)
int wb_supervisor_field_get_mf_in32(WbFieldRef field, int index)
double wb_supervisor_field_get_mf_float(WbFieldRef field, int index)
const double *wb_supervisor_field_get_mf_vec2f(WbFieldRef field, int index)
const double *wb_supervisor_field_get_mf_vec3f(WbFieldRef field, int index)
const double *wb_supervisor_field_get_mf_rotation(WbFieldRef field, int index)
const double *wb_supervisor_field_get_mf_color(WbFieldRef field, int index)
const char *wb_supervisor_field_get_mf_string(WbFieldRef field, int index)
WbNodeRef wb_supervisor_field_get_mf_node(WbFieldRef field, int index)
```

**Description**

The `wb_supervisor_field_get_sf_*()` functions retrieve the value of a specified
single `field` (SF). The type of the field has to match the name of the function
used, otherwise the return value is undefined (and a warning message is
displayed). If the `field` parameter is NULL, it has the wrong type, or the
`index` is not valid, then a default value is returned. Default values are
defined as `0` and `0.0` for integer and double values, `false` in case of
boolean values, and NULL for vectors, strings and pointers.

The `wb_supervisor_field_get_mf_*()` functions work the same way as the
`wb_supervisor_field_get_sf_*()` functions but with multiple `field` argument.
They take an additional `index` argument which refers to the index of the item
in the multiple field (MF). The type of the field has to match the name of the
function used and the index should be comprised between 0 and the total number
of item minus one, otherwise the return value is undefined (and a warning
message is displayed).

---

**Name**

**wb\_supervisor\_field\_set\_sf\_bool**, **wb\_supervisor\_field\_set\_sf\_int32**, **wb\_supervisor\_field\_set\_sf\_float**, **wb\_supervisor\_field\_set\_sf\_vec2f**, **wb\_supervisor\_field\_set\_sf\_vec3f**, **wb\_supervisor\_field\_set\_sf\_rotation**, **wb\_supervisor\_field\_set\_sf\_color**, **wb\_supervisor\_field\_set\_sf\_string**, **wb\_supervisor\_field\_set\_mf\_bool**, **wb\_supervisor\_field\_set\_mf\_int32**, **wb\_supervisor\_field\_set\_mf\_float**, **wb\_supervisor\_field\_set\_mf\_vec2f**, **wb\_supervisor\_field\_set\_mf\_vec3f**, **wb\_supervisor\_field\_set\_mf\_rotation**, **wb\_supervisor\_field\_set\_mf\_color**, **wb\_supervisor\_field\_set\_mf\_string** - *set the value of a field*

{[C++](cpp-api.md#cpp_field)}, {[Java](java-api.md#java_field)}, {[Python](python-api.md#python_field)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_field_set_sf_bool(WbFieldRef field, bool value)
void wb_supervisor_field_set_sf_int32(WbFieldRef field, int value)
void wb_supervisor_field_set_sf_float(WbFieldRef field, double value)
void wb_supervisor_field_set_sf_vec2f(WbFieldRef sf_field, const double values[2])
void wb_supervisor_field_set_sf_vec3f(WbFieldRef field, const double values[3])
void wb_supervisor_field_set_sf_rotation(WbFieldRef field, const double values[4])
void wb_supervisor_field_set_sf_color(WbFieldRef field, const double values[3])
void wb_supervisor_field_set_sf_string(WbFieldRef field, const char *value)
void wb_supervisor_field_set_mf_bool(WbFieldRef field, int index, bool value)
void wb_supervisor_field_set_mf_int32(WbFieldRef field, int index, int value)
void wb_supervisor_field_set_mf_float(WbFieldRef field, int index, double value)
void wb_supervisor_field_set_mf_vec2f(WbFieldRef field, int index, const double values[2])
void wb_supervisor_field_set_mf_vec3f(WbFieldRef field, int index, const double values[3])
void wb_supervisor_field_set_mf_rotation(WbFieldRef field, int index, const double values[4])
void wb_supervisor_field_set_mf_color(WbFieldRef field, int index, const double values[3])
void wb_supervisor_field_set_mf_string(WbFieldRef field, int index, const char *value)
```

**Description**

The `wb_supervisor_field_set_sf_*()` functions assign a value to a specified
single `field` (SF). The type of the field has to match with the name of the
function used, otherwise the value of the field remains unchanged (and a warning
message is displayed).

The `wb_supervisor_field_set_mf_*()` functions work the same way as the
`wb_supervisor_field_set_sf_*()` functions but with a multiple `field` (MF)
argument. They take an additional `index` argument which refers to the index of
the item in the multiple field. The type of the field has to match with the name
of the function used and the index should be comprised between minus the total
number of items and the total number of items minus one, otherwise the value of the field remains unchanged (and a warning message is displayed). Using a negative index starts the count from the last element of the field until the first one. Index 0 is equivalent to minus number of items. Index -1 is equivalent to the number of items minus one.

> **note**:
Since Webots 7.4.4, the inertia of a solid is no longer automatically reset when
changing its translation or rotation using `wb_supervisor_field_set_sf_vec2f`
and `wb_supervisor_field_set_sf_rotation` functions. If needed, the user has to
explicitly call [this section](#wb_supervisor_node_reset_physics) function.

**Examples**

The "texture\_change.wbt" world, located in the "projects/samples/howto/worlds"
directory, shows how to change a texture from the supervisor while the
simulation is running. The "soccer.wbt" world, located in the
"projects/samples/demos/worlds" directory, provides a simple example for getting
and setting fields with the above described functions.

---

**Name**

**wb\_supervisor\_field\_import\_mf\_node**, **wb\_supervisor\_field\_import\_mf\_node\_from\_string**, **wb\_supervisor\_field\_remove\_mf\_node** - *import/remove a node into/from an MF\_NODE field (typically a "children" field)*

{[C++](cpp-api.md#cpp_field)}, {[Java](java-api.md#java_field)}, {[Python](python-api.md#python_field)}, {[Matlab](matlab-api.md#matlab_supervisor)}, {[ROS](ros-api.md)}

``` c
#include <webots/supervisor.h>

void wb_supervisor_field_import_mf_node(WbFieldRef field, int position, const char *filename)
void wb_supervisor_field_import_mf_node_from_string(WbFieldRef field, int position, const char *node_string)
void wb_supervisor_field_remove_mf_node(WbFieldRef field, int position)
```

**Description**

The `wb_supervisor_field_import_mf_node()` function imports a Webots node into
an MF\_NODE. This node should be defined in a `.wbo` file referenced by the
`filename` parameter. Such a file can be produced easily from Webots by
selecting a node in the scene tree window and using the `Export` button.

The `position` parameter defines the position in the MF\_NODE where the new node
will be inserted. It can be positive or negative. Here are a few examples for
the `position` parameter:

- 0: insert at the beginning of the scene tree.
- 1: insert at the second position.
- 2: insert at the third position.
- -1: insert at the last position.
- -2: insert at the second position from the end of the scene tree.
- -3: insert at the third position from the end.

The `filename` parameter can be specified as an absolute or a relative path. In
the later case, it is relative to the location of the supervisor controller.

This function is typically used in order to add a node into a "children" field.
Note that a node can be imported into the scene tree by calling this function
with the "children" field of the root node.

The `wb_supervisor_field_import_mf_node_from_string()` function is very similar
to the `wb_supervisor_field_import_mf_node` function, except that the node is
constructed from the `node_string` string. For example, if you want to create a
new robot with a specific controller:

```c
#include <webots/robot.h>
    include <webots/supervisor.h>

    #define TIME_STEP 32

    int main(int argc, char **argv) {
      wb_robot_init();

      WbNodeRef root_node = wb_supervisor_node_get_root();
      WbFieldRef root_children_field = wb_supervisor_node_get_field(root_node, "children");
      wb_supervisor_field_import_mf_node_from_string(root_children_field, 4, "DEF MY_ROBOT Robot { controller \"my_controller\" }");

      ...
    }
```

The `wb_supervisor_field_remove_mf_node()` function removes a Webots node from
an MF\_NODE (like if the node was manually removed from the scene tree).

> **note**:
Note that these functions are still limited in the actual Webots version. For
example, a device imported into a Robot node doesn't reset the Robot, so the
device cannot be get by using the `wb_robot_get_device()` function.
