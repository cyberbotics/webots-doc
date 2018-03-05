## BlueBotics's Shrimp

%figure "Shrimp model in Webots"

![model.png](images/robots/shrimp/model.png)

%end

The "Shrimp" robot is a mobile platform for rough terrain from [Bluebotics](http://www.bluebotics.ch).
It has 6 wheels and a passive structure that adapts to the terrain profile and climbs obstacles.
It can also turn on the spot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/bluebotics/shrimp/worlds".

#### shrimp.wbt

![shrimp.wbt.png](images/robots/shrimp/shrimp.wbt.png) In this example the robot will first move on its own to the center of the world; then you may drive it yourself using the keyboard.
Several obstacles are present in this world.
To find out which keys will allow you to perform these operations, please read the explanation message printed at the beginning of the simulation in the Console window.

Because of its particular structure, this model is also an example of custom ODE plugins for:

- How to create and manage ODE joints.
- How to add custom force.
- How to create spongy tires.
