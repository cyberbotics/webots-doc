# Webots World Files

## Generalities

Webots world files must use the ".wbt" file name extension. The first line of a
".wbt" file uses this header:


```
#VRML_SIM V6.0 utf8
```

where the version *6.0* specifies that the file can be open with *Webots 6* and
*Webots 7*. Although the header specifies *utf8*, at the moment only ascii is
supported.

The comments placed just below the header store the window configuration
associated with this world.

One (and only one) instance of each of the `WorldInfo, ViewPoint` and
`Background` nodes must be present in every ".wbt" file. For example:


```
#VRML_SIM V6.0 utf8

WorldInfo {
  info [
    "Description"
    "Author: first name last name lte-mailgt"
    "Date: DD MMM YYYY"
  ]
}
Viewpoint {
  orientation 1 0 0 -0.8
  position 0.25 0.708035 0.894691
}
Background {
  skyColor [
    0.4 0.7 1
  ]
}
PointLight {
  ambientIntensity 0.54
  intensity 0.5
  location 0 1 0
}
```

## Nodes and Keywords

### VRML97 nodes

Webots implements only a subset of the nodes and fields specified by the VRML97
standard. In the other hand, Webots also adds many nodes, which are not part of
the VRML97 standard, but are specialized to model robotic experiments.

The following VRML97 nodes are supported by Webots:

`Appearance, Background, Box, Color, Cone, Coordinate, Cylinder,
DirectionalLight, ElevationGrid, Fog, Group, ImageTexture, IndexedFaceSet,
IndexedLineSet, Material, PointLight, Shape, Sphere, SpotLight,
TextureCoordinate, TextureTransform, Transform, Viewpoint` and `WorldInfo`.

Please refer to  for a detailed description of Webots nodes and fields. It
specifies which fields are actually used. For a comprehensive description of the
VRML97 nodes, you can also refer to the VRML97 documentation.

The exact features of VRML97 are subject to a standard managed by the
International Standards Organization (ISO/IEC 14772-1:1997). You can find the
complete specification of VRML97 on the `Web3D Web site`.

### Webots specific nodes

In order to describe more precisely robotic simulations, Webots supports
additional nodes that are not specified by the VRML97 standard. These nodes are
principally used to model commonly used robot devices. Here are Webots
additional nodes:

`Accelerometer, BallJoint, BallJointParameters, Camera, CameraZoom, Capsule,
Charger, Compass, Connector, ContactProperties, Damping, DifferentialWheels,
DistanceSensor, Display, Emitter, GPS, Gyro, HingeJoint, HingeJointParameters,
Hinge2Joint, Hinge2JointParameters, InertialUnit, JointParameters, LED,
LightSensor, LinearMotor, Pen, Physics, Plane, PositionSensor, Receiver, Robot,
RotationalMotor, Servo, SliderJoint, Solid, SolidReference, Supervisor` and
`TouchSensor`.

Please refer to  for a detailed description of Webots nodes and fields.

### Reserved keywords

These reserved keywords cannot be used in DEF or PROTO names:

`DEF, USE, PROTO, IS, TRUE, FALSE, NULL, field, vrmlField, SFNode, SFColor,
SFFloat, SFInt32, SFString, SFVec2f, SFVec3f, SFRotation, SFBool, MFNode,
MFColor, MFFloat, MFInt32, MFString, MFVec2f, MFVec3f, MFRotation` and
`MFBool`.

## DEF and USE

A node which is named using the DEF keyword can be referenced later by its name
in the same file with USE statements. The DEF and USE keywords can be used to
reduce redundancy in ".wbt" and ".proto" files. DEF name are limited in scope to
a single ".wbt" or ".proto" file. If multiple nodes are given the same DEF name,
each USE statement refers to the closest node with the given DEF name preceding
it in the ".wbt" or ".proto" file.


```
[DEF defName] nodeName { nodeBody }
```


```
USE defName
```

