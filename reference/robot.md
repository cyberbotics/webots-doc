## Robot

Derived from `Solid`.


```
Robot {
  SFString   controller        "void"
  SFString   controllerArgs    ""
  SFString   data              ""
  SFBool     synchronization   TRUE
  MFFloat    battery           []
  SFFloat    cpuConsumption    0   # [0,inf)
  SFBool     selfCollision     FALSE
  SFBool     showRobotWindow   FALSE
  SFString   robotWindow       ""
  SFString   remoteControl     ""
}
```

Direct derived nodes: `DifferentialWheels`, `Supervisor`.

### Description

The `Robot` node can be used as basis for building a robot, e.g., an articulated
robot, a humanoid robot, a wheeled robot... If you want to build a two-wheels
robot with differential-drive you should also consider the `DifferentialWheels`
node. If you would like to build a robot with supervisor capabilities use the
`Supervisor` node instead (Webots PRO license required).

### Field Summary

- `controller`: name of the controller program that the simulator must use to
control the robot. This program is located in a directory whose name is equal to
the field's value. This directory is in turn located in the "controllers"
subdirectory of the current project directory. For example, if the field value
is "my\_controller" then the controller program should be located in
"my\_project/controllers/my\_controller/my\_controller[.exe]". The ".exe"
extension is added on the Windows platforms only.
- `controllerArgs`: string containing the arguments (separated by space
characters) to be passed to the `main()` function of the C/C++ controller
program or the `main()` method of the Java controller program.
- `data`: this field may contain any user data, for example parameters
corresponding to the configuration of the robot. It can be read from the robot
controller using the  `wb_robot_get_data()` function and can be written using
the `wb_robot_set_data()` function. It may also be used as a convenience for
communicating between a robot and a supervisor without implementing a Receiver /
Emitter system: The supervisor can read and write in this field using the
generic supervisor functions for accessing fields.
- `synchronization`: if the value is `TRUE` (default value), the simulator is
synchronized with the controller; if the value is `FALSE`, the simulator runs as
fast as possible, without waiting for the controller. The
`wb_robot_get_synchronization()` function can be used to read the value of this
field from a controller program.
- `battery`: this field should contain three values: the first one corresponds to
the present energy level of the robot in Joules (*J*), the second is the maximum
energy the robot can hold in Joules, and the third is the energy recharge speed
in Watts (*[W]=[J]/[s]*). The simulator updates the first value, while the other
two remain constant. *Important:* when the current energy value reaches zero,
the corresponding controller process terminates and the simulated robot stops
all motion. Note: *[J]=[V].[A].[s] and [J]=[V].[A.h]/3600*
- `cpuConsumption`: power consumption of the CPU (central processing unit) of the
robot in Watts.
- `selfCollision`: setting this field to TRUE will enable the detection of
collisions within the robot and apply the corresponding contact forces, so that
the robot limbs cannot cross each other (provided that they have a `Physics`
node). This is useful for complex articulated robots for which the controller
doesn't prevent inner collisions. Enabling self collision is, however, likely to
decrease the simulation speed, as more collisions will be generated during the
simulation. Note that only collisions between non-consecutive solids will be
detected. For consecutive solids, e.g., two solids attached to each other with a
joint, no collision detection is performed, even if the self collision is
enabled. The reason is that this type of collision detection is usually not
wanted by the user, because a very accurate design of the bounding objects of
the solids would be required. To prevent two consecutive solid nodes from
penetrating each other, the `minStop` and `maxStop` fields of the corresponding
joint node should be adjusted accordingly. Here is an example of a robot leg
with self collision enabled:

```
Thigh (solid)
  |
Knee (joint)
  |
Leg (solid)
  |
Ankle (joint)
  |
Foot (solid)
```

In this example, no collision is detected between the "Thigh" and the "Leg"
solids because they are consecutive, e.g., directly joined by the "Knee". In the
same way no collision detection takes place between the "Leg" and the "Foot"
solids because they are also consecutive, e.g., directly joined by the "Ankle".
However, collisions may be detected between the "Thigh" and the "Foot" solids,
because they are non-consecutive, e.g., they are attached to each other through
an intermediate solid ("Leg"). In such an example, it is probably a good idea to
set `minStop` and `maxStop` values for the "Knee" and "Ankle" joints.
- `showRobotWindow`: defines whether the robot window should be shown at the
startup of the controller. If yes, the related entry point function of the robot
window controller plugin (`wbw_show()`) is called as soon as the controller is
initialized.
- `robotWindow`: defines the path of the robot window controller plugin used to
display the robot window. If the `robotWindow` field is empty, the default
generic robot window is loaded. The search algorithm works as following: Let
$(VALUE) be the value of the `robotWindow` field, let $(EXT) be the shared
library file extension of the OS (".so", ".dll" or ".dylib"), let $(PREFIX) be
the shared library file prefix of the OS ("" on windows and "lib" on other OS),
let $(PROJECT) be the current project path, let $(WEBOTS) be the webots
installation path, and let $(...) be a recursive search, then the first existing
file will be used as absolute path:
$(PROJECT)/plugins/robot\_windows/$(VALUE)/$(PREFIX)$(VALUE)$(EXT) $(WEBOTS)/res
ources/$(...)/plugins/robot\_windows/$(VALUE)/$(PREFIX)$(VALUE)$(EXT)
- `remoteControl`: defines the path of the remote-control controller plugin used
to remote control the real robot. The search algorithm is identical to the one
used for the robotWindow field, except that the subdirectory of `plugins` is
`remote_controls` rather than `robot_windows`.

### Synchronous versus Asynchronous controllers

The `synchronization` field specifies if a robot controller must be synchronized
with the simulator or not.

If `synchronization` is `TRUE` (the default), the simulator will wait for the
controller's `wb_robot_step()` whenever necessary to keep the simulation and the
controller synchronized. So for example if the simulation step
(`WorldInfo.basicTimeStep`) is 16 ms and the control step (`wb_robot_step()`) is
64 ms, then Webots will always execute precisely 4 simulation steps during one
control step. After the 4th simulation step, Webots will wait for the
controller's next control step (call to `wb_robot_step(64)`).

If `synchronization` is `FALSE`, the simulator will run as fast a possible
without waiting for the control step. So for example, with the same simulation
step (16 ms) and control step (64 ms) as before, if the simulator has finished
the 4th simulation step but the controller has not yet reached the call to
`wb_robot_step(64)`, then Webots will not wait; instead it will continue the
simulation using the latest actuation commands. Hence, if `synchronization` is
`FALSE`, the number of simulation steps that are executed during a control step
may vary; this will depend on the current simulator and controller speeds and on
the current CPU load, and hence the outcome of the simulation may also vary.
Note that if the number of simulation steps per control step varies, this will
appear as a variations of the "speed of the physics" in the controller's point
of view, and this will appear as a variation of the robot's reaction speed in
the user's point of view.

So generally the `synchronization` field should be set to `TRUE` when robust
control is required. For example if a motion (or ".motion file") was designed in
synchronous mode then it may appear completely different in asynchronous mode.
The asynchronous mode is currently used only for the robot competitions, because
in this case it is necessary to limit the CPU time allocated to each
participating controller. Note that it is also possible to combine synchronous
and asynchronous controllers, e.g., for the robot competitions generally the
`Supervisor` controller is synchronous while the contestants controllers are
asynchronous. Asynchronous controllers may also be recommended for networked
simulations involving several robots distributed over a computer network with an
unpredictable delay (like the Internet).

### Robot Functions

#### Description

The `wb_robot_step()` function is crucial and must be used in every controller.
This function synchronizes the sensor and actuator data between Webots and the
controllers. If the `wb_robot_step()` function is not called then there will be
no actuation in Webots and no update of the sensors in the controller.

The `ms` parameter specifies the number of milliseconds that must be simulated
until the `wb_robot_step()` function returns. Note that this is not real time
but virtual (simulation) time, so this is not like calling the system's
`sleep()`. In fact the function may return immediately, however the important
point is that when it returns `ms` milliseconds of simulation will have elapsed.
In other words the physics will have run for `ms` milliseconds and hence the
motors may have moved, the sensor values may have changed, etc. Note that `ms`
parameter must be a multiple of the `WorldInfo.basicTimeStep`.

If this function returns -1, this indicates that Webots wishes to terminate the
controller. This happens when the user hits the `Revert` button or quits Webots.
So if your code needs to do some cleanup, e.g.,  flushing or closing data files,
etc., it is necessary to test this return value and take proper action. The
controller termination cannot be vetoed: one second later the controller is
killed by Webots. So only one second is available to do the cleanup.

If the `synchronization` field is TRUE, this function always returns 0 (or -1 to
indicate termination). If the `synchronization` field is FALSE, the return value
can be different from 0: Let `controller_time` be the current time of the
controller and let `dt` be the return value. Then `dt` may be interpreted as
follows:

- if `dt` = 0, then the asynchronous behavior was equivalent to the synchronous
behavior.
- if 0 lt= `dt` lt= `ms`, then the actuator values were set at `controller_time` +
`dt`, and the sensor values were measured at `controller_time` + `ms`, as
requested. It means that the step actually lasted the requested number of
milliseconds, but the actuator commands could not be executed on time.
- if `dt` gt `ms`, then the actuators values were set at `controller_time` + `dt`,
and the sensor values were also measured at `controller_time` + `dt`. It means
that the requested step duration could not be respected.

The C API has two additional functions `wb_robot_init()` and
`wb_robot_cleanup()`. There is not equivalent of the `wb_robot_init()` and
`wb_robot_cleanup()` functions in the Java, Python, C++ and MATLAB APIs. In
these languages the necessary initialization and cleanup of the controller
library is done automatically.

The `wb_robot_init()` function is used to initialize the Webots controller
library and enable the communication with the Webots simulator. Note that the
`wb_robot_init()` function must be called before any other Webots API function.

Calling the `wb_robot_cleanup()` function is the clean way to terminate a C
controller. This function frees the various resources allocated by Webots on the
controller side. In addition `wb_robot_cleanup()` signals the termination of the
controller to the simulator. As a consequence, Webots removes the controller
from the simulation which can continue normally with the execution of the other
controllers (if any). If a C controller exits without calling
`wb_robot_cleanup()`, then its termination will not be signalled to Webots. In
this case the simulation will remain blocked (sleeping) on the current step (but
only if this `Robot`'s `synchronization` field is TRUE). Note that the call to
the `wb_robot_cleanup()` function must be the last API function call in a C
controller. Any subsequent Webots API function call will give unpredictable
results.

#### Simple C controller Example

#### Description

This function returns a unique identifier for a device corresponding to a
specified `name`. For example, if a robot contains a `DistanceSensor` node whose
`name` field is "ds1", the function will return the unique identifier of that
device. This `WbDeviceTag` identifier will be used subsequently for enabling,
sending commands to, or reading data from this device. If the specified device
is not found, the function returns 0.

#### See also

.

#### Description

These functions return a reference to an object corresponding to a specified
`name`. Depending on the called function, this object can be an instance of a
`Device` subclass. For example, if a robot contains a `DistanceSensor` node
whose `name` field is "ds1", the function `getDistanceSensor` will return a
reference to a `DistanceSensor` object. If the specified device is not found,
the function returns `NULL` in C++, `null` in Java or the `none` in Python.

#### See also

.

#### Description

These functions allows to get the robot devices by introspection. Indeed they
allow to get the devices from an internal flat list storing the devices. The
size of this list matches with the number of devices. The order of this list
matches with their declaration in the scene tree.

If `index` is out of the bounds of the list index (from 0 to
wb\_robot\_get\_number\_of\_devices() - 1) then the returned WbDeviceTag is
equal to 0.

The following example shows a typical example of introspection. It is used with
the device API allowing to retrieve some information from a WbDeviceTag.


``` c
int n_devices = wb_robot_get_number_of_devices();
int i;
for(i=0; iltn_devices; i++) {
  WbDeviceTag tag = wb_robot_get_device_by_index(i);

  const char *name = wb_device_get_name(tag);
  WbNodeType type = wb_device_get_node_type(tag);

  // do something with the device
  printf("Device #%d name = %s\n", i, name);

  if (type == WB_NODE_CAMERA) {
    // do something with the camera
    printf("Device #%d is a camera\n", i);
  }
}
```

#### Description

These functions allow you to measure the present energy level of the robot
battery. First, it is necessary to enable battery sensor measurements by calling
the `wb_robot_battery_sensor_enable()` function. The `ms` parameter is expressed
in milliseconds and defines how frequently measurements are performed. After the
battery sensor is enabled a value can be read from it by calling the
`wb_robot_battery_sensor_get_value()` function. The returned value corresponds
to the present energy level of the battery expressed in Joules (*J*).

The `wb_robot_battery_sensor_disable()` function should be used to stop battery
sensor measurements.

The `wb_robot_get_battery_sampling_period()` function returns the period given
into the `wb_robot_battery_sensor_enable()` function, or 0 if the device is
disabled.

#### Description

This function returns the value of the `basicTimeStep` field of the `WorldInfo`
node.

#### Description

The `wb_robot_get_mode` function returns an integer value indicating the current
operating mode for the controller.

The `wb_robot_set_mode` function allows to switch between the simulation and the
remote control mode. When switching to the remote-control mode, the `wbr_start`
function of the remote control plugin is called. The argument `arg` is passed
directly to the `wbr_start` function (more information in the user guide).

The integers can be compared to the following enumeration items:

%figure "Helper enumeration to interpret the integer argument and return value of the"
| Mode | Purpose |
| --- | --- |
| WB\_MODE\_SIMULATION | simulation mode |
| WB\_MODE\_CROSS\_COMPILATION | cross compilation mode |
| WB\_MODE\_REMOTE\_CONTROL | remote control mode |
%%end

#### Description

This function returns the name as it is defined in the name field of the robot
node (Robot, DifferentialWheels, Supervisor, etc.) in the current world file.
The string returned should not be deallocated, as it was allocated by the
"libController" shared library and will be deallocated when the controller
terminates. This function is very useful to pass some arbitrary parameter from a
world file to a controller program. For example, you can have the same
controller code behave differently depending on the name of the robot. This is
illustrated in the "soccer.wbt" sample demo, where the goal keeper robot runs
the same control code as the other soccer players, but its behavior is different
because its name was tested to determine its behavior (in this sample world,
names are "b3" for the blue goal keeper and "y3" for the yellow goal keeper,
whereas the other players are named "b1", "b2", "y1" and "y2"). This sample
world is located in the "projects/samples/demos/worlds" directory of Webots.

#### Description

This function returns the model string as it is defined in the model field of
the robot node (Robot, DifferentialWheels, Supervisor, etc.) in the current
world file. The string returned should not be deallocated, as it was allocated
by the "libController" shared library and will be deallocated when the
controller terminates.

#### Description

The `wb_robot_get_data` function returns the string contained in the `data`
field of the robot node.

The `wb_robot_set_data` function set the string contained in the `data` field of
the robot node.

#### Description

This function returns the type of the current mode (WB\_NODE\_ROBOT,
WB\_NODE\_SUPERVISOR or WB\_NODE\_DIFFERENTIAL\_WHEELS).

#### Description

This function returns the full path of the current project, that is the
directory which contains the worlds and controllers subdirectories (among
others) of the current simulation world. It doesn't include the final directory
separator char (slash or anti-slash). The returned pointer is a UTF-8 encoded
char string. It should not be deallocated.

#### Description

This function returns the full path of the current opened world. The returned
pointer is a UTF-8 encoded char string which does include the final ".wbt". It
should not be deallocated.

#### Description

These functions return the content of respectively the Robot::controller and the
Robot::controllerArgs fields.

#### Description

This function returns the boolean value corresponding to the synchronization
field of the Robot node.

#### Description

This function returns the current simulation time in seconds. This correspond to
the simulation time displayed in the speedometer located in the main toolbar. It
does not matter whether the controller is synchronized or not.

#### Description

These functions allow you to read a key pressed on the computer keyboard from a
controller program while the main window of Webots is selected and the
simulation is running. First, it is necessary to enable keyboard input by
calling the `wb_robot_keyboard_enable()` function. The `ms` parameter is
expressed in milliseconds, and defines how frequently readings are updated.
After the enable function is called, values can be read by calling the
`wb_robot_keyboard_get_key()` function repeatedly until this function returns 0.
The returned value, if non-null, is a key code corresponding to a key currently
pressed. If no modifier (shift, control or alt) key is pressed, the key code is
the ASCII code of the corresponding key or a special value (e.g., for the arrow
keys). However, if a modifier key was pressed, the ASCII code (or special value)
can be obtained by applying a binary AND between to the `WB_ROBOT_KEYBOARD_KEY`
mask and the returned value. In this case, the returned value is the result of a
binary OR between one of `WB_ROBOT_KEYBOARD_SHIFT`, `WB_ROBOT_KEYBOARD_CONTROL`
or `WB_ROBOT_KEYBOARD_ALT` and the ASCII code (or the special value) of the
pressed key according to which modifier key was pressed simultaneously.  If no
key is currently pressed, the function will return 0. Calling the
`wb_robot_keyboard_get_key()` function a second time will return either 0 or the
key code of another key which is currently simultaneously pressed. The function
can be called up to 7 times to detect up to 7 simultaneous keys pressed. The
`wb_robot_keyboard_disable()` function should be used to stop the keyboard
readings.

#### Description

This function creates and starts a new thread of execution for the robot
controller. The `task` function is immediately called using the `param`
parameter. It will end only when the `task` function returns. The Webots
controller API is thread safe, however, some API functions use or return
pointers to data structures which are not protected outside the function against
asynchronous access from a different thread. Hence you should use mutexes (see
below) to ensure that such data is not accessed by a different thread.

#### See also

.

#### Description

The `wb_robot_mutex_new()` function creates a new mutex and returns a reference
to that mutex to be used with other mutex functions. A newly created mutex is
always initially unlocked. Mutexes (mutual excluders) are useful with multi-
threaded controllers to protect some resources (typically variables or memory
chunks) from being used simultaneously by different threads.

The `wb_robot_mutex_delete()` function deletes the specified `mutex`. This
function should be used when a mutex is no longer in use.

The `wb_robot_mutex_lock()` function attempts to lock the specified `mutex`. If
the mutex is already locked by another thread, this function waits until the
other thread unlocks the mutex, and then locks it. This function returns only
after it has locked the specified `mutex`.

The `wb_robot_mutex_unlock()` function unlocks the specified `mutex`, allowing
other threads to lock it.

#### See also

.

Users unfamiliar with the mutex concept may wish to consult a reference on
multi-threaded programming techniques for further information.

#### Description

The `wb_robot_window_custom_function` function allows a robot controller to
communicate with the robot window plugin. When this function is called, the
robot window corresponding `wbw_robot_window_custom_function` function is
executed. This robot window entry point has to be explicitly defined in the
plugin. Please also note that it can correctly be executed only if the robot
window has already been initialized, i.e. if it has already been open at least
once. You can find more information about robot window plugin in the user guide.

No particular format on the argument is imposed but any user chosen format is
suitable as long as the controller and robot window codes agree. The following
example shows how to send and receive data from the robot window plugin:

And here is the corresponding robot window function definition:

