# Programming Fundamentals

This chapter introduces the basic concepts of programming with Webots. Webots
controllers can be written in C/C++, Java, Python or `MATLAB`. Besides their
syntactic differences all these languages share the same low-level
implementation. As long as the sequence of function/method calls does not vary,
every programming language will yield exactly the same simulation results. Hence
the concepts explained here with C examples also apply to
C++/Java/Python/Matlab.

## Controller Programming

The programming examples provided here are in C, but same concepts apply to
C++/Java/Python/Matlab.

### Hello World Example

The tradition in computer science is to start with a "Hello World!" example. So
here is a "Hello World!" example for a Webots controller: `#include
ltwebots/robot.hgt #include ltstdio.hgt  int main() { wb_robot_init();  while
(1) { printf("Hello World!\n"); wb_robot_step(32); }  return 0; }` This code
repeatedly prints `"Hello World!"` to the standard output stream which is
redirected to Webots console. The standard output and error streams are
automatically redirected to Webots console for all Webots supported languages.

Webots C API (Application Programming Interface) is provided by regular C header
files. These header files must be included using statements like `#include
ltwebots/xyz.hgt` where `xyz` represents the name of a Webots node in lowercase.
Like with any regular C code it is also possible to include the standard C
headers, e.g. `#include ltstdio.hgt`. A call to the initialization function
`wb_robot_init()` is required before any other C API function call. This
function initializes the communication between the controller and Webots. Note
that  `wb_robot_init()` exists only in the C API, it does not have any
equivalent in the other supported programming languages.

Usually the highest level control code is placed inside a `for` or a `while`
loop. Within that loop there is a call to the `wb_robot_step()` function. This
function synchronizes the controller's data with the simulator. The function
`wb_robot_step()` needs to be present in every controller and it must be called
at regular intervals, therefore it is usually placed in the main loop as in the
above example. The value 32 specifies the duration of the control steps, i.e.
the function  `wb_robot_step()` shall compute 32 milliseconds of simulation and
then return. This duration specifies an amount of simulated time, not real (wall
clock) time, so it may actually take 1 millisecond or one minute of CPU time,
depending on the complexity of the simulated world.

Note that in this "Hello World!" example the `while` loop has no exit condition,
hence the return statement is never reached. It is usual to have an infinite
loop like this in the controller code: the result is that the controller runs as
long as the simulation runs.

### Reading Sensors

Now that we have seen how to print a message to the console, we shall see how to
read the sensors of a robot. The next example does continuously update and print
the value returned by a `DistanceSensor`: `#include ltwebots/robot.hgt #include
ltwebots/distance_sensor.hgt #include ltstdio.hgt  #define TIME_STEP 32  int
main() { wb_robot_init();  WbDeviceTag ds =
wb_robot_get_device("my_distance_sensor"); wb_distance_sensor_enable(ds,
TIME_STEP);  while (1) { wb_robot_step(TIME_STEP); double dist =
wb_distance_sensor_get_value(ds); printf("sensor value is %f\n", dist); }
return 0; }` As you can notice, prior to using a device, it is necessary to get
the corresponding device tag (`WbDeviceTag`); this is done using the
`wb_robot_get_device()` function. The `WbDeviceTag` is an opaque type that is
used to identify a device in the controller code. Note that the string passed to
this function, *"my_distance_sensor"* in this example, refers to a device name
specified in the robot description (".wbt" or ".proto" file). If the robot has
no device with the specified name, this function returns 0.

Each sensor must be enabled before it can be used. If a sensor is not enabled it
returns undefined values. Enabling a sensor is achieved using the corresponding
`wb_*_enable()` function, where the star (*) stands for the sensor type. Every
`wb_*_enable()` function allows to specify an update delay in milliseconds. The
update delay specifies the desired interval between two updates of the sensor's
data.

In the usual case, the update delay is chosen to be similar to the control step
(`TIME_STEP`) and hence the sensor will be updated at every `wb_robot_step()`.
If, for example, the update delay is chosen to be twice the control step then
the sensor data will be updated every two `wb_robot_step()`: this can be used to
simulate a slow device. Note that a larger update delay can also speed up the
simulation, especially for CPU intensive devices like the `Camera`. On the
contrary, it would be pointless to choose an update delay smaller than the
control step, because it will not be possible for the controller to process the
device's data at a higher frequency than that imposed by the control step. It is
possible to disable a device at any time using the corresponding
`wb_*_disable()` function. This may increase the simulation speed.

The sensor value is updated during the call to `wb_robot_step()`. The call to
`wb_distance_sensor_get_value()` retrieves the latest value.

Note that some device return vector values instead of scalar values, for example
these functions: `const double *wb_gps_get_values(WbDeviceTag tag); const double
*wb_accelerometer_get_values(WbDeviceTag tag); const double
*wb_gyro_get_values(WbDeviceTag tag); ` Each function returns a pointer to three
double values. The pointer is the address of an array allocated by the function
internally. These arrays should never be explicitly deleted by the controller
code. They will be automatically deleted when necessary. The array contains
exactly three double values. Hence accessing the array beyond index 2 is illegal
and may crash the controller. Finally, note that the array elements should not
be modified, for this reason the pointer is declared as *const*. Here are
correct examples of code using these functions: `const double *pos =
wb_gps_get_values(gps);  // OK, to read the values they should never be
explicitly deleted by the controller code. printf("MY_ROBOT is at position: %g
%g %g\n", pos[0], pos[1], pos[2]);  // OK, to copy the values double x, y, z; x
= pos[0]; y = pos[1]; z = pos[2];  // OK, another way to copy the values double
a[3] = { pos[0], pos[1], pos[2] };  // OK, yet another way to copy these values
double b[3]; memcpy(b, pos, sizeof(b));` And here are incorrect examples: `const
double *pos = wb_gps_get_values(gps);  pos[0] = 3.5;      // ERROR: assignment
of read-only location double a = pos[3]; // ERROR: index out of range delete []
pos;     // ERROR: illegal free free(pos);         // ERROR: illegal free`

### Using Actuators

The example below shows how to make a rotational motor oscillate with a 2 Hz
sine signal.

Just like sensors, each Webots actuator must be identified by a `WbDeviceTag`
returned by the `wb_robot_get_device()` function. However, unlike sensors,
actuators don't need to be expressly enabled; they actually don't have
`wb_*_enable()` functions.

To control a motion, it is generally useful to decompose that motion in discrete
steps that correspond to the control step. As before, an infinite loop is used
here: at each iteration a new target position is computed according to a sine
equation. The `wb_motor_set_position()` function stores a new position request
for the corresponding rotational motor. Note that `wb_motor_set_position()`
stores the new position, but it does not immediately actuate the motor. The
effective actuation starts on the next line, in the call to `wb_robot_step()`.
The `wb_robot_step()` function sends the actuation command to the
`RotationalMotor` but it does not wait for the `RotationalMotor` to complete the
motion (i.e. reach the specified target position); it just simulates the motor's
motion for the specified number of milliseconds. `#include ltwebots/robot.hgt
#include ltwebots/motor.hgt #include ltmath.hgt  #define TIME_STEP 32  int
main() { wb_robot_init();  WbDeviceTag motor = wb_robot_get_device("my_motor");
double F = 2.0;   // frequency 2 Hz double t = 0.0;   // elapsed simulation time
while (1) { double pos = sin(t * 2.0 * M_PI * F); wb_motor_set_position(motor,
pos); wb_robot_step(TIME_STEP); t += (double)TIME_STEP / 1000.0; }  return 0; }`
When `wb_robot_step()` returns, the motor has moved by a certain (linear or
rotational) amount which depends on the target position, the duration of the
control step (specified with `wb_robot_step()`), the velocity, acceleration,
force, and other parameters specified in the ".wbt" description of the `Motor`.
For example, if a very small control step or a low motor velocity is specified,
the motor will not have moved much when `wb_robot_step()` returns. In this case
several control steps are required for the `RotationalMotor` to reach the target
position. If a longer duration or a higher velocity is specified, then the motor
may have fully completed the motion when `wb_robot_step()` returns.

Note that `wb_motor_set_position()` only specifies the *desired* target
position. Just like with real robots, it is possible (in physics-based
simulations only), that the `RotationalMotro` is not able to reach this
position, because it is blocked by obstacles or because the motor's torque
(`maxForce`) is insufficient to oppose to the gravity, etc.

If you want to control the motion of several `RotationalMotor`s simultaneously,
then you need to specify the desired position for each `RotationalMotor`
separately, using    `wb_motor_set_position()`. Then you need to call
`wb_robot_step()` once to actuate all the `RotationalMotor`s simultaneously.

### How to use wb_robot_step()

Webots uses two different time steps:

The control step is the duration of an iteration of the control loop. It
corresponds to the parameter passed to the `wb_robot_step()` function. The
`wb_robot_step()` function advances the controller time of the specified
duration. It also synchronizes the sensor and actuator data with the simulator
according to the controller time.

Every controller needs to call `wb_robot_step()` at regular intervals. If a
controller does not call `wb_robot_step()` the sensors and actuators won't be
updated and the simulator will block (in synchronous mode only). Because it
needs to be called regularly, `wb_robot_step()` is usually placed in the main
loop of the controller.

The simulation step is the value specified in `WorldInfo.basicTimeStep` (in
milliseconds). It indicates the duration of one step of simulation, i.e. the
time interval between two computations of the position, speed, collisions, etc.
of every simulated object. If the simulation uses physics (vs. kinematics), then
the simulation step also specifies the interval between two computations of the
forces and torques that need to be applied to the simulated rigid bodies.

The execution of a simulation step is an atomic operation: it cannot be
interrupted. Hence a sensor measurement or a motor actuation can only take place
between two simulation steps. For that reason the control step specified with
each `wb_robot_step()` must be a multiple of the simulation step. So for
example, if the simulation step is 16 ms, then the control step argument passed
to `wb_robot_step()` can be 16, 32, 64, 128, etc.

### Using Sensors and Actuators Together

Webots and each robot controller are executed in separate processes. For
example, if a simulation involves two robots, there will be three processes in
total: one for Webots and two for the two robots. Each controller process
exchanges sensors and actuators data with the Webots process during the calls to
`wb_robot_step()`. So for example, `wb_motor_set_position()` does not
immediately send the data to Webots. Instead it stores the data locally and the
data are effectively sent when `wb_robot_step()` is called.

For that reason the following code snippet is a bad example. Clearly, the value
specified with the first call to `wb_motor_set_position()` will be overwritten
by the second call: `wb_motor_set_position(my_leg, 0.34);  // BAD: ignored
wb_motor_set_position(my_leg, 0.56); wb_robot_step(40);`

Similarly this code does not make much sense either: `while (1) { double d1 =
wb_distance_sensor_get_value(ds1); double d2 =
wb_distance_sensor_get_value(ds1); if (d2 lt d1)   // WRONG: d2 will always
equal d1 here avoidCollision(); wb_robot_step(40); }` since there was no call to
`wb_robot_step()` between the two sensor readings, the values returned by the
sensor cannot have changed in the meantime. A working version would look like
this: `while (1) { double d1 = wb_distance_sensor_get_value(ds1);
wb_robot_step(40); double d2 = wb_distance_sensor_get_value(ds1); if (d2 lt d1)
avoidCollision(); wb_robot_step(40); }` However the generally recommended
approach is to have a single `wb_robot_step()` call in the main control loop,
and to use it to update all the sensors and actuators simultaneously, like this:
`while (1) { readSensors(); actuateMotors(); wb_robot_step(TIME_STEP); }` Note
that it may also be judicious to move `wb_robot_step()` to the beginning of the
loop, in order to make sure that the sensors already have valid values prior to
entering the `readSensors()` function. Otherwise the sensors will have undefined
values during the first iteration of the loop, hence: `while (1) {
wb_robot_step(TIME_STEP); readSensors(); actuateMotors(); }` Here is a complete
example of using sensors and actuators together. The robot used here is a
`DifferentialWheels` using differential steering. It uses two proximity sensors
(`DistanceSensor`) to detect obstacles. `#include ltwebots/robot.hgt #include
ltwebots/differential_wheels.hgt #include ltwebots/distance_sensor.hgt  #define
TIME_STEP 32  int main() { wb_robot_init();  WbDeviceTag left_sensor =
wb_robot_get_device("left_sensor"); WbDeviceTag right_sensor =
wb_robot_get_device("right_sensor"); wb_distance_sensor_enable(left_sensor,
TIME_STEP); wb_distance_sensor_enable(right_sensor, TIME_STEP);  while (1) {
wb_robot_step(TIME_STEP);  // read sensors double left_dist =
wb_distance_sensor_get_value(left_sensor); double right_dist =
wb_distance_sensor_get_value(right_sensor);  // compute behavior double left =
compute_left_speed(left_dist, right_dist); double right =
compute_right_speed(left_dist, right_dist);  // actuate wheel motors
wb_differential_wheels_set_speed(left, right); }  return 0; }`

### Using Controller Arguments

In the ".wbt" file, it is possible to specify arguments that are passed to a
controller when it starts. They are specified in the `controllerArgs` field of
the `Robot, Supervisor` or `DifferentialWheels` node, and they are passed as
parameters of the `main()` function. For example, this can be used to specify
parameters that vary for each robot's controller.

For example if we have: `Robot { ... controllerArgs "one two three" ... }` and
if the controller name is *"demo"*, then this sample controller code: `#include
ltwebots/robot.hgt #include ltstdio.hgt  int main(int argc, const char *argv[])
{ wb_robot_init();  int i; for (i = 0; i lt argc; i++) printf("argv[%i]=%s\n",
i, argv[i]);  return 0; }` will print: `argv[0]=demo argv[1]=one argv[2]=two
argv[3]=three `

### Controller Termination

Usually a controller process runs in an endless loop: it is terminated (killed)
by Webots when the user reverts (reloads) the simulation or quits Webots. The
controller cannot prevent its own termination but it can be notified shortly
before this happens. The `wb_robot_step()` function returns -1 when the process
is going to be terminated by Webots. Then the controller has 1 second (clock
time) to save important data, close files, etc. before it is effectively killed
by Webots. Here is an example that shows how to detect the upcoming termination:
`#include ltwebots/robot.hgt #include ltwebots/distance_sensor.hgt #include
ltstdio.hgt  #define TIME_STEP 32  int main() { wb_robot_init();  WbDeviceTag ds
= wb_robot_get_device("my_distance_sensor"); wb_distance_sensor_enable(ds,
TIME_STEP);  while (wb_robot_step(TIME_STEP) != -1) { double dist =
wb_distance_sensor_get_value(); printf("sensor value is %f\n", dist); }  //
Webots triggered termination detected!  saveExperimentData();
wb_robot_cleanup();  return 0; }` In some cases, it is up to the controller to
make the decision of terminating the simulation. For example in the case of
search and optimization algorithms: the search may terminate when a solution is
found or after a fixed number of iterations (or generations).

In this case the controller should just save the experiment results and quit by
returning from the `main()` function or by calling the `exit()` function. This
will terminate the controller process and freeze the simulation at the current
simulation step. The physics simulation and every robot involved in the
simulation will stop. `// freeze the whole simulation if (finished) {
saveExperimentData(); exit(0); }`

If only one robot controller needs to terminate but the simulation should
continue with the other robots, then the terminating robot should call
`wb_robot_cleanup()` right before quitting: `// terminate only this robot
controller if (finished) { saveExperimentsData(); wb_robot_cleanup(); exit(0);
}` Note that the exit status as well as the value returned by the `main()`
function are ignored by Webots.

### Shared libraries

Creating shared libraries can be very useful to share code between controllers
and/or plugins. There are several ways to do so, but we recommend to place them
into a subdirectory of the `libraries` directory of your project. Indeed the
environment variables of the controllers are modified to include these paths
into your [[DY]LD_LIBRARY_]PATH environment variable (depending on the OS).
Moreover the main Makefile (`WEBOTS_HOME/resources/Makefile.include`) used to
compile Webots controllers is able to create shared libraries and to link easily
with the Controller libraries, ODE or the Qt framework.

A good example of this is the Qt utility library located there:
`WEBOTS_HOME/resources/projects/libraries/qt_utils`

If for some reason shared libraries cannot be in the `libraries` directory, the
`WEBOTS_LIBRARY_PATH` environment variable will be very helpful. The paths it
contains will be added at the beginning of the library search
path([[DY]LD_LIBRARY_]PATH) when starting the controller.

### Environment variables

For some projects it will be necessary to define or change variables defined in
your environment. They can be changed in the settings of the computer but it may
last only for the current session or create conflict with other applications or
projects. Webots offers an elegant solution to this. A configuration file named
"runtime.ini" can be added to the controller directory. Any environment variable
defined in this file will be loaded to the environment each time the controller
starts.

This configuration file uses the standard INI template that is really simple and
easy to write and read. It contains pairs of key and value that can be inside
[sections]. Comments can be written on a line after using a semicolon ';'
character.

Environment variables in this file can contain references to other environment
variables using this syntax : `$(MY_VARIABLE_NAME)`. They will be automatically
replaced by the actual value already existing in the environment. The Webots
"runtime.ini" supports 7 sections:

Here is an example of a typical runtime.ini file. `       ; typical runtime.ini
[environment variables with relative paths] WEBOTS_LIBRARY_PATH =
lib:$(WEBOTS_LIBRARY_PATH):../../library  [environment variables] ROS_MASTER_URI
= http://localhost:11311  [environment variables for Windows]
NAOQI_LIBRARY_FOLDER = "bin;C:\Users\My Documents\Naoqi\bin"  [environment
variables for Mac OS X] NAOQI_LIBRARY_FOLDER = lib  [environment variables for
Linux] NAOQI_LIBRARY_FOLDER = lib`

### Languages settings

The "runtime.ini" file may also contain language specific sections, named
`[java]`, `[python]` and `[matlab]`. Each of this section may include two keys,
namely `COMMAND` and `OPTIONS`. The `COMMAND` key allows you to define a
specific version of the language interpreter whereas the `OPTIONS` key allows
you to specific options that will be passed immediately to the language
interpreter. For example:


``` c
       ; runtime.ini for a Python controller on Mac OS X

       [python]
       COMMAND = /opt/local/bin/python2.7
       OPTIONS = -m package.name.given
```

In the above example, the resulting command issued by Webots will be:
`/opt/local/bin/python2.7 -m package.name.given my_controller.py` possibly
followed by the value of the `controllerArgs` field of the corresponding `Robot`
node.


``` c
       ; runtime.ini for a Java controller on Windows

       [environment variables with relative paths]
       CLASSPATH = ../lib/MyLibrary.jar

       [java]
       COMMAND = javaw.exe
       OPTIONS = -Xms6144k
```

## Supervisor Programming

The programming examples provided here are in C, but same concepts apply to
C++/Java/Python/Matlab.

### Introduction

The `Supervisor` is a special kind of `Robot`. In object-oriented jargon we
would say that the `Supervisor` class *inherits* from the `Robot` class or that
the `Supervisor` class *extends* the `Robot` class. The important point is that
the `Supervisor` node offers the `wb_supervisor_*()` functions in addition to
the regular `wb_robot_*()` functions. These extra functions can only be invoked
from a controller program associated with a `Supervisor` node, not with a
`Robot` or a `DifferentialWheels` node. Note that Webots PRO is required to
create `Supervisor` nodes or use the `wb_supervisor_*()` functions.

In the Scene Tree, a `Supervisor` node can be used in the same context where a
`Robot` node is used, hence it can be used as a basis node to model a robot. But
in addition, the `wb_supervisor_*()` functions can also be used to control the
simulation process and modify the Scene Tree. For example the `Supervisor` can
replace human actions such as measuring the distance travelled by a robot or
moving it back to its initial position, etc. The `Supervisor` can also take a
screen shot or a video of the simulation, restart or terminate the simulation,
etc. It can read or modify the value of every fields in the Scene Tree, e.g.
read or change the position of robots, the color of objects, or switch on or off
the light sources, and do many other useful things.

One important thing to keep in mind is that the `Supervisor` functions
correspond to functionalities that are usually not available on real robots;
they rather correspond to a human intervention on the experimental setup. Hence,
the `Robot` vs. `Supervisor` distinction is intentional and aims at reminding
the user that `Supervisor` code may not be easily transposed to real robots.

Now let's examine a few examples of `Supervisor` code.

### Tracking the Position of Robots

The `Supervisor` is frequently used to record robots trajectories. Of course, a
robot can find its position using a GPS, but when it is necessary to keep track
of several robots simultaneously and in a centralized way, it is much simpler to
use a `Supervisor`.

The following `Supervisor` code shows how to keep track of a single robot, but
this can easily be transposed to an arbitrary number of robots. This example
code finds a `WbNodeRef` that corresponds to the robot node and then a
`WbFieldRef` that corresponds to the robot's `translation` field. At each
iteration it reads and prints the field's values. `#include ltwebots/robot.hgt
#include ltwebots/supervisor.hgt #include ltstdio.hgt  int main() {
wb_robot_init();  // do this once only WbNodeRef robot_node =
wb_supervisor_node_get_from_def("MY_ROBOT"); WbFieldRef trans_field =
wb_supervisor_node_get_field(robot_node, "translation");  while (1) { // this is
done repeatedly const double *trans =
wb_supervisor_field_get_sf_vec3f(trans_field); printf("MY_ROBOT is at position:
%g %g %g\n", trans[0], trans[1], trans[2]); wb_robot_step(32); }  return 0; }`
Note that a `Supervisor` controller must include the `supervisor.h` header file
in addition to the `robot.h` header file. Otherwise the `Supervisor` works like
a regular `Robot` controller and everything that was explained in the
"Controller Programming" section does also apply to "Supervisor Programming".

As illustrated by the example, it is better to get the `WbNodeRef`s and
`WbFieldRef`s only once, at the beginning of the simulation (keeping the
invariants out of the loop). The call to `wb_supervisor_node_get_from_def()`
searches for an object named "MY_ROBOT" in the Scene Tree. Note that the name in
question is the DEF name of the object, not the name field which is used to
identify devices. The function returns a `WbNodeRef` which is an opaque and
unique reference to the corresponding Scene Tree node. Then the call to
`wb_supervisor_node_get_field()` finds a `WbFieldRef` in the specified node. The
"translation" field represents the robot's position in the global (world)
coordinate system.

In the `while` loop, the call to `wb_supervisor_field_get_sf_vec3f()` is used to
read the latest values of the specified field. Note that, unlike sensor or
actuator functions, the `wb_supervisor_field_*()` functions are executed
immediately: their execution is not postponed to the next `wb_robot_step()`
call.

### Setting the Position of Robots

Now let's examine a more sophisticated `Supervisor` example. In this example we
seek to optimize the locomotion of a robot: it should walk as far as possible.
Suppose that the robot's locomotion depends on two parameters (a and b), hence
we have a two-dimensional search space.

In the code, the evaluation of the a and b parameters is carried out in the the
`while` loop. The `actuateMotors()` function here is assumed to call
`wb_motor_set_postion()` for each motor involved in the locomotion. After each
evaluation the distance travelled by the robot is measured and logged. Then the
robot is moved (translation) back to its initial position (0, 0.5, 0) for the
next evaluation. To move the robot we need the `wb_supervisor_*()` functions and
hence the base node of this robot in the Scene Tree must be a `Supervisor` and
not a Robot. `#include ltwebots/robot.hgt #include ltwebots/supervisor.hgt
#include ltstdio.hgt #include ltmath.hgt  #define TIME_STEP 32  int main() {
wb_robot_init();  // get handle to robot's translation field WbNodeRef
robot_node = wb_supervisor_node_get_from_def("MY_ROBOT"); WbFieldRef trans_field
= wb_supervisor_node_get_field(robot_node, "translation");  double a, b, t; for
(a = 0.0; a lt 5.0; a += 0.2) { for (b = 0.0; b lt 10.0; b += 0.3) { // evaluate
robot during 60 seconds (simulation time) for (t = 0.0; t lt 60.0; t +=
TIME_STEP / 1000.0) { actuateMotors(a, b, t); wb_robot_step(TIME_STEP); }  //
compute travelled distance const double *pos =
wb_supervisor_field_get_sf_vec3f(trans_field); double dist = sqrt(pos[0] *
pos[0] + pos[2] * pos[2]); printf("a=%g, b=%g -> dist=%g\n", a, b, dist);  //
reset robot position const double INITIAL[3] = { 0, 0.5, 0 };
wb_supervisor_field_set_sf_vec3f(trans_field, INITIAL); } }  return 0; }` As in
the previous example, the `trans_field` variable is a `WbFieldRef` that
identifies the `translation` field of the robot. In this example the
`trans_field` is used both for getting (`wb_supervisor_field_get_sf_vec3f()`)
and for setting (`wb_supervisor_field_set_sf_vec3f`) the field's value.

Please note that the program structure is composed of three nested `for` loops.
The two outer loops change the values of the a and b parameters. The innermost
loop makes the robot walk during 60 seconds. One important point here is that
the call to `wb_robot_step()` is placed in the innermost loop. This allows the
motor positions to be updated at each iteration of the loop. If
`wb_robot_step()` was placed anywhere else, this would not work.

## Using Numerical Optimization Methods

### Choosing the correct Supervisor approach

There are several approaches to using optimization algorithms in Webots. Most
approaches need a `Supervisor` and hence Webots PRO is usually required.

A numerical optimization can usually be decomposed in two separate tasks:

One of the important things that needs to be decided is whether the
implementation of these two distinct tasks should go into the same controller or
in two separate controllers. Let's discuss both approaches:

#### Using a single controller

If your simulation needs to evaluate only one robot at a time, e.g. you are
optimizing the locomotion gait of a humanoid or the behavior of a single robot,
then it is possible to have both tasks implemented in the same controller; this
results in a somewhat simpler code. Here is a pseudo-code example for the
systematical optimization of two parameters *a* and *b* using only one
controller: `#include ltwebots/robot.hgt #include ltwebots/supervisor.hgt
#define TIME_STEP 5  int main() { wb_robot_init(); double a, b, time; for (a =
0.5; a lt 10.0; a += 0.1) { for (b = 0.1; b lt 5.0; b += 0.5) { resetRobot();
// move robot to initial position  // run robot simulation for 30 seconds for
(time = 0.0; time lt 30.0; time += TIME_STEP / 1000.0) { actuateMotors(a, b,
time); wb_robot_step(TIME_STEP); }  // compute and print fitness double fitness
= computeFitness(); printf("with parameters: %g %g, fitness was: %g\n", a, b,
fitness); } }  wb_robot_cleanup(); return 0; } ` In this example the robot runs
for 30 simulated seconds and then the fitness is evaluated and the robot is
moved back to it initial position. Note that this controller needs to be
executed in a `Supervisor` in order to access the `wb_supervisor_field_*()`
functions that are necessary to read and reset the robot's position. So when
using this approach, the robot must be based on a `Supervisor` node in the Scene
Tree. Note that this approach is not suitable to optimize a `DifferentialWheels`
robot, because due to the class hierarchy, a robot cannot be a
`DifferentialWheels` and a `Supervisor` at the same time.

#### Using two distinct types of controllers

If, on the contrary, your simulation requires the simultaneous execution of
several robots, e.g. swarm robotics, or if your robot is a `DifferentialWheels`,
then it is advised to use two distinct types of controller: one for the
optimization algorithm and one for the robot's behavior. The optimization
algorithm should go in a `Supervisor` controller while the robots' behavior can
go in a regular (non-Supervisor) controller.

Because these controllers will run in separate system processes, they will not
be able to access each other's variables. Though, they will have to communicate
by some other means in order to specify the sets of parameters that need to be
evaluated. It is possible, and recommended, to use Webots `Emitter`s and
`Receiver`s to exchange information between the `Supervisor` and the other
controllers. For example, in a typical scenario, the `Supervisor` will send
evaluation parameters (e.g., genotype) to the robot controllers. The robot
controllers listen to their `Receiver`s, waiting for a new set of parameters.
Upon receipt, a robot controller starts executing the behavior specified by the
set of parameters. In this scenario, the `Supervisor` needs an `Emitter` and
each individual robot needs a `Receiver`.

Depending on the algorithms needs, the fitness could be evaluated either in the
`Supervisor` or in the individual robot controllers. In the case it is evaluated
in the robot controller then the fitness result needs to be sent back to the
`Supervisor`. This bidirectional type of communication requires the usage of
additional `Emitter`s and `Receiver`s.

### Resetting the robot

When using optimization algorithm, you will probably need to reset the robot
after or before each fitness evaluation. There are several approaches to
resetting the robot:

#### Using the wb_supervisor_field_set_*() and wb_supervisor_simulation_reset_physics() functions

You can easily reset the position, orientation and physics of the robot using
the `wb_supervisor_field_set...()` and
`wb_supervisor_simulation_reset_physics()` functions, here is an example: `//
get handles to the robot's translation and rotation fields WbNodeRef robot_node
= wb_supervisor_node_get_from_def("MY_ROBOT"); WbFieldRef trans_field =
wb_supervisor_node_get_field(robot_node, "translation"); WbFieldRef rot_field =
wb_supervisor_node_get_field(robot_node, "rotation");  // reset the robot const
double INITIAL_TRANS[3] = { 0, 0.5, 0 }; const double INITIAL_ROT[4] = { 0, 1,
0, 1.5708 }; wb_supervisor_field_set_sf_vec3f(trans_field, INITIAL_TRANS);
wb_supervisor_field_set_sf_rotation(rot_field, INITIAL_ROT);
wb_supervisor_simulation_reset_physics();` The drawback with the above method is
that it only resets the robot's main position and orientation. This may be fine
for some types of optimization, but insufficient for others. Although it is
possible to add more parameters to the set of data to be reset, it is sometimes
difficult to reset everything. Neither motor positions, nor the robot
controller(s) are reset this way. The motor positions should be reset using the
`wb_motor_set_position()` and the robot controller should be reset by sending a
message from the supervisor process to the robot controller process (using
Webots `Emitter` / `Receiver` communication system). The robot controller
program should be able to handle such a message and reset its state accordingly.

#### Using the wb_supervisor_simulation_revert() function

This function restarts the physics simulation and all controllers from the very
beginning. With this method, everything is reset, including the physics and the
motor positions and the controllers. But this function does also restart the
controller that called `wb_supervisor_simulation_revert()`, this is usually the
controller that runs the optimization algorithm, and as a consequence the
optimization state is lost. Hence for using this technique, it is necessary to
develop functions that can save and restore the complete state of the
optimization algorithm. The optimization state should be saved before calling
`wb_supervisor_simulation_revert()` and reloaded when the `Supervisor`
controller restarts. Here is a pseudo-code example: `#include ltwebots/robot.hgt
#include ltwebots/supervisor.hgt  void run_robot(const double params[]) {
read_sensors(params); compute_behavior(params): actuate_motors(params); }  void
evaluate_next_robot() { const double *params = optimizer_get_next_parameters();
... // run robot for 30 seconds double time; for (time = 0.0; time lt 30.0; time
+= TIME_STEP / 1000.0) { run_robot(params); wb_robot_step(TIME_STEP); } ... //
compute and store fitness double fitness = compute_fitness();
optimizer_set_fitness(fitness); ... // save complete optimization state to a
file optimizer_save_state("my_state_file.txt"); ... // start next evaluation
wb_supervisor_simulation_revert(); wb_robot_step(TIME_STEP); exit(0); }  int
main() { wb_robot_init(); ... // reload complete optimization state
optimizer_load_state("my_state_file.txt"); ... if
(optimizer_has_more_parameters()) evaluate_next_robot(); ... wb_robot_cleanup();
return 0; }` If this technique is used with Genetic Algorithms for example, then
the function `optimizer_save_state()` should save at least all the genotypes and
fitness results of the current GA population. If this technique is used with
Particle Swarm Optimization, then the `optimizer_save_state()` function should
at least save the position, velocity and fitness of all particles currently in
the swarm.

#### By starting and quitting Webots

Finally, the last method is to start and quit the Webots program for each
parameter evaluation. This may sound like an overhead, but in fact Webots
startup time is usually very short compared to the time necessary to evaluate a
controller, so this approach makes perfectly sense.

For example, Webots can be called from a shell script or from any type of
program suitable for running the optimization algorithm. Starting Webots each
time does clearly revert the simulation completely, so each robot will start
from the same initial state. The drawback of this method is that the
optimization algorithm has to be programmed outside of Webots. This external
program can be written in any programming language, e.g. shell script, C, PHP,
perl, etc., provided that there is a way to call webots and wait for its
termination, e.g. like the C standard `system()` does. On the contrary, the
parameter evaluation must be implemented in a Webots controller.

With this approach, the optimization algorithm and the robot controller(s) run
in separate system processes, but they must communicate with each other in order
to exchange parameter sets and fitness results. One simple way is to make them
communicate by using text files. For example, the optimization algorithm can
write the genotypes values into a text file then call Webots. When Webots
starts, the robot controller reads the genotype file and carries out the
parameter evaluation. When the robot controller finishes the evaluation, it
writes the fitness result into another text file and then it calls the
`wb_supervisor_simulation_quit()` function to terminate Webots. Then the control
flow returns to the optimization program that can read the resulting fitness,
associate it with the current genotype and proceed with the next genotype.

Here is a possible (pseudo-code) implementation for the robot evaluation
controller: `#include ltwebots/robot.hgt #include ltwebots/supervisor.hgt
#define TIME_STEP 10  double genotype[GENOME_SIZE];  int main() {
wb_robot_init(); ... genotype_read("genotype.txt", genotype); ... // run
evaluation for 30 seconds for (double time = 0.0; time lt 30.0; time +=
TIME_STEP / 1000.0) { read_sensors(genotype); actuate_motors(time, genotype);
wb_robot_step(TIME_STEP); } ... double fitness = compute_fitness();
fitness_save(fitness, "fitness.txt"); ... wb_supervisor_simulation_quit();
wb_robot_step(TIME_STEP); return 0; }`

You will find complete examples of simulations using optimization techniques in
Webots distribution: look for the worlds called
"advanced_particle_swarm_optimization.wbt" and "advanced_genetic_algorithm.wbt"
located in the "WEBOTS_MODULES_PATH/projects/samples/curriculum/worlds"
directory. These examples are described in the *Advanced Programming Exercises*
of `Cyberbotics' Robot Curriculum`.

## C++/Java/Python

This section explains the main differences between the C API and the
C++/Java/Python APIs.

### Classes and Methods

C++, Java and Python are object-oriented programming languages and therefore the
corresponding Webots APIs are organized in classes. The class hierarchy is built
on top of the C API and currently contains about 25 classes and 200 methods
(functions).

The Java and Python APIs are automatically generated from the C++ API using
SWIG. Therefore the class and method names, as well as the number of parameters
and their types, are very similar in these three languages.

![Webots APIs Overview](pdf/api_overview.pdf)
**Webots APIs Overview**

The naming convention of the C++/Java/Python classes and methods directly
matches the C API function names. For example, for this C function: `double
wb_distance_sensor_get_value(WbDeviceTag tag)` there will be a matching
C++/Java/Python method called `getValue()` located in a class called
`DistanceSensor`. Usually the C++/Java/Python methods have the same parameters
as their C API counterparts, but without the `WbDeviceTag` parameter.

### Controller Class

The C++/Java/Python controller implementation should be placed in a user-defined
class derived from one of the Webots class: `Robot, DifferentialWheels` or
`Supervisor`. It is important that the controller class is derived from the same
class as that used in Scene Tree, otherwise some methods may not be available or
may not work. For example, if in the Scene Tree a robot is of type
`DifferentialWheels`, then the corresponding C++/Java/Python controller class
must extend the `DifferentialWheels` class. If in the Scene Tree a robot is of
type `Supervisor`, then the C++/Java/Python controller class must be derived
from the `Supervisor` class, etc.

As you can see in , both `DifferentialWheels` and `Supervisor` are subclasses of
the `Robot` class. Hence it is possible to call the `Robot`'s methods, such as,
e.g., `step()` or `getLED()`, from the `DifferentialWheels` and `Supervisor`
controllers. But it is not possible to call the `Supervisor` methods from a
`DifferentialWheels` controller, and vice versa. For example it won't be
possible to call `simulationRevert()` from a `DifferentialWheels` controller.

![A small subset of Webots oriented-object APIs](pdf/oo_api.pdf)
**A small subset of Webots oriented-object APIs**

Generally, the user-defined controller class should have a `run()` function that
implements the main controller loop. That loop should contains a call to the
`Robot`'s `step()` method. Then the only responsibility of the controller's
`main()` function is to create an instance of the user-defined controller class,
call its `run()` method and finally delete (C++ only) the instance: see examples
below. Note that the controller should never create more than one instance of a
derived class, otherwise the results are undefined.

Note that unlike the C API, the C++/Java/Python APIs don't have (and don't need)
functions like `wb_robot_init()` and `wb_robot_cleanup()`. The necessary
initialization and cleanup routines are automatically invoked from the
constructor and destructor of the base class.

In C++/Java/Python, each Webots device is implemented as a separate class, there
is a `DistanceSensor` class, a `TouchSensor` class, a `RotationalMotor` class,
etc. The various devices instances can be obtained with dedicated methods of the
`Robot` class, like `getDistanceSensor(), getTouchSensor()`, etc. There is no
`WbDeviceTag` in C++/Java/Python.

### C++ Example

`#include ltwebots/Robot.hppgt #include ltwebots/LED.hppgt #include
ltwebots/DistanceSensor.hppgt  using namespace webots;  #define TIME_STEP 32
class MyRobot : public Robot { private: LED *led; DistanceSensor
*distanceSensor;  public: MyRobot() : Robot() { led = getLED("ledName");
distanceSensor = getDistanceSensor("distanceSensorName");
distanceSensor->enable(TIME_STEP); }  virtual ~MyRobot() { // Enter here exit
cleanup code }  void run() { // Main control loop while (step(TIME_STEP) != -1)
{ // Read the sensors double val = distanceSensor->getValue();  // Process
sensor data here  // Enter here functions to send actuator commands led->set(1);
} } };  int main(int argc, char **argv) { MyRobot *robot = new MyRobot();
robot->run(); delete robot; return 0; }`

### Java Example

`import com.cyberbotics.webots.controller.*;  public class MyRobot extends Robot
{ private LED led; private DistanceSensor distanceSensor; private static final
int TIME_STEP = 32;  // milliseconds  public MyRobot() { super(); led =
getLED("my_led"); distanceSensor = getDistanceSensor("my_distance_sensor");
distanceSensor.enable(TIME_STEP); }  public void run() { // main control loop
while (step(TIME_STEP) != -1) { // Read the sensors, like: double val =
distanceSensor.getValue();  // Process sensor data here  // Enter here functions
to send actuator commands, like: led.set(1); }  // Enter here exit cleanup code
}  public static void main(String[] args) { MyRobot robot = new MyRobot();
robot.run(); } }`

### Python Example

`from controller import *  class MyRobot (Robot): def run(self): led =
self.getLed('ledName') distanceSensor =
self.getDistanceSensor('distanceSensorName') distanceSensor.enable(32)  while
(self.step(32) != -1): # Read the sensors, like: val = distanceSensor.getValue()
# Process sensor data here  # Enter here functions to send actuator commands,
like: led.set(1)  # Enter here exit cleanup code  robot = MyRobot() robot.run()`

## Matlab

The `MATLAB` API for Webots is very similar to the C API. The functions names
are identical, only the type and number of parameters differs slightly in some
cases. The `MATLAB` functions and prototypes are described in Webots Reference
Manual. Note that unlike with the C API, there are no `wb_robot_init()` and
`wb_robot_cleanup()` functions in the `MATLAB`  API. The necessary
initialization and cleanup are automatically carried out respectively before
entering and after leaving the controller code.

If the `MATLAB` code uses graphics, it is necessary to call the `drawnow`
command somewhere in the control loop in order to flush the graphics.

Here is a simple `MATLAB` controller example: `% uncomment the next two lines to
use the `

### Using the 

In order to avoid cluttering the desktop with too many windows, Webots starts
`MATLAB` with the *-nodesktop* option. The *-nodesktop* option starts `MATLAB`
without user interface and therefore it keeps the memory usage low which is
useful in particular for multi-robot experiments. If you would like to use the
`MATLAB` desktop to interact with your controller you just need to add these two
`MATLAB` commands somewhere at the beginning of your controller m-file:


```
desktop;
keyboard;
```

The `desktop` command brings up the `MATLAB` desktop. The `keyboard` stops the
execution of the controller and gives control to the keyboard (`Kgtgt` prompt).
Then `MATLAB` opens your controller m-file in its editor and indicates that the
execution is stopped at the `keyboard` command. After that, the controller
m-file can be debugged interactively, i.e., it is possible to continue the
execution step-by-step, set break points, watch variable, etc. While debugging,
the current values of the controller variables are shown in the `MATLAB`
workspace. It is possible to *continue* the execution of the controller by
typing `return` at the `Kgtgt` prompt. Finally the execution of the controller
can be terminated with `Ctrl-C` key combination.

Once the controller is terminated, the connection with Webots remains active.
Therefore it becomes possible to issue Webots commands directly at the `MATLAB`
prompt, for example you can interactively issue commands to query the sensors,
etc.:


```
gtgt wb_differential_wheels_set_speed(600, 600);
gtgt wb_robot_step(1000);
gtgt wb_gps_get_values(gps)

ans =

    0.0001    0.0030   -0.6425
gtgt |
```

It is possible to use additional `keyboard` statements in various places in your
".m" controller. So each time `MATLAB` will run into a `keyboard` statement, it
will return control to the `Kgtgt` prompt where you will be able to debug
interactively.

At this point, it is also possible to restart the controller by calling its
m-file from `MATLAB` prompt. Note that this will restart the controller only,
not the whole simulation, so the current robot and motor positions will be
preserved. If you want to restart the whole simulation you need to use the
`Revert` button as usual.

## Controller Plugin

The controller functionality can be extended with user-implemented plugins. The
purpose of a controller plugin is to facilitate the programming of robot-
specific robot windows and remote-control wrappers.

Programming controller plugins rather than programming directly in the
controller is more convenient because it increases considerably the modularity
and the scalability of the code. For example a robot window can be used for
several robots.

### Fundamentals

Whatever its language, a controller executable is linked with the Webots
controller library (libController) at startup. A controller plugin is a shared
library loaded dynamically (at runtime) by libController after a specific event
depending on its type.

The  shows an overview of the controller plugin system. In this figure, the
dashed arrows shows how the shared libraries are loaded, and the large dash
lines represents an Inter-Process Communication (IPC). The IPC between
libController and Webots is a pipe (On Windows this is a named pipe, and
otherwise a local domain socket). The IPC between libRemoteControl and the real
robot is defined by the user (TCP/IP, Serial, etc.).

The system has been designed as follow. Every entities (the controller, the
remote control library and the robot window library) should only call the
libController interface (Webots API) functions. The controller should not be
aware of its robot window and its real robot for modularity reasons. The only
exception is about the robot window library which can be aware of the remote
control library to initialise and monitor it. This can be done trough the
libController API through the `wb_robot_get_mode()`, `wb_robot_set_mode()` and
the `wb_remote_control_custom_function()` functions. Of course these rules can
be easily broken because every entities runs into the same process. However we
recommend to respect them to get a good design.

The controller plugins have been designed to be written in C/C++, because the
result should be a dynamic library. However it's certainly possible to write
them in other languages using a C/C++ wrapper inbetween.

After its loading, some controller plugin functions (entry points) are called by
libController. A set of entry points have to be defined to let the controller
plugin work smoothly. Some of these entry points are required and some are
optional.

The `Robot` node defines the location of the controller plugin through its
*robotWindow* and its *remoteControl* fields (cf. reference manual)

The controller plugin run in the main thread of the process (also known as GUI
thread): the same as the controller executable. This implies that if an entry
point of a plugin is blocking, the controller will also be blocked. And if the
plugin crashes, the controller is also crashed.

The search algorithm to convert the *robotWindow* and the *remoteControl* to an
existing path is explained in the reference manual.

Each distributed shared library is built thanks to the main Makefile (the same
as the one used to build the controllers):
`WEBOTS_HOME/resources/Makefile.include`

![Controller plugin overview](pdf/controller_plugin.pdf)
**Controller plugin overview**

### Robot Window Plugin

A robot window plugin allows the programmer to efficiently create custom robot
windows. Robot windows can be opened by double-clicking on the virtual robot, or
by selecting the `Robot | Show Robot Window` menu item.

The *robotWindow* field of the `Robot` node specifies a robot window (cf.
documentation in the reference manual).

The entry points of a robot window controller plugin are:

The internal behavior of the `wb_robot_step()` call is the key point to
understand how the different entry points of the robot window plugin are called
(pseudo-code):


``` c
wb_robot_step() {
  wbw_write_actuators()
  wbw_pre_update_gui()
  write_request_to_webots_pipe()
  wbw_update_gui() // returns when something on the pipe
  read_request_to_webots_pipe()
  wbw_read_sensors()
}
```

As the Qt libraries are included in Webots (used by the Webots GUI), and all our
samples are based on it, we recommend to choose also this framework to create
your GUI. The `Makefile.include` mentioned above allows you to efficiently link
with the Qt framework embedded in Webots.

The Webots pipe handle (integer id) is available in the WEBOTS_PIPE_IN
environment variable.

The Qt utility library helps you to initialize Qt correctly (pipe, window
visibility, ...). Refer to the next section for more information related with
this library.

If the robot window cannot be loaded (bad path, bad initialization, etc.), a
generic robot window is opened instead. This generic robot window displays
several sensors and actuators. The source code of this robot window is a good
demonstrator of the robot window plugin abilities. All the source code is
located there:
`WEBOTS_HOME/resources/projects/plugins/robot_windows/generic_window`

Other samples can be found:

`WEBOTS_MODULES_PATH/projects/robots/e-puck/plugins/robot_windows/botstudio`

`WEBOTS_MODULES_PATH/projects/robots/e-puck/plugins/robot_windows/e-puck_window`

### Qt utility library

In order to facilitate the creation of robot window plugins using the Qt
framework, Webots has a utility library allowing to hide the complexity of the
management of the robot windows.

This library contains various classes including a subclass of QMainApplication
managing the pipe events, a subclass of QMainWindow dealing with the close
events, a class to handle Webots standard paths, and a collection of widgets to
display the Webots devices. The source code of the generic robot window is a
good example illustrating how to use this library.

The location of the qt utility library is
`WEBOTS_HOME/resources/projects/libraries/qt_utils`


### Motion editor

A motion is a chronological sequence of robot poses. A pose is defined by a set
of commands (in position) of the robot motors.

The motion is stored in a motion file in a user-readable format. The controller
API allows to play easily the motion files on your robot. You can get the
complete motion API in the reference manual.

The motion editor (cf. the ) is a GUI helping to create motions which can be
played by a robot. It is implemented in the Qt utils library, and is embedded
inside the generic robot window plugin. This implies that the motion editor is
accessible only if the robot is linked (cf. the Robot::robotWindow field) with
either the generic window, or on a window using the Qt utils library's
corresponding widget.

In the motion editor different fonts and colors are used to identify the status
of poses and motor states: modified items are displayed using bold font,
disabled states are written in gray, and items with values outside the valid
motor position range are written in red.

![Motion editor view](png/motion_editor.png)
**Motion editor view**

### Remote-control Plugin

A remote-control plugin allow to simply and efficiently create an interface
using the Webots API to communicate with a real robot. The main purpose of a
remote-control library is to wrap all the Webots API functions used by the robot
with a protocol communicating to the real robot. Generally, a program (client)
runs on the real robot, and decodes the communication protocol to dialog with
the real robot devices.

The remote-control library is initialized when an entity calls the
`wb_robot_set_mode()` libController function. This entity is typically
libRobotWindow, because it's quite convenient to use the GUI to initialize the
communication (i.e. entering the IP address of the robot, etc.)

There are two entry points to the remote-control library:

The `WbrInterface` structure has several functions (mandatory) which have to be
mapped to let the remote-control library run smoothly. Here they are:

As said above, all the Webots API functionalities that should work with the real
robot have to be wrapped into the remote-control library. To achieve this:

The complete definition of the remote control API and of the `WbrInterface`
structure is contained in
`WEBOTS_HOME/include/controller/c/webots/remote_control.h`

For example, if you want to be able to use the distance sensor of the real
robot, you have to wrap the `wbr_set_refresh_rate()` function (to set the
internal state of the remote control library to read this distance sensor only
when required), and to call `wbr_distance_sensor_set_value()` into the remote-
control library when the distance sensor is refreshed (typically into the
`wbr_robot_step()` function).

A complete sample (communicating with the e-puck robot using bluetooth) can be
found in this directory:

`WEBOTS_MODULES_PATH/projects/robots/e-puck/plugins/remote_controls/e-puck_bluet
ooth`

## Webots Plugin

Webots functionality can be extended with user-implemented plugins.

### Physics Plugin

A *physics* plugin offers the possibility to add custom ODE instructions to the
default physics behavior of Webots. For instance it is possible to add or
measure forces. By adding forces, it is possible to simulate new types of
environments or devices. For example, a wind can be simulated as a constant
unidirectional force applied to each object in the world and proportional to the
size of the object. The reactor of an airplane can be simulated by adding a
force of varying intensity, etc.

Webots distribution comes with some implementations and usage examples for these
plugins. You will find more info on this topic in Webots Reference Manual.

