## Unimation's PUMA 560

%figure "PUMA 560 model in Webots"

![model.png](images/robots/puma/model.png)

%end

The [PUMA robotic arm](https://en.wikipedia.org/wiki/Programmable_Universal_Machine_for_Assembly#Model_560_C) (for "Programmable Universal Machine for Assembly") is a six axes arm with three axes making up a spherical wrist.

### Movie Presentation

![youtube video](https://www.youtube.com/watch?v=tjOhGqOHfhg)

### Puma560 PROTO

```
Puma560 {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "PUMA 560"
  SFString   controller      "puma560"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFNode     bodySlot        []
  MFNode     gripperSlot     []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/unimation/puma/protos/Puma560.proto"

#### Puma560 Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `bodySlot`: Extends the robot with new nodes in the body slot.

- `gripperSlot`: Extends the robot with new nodes in the gripper slot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/unimation/puma/worlds".

#### puma560.wbt

![puma560.wbt.png](images/robots/puma/puma560.wbt.png) This simulation shows the PUMA robot which moves to different targets.
