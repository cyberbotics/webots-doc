## Tutorial 1: Your first Simulation in Webots (20 minutes)

In this first tutorial, you will create your first simulation. This simulation
will contain a simple environment (a light and an arena with floor and walls), a
predefined robot (e-puck) and a controller program that will make the robot move
(see [this figure](#what-you-should-see-at-the-end-of-the-tutorial)). The
objective of this tutorial is to familiarize yourself with the user interface
and with the basic concepts of Webots.

%figure "What you should see at the end of the tutorial."

![tutorial_e-puck.png](images/tutorial_e-puck.png)

%end

### Create a new World

A World contains information like where the objects
are, what they look like, how they interact with each other, what is the sky
color, where is the gravity vector, etc.

> **Theory**:
A **World** defines the initial state of a simulation.
The different objects are called **Nodes** and are organized hierarchically
in a **Scene Tree**. It means that a node can have some sub-nodes.

<!-- -->

> **Note**:
A world is stored in a file having the ".wbt" extension.
The file format is derived from the **VRML** language, and is
human readable. The world files must be stored directly in the project
subdirectory called "worlds".

Webots is currently open and runs an arbitrary simulation.

> **Hands on**:
Pause the current simulation by clicking on the `Pause` button of the 3D view.
The simulation is paused if the virtual time counter on the 3D view toolbar is
stable.

<!-- -->

> **Hands on**:
Create a new world by selecting the `File / New World` menu item.

A new world is now open. For now, the 3D window displays a black screen.
The Scene Tree view (on the left hand side) currently lists the fundamental nodes:
- `WorldInfo`: containing misc global parameters ;
- `Viewpoint`: defining the main camera parameters ;
- and `Background`: defining the background color.

As no light and no 3D object are defined, the entire scene is empty and unlit, and thus black.

Each node has some customizable properties called **fields**.
The first step is about to modify the background color.

> **Hands on**:
Modify the background color, by setting up the `skyColor` field of the
`Background` node. Choose a blue color (e.g. red = 0.4, green = 0.7 and blue =
1.0) using the color picker at the bottom of the Scene Tree view. The background of
the 3D view should be modified accordingly.

Now, we would like to add some environment object (a floor and some walls).
A predefined node called `RectangleArena` is designed to accomplish this task
quickly.

> **Hands on**:
Select the last node of the Scene Tree view (`Background`). Click on the
`Add` button at the top of the Scene Tree view.
In the open dialog box, choose `PROTO (Webots) / objects / floors
/ RectangleArena`. The new node has been added and is appearing far away. Use
the left click and the wheel of the mouse in the 3D view to choose a better
viewpoint.

However, the rectangle arena appears black because the scene is still unlit.
Now we would like to add some light to the scene.

> **Hands on**:
Select the last node of the Scene Tree view (`RectangleArena`).
Click on the `Add` button. In the open dialog box, choose
`New node / DirectionalLight`. The new node has been added and we can admire our
rectangle arena's colors.

It's a good time to improve the scene light.

> **Hands on**:
Modify the following fields of the `DirectionalLight` node:
- `ambientIntensity` to 1 ;
- `direction` to [-0.33 -1 -0.5] ;
- and `castShadows` to TRUE.

<!-- -->

> **Note**:
In the Scene Tree view, the fields are displayed in blue if they differ from their
default values.

Now your environment should look like the one depicted in the
[figure](prerequisites.md#the-webots-main-window-splits-into-four-dockable-subwindows-the-scene-tree-view-on-the-left-hand-side-including-a-panel-at-the-bottom-for-editing-fields-values-the-3d-view-in-the-center-the-text-editor-on-the-right-hand-side-and-the-console-at-bottom-of-the-window-note-that-some-of-these-subwindows-have-a-toolbar-with-buttons-the-main-menus-appear-on-the-top-of-the-main-window-the-virtual-time-counter-and-the-speedometer-are-displayed-in-the-right-part-of-the-3d-view-toolbar-the-status-text-is-displayed-in-the-bottom-left-of-the-main-window).

> **Hands on**:
Save the new world into your project by selecting the `File / Save World As...`
menu item. Using the dialog box save the world into the
"my\_webots\_projects/tutorials/worlds/my\_first\_simulation.wbt" file location.

<!-- -->

> **Hands on**:
Revert the simulation by selecting the `File / Revert World` menu item.

<!-- -->

> **Note**:
You can change the viewpoint of the 3D view by using the mouse buttons (left
button, right button and the wheel).

<!-- -->

> **Theory**:
Webots nodes stored in world files are organized in a tree structure called the
**scene tree**. The scene tree can be viewed in two subwindows of the main
window: the 3D view (at the center of the main window) is the 3D representation
of the scene tree and the scene tree view (on the left) is the hierarchical
representation of the scene tree. The scene tree view is where the nodes and the
fields can be modified.

<!-- -->

> **Hands on**:
In the 3D view, click on the floor to selected it. When it is selected, the floor
is surrounded by white lines and the corresponding node is selected in the Scene
Tree view. Now click on the blue sky to unselect the floor.

### Add an e-puck Robot

The e-puck is a small robot having differential wheels, 10 LEDs, and several
sensors including 8 distance sensors and a camera. In this tutorial we are only
interested in using its wheels. We will learn how to use some other e-puck
features in the other tutorials.

Now, we are going to add an e-puck model to the world. Make sure that the
simulation is paused and that the virtual time elapsed is 0.

> **Theory**:
When a Webots world is modified with the intention of being saved, it is
fundamental that the simulation is first paused and reverted to its initial
state, i.e. the virtual time counter on the 3D view toolbar should show
0:00:00:000. Otherwise at each save, the position of each 3D objects can
accumulate errors. Therefore, any modification of the world should be performed
in that order: **pause, revert, modify and save the simulation**.

As we don't need to create the e-puck robot from scratch, we will just have to
import a special E-puck node (in fact: a PROTO node as the `RectangleArena` we
introduced before). A PROTO is an abstract assemblage of several nodes. PROTO
nodes are defined in separate ".proto", but this will be explained in more
details later. For now, consider the E-puck node as a black box that contains all
the necessary nodes to define a e-puck robot.

> **Hands on**:
Select the last node of the Scene Tree view (called `RectangleArena`). In order
to add the E-puck node, click on the `Add` button at the top of the Scene Tree
view. In the open dialog box, and choose `PROTO (Webots) / robots / e-puck /
E-puck (DifferentialWheels)`. Then save the simulation.

<!-- -->

> **Note**:
Now if you run the simulation, the robot moves: that's because the robot uses a
default controller with that behavior. Please pause and revert the simulation
before going on.

<!-- -->

> **Note**:
You can change the robot's position in the 3D view using the translation and
rotation handles (see [this section](the-3d-window.md#axis-aligned-handles)).

> Alternatively, the following keyboard shortcuts are available:

> * SHIFT + left-clicking + drag* to move the robot parallel to the floor;

> *SHIFT + mouse-wheel* to move the robot up or down.

> Finally, it is possible to add a force to the robot: *CTRL + ALT + left-clicking
+ drag*.

<!-- -->

> **Note**:
Starting the simulation by pressing the `Run` button will make Webots running
the simulation as fast as possible. In order to obtain a real-time simulation
speed, the `Real-Time` button has to be pressed.

Now we are going to modify the world and decrease the step of the physics
simulation: this will increase the accuracy of the simulation.

> **Hands on**:
In the Scene Tree view, expand the WorldInfo node (the first node). Set its
`basicTimeStep` field to *16*. Then save the simulation.

Just after you added the E-puck node, a black window appeared in the upper left
corner of the 3D view. It shows the content of Camera nodes, but it will stay
black until not explicitly used during a simulation. In order to hide it, you
simply have to set the `pixelSize` equal to 0. Then, if you want to re-enable
them, you have to set this field value to a positive number. Detailed
definitions can be found in chapter 3 of the [Reference
Manual](http://www.cyberbotics.com/reference/).

> **Hands on**:
In this tutorial we will not use the Camera devices of the E-puck. So we can
hide the window by expanding the E-puck node and setting the fields
`camera_pixelSize` to 0. Don't forget to revert the simulation before changing
the values and to save it after the modifications.

### Create a new Controller

We will now program a simple controller that will just make the robot move
forwards. As there is no obstacle, the robot will go forwards for ever. Firstly
we will create and edit the C controller, then we will link it to the robot.

> **Theory**:
A **controller** is a program that defines the behavior of a robot. Webots
controllers can be written in the following programming languages: C, C++, Java,
Python, Matlab, etc. Note that C, C++ and Java controllers need to be compiled
before they can be run as robot controllers. Python and Matlab controllers are
interpreted languages so they will run without being compiled. The `controller`
field of a robot specifies which controller is currently linked with to it.
Please take notice that a controller can be used by several robots, but a robot
cans use only one controller at a time.

<!-- -->

> **Note**:
Each robot controller is executed in a separate child process spawned by Webots.
Controllers don't share the same address space, and they can run in different
processor cores.

<!-- -->

> **Note**:
Other languages than C are available but may require a setup. Please refer to
the language chapter to setup the other languages (see [this
chapter](language-setup.md)).

<!-- -->

> **Hands on**:
Create a new C controller called *e-puck\_go\_forward* using the `Wizards / New
Robot Controller...` menu. This will create a new "e-puck\_go\_forward"
directory in "my\_webots\_projects/tutorials/controllers". Select the option
asking you to open the source file in the text editor.

The new C source file is displayed in Webots text editor window. This C file can
be compiled without any modification, however the code has no real effect. We
will now link the E-puck node with the new controller before modifying it.

> **Hands on**:
Link the `E-puck` node with the *e-puck\_go\_forward* controller. This can be
done in the Scene Tree view by selecting the `controller` field of the E-puck
node, then use the field editor at the bottom of the Scene Tree view: press the
`Select...` button and then select *e-puck\_go\_forward* in the list. Once the
controller is linked, save the world.

<!-- -->

> **Hands on**:
Modify the program by inserting an include statement (`#include
<webots/differential_wheels.h>`), and by applying a differential wheels command
(`wb_differential_wheels_set_speed(100, 100)`) :

> ```c
> #include <webots/robot.h>
>
> // Added a new include file
> #include <webots/differential_wheels.h>
>
> #define TIME_STEP 64
>
> int main(int argc, char **argv)
> {
>   wb_robot_init();
>
>   // set up the speeds
>   wb_differential_wheels_set_speed(100, 100);
>
>   while (wb_robot_step(TIME_STEP) != -1);
>
>   wb_robot_cleanup();
>
>   return 0;
> }
> ```

<!-- -->

> **Hands on**:
Save the modified source code (`File / Save Text File`), and compile it (`Build
/ Build`). Fix any compilation error if necessary. When Webots proposes to
revert the simulation, choose `Yes`.

If everything is ok, your robot should go forwards.

> **Note**:
In the "controllers" directory of your project, a directory containing the
*e-puck\_go\_forward* controller has been created. The "e-puck\_go\_forward"
directory contains an "e-puck\_go\_forward" binary file generated after the
compilation of the controller. Note that the controller directory name should
match with the binary name.

### Conclusion

We hope you enjoyed creating your first simulation. You have been able to set up
your environment, to add a robot and to program it. The important thing is that
you learnt the fundamental concepts summarized below:

A Webots world is made up of nodes organized in a VRML-like tree structure. A world
is saved in a ".wbt" file stored in a Webots project. The project also contains
the robot controllers which are the programs that define the robots' behavior.
Robot controllers can be written in C (or other languages). C controllers have
to be compiled before they can be executed. Controllers are linked to robots via
the `controller` fields of the robot nodes.
