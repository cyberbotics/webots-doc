## Mouse

The [Mouse](#mouse) API provides a set of functions available by default for each [Robot](robot.md) node and it is used to read the computer mouse input.
It doesn't have any corresponding Node.

> **Note** [C++, Python, Java]: In C++, Python and Java, the mouse functions are in a dedicated class called `Mouse`.
In order to get the `Mouse` instance, you should call the `Robot.getMouse` function.

### WbMouseState

The state of a mouse is defined like this:

%tab-component

%tab "C"

```c
typedef struct {
  // mouse buttons state
  bool left;
  bool middle;
  bool right;
  // mouse 3D position
  double x;
  double y;
  double z;
} WbMouseState;
```
%tab-end

%tab "C++"

```cpp
#include <webots/Mouse.hpp>

namespace webots {
  typedef struct {
    // mouse buttons state
    bool left;
    bool middle;
    bool right;
    // mouse 3D position
    double x;
    double y;
    double z;
  } MouseState;
}
```

%tab-end

%tab "Python"

```python
from controller import MouseState

class MouseState:
    @property
    left, middle, right  # mouse button state
    @property
    x, y, z  # mouse 3D position
```

%tab-end

%tab "Java"

```java
import com.cyberbotics.webots.controller.MouseState;

public class MouseState {
  public double getLeft();
  public double getMiddle();
  public double getRight();
  public double getX();
  public double getY();
  public double getZ();
}
```

%tab-end

%tab "MATLAB"

```matlab
TODO
```

%tab-end

%tab "ROS"

%tab-end

> `MouseState` data is directly accessible from the related [`/mouse/get_state` service](#wb_mouse_enable).

%end

The `left`, `middle` and `right` fields are matching respectively with the left, middle and right buttons of the computer mouse.
A `true` state means the button is pressed while a `false` state means the button is released.

The `x`, `y` and `z` fields are indicating the 3D coordinate where the mouse is pointing in the 3D window.
These values may be `NaN` if not applicable, for example when the mouse is pointing to the scene background.

### Mouse Functions

#### `wb_mouse_enable`
#### `wb_mouse_disable`
#### `wb_mouse_get_sampling_period`
#### `wb_mouse_get_key`

%tab-component

%tab "C"

```c
#include <webots/mouse.h>

void wb_mouse_enable(int sampling_period);
void wb_mouse_disable();
int wb_mouse_get_sampling_period();
WbMouseState wb_mouse_get_state();
```

%tab-end

%tab "C++"

```cpp
#include <webots/Mouse.hpp>

namespace webots {
  class Mouse {
    virtual void enable(int sampling_period);
    virtual void disable();
    int getSamplingPeriod();
    MouseState getState() const;
  }
}
```

%tab-end

%tab "Python"

```python
from controller import Mouse

class Mouse:
    def enable(self, sampling_period):
    def disable(self):
    def getSamplingPeriod(self):
    def getState(self):
```

%tab-end

%tab "Java"

```java
import com.cyberbotics.webots.controller.Mouse;

public class Mouse {
  public void enable(int sampling_period);
  public void disable();
  public int getSamplingPeriod();
  public MouseState getState();
}
```

%tab-end

%tab "MATLAB"

```matlab
wb_mouse_enable(sampling_period)
wb_mouse_disable()
period = wb_mouse_get_sampling_period()
state = wb_mouse_get_state()
```

%tab-end

%tab "ROS"

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/mouse/key` | `topic` | webots_ros::Int32Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`int32 data` |
| `/mouse/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/mouse/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/mouse/get_state` | `service` | `webots_ros::sensor_get_state` | `uint8 ask`<br/>`---`<br/>`uint8 x`<br/>`uint8 y`<br/>`uint8 z`<br/>`float64 x`<br/>`float64 y`<br/>`float64 z` |

%tab-end

%end

##### Description

*mouse reading function*

The state of the computer mouse can be read from a controller program while the simulation is running by using the above functions.
Firstly it is necessary to enable mouse input by calling the `wb_mouse_enable` function.
The `sampling_period` parameter is expressed in milliseconds, and defines how frequently readings are updated.
Note that the first state will be available only after the first sampling period elapsed.
After that, the state can be read by calling the `wb_mouse_get_state` function (for more details, see [`WbMouseState`](#wbmousestate)).
The `wb_mouse_disable` function should be used to stop the mouse readings.
