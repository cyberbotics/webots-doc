## Driver library

The [driver](#driver-library) library provides all the usual functionality
available to a human driving his own car. All the functions included in this
library are explained below.

<a name="wbu_driver_step">**Name**</a>

**wbu\_driver\_init**, **wbu\_driver\_cleanup**, **wbu\_driver\_step** - *Initialise, clean and run a driver step*

``` c
#include <webots/driver.h>

void wbu_driver_init()
void wbu_driver_cleanup()
int wbu_driver_step()
```

**Description**

These functions are the equivalent of the init, cleanup and step function of any
regular robot controller. As a reminder, the `init` function should be called at
the very beginning of any controller program, the `cleanup` function at the end
of the controller program just before exiting and the `step` function should be
called in the main loop to run one simulation step. Unlike the robot step, the
driver step does not have any argument, the default time step of the world being
used.

---

<a name="wbu_driver_set_steering_angle">**Name**</a>

**wbu\_driver\_set\_steering\_angle**, **wbu\_driver\_get\_steering\_angle** - *Set and get the stearing angle*

``` c
#include <webots/driver.h>

void wbu_driver_set_steering_angle(double steering_angle)
double wbu_driver_get_steering_angle()
```

**Description**

The first function is used to steer the car, it steers the front wheels
according to the Ackermann geometry (left and right wheels are not steered with
the exact same angle). The angle is set in radians, a positive angle steers
right and a negative angle steers left. The formulas used in order to compute
the right and left angles are the following (`trackFront` and `wheelbase` are
the parameters of the [Car](car.md#car) PROTO):

```
angle_right = atan(1 / cot(steering_angle) - trackFront / (2 * wheelbase))
angle_left = atan(1 / cot(steering_angle) + trackFront / (2 * wheelbase))
```

The second function simply returns the steering angle (argument of the last call
to the previous function).

---

<a name="wbu_driver_set_cruising_speed">**Name**</a>

**wbu\_driver\_set\_cruising\_speed**, **wbu\_driver\_get\_target\_cruising\_speed** - *Set and get the target cruising speed*

``` c
#include <webots/driver.h>

void wbu_driver_set_cruising_speed(double speed)
double wbu_driver_get_target_cruising_speed()
```

**Description**

The first function activates the control in cruising speed of the car, the
rotational speed of the wheels is forced (respecting the geometric differential
constraint) in order that the car moves at the speed given in argument of the
function (in kilometers per hour). When the control in cruising speed is
activated, the speed is directly applied to the wheel without any engine model
simulation, therefore any call to functions like `wbu_driver_get_rpm()` will
raise an error. The acceleration of the car is computed using the `time0To100`
field of the [Car](car.md#car) PROTO.

The second function simply returns the target cruising speed (argument of the
last call to the previous function).

---

<a name="wbu_driver_get_current_speed">**Name**</a>

**wbu\_driver\_get\_current\_speed** - *Get the current speed*

``` c
#include <webots/driver.h>

double wbu_driver_get_current_speed()
```

**Description**

This function returns the current speed of the car (in kilometers per hour). The
estimated speed is computed using the rotational speed of the actuated wheels
and their respective radius.

---

<a name="wbu_driver_set_throttle">**Name**</a>

**wbu\_driver\_set\_throttle**, **wbu\_driver\_get\_throttle** - *Set and get the throttle*

``` c
#include <webots/driver.h>

void wbu_driver_set_throttle(double throttle)
double wbu_driver_get_throttle()
```

**Description**

The first function is used in order to control the car in torque, it sets the
state of the throttle. The argument should be between 0.0 and 1.0, 0 means that
0% of the output torque of the engine is sent to the wheels and 1.0 means that
100% of the output torque of the engine is sent to the wheels. For more
information about how the output torque of the engine is computed see section
[Engine models](#engine-models).

The second function simply returns the state of the throttle (argument of the
last call to the previous function).

---

<a name="wbu_driver_set_brake">**Name**</a>

**wbu\_driver\_set\_brake**, **wbu\_driver\_get\_brake** - *Set and get the brake*

``` c
#include <webots/driver.h>

void wbu_driver_set_brake(double brake)
double wbu_driver_get_brake()
```

**Description**

This function brakes the car by increasing the `dampingConstant` coefficient of
the rotational joints of each of the four wheels. The argument should be between
0.0 and 1.0, 0 means that no damping constant is added on the joints (no
breaking), 1 means that the parameter `brakeCoefficient` of the
[Car](car.md#car) PROTO is applied on the `dampingConstant` of each joint (the
value will be linearly interpolated between 0 and `brakeCoefficient` for any
arguments between 0 and 1).

The second function simply returns the state of the brake (argument of the last
call to the previous function).

---

<a name="wbu_driver_set_indicator">**Name**</a>

**wbu\_driver\_set\_indicator**, **wbu\_driver\_set\_indicator\_warning** - *Set the indicator state*

``` c
#include <webots/driver.h>

void wbu_driver_set_indicator(int state)
void wbu_driver_set_indicator_warning(bool state)
```

**Description**

The first function allows the user to set (using the `wbu_indicator_state` enum)
if the indicator should be on only for the right side of the car, the left side
of the car or should be off.

%figure "wbu_indicator_state enumeration"

| ENUM  | Value |
| ----- | ----- |
| OFF   | 0     |
| RIGHT | 1     |
| LEFT  | 2     |

%end

The second function allows the user to switch the warning on (indicator on both
side of the car) or off.

---

<a name="wbu_driver_set_dipped_beams">**Name**</a>

**wbu\_driver\_set\_dipped\_beams**, **wbu\_driver\_set\_antifog\_lights**, **wbu\_driver\_get\_dipped\_beams**, **wbu\_driver\_get\_antifog\_lights** - *Set and get the lights*

``` c
#include <webots/driver.h>

void wbu_driver_set_dipped_beams(bool state)
void wbu_driver_set_antifog_lights(bool state)
bool wbu_driver_get_dipped_beams()
bool wbu_driver_get_antifog_lights()
```

**Description**

The first two functions are used to enable or disable the dipped beams and the
anti-fog lights.

The second two functions return the state of the dipped beams or the anti-fog
lights.

---

<a name="wbu_driver_get_rpm">**Name**</a>

**wbu\_driver\_get\_rpm** - *Get the motor rpm*

``` c
#include <webots/driver.h>

double wbu_driver_get_rpm()
```

**Description**

This function returns the estimation of the engine rotation speed.

> **note**:
If the control in cruising speed is enabled, this function returns an error
because there is no engine model when control in cruising speed is enabled.

---

<a name="wbu_driver_set_gear">**Name**</a>

**wbu\_driver\_set\_gear**, **wbu\_driver\_get\_gear**, **wbu\_driver\_get\_gear\_number** - *Get and set the gear*

``` c
#include <webots/driver.h>

void wbu_driver_set_gear(int gear)
int wbu_driver_get_gear()
int wbu_driver_get_gear_number()
```

**Description**

The first function sets the engaged gear. An argument of `-1` is used in order
to engage the reverse gear, an argument of `0` is used in order to disengaged
the gearbox. Any other arguments than `0` and `-1` should be between 1 and the
number of coefficients set in the `gearRatio` parameter of the [Car](car.md#car)
PROTO.

The second function returns the currently engaged gear.

The last function simply returns the number of available gears (including the
reverse gear).

---

<a name="wbu_driver_get_control_mode">**Name**</a>

**wbu\_driver\_get\_control\_mode** - *Get the control mode*

``` c
#include <webots/driver.h>

wbu_control_mode wbu_driver_get_control_mode()
```

**Description**

This function returns the current control mode of the car.

%figure "wbu_control_mode enumeration"

| ENUM   | Value |
| ------ | ----- |
| SPEED  | 0     |
| TORQUE | 1     |

%end

### Engine models

When the control in torque of the car is enabled, at each step the output torque
of the engine is recomputed. First the rotational speed of the engine is
estimated from the rotational speed of the wheels, then the output torque of the
engine is computed (the formula depends on the engine type) using the rotational
speed of the engine, then this output torque is multiplied by the state of the
throttle and the gearbox coefficient, finally the torque is distributed
(respecting the differential constraint) on the actuated wheels (depending on
the car type).

#### Combustion engine

If `a`, `b` and `c` are the values of the `engineFunctionCoefficients` parameter
of the `Car` PROTO, the output torque is:

```
output_torque = c * rpm^2 + b * rpm + a
```

> **note**:
if the rpm is below the `engineMinRPM` parameter of the [Car](car.md#car) PROTO,
`engineMinRPM` is used instead of the real rpm, but if the rpm is above the
`engineMaxRPM` parameter, then the output torque is 0.

#### Electric engine

If `maxP` and `maxT` are respectively the `engineMaxPower` and `engineMaxTorque`
parameters of the `Car` PROTO, the ouput torque is:

```
output_torque = min(maxT; maxP * 60 / 2 * pi * rpm)
```

#### Parallel hybrid engine

In that case, the output torque is simply the sum of the two previous models.
But if the real rpm is below the `engineMinRPM` parameter of the `Car` PROTO,
the combustion engine is switched off.

#### Serial hybrid engine

Since this case is very similar to the electric engine model (from a simulation
point of view), you should use the electric model instead.

#### Power-split hybrid engine

If `ratio` and `splitRpm` are respectively the `hybridPowerSplitRatio` and
`hybridPowerSplitRPM` parameters of the `Car` PROTO, the output torque is
computed as follow:

```
output_torque_c = c * splitRpm^2 + b * splitRpm + a
        output_torque_e = min(maxT; maxP * 60 / 2 * pi * rpm)
        output_torque_total = output_torque_e + (1 - ratio) * output_torque_c
```

Here again, if the real rpm is below the `engineMinRPM` parameter of the `Car`
PROTO the combustion engine is switched off.\\

