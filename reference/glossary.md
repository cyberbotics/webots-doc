# Glossary

This glossary defines the terminology used to describe the various concepts related to a Webots simulation.

**Actuator**: An *actuator* is a *node* representing a real robotics actuator such as a motor, a LED, a radio emitter, etc. *Actuators* may receive commands from a *controller*. Their behavior will affect the outcome of a simulation. Some *actuators* are also *sensors* if they make sensory measurement, such as a motor than can provide position or force feedback.

**Basic Time Step**: The *basic time step* is the time step increment used by Webots to advance the *virtual time* and perform physics simulation. It is specified as a field of the [WorldInfo](#worldinfo) *node* and is expressed in milliseconds.

**Controller**: A *controller* is a program controlling the behavior of a *robot* and running on its own process. It can be written in different languages, including C, C++, Python, Java or MATLAB. It communicates with Webots through a local pipe to read the data measured by the *sensors* of a *robot* and send commands to the *actuators* of the *robot*.

**Controller Time Step**: The *controller time step* is the time increment executed at each iteration of the control loop of a *controller*. It is usually passed directly as an argument of the [wb_robot_step](robot.md#wb_robot_step)() function. It should be an exact multiple of the *basic time step* for an optimal simulation performance.

**Descendant**: A *descendant* is a *node* which is hierarchically included inside another *node* in the *scene tree*.

**Device**: A *device* is either an *actuator* or a *sensor*.

**Dynamic Solid**: A *dynamic solid* is a *solid* which has a [Physics](#physics) *node* defined and can move according to the Webots dynamic physics engine (ODE).

**Kinematic Solid**: A *kinematic solid* is a *solid* which has no [Physics](#physics) *node* defined, but which can move using the Webots kinematic physics engine.

**Node**: A *node* is an object used to define a simulation *world*. All the Webots *nodes* are depicted in the [Node Chart](#node-chart) and described in details in the [Nodes and API functions](#nodes-and-api-functions.md) section of this manual.

**Passive Solid**: A *passive solid* is a *solid* which is not a *robot*, neither a *sensor* or an *actuator*. It may be either a *kinematic* or a *dynamic solid*.

**Robot**: A *robot* is a [Robot](#robot) *node* defining a robotic system. It usually includes *sensors* and *actuators* in its *descendants*.

**Scene Tree**: The *scene tree* is the hierarchical tree structure containing all the *nodes* included in a *world*.

**Sensor**: A *sensor* is a *node* representing a real robotics sensor such as a camera, a sonar or a gyroscope. *Sensors* can send measurement data, such as a camera image or a distance measurement to a *controller*.

**Solid**: A *solid* is a [Solid](#Solid) node defining a physical object, including *robots*, *sensors*, *actuators* and *passive solids*.

**Static Environment**: The *static environment* is a made up of all the *solids* of a *world* that have no [Physics](#physics) *node* and cannot move, but have a bounding object defined. It is used to detect collisions with the *dynamic* and *kinematic solids* in order to prevent them from penetrating it.

**Supervisor**: A *supervisor* is a special *robot* defined by a [Supervisor](#supervisor) *node* that has some extra capabilities not available in real robots. It is therefore not realistic to model a real robot with a *supervisor*. *Supervisors* are nevertheless very useful to script a simulation and perform various operations that a normal user could do manually from the Webots graphical user interface (like moving objects, recording trajectories, making a movie, etc.).

**Virtual Time**: The *virtual time* is the simulated time of a running simulation. It may run faster or slower than the real time, depending on the complexity of the simulation. The "run real time" feature of Webots allows the user to synchronize the *virtual time* with the real time to ensure a simulation is running no faster than real time.

**World**: A *world* is a file defining a simulation. It includes *nodes* organized hierarchically in a *scene tree*.
