## Motion Manager

The `RobotisOp2MotionManager` class allows you to play a predefined motion stored in the "motion\_4096.bin" file.
The main motions and their corresponding ids are listed in [appendix](motions-files.md).

It is also possible to add custom motions to this file by using the `Action Editor` tool.

> **Note**: The `Action Editor` tool is provided by ROBOTIS.
More information about are available on the [website](http://support.robotis.com/en/product/darwin-op/development/tools/action_editor.htm).

**Name**

**RobotisOp2MotionManager(webots::Robot \*robot)** - *Motion Manager constructor*

```cpp
#include <RobotisOp2MotionManager.hpp>

RobotisOp2MotionManager(webots::Robot *robot);
```

**Description**

The first parameter is the robot on which the algorithm applies.

---

**Name**

**void playPage(int id)** - *Plays a motion*

```cpp
#include <RobotisOp2MotionManager.hpp>

void playPage(int id);
```

**Description**

Plays the motion associated with page `id`.

### Motion Manager in Step-by-Step

By default when starting a motion, the motion is run synchronously.
It means that the controller execution is stopped until the motion is finished.
But it is also possible to run a motion asynchronously, in that case, the motion is started but the execution flow of the controller is not stopped.
This can be done by calling the method `playPage` with the second parameter set to false:

**Name**

**void playPage(int id, bool sync = true)**, **void step(int duration)**, **bool isMotionPlaying()** - *Starts the motion in Step-by-Step mode.*

```cpp
#include <RobotisOp2MotionManager.hpp>

void playPage(int id, bool sync);
void step(int duration);
bool isMotionPlaying();
```

**Description**

The *playPage* function initializes the motion, but does not run it.
The *step* method has to be called to run it (before calling the robot *step* function).
The *duration* argument is expressed in milliseconds.
The *isMotionPlaying* method determines if the motion is currently running.

Here is a typical use of the motion manager in step-by-step mode:

```cpp
mMotionManager->playPage(1, false);
while (mMotionManager->isMotionPlaying()) {
  mMotionManager->step(mTimeStep);
  /*
  * Do something,
  * like image processing for example
  */
  myStep();
}
```