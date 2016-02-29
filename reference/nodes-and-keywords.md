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

Please refer to [this chapter](#nodes-and-api-functions) for a detailed
description of Webots nodes and fields. It specifies which fields are actually
used. For a comprehensive description of the VRML97 nodes, you can also refer to
the VRML97 documentation.

The exact features of VRML97 are subject to a standard managed by the
International Standards Organization (ISO/IEC 14772-1:1997). You can find the
complete specification of VRML97 on the [Web3D Web site](http://www.web3d.org).

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

Please refer to [this chapter](#nodes-and-api-functions) for a detailed
description of Webots nodes and fields.

### Reserved keywords

These reserved keywords cannot be used in DEF or PROTO names:

`DEF, USE, PROTO, IS, TRUE, FALSE, NULL, field, vrmlField, SFNode, SFColor,
SFFloat, SFInt32, SFString, SFVec2f, SFVec3f, SFRotation, SFBool, MFNode,
MFColor, MFFloat, MFInt32, MFString, MFVec2f, MFVec3f, MFRotation` and
`MFBool`.

