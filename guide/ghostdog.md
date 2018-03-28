## BioRob GhostDog

%figure "GhostDog model in Webots"

![model.png](images/robots/ghostdog/model.png)

%end

The "GhostDog" robot is a dog-like robot developed by the [EPFL BioRob laboratory](https://biorob.epfl.ch/).

It is a quadruped robot made of active hip joints and passive knee joints (using springs and dampers).
Each knee is made of two embedded HingeJoint nodes, one active and one passive, sharing the same rotation axis.
The passive HingeJoint simulates the spring and damping.
The active HingeJoint is not actuated in the following demo but it could be used for controlling the knee joints.

### GhostDog PROTO

```
GhostDog {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "GhostDog"
  SFString   controller      "ghostdog"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFNode     extensionSlot   []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/epfl/biorob/protos/GhostDog.proto"

#### GhostDog Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `extensionSlot`: Extends the robot with new nodes in the extension slot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/epfl/biorob/worlds".

#### ghostdog.wbt

![ghostdog.png](images/robots/ghostdog/ghostdog.wbt.png) This example shows the GhostDog robot which gallops.
The keyboard can be used to control the robot's direction and to change the amplitude of the galloping motion.
