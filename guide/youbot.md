## KUKA's youBot

%figure "youBot model in Webots"

![model.png](images/robots/youbot/model.png)

%end

The youBot is a mobile robotic arm developed by [KUKA](http://www.youbot-store.com/).
Its arm has five degrees of freedom and a linear gripper.
Its base has four [Mecanum wheels](https://en.wikipedia.org/wiki/Mecanum_wheel) allowing for omnidirectional movement.
These wheels are efficiently modeled using asymmetric friction.

### Movie Presentation

![youtube video](https://www.youtube.com/watch?v=vFwNwT8dZTU)

![youtube video](https://www.youtube.com/watch?v=9Fjyu_wzIgc)

### Samples

You will find some samples in this folder: "WEBOTS\_HOME/projects/robots/kuka/youbot/worlds".

#### youbot.wbt

![youbot.wbt.png](images/robots/youbot/youbot.wbt.png) This simulation shows the youBot grabbing a box, releasing it on its plate, moving to a target, and leaving it on the ground.
Once this automatic behavior is completed, you can move the robot and its arm using the computer keyboard (please refer to the instruction displayed in the Webots console).
A small C library called "youbot_control" (and located there: "WEBOTS\_HOME/projects/robots/kuka/youbot/libraries/youbot_control") facilitate the robot control.

#### youbot\_matlab.wbt

![youbot.wbt.png](images/robots/youbot/youbot.wbt.png) The same simulation as above, but with a controller written in Matlab.

#### tower\_of\_hanoi.wbt

![tower_of_hanoi.wbt.png](images/robots/youbot/tower_of_hanoi.wbt.png) In this simulation, the youBot is moving a pyramid of colored blocks from one position to another, using a temporary slot.
This example is based on the [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) mathematical game.
