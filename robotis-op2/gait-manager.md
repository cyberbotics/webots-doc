## Gait Manager

The `RobotisOp2GaitManager` class allows you to use
the walking algorithm of the Framework.

A lot of parameters are available in the Framework algorithm to tune the gait.
But in order to make this manager easy to use, only a subset of the parameters
can be set. The other parameters are set to default values that are known to
works fine. It is however possible to change them if needed, by changing the
default values that are stored in a ".ini" configuration file. In the
[appendix](walking-parameters.md), all the parameters of the gait are explained.

**Name**

**RobotisOp2GaitManager(webots::Robot \*robot, const std::string &iniFilename)** - *Gait Manager constructor*

```c++
#include <RobotisOp2GaitManager.hpp>

RobotisOp2GaitManager(webots::Robot *robot, const std::string &iniFilename);
```

**Description**

The first parameter is the robot on which the algorithm applies and the second
is the file name in which the default parameters are stored.

The following methods are available in order to modify the main parameters in
your controller:

---

**Name**

**void setXAmplitude(double x)**, **void setYAmplitude(double y)**, **void setAAmplitude(double a)**, **void setMoveAimOn(bool q)**, **void setBalanceEnable(bool q)** - *Change the gait parameters*

```c++
#include <RobotisOp2GaitManager.hpp>

void setXAmplitude(double x);
void setYAmplitude(double y);
void setAAmplitude(double a);
void setMoveAimOn(bool q);
void setBalanceEnable(bool q);
```

**Description**

These are the open parameters, they have the following impact on the gait:

- X influences the length of the foot step forward, it can take any value between
-1 and 1.
- Y influences the length of the foot step in the side direction, it can take any
value between -1 and 1.
- A influences the angle of the gait and allows also the robot to rotate during
the walk, it can take any value between 0 and 1.
- If MoveAimOn is set, it allows the robot to rotate around something by inversing
the sense of rotation, it can be very useful to turn around a ball in order to
kick it in the right direction for example.
- If BalanceEnable is set, the gyroscope is used in the control loop to make the
walking gait more robust.

Finally the following methods can be used in order to run the algorithm:

---

**Name**

**void start()**, **void step(int duration)**, **void stop()** - *Start, stop and run the gait.*

```c++
#include <RobotisOp2GaitManager.hpp>

void start();
void step(int duration);
int  stop();
```

**Description**

The *start* and *stop* functions are used to start and stop the algorithm. The *step* function is used to
run the algorithm for a specified *duration*, expressed in milliseconds.

> **Note**:
In order to run, the gait manager needs to know the position of each
servo and the values of the gyroscope. It is therefore essential to enable the
`Gyro` device and the position feedback of each servo before using it.
If it is not the case, a warning will appear and they will automatically be
enabled.
