## Adept's Pioneer 3-AT

%figure "Pioneer 3-AT model in Webots"

![pioneer3at_real.png](images/robots/pioneer-3at/model.png)

%end

The Pioneer 3-AT robot is an all-purpose outdoor base, used for research and prototyping applications involving mapping, navigation, monitoring, reconnaissance and other behaviors.
It is caracterized by a set of features listed in [this table](#pioneer-3-at-characteristics).
This model includes support for 4 motors and 16 sonar sensors (8 forward-facing, 8 rear-facing) for proximity measurements.

More information on the specifications and optional devices is available on the Adept Mobile Robots official [webpage](http://www.mobilerobots.com/ResearchRobots/ResearchRobots/P3AT.aspx).

### Movie Presentation

![youtube video](https://www.youtube.com/watch?v=x52vlsr8Ic0)

### Pioneer 3-AT Model

%figure "Pioneer 3-AT characteristics"

| Characteristics             | Values       |
| --------------------------- | ------------ |
| Length                      | 508 mm       |
| Width                       | 497 mm       |
| Height                      | 277 mm       |
| Weight                      | 12 kg        |
| Max. forward/backward speed | 0.7 m/s      |

%end

The standard model of the Pioneer 3-AT is provided in the "pioneer3AT.wbt" file which is located in the "WEBOTS\_HOME/projects/robots/adept/pioneer3/worlds" directory of the Webots distribution.

The Pioneer 3-AT motors are `RotationalMotor` nodes named according to [this figure](#pioneer-3-at-motor-names).
The `wb_set_motor_position` and `wb_set_motor_velocity` functions allow the user to control the rotation of the wheels.

%figure "Pioneer 3-AT motor names"

![pioneer3at_wheels.png](images/robots/pioneer-3at/wheels.png)

%end

The sonar sensors are numbered according to [this figure](#sonar-sensors-positions).

%figure "Sonar sensors positions"

![pioneer3at_sonars.png](images/robots/pioneer-3at/sonars.png)

%end

The angle between two consecutive sensor directions is 20 degrees except for the four side sensors (so0, so7, so8 and so15) for which the angle is 40 degrees.

### Pioneer3at PROTO

Derived from [Robot](../reference/robot.md).

```
Pioneer3at {
  SFVec3f    translation     0 0.11 0
  SFRotation rotation        0 1 0 0
  SFString   name            "Pioneer 3-AT"
  SFString   controller      "void"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFNode     extensionSlot   []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/adept/pioneer3/protos/Pioneer3at.proto"

#### Pioneer3at Field Summary

- `extensionSlot`: Extends the robot with new nodes in the extension slot.

### Samples

#### pioneer3at.wbt

![pioneer3at_avoidance.png](images/robots/pioneer-3at/pioneer3at_avoidance.wbt.png) The "pioneer3at.wbt" world file is a simulation example of a simple obstacle avoidance behavior based on the use of a SICK LMS 291 Lidar (see the "obstacle\_avoidance\_with\_lidar.c" controller file in the "WEBOTS\_HOME/projects/robots/adept/pioneer3/controller" directory).
The Lidar depth output is used to compute two stimuli in front of the robot.
These two stimuli are computed by a [Gaussian function](https://en.wikipedia.org/wiki/Gaussian_function) applied slightly on the front left, and respectively on the front right of the robot.
