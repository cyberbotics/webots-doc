## DistanceSensor

Derived from `Device`.


```
DistanceSensor {
  MFVec3f    lookupTable     [ 0 0 0, 0.1 1000 0 ]
  SFString   type            "generic"
  SFInt32    numberOfRays    1        # [1,inf)
  SFFloat    aperture        1.5708   # [0,2pi]
  SFFloat    gaussianWidth   1
  SFFloat    resolution     -1
}
```

### Description

The `DistanceSensor` node can be used to model a generic sensor, an infra-red
sensor, a sonar sensor, or a laser range-finder. This device simulation is
performed by detecting the collisions between one or several sensor rays and
objects in the environment. In case of generic, sonar and laser type the
collision occurs with the bounding objects of `Solid` nodes, whereas infra-red
rays collision detection uses the `Solid` nodes themselves.

The rays of the `DistanceSensor` nodes can be displayed by checking the menu
`View > Optional Rendering > Show Distance Sensor Rays`. The red/green
transition on the rays indicates the points of intersection with the bounding
objects.

### Field Summary

### DistanceSensor types

This table summarizes the difference between the three types of DistanceSensor.

Two different methods are used for calculating the distance from an object.
*Average* method computes the average of the distances measured by all the rays,
whereas *Nearest* method uses the shortest distance measured by any of the rays.

type (field) | "generic" | "infra-red" | "sonar" | "laser"
--- | --- | --- | --- | ---
numberOfRays (field) | gt 0 | gt 0 | gt 0 | 1
Distance calculation | Average | Average | Nearest | Nearest
gaussianWidth (field) | Used | Used | Ignored | Ignored
Sensitive to red objects | No | Yes | No | No
Draws a red spot | No | No | No | Yes

### Infra-Red Sensors

In the case of an "infra-red" sensor, the value returned by the lookup table is
modified by a reflection factor depending on the color properties of the object
hit by the sensor ray. The reflection factor is computed as follows: *f = 0.2 +
0.8 * red_level* where *red_level* is the level of red color of the object hit
by the sensor ray. This level is evaluated combining the `diffuseColor` and
`transparency` values of the object, the pixel value of the image texture and
the paint color applied on the object with the `Pen` device. Then, the distance
value computed by the simulator is divided by the reflection factor before the
lookup table is used to compute the output value.

### Sonar Sensors

In the case of a "sonar" sensor, the return value will be the last value entered
in the lookup table, i.e. the value corresponding to sonar sensor's range, if
the angle of incidence is greater than 22.5 degrees (pi/8 radians). In other
words, sonar rays which lie outside the reflexion cone of aperture 45 degrees
never return and thus are lost for distance computation (see ).

![Sonar sensor](pdf/sonar_reflection.pdf)

**Sonar sensor**

### Line Following Behavior

Some support for `DistanceSensor` nodes used for reading the red color level of
a textured floor is implemented. This is useful to simulate line following
behaviors. This feature is demonstrated in the "rover.wbt" example (see in the
"projects/robots/mindstorms/worlds" directory of Webots). The ground texture
must be placed in a `Plane`.

### DistanceSensor Functions

