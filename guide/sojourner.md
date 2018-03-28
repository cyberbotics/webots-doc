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

#### Sojourner PROTO Field Summary

- `translation` is `Transform.translation`.
- `rotation` is `Transform.rotation`.
- `name` is `Solid.name`.
- `controller` is `Robot.controller`.
- `controllerArgs` is `Robot.controllerArgs`.
- `customData` is `Robot.customData`.
- `synchronization` is `Robot.synchronization`.
- `camera_fieldOfView` is `Camera.fieldOfView`.
- `camera_width` is `Camera.width`.
- `camera_height` is `Camera.height`.
- `camera_antiAliasing` is `Camera.antiAliasing`.
- `extensionSlot` extends the robot with new nodes in the extension slot.
- `window` is `Robot.window`.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/nasa/worlds".

#### qrio.wbt

![sojourner.wbt.png](images/robots/sojourner/sojourner.wbt.png) This simulation shows the Sojourner model in a Mars-like environment.
A large obstacle is placed in front of the robot so that it is possible to observe how the robot climbs over it.
The keyboard can be used to control the motion of the robot.
