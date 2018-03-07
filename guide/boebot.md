## Parallax's Boe-Bot

%figure "Boe-Bot model in Webots"

![model.png](images/robots/boebot/model.png)

%end

The "Boe-Bot" is a 3 wheeled robot (2 motorized wheels and a passive caster wheel) created by [Parallax Inc.](https://www.parallax.com/product/boe-bot-robot).
Its sensors and actuators can be extended.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/parallax/boebot/worlds".

#### boebot.wbt

![boebot.wbt.png](images/robots/boebot/boebot.wbt.png) In this example, BoeBot moves inside an arena while avoiding the walls.
When the robot detects an obstacle with one of its `DistanceSensor`s, it turns the corresponding `LED` on.
