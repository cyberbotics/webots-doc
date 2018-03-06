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
    BoundingObject[Bounding Object] --- BoundingObjectDefinition[can be used as BoundingObject<br>in a Solid node]
    VRML[VRML] --- VRMLDefinition[valid VRML node]
    style AbstractClass fill:#f9f
    style AbstractClassDefinition fill:#ffffde,stroke-width:0px
    style BoundingObject fill:#63639c
    style BoundingObjectDefinition fill:#ffffde,stroke-width:0px
    style VRML fill:#ffffcc,stroke:#f66,stroke-width:5px,align:right
    style VRMLDefinition fill:#ffffde,stroke-width:0px
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
  style Geometry fill:#f9f
  style Box fill:#63639c,stroke:#f66,stroke-width:5px
  style Capsule fill:#63639c
  style Cone stroke:#f66,stroke-width:5px
  style Cylinder fill:#63639c,stroke:#f66,stroke-width:5px
  style EleveationGrid fill:#63639c,stroke:#f66,stroke-width:5px
  style IndexedFaceSet fill:#63639c,stroke:#f66,stroke-width:5px
  style IndexedLineSet stroke:#f66,stroke-width:5px
  style Plane fill:#63639c
  style PointSet stroke:#f66,stroke-width:5px
  style Sphere fill:#63639c,stroke:#f66,stroke-width:5px

  Device(Device) -.-> JointDevice(Joint Device)
  Device -.-> SolidDevice(Solid Device)
  style Device fill:#f9f

  Group[Group] --> Transform[Transform]
    Transform --> Solid[Solid]
      Solid --> SolidDevice
      style SolidDevice fill:#f9f
        SolidDevice --> Accelerometer[Acclerometer]
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
  style Group stroke:#f66,stroke-width:5px
  style Transform stroke:#f66,stroke-width:5px

  JointDevice -.-> Motor(Motor)
    Motor -.-> LinearMotor[LinearMotor]
    Motor -.-> RotationalMotor[RotationalMotor]
  JointDevice -.-> brake[Brake]
  JointDevice -.-> PositionSensor[PositionSensor]
  style JointDevice fill:#f9f
  style Motor fill:#f9f

  Light(Light) -.-> DirectionalLight[DirectionalLight]
  Light -.-> PointLight[PointLight]
  Light -.-> SpotLight[SpotLight]
  style Light fill:#f9f
  style DirectionalLight stroke:#f66,stroke-width:5px
  style PointLight stroke:#f66,stroke-width:5px
  style SpotLight stroke:#f66,stroke-width:5px
  click Light "#light.md" "Got to Light node description"
  click directionalLight "#directionallight.md" "Got to DirectionalLight node description"
  click pointLight "#pointlight.md" "Got to PointLight node description"
  click spotLight "#spotlight.md" "Got to SpotLight node description"

  Joint(Joint) -.-> BallJoint[BallJoint]
  Joint -.-> HingeJoint[HingeJoint]
    HingeJoint(HingeJoint) --> Hinge2Joint(Hinge2Joint)
  Joint -.-> sliderJoint[SliderJoint]
  style Joint fill:#f9f

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
    style Appearance stroke:#f66,stroke-width:5px
    style BackGround stroke:#f66,stroke-width:5px
    style Color stroke:#f66,stroke-width:5px
    style BackGround stroke:#f66,stroke-width:5px
    style Fog stroke:#f66,stroke-width:5px
    style Material stroke:#f66,stroke-width:5px
    style ImageTexture stroke:#f66,stroke-width:5px
    style TextureCoordinate stroke:#f66,stroke-width:5px
    style TextureTransform stroke:#f66,stroke-width:5px
    style WorldInfo stroke:#f66,stroke-width:5px
  end
%end
