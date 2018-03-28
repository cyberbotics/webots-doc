## ROBOTIS' DARwIn-OP

%figure "DARwIn-OP model in Webots"

![model.png](images/robots/darwin-op/model.png)

%end

Please refer to the [ROBOTIS OP2](robotis-op2.md) documentation.

### Darwin-op PROTO

```
Darwin-op {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "DARwIn-OP"
  SFString   controller      "motion_player"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFFloat    battery         []
  SFBool     selfCollision   FALSE
  SFColor    plasticColor    0.301961 0.301961 0.301961
  SFInt32    cameraWidth     160
  SFInt32    cameraHeight    120
  SFNode     jersey          NULL
  SFInt32    channel         0
  SFBool     showWindow      FALSE
  MFNode     bodySlot        []
  MFNode     headSlot        []
  MFNode     leftFootSlot    []
  MFNode     rightFootSlot   []
  MFNode     leftHandSlot    []
  MFNode     rightHandSlot   []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/robotis/darwin-op/protos/Darwin-op.proto"

#### Darwin-op Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `battery`: Inherited from [Robot](../reference/robot.md) node.

- `selfCollision`: Inherited from [Robot](../reference/robot.md) node.

- `plasticColor`: Inherited from [Material](../reference/material.md) node.

- `cameraWidth`: Inherited from [Camera](../reference/camera.md) node.

- `cameraHeight`: Inherited from [Camera](../reference/camera.md) node.

- `jersey`: Extends the robot with a jersey: typically RobotisJersey.proto.

- `channel`: Defines the channel for the [Emitter](../reference/emitter.md) and [Receiver](../reference/receiver.md) devices.

- `showWindow`: Inherited from [Robot](../reference/robot.md) node.

- `bodySlot`: Extends the robot with new nodes in the body slot.

- `headSlot`: Extends the robot with new nodes in the head slot.

- `leftFootSlot`: Extends the robot with new nodes in the left foot slot.

- `rightFootSlot`: Extends the robot with new nodes in the right foot slot.

- `leftHandSlot`: Extends the robot with new nodes in the left hand slot.

- `rightHandSlot`: Extends the robot with new nodes in the right hand slot.
