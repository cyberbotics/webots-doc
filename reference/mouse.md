## Mouse

The [Mouse](#mouse) API provides a set of functions available by default for each [Robot](robot.md) node and it is used to read the computer mouse input.
It doesn't have any corresponding Node.

> **Note** [C++, Python, Java]: In C++, Python and Java, the mouse functions are in a dedicated class called `Mouse`.
In order to get the `Mouse` instance, you should call the `Robot.getMouse` function.

#### WbMouseState

The state of a mouse is defined by the following structure:

```c
typedef struct {
  // mouse buttons state
  bool left;
  bool middle;
  bool right;
  // mouse 2D position in screen space
  double u;
  double v;
  // mouse 3D position
  double x;
  double y;
  double z;
} WbMouseState;
```

The `left`, `middle` and `right` fields are matching respectively with the left, middle and right buttons of the computer mouse.
A `true` state means the button is pressed while a `false` state means the button is released.

The `u` and `v` fields are indicating the 2D coordinate where the mouse is pointing in the 3D view.
The `u` coordinate goes from 0 to the left border of the 3D view to 1 to the right border, and the `v` goes from 0 to the top border to 1 to the bottom border.
These values may be `NaN` if the mouse is outside of the 3D view.

The `x`, `y` and `z` fields are indicating the 3D coordinate where the mouse is pointing in the 3D window.
These values may be `NaN` if not applicable, for example when the mouse is pointing to the scene background.

> **Note** [C++]: In C++ the name of the structure is `MouseState`.

> **Note** [Java/Python]: In Java and Python, the structure is replaced by a class called `MouseState`.

### Mouse Functions

**Name**

**wb\_mouse\_enable**, **wb\_mouse\_disable**, **wb\_mouse\_get\_sampling\_period**, **wb\_mouse\_get\_key** - *mouse reading function*

{[C++](cpp-api.md#cpp_mouse)}, {[Java](java-api.md#java_mouse)}, {[Python](python-api.md#python_mouse)}, {[Matlab](matlab-api.md#matlab_mouse)}, {[ROS](ros-api.md)}

```c
#include <webots/mouse.h>

void wb_mouse_enable(int sampling_period);
void wb_mouse_disable();
int wb_mouse_get_sampling_period();
WbMouseState wb_mouse_get_state();
```

**Description**

The state of the computer mouse can be read from a controller program while the simulation is running by using the above functions.
Firstly it is necessary to enable mouse input by calling the `wb_mouse_enable` function.
The `sampling_period` parameter is expressed in milliseconds, and defines how frequently readings are updated.
Note that the first state will be available only after the first sampling period elapsed.
After that, the state can be read by calling the `wb_mouse_get_state` function (for more details, see [`WbMouseState`](#wbmousestate)).
The `wb_mouse_disable` function should be used to stop the mouse readings.
