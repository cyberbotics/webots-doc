## Tutorial 4: More about Controllers (20 minutes)

Now we start to tackle the topics related to programming robot controllers. We
will design a simple controller that avoids the obstacles created in the
previous tutorials.

This tutorial will introduce you to the basics of robot programming in Webots.
At the end of this chapter, you should understand what is the link between the
scene tree nodes and the controller API, how the robot controller has to be
initialized and cleaned up, how to initialize the robot devices, how to get the
sensor values, how to command the actuators, and how to program a simple
feedback loop.

This chapter only addresses the correct usage of Webots functions. The study of
robotics algorithms is beyond the goals of this tutorial and so it won't be
addressed here. Some rudimentary programming knowledge is required to tackle
this chapter (any C tutorial should be a sufficient introduction). At the end of
the chapter, links to further robotics algorithmics are given.

### New World and new Controller

> **hands on**:
Save the previous world as "collision\_avoidance.wbt".

<!-- -->

> **hands on**:
Create a new C controller called "e-puck\_avoid\_collision" using the wizard.
Modify the `controller` field of the E-puck node in order to link it to the new
controller.

### Understand the e-puck Model

Controller programming requires some information related to the e-puck model.
in order to create the collision avoidance algorithm, we need to read the values of its 8
infra-red distance sensors located around its turret, and we need to actuate its
two wheels. The way that the distance sensors are distributed around the turret
and the e-puck direction are depicted in [this
figure](#top-view-of-the-e-puck-model-the-green-arrow-indicates-the-front-of-the-robot-the-red-lines-represent-the-directions-of-the-infrared-distance-sensors-the-string-labels-corresponds-to-the-distance-sensor-names).

The distance sensors are modeled by 8 DistanceSensor nodes in the hierarchy of
the robot. These nodes are referenced by their `name` fields (from "ps0" to
"ps7"). We will explain later how these nodes are defined. For now, simply note
that a DistanceSensor node can be accessed through the related module of the
Webots API (through the "webots/distance\_sensor.h" include file). The values
returned by the distance sensors are scaled between 0 and 4096 (piecewise
linearly to the distance). While 4096 means that a big amount of light is
measured (an obstacle is close) and 0 means that no light is measured (no
obstacle).

In the same way, the e-puck root node is a DifferentialWheel node and can be
accessed by the "webots/differential\_wheel.h" include-file. The speed is given in
a number of ticks/seconds where 1000 ticks correspond to a complete rotation of
the wheel. The values are clamped between -1000 and 1000.

> **Theory**:
The **controller API** is the programming interface that gives you access to the
simulated sensors and actuators of the robot. For example, including the
"webots/distance\_sensor.h" file allows to use the `wb_distance_sensor_*()`
functions and with these functions you can query the values of the
DistanceSensor nodes. The documentation on the API functions can be found in
Chapter 3 of the `Reference Manual` together with the description of each node.

%figure "Top view of the e-puck model. The green arrow indicates the front of the robot. The red lines represent the directions of the infrared distance sensors. The string labels corresponds to the distance sensor names."

![tutorial_e-puck_top_view.png](images/tutorial_e-puck_top_view.png)

%end

%figure "UML state machine of a simple feedback loop"

![tutorial_feedback_loop.png](images/tutorial_feedback_loop.png)

%end

### Program a Controller

We would like to program a very simple collision avoidance behavior. You will
program the robot to go forwards until an obstacle is detected by the front
distance sensors, and then to turn towards the obstacle-free direction. In order to
do that, we will use the simple feedback loop depicted in the UML state
machine in [this figure](#uml-state-machine-of-a-simple-feedback-loop).

The complete code of this controller is given in the next subsection.

> **hands on**:
At the beginning of the controller file, add the include directives
corresponding to the Robot, the DifferentialWheels and the DistanceSensor nodes
in order to be able to use the corresponding API (documented in chapter 3 of the
`Reference Manual`):

> ```c
> #include <webots/robot.h>
> #include <webots/differential_wheels.h>
> #include <webots/distance_sensor.h>
> ```

<!-- -->

> **hands on**:
Just after including the statements add a macro that defines the duration of each
physics step. This macro will be used as argument to the `wb_robot_step()`
function, and it will also be used to enable the devices. This duration is
specified in milliseconds and it must be a multiple of the value in the
`basicTimeStep` field of the WorldInfo node.

> ```c
> #define TIME_STEP 64
> ```

<!-- -->

> **Theory**:
The function called `main()` is where the controller program starts execution.
The arguments passed to main() are given by the `controllerArgs` field of the
Robot node. The Webots API has to be initialized using the `wb_robot_init()`
function and it has to be cleaned up using the `wb_robot_cleanup()` function.

<!-- -->

> **hands on**:
Write the prototype of the `main()` function as follows:

> ```c
> // entry point of the controller
> int main(int argc, char **argv)
> {
>   // initialize the Webots API
>   wb_robot_init();
>   // initialize devices
>   // feedback loop
>   while (1) {
>     // step simulation
>     int delay = wb_robot_step(TIME_STEP);
>     if (delay == -1) // exit event from webots
>       break;
>     // read sensors outputs
>     // process behavior
>     // write actuators inputs
>   }
>   // cleanup the Webots API
>   wb_robot_cleanup();
>   return 0; //EXIT_SUCCESS
> }
> ```

<!-- -->

> **Theory**:
A robot device is referenced by a `WbDeviceTag`. The `WbDeviceTag` is retrieved
by the `wb_robot_get_device()` function. Then it is used as first argument in
every function call concerning this device.

> A sensor such as the DistanceSensor has to be enabled before use. The second
argument of the enable function defines at which rate the sensor will be
refreshed.

<!-- -->

> **hands on**:
Just after the comment *"// initialize devices"*, get and enable the distance
sensors as follows:

> ```c
> // initialize devices
> int i;
> WbDeviceTag ps[8];
> char ps_names[8][4] = {
>   "ps0", "ps1", "ps2", "ps3",
>   "ps4", "ps5", "ps6", "ps7"
> };
>
> for (i=0; i<8; i++) {
>   ps[i] = wb_robot_get_device(ps_names[i]);
>   wb_distance_sensor_enable(ps[i], TIME_STEP);
> }
> ```

<!-- -->

> **hands on**:
In the main loop, just after the comment *"// read sensors outputs"*, read the
distance sensor values as follows:

> ```c
> // read sensors outputs
> double ps_values[8];
> for (i=0; i<8 ; i++)
>   ps_values[i] = wb_distance_sensor_get_value(ps[i]);
> ```

<!-- -->

> **hands on**:
In the main loop, just after the comment *"// process behavior"*, detect if a
collision occurs (i.e. the value returned by a distance sensor is bigger than a
threshold) as follows:

> ```c
> // detect obstacles
> bool left_obstacle =
>   ps_values[0] > 100.0 ||
>   ps_values[1] > 100.0 ||
>   ps_values[2] > 100.0;
> bool right_obstacle =
>   ps_values[5] > 100.0 ||
>   ps_values[6] > 100.0 ||
>   ps_values[7] > 100.0;
> ```

<!-- -->

> **hands on**:
Finally, use the information about the obstacle to actuate the wheels as
follows:

> ```c
> // init speeds
> double left_speed  = 500;
> double right_speed = 500;
> // modify speeds according to obstacles
> if (left_obstacle) {
>   // turn right
>   left_speed  -= 500;
>   right_speed += 500;
> }
> else if (right_obstacle) {
>   // turn left
>   left_speed  += 500;
>   right_speed -= 500;
> }
> // write actuators inputs
> wb_differential_wheels_set_speed(left_speed, right_speed);
> ```

<!-- -->

> **hands on**:
Compile your code by selecting the `Build / Build` menu item. Compilation errors
are displayed in red in the console. If there are any, fix them and retry to
compile. Revert the simulation.

### The Controller Code

Here is the complete code of the controller detailed in the previous subsection.

```c
#include <webots/robot.h>
#include <webots/differential_wheels.h>
#include <webots/distance_sensor.h>

// time in [ms] of a simulation step
#define TIME_STEP 64

// entry point of the controller
int main(int argc, char **argv)
{
  // initialize the Webots API
  wb_robot_init();

  // internal variables
  int i;
  WbDeviceTag ps[8];
  char ps_names[8][4] = {
    "ps0", "ps1", "ps2", "ps3",
    "ps4", "ps5", "ps6", "ps7"
  };

  // initialize devices
  for (i=0; i<8 ; i++) {
    ps[i] = wb_robot_get_device(ps_names[i]);
    wb_distance_sensor_enable(ps[i], TIME_STEP);
  }

  // feedback loop
  while (1) {
    // step simulation
    int delay = wb_robot_step(TIME_STEP);
    if (delay == -1) // exit event from webots
      break;

    // read sensors outputs
    double ps_values[8];
    for (i=0; i<8 ; i++)
      ps_values[i] = wb_distance_sensor_get_value(ps[i]);

    // detect obstacles
    bool left_obstacle =
      ps_values[0] > 100.0 ||
      ps_values[1] > 100.0 ||
      ps_values[2] > 100.0;
    bool right_obstacle =
      ps_values[5] > 100.0 ||
      ps_values[6] > 100.0 ||
      ps_values[7] > 100.0;

    // init speeds
    double left_speed  = 500;
    double right_speed = 500;

    // modify speeds according to obstacles
    if (left_obstacle) {
      left_speed  -= 500;
      right_speed += 500;
    }
    else if (right_obstacle) {
      left_speed  += 500;
      right_speed -= 500;
    }

    // write actuators inputs
    wb_differential_wheels_set_speed(left_speed, right_speed);
  }

  // cleanup the Webots API
  wb_robot_cleanup();
  return 0; //EXIT_SUCCESS
}
```

### Conclusion

Here is a quick summary of the key points you need to understand before continuing
on:

- The controller entry point is the `main()` function like any standard C program.
- No Webots function should be called before the call of the `wb_robot_init()`
function.
- The last function to call before leaving the main function is the
`wb_robot_cleanup()` function.
- A device is referenced by the `name` field of its device node. The reference of
the node can be retrieved thanks to the `wb_robot_get_device()` function.
- Each controller program is executed as a child process of the Webots process. A
controller process does not share any memory with Webots (except the cameras'
images) and it can run on another CPU (or CPU core) than Webots.
- The controller code is linked with the "libController" dynamic library. This
library handles the communication between your controller and Webots.

This [section](controller-programming.md) explains in more details controller
programming. We invite you to read carefully this section before going on.
