## Real Robots

This section discusses worlds containing models of real robots.
The world files for these examples are located in the "robots/(robot\_name)/worlds" directory, and the corresponding controllers are located in the "robots/(robot\_name)/controllers" directory.

### pioneer2.wbt

**Keywords**: differential wheels, DistanceSensor, Braitenberg, Pioneer 2

%figure "pioneer2"

![pioneer2.png](images/pioneer2.png)

%end

In this example, you can see a Pioneer 2 robot from ActivMedia Robotics moving inside an arena while avoiding the walls.
Like many other examples, this one uses the `braitenberg` controller.
The source code for this controller is in the "WEBOTS\_HOME/projects/default/controllers/braitenberg" directory.
