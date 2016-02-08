## TouchSensor

Derived from `Device`.


```
TouchSensor {
  SFString   type          "bumper" 
  MFVec3f    lookupTable   [ 0 0 0, 5000 50000 0 ]
  SFFloat    resolution    -1
}
```

### Description

A `TouchSensor` node is used to model a bumper or a force sensor. The
`TouchSensor` comes in three different types. The "bumper" type simply detects
collisions and returns a boolean status. The "force" type measures the force
exerted on the sensor's body on one axis (*z*-axis). The "force-3d" type
measures the 3d force vector exerted by external object on the sensor's body.

Examples of using the `TouchSensor` are provided by the "hoap2\_sumo.wbt" and
"hoap2\_walk.wbt" worlds (located in the "projects/robots/hoap2/worlds"
directory of Webots) and by the "force\_sensor.wbt" and "bumper.wbt" worlds
(located in the "projects/samples/devices/worlds" directory of Webots).

### Field Summary

- `type`: allows the user to select the type of sensor: "bumper", "force", or "force-3d", described below.
- `lookupTable`: similar to the one used by the `DistanceSensor` node.
- `resolution`: This field allows to define the resolution of the sensor, the resolution is the smallest change that it is able to measure. Setting this field to -1 (default) means that the sensor has an 'infinite' resolution (it can measure any infinitesimal change). This field is used only if the type is "force" or "force-3d" and accepts any value in the interval (0.0, inf).

### Description

#### "bumper" Sensors

A "bumper" `TouchSensor` returns a boolean value that indicates whether or not
there is a collision with another object. More precisely, it returns 1.0 if a
collision is detected and 0.0 otherwise. A collision is detected when the
`boundingObject` of the `TouchSensor` intersects the `boundingObject` of any
other `Solid` object. The `lookupTable` field of a "bumper" sensor is ignored.
The `Physics` node of a "bumper" sensor is not required.

#### "force" Sensors

A "force" `TouchSensor` computes the (scalar) amount of force currently exerted
on the sensor's body along the *z*-axis. The sensor uses this equation:
`r=|f|*cos(alpha)`, where *r* is the return value, `f` is the cumulative force
currently exerted on the sensor's body, and `alpha` is the angle between `f` and
the sensor's *z*-axis. So the "force" sensor returns the projection of the force
on its *z*-axis; a force perpendicular to the *z*-axis yields zero. For this
reason, a "force" sensor must be oriented such that its positive *z*-axis points
outside of the robot, in the direction where the force needs to me measured. For
example if the `TouchSensor` is used as foot sensor then the *z*-axis should be
oriented downwards. The scalar force value must be read using the
`wb_touch_sensor_get_value()` function.

#### "force-3d" Sensors

A "force-3d" `TouchSensor` returns a 3d-vector that represents the cumulative
force currently applied to its body. This 3d-vector is expressed in the
coordinate system of the `TouchSensor`. The length of the vector reflects the
magnitude of the force. The force vector must be read using the
`wb_touch_sensor_get_values()` function.

%figure "TouchSensor types"
| sensor type | "bumper" | "force" | "force-3d" |
| --- | --- | --- | --- |
| boundingObject | required | required | required |
| Physics node | not required | required | required |
| lookupTable | ignored | used | used |
| return value | 0 or 1 | scalar | vector |
| API function | wb\_touch\_sensor\_get\_value() | wb\_touch\_sensor\_get\_value() | wb\_touch\_sensor\_get\_values() |
%%end

#### Lookup Table


A "force" and "force-3d" sensors can optionally specify a `lookupTable` to simulate the possible non-linearity (and saturation) of the real device.
The `lookupTable` allows the user to map the simulated force measured in Newtons (N) to an output value that will be returned by the `wb_touch_sensor_get_value()` function.
The value returned by the force sensor is first computed by the ODE physics engine, then interpolated using
the `lookupTable`, and finally noise is added (if specified in the lookupTable).
Each line of the `lookupTable` contains
three numbers: (1) an input force in Newtons, (2) the corresponding
output value, and (3) a noise level between 0.0 and 1.0 (see `DistanceSensor` for more info).
Note that the default `lookupTable` of the `TouchSensor` node is:

```
[   0     0 0
 5000 50000 0 ]
```
and hence it maps forces between 0 and 5000 Newtons to output values between 0 and 50000, the output unit being 0.1 Newton.
You should empty the `lookupTable` to have Newtons as output units.


#### Collision detection

`TouchSensor`s detect collisions based on the 3D geometry of its
`boundingObject`. So the `boundingObject` must be specified for every type of
`TouchSensor`. Because the actual 3D intersection of the sensors
`boundingObject`s with other `boundingObject`s is used in the calculation, it is
very important that the sensors' `boundingObject`s are correctly positioned;
they should be able to collide with other objects, otherwise they would be
ineffective. For that reason, the `boundingObject`s of `TouchSensor`s should
always extend beyond the other `boundingObject`s of the robot in the area where
the collision is expected.

For example, let's assume that you want to add a `TouchSensor` under the foot of
a humanoid robot. In this case, it is critical that the `boundingObject` of this
sensor (and not any other `boundingObject` of the robot) makes the actual
contact with the floor. Therefore, it is necessary that the sensor's
`boundingObject` extend below any other `boundingObject` of the robot (e.g.,
foot, ankle, etc.).

#### Coordinate System

It is easy to check the orientation of the coordinate system of a `TouchSensor`:
if you select the `TouchSensor` object in the Scene Tree, then only the bounding
object of this `TouchSensor` should be shown in the 3D window. If you zoom in on
this bounding object, you should see the red/green/blue depiction of the
`TouchSensor`'s coordinate system (the color coding is: *x/y/z* =
red/green/blue). For a "force" sensor, the blue (*z*) component should point in
the direction where the collision is expected.

#### Accuracy

The force measured by the ODE physics engine is only a rough approximation of a
real physical force. This approximation usually improves as the `basicTimeStep`
(`WorldInfo` node) decreases.

### TouchSensor Functions

#### Description

`wb_touch_sensor_enable()` allows the user to enable a touch sensor measurement
every `ms` milliseconds.

`wb_touch_sensor_disable()` turns the touch sensor off, saving computation time.

`wb_touch_sensor_get_value()` returns the last value measured by a "bumper" or
"force" `TouchSensor`. This function can be used with a sensor of type "bumper"
or "force". For a "force" sensor, the value may be altered by an optional lookup
table. For a "bumper" sensor, the value can be 0.0 or 1.0.

The `wb_touch_sensor_get_sampling_period()` function returns the period given
into the `wb_touch_sensor_enable()` function, or 0 if the device is disabled.

`wb_touch_sensor_get_values()` returns the last force vector measured by a
"force-3d" `TouchSensor`. This function can be used with a sensor of type
"force-3d" exclusively.

#### Description

This function allows to retrieve the touch sensor type defined by the `type`
field. If the value of the `type` field is "force" then this function returns
WB\_TOUCH\_SENSOR\_FORCE, if it is "force-3d" then it returns
WB\_TOUCH\_SENSOR\_FORCE3D and otherwise it returns WB\_TOUCH\_SENSOR\_BUMPER.

%figure "Return values for the"
| TouchSensor.type | return value |
| --- | --- |
| "bumper" | WB\_TOUCH\_SENSOR\_BUMPER |
| "force" | WB\_TOUCH\_SENSOR\_FORCE |
| "force-3d" | WB\_TOUCH\_SENSOR\_FORCE3D |
%%end

