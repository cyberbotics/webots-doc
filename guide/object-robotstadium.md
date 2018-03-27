# Robotstadium

## RobotstadiumGoal

%figure "RobotstadiumGoal model in Webots."

![RobotstadiumGoal](images/objects/robotstadium/RobotstadiumGoal/model.png)

%end

```
RobotstadiumGoal {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "robotstadium goal"
  SFFloat    postRadius  0.05                 
  SFColor    frameColor  1 1 1                
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/robotstadium/protos/RobotstadiumGoal.proto"

### RobotstadiumGoal Description

Robot soccer goal inspired from the RoboCup 2013-2014 Standard Platform League.
The color of the goal and the support polygons can be modified.

### RobotstadiumGoal Field Summary

- `postRadius`: Defines the radius of the goal posts.

- `frameColor`: Defines the color of the goal frame.

## RobotstadiumSoccerField

%figure "RobotstadiumSoccerField model in Webots."

![RobotstadiumSoccerField](images/objects/robotstadium/RobotstadiumSoccerField/model.png)

%end

```
RobotstadiumSoccerField {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "robotstadium soccer field"
  SFString   contactMaterial "default"                    
  SFColor    frame1Color     1 1 1                        
  SFColor    frame2Color     1 1 1                        
  SFFloat    postRadius      0.05                         
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/robotstadium/protos/RobotstadiumSoccerField.proto"

### RobotstadiumSoccerField Description

Robot soccer field inspired from the RoboCup 2014 Standard Platform League.
The soccer field is built on a total carpet area of length 10.4 m and width 7.4 m.
The field dimensions (within the white lines) are 9 x 6 m.

### RobotstadiumSoccerField Field Summary

- `contactMaterial`: Is equivalent to the `contactMaterial` field of the [Solid](../reference/solid.md) node.

- `frame1Color`: Defines the color of the first goal frame.

- `frame2Color`: Defines the color of the second goal frame.

- `postRadius`: Defines the radius of the goal posts.

