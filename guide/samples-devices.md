## Devices

The "WEBOTS\_HOME/projects/samples/devices" directory contains Webots worlds that individually demonstrate the Webots devices and their API.

The world files are located in the "WEBOTS\_HOME/projects/samples/devices/worlds" directory, and their controllers in the "WEBOTS\_HOME/projects/samples/devices/controllers" directory.
The world files and the corresponding controllers are named according to the device they demonstrate.

Most of the devices below use a simple two-wheeled blue robot called MyBot moving in a closed square arena containing obstacles (see [figure below](#mybot-in-a-squared-arena)).

The studied devices are attached on this robot.
`MyBot` moves and avoid obstacles using two [DistanceSensors](../reference/distancesensor.md) and a technique based on Braitenberg vehicles.

%figure "MyBot in a squared arena."

![mybot.png](images/samples/mybot.png)

%end

### battery.wbt

**Keywords**: Battery, Charger

![battery.png](images/samples/battery.png) In this example, `MyBot` moves in a closed arena filled with obstacles.
The energy consumed by the wheel motors slowly discharges the robot's battery.
When the battery level reaches zero, the robot is powered off and stops moving.
In order to remain powered, the robot must recharge its battery at energy chargers.
Chargers are represented by the semi-transparent colored cylinders in the four corners of the arena.
Only a full charger can recharge the robot's battery.
The color of a charger changes with its energy level: it is red when completely empty and green when completely full.

### bumper.wbt

**Keywords**: TouchSensor, bumper

![bumper.png](images/samples/bumper.png) In this example, `MyBot` moves in a closed arena filled with obstacles.
Its "bumper" [TouchSensor](../reference/touchsensor.md) (represented by a black box) detects collisions.
`MyBot` moves back and turns a little each time a collision is detected.

### camera.wbt

**Keywords**: Camera, image processing, RGB pixel, Camera noise, PNG, ANSI

![camera.png](images/samples/camera.png) In this example, `MyBot` uses a camera to detect colored objects.
The robot analyzes the RGB color level of each pixel of the camera images.
When it has detected something, it turns, stops for a few seconds and saves the image in a PNG file to the user directory.
It also prints a colored message (using ANSI codes) in the `Console` explaining the type of object it has detected.
White noise is applied on the [Camera](../reference/camera.md).

### camera\_auto\_focus.wbt

**Keywords**: Camera, autofocus, depth-of-field

![camera_auto_focus.png](images/samples/camera_auto_focus.png) In this example, `MyBot` demonstrates a [Camera](../reference/camera.md) with autofocus.
The robot uses a [DistanceSensor](../reference/distancesensor.md) to get the distance to the front object and adjusts the [Camera](../reference/camera.md) focal length accordingly.
The objects displayed before or after this distance are blurred.

### camera\_motion\_blur.wbt

**Keywords**: Camera, motion blur

![camera_compositor.png](images/samples/camera_motion_blur.png) In this example, `MyBot` demonstrates the camera motion blur effect.
The motion blur response time is given by the `Camera.motionBlur` field.

### camera\_noise\_mask.wbt

**Keywords**: Camera, noise mask

![camera_noise_mask.png](images/samples/camera_noise_mask.png) In this example, `MyBot` demonstrates noise effect based on noise mask.
The noise mask is determined by the `Camera.noiseMaskUrl` field.

### camera\_recognition.wbt

**Keywords**: Camera, pattern recognition, smart camera

![camera_recognition.png](images/samples/camera_recognition.png) In this example, `MyBot` demonstrates object recognition capabilities.
The robot camera displays yellow rectangles around the recognized objects.
Information about the objects currently recognized are displayed in the `Console`.
The camera recognizes [Solid](../reference/solid.md) nodes whose `recognitionColors` field is not empty.

### connector.wbt

**Keywords**: Connector, RotationalMotor, IndexedLineSet

![connector.png](images/samples/connector.png) In this example, a light `MyBot` (light blue) is lifted over two heavier `MyBot`s (dark blue).
All three robots are equipped with a [Connector](../reference/connector.md) placed at the tip of a moveable handle ([HingeJoint](../reference/hingejoint.md)).
An `IndexedLineSet` is added to every [Connector](../reference/connector.md) in order to show the axes.
When the simulation starts, the light robot approaches the first heavy robot and their connectors dock to one another.
Then both robots rotate their handles simultaneously, hence the light robot gets lifted over the heavy one.
Then the light robot gets passed over another time by the second heavy robot and so on...
All the robots in this simulation use the same controller; the different behaviors are selected according to the robot's name.

### display.wbt

**Keywords**: Display, write in textures, overlay

![display.png](images/samples/display.png) This example demonstrates several use of the [Display](../reference/display.md) device.

- The `MyBot` [Display](../reference/display.md) called "emoticon_display" is displayed as a 2D overlay on top of the 3D window, and is displayed as a texture on the screen mounted on the `MyBot`.
It loads the `emoticons.png` image contains a grid of emoticons (as a sprite sheet), and randomly selects an emoticon from this image every 30 steps.
- The `MyBot` [Display](../reference/display.md) called "camera_display" is displayed as a 2D overlay on top of the 3D window.
It copies the [Camera](../reference/camera.md) image, and draws a yellow rectangle and text over it where yellow pixels are detected.
- The [Supervisor](../reference/supervisor.md) [Display](../reference/display.md) called "ground display" is displayed as a texture on the floor.
The [Supervisor](../reference/supervisor.md) get the position of `MyBot` and draws a green dot at this location.

### distance\_sensor.wbt

**Keywords**: DistanceSensor, Braitenberg

![distance_sensor.png](images/samples/distance_sensor.png) In this example, eight [DistanceSensors](../reference/distancesensor.md) are mounted at regular intervals around the `MyBot` body.
The robot avoids obstacles using a technique based on Braitenberg vehicles.

### emitter\_receiver.wbt

**Keywords**: Emitter, Receiver, infra-red transmission

![emitter_receiver.png](images/samples/emitter_receiver.png) In this example, there are two robots: one is equipped with an [Emitter](../reference/emitter.md) and the other one with a [Receiver](../reference/receiver.md).
Both robots move among the obstacles while the *emitter* robot sends messages to the *receiver* robot.
The range of the [Emitter](../reference/emitter.md) device is indicated by the radius of the transparent gray sphere around the emitter robot.
The state of the communication between the two robots is displayed in the Console.
You can observe this when the *receiver* robot enters the *emitter*'s sphere while no direct obstacle is present on the route, then the communication is established, otherwise the communication is interrupted.
Note that the communication between "infra-red" [Emitters](../reference/emitter.md) and [Receivers](../reference/receiver.md) can be blocked by an obstacle, this is not the case with "radio" [Emitters](../reference/emitter.md) and [Receivers](../reference/receiver.md).

### encoders.wbt

**Keywords**: PositionSensor, encoders

![encoders.png](images/samples/encoders.png) This example demonstrates the usage of the wheel encoders of two-wheeled robots.
The controller randomly chooses target encoder positions, then it rotates its wheels until the encoder values reach the chosen target position.
Then the encoders are reset and the controller chooses new random values.
[PositionSensor](../reference/positionsensor.md) nodes applied on [HingeJoint](../reference/hingejoint.md) nodes model the encoders.
The robot does not pay any attention to obstacles.

### force\_sensor.wbt

**Keywords**: TouchSensor, force sensor

![force_sensor.png](images/samples/force_sensor.png) This example is nearly the same as [bumper.wbt](#bumper-wbt).
The only difference is that this robot uses a "force" [TouchSensor](../reference/touchsensor.md) instead of a "bumper".
So this robot can measure the force of each collision, which is printed in the `Console`.

### force3d\_sensor.wbt

**Keywords**: TouchSensor, 3D force sensor

![force3d_sensor.png](images/samples/force3d_sensor.png) This example demonstrates how to use a 3D force sensor.
The opaque box in the center of the transparent one is a [Robot](../reference/robot.md) node.
The [TouchSensor](../reference/touchsensor.md) is the child of the [Robot](../reference/robot.md) node.
This setup allow to measure the force on the six sides of the [TouchSensor](../reference/touchsensor.md).
The resulting force vector is displayed in the `Console`.
Moving and rotating the box will change the displayed force.

### gps.wbt

**Keywords**: GPS, Keyboard, get robot position

![gps.png](images/samples/gps.png) This example shows two different techniques to find the current position of `MyBot`.
The first technique consists in using an on-board [GPS](../reference/gps.md) device.
The second method uses a [Supervisor](../reference/supervisor.md) controller that reads and transmits the position info to the robot.
Note that a [Supervisor](../reference/supervisor.md) can read (or change) the position of any object in the simulation at any time.
This example implements both techniques, and you can choose either one or the other with the keyboard.
The `G` key prints the robot's [GPS](../reference/gps.md) device position.
The `S` key prints the position read by the [Supervisor](../reference/supervisor.md).

### gps\_lat\_long.wbt

**Keywords**: GPS, WGS84, Latitude-Longitude

![gps.png](images/samples/gps.png) This example shows how to set a `WGS84` reference, and how to retrieve the robot's `WGS84` latitude and longitude in this reference.
The reference is set in the `WorldInfo.gpsCoordinateSytem` and `WorldInfo.gpsReference`.
The resulting position is displayed in the `Console` at each step.

### gyro.wbt

**Keywords**: Gyro, angular velocity

![gyro.png](images/samples/gyro.png) This example shows how to measure angular velocity.
A [Gyro](../reference/gyro.md) is mounted on three rotational motors (each motor corresponds to one axis).
The motors a running consecutively for a while.
The resulting angular velocity measured by the gyro is displayed in the `Console`.

### hokuyo.wbt

**Keywords**: Hokuyo, Lidar, Display plot

![hokuyo.png](images/samples/hokuyo.png) This example shows how to use [Lidars](../reference/lidar.md) and plot their depth output on a [Display](../reference/display.md) device.
Two `Hokuyo` [Lidars](../reference/lidar.md) are mounted on the `MyBot`.
At each step, the lidars are updated, and their depth output are displayed in distinct [Displays](../reference/display.md).

### inertial\_unit.wbt

**Keywords**: InertialUnit, roll/pitch/yaw angles

![inertial_unit.png](images/samples/inertial_unit.png) This example demonstrates the use of an [InertialUnit](../reference/inertialunit.md) device.
An [InertialUnit](../reference/inertialunit.md) is mounted on a 3 DOF (Degrees Of Freedom) arm which moves from one random target to another.
Each time a target is reached, the absolute roll, pitch and yaw angles of the [InertialUnit](../reference/inertialunit.md) are displayed in the `Console`.

### laser\_pointer.wbt

**Keywords**: DistanceSensor, laser

![laser_pointer.png](images/samples/laser_pointer.png) This example demonstrates the use of [DistanceSensor](../reference/distancesensor.md) devices in laser mode.
`MyBot` turns round with two laser pointers enabled.
Red dots are displayed where the laser beam hits obstacles.

### led.wbt

**Keywords**: LED

![led.png](images/samples/led.png) In this example, `MyBot` moves while randomly changing the color of three [LEDs](../reference/led.md) on the top of its body.
Each [LED](../reference/led.md)'s material emissive color and embedded [PointLight](../reference/pointlight.md) are modified accordingly.
The color choice is printed in the `Console`.

### lidar.wbt

**Keywords**: Lidar

![lidar.png](images/samples/lidar.png) In this example, `MyBot` demonstrates the use of a [Lidar](../reference/lidar.md) device.
The [Lidar](../reference/lidar.md) mounted on the `MyBot` scans the environment.
The [Lidar](../reference/lidar.md) point cloud can be shown by enabling the `View / Optional Rendering / Show Lidar Point Cloud`.

### light\_sensor.wbt

**Keywords**: LightSensor

![light_sensor.png](images/samples/light_sensor.png) In this example, `MyBot` uses two [LightSensors](../reference/lightsensor.md) to follow a light source.
The light source can be moved with the mouse; the robot will follow it.

### linear\_motor.wbt

**Keywords**: LinearMotor, set motor position

![linear_motor.png](images/samples/linear_motor.png) In this example, a linear motor from position `0` and then progresses by steps of `2 [cm]` until it reaches `20 [cm]`.
Once done, it comes back to position `0` and restarts.
A ruler indicates the linear motor progression.

### motor.wbt

**Keywords**: RotationalMotor, force control, energy consumption

![motor.png](images/samples/motor.png) In this example, a rotational motor is controlled in force mode to push a cardboard.
The force feedback applied on the motor and the energy consumed by the robot are displayed in the `Console`.

### pen.wbt

**Keywords**: Pen, keyboard

![pen.png](images/samples/pen.png) In this example, `MyBot` uses a [Pen](../reference/pen.md) device to draw on the floor.
The controller randomly chooses the ink color.
The ink on the floor fades slowly.
Use the `Y` and `X` keys to switch the [Pen](../reference/pen.md) on and off.

### position\_sensor.wbt

**Keywords**: PositionSensor, force control

![position_sensor.png](images/samples/position_sensor.png) In this example, `MyBot` uses a [PositionSensor](../reference/positionsensor.md) to maintain a red log in balance.

### propeller.wbt

**Keywords**: Propeller, rotors, fan

![propeller.png](images/samples/propeller.png) In this example, 3 helicopters with different designs demonstrate the use of the `Propeller` node.

- *Red helicopter*: It is composed of axial and tail rotors.
- *Green helicopter*: It is composed of 2 coaxial rotors.
- *Blue helicopter*: It is composed of a single axial rotor.

### radar.wbt

**Keywords**: Radar

![radar.png](images/samples/radar.png) In this example, the `MyBot` with the black box detects the `MyBot`s with red boxes.
The black box is a [Radar](../reference/radar.md) device, while the red boxes are [Solids](../reference/solid.md) with a positive `radarCrossSection` (this is required to be detected by the [Radar](../reference/radar.md)).

### range\_finder.wbt

**Keywords**: RangeFinder

![range_finder.png](images/samples/range_finder.png) In this example, `MyBot` uses a [RangeFinder](../reference/rangefinder.md) to avoid obstacles.
The [RangeFinder](../reference/rangefinder.md) measures the distance to objects, so the robot knows if there is enough room to move forward or not.

### receiver\_noise.wbt

**Keywords**: Receiver, signal strength, direction noise

![receiver_noise.png](images/samples/receiver_noise.png) In this example, the `MyBot` at the center uses its [Receiver](../reference/receiver.md) device to get the [Emitter](../reference/emitter.md) device position of the other `MyBot`.
This noisy position is compared to the actual [Emitter](../reference/emitter.md) position measured with a noise-free [GPS](../reference/gps.md).

### sick.wbt

**Keywords**: Sick LMS 291, Lidar, 3-wheeled robot, lidar plot

![sick.png](images/samples/sick.png) In this example, a 3-wheeled robot mounted with a `Sick LMS 291` lidar sensor moves through an area with obstacles.
The robot use the lidar depth output to avoid collisions.
The lidar depth output is also plot into a [Display](../reference/display.md) device.

### speaker.wbt

**Keywords**: Speaker, WAV

![speaker.png](images/samples/speaker.png) In this example, a `Speaker` device is mounted on the `MyBot`.
A WAV file is played on this speaker, while the `MyBot` is moving over the camera.
The intensity of the left and right audio channels differs depending on the robot position.
The Webots sound should be enabled to hear the result on the computer loudspeakers.

### speaker\_text\_to\_speech.wbt

**Keywords**: Speaker, text to speech

![speaker_text_to_speech.png](images/samples/speaker_text_to_speech.png) In this example, a `Speaker` device is mounted on the `MyBot`.
A text formated in XML is played in this speaker.
This text is containing voice modulations including pitch, rate and volume modifications.
The Webots sound should be enabled to hear the result on the computer loudspeakers.

### spherical\_camera.wbt

**Keywords**: Camera, spherical projection

![spherical_camera.png](images/samples/spherical_camera.png) In this example, a spherical [Camera](../reference/camera.md) device is mounted on the `MyBot`.
The resulting projection is shown in a 2D camera overlay.

### supervisor.wbt

**Keywords**: Supervisor, queries on scene tree

![supervisor.png](images/samples/supervisor.png) This example shows basic operations of a [Supervisor](../reference/supervisor.md) node.
The [Supervisor](../reference/supervisor.md) starts with displaying the names of the scene tree root nodes.
Then it displays the content of the `WorldInfo.gravity` field.
Finally, after eight seconds, it moves the [PointLight](../reference/pointlight.md).

### track.wbt

**Keywords**: Track, caterpillar track, conveyor belt

![track.png](images/samples/track.png) This example shows two use cases of the [Track](../reference/track.md) node.
The [Track](../reference/track.md) node is used to model two caterpillar tracks, and a conveyor belt.
