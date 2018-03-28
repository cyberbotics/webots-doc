## Parallax's Boe-Bot

%figure "Boe-Bot model in Webots"

![model.png](images/robots/boebot/model.png)

%end

The "Boe-Bot" is a 3 wheeled robot (2 motorized wheels and a passive caster wheel) created by [Parallax Inc.](https://www.parallax.com/product/boe-bot-robot).
Its sensors and actuators can be extended.

### BoeBot PROTO

```
BoeBot {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "BoeBot"
  SFString   controller      "boebot"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFNode     extensionSlot   []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/parallax/boebot/protos/BoeBot.proto"

#### BoeBot Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `extensionSlot`: Extends the robot with new nodes in the extension slot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/parallax/boebot/worlds".

#### boebot.wbt

![boebot.wbt.png](images/robots/boebot/boebot.wbt.png) In this example, BoeBot moves inside an arena while avoiding the walls.
When the robot detects an obstacle with one of its `DistanceSensor`s, it turns the corresponding `LED` on.
