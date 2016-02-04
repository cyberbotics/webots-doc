## Structure of ODE objects

This table shows how common ".wbt" constructs are mapped to ODE objects. This
information shall be useful for implementing physics plugins.

%figure "Mapping between common Webots constructs and ODE objects."
| Webots construct | ODE construct |
| --- | --- |
| Solid { physics Physics {...} } | dBodyID |
| Solid { boundingObject ... } | dGeomID |
| Solid { boundingObject Box {...} } | dGeomID (dBoxClass) |
| Solid { boundingObject Sphere {...} } | dGeomID (dSphereClass) |
| Solid { boundingObject Capsule {...} } | dGeomID (dGeomTransformClass + dCapsuleClass) |
| Solid { boundingObject Cylinder {...} } | dGeomID (dGeomTransformClass + dCylinderClass) |
| Solid { boundingObject Plane {...} } | dGeomID (dPlaneClass) |
| Solid { boundingObject IndexedFaceSet {...} } | dGeomID (dTriMeshClass) |
| Solid { boundingObject ElevationGrid {...} } | dGeomID (dHeightfieldClass) |
| Solid { boundingObject Transform {...} } | dGeomID (dGeomTransformClass) |
| Solid { boundingObject Group {...} } | dSpaceID (dSimpleSpaceClass) |
| BallJoint { } | dJointID (dJointTypeBall) |
| HingeJoint { } | dJointID (dJointTypeHinge) |
| Hinge2Joint { } | dJointID (dJointTypeHinge2) |
| SliderJoint { } | dJointID (dJointTypeSlider) |
%%end

