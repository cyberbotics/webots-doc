## Boston Dynamics' Atlas

%figure "Atlas model in Webots"

![model.png](images/robots/atlas/model.png)

%end

The "Atlas" is a humanoid robot developed by [Boston Dynamics](https://www.bostondynamics.com/atlas) with funding and oversight from DARPA.
The robot is 1.8 meters tall and is designed for a variety of search and rescue tasks.

### Atlas PROTO

```
Atlas {
  SFVec3f    translation     0 1 0
  SFRotation rotation        1 0 0 -1.5708
  SFString   name            "Atlas"
  SFString   controller      "hello_world_demo"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFNode     pelvisSlot      []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/boston_dynamics/atlas/protos/Atlas.proto"

#### Atlas Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `pelvisSlot`: Extends the robot with new nodes in the pelvis slot.

### Samples

You will find the following sample in the folder: "WEBOTS\_HOME/projects/robots/boston_dynamics/atlas/worlds".

#### atlas.wbt

![atlas.wbt.png](images/robots/atlas/atlas.wbt.png) This simulation shows an Atlas robot in a simple environment. The robot is moving its right arm.
