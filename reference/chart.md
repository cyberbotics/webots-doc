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

  Geometry(Geometry) -.-> Box[Box]
  Geometry -.-> Capsule[Capsule]
  Geometry -.-> Cone[Cone]
  Geometry -.-> Cylinder[Cylinder]
  Geometry -.-> EleveationGrid[EleveationGrid]
  Geometry -.-> IndexedFaceSet[IndexedFaceSet]
  Geometry -.-> IndexedLineSet[IndexedLineSet]
  Geometry -.-> Plane[Plane]
  Geometry -.-> PointSet[PointSet]
  Geometry -.-> Sphere[Sphere]

  Device(Device) -.-> JointDevice(Joint Device)
  Device -.-> SolidDevice(Solid Device)

  Group[Group] --> Transform[Transform]
    Transform --> Solid[Solid]
      Solid --> SolidDevice
        SolidDevice --> Accelerometer[Accelerometer]
        SolidDevice --> Camera[Camera]
        SolidDevice --> Compass[Compass]
        SolidDevice --> Connector[Connector]
        SolidDevice --> Display[Display]
        SolidDevice --> DistanceSensor[DistanceSensor]
        SolidDevice --> Emitter[Emitter]
        SolidDevice --> GPS[GPS]
        SolidDevice --> Gyro[Gyro]
        SolidDevice --> InertialUnit[InertialUnit]
        SolidDevice --> LED[LED]
        SolidDevice --> Lidar[Lidar]
        SolidDevice --> Pen[Pen]
        SolidDevice --> Propeller[Propeller]
        SolidDevice --> Radar[Radar]
        SolidDevice --> RangeFinder[RangeFinder]
        SolidDevice --> Receiver[Receiver]
        SolidDevice --> Speaker[Speaker]
        SolidDevice --> TouchSensor[TouchSensor]
        SolidDevice --> Track[Track]
      Solid --> Charger[Charger]
      Solid --> Robot[Robot]
        Robot --> Supervisor[Supervisor]
    Transform --> Fluid[Fluid]
  Group --> TrackWheel[TrackWheel]

  JointDevice -.-> Motor(Motor)
    Motor -.-> LinearMotor[LinearMotor]
    Motor -.-> RotationalMotor[RotationalMotor]
  JointDevice -.-> Brake[Brake]
  JointDevice -.-> PositionSensor[PositionSensor]

  Light(Light) -.-> DirectionalLight[DirectionalLight]
  Light -.-> PointLight[PointLight]
  Light -.-> SpotLight[SpotLight]
  click Light "#light.md" "Got to Light node description"
  click directionalLight "#directionallight.md" "Got to DirectionalLight node description"
  click pointLight "#pointlight.md" "Got to PointLight node description"
  click spotLight "#spotlight.md" "Got to SpotLight node description"

  Joint(Joint) -.-> BallJoint[BallJoint]
  Joint -.-> HingeJoint[HingeJoint]
    HingeJoint(HingeJoint) --> Hinge2Joint(Hinge2Joint)
  Joint -.-> SliderJoint[SliderJoint]

  BallJointParameters[BallJointParameters]
  JointParameters[JointParameters] --> HingeJointParameters[HingeJointParameters]

  subgraph other Nodes
    Appearance[Appearance]
    BackGround[BackGround]
    Color[Color]
    ContactProperties[ContactProperties]
    Coordinate[Coordinate]
    Damping[Damping]
    Focus[Focus]
    Fog[Fog]
    ImageTexture[ImageTexture]
    ImmersionProperties[ImmersionProperties]
    Lens[Lens]
    LensFlare[LensFlare]
    Material[Material]
    Muscle[Muscle]
    Physics[Physics]
    Recognition[Recognition]
    Shape[Shape]
    Slot[Slot]
    SolidReference[SolidReference]
    TextureCoordinate[TextureCoordinate]
    TextureTransform[TextureTransform]
    Viewpoint[Viewpoint]
    WorldInfo[WorldInfo]
    Zoom[Zoom]
  end

  classDef AbstractClassStyle fill:#f9f;
  classDef BoundingObjectStyle fill:#63639c
  classDef VRMLBoundingObjectStyle fill:#63639c,stroke:#f66,stroke-width:5px
  classDef VRMLNodeStyle fill:#70a6ff,stroke:#f66,stroke-width:5px
  classDef NodeStyle fill:#70a6ff
  classDef DefinitionStyle fill:#ffffde,stroke-width:0px
  style VRML fill:#ffffcc,stroke:#f66,stroke-width:5px,align:right

  class AbstractClass,Geometry,Device,SolidDevice,JointDevice,Motor,Light,Joint AbstractClassStyle;
  class BoundingObject,Capsule,Plane BoundingObjectStyle;
  class Box,Cylinder,EleveationGrid,IndexedFaceSet,Sphere VRMLBoundingObjectStyle;
  class Cone,IndexedLineSet,PointSet,DirectionalLight,PointLight,SpotLight,Group,Transform,Appearance,BackGround,Color,Fog,ImageTexture,Material,TextureCoordinate,TextureTransform,WorldInfo VRMLNodeStyle;
  class BallJoint,HingeJoint,Hinge2Joint,SliderJoint,BallJointParameters,JointParameters,HingeJointParameters,TrackWheel,Fluid,Solid,Charger,Robot,Supervisor,Brake,LinearMotor,RotationalMotor,PositionSensor,Accelerometer,Camera,Compass,Connector,Display,DistanceSensor,Emitter,GPS,Gyro,InertialUnit,LED,Lidar,Pen,Propeller,Radar,RangeFinder,Receiver,Speaker,TouchSensor,Track,ContactProperties,Coordinate,Damping,Focus,ImmersionProperties,Lens,LensFlare,Muscle,Physics,Recognition,Shape,Slot,SolidReference,Viewpoint,Zoom NodeStyle;
  class AbstractClassDefinition,BoundingObjectDefinition,VRMLDefinition DefinitionStyle;
%end
