## K-Team's Khepera III

%figure "Khepera III model in Webots"

![model.png](images/robots/khepera3/model.png)

%end

The "Khepera III" robot is a two-wheeled robot produced by [K-Team](https://www.k-team.com/mobile-robotics-products/old-products/khepera-iii).
It is mounted by multiple sensors including 8 distance sensors.

### Khepera3 PROTO

```
Khepera3 {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "Khepera III"
  SFString   controller      "braitenberg"
  SFString   controllerArgs  ""
  SFString   customData      ""
  SFBool     synchronization TRUE
  SFString   wheelMaterial   "default"
  SFString   bodyMaterial    "default"
  MFNode     turretSlot      []
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/k-team/khepera3/protos/Khepera3.proto"

#### Khepera3 Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `wheelMaterial`: Defines the [Solid](../reference/solid.md) for the wheels.

- `bodyMaterial`: Defines the [Solid](../reference/solid.md) for the body.

- `turretSlot`: Extends the robot with new nodes in the turret slot.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/k-team/khepera3/worlds":

#### khepera3.wbt

![khepera3.wbt.png](images/robots/khepera3/khepera3.wbt.png) In this example, you can see a Khepera III robot moving inside an arena while avoiding the walls.
It uses a Braitenberg's vehicle algorithm to avoid obstacles.

#### khepera3\_gripper.wbt

![khepera3_gripper.wbt.png](images/robots/khepera3/khepera3_gripper.wbt.png) In this example, you can see a Khepera III robot mounted with a gripper.
It grabs an orange stick, moves and leaves the stick.
