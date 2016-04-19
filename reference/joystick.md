## Joystick

The [Joystick](#joystick) is not a node, it is a set of functions available by default for each [Robot](robot.md) node to read the joystick input. It is therefore not a device and the functions do not require any `WbDeviceTag`.

Each physical joystick can be used by one controller at the time only. If several joysticks are connected, each controller will get one.

> **note**:
In C++, Python and Java the joystick functions are in a dedicated class called
`Joystick`. In order to get the `Joystick` instance, you should call the
`getJoystick()` function of the `Robot` class.

### Joystick Functions

**Name**

**wb\_joystick\_enable**, **wb\_joystick\_disable**, **wb\_joystick\_get\_sampling\_period** - *enable/disable joystick*

{[C++](cpp-api.md#cpp_joystick)}, {[Java](java-api.md#java_joystick)}, {[Python](python-api.md#python_joystick)}, {[Matlab](matlab-api.md#matlab_joystick)}, {[ROS](ros-api.md)}

``` c
#include <webots/joystick.h>

void wb_joystick_enable(int ms)
void wb_joystick_disable()
int wb_joystick_get_sampling_period()
```

**Description**

The `wb_joystick_enable()` function allows the user to enable the joystick measurement each `ms` milliseconds. When this function is called the first free joystick is paired with the controller.

The `wb_joystick_disable()` function turns the joystick off. the joystick is released and can be used from another controller.

The `wb_joystick_get_sampling_period()` function returns the period given into the `wb_joystick_get_sampling_period()` function, or 0 if the device is disabled.

---

**Name**

**wb\_joystick\_is\_connected** - *check if a joystick is paired with this controller joystick*

{[C++](cpp-api.md#cpp_joystick)}, {[Java](java-api.md#java_joystick)}, {[Python](python-api.md#python_joystick)}, {[Matlab](matlab-api.md#matlab_joystick)}, {[ROS](ros-api.md)}

``` c
#include <webots/joystick.h>

bool wb_joystick_is_connected(int ms)
```

**Description**

Once the joystick is enabled, this function can be used to check if a free joystick has been paired with the controller or if no available joystick was found.

---

**Name**

**wb\_joystick\_get\_number\_of\_axes**,
**wb\_joystick\_get\_axis\_value** - *get number of axes and axis value*

{[C++](cpp-api.md#cpp_joystick)}, {[Java](java-api.md#java_joystick)}, {[Python](python-api.md#python_joystick)}, {[Matlab](matlab-api.md#matlab_joystick)}, {[ROS](ros-api.md)}

``` c
#include <webots/joystick.h>

int  wb_joystick_get_number_of_axes()
int  wb_joystick_get_axis_value(int axis)
```

**Description**

The `wb_joystick_get_number_of_axes()` function returns the number of axes of the joystick.

The `wb_joystick_get_axis_value()` function returns the current value of the axis set in argument.

---

**Name**

**wb\_joystick\_get\_pressed\_button** - *joystick button state reading function*

{[C++](cpp-api.md#cpp_joystick)}, {[Java](java-api.md#java_joystick)}, {[Python](python-api.md#python_joystick)}, {[Matlab](matlab-api.md#matlab_joystick)}, {[ROS](ros-api.md)}

``` c
#include <webots/joystick.h>

int wb_joystick_get_pressed_button()
```

**Description**

This function allows you to read a button pressed on the joystick from a paired with this controller (if any). The Webots window must be selected and the simulation running.
All the button pressed can be read by calling the `wb_joystick_get_key()` function repeatedly until this function returns -1. The returned value, if non-negative, is a button code corresponding to a button currently pressed. If no button is currently pressed, the function will return -1. Calling the `wb_joystick_get_key()` function a second time will return either -1 or the button code of another button which is currently simultaneously pressed. On Mac OSX, only the 12 first buttons and 2 first axes of the joystick are taken into account.

---

**Name**

**wb\_joystick\_set\_constant\_force**,
**wb\_joystick\_set\_constant\_force\_duration**,
**wb\_joystick\_set\_auto\_centering\_gain**,
**wb\_joystick\_set\_resistance\_gain** - *set the force feedback parameters*

{[C++](cpp-api.md#cpp_joystick)}, {[Java](java-api.md#java_joystick)}, {[Python](python-api.md#python_joystick)}, {[Matlab](matlab-api.md#matlab_joystick)}, {[ROS](ros-api.md)}

``` c
#include <webots/joystick.h>

void wb_joystick_set_constant_force(int level);
void wb_joystick_set_constant_force_duration(double duration);
void wb_joystick_set_auto_centering_gain(double gain);
void wb_joystick_set_resistance_gain(double gain);
```

**Description**

The `wb_joystick_set_constant_force()` function use force the joystick force feedback to add a constant force on an axis. The joystick must support force feedback and the unit of `level` is hardware specific.

The `wb_joystick_set_constant_force_duration()` function set for how long (in seconds) a force added with the `wb_joystick_set_constant_force()` function should be applied. After this duration if no other call to `wb_joystick_set_constant_force()` was done, the constant force is stopped. This is particularly useful in case the simulation is paused to make sure the force stops too. By default the duration is 1 second.

The `wb_joystick_set_auto_centering_gain()` function sets the auto-centering gain of the force feedback. Auto-centering is an effect that tend to align the axis with the zero position. The joystick must support force feedback and the unit of `gain` is hardware specific.

The `wb_joystick_set_resistance_gain()` function sets the resistance gain of the force feedback. Resistance is an effect that tend to prevent the axis from moving. The joystick must support force feedback and the unit of `gain` is hardware specific.

> **note**:
The units of the force feedback (both the level and gain) are hardware specific, it is therefore recommended to try first with a small value in order to avoid instabilities.
