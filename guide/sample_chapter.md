# Sample Webots Applications

This chapter gives an overview of sample worlds provided with the Webots
package. The examples world can be tried easily; the ".wbt" files are located in
various "worlds" directories of the "WEBOTS_MODULES_PATH/projects" directory and
can be directly opened from Webots using the `Open Sample World` item in `File`
menu. The controller code is located in the corresponding "controllers"
directory. This chapter provides each example a with short abstract only. More
detailed explanations can be found in the source code.

## Samples

This section provides a list of interesting worlds that broadly illustrate
Webots capabilities. Several of these examples have stemmed from research or
teaching projects. You will find the corresponding ".wbt" files in the
"WEBOTS_MODULES_PATH/projects/samples/demos/worlds" directory, and their
controller source code in the
"WEBOTS_MODULES_PATH/projects/samples/demos/controllers" directory. For each
demo, the world file and its corresponding controller have the same name.

### blimp_lis.wbt

![blimp_lis.wbt](png/blimp_lis.png)
**blimp_lis.wbt**

This is an example of the flying blimp robot developed at the Laboratory of
Intelligent Systems (LIS) at EPFL. You can use your keyboard, or a joystick to
control the blimp's motion across the room. Use the up, down, right, left, page
up, page down and space (reset) keys. Various `Transform` and `IndexedFaceSet`
nodes are used to model the room using textures and transparency. A *physics
plugin* is used to add thrust and other forces to the simulation.

### gantry.wbt

![gantry.wbt](png/gantry.png)
**gantry.wbt**

In this example, a gantry robot plays "Towers of Hanoi" by stacking three
colored boxes. The gantry robot is modeled using a combination of `LinearMotor`
and `RotationalMotor` devices. A recursive algorithm is used to solve the Hanoi
Towers problem.

### hexapod.wbt

![hexapod.wbt](png/hexapod.png)
**hexapod.wbt**

In this example, an insect-shaped robot is made of a combination of
`LinearMotor` and `RotationalMotor` devices. The robot moves using an
alternating tripod gait.

### humanoid.wbt

![humanoid.wbt](png/humanoid.png)
**humanoid.wbt**

In this example, a humanoid robot performs endless gymnastic movements.

### moon.wbt

![moon.wbt](png/moon.png)
**moon.wbt**

In this example, two Koala robots (K-Team) circle on a moon-like surface. You
can modify their trajectories with the arrow keys on your keyboard. The moon-
like scenery is made of `IndexedFaceSet` nodes. Both robots use the same
controller code.

### ghostdog.wbt

![ghostdog.wbt](png/ghostdog.png)
**ghostdog.wbt**

This example shows a galloping quadruped robot made of active hip joints and
passive knee joints (using spring and dampers). The keyboard can be used to
control the robot's direction and to change the amplitude of the galloping
motion. Each knee is built of two embedded HingeJoint nodes, one active and one
passive, sharing the same rotation axis. The passive HingeJoint simulates the
spring and damping. The active HingeJoint is not actuated in this demo but it
could be used for controlling the knee joints.

### salamander.wbt

![salamander.wbt](png/salamander.png)
**salamander.wbt**

A salamander-shaped robot walks down a slope and reaches a pool where it starts
to swim. The controller uses two different types of locomotion: it walks on the
ground and swims in the water. This demo simulates propulsive forces caused by
the undulations of the body and the resistance caused by the robot's shape. In
addition, the buoyancy of the robot's body is also simulated using Archimedes'
principle.

### soccer.wbt

![soccer.wbt](png/soccer_world.png)
**soccer.wbt**

In this example, two teams of simple `DifferentialWheels` robots play soccer. A
`Supervisor` is used as the referee; it counts the goals and displays the
current score and the remaining time in the 3D view. This example shows how a
`Supervisor` can be used to read and change the position of objects.

### sojourner.wbt

![sojourner.wbt](png/sojourner.png)
**sojourner.wbt**

This is a realistic model of the "Sojourner" Mars exploration robot (NASA). A
large obstacle is placed in front of the robot so that it is possible to observe
how the robot manages to climb over it. The keyboard can be used to control the
robot's motion.

### yamor.wbt

![yamor.wbt](png/yamor.png)
**yamor.wbt**

In this example, eight "Yamor" robot modules attach and detach to and from each
other using `Connector` devices. Connector devices are used to simulate the
mechanical connections of docking systems. In this example, the robot modules go
through a sequence of loops and worm-like configurations while changing their
mode of locomotion. All modules use the same controller code, but their actual
module behaviour is chosen according to the name of the module.

### stewart_platform.wbt

![stewart_platform.wbt](png/stewart_platform.png)
**stewart_platform.wbt**

This is an example of a *Stewart platform*. A Stewart platform is a kind of
parallel manipulator that uses an octahedral assembly of linear actuators. It
has six degrees of freedom (*x*, *y*, *z*, pitch, roll, and yaw). In this
example, the Stewart platform is loaded with a few stacked boxes, then the
platform moves and the boxes stumble apart. This simulation attaches both ends
of the linear actuators (hydraulic pistons) to the lower and the upper parts of
the Stewart platform.

## Webots Devices

This section provides a simple example for each Webots device. The world files
are located in the "WEBOTS_MODULES_PATH/projects/samples/devices/worlds"
directory, and their controllers in the
"WEBOTS_MODULES_PATH/projects/samples/devices/controllers" directory. The world
files and the corresponding controller are named according to the device they
exemplify.

### battery.wbt

![battery.wbt](png/battery.png)
**battery.wbt**

In this example, a robot moves in a closed arena. The energy consumed by the
wheel motors slowly discharges the robot's battery. When the battery level
reaches zero, the robot is powered off. In order to remain powered, the robot
must recharge its battery at energy chargers. Chargers are represented by the
semi-transparent colored cylinders in the four corners of the arena. Only a full
charger can recharge the robot's battery. The color of a charger changes with
its energy level: it is red when completely empty and green when completely
full.

### bumper.wbt

![bumper.wbt](png/bumper.png)
**bumper.wbt**

In this example, a robot moves in a closed arena filled with obstacles. Its
"bumper" `TouchSensor` is used to detect collisions. Each time a collision is
detected, the robot moves back and turns a bit.

### camera.wbt

![camera.wbt](png/camera.png)
**camera.wbt**

In this example, a robot uses a camera to detect colored objects. The robot
analyses the RGB color level of each pixel of the camera images. It turns and
stops for a few seconds when it has detected something. It also prints a message
in the Console explaining the type of object it has detected. You can move the
robot to different parts of the arena (using the mouse) to see what it is able
to detect.

### connector.wbt

![connector.wbt](png/connector.png)
**connector.wbt**

In this example, a light robot (light blue) is lifted over two heavier robots
(dark blue). All three robots are equipped with a `Connector` placed at the tip
of a moveable handle (`HingeJoint`). An `IndexedLineSet` is added to every
`Connector` in order to show the axes. When the simulation starts, the light
robot approaches the first heavy robot and their connectors dock to each other.
Then both robots rotate their handles simultaneously, and hence the light robot
gets passed over the heavy one. Then the light robot gets passed over another
time the second heavy robot and so on ... All the robots in this simulation use
the same controller; the different behaviors are selected according to the
robot's name.

### distance_sensor.wbt

![distance_sensor.wbt](png/distance_sensor.png)
**distance_sensor.wbt**

In this example, a robot has eight `DistanceSensor`s placed at regular intervals
around its body. The robot avoids obstacles using the Braitenberg technique.

### emitter_receiver.wbt

![emitter_receiver.wbt](png/emitter_receiver.png)
**emitter_receiver.wbt**

In this example, there are two robots: one is equipped with an `Emitter`, the
other one with a `Receiver`. Both robots move among the obstacles while the
*emitter* robot sends messages to the *receiver* robot. The range of the
`Emitter` device is indicated by the radius of the transparent sphere around the
emitter robot. The state of the communication between the two robots is
displayed in the Console. You can observe that when the *receiver* robot enters
the *receiver*'s sphere, and that at the same time there is no obstacle between
the robots, then the communication is established, otherwise the communication
is interrupted. Note that the communication between "infra-red" `Emitter`s and
`Receiver`s can be blocked by an obstacle, this is not the case with "radio"
`Emitter`s and `Receiver`s.

### encoders.wbt

![encoders.wbt](png/encoders.png)
**encoders.wbt**

This example demonstrates the usage of the wheel encoders of
`DifferentialWheels` robots. The controller randomly chooses target encoder
positions, then it rotates its wheels until the encoder values reach the chosen
target position. Then the encoders are reset and the controller chooses new
random values. The robot does not pay any attention to obstacles.

### force_sensor.wbt

![force_sensor.wbt](png/force_sensor.png)
**force_sensor.wbt**

This example is nearly the same as "bumper.wbt" (see ). The only difference is
that this robot uses a "force" `TouchSensor` instead of a "bumper". So this
robot can measure the force of each collision, which is printed in the Console
window.

### gps.wbt

![gps.wbt](png/gps.png)
**gps.wbt**

This example shows two different techniques for finding out the current position
of a robot. The first technique consists in using an on-board `GPS` device. The
second method uses a `Supervisor` controller that reads and transmits the
position info to the robot. Note that a `Supervisor` can read (or change) the
position of any object in the simulation at any time. This example implements
both techniques, and you can choose either one or the other with the keyboard.
The 'G' key prints the robot's GPS device position. The 'S' key prints the
position read by the Supervisor.

### led.wbt

![led.wbt](png/led.png)
**led.wbt**

In this example, a robot moves while randomly changing the color of three `LED`s
on the top of its body. The color choice is printed in the Console.

### light_sensor.wbt

![light_sensor.wbt](png/light_sensor.png)
**light_sensor.wbt**

In this example, the robot uses two `LightSensor`s to follow a light source. The
light source can be moved with the mouse; the robot will follow it.

### pen.wbt

![pen.wbt](png/pen.png)
**pen.wbt**

In this example, a robot uses a `Pen` device to draw on the floor. The
controller randomly chooses the ink color. The ink on the floor fades slowly.
Use the 'Y' and 'X' keys to switch the `Pen` on and off.

### range_finder.wbt

![range_finder.wbt](png/range_finder.png)
**range_finder.wbt**

In this example, the robot uses a "range-finder" `Camera` to avoid obstacles.
The "range-finder" measures the distance to objects, so the robot knows if there
is enough room to move forward.

## How To

This section gives various examples of complexe behaviours and/or
functionalities. The world files are located in the
"WEBOTS_MODULES_PATH/projects/samples/howto/world" directory, and their
controllers in the "WEBOTS_MODULES_PATH/projects/samples/howto/controllers"
directory. For each, the world file and its corresponding controller are named
according to the behaviour they exemplify.

### binocular.wbt

![binocular.wbt](png/binocular.png)
**binocular.wbt**

This example simply shows how to equip a robot with two `Camera`s for
stereovision. The example does not actually perform stereovision or any form of
computer vision.

### biped.wbt

![biped.wbt](png/biped.png)
**biped.wbt**

In this example, a biped robot stands up while his head rotates. After a few
seconds, all the motors are turned off and the robot collapses. This example
illustrates how to build a simple articulated robot and also how to turn off
motor power.

### force_control.wbt

![force_control.wbt](png/force_control.png)
**force_control.wbt**

This world shows two boxes connected by a `LinearMotor`. Here, the purpose is to
demonstrate the usage of the `wb_motor_set_force()` function to control a
`LinearMotor` with a user specified force. In this example,
`wb_motor_set_force()` is used to simulate the effect of a spring and a damper
between the two boxes. When the simulation starts, the motor force is used to
move the boxes apart. Then the motor force is turned off and boxes oscillate for
a while now according to the spring and damping equations programmed in the
controller.

### inverted_pendulum.wbt

![inverted_pendulum.wbt](png/inverted_pendulum.png)
**inverted_pendulum.wbt**

In this example, a robot moves from left to right in order to keep an inverted
pendulum upright. This is known as the "Inverted Pendulum Problem", and it is
solved in our example by using a PID (Proportional Integral Differential)
controller.

### physics.wbt

![physics.wbt](png/physics.png)
**physics.wbt**

In this example, a robot flies using a physics plugin. This plugins is an
example of:

### supervisor.wbt

![supervisor.wbt](png/supervisor.png)
**supervisor.wbt**

This shows a simple soccer game with six robots and a referee. The `Supervisor`
code demonstrates the usage of several `Supervisor` functions. For example, the
`Supervisor` inserts a second ball to the simulation, changes its color, takes a
picture of the 3D view, restarts the simulation, etc. In addition the
`Supervisor` also plays the role of a soccer referee: it displays the current
score, places the players to their initial position when a goal is scored, etc.

### texture_change.wbt

![texture_change.wbt](png/texture_change.png)
**texture_change.wbt**

In this example, a robot moves forward and backward in front of a large textured
panel. The robot watches the panel with its `Camera`. Meanwhile a `Supervisor`
switches the image displayed on the panel.

### town.wbt

![town.wbt](png/town.png)
**town.wbt**

This example shows a complex city model built with various `Transform` nodes.
The model makes a intensive use of the `DEF` and `USE` VRML keywords.

## Geometries

This section shows the geometric primitives available in Webots. The world files
for these examples are located in the "sample/geometries /worlds" directory.

In this directory, you will find the following world files :

## Real Robots

This section discusses worlds containing models of real robots. The world files
for these examples are located in the "robots/(robot_name)/worlds" directory,
and the corresponding controllers are located in the
"robots/(robot_name)/controllers" directory.

### aibo_ers210_rough.wbt

![aibo_ers210_rough.wbt](png/aibo_ers210_rough.png)
**aibo_ers210_rough.wbt**

In this example, you can see a silver Aibo ERS-210 robot walking on an uneven
floor while a ball rolls and falls off. The uneven floor is principally made of
a `IndexedFaceSet`.

### aibo_ers7.wbt

![aibo_ers7.wbt](png/aibo_ers7.png)
**aibo_ers7.wbt**

In this example, you can see a silver Aibo ERS-7 robot walking on a textured
soccer field. On this field you can also see its toys : a ball, a charger and a
bone.

### alice.wbt

![alice.wbt](png/alice.png)
**alice.wbt**

In this example, you can see an Alice robot moving inside an arena while
avoiding the walls. Its world file is in the "others/worlds" directory. Like
many others, this example uses the `braitenberg` controller.

### boebot.wbt

![boebot.wbt](png/boebot.png)
**boebot.wbt**

In this example, BoeBot moves inside an arena while avoiding the walls. When the
robot detects an obstacle with one of its `DistanceSensor`s, it turns the
corresponding `LED` on.

### e-puck.wbt

![e-puck.wbt](png/e-puck.png)
**e-puck.wbt**

In this example, you can see the e-puck robot avoiding obstacles inside an arena
by using the Braitenberg technique. The odometry of the e-puck is computed at
each simulation steps. The accelerometer values and an estimation the coverage
distance and the orientation of the e-puck are displayed. The source code for
this controller is in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### e-puck_line.wbt

![e-puck_line.wbt](png/e-puck_line.png)
**e-puck_line.wbt**

In this example, you can see the E-puck robot following a black line drawn on
the ground. In the middle of this line there is an obstacle which the robot is
unable to avoid. This example has been developed as a practical assignment on
behavior-based robotics. When completed, the controller should allow the E-puck
robot to avoid this obstacle and recover its path afterwards. A solution for
this assignment is shown in the world e-puck_line_demo.wbt (see ). The source
code for this controller is in the "e-puck_line" directory.

### e-puck_line_demo.wbt

![e-puck_line_demo.wbt](png/e-puck_line_demo.png)
**e-puck_line_demo.wbt**

This example is the solution for the assignment given in the
`e-puck_line_demo.wbt` example (see ). In this case, you can see that the robot
avoids the obstacle, then recovers its path along the line. As the controller
used in this world is the solution to the assignment, the source code is not
distributed.

### hemisson_cross_compilation.wbt

![hemisson_cross_compilation.wbt](png/hemisson_cross_compilation.png)
**hemisson_cross_compilation.wbt**

In this example, a Hemisson robot moves on a white floor while avoiding the
obstacles. Its `Pen` device draws a black line which slowly fades. This example
is a cross-compilation example for the real Hemisson robot. The source code for
this controller is in the "hemisson" directory.

### hoap2_sumo.wbt

![hoap2_sumo.wbt](png/hoap2_sumo.png)
**hoap2_sumo.wbt**

In this example, a Hoap2 robot from Fujitsu performs the Shiko dance (the dance
which sumos perform before a match). This robot is equipped with `TouchSensors`
on the soles of its feet; it measures and logs the pressure exerted by its body
on the ground. The source code for this controller is in the "hoap2" directory.

### hoap2_walk.wbt

![hoap2_walk.wbt](png/hoap2_walk.png)
**hoap2_walk.wbt**

In this example, a Hoap2 robot from Fujitsu walks straight forward on a tatami.
This robot is equipped with `TouchSensors` on the soles of its feet; it measures
and logs the pressure exerted by its body on the ground. The source code for
this controller is in the "hoap2" directory.

### ipr_collaboration.wbt

![ipr_collaboration.wbt](png/ipr_collaboration.png)
**ipr_collaboration.wbt**

In this example, two IPR robots from Neuronics work together to put three red
cubes into a basket which is on the opposite side of the world. All the IPR
robots use the same controller, whose source code is in the "ipr_serial"
directory. This particular example uses, in addition to this controller, a
client program which coordinates the movements of the robots. The source code
for this client is in the "ipr_serial/client/ipr_collaboration.c" file.

### ipr_cube.wbt

![ipr_cube.wbt](png/ipr_cube.png)
**ipr_cube.wbt**

In this example, an IPR robots from Neuronics moves a small red cube onto a
bigger one. All the IPR robots use the same controller, whose source code is in
the "ipr_serial" directory. This example also uses a client program which drives
the movements of the robot. The source code of this client is in the
"ipr_serial/client/ipr_cube.c" file.

### ipr_factory.wbt

![ipr_factory.wbt](png/ipr_factory.png)
**ipr_factory.wbt**

In this example, two IPR robots from Neuronics take industrial parts from a
conveyor belt and place them into slots. One of the robots detects the objects
using an infrared sensor on the conveyor belt, while the other one waits. All
the IPR robots use the same controller, whose source code is in the "ipr_serial"
directory. This example also uses a client program which coordinates the
movements of the robots. The source code for this client is in the file
"ipr_serial/client/ipr_factory.c".

### ipr_models.wbt

![ipr_models.wbt](png/ipr_models.png)
**ipr_models.wbt**

In this example, you can see all the different types of IPR model provided by
Webots : HD6M180, HD6Ms180, HD6M90 and HD6Ms90. This world is intended to be the
example from which you can copy the models of IPR robots into your own worlds.
All the IPR robots use the same controller, whose source code is in the
"ipr_serial" directory.

### khepera.wbt

![khepera.wbt](png/khepera.png)
**khepera.wbt**

In this example, you can see a Khepera robot from K-Team moving inside an arena
while avoiding the walls. Like many other examples, this one uses the
`braitenberg` controller. The source code for this controller is located in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### khepera2.wbt

![khepera2.wbt](png/khepera2.png)
**khepera2.wbt**

In this example, you can see a Khepera II robot from K-Team moving inside an
arena while avoiding the walls. Like many other examples, this one uses the
`braitenberg` controller. The source code for this controller is in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### khepera3.wbt

![khepera3.wbt](png/khepera3.png)
**khepera3.wbt**

In this example, you can see a Khepera III robot from K-Team moving inside an
arena while avoiding the walls. Like many other examples, this one uses the
`braitenberg` controller. The source code for this controller is in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### khepera_kinematic.wbt

![khepera_kinematic.wbt](png/khepera_kinematic.png)
**khepera_kinematic.wbt**

In this example, you can see two Khepera robots from K-Team moving inside an
arena while avoiding each other and the walls. It is a good example of how to
use teh kinematic mode of Webots. Like many other examples, this one uses the
`braitenberg` controller. The source code for this controller is in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### khepera_gripper.wbt

![khepera_gripper.wbt](png/khepera_gripper.png)
**khepera_gripper.wbt**

In this example, you can see a Khepera robot from K-Team equipped with a
gripper. The robot uses its gripper to grab a stick, move a bit with it and drop
it on the ground. This behavior is repeated endlessly. The source code for this
controller is in the "khepera_gripper" directory.

### khepera_gripper_camera.wbt

![khepera_gripper_camera.wbt](png/khepera_gripper_camera.png)
**khepera_gripper_camera.wbt**

In this example, you can see a Khepera robot from K-Team equipped with a gripper
and a `Camera` device. The robot uses its gripper to grab a stick, move a bit
with it and drop it on the floor. This behavior is repeated endlessly. In this
world, the robot does not analyse the images it takes with its camera. The
source code for this controller is in the "khepera_gripper" directory.

### khepera_k213.wbt

![khepera_k213.wbt](png/khepera_k213.png)
**khepera_k213.wbt**

In this example, you can see a Khepera robot from K-Team equipped with a K213
`Camera` device. This camera is a linear vision turret with greyscale images.
Using this device, the robot is able to translate the information contained in
the image into text and print this result in the Console window. When you load
this world, the robot will not begin to move immediately. It will give you
enough time to read the explanations printed in the Console window concerning
this world. The source code for this controller is in the "khepera_k213"
directory.

### khepera_pipe.wbt

![khepera_pipe.wbt](png/khepera_pipe.png)
**khepera_pipe.wbt**

In this example, you can see a Khepera robot from K-Team inside an arena. The
controller for this robot opens a UNIX pipe in order to receive commands using
the Khepera serial communication protocol. This example is provided with a
sample client program which interacts with the controller of the robot to make
it move straight forward until it detects an obstacle. This client program
`client` must be launched separately from Webots. The source code for this
controller and for the client program are in the "pipe" directory.

### khepera_tcpip.wbt

![khepera_tcpip.wbt](png/khepera_tcpip.png)
**khepera_tcpip.wbt**

In this example, you can see a Khepera robot from K-Team inside an arena. The
controller for this robot acts as a TCP/IP server, waiting for a connection.
Through this connection, the robot can receive commands using the Khepera serial
communication protocol. This example is provided with a sample client program
which displays a command prompt, with which you can control the movements of the
robot. This client program `client` must be launched separately from Webots. The
source code for this controller and for the client program are in the "tcpip"
directory.

### koala.wbt

![koala.wbt](png/koala.png)
**koala.wbt**

In this example, you can see a Koala robot from K-Team moving inside an arena
while avoiding the walls. Like many other examples, this one uses the
`braitenberg` controller. The source code for this controller is located in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### magellan.wbt

![magellan.wbt](png/magellan.png)
**magellan.wbt**

In this example, you can see a Magellan robot moving inside an arena while
avoiding the walls. As this robot is no longer produced, its world file is in
the "others/worlds" directory. Like many other examples, this one uses the
`braitenberg` controller. The source code for this controller is located in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### pioneer2.wbt

![pioneer2.wbt](png/pioneer2.png)
**pioneer2.wbt**

In this example, you can see a Pioneer 2 robot from ActivMedia Robotics moving
inside an arena while avoiding the walls. Like many other examples, this one
uses the `braitenberg` controller. The source code for this controller is in the
"WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### rover.wbt

![rover.wbt](png/rover_world.png)
**rover.wbt**

In this example you can see the Mindstorms Rover robot from LEGO following a
black line drawn on the ground. In the middle of this line there is an obstacle
which the robot navigates around after detecting a collision with it. The robot
will then recover its path. As this robot is a *Mindstorms* robot, its world
file and its controller are in the "mindstorms" directory. This example is
written both in Java and C, as a reference for translating Webots code from one
language to another. The source code for this controller is in the "Rover"
directory.

### scout2.wbt

![scout2.wbt](png/scout2.png)
**scout2.wbt**

In this example, a Scout 2 robot moves inside an arena while avoiding the walls.
Its world file is in the "others/worlds" directory. Like many other examples,
this one uses the braitenberg controller. The source code for this controller is
in the "WEBOTS_MODULES_PATH/projects/default/controllers/braitenberg" directory.

### shrimp.wbt

![shrimp.wbt](png/shrimp.png)
**shrimp.wbt**

This example contains a model of the *Shrimp* robot, which is a mobile platform
for rough terrain from `Bluebotics`. It has 6 wheels and a passive structure
which allows it to adapt to the terrain profile and climb obstacles. It can also
turn on the spot. In this example the robot will first move on its own to the
center of the world; then you may drive it yourself using the keyboard. To find
out which keys will allow you to perform these operations, please read the
explanation message printed at the beginning of the simulation in the Console
window.

Because of its particular structure, this model is also an example of custom ODE
plugins for:

The source code for this controller is in the
"WEBOTS_MODULES_PATH/projects/robots/shrimp/controllers/shrimp" directory, and
the ODE plugin is in the
"WEBOTS_MODULES_PATH/projects/robots/shrimp/plugins/physics/shrimp" directory.

### bioloid.wbt

![bioloid.wbt](png/bioloid.png)
**bioloid.wbt**

In this example, the four-legged robot model ( (a)) corresponds to a real
`Bioloid` robot ( (b)) developed by and commercially available from `Tribotix`.
This dog-robot model was build from the Bioloid Comprehensive Kit.

Both the visual aspect and the physical properties of the real robot have been
modeled. The physical dimensions, friction coefficients and mass distribution
have been estimated after various measurements on the components of the real
robot.

The source code for the controller of the robot, as well as the model of the
robot are located under the Webots installation directory, in the
"WEBOTS_MODULES_PATH/projects/robots/bioloid" sub folder:

Using the keyboard, the user can control the quadruped robot by setting the
walking direction (forward or backwards) and also the heading direction (right
or left). Keyboard actions include:

The walking gait used in the controller relies on an inverse kinematics model.
Further details are available from `BIRG web site`. The  included controller
illustrates a trotting gait showing the best performance so far. The turning
capabilities of the robot are based on the stride length modulation. When the
robot is asked to turn right, the stride length of the right side and left side
are respectively decreased and increased. During the walk, the extremity of each
leg is describing an ellipsoid, the diameters of these ellipsoids are updated
according to the stride length to allow the robot to turn either right or left.

Other keyboard actions are also provided to fine-tune the frequency and the
stride length factor:

