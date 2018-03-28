## NASA Sojourner

%figure "Sojourner model in Webots"

![model.png](images/robots/sojourner/model.png)

%end

[Sojourner](https://en.wikipedia.org/wiki/Sojourner_(rover)) is the [NASA Pathfinder robotic rover](https://www.nasa.gov/mission_pages/mars-pathfinder) that landed on 1997 in the Ares Vallis region, and explored Mars for around three months.

### Movie Presentation

![youtube video](https://www.youtube.com/watch?v=_9d_vukS0Qg)

### Sojourner PROTO

```
Sojourner {
  SFVec3f    translation         0 0.143 0
  SFRotation rotation            1 0 0 -0.05
  SFString   name                "ERS-7"
  SFString   controller          "ers7"
  SFString   controllerArgs      ""
  SFString   customData          ""
  SFBool     synchronization     TRUE
  SFFloat    camera_fieldOfView  0.993092
  SFInt32    camera_width        208
  SFInt32    camera_height       160
  SFBool     camera_antiAliasing FALSE
  MFNode     extensionSlot       []
  SFString   window              ""
}
```

> **File location**: "WEBOTS\_HOME/projects/robots/nasa/protos/Sojourner.proto"

#### Sojourner Field Summary

- `translation`: Inherited from [Transform](../reference/transform.md) node.

- `rotation`: Inherited from [Transform](../reference/transform.md) node.

- `name`: Inherited from [Solid](../reference/solid.md) node.

- `controller`: Inherited from [Robot](../reference/robot.md) node.

- `controllerArgs`: Inherited from [Robot](../reference/robot.md) node.

- `customData`: Inherited from [Robot](../reference/robot.md) node.

- `synchronization`: Inherited from [Robot](../reference/robot.md) node.

- `camera_fieldOfView`: Inherited from [Camera](../reference/camera.md) node.

- `camera_width`: Inherited from [Camera](../reference/camera.md) node.

- `camera_height`: Inherited from [Camera](../reference/camera.md) node.

- `camera_antiAliasing`: Inherited from [Camera](../reference/camera.md) node.

- `extensionSlot`: Extends the robot with new nodes in the extension slot.

- `window`: Inherited from [Robot](../reference/robot.md) node.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/nasa/worlds".

#### sojourner.wbt

![sojourner.wbt.png](images/robots/sojourner/sojourner.wbt.png) This simulation shows the Sojourner model in a Mars-like environment.
A large obstacle is placed in front of the robot so that it is possible to observe how the robot climbs over it.
The keyboard can be used to control the motion of the robot.
