## Real Robots

This section discusses worlds containing models of real robots.
The world files for these examples are located in the "robots/(robot\_name)/worlds" directory, and the corresponding controllers are located in the "robots/(robot\_name)/controllers" directory.

### koala.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, Koala

%figure "koala"

![koala.png](images/koala.png)

%end

In this example, you can see a Koala robot from K-Team moving inside an arena while avoiding the walls.
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
