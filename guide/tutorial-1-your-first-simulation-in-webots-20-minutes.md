## Tutorial 1: Your first Simulation in Webots (20 minutes)

In this first tutorial, you will create your first simulation. This simulation
will contain a simple environment (a light and an arena with floor and walls), a
predefined robot (e-puck) and a controller program that will make the robot move
(see ). The objective of this tutorial is to familiarize yourself with the user
interface and with the basic concepts of Webots.


%figure "What you should see at the end of the tutorial."
![What you should see at the end of the tutorial.](png/tutorial_e-puck.png)
%end

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
definitions can be found in chapter 3 of the [Reference
Manual](http://www.cyberbotics.com/reference/).

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

