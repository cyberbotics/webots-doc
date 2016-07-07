## Gait Manager

This manager implements the `DARwInOPGaitManager` class and allows you to use
the walking algorithm of the Framework.

A lot of parameters are available in the Framework algorithm to tune the gait.
But in order to make this manager easy to use, only a subset of the parameters
can be set. The other parameters are set to default values that are known to
works fine. It is however possible to change them if needed, by changing the
default values that are stored in a "*.ini" configuration file. In the
[appendix](walking-parameters.md), all the parameters of the gait are explained.

**Name**

**DARwInOPGaitManager(webots::Robot *robot, const std::string &iniFilename)** - *Gait Manager constructor*

```c
#include <DARwInOPGaitManager.hpp>

DARwInOPGaitManager(webots::Robot * robot, const std::string iniFilename);
```

**Description**

The first parameter is the robot on which the algorithm applies and the second
is the file name in which the default parameters are stored.

The following method are available in order to modify the main parameters in
your controller:

---

**Name**

**void setXAmplitude(double x)**, **void setYAmplitude(double y)**, **void setAAmplitude(double a)**, **void setMoveAimOn(bool q)**, **void setBalanceEnable(bool q)** - *Change the gait parameters*

```c
#include <DARwInOPGaitManager.hpp>

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

**void start()**, **void step(int ms)**, **void stop()** - *Start, stop and run the gait.*

```c
#include <DARwInOPGaitManager.hpp>

void start();
void step();
int msstop();
```

**Description**

Start and stop need to be used to stop/start the algorithm and step is used to
run `ms` milliseconds of the algorithm.

> **note**:
Note that, in order to run, the gait manager needs to know the position of each
servo and the values of the gyro. It is therefore essential to enable the gyro
and the position feedback of each servo before to use it, if it is not the case,
a warning will appear and they will automatically be enabled.
