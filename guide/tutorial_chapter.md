# Tutorials

The aim of this chapter is to explain the fundamental concepts of Webots
required to create your own simulations. Learning is focused on the modeling of
robots and of their environment, as well as on the programming of robot
controllers. You will also learn where to find the documentation to go further.

This chapter is suitable for absolute beginners in Webots. A background in
programming is nevertheless required. The examples are written in C language. If
you are not familiar with the C language, you should be able to understand this
chapter anyway, because the C programs below are very simple. Except for
programming, you don't need any particular knowledge to go through the tutorials
included in this chapter. However a basic background knowledge in robotics,
mathematics, modeling and tree representation might turn out to be helpful.
Experienced Webots users may skip the first tutorials. However, we would
recommend them to read at least the introduction and conclusion of these
tutorials.

Each section of this chapter (except the first one and the last one) is a
tutorial. Each tutorial has a precise educational objective explained in the
first paragraph. The acquired  concepts are then summarized in the conclusion
subsection. A tutorial is designed as a sequence of interactive steps. The
knowledge acquired in a tutorial is often required to continue with the next
tutorial. Therefore we strongly recommend you to respect their natural order.
Moreover we recommend you to ensure you understood all the concepts of a
tutorial before proceeding further.

A Webots PRO license or a 30-days trial license is required to follow all the
tutorials. However, an EDU license is sufficient to follow about 95% of this
chapter, as it won't allow you to program supervisor processes and physics
plugins.

The last section will provide you with some hints to address problems that are
not covered in this chapter.

The solutions of the tutorials are located into the
"WEBOTS_MODULES_PATH/projects/samples/tutorials" subdirectory of the Webots
installation directory.

We hope you will enjoy your first steps with Webots. Meanwhile, we would really
appreciate to receive your feedback regarding this chapter.

## Prerequisites

In this section, you will learn how to setup your Webots environment. It is
obviously a necessary step to get started with the tutorials.

### Install Webots

Webots has to be installed on your computer.

### Create a directory for all your Webots files

The first step is to create a directory which will contain all your files
related to Webots.

### Start Webots

You need to learn how to launch Webots.

Now a simulation is running.

### Create a new Project

The freshly created "my_webots_projects" directory will contain all your Webots
projects. Your first Webots project will be the tutorials of this chapter. So
let's create now a project named "tutorials" which will contain all the
simulations of this chapter.

### The Webots Graphical User Interface (GUI)

The Webots main window is shown in . Make sure you understand well how the
Webots main window is divided into subwindows before continuing. A more detailed
description of the Webots GUI is provided in .

![
    The Webots main window splits into four dockable subwindows:
    the scene tree view on the left hand side (including a panel at the bottom for editing fields values),
    the 3D view in the center,
    the text editor on the right hand side,
    and the console at bottom of the window.
    Note that some of these subwindows have a toolbar with buttons.
    The main menus appear on the top of the main window.
    The virtual time counter and the speedometer are displayed in the right part of the 3D view toolbar.
    The status text is displayed in the bottom left of the main window.
   ](png/tutorial_gui.png)
**
    The Webots main window splits into four dockable subwindows:
    the scene tree view on the left hand side (including a panel at the bottom for editing fields values),
    the 3D view in the center,
    the text editor on the right hand side,
    and the console at bottom of the window.
    Note that some of these subwindows have a toolbar with buttons.
    The main menus appear on the top of the main window.
    The virtual time counter and the speedometer are displayed in the right part of the 3D view toolbar.
    The status text is displayed in the bottom left of the main window.
   **

## Tutorial 1: Your first Simulation in Webots (20 minutes)

In this first tutorial, you will create your first simulation. This simulation
will contain a simple environment (a light and an arena with floor and walls), a
predefined robot (e-puck) and a controller program that will make the robot move
(see ). The objective of this tutorial is to familiarize yourself with the user
interface and with the basic concepts of Webots.

![
    What you should see at the end of the tutorial.
   ](png/tutorial_e-puck.png)
**
    What you should see at the end of the tutorial.
   **

### Create a new World

In this subsection, we will create a new simulation. The content of a simulation
is stored in a world file. This world file contains all the information related
to your simulation, i.e. where are the objects, how do they look like, how do
they interact with each other, what is the color of the sky, where is the
gravity vector, etc.

Webots is currently open and runs an arbitrary simulation.

A new world is now open. For now, the 3D window displays a black screen. This is
normal because the scene tree contains only the following fundamental nodes:
`WorldInfo` (containing misc global parameters), `Viewpoint` (defining the main
camera parameters) and `Background` (defining the background color). As no light
and no 3D object are defined, the entire scene is empty and unlit, and so black.

The first step is about to modify the background color.

Now we would like to add some light to the scene.

Now we would like to add some environment (a floor and some walls). A predefined
high-level node called `RectangleArena` is designed to do this task quickly.

It's a good time to improve the scene light.

Now your environment should look like the one depicted in the .

### Add an e-puck Robot

The e-puck is a small robot having differential wheels, 10 LEDs, and several
sensors including 8 distance sensors and a camera. In this tutorial we are only
interested in using its wheels. We will learn how to use some other e-puck
features in the other tutorials.

Now we are going to add an e-puck model to the world. Make sure that the
simulation is paused and that the virtual time elapsed is 0.

As we don't need to create the e-puck robot from scratch, we will just have to
import a special E-puck node (in fact: a PROTO node as the `RectangleArena` we
introduced before). A PROTO is an abstract assemblage of several nodes. PROTO
nodes are defined in separate ".proto", but this will be explained in more
details later. For now consider the E-puck node as a black box that contains all
the necessary nodes to define a e-puck robot.

Now we are going to modify the world and decrease the step of the physics
simulation: this will increase the accuracy of the simulation.

Just after you added the E-puck node, a black window appeared in the upper left
corner of the 3D view. It shows the content of Camera nodes, but it will stay
black until not explicitly used during a simulation. In order to hide it, you
simply have to set the `pixelSize` equal to 0. Then, if you want to re-enable
them, you have to set this field value to a positive number. Detailed
definitions can be found in chapter 3 of the `Reference Manual`.

### Create a new Controller

We will now program a simple controller that will just make the robot move
forwards. As there is no obstacle, the robot will go forwards for ever. Firstly
we will create and edit the C controller, then we will link it to the robot.

The new C source file is displayed in Webots text editor window. This C file can
be compiled without any modification, however the code has no real effect. We
will now link the E-puck node with the new controller before modifying it.

If everything is ok, your robot should go forwards.

### Conclusion

We hope you enjoyed creating your first simulation. You have been able to set up
your environment, to add a robot and to program it. The important thing is that
you learnt the fundamental concepts summarized below:

A Webots world is made of nodes organized in a VRML-like tree structure. A world
is saved in a ".wbt" file stored in a Webots project. The project also contains
the robot controllers which are the programs that define the robots behavior.
Robot controllers can be written in C (or other languages). C controllers have
to be compiled before they can be executed. Controllers are linked to robots via
the `controller` fields of the robot nodes.

## Tutorial 2: Modification of the Environment (20 minutes)

In this tutorial, we will teach you how to create simple objects in the
environment. The first step will be to create a ball which will interact with
the environment. We will tackle several concepts related to the nodes: what is
their meaning, how to create them, how they have to be affiliated, etc. Moreover
we will see how to set up physics.

Several kinds of nodes will be introduced. We won't define each of them
precisely. Their detailed definition can be found in chapter 3 of the `Reference
Manual`. Having the nodes chart diagram (chapter 2 of the `Reference Manual`) in
front of you, will also help understanding the nodes inheritance relationship.

### A new Simulation

First we create a new simulation based on the one created in Tutorial 1.

### Modification of the Floor

The default `RectangleArena` PROTO defines a simple floor pinned on the statical
environment, i.e. without Physics node, and surrounded by walls.

Other pre-built floors are available in the Webots objects library. We will now
delete the default arena and add a simple floor that we will manually surround
the walls later in this this tutorial.

The newly added `Floor` PROTO has a default size of 10mx10m, but it is possible
to adjust its size, its position and texture by changing the corresponding
fields.

### The Solid Node

This subsection introduces the most important node in Webots: the `Solid` node.
But let's start with a definition.

The physics engine of Webots is designed for simulating rigid bodies. An
important steps, when designing a simulation, is to break up the various
entities into undividable rigid bodies.

To define a rigid body, you will have to create a Solid node. Inside this node
you will find different subnodes corresponding to the characteristics of the
rigid body. The  depicts a rigid body and its subnodes. The graphical
representation of the Solid is defined by the Shape nodes populating its
`children` list. The collision bounds are defined by its `boundingObject` field.
The graphical representation and the collision shape are often but not
necessarily identical. Finally the `physics` field defines if the object belongs
to the dynamical or to the statical environment. All these subnodes are
optional, but the `physics` field needs the `boundingObject` to be defined.

![
     The simplest model of a rigid body in Webots having a graphical representation (Shape),
     a physical bound (boundingObject) and being in the dynamical environment (Physics).
    ](pdf/tutorial_solid.pdf)
**
     The simplest model of a rigid body in Webots having a graphical representation (Shape),
     a physical bound (boundingObject) and being in the dynamical environment (Physics).
    **

The Geometry box (in ) stands for any kind of geometrical primitive. In fact it
can be substituted by a Sphere, a Box, a Cylinder, etc.

### Create a Ball

We will now add a ball to the simulation. That ball will be modeled as a rigid
body as shown in the . As Geometry nodes we will use Spheres.

![
     Your first rigid body in Webots.
    ](png/tutorial_ball.png)
**
     Your first rigid body in Webots.
    **

### Geometries

To define the ball, we used the Sphere node in two different contexts: for the
graphical representation (`children`) and to define the physical bounds
(`boundingObject`). All Geometry node (such as the Sphere node) can be used in a
graphical context. However, only a subset of them can be used in a physical
context. Take a look at the schema of the chapter 2 of the `Reference Manual` to
now which primitive you can use.

We want now to reduce the size of the Sphere and to increase its graphical
quality by increasing the number of triangles used to represent it.

### DEF-USE mechanism

We will see in this subsection a mechanism which can be useful to avoid
redundancy in the world files.

The two Sphere definitions that we have used earlier to define the ball, are
redundant. We will now merge these two Spheres into only once using the DEF-USE
mechanism.

![
    DEF-USE mechanism on the Sphere node called "BALL_GEOMETRY".
   ](png/tutorial_def_use.png)
**
    DEF-USE mechanism on the Sphere node called "BALL_GEOMETRY".
   **

![
    DEF-USE mechanism applied on the Shape node of a Solid.
   ](pdf/tutorial_def_use_shape.pdf)
**
    DEF-USE mechanism applied on the Shape node of a Solid.
   **

### Add Walls

In order to verify your progression, implement by yourself four walls to
surround the environment. The walls have to be defined statically to the
environment, and use as much as possible the DEF-USE mechanism at the Shape
level rather than at the Geometry level. Indeed it's more convenient to add an
intermediate Shape node in the `boundingObject` field of the Solid node. The
best Geometry primitive to implement the walls is the Box node. Only one Shape
has to be defined for all the walls. The expected result is shown in .

The solution is located in the solution directory under the "obstacle.wbt".

![
    The simulation state at the end of this second tutorial.
   ](png/tutorial_walls.png)
**
    The simulation state at the end of this second tutorial.
   **

### Efficiency

### Conclusion

At the end of this tutorial, you are able to create simple environments based on
rigid bodies. You are able to add nodes from the scene tree view and to modify
their fields. You have a more precise idea of what are the Solid, the Physics,
the Shape, the Sphere and the Box nodes. You saw also the DEF-USE mechanism that
allows to reduce node redundancy of the scene tree.

## Tutorial 3: Appearance (15 minutes)

The aim of this tutorial is to familiarize yourself with some nodes related to
the graphical rendering. Good looking simulations can be created very quickly
when these nodes are used adequately. A good graphics quality does not only
enhance the user's experience, it is also essential for simulations where robots
perceive their environment (camera image processing, line following, etc.).

The result at the end of this tutorial is shown in .

### New simulation

### Lights

Your simulation is currently lighted by a PointLight node at the top of the
scene. We want to replace this light node by a DirectionalLight node casting
shadows.

### Modify the Appearance of the Walls

The aim of this subsection is to color the walls with blue.

### Add a Texture to the Ball

The aim of this subsection is to apply a texture on the ball. A texture on a
rolling object can help to appreciate its movement.

![
    Simulation after having setup the Light and the Appearance nodes.
   ](png/tutorial_appearance.png)
**
    Simulation after having setup the Light and the Appearance nodes.
   **

### Rendering Options

Webots offers several rendering modes available in the `View` menu.

### Conclusion

In this tutorial, you have learnt how to set up a good looking environment using
the Appearance node and the light nodes.

You can go further on this topic by reading the detailed description of these
nodes in the `Reference Manual`. The  will give you a method to efficiently
setup these nodes.

## Tutorial 4: More about Controllers (20 minutes)

Now we start to tackle the topics related to programming robot controllers. We
will design a simple controller that avoids the obstacles created in the
previous tutorials.

This tutorial will introduce you to the basics of robot programming in Webots.
At the end of this chapter, you should understand what is the link between the
scene tree nodes and the controller API, how the robot controller has to be
initialized and cleaned up, how to initialize the robot devices, how to get the
sensor values, how to command the actuators, and how to program a simple
feedback loop.

This chapter only addresses the correct usage of Webots functions. The study of
robotics algorithms is beyond the goals of this tutorial and so this won't be
addressed here. Some rudimentary programming knowledge is required to tackle
this chapter (any C tutorial should be a sufficient introduction). At the end of
the chapter, links to further robotics algorithmics are given.

### New World and new Controller

### Understand the e-puck Model

Controller programming requires some information related to the e-puck model.
For doing the collision avoidance algorithm, we need to read the values of its 8
infra-red distance sensors located around its turret, and we need to actuate its
two wheels. The way that the distance sensors are distributed around the turret
and the e-puck direction are depicted in .

The distance sensors are modeled by 8 DistanceSensor nodes in the hierarchy of
the robot. These nodes are referenced by their `name` fields (from "ps0" to
"ps7"). We will explain later how these nodes are defined. For now, simply note
that a DistanceSensor node can be accessed through the related module of the
Webots API (through the "webots/distance_sensor.h" include file). The values
returned by the distance sensors are scaled between 0 and 4096 (piecewise
linearly to the distance), while 4096 means that a big amount of light is
measured (an obstacle is close) and 0 means that no light is measured (no
obstacle).

In the same way, the e-puck root node is a DifferentialWheel node and can be
access by the "webots/differential_wheel.h" include file. The speed is given in
a number of ticks/seconds where 1000 ticks correspond to a complete rotation of
the wheel. The values are clamped between -1000 and 1000.

![
    Top view of the e-puck model.
    The green arrow indicates the front of the robot.
    The red lines represent the directions of the infrared distance sensors.
    The string labels corresponds to the distance sensor names.
   ](png/tutorial_e-puck_top_view.png)
**
    Top view of the e-puck model.
    The green arrow indicates the front of the robot.
    The red lines represent the directions of the infrared distance sensors.
    The string labels corresponds to the distance sensor names.
   **

![
    UML state machine of a simple feedback loop
   ](pdf/tutorial_feedback_loop.pdf)
**
    UML state machine of a simple feedback loop
   **

### Program a Controller

We would like to program a very simple collision avoidance behavior. You will
program the robot to go forwards until an obstacle is detected by the front
distance sensors, and then to turn towards the obstacle-free direction. For
doing that, we will use the simple feedback loop depicted in the UML state
machine in .

The complete code of this controller is given in the next subsection.

### The Controller Code

Here is the complete code of the controller detailed in the previous subsection.


``` c
#include ltwebots/robot.hgt
#include ltwebots/differential_wheels.hgt
#include ltwebots/distance_sensor.hgt

// time in [ms] of a simulation step
#define TIME_STEP 64

// entry point of the controller
int main(int argc, char **argv)
{
  // initialize the Webots API
  wb_robot_init();

  // internal variables
  int i;
  WbDeviceTag ps[8];
  char ps_names[8][4] = {
    "ps0", "ps1", "ps2", "ps3",
    "ps4", "ps5", "ps6", "ps7"
  };
  
  // initialize devices
  for (i=0; ilt8 ; i++) {
    ps[i] = wb_robot_get_device(ps_names[i]);
    wb_distance_sensor_enable(ps[i], TIME_STEP);
  }
  
  // feedback loop
  while (1) { 
    // step simulation
    int delay = wb_robot_step(TIME_STEP);
    if (delay == -1) // exit event from webots
      break;
      
    // read sensors outputs
    double ps_values[8];
    for (i=0; ilt8 ; i++)
      ps_values[i] = wb_distance_sensor_get_value(ps[i]);
    
    // detect obstacles
    bool left_obstacle =
      ps_values[0] gt 100.0 ||
      ps_values[1] gt 100.0 ||
      ps_values[2] gt 100.0;
    bool right_obstacle =
      ps_values[5] gt 100.0 ||
      ps_values[6] gt 100.0 ||
      ps_values[7] gt 100.0;

    // init speeds
    double left_speed  = 500;
    double right_speed = 500;
    
    // modify speeds according to obstacles
    if (left_obstacle) {
      left_speed  -= 500;
      right_speed += 500;
    }
    else if (right_obstacle) {
      left_speed  += 500;
      right_speed -= 500;
    }
    
    // write actuators inputs
    wb_differential_wheels_set_speed(left_speed, right_speed);
  }
  
  // cleanup the Webots API
  wb_robot_cleanup();
  return 0; //EXIT_SUCCESS
}
```

### Conclusion

Here is a quick summary of the key points you need to understand before going
on:

The  explains in more detail controller programming. We invite you to read
carefully this section before going on.

## Tutorial 5: Compound Solid and Physics Attributes (15 minutes)

The aim of this chapter is to explore in more detail the physics simulation by
creating a solid with several bounding objects: a dumbbell made of two spheres
and one cylinder. The expected result is depicted in .

![
    Expected result at the end of the tutorial about compound solids.
   ](png/tutorial_dumbbell.png)
**
    Expected result at the end of the tutorial about compound solids.
   **

### New simulation

### Compound Solid

It is possible to build Solid nodes more complex than what we have seen before
by aggregating Shape nodes. In fact, both the physical and the graphical
properties of a Solid can be made of several Shape nodes. Moreover each Shape
node can be placed in a Transform node in order to change its relative position
and orientation. Group nodes can also be used to group several subnodes.

We want to implement a dumbbell made of a handle (Cylinder) and of two weights
(Sphere) located at each end of the handle. The  depicts the Solid nodes and its
subnodes required to implement the dumbbell.

![
    Representation of the subnodes of a compound solid made of
    several transformed geometries.
   ](pdf/tutorial_compound_solid.pdf)
**
    Representation of the subnodes of a compound solid made of
    several transformed geometries.
   **

### Physics Attributes

The aim of this subsection is to learn how to set some simple physics properties
for a Solid node. The Physics node contains fields related to the physics of the
current rigid body (Solid).

### The Rotation Field

### How to choose bounding Objects?

As said before, minimizing the number of bounding objects increases the
simulation speed. However choosing the bounding objects primitives carefully is
also crucial to increase the simulation speed.

Using a combination of Sphere, Box, Capsule and Cylinder nodes for defining
objects is very efficient. Generally speaking, the efficiency of these
primitives can be sorted like this: Sphere > Box > Capsule > Cylinder. Where the
Sphere is the most efficient. But this can be neglected for a common usage.

The IndexdedFaceSet geometry primitive can also be used in a bounding object.
But this primitive is less efficient than the other primitives listed above.
Moreover its behavior is sometimes buggy. For this reasons, we don't recommend
using the IndexdedFaceSet when another solution using a combination of the other
primitives is possible.

Grounds can be defined using the Plane or the ElevationGrid primitives. The
Plane node is much more efficient than the ElevationGrid node, but it can only
be used to model a flat terrain while the ElevationGrid can be used to model an
uneven terrain.

### Contacts

We want now to modify the friction model between the dumbbell and the other
solids of the environment.

### basicTimeStep, ERP and CFM

The most critical parameters for a physics simulation are stored in the
`basicTimeStep`, `ERP` and `CFM` fields of the WorldInfo node.

The `basicTimeStep` field determines the duration (in [ms]) of a physics step.
The bigger this value is, the quicker the simulation is, the less precise the
simulation is. We recommend values between *8* and *16* for a regular use of
Webots.

It's more difficult to explain the behavior of the `ERP` and `CFM` fields. These
values are directly used by the physics engine to determine how the constraints
are solved. The default values are well defined  for a regular use of Webots. We
recommend to read the `Reference Manual` and the documentation of `ODE` (physics
engine used in Webots) to understand completely their purpose.

### Minor physics Parameters

There are also other physics parameters which are less useful in a regular use
of Webots. A complete description of these parameters can be found in the
`Reference Manual`. Remark simply that the Physics, WorldInfo and
ContactProperties nodes contains other fields.

### Conclusion

You are now able to build a wide range of solids including those being composed
of several rigid bodies. You know that a Geometry node can be moved and rotated
if it is included in a Transform node. You are aware about all the physics
parameters allowing you to design robust simulations. The next step will be to
create your own robot.

You can test your skills by creating common objects such as a table.

## Tutorial 6: 4-Wheels Robot

The aim of this tutorial is to create your first robot from scratch. This robot
will be made of a body, four wheels, and two distance sensors. The result is
depicted in . The  shows the robot from a top view.

![
    3D view of the 4 wheels robot.
    Note that the coordinate system representations of the robot body
    and of its wheels are oriented the same way.
    Their +x-vector (in red) defines the left of the robot,
    their +y-vector (in green) defines the top of the robot, and
    their +z-vector (in blue) defines the front of the robot.
    The distance sensors are oriented in a different way,
    their +x-vector indicates the direction of the sensor.
   ](png/tutorial_4_wheels_robot.png)
**
    3D view of the 4 wheels robot.
    Note that the coordinate system representations of the robot body
    and of its wheels are oriented the same way.
    Their +x-vector (in red) defines the left of the robot,
    their +y-vector (in green) defines the top of the robot, and
    their +z-vector (in blue) defines the front of the robot.
    The distance sensors are oriented in a different way,
    their +x-vector indicates the direction of the sensor.
   **

![
    Top view of the 4 wheels robot.
    The grid behind the robot has a dimension of 0.2 x 0.3 [m].
    The text labels correspond to the name of the devices.
   ](png/tutorial_4_wheels_top_schema.png)
**
    Top view of the 4 wheels robot.
    The grid behind the robot has a dimension of 0.2 x 0.3 [m].
    The text labels correspond to the name of the devices.
   **

### New simulation

### Separating the Robot in Solid Nodes

Some definitions are required before giving rules to create a robot model.

The set containing the Solid node and all its derived nodes is called the *solid
nodes*. A similar definition is applied for the Device, Robot, Joint and Motor
nodes. You can get more information about the node hierarchy in the `Reference
Manual`. Note that the solid nodes and device nodes is close but don't match
perfectly.

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

In our case, the body box is obviously the better choice. The  depicts the solid
nodes hierarchy of the robot.

![
    High level representation of the 4 wheels robot
   ](pdf/tutorial_4_wheels_highlevel.pdf)
**
    High level representation of the 4 wheels robot
   **

![
    Low level representation of the 4 wheels robot
   ](pdf/tutorial_4_wheels_lowlevel.pdf)
**
    Low level representation of the 4 wheels robot
   **

### HingeJoints

The initial position of the Wheel is defined by the translation and the rotation
fields of the Solid node. While the rotation origin (anchor) and the rotation
axis (axis) are defined by the optional HingeJointParameters child of the
HingeJoint node.

For the first wheel, the Solid translation should be defined to *(0.06, 0,
0.05)* in order to define the relative gap between the body and the wheel. The
HingeJointParameters anchor should also be defined to *(0.06, 0, 0.05)* to
define the rotation origin (relatively to the body). Finally the
HingeJointParameters axis should define the rotation axis. In our case it's
along the x-axis (so *(1, 0, 0)*).

We want now to implement the cylinder shape of the wheels. As the Cylinder node
is defined along the *y*-axis, a Transform node should encapsulate the Shape to
rotate the Cylinder along the along the *x*-axis.

### Sensors

The last part of the robot modeling is to add the two distance sensors to the
robot. This can be done by adding two DistanceSensor nodes as direct children of
the Robot node. Note that the distance sensor acquires its data along the
+*x*-axis. So rotating the distance sensors in order to point their *x*-axis
outside the robot is necessary (see the ).

### Controller

In the previous tutorials, you learnt how to setup a feedback loop and how to
read the distance sensor values. However actuating the RotationalMotor nodes is
new. The following note explain how to proceed.

### Conclusion

You are now able to design simple robot models, to implement them and to create
their controllers.

More specifically you learnt the different kind of nodes involved in the
building of the robot models, the way to translate and rotate a solid relatively
to another, the way that a rotational motor is actuated by the controller.

## Tutorial 7: Using ROS

This tutorial explains how to implement a Webots controller as a ROS node. This
process is exemplified by describing how we built the "joystick" controller
located in "WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick".

### Creating a Webots project that contains a ROS package

The "joystick" controller is a Webots controller written in C++ and implemented
as a ROS node. It subscribes to the *joy/joy* topic of the "joy_node" (see ROS
"joy" package) in order to listen to the joystick state. The relevant line in
"webots_joystick_node.cpp" is: `ros::Subscriber sub=nh.subscribe("joy", 10,
joy_callback);` which prompts ten times per second the callback function
*joycall_back* to transform the joystick sensed values into a robot motion
command.

We now describe the actions to setup the controller directory
"WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick" both on ROS
and Webots side (as provided in your Webots distribution). We are to recreate
the corresponding project based on its bare bones: the world file
"WEBOTS_MODULES_PATH/projects/languages/ros/worlds/joystick.wbt", the source
file "WEBOTS_MODULES_PATH/projects/languages/ros/controller/catkin_ws/src/webots
_joystick/src/webots_joystick_node.cpp" and the ROS launcher file
"WEBOTS_MODULES_PATH/projects/languages/ros/controller/joy.launch". Note that
"joy.launch" is used in "webots_joystick_node.cpp" to launch the ROS node
"joy_node" as child process:


```
  // launch the joy ROS node
      int roslaunch=fork();
      if (roslaunch==0) { // child process
        execlp("roslaunch","roslaunch","joy.launch",NULL);
        return 0;
      }
    
```

We will be done once we will have provided Webots with an executable file in
"WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick" whose name
matches the controller directory name, i.e. "joystick" (which is also the name
specified in "joystick.wbt"). As we want this executable to be a ROS a node, we
will create and build a ROS package called "webots_joystick" and copy the
resulting executable in
"WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick".

Prior to package construction, we create and setup a *catkin* workspace from
which we will run most of the build process through the `catkin_make` command.

### Conclusion

You should be able to run the "joystick" you just built as the original one
(open "~/my_ros/worlds/joystick.wbt" and hit the play button). You hence
achieved a fully functional Webots controller implemented as a ROS node.
Exploring further Webots C/C++ and Python APIs will allow you to integrate
larger ROS frameworks.

## Going Further

You have now enough knowledge to set up your own simulation Webots. You are able
to design and implement a robot, to setup its controller and to design an
environment.

However the Webots possibilities go much beyond this. Reading the documentation
related with your application in the `User Guide` or in the `Reference Manual`
is the first step to extend your knowledge.

The algorithmic to develop your controllers is not explained in the Webots
documentation. However another tutorial known as "curriculum" tackle some famous
robot programming problems through a sequence of exercises using the e-puck
robot and the C language.

