## iRobot's Create

%figure "Create model in Webots"

![model.png](images/robots/create/model.png)

%end

The [iRobot Create](http://www.irobot.com/About-iRobot/STEM/Create-2.aspx) robot is a customizable frame based on the famous Roomba vacuum cleaning platform, and is produced by iRobot.

### Movie Presentation

![youtube video](https://www.youtube.com/watch?v=dEgLYioQycA)

### Create PROTO

```
Create {
  SFVec3f    translation     0 0.044 0
  SFRotation rotation        0 1 0 0
  SFString   name            "Create"
  SFString   controller      "create_avoid_obstacles"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFNode     bodySlot        []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/irobot/create/protos/Create.proto"

#### Create Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `bodySlot`: Extends the robot with new nodes in the body slot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/irobot/create/worlds".

#### create.wbt

![create.wbt.png](images/robots/create/create.wbt.png) This simulation shows the Create robot which cleans a small apartment.
The robot moves straight ahead.
When hitting an obstacle or detecting a virtual wall, the robot turns randomly.
The dust on the ground is a texture of a Display device managed by a Supervisor controller.
The Supervisor removes draws transparent circles into this texture at the robot's location to simulate cleaning dust.
