## Using the IPR robot

%figure "IPR"

![ipr.png](images/ipr.png)

%end

The IPR robot is a robotic arm developed by [Neuronics](http://www.neuronics.be/).
Four models are currently supported in Webots: HD6M180, HD6Ms180, HD6M90 and HD6Ms90 which include 7 motors and 9 sensors.

More information is available on the Neuronics official [webpage](http://www.neuronics.be/).

### IPR models

XXX.

### Samples

Here are listed the different example worlds based on the IPR.
The worlds and controllers can be accessed in the "WEBOTS\_HOME/projects/robots/sony/aibo" directory.

#### ipr\_collaboration.wbt

![ipr_collaboration.png](images/ipr_collaboration.png) In this example, two IPR robots from Neuronics work together to put three red cubes into a basket which is on the opposite side of the world.
All the IPR robots use the same controller, whose source code is in the "ipr/controllers" directory.
This particular example uses, in addition to this controller, a client program which coordinates the movements of the robots.
The source code for this client is in the "ipr/controllers/ipr\_collaboration.c" file.

#### ipr\_cube.wbt

![ipr_cube.png](images/ipr_cube.png) In this example, an IPR robots from Neuronics moves a small red cube onto a bigger one.
This example also uses a client program which drives the movements of the robot.
The source code for this client is in the "ipr/controllers/ipr\_cube.c" file.

#### ipr\_factory.wbt

![ipr_factory.png](images/ipr_factory.png) In this example, two IPR robots from Neuronics take industrial parts from a conveyor belt and place them into slots.
One of the robots detects the objects using an infrared sensor on the conveyor belt, while the other one waits.
This example also uses a client program which coordinates the movements of the robots.
The source code for this client is in the "ipr/controllers/ipr\_factory.c" file.

#### ipr\_models.wbt

![ipr_models.png](images/ipr_models.png) In this example, you can see all the different types of IPR model provided by Webots : HD6M180, HD6Ms180, HD6M90 and HD6Ms90.
This world is intended to be the example from which you can copy the models of IPR robots into your own worlds.
