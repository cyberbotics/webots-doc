## Motion Manager

This manager implement the `DARwInOPMotionManager` class and allows you to play
a predefined motion stored in the "motion\_4096.bin" file. The main motions and
their corresponding ids are listed in [appendix](motions-files.md).

It is also possible to add custom motions to this file by using the `Action
Editor` tool.

> **note**:
More informations about this tool provided by ROBOTIS is available on Robotis
[website](http://www.support.robotis.com/ko/product/darwin-op/development/tools/action_editor.htm).

**Name**

**DARwInOPMotionManager(webots::Robot *robot)** - *Motion Manager constructor*

``` c
#include <DARwInOPMotionManager.hpp>

DARwInOPMotionManager(webots::Robot * robot)
```

**Description**

The first parameter is the robot on which the algorithm applies.

---

**Name**

**void playPage(int id)** - *Plays a motion*

``` c
#include <DARwInOPMotionManager.hpp>

playPage(int id)
```

**Description**

Plays the motion associated with page `id`

### Motion Manager in Step-by-Step

By default when starting a motion, the motion is run synchronously. That is the
controller is stopped until the motion is finished. But it is also possible to
run a motion asynchronously, in that case, the motion is started but the
execution flow of the controller is not stopped. This can be done by calling the
method `playPage` with the second parameter set to false:

**Name**

**void playPage(int id, bool sync = true)**, **void step(int ms)**, **bool isMotionPlaying()** - *Starts the motion in Step-by-Step mode.*

``` c
#include <DARwInOPMotionManager.hpp>

playPage(int id, bool sync)
step(int ms)
isMotionPlaying()
```

**Description**

The first function initiate the motion, but not run it, then in order to play ms
second of the motion, the second method need to be called (before the robot
step). In order to know if the motion is finished, the third method can be
called.

A typical use of the motion manager in mode step-by-step will be the following:

``` c
mMotionManager->playPage(1, false);
while(mMotionManager->isMotionPlaying()) {
  mMotionManager->step(mTimeStep);
  /*
  * Do something,
  * like image processing for example
  */
  myStep();
}
```

