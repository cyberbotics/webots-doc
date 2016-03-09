## Car library

The [car](#car-library) library is supposed to be used together with the
[driver](driver-library.md) library. It provides additional information and
functions to which a normal human driver of a car does not have access (e.g.,
changing the blinking period of the indicator or getting the value of the wheels
encoders). All the functions included in this library are explained below.

<a name="wbu_car_init">**Name**</a>

**wbu\_car\_init**, **wbu\_car\_cleanup** - *Initialise and clean*

``` c
#include <webots/car.h>

void wbu_car_init()
void wbu_car_cleanup()
```

**Description**

These two functions are respectively used to initialize and properly close the
[car](#car-library) library (the first one should be called at the very
beginning of the controller program and the second one at the very end). If you
use the [driver](driver-library.md) library it is not needed to call these
functions since they are already called from the corresponding functions of the
[driver](driver-library.md) library.

---

<a name="wbu_car_get_type">**Name**</a>

**wbu\_car\_get\_type**, **wbu\_car\_get\_engine\_type** - *Get the car and engine type*

``` c
#include <webots/car.h>

wbu_car_type wbu_car_get_type()
wbu_car_engine_type wbu_car_get_type()
```

**Description**

These two functions return respectively the type of transmission and of engine
of the car.

%figure "wbu_car_type enumeration"

| ENUM                     | Value |
| ------------------------ | ----- |
| WBU\_CAR\_TRACTION       | 0     |
| WBU\_CAR\_PROPULSION     | 1     |
| WBU\_CAR\_FOUR\_BY\_FOUR | 2     |

%end

%figure "wbu_car_engine_type enumeration"

| ENUM                                   | Value |
| -------------------------------------- | ----- |
| WBU\_CAR\_COMBUTSION\_ENGINE           | 0     |
| WBU\_CAR\_ELECTRIC\_ENGINE             | 1     |
| WBU\_CAR\_PARALLEL\_HYBRID\_ENGINE     | 2     |
| WBU\_CAR\_POWER\_SPLIT\_HYBRID\_ENGINE | 3     |

%end

---

<a name="wbu_car_set_indicator_period">**Name**</a>

**wbu\_car\_set\_indicator\_period**, **wbu\_car\_get\_indicator\_period** - *Set and get the indicator period*

``` c
#include <webots/car.h>

void wbu_car_set_indicator_period(double period)
double wbu_car_get_indicator_period()
```

**Description**

The first function is used to change the blinking period of the indicators. The
argument should be specified in seconds.

The second function returns the current blinking period of the indicators.

---

<a name="wbu_car_get_backwards_lights">**Name**</a>

**wbu\_car\_get\_backwards\_lights**, **wbu\_car\_get\_brake\_lights** - *Get the state of the backwards/brake lights*

``` c
#include <webots/car.h>

bool wbu_car_get_backwards_lights()
bool wbu_car_get_brake_lights()
```

**Description**

This two functions return respectively the state of the backwards and brake
lights (these two lights are switched on automatically by the library when
appropriated).

---

<a name="wbu_car_get_track_front">**Name**</a>

**wbu\_car\_get\_track\_front**, **wbu\_car\_get\_track\_rear**, **wbu\_car\_get\_wheelbase**, **wbu\_car\_get\_front\_wheel\_radius**, **wbu\_car\_get\_rear\_wheel\_radius** - *Get car caracteristics*

``` c
#include <webots/car.h>

double wbu_car_get_track_front()
double wbu_car_get_track_rear()
double wbu_car_get_wheelbase()
double wbu_car_get_front_wheel_radius()
double wbu_car_get_rear_wheel_radius()
```

**Description**

All these functions provide important physical characteristics of the car.

---

<a name="wbu_car_get_wheel_encoder">**Name**</a>

**wbu\_car\_get\_wheel\_encoder**, **wbu\_car\_get\_wheel\_speed** - *Get the wheels speed/encoder*

``` c
#include <webots/car.h>

double wbu_car_get_wheel_encoder(int wheel_index)
double wbu_car_get_wheel_speed(int wheel_index)
```

**Description**

These two functions return respectively the state of the wheel encoder (in
radians) and the instantaneous wheel rotational speed (in radians per second).
The `wheel_index` argument should match a value of the `wbu_car_wheel_index`
enum.

%figure "wbu_car_wheel_index enumeration"

| ENUM                          | Value |
| ----------------------------- | ----- |
| WBU\_CAR\_WHEEL\_FRONT\_RIGHT | 0     |
| WBU\_CAR\_WHEEL\_FRONT\_LEFT  | 1     |
| WBU\_CAR\_WHEEL\_REAR\_RIGHT  | 2     |
| WBU\_CAR\_WHEEL\_REAR\_LEFT   | 3     |
| WBU\_CAR\_WHEEL\_NB           | 4     |

%end

---

<a name="wbu_car_get_right_steering_angle">**Name**</a>

**wbu\_car\_get\_right\_steering\_angle**, **wbu\_car\_get\_left\_steering\_angle** - *Get the right/left steering angle*

``` c
#include <webots/car.h>

double wbu_car_get_right_steering_angle()
double wbu_car_get_left_steering_angle()
```

**Description**

These two functions return respectively the right and left steering angle
(because of the Ackermann steering geometry, the two angles are slightly
different).

---

<a name="wbu_car_enable_limited_slip_differential">**Name**</a>

**wbu\_car\_enable\_limited\_slip\_differential** - *Enable/disable the limited slip differential mechanism*

``` c
#include <webots/car.h>

void wbu_car_enable_limited_slip_differential(bool enable)
```

**Description**

These functions allow the user to enable or disable the limited differential
slip (it is enabled by default). When the limited differential slip is enabled,
at each time step, the torque (when control in torque is enabled) is
redistributed among all the actuated wheels so that they rotate at the same
speed (except the difference due to the geometric differential constraint). If
the limited differential slip is disabled, when a wheel starts to slip, it will
rotate faster than the others.

