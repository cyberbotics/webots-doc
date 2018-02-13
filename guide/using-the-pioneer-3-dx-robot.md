## Using the Pioneer 3-DX robot

%figure "Pioneer 3-DX, an all-purpose base, used for research and applications"

![pioneer3dx.png](images/pioneer3dx.png)

%end

The Pioneer 3-DX robot is an all-purpose base, used for research and applications involving mapping, teleoperation, localization, monitoring, reconnaissance and other behaviors.
Pioneer 3-DX is caracterized by a set of features listed in [this table](#pioneer-3-dx-characteristics).

The base Pioneer 3-DX platform is assembled with motors featuring 500-tick encoders, 19 cm wheels, tough aluminum body, 8 forward-facing ultrasonic (sonar) sensors, 8 optional rear-facing sonars, 1, 2 or 3 hot-swappable batteries, and a complete software development kit.
The base Pioneer 3-DX platform can reach speeds of 1.6 meters per second and carry a payload of up to 23 kg.

More information on the specifications and optional devices is available on Adept Mobile Robots official [webpage](http://www.mobilerobots.com/ResearchRobots/PioneerP3DX.aspx).

### Pioneer 3-DX model

%figure "Pioneer 3-DX characteristics"

| Characteristics     | Description                                                                     |
| ------------------- | ------------------------------------------------------------------------------- |
| Dimensions          | 485 mm long, 381 mm large, 217 mm high                                          |
| Weight              | 10 kg, operating playload of 17 kg                                              |
| Speed               | Max. forward/backward speed: 0.5 m/s; Rotation speed: 5.24 rad/s                |

%end

This model includes support for two motors, the caster wheel, 7 LEDs on the control panel and 16 sonar sensors (8 forward-facing, 8 rear-facing) for proximity measurements.
The standard model of the Pioneer 3-DX is provided in the "pioneer3dx.wbt" file which is located in the "WEBOTS\_HOME/projects/robots/adept/pioneer3/worlds" directory of the Webots distribution.

The Pioneer 3-DX motors are `RotationalMotor` nodes named according to [this figure](#pioneer-3-dx-motor-names).
The `wb_set_motor_position` and `wb_set_motor_velocity` functions allow the user to control the rotation of the wheels.

%figure "Pioneer 3-DX motor names"

![pioneer3dx_servos.png](images/pioneer3dx_servos.png)

%end

The sonar sensors are numbered according to [this figure](#sonar-sensors-positions).

%figure "Sonar sensors positions"

![pioneer3at_sonars.png](images/pioneer3at_sonars.png)

%end

The angle between two consecutive sensor directions is 20 degrees except for the four side sensors (so0, so7, so8 and so15) for which the angle is 40 degrees.

## Samples

Here are listed the different example worlds based on the Pionner 3-DX.
The worlds can be accessed in the "WEBOTS\_HOME/projects/robots/adept/pioneer3/worlds" directory and the controllers in the "WEBOTS\_HOME/projects/robots/adept/pioneer3/controller" directory.

### pioneeer3dx.wbt

The "pioneer3dx.wbt" world file shows a simulation example of the Braitenberg avoidance algorithm based on the use of the 16 sonar sensors (see the "collision\_avoidance.c" controller file) as seen in [this figure](#pioneer-3-dx-world-example).

%figure "Pioneer 3-DX world example"

![pioneer3dx_example.png](images/pioneer3dx_example.png)

%end

### pioneeer3dx\_collision\_avoidance.wbt

The "pioneer3dx\_collision\_avoidance.wbt" world file is a simulation example of the Braitenberg avoidance algorithm based on the use of the 16 sonar sensors in a dark environment (see the "obstacle\_avoidance.c" controller file) as seen in [this figure](#pioneer-3-dx-world-example-of-collision-avoidance).

%figure "Pioneer 3-DX world example of collision avoidance"

![pioneer3dx_collision_avoidance.png](images/pioneer3dx_collision_avoidance.png)

%end

### pioneeer3dx_gripper.wbt

The "pioneer3dx_gripper.wbt" world file is a simulation example where a gripper is used to move a ball (see the "gripper.c" controller file) as seen in [this figure](#pioneer-3-dx-world-example-using-a-gripper).

%figure "Pioneer 3-DX world example using a gripper"

![pioneer3dx_gripper.png](images/pioneer3dx_gripper.png)

%end

### pioneeer3dx_matlab.wbt

The "pioneer3dx_matlab.wbt" world file is a simulation example an obstacle avoidance behavior using a MATLAB controller (see the "matlab.c" controller file) as seen in [this figure](#pioneer-3-dx-world-example-of-a-matlab-controller).

%figure "Pioneer 3-DX world example of a MATLAB controller"

![pioneer3dx_matlab.png](images/pioneer3dx_matlab.png)

%end

### pioneeer3dx\_with_kinect.wbt

The "pioneer3dx\_with\_kinect.wbt" world file is a simple simulation example of an obstacle avoidance behavior based on a Microsoft Kinect sensor (see the "obstacle\_avoidance\_kinect.c" controller file) as seen in [this figure](#pioneer-3-dx-world-example-using-a-kinect).

%figure "Pioneer 3-DX world example using a Kinect"

![pioneer3dx_with_kinect.png](images/pioneer3dx_with_kinect.png)

%end
