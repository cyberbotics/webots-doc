## Chart

The Webots Node Chart outlines all the nodes available to build Webots worlds.

In the chart, an arrow between two nodes represents an inheritance relationship.
The inheritance relationship indicates that a derived node (at the arrow tail) inherits all the fields and API functions of a base node (at the arrow head).
For example, the [Supervisor](supervisor.md) node inherits from the [Robot](robot.md) node, and therefore all the fields and functions available in the [Robot](robot.md) node are also available in the [Supervisor](supervisor.md) node.

Boxes depicted with a dashed line ([Light](light.md), `Device` and `Geometry`) represent *abstract* nodes, that is, nodes that cannot be instantiated (either using the SceneTree or in a ".wbt" file).
Abstract nodes are used to group common fields and functions that are shared by derived nodes.

A box with round corners represents a `Geometry` node; that is, a node that will be graphically depicted when placed in the `geometry` field of a [Shape](shape.md) node.

A box with a gray background indicates a node that can be used directly (or composed using [Group](group.md) and [Transform](transform.md) nodes) to build a *boundingObject* used to detect collisions between [Solid](solid.md) objects.
Note that not all geometry nodes can be used as boundingObjects, and that although [Group](group.md) and [Transform](transform.md) can be used, not every combination of these will work correctly.

%chart
graph LR
  subgraph ""
    AbstractClass(Abstract Class) --- AbstractClassDefinition[cannot be instantiated]
    click AbstractClass "https://www.google.ch" "test tooltip"
    BoundingObject[Bounding Object] --- BoundingObjectDefinition[can be used as BoundingObject<br>in a Solid node]
    VRML[VRML] --- VRMLDefinition[valid VRML node]
  end
  PositionSensor --- Appearance
  AbstractClassDefinition --- JointDevice
  linkStyle 0 stroke-width:0px;
  linkStyle 1 stroke-width:0px;
  linkStyle 2 stroke-width:0px;
  linkStyle 3 stroke-width:0px;
  linkStyle 4 stroke-width:0px;

  Geometry(Geometry) -.-> Box[[Box](box.md)]
  Geometry -.-> Capsule[[Capsule](capsule.md)]
  Geometry -.-> Cone[[Cone](cone.md)]
  Geometry -.-> Cylinder[[Cylinder](cylinder.md)]
  Geometry -.-> EleveationGrid[[EleveationGrid](elevationgrid.md)]
  Geometry -.-> IndexedFaceSet[[IndexedFaceSet](indexedfaceset.md)]
  Geometry -.-> IndexedLineSet[[IndexedLineSet](indexedlineset.md)]
  Geometry -.-> Plane[[Plane](plane.md)]
  Geometry -.-> PointSet[[PointSet](pointset.md)]
  Geometry -.-> Sphere[[Sphere](sphere.md)]

  Device([Device](device.md)) -.-> JointDevice(Joint Device)
  Device -.-> SolidDevice(Solid Device)

  Group[[Group](group.md)] --> Transform[[Transform](transform.md)]
    Transform --> Solid[[Solid](solid.md)]
      Solid --> SolidDevice
        SolidDevice --> Accelerometer[[Accelerometer](accelerometer.md)]
        SolidDevice --> Camera[[Camera](camera.md)]
        SolidDevice --> Compass[[Compass](compass.md)]
        SolidDevice --> Connector[[Connector](connector.md)]
        SolidDevice --> Display[[Display](display.md)]
        SolidDevice --> DistanceSensor[[DistanceSensor](distancesensor.md)]
        SolidDevice --> Emitter[[Emitter](emitter.md)]
        SolidDevice --> GPS[[GPS](gps.md)]
        SolidDevice --> Gyro[[Gyro](gyro.md)]
        SolidDevice --> InertialUnit[[InertialUnit](inertialunit.md)]
        SolidDevice --> LED[[LED](led.md)]
        SolidDevice --> Lidar[[Lidar](lidar.md)]
        SolidDevice --> Pen[[Pen](pen.md)]
        SolidDevice --> Propeller[[Propeller](propeller.md)]
        SolidDevice --> Radar[[Radar](radar.md)]
        SolidDevice --> RangeFinder[[RangeFinder](rangefinder.md)]
        SolidDevice --> Receiver[[Receiver](receiver.md)]
        SolidDevice --> Speaker[[Speaker](speaker.md)]
        SolidDevice --> TouchSensor[[TouchSensor](touchsensor.md)]
        SolidDevice --> Track[[Track](track.md)]
      Solid --> Charger[[Charger](charger.md)]
      Solid --> Robot[[Robot](robot.md)]
        Robot --> Supervisor[[Supervisor](supervisor.md)]
    Transform --> Fluid[[Fluid](fluid.md)]
  Group --> TrackWheel[[TrackWheel](trackwheel.md)]

  JointDevice -.-> Motor([Motor](motor.md))
    Motor -.-> LinearMotor[[LinearMotor](linearmotor.md)]
    Motor -.-> RotationalMotor[[RotationalMotor](rotationalmotor.md)]
  JointDevice -.-> Brake[[Brake](brake.md)]
  JointDevice -.-> PositionSensor[[PositionSensor](positionsensor.md)]

  Light([Light](light.md)) -.-> DirectionalLight[[DirectionalLight](directionallight.md)]
  Light -.-> PointLight[[PointLight](pointlight.md)]
  Light -.-> SpotLight[[SpotLight](spotlight.md)]

  Joint([Joint](joint.md)) -.-> BallJoint[[BallJoint](balljoint.md)]
  Joint -.-> HingeJoint[[HingeJoint](hingejoint.md)]
    HingeJoint --> Hinge2Joint([Hinge2Joint](hinge2joint.md))
  Joint -.-> SliderJoint[[SliderJoint](sliderjoint.md)]

  BallJointParameters[[BallJointParameters](balljointparameters.md)]
  JointParameters[[JointParameters](jointparameters.md)] --> HingeJointParameters[[HingeJointParameters](hingejointparameters.md)]

  subgraph other Nodes
    Appearance[[Appearance](appearance.md)]
    BackGround[[Background](background.md)]
    Color[[Color](color.md)]
    ContactProperties[[ContactProperties](contactProperties.md)]
    Coordinate[[Coordinate](coordinate.md)]
    Damping[[Damping](damping.md)]
    Focus[[Focus](focus.md)]
    Fog[[Fog](fog.md)]
    ImageTexture[[ImageTexture](imagetexture.md)]
    ImmersionProperties[[ImmersionProperties](immersionproperties.md)]
    Lens[[Lens](lens.md)]
    LensFlare[[LensFlare](lensflare.md)]
    Material[[Material](material.md)]
    Muscle[[Muscle](muscle.md)]
    Physics[[Physics](physics.md)]
    Recognition[[Recognition](recognition.md)]
    Shape[[Shape](shape.md)]
    Slot[[Slot](slot.md)]
    SolidReference[[SolidReference](solidreference.md)]
    TextureCoordinate[[TextureCoordinate](texturecoordinate.md)]
    TextureTransform[[TextureTransform](texturetransform.md)]
    Viewpoint[[Viewpoint](viewpoint.md)]
    WorldInfo[[WorldInfo](worldinfo.md)]
    Zoom[[Zoom](zoom.md)]
  end

  classDef AbstractClassStyle stroke-width:3px,stroke-dasharray:5,5;
  classDef BoundingObjectStyle fill:#d3ffc9;
  classDef VRMLBoundingObjectStyle fill:#d3ffc9,stroke:#444444,stroke-width:3px;
  classDef VRMLNodeStyle stroke:#444444,stroke-width:3px;
  classDef DefinitionStyle fill:#f1f1f1,stroke-width:0px;
  style VRML fill:#f1f1f1,stroke:#444444,stroke-width:3px;

  class AbstractClass,Device,Geometry,Joint,JointDevice,Light,Motor,SolidDevice AbstractClassStyle;
  class BoundingObject,Capsule,Plane BoundingObjectStyle;
  class Box,Cylinder,EleveationGrid,IndexedFaceSet,Sphere VRMLBoundingObjectStyle;
  class Appearance,BackGround,Color,Cone,DirectionalLight,Fog,Group,ImageTexture,IndexedLineSet,Material,PointLight,PointSet,SpotLight,TextureCoordinate,TextureTransform,Transform,WorldInfo VRMLNodeStyle;
  class AbstractClassDefinition,BoundingObjectDefinition,VRMLDefinition DefinitionStyle;
%end
