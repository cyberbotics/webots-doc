# Create Wall

## CreateWall

%figure "CreateWall model in Webots."

![CreateWall](images/objects/create_wall/CreateWall/model.png)

%end

```
CreateWall {
  SFVec3f    translation 0 0 0
  SFRotation rotation  0 1 0 0
  SFFloat    range 2.4384
  SFFloat    aperture 0.157
  SFString   controller "create_wall_emit_signal"
  SFString   controllerArgs ""
  SFString   name "iRobot wall"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/create_wall/protos/CreateWall.proto"

### CreateWall Description

Virtual walls are an accessory of the IRobot Create allowing to inform the robot about areas typically for restricted access to a room.
