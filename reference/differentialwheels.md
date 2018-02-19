## DifferentialWheels

> **Note**: From Webots R2018a, the [DifferentialWheels](#differentialwheels) node is deprecated and should not be used in any new simulation models.
It is kept for backwards compatibility only.
Instead of using a [DifferentialWheels](#differentialwheels) node, a Robot node should be used instead with two [HingeJoint](#hingejoint), [RotationalMotor](#rotationalmotor) and [PositionSensor](#positionsensor) nodes.
In that case, it is recommended to name the two [RotationalMotor](#rotationalmotor) nodes `left wheel motor` and `right wheel motor` and the two [PositionSensor](#positionsensor) nodes `left wheel sensor` and `right wheel sensor`.

Derived from [Robot](robot.md).

```
DifferentialWheels {
  SFFloat motorConsumption  0      # [0, inf)
  SFFloat axleLength        0.1    # [0, inf)
  SFFloat wheelRadius       0.01   # [0, inf)
  SFFloat maxSpeed          10     # [0, inf)
  SFFloat maxAcceleration   10     # [0, inf)
  SFFloat speedUnit         1      # [0, inf)
  SFFloat slipNoise         0.1    # [0, inf)
  SFFloat encoderNoise      -1     # {-1, [0, inf)}
  SFFloat encoderResolution -1     # {-1, [0, inf)}
  SFFloat maxForce          0.3    # [0, inf)
}
```

### Description

The [DifferentialWheels](#differentialwheels) node can be used as base node to build robots with two wheels and differential steering.
Any other type of robot (legged, humanoid, vehicle, etc.) needs to use [Robot](robot.md) as base node.

A [DifferentialWheels](#differentialwheels) robot will automatically take control of its wheels if they are placed in the `children` field.
The wheels must be [Solid](solid.md) nodes, and they must be named "right wheel" and "left wheel".
If the wheel objects are found, Webots will automatically make them rotate at the speed specified by the `wb_differential_wheels_set_speed` function.

The origin of the robot coordinate system is the projection on the ground plane of the middle of the wheels' axle.
The *x* axis is the axis of the wheel axle, *y* is the vertical axis and *z* is the axis pointing towards the rear of the robot (the front of the robot has negative *z* coordinates).

### Field Summary

- `motorConsumption`: power consumption of the motor in Watts.

- `axleLength`: distance between the two wheels (in meters).
This field must be specified for "kinematics" based robot models.
It will be ignored by "physics" based models.

- `wheelRadius`: radius of the wheels (in meters).
Both wheels must have the same radius.
This field must be specified for "kinematics" based robot models.
It will be ignored by "physics" based models.

- `maxSpeed`: maximum speed of the wheels, expressed in *rad/s*.

- `maxAcceleration`: maximum acceleration of the wheels, expressed in *rad/s^2*.
It is used only in "kinematics" mode.

- `speedUnit`: defines the unit used in the `wb_differential_wheels_set_speed` function, expressed in *rad/s*.

- `slipNoise`: slip noise added to each move expressed in percent.
If the value is 0.1, a noise component of +/- 10 percent is added to the command for each simulation step.
The noise is, of course, different for each wheel.
The noise has a uniform distribution, also known as as "white noise."

- `encoderNoise`: white noise added to the incremental encoders.
If the value is -1, the encoders are not simulated.
If the value is 0, encoders are simulated without noise.
Otherwise a cumulative uniform noise is added to encoder values.
At every simulation step, an increase value is computed for each encoder.
Then, a random uniform noise is applied to this increase value before it is added to the encoder value.
This random noise is computed in the same way as the slip noise (see above).
When the robot encounters an obstacle, and if no physics simulation is used, the robot wheels do not slip, hence the encoder values are not incremented.
This is very useful to detect that a robot has hit an obstacle.
For each wheel, the angular velocity is affected by the `slipNoise` field.
The angular speed is used to compute the rotation of the wheel for a basic time step (by default 32 ms).
The wheel is actually rotated by this amount.
This amount is then affected by the `encoderNoise` (if any).
This means that a noise is added to the amount of rotation in a similar way as with the `slipNoise`.
Finally, this amount is multiplied by the `encoderResolution` (see below) and used to increment the encoder value, which can be read by the controller program.

- `encoderResolution`: defines the number of encoder increments per radian of the wheel.
An `encoderResolution` of *100* will make the encoders increment their value by (approximately) 628 each time the wheel makes a complete revolution.
The -1 default value means that the encoder functionality is disabled as with `encoderNoise`.

- `maxForce`: defines the maximum torque used by the robot to rotate each wheel in a "physics" based simulation.
It corresponds to the `dParamFMax` parameter of an ODE hinge joint.
It is ignored in "kinematics" based simulations.

### Simulation Modes

The [DifferentialWheels](#differentialwheels)'s motion can be computed by different algorithms: "physics" or "kinematics" depending on the structure of the world.

#### Physics mode

A [DifferentialWheels](#differentialwheels) is simulated in "physics" mode if it contains [Physics](physics.md) nodes in its body and wheels.
In this mode, the simulation is carried out by the ODE physics engine, and the robot's motion is caused by the friction forces generated by the contact of the wheels with the floor.
The wheels can have any arbitrary shape (usually a cylinder), but their contact with the floor is necessary for the robot's motion.
In "physics" mode the inertia, weight, etc. of the robot and wheels is simulated, so for example the robot will fall if you drop it.
The friction is simulated with the Coulomb friction model, so a [DifferentialWheels](#differentialwheels) robot would slip on a wall with some friction coefficient that you can tune in the [Physics](physics.md) nodes.
The "physics" mode is the most realistic but also the slowest simulation mode.

#### Kinematics mode

When a [DifferentialWheels](#differentialwheels) does not have [Physics](physics.md) nodes then it is simulated in "kinematics" mode.
In the "kinematics" mode the robot's motion is calculated according to 2D kinematics algorithms and the collision detection is calculated with 3D algorithms.
Friction is not simulated, so a [DifferentialWheels](#differentialwheels) does not actually require the contact of the wheels with the floor to move.
Instead, its motion is controlled by a 2D kinematics algorithm using the `axleLength, wheelRadius` and `maxAcceleration` fields.
Because friction is not simulated the [DifferentialWheels](#differentialwheels) will not slide on a wall or on another robot.
The simulation will rather look as if obstacles (walls, robots, etc.) are very rough or harsh.
However the robots can normally avoid to become blocked by changing direction, rotating the wheels backwards, etc.
Unlike the "physics" mode, in the "kinematics" mode the gravity and other forces are not simulated therefore a [DifferentialWheels](#differentialwheels) robot will keep its initial elevation throughout the simulation.

%figure "DifferentialWheels simulation modes"

| &nbsp;                | Physics mode       | Kinematics mode                    |
| --------------------- | ------------------ | ---------------------------------- |
| Motion triggered by   | Wheels friction    | 2d Webots kinematics               |
| Friction simulation   | Yes, Coulomb model | No, robot slides against obstacles |
| Inertia/Weight/Forces | Yes                | No                                 |
| Collision detection   | 3D (ODE)           | 3D (ODE)                           |
| wheelRadius field     | Ignored            | Used                               |
| axleLength field      | Ignored            | Used                               |
| maxAcceleration field | Ignored            | Used                               |
| maxForce field        | Used               | Ignored                            |

%end

### DifferentialWheels Functions

**Name**

**wb\_differential\_wheels\_set\_speed** - *control the speed of the robot*

{[C++](cpp-api.md#cpp_differential_wheels)}, {[Java](java-api.md#java_differential_wheels)}, {[Python](python-api.md#python_differential_wheels)}, {[Matlab](matlab-api.md#matlab_differential_wheels)}, {[ROS](ros-api.md)}

```c
#include <webots/differential_wheels.h>

void wb_differential_wheels_set_speed(double left, double right);
double wb_differential_wheels_get_left_speed();
double wb_differential_wheels_get_right_speed();
```

**Description**

The `wb_differential_wheels_set_speed` function allows the user to specify a speed for the [DifferentialWheels](#differentialwheels) robot.
This speed will be sent to the motors of the robot at the beginning of the next simulation step.
The speed unit is defined by the `speedUnit` field of the [DifferentialWheels](#differentialwheels) node.
The default value is 1 radians per seconds.
Hence a speed value of 2 will make the wheel rotate at a speed of 2 radians per seconds.
The linear speed of the robot can then be computed from the angular speed of each wheel, the wheel radius and the noise added.
Both the wheel radius and the noise are documented in the [DifferentialWheels](#differentialwheels) node.

The `wb_differential_wheels_get_left_speed` and `wb_differential_wheels_get_right_speed` functions allow to retrieve the last speed commands given as an argument of the `wb_differential_wheels_set_speed` function.

---

**Name**

**wb\_differential\_wheels\_enable\_encoders**, **wb\_differential\_wheels\_disable\_encoders**, **wb\_differential\_wheels\_get\_encoders\_sampling\_period** - *enable or disable the incremental encoders of the robot wheels*

{[C++](cpp-api.md#cpp_differential_wheels)}, {[Java](java-api.md#java_differential_wheels)}, {[Python](python-api.md#python_differential_wheels)}, {[Matlab](matlab-api.md#matlab_differential_wheels)}, {[ROS](ros-api.md)}

```c
#include <webots/differential_wheels.h>

void wb_differential_wheels_enable_encoders(int sampling_period);
void wb_differential_wheels_disable_encoders();
int wb_differential_wheels_get_encoders_sampling_period(WbDeviceTag tag);
```

**Description**

These functions allow the user to enable or disable the incremental wheel encoders for both wheels of the [DifferentialWheels](#differentialwheels) robot.
The `sampling_period` argument defines the sampling period of the encoder and is expressed in milliseconds.
Incremental encoders are counters that increment each time a wheel turns.
The amount added to an incremental encoder is computed from the angle the wheel rotated and from the `encoderResolution` parameter of the [DifferentialWheels](#differentialwheels) node.
Hence, if the `encoderResolution` is 100 and the wheel made a whole revolution, the corresponding encoder will have its value incremented by about 628.
Please note that in a kinematic simulation (with no [Physics](physics.md) node set) when a [DifferentialWheels](#differentialwheels) robot encounters an obstacle while trying to move forward, the wheels of the robot do not slip, hence the encoder values are not increased.
This is very useful to detect that the robot has hit an obstacle.
On the contrary, in a physics simulation (when the [DifferentialWheels](#differentialwheels) node and its children contain appropriate [Physics](physics.md) nodes), the wheels may slip depending on their friction parameters and the force of the motors (`maxForce` field of the [DifferentialWheels](#differentialwheels) node).
If a wheel slips, then its encoder values are modified according to its actual rotation, even though the robot doesn't move.

The `wb_differential_wheels_get_encoders_sampling_period` function returns the period given into the `wb_differential_wheels_enable_encoders` function, or 0 if the device is disabled.
Note that the first encoders values will be available only after the first sampling period elapsed.

---

**Name**

**wb\_differential\_wheels\_get\_left\_encoder**, **wb\_differential\_wheels\_get\_right\_encoder**, **wb\_differential\_wheels\_set\_encoders** - *read or set the encoders of the robot wheels*

{[C++](cpp-api.md#cpp_differential_wheels)}, {[Java](java-api.md#java_differential_wheels)}, {[Python](python-api.md#python_differential_wheels)}, {[Matlab](matlab-api.md#matlab_differential_wheels)}, {[ROS](ros-api.md)}

```c
#include <webots/differential_wheels.h>

double wb_differential_wheels_get_left_encoder();
double wb_differential_wheels_get_right_encoder();
void wb_differential_wheels_set_encoders(double left, double right);
```

**Description**

These functions are used to read or set the values of the left and right encoders.
The encoders must be enabled with the `wb_differential_wheels_enable_encoders` function, so that the functions can read valid data.
Additionally, the `encoderNoise` of the corresponding [DifferentialWheels](#differentialwheels) node should be positive.
Setting the encoders' values will not make the wheels rotate to reach the specified value; instead, it will simply reset the encoders with the specified value.

---

**Name**

**wb\_differential\_wheels\_get\_max\_speed** - *get the value of the maxSpeed field*

{[C++](cpp-api.md#cpp_differential_wheels)}, {[Java](java-api.md#java_differential_wheels)}, {[Python](python-api.md#python_differential_wheels)}, {[Matlab](matlab-api.md#matlab_differential_wheels)}, {[ROS](ros-api.md)}

```c
#include <webots/differential_wheels.h>

double wb_differential_wheels_get_max_speed();
```

**Description**

The `wb_differential_wheels_get_max_speed` function allows the user to get the value of the `maxSpeed` field of the [DifferentialWheels](#differentialwheels) node.

---

**Name**

**wb\_differential\_wheels\_get\_speed\_unit** - *get the value of the speedUnit field*

{[C++](cpp-api.md#cpp_differential_wheels)}, {[Java](java-api.md#java_differential_wheels)}, {[Python](python-api.md#python_differential_wheels)}, {[Matlab](matlab-api.md#matlab_differential_wheels)}, {[ROS](ros-api.md)}

```c
#include <webots/differential_wheels.h>

double wb_differential_wheels_get_speed_unit();
```

**Description**

The `wb_differential_wheels_get_speed_unit` function allows the user to get the value of the `speedUnit` field of the [DifferentialWheels](#differentialwheels) node.
