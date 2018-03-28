## Clearpath Robotics' PR2

%figure "PR2 model in Webots"

![model.png](images/robots/pr2/model.png)

%end

The [clearpath's PR2 robot](http://wiki.ros.org/Robots/PR2) is a mobile manipulation platform.
The robot is mounted on four directional wheels, had two articulated arms with grippers, an articulated body and head.
It is mounted by several sensors including cameras.

### Movie Presentation

![youtube video](https://www.youtube.com/watch?v=Lm0FhXAxkXg)

### Pr2 PROTO

```
Pr2 {
  SFVec3f    translation     0 0 0
  SFRotation rotation        1 0 0 -1.57
  SFString   name            "PR2"
  SFString   controller      "pr2_demo"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  SFBool     selfCollision   FALSE
  MFNode     baseSlot        []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/clearpath/pr2/protos/Pr2.proto"

#### Pr2 Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `selfCollision`: Inherited from [Robot](../reference/robot.md) node.

- `baseSlot`: Extends the robot with new nodes in the base slot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/clearpath/pr2/worlds".

#### pr2.wbt

![pr2.wbt.png](images/robots/pr2/pr2.wbt.png) This simulation shows a PR2 robot grabbing biscuit boxes from one table, and putting them on another table.
