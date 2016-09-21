## Tutorial 6: 4-Wheels Robot

The aim of this tutorial is to create your first robot from scratch. This robot
will be made of a body, four wheels, and two distance sensors. The result is
depicted on [this
figure](#3d-view-of-the-4-wheels-robot-note-that-the-coordinate-system-representations-of-the-robot-body-and-of-its-wheels-are-oriented-the-same-way-their-px-vector-in-red-defines-the-left-of-the-robot-their-py-vector-in-green-defines-the-top-of-the-robot-and-their-pz-vector-in-blue-defines-the-front-of-the-robot-the-distance-sensors-are-oriented-in-a-different-way-their-px-vector-indicates-the-direction-of-the-sensor).
The
[next figure](#top-view-of-the-4-wheels-robot-the-grid-behind-the-robot-has-a-dimension-of-0-2-x-0-3-meters-the-text-labels-correspond-to-the-name-of-the-devices)
shows the robot from a top view.

%figure "3D view of the 4 wheels robot. Note that the coordinate system representations of the robot body and of its wheels are oriented the same way. Their +x-vector (in red) defines the left of the robot, their +y-vector (in green) defines the top of the robot, and their +z-vector (in blue) defines the front of the robot. The distance sensors are oriented in a different way, their +x-vector indicates the direction of the sensor."

![tutorial_4_wheels_robot.png](images/tutorial_4_wheels_robot.png)

%end

%figure "Top view of the 4 wheels robot. The grid behind the robot has a dimension of 0.2 x 0.3 meters. The text labels correspond to the name of the devices."

![tutorial_4_wheels_top_schema.png](images/tutorial_4_wheels_top_schema.png)

%end

### New simulation

> **Hands on**:
Save the world of the previous tutorial as "4\_wheels\_robot.wbt".

<!-- -->

> **Hands on**:
Remove the nodes defining the e-puck, the ball, the dumbbell and the contact
properties. The ground, the walls and the lighting are kept.

### Separating the Robot in Solid Nodes

Some definitions are required before giving rules to create a robot model.

The set containing the Solid node and all its derived nodes is called the *solid
nodes*. A similar definition is applied for the Device, Robot, Joint and Motor
nodes. You can get more information about the node hierarchy in the `Reference
Manual`. Note that the solid nodes and device nodes are close but don't match
perfectly.

> **Theory**:
The main structure of a robot model is a tree of solid nodes linked together.
The root node of this tree should be a robot node. The solids are linked together
by joint nodes. A device node should be the direct child of either a robot node,
 a solid node or a joint node.

<!-- -->

> **Theory**:
A joint node is used to add one (or two) degree(s) of freedom (DOF), between its
parent and its child. The direct parent and child of a joint node are both solid
nodes.

> The nodes derived from Joint allow to create different kinds of constraints
between the linked solid nodes. The most used one in robotics, is the HingeJoint
allowing to model amongst others rotational motors including wheels.

> A joint node can be monitored or actuated by adding respectively a
PositionSensor node, or a motor node to its *device* field.

Having these rules in mind, we can start to design the node hierarchy used to
model the robot. The first step is to determine which part of the robot should
be modeled as a solid node.

In our example, this operation is quite obvious. The robot has 4 DOF
corresponding to the wheel motors. It can be divided in five solid nodes: the
body and the four wheels.

Depending on the expected application of the robot model, reducing the number of
DOF when modeling could be important to get an efficient simulation. For
example, when modeling a caster wheel, a realistic approach implies to model 2
DOF. But if this degree of precision is useless for the simulation, a more
efficient approach can be found. For example, to model the caster wheel as a
Sphere having a null friction coefficient with the ground.

The second step is to determine which solid node is the robot node (the root
node). This choice is arbitrary, but a solution is often much easier to
implement. For example, in the case of an humanoid robot, the robot node would
be typically the robot chest, because the robot symmetry facilitates the
computation of the joint parameters.

In our case, the body box is obviously the better choice. The
[figure](#high-level-representation-of-the-4-wheels-robot) depicts the solid
nodes hierarchy of the robot.

> **Hands on**:
At the end of the scene tree, add a Robot node having four HingeJoints having a
Solid child. Please refer to [this
figure](#high-level-representation-of-the-4-wheels-robot).

<!-- -->

> **Hands on**:
Add a Shape node containing a Box geometry to the Robot node. Set the color of
the Shape to red. Use the Shape to define also the `boundingObject` field of the
Robot node. The dimension of the box is *(0.1, 0.05, 0.2)*. Add a Physics node
to the Robot. The [figure](#low-level-representation-of-the-4-wheels-robot)
represents all the nodes defining the robot. So far only the direct children
nodes of the root Robot node are implemented.

%figure "High level representation of the 4 wheels robot"

![tutorial_4_wheels_highlevel.png](images/tutorial_4_wheels_highlevel.png)

%end

%figure "Low level representation of the 4 wheels robot"

![tutorial_4_wheels_lowlevel.png](images/tutorial_4_wheels_lowlevel.png)

%end

### HingeJoints

The initial position of the Wheel is defined by the translation and the rotation
fields of the Solid node. While the rotation origin (anchor) and the rotation
axis (axis) are defined by the optional HingeJointParameters child of the
HingeJoint node.

%figure "Representation of a hinge joint"

![hinge_joint.png](images/hinge_joint.png)

%end

For the first wheel, the Solid translation should be defined to *(0.06, 0,
0.05)* in order to define the relative gap between the body and the wheel. The
HingeJointParameters anchor should also be defined to *(0.06, 0, 0.05)* to
define the rotation origin (relatively to the body). Finally the
HingeJointParameters axis should define the rotation axis. In our case it's
along the x-axis (so *(1, 0, 0)*).

> **Hands on**:
Add a HingeJointParameters node, and enter the field values as described above.
Some signs obviously have to be updated for other wheels.

We want now to implement the cylinder shape of the wheels. As the Cylinder node
is defined along the *y*-axis, a Transform node should encapsulate the Shape to
rotate the Cylinder along the along the *x*-axis.

> **Hands on**:
Complete the missing nodes to get the same structure as the one depicted in
[this figure](#low-level-representation-of-the-4-wheels-robot). Don't forget the
Physics nodes. Rotate the Transform node by an Euler axis and angle of *(0, 0,
1, Pi/2)* in order to inverse the *x*-axis and the *y*-axis. The Cylinder should
have a `radius` of *0.04* and a `height` of *0.02*. Set the color of the wheels
to green.

<!-- -->

> **Hands on**:
In order to be able to actuate the wheels, add a RotationalMotor to each
HingeJoint, and set their `name` fields from *"wheel1"* to *"wheel4"*. These
labels will be used to reference the wheels from the controller.

### Sensors

The last part of the robot modeling is to add the two distance sensors to the
robot. This can be done by adding two DistanceSensor nodes as direct children of
the Robot node. Note that the distance sensor acquires its data along the
+*x*-axis. So rotating the distance sensors in order to point their *x*-axis
outside the robot is necessary (see the
[figure](#top-view-of-the-4-wheels-robot-the-grid-behind-the-robot-has-a-dimension-of-0-2-x-0-3-meters-the-text-labels-correspond-to-the-name-of-the-devices)).

> **Hands on**:
Add the two distance sensors as explained above. The distance sensors are at an
angle to 0.3 [rad] with the robot front vector. Set their `type` field to
"sonar". Set their graphical and physical shape to a cube (not transformed)
having a edge of *0.01* [m]. Set their color to blue. Set their `name` field
according to the labels of [this
figure](#top-view-of-the-4-wheels-robot-the-grid-behind-the-robot-has-a-dimension-of-0-2-x-0-3-meters-the-text-labels-correspond-to-the-name-of-the-devices).

### Controller

In the previous tutorials, you have learnt how to setup a feedback loop and how to
read the distance sensor values. However, actuating the RotationalMotor nodes is
new. The following note explain how to proceed.

> **Note**:
To program the rotational motors, the first step is to include the API module
corresponding to the RotationalMotor node:

> ```c
>  #include <webots/motor.h>
> ```

> Then to get the references of the RotationalMotor nodes:

> ```c
>  // initialize motors
>  WbDeviceTag wheels[4];
>  char wheels_names[4][8] = {
>    "wheel1", "wheel2", "wheel3", "wheel4"
>  };
>  for (i=0; i<4 ; i++)
>    wheels[i] = wb_robot_get_device(wheels_names[i]);
> ```

> A motor can be actuated by setting its position, its velocity, its acceleration
or its force (cf. `Reference Manual`). Here we are interested in setting its
velocity. This can be achieved by setting its position at infinity, and by
bounding its velocity:

> ```c
>  double speed = -1.5; // [rad/s]
>  wb_motor_set_position(wheels[0], INFINITY);
>  wb_motor_set_velocity(wheels[0], speed);
> ```

<!-- -->

> **Hands on**:
Implement a controller called "4\_wheels\_collision\_avoidance" moving the robot
and avoiding obstacles by detecting them by the distance sensors.

> Note that the `lookupTable` field of the DistanceSensor nodes indicates which
values are returned by the sensor (cf. `Reference Manual`).

> Don't forget to set the `controller` field of the Robot node to indicate your
new controller.

> As usual a possible solution of this exercise is located in the tutorials
directory.

### Conclusion

You are now able to design simple robot models, to implement them and to create
their controllers.

More specifically, you learnt the different kinds of nodes involved in the
building of the robot models, the way to translate and rotate a solid relative
to another and the way that a rotational motor is actuated by the controller.
