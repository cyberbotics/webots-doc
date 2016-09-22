## Using the Nao robot

### Introduction

The Nao robot is a humanoid robot developed by [Aldebaran
Robotics](http://www.aldebaran-robotics.com). This section explains how to use
Nao robot simulated in Webots together with the Choregraphe program of
[Aldebaran Robotics](http://www.aldebaran-robotics.com). Currently, Webots
supports the Nao v3.3, v4.0 and v5.0 versions, with and without their
articulated fingers (respectively with 25 and 21 degrees of freedom) for the
first two.

The Webots installation includes several world files with Nao robots. You will
find some in this folder: "WEBOTS\_HOME/projects/robots/aldebaran/worlds". The
"nao.wbt" and "nao\_indoors.wbt" are meant to be used with Choregraphe (see
below). The "nao\_demo.wbt" is a demonstration of a very simple controller that
uses Webots C API instead of Choregraphe. The "nao\_matlab.wbt" world is an
example of programming Webots using the Matlab API. The "nao\_robocup.wbt" world
is an example of how to use the NAOqi API inside Webots. It is the same API that
is used in Choregraphe, meaning that you can program Nao inside Webots without
using Choregraphe if you want to. In this world, Nao tries to shoot the ball in
the goal. You can find another NAOqi example in the
"WEBOTS\_HOME/projects/contests/nao\_challenge/2013-2014/worlds" folder. The
"challenge.wbt" file in this folder is a solution to the NAO Challenge contest
(edition 2013-2014).

In addition to that, Nao robots are also used in the world files of the
[Robotstadium](http://www.robotstadium.org) contest. These files are located in
this folder: "WEBOTS\_HOME/projects/contests/robotstadium/worlds".

### Using Webots with Choregraphe

These instructions have been tested with Webots 8.0.0 and Choregraphe 2.1.1.10.
Please note that Webots must not be launched as root when using any world
containing naoqisim, otherwise Choregraphe won't be able to send instructions to
the robot in Webots.

Start Webots and open this world file:
"WEBOTS\_HOME/projects/robots/aldebaran/worlds/nao.wbt" You should see a red Nao
in an empty environment. If the simulation is paused, then please start it by
pushing the `Real-time` button in Webots.

The camera images in Webots (small purple viewports) should reflect what the
robot sees.

Several lines of text information corresponding to the output of NAOqi should be
printed to Webots console.

Now you can start Choregraphe with the --no-naoqi option. Please make sure the
Choregraphe version matches the NAOqi version printed in Webots console. In
Choregraphe choose the menu `Connection / Connect to...`. Then in the list,
select the NAOqi that was started by Webots, on you local machine, it will have
the port number 9559, unless you change it. Note that the NAOqi will not appear
in the list if the simulation was not started in Webots. If the simulation was
started but the robot still doesn't appear in the list, force the IP and port to
127.0.0.1 and 9559 in Choregraphe and then press connect.

At this point a Nao model matching the Webots model should appear in
Choregraphe. Now, in Choregraphe toggle the "Wake up" button, which is a little
sun in the rop right of the window. Nao is currently in the "Stand Zero" pose,
you can change its starting pose using the posture library in Choregraphe.

Then double-click on any of the Nao parts in Choregraphe: a small window with
control sliders appears. Now, move any of the sliders: the motor movement in
Choregraphe should be reflected in the Webots simulation. If you open the Video
monitor in Choregraphe you should see the picture of the Nao camera simulated by
Webots.

### Nao models

You can switch between the Nao model thanks to the following Nao PROTO fields:

- *version* corresponds to the real Nao version. The supported versions are "3.3",
"4.0" and "5.0". The main difference between these models is the different
calibration of the physics. The field of view of the cameras is slightly
different, too. Please refer directly to the Nao.proto file to see the complete
difference. Note that each version having a different weight repartition in
their body, the best contact properties in the simulated world aren't always the
same. They are currently optimized for the version 5.0 of Nao in the default Nao
worlds and may not perform as well with previous versions of Nao.
- *degreeOfFreedom* corresponds to the degree of freedom of the real Nao. For
versions 3.3 and 4.0 of Nao, the supported degreeOfFreedom values are 25 and 21.
This corresponds to a model respectively with and without articulated fingers.
We recommend to use articulated fingers only if necessary because of their big
resource consumption. Version 5.0 does not exist without articulated fingers, so
the only possible value is 25 in this case.

### Using motion boxes

Now we can test some of the motion boxes of Choregraphe. A simple example is a
sit down -> stand up motion. In Choregraphe, select the "Sit Down" and "Stand
Up" boxes from `Box libraries > default`. Drag and drop them in central view.
Then connect the global "onStart" input to the "Sit Down" box's "onStart" input,
and the output of this box to the "Stand Up" box's "onStart" input. Now make
sure the simulation is running, and, push the `Play` button in Choregraphe. This
will make the robot sit down, and then stand up once he is done sitting down.

### Using the cameras

Webots simulates Nao's top and bottom cameras. Using Aldebaran's Choregraphe or
the Monitor programs, it is possible to switch between these cameras. In
Choregraphe, use the "Select Camera" box in `Box Library / Vision`. The
simulated camera image can be viewed in Choregraphe: `View / Video monitor`. The
resolution of the image capture can be changed in Webots using the `cameraWidth`
and `cameraHeight` fields of the robot. Note that the simulation speed decreases
as the resolution increases. It is possible to hide the camera viewports (purple
frame) in Webots, by setting the `cameraPixelSize` field to 0. It is also
possible to completely switch off the simulation of the cameras by adding the
"-nocam" option before the NAOqi port number in the `controllerArgs` field, e.g.
"-nocam 9559".

### Using Several Nao robots

It is possible to have several Nao robots in your simulation, however each Nao
robot must use a different NAOqi port. Here's how to copy a Nao and assign the
NAOqi port number:

1. Pause the simulation: push the `Pause` button in Webots 3D View
2. Revert the simulation: push the `Revert` button in Webots 3D View
3. In Webots Scene Tree, select a top level nodes, e.g. the Nao robot
4. Then push the `Add` button, a dialog appears
5. In the dialog, select `PROTO (Webots) / robots`
6. Then select one of the Nao models from the list, the Nao is added to the current
world
7. Select the Nao in the 3D view and move it away from the other one: SHIFT + left
mouse button
8. Select the `controllerArgs` field in the newly created robot and increase the
port number, e.g. 9560
9. Save the .wbt file: push the `Save` button
10. Now you can push the `Real-time` button to run the simulation with several
robots

Repeat the above procedure for each additional robot that you need. Remember
that every robot must have a different port number specified in
`controllerArgs`.

### Getting the right speed for realistic simulation

Choregraphe uses exclusively real-time and so the robot's motions are meant to
be carried out in real-time. The Webots simulator uses a virtual time base that
can be faster or slower than real-time, depending on the CPU and GPU power of
the host computer. If the CPU and GPU are powerful enough, Webots can keep up
with real-time, in this case the speed indicator in Webots shows approximately
1.0x, otherwise the speed indicator goes below 1.0x. Choregraphe motions will
play accurately only if Webots simulation speed is around 1.0x. When Webots
simulation speed drifts away from 1.0x, the physics simulation gets wrong
(unnatural) and thus Choregraphe motions don't work as expected any more. For
example if Webots indicates 0.5x, this means that it is only able to simulate at
half real-time the motion provided by Choregraphe: the physics simulation is too
slow. Therefore it is important to keep the simulation speed as close as possible to 1.0x. There are currently no means of synchronizing Webots and
Choregraphe, but this problem will be addressed in a future release. It is often
possible to prevent the simulation speed from going below 1.0x, by keeping the
CPU and GPU load as low as possible. There are several ways to do that, here are
the most effective ones:

- Switch off the simulation of the Nao cameras with the "-nocam" option, as
mentioned above
- Increase the value of `WorldInfo.displayRefesh` in the Scene Tree
- Switch off the rendering of the shadows: change to FALSE the `castShadows` field
of each light source in the Scene Tree
- Reduce the dimensions of the 3D view in Webots, by manually resizing the GUI
components
- Remove unnecessary objects from the simulation, in particular objects with
physics

### Known Problems

If for some unexpected reason Webots crashes, it is possible that the `hal` or
`naoqi-bin` processes remain active in memory. In this case we recommend you to
terminate these processes manually before restarting Webots.

On Windows, use the Task Manager (the Task Manager can be started by pressing
Ctrl-Alt-Delete): In the Task Manager select the `Processes` tab, then select
each `hal.exe` and `naoqi-bin.exe` line and push the "End Process" button for
each one.

On Linux, you can use the `killall` or the `pkill` commands, e.g.:

```sh
$ killall hal naoqi-bin
```
