## Keyboard

The [Keyboard](#keyboard) is not a node, it is a set of functions available by
default for each [Robot](robot.md) node to read the keyboard input. It is
therefore not a device and the functions do not require any `WbDeviceTag`.

> **note** [Python]:
In C++, Python and Java the keyboard functions are in a dedicated class called
`Keyboard`. In order to get the `Keyboard` instance, you should call the
`getKeyboard()` function of the `Robot` class.

### Keyboard Functions

**Name**

**wb\_keyboard\_enable**, **wb\_keyboard\_disable**, **wb\_keyboard\_get\_sampling\_period**, **wb\_keyboard\_get\_key** - *keyboard reading function*

{[C++](cpp-api.md#cpp_keyboard)}, {[Java](java-api.md#java_keyboard)}, {[Python](python-api.md#python_keyboard)}, {[Matlab](matlab-api.md#matlab_keyboard)}, {[ROS](ros-api.md)}

``` c
#include <webots/keyboard.h>

void wb_keyboard_enable(int ms)
void wb_keyboard_disable()
int wb_keyboard_get_sampling_period()
int wb_keyboard_get_key()
```

**Description**

These functions allow you to read a key pressed on the computer keyboard from a
controller program while the 3D window of Webots is selected and the simulation
is running. First, it is necessary to enable keyboard input by calling the
`wb_keyboard_enable()` function. The `ms` parameter is expressed in
milliseconds, and defines how frequently readings are updated.
The provided `ms` argument specifies the sensor's sampling period.
Note that the first key will be available only after the first sampling period elapsed.
After that, values can be read by calling the `wb_keyboard_get_key()`
function repeatedly until this function returns -1. The returned value, if
non-negative, is a key code corresponding to a key currently pressed. If no
modifier (shift, control or alt) key is pressed, the key code is the ASCII code
of the corresponding key or a special value (e.g., for the arrow keys). However,
if a modifier key was pressed, the ASCII code (or special value) can be obtained
by applying a binary AND between to the `WB_KEYBOARD_KEY` mask and the returned
value. In this case, the returned value is the result of a binary OR between one
of `WB_KEYBOARD_SHIFT`, `WB_KEYBOARD_CONTROL` or `WB_KEYBOARD_ALT` and the ASCII
code (or the special value) of the pressed key according to which modifier key
was pressed simultaneously.  If no key is currently pressed, the function will
return -1. Calling the `wb_keyboard_get_key()` function a second time will
return either -1 or the key code of another key which is currently
simultaneously pressed. The function can be called up to 7 times to detect up to
7 simultaneous keys pressed. The `wb_keyboard_disable()` function should be used
to stop the keyboard readings.

> **note** [C++]:
The keyboard predefined values are located into a (static) enumeration of the
Keyboard class. For example, `Keyboard.CONTROL` corresponds to the
*Control* key stroke.

<!-- -->

> **note** [Java]:
The keyboard predefined values are final integers located in the Keyboard class.
For example, *Ctrl+B* can be tested like this:

>     int key=keyboard.getKey()
>     if (key==Keyboard.CONTROL+'B')
>       System.out.Println("Ctrl+B is pressed");

<!-- -->

> **note** [Python]:
The keyboard predefined values are integers located into the Keyboard class. For
example, *Ctrl+B* can be tested like this:

>     key=keyboard.getKey()
>     if (key==Keyboard.CONTROL+ord('B')):
>       print 'Ctrl+B is pressed'
