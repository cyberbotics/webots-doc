## LIS Blimp

%figure "Blimp model in Webots"

![model.png](images/robots/blimp/model.png)

%end

The "Blimp" robot is a Zeppelin-like aerial robot developed by the [EPFL LIS laboratory](https://lis.epfl.ch/).

### Blimp PROTO

```
Blimp {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "Blimp"
  SFString   controller      "blimp"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  MFNode     extensionSlot   []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/epfl/lis/protos/Blimp.proto"

#### Blimp Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `extensionSlot`: Extends the robot with new nodes in the extension slot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/epfl/lis/worlds".

### blimp\_lis.wbt

![blimp.png](images/robots/blimp/blimp.wbt.png) This is an example of the flying blimp robot developed at the Laboratory of Intelligent Systems (LIS) at EPFL.
You can use your keyboard, or a joystick to control the Blimp's motion across the room.
Use the up, down, right, left, page up, page down and space (reset) keys.
Various `Transform` and `IndexedFaceSet` nodes are used to model the room using textures and transparency.
A *physics plugin* is used to add thrust and other forces to the simulation.

> **Note**:
`Fluid` and `Propeller` nodes are now recommended to create flying robots.
