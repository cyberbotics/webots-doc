## Real Robots

This section discusses worlds containing models of real robots.
The world files for these examples are located in the "robots/(robot\_name)/worlds" directory, and the corresponding controllers are located in the "robots/(robot\_name)/controllers" directory.

### alice.wbt

**Keywords**: Alice, Braitenberg, DistanceSensor

%figure "alice"

![alice.png](images/alice.png)

%end

In this example, you can see an Alice robot moving inside an arena while avoiding the walls.
Its world file is in the "others/worlds" directory.
Like many others, this example uses the `braitenberg` controller.

### boebot.wbt

**Keywords**: BoeBot, DistanceSensor, LED

%figure "boebot"

![boebot.png](images/boebot.png)

%end

In this example, BoeBot moves inside an arena while avoiding the walls.
When the robot detects an obstacle with one of its `DistanceSensor`s, it turns the corresponding `LED` on.

### hemisson\_cross\_compilation.wbt

**Keywords**: differential wheels, Pen, cross-compilation, texture, Hemisson

%figure "hemisson_cross_compilation"

![hemisson_cross_compilation.png](images/hemisson_cross_compilation.png)

%end

In this example, a Hemisson robot moves on a white floor while avoiding the obstacles.
Its `Pen` device draws a black line which slowly fades.
This example is a cross-compilation example for the real Hemisson robot.
The source code for this controller is in the "hemisson" directory.

### hoap2\_sumo.wbt

**Keywords**: Robot node, humanoid, texture, dancing, Hoap 2, IndexedFaceSet, RotationalMotor,
    active joint, force, TouchSensor

%figure "hoap2_sumo"

![hoap2_sumo.png](images/hoap2_sumo.png)

%end

In this example, a Hoap2 robot from Fujitsu performs the Shiko dance (the dance sumos perform before a combat).
This robot is equipped with `TouchSensors` on the soles of its feet; it measures and logs the pressure exerted by its body on the ground.
The source code for this controller is in the "hoap2" directory.

### hoap2\_walk.wbt

**Keywords**: Robot node, humanoid, texture, walking, Hoap 2, IndexedFaceSet, RotationalMotor,
    active joint, force, TouchSensor

%figure "hoap2_walk"

![hoap2_walk.png](images/hoap2_walk.png)

%end

In this example, a Hoap2 robot from Fujitsu walks straight forward on a tatami.
This robot is equipped with `TouchSensors` on the soles of its feet; it measures and logs the pressure exerted by its body on the ground.
The source code for this controller is in the "hoap2" directory.

### khepera.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, texture, Khepera

%figure "khepera"

![khepera.png](images/khepera.png)

%end

In this example, you can see a Khepera robot from K-Team moving inside an arena while avoiding the walls.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is located in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.

### khepera2.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, texture, Khepera II

%figure "khepera2"

![khepera2.png](images/khepera2.png)

%end

In this example, you can see a Khepera II robot from K-Team moving inside an arena while avoiding the walls.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.

### khepera3.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, texture, Khepera III

%figure "khepera3"

![khepera3.png](images/khepera3.png)

%end

In this example, you can see a Khepera III robot from K-Team moving inside an arena while avoiding the walls.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.

### khepera\_kinematic.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, Kinematic, Khepera

%figure "khepera_kinematic"

![khepera\_kinematic.png](images/khepera_kinematic.png)

%end

In this example, you can see two Khepera robots from K-Team moving inside an arena while avoiding each other and the walls.
It is a good example of how to use the kinematic mode of Webots.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.

### khepera\_gripper.wbt

**Keywords**: differential wheels, Gripper, Khepera

%figure "khepera_gripper"

![khepera_gripper.png](images/khepera_gripper.png)

%end

In this example, you can see a Khepera robot from K-Team equipped with a gripper.
The robot uses its gripper to grab a stick, move a bit with it and drop it on the ground.
This behavior is repeated endlessly.
The source code for this controller is in the "khepera\_gripper" directory.

### khepera\_gripper\_camera.wbt

**Keywords**: differential wheels, Gripper, Camera, Khepera

%figure "khepera_gripper_camera"

![khepera_gripper_camera.png](images/khepera_gripper_camera.png)

%end

In this example, you can see a Khepera robot from K-Team equipped with a gripper and a `Camera` device.
The robot uses its gripper to grab a stick, move a bit with it and drop it on the floor.
This behavior is repeated endlessly.
In this world, the robot does not analyse the images it takes with its camera.
The source code for this controller is in the "khepera\_gripper" directory.

### khepera\_k213.wbt

**Keywords**: differential wheels, DistanceSensor, K213, linear Camera, Khepera

%figure "khepera_k213"

![khepera_k213.png](images/khepera_k213.png)

%end

In this example, you can see a Khepera robot from K-Team equipped with a K213 `Camera` device.
This camera is a linear vision turret with grayscale images.
Using this device, the robot is able to translate the information contained in the image into text and print this result in the Console window.
When you load this world, the robot will not begin to move immediately.
It will give you enough time to read the explanations printed in the Console window concerning this world.
The source code for this controller is in the "khepera\_k213" directory.

### khepera\_pipe.wbt

**Keywords**: differential wheels, UNIX pipe, client program, Khepera

%figure "khepera_pipe"

![khepera_pipe.png](images/khepera_pipe.png)

%end

In this example, you can see a Khepera robot from K-Team inside an arena.
The controller for this robot opens a UNIX pipe in order to receive commands using the Khepera serial communication protocol.
This example is provided with a sample client program which interacts with the controller of the robot to make it move straight forward until it detects an obstacle.
This client program `client` must be launched separately from Webots.
The source code for this controller and for the client program are in the "pipe" directory.

> **Note**: As this example is based on standard UNIX pipes, it does not work under Windows.

### khepera\_tcpip.wbt

**Keywords**: differential wheels, TCP/IP, client program, Khepera

%figure "khepera_tcpip"

![khepera_tcpip.png](images/khepera_tcpip.png)

%end

In this example, you can see a Khepera robot from K-Team inside an arena.
The controller for this robot acts as a TCP/IP server, waiting for a connection.
Through this connection, the robot can receive commands using the Khepera serial communication protocol.
This example is provided with a sample client program which displays a command prompt, with which you can control the movements of the robot.
This client program `client` must be launched separately from Webots.
The source code for this controller and for the client program are in the "tcpip" directory.

### koala.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, Koala

%figure "koala"

![koala.png](images/koala.png)

%end

In this example, you can see a Koala robot from K-Team moving inside an arena while avoiding the walls.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is located in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.

### magellan.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, Magellan

%figure "magellan"

![magellan.png](images/magellan.png)

%end

In this example, you can see a Magellan robot moving inside an arena while avoiding the walls.
As this robot is no longer produced, its world file is in the "others/worlds" directory.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is located in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.

### pioneer2.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, Pioneer 2

%figure "pioneer2"

![pioneer2.png](images/pioneer2.png)

%end

In this example, you can see a Pioneer 2 robot from ActivMedia Robotics moving inside an arena while avoiding the walls.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.

### rover.wbt

**Keywords**: differential wheels, bumper, TouchSensor, line following, Rover, Java

%figure "rover"

![rover_world.png](images/rover_world.png)

%end

In this example you can see the Mindstorms Rover robot from LEGO following a black line drawn on the ground.
In the middle of this line there is an obstacle which the robot navigates around after detecting a collision with it.
The robot will then recover its path.
As this robot is a *Mindstorms* robot, its world file and its controller are in the "mindstorms" directory.
This example is written both in Java and C, as a reference for translating Webots code from one language to another.
The source code for this controller is in the "Rover" directory.

### scout2.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, Scout 2

%figure "scout2"

![scout2.png](images/scout2.png)

%end

In this example, a Scout 2 robot moves inside an arena while avoiding the walls.
Its world file is in the "others/worlds" directory.
Like many other examples, this one uses the braitenberg controller.
The source code for this controller is in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.
