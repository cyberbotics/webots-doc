## Using ROS

### What is ROS?

[ROS](http://www.ros.org/) (Robot Operating System) is a framework for robot
software development, providing operating system-like functionality on top of a
heterogenous computer cluster. ROS was originally developed in 2007 by the
Stanford Artificial Intelligence Laboratory. As of 2008, development continues
primarily at [Willow Garage](http://www.willowgarage.com/).

ROS provides standard operating system services such as hardware abstraction,
low-level device control, implementation of commonly-used functionality,
message-passing between processes, and package management. It is based on a
graph architecture where processing takes place in nodes that may receive, post
and multiplex sensor, control, state, planning, actuator and other messages. The
library is geared towards a Unix-like system and is supported under Linux,
experimental on Mac OS X and has partial functionality under Windows.

ROS has two basic "sides": The operating system side, ros, as described above
and ros-pkg, a suite of user contributed packages (organized into sets called
stacks) that implement functionality such as simultaneous localization and
mapping, planning, perception, simulation etc.

ROS is released under the terms of the BSD license, and is open source software.
It is free for commercial and research use. The ros-pkg contributed packages are
licensed under a variety of open source licenses.

### ROS for Webots

There are two ways to use ROS with Webots. The first solution and the easiest
one is to use the standard ROS controller. It is part of the Webots default
controllers and is available in any project. This controller can be used on any
robot in Webots and acts as a ROS node, providing all the Webots functions as
services or topics to other ROS nodes. The second custom and more complicated
solution is to build your own Webots controller that will also be a ROS node
using Webots and ROS libraries. This solution should only be used for specific
application that cannot be done with the standard controller.

#### Standard Controller

This controller uses the "libCppController" library and proposes the available
Webots functionalities on the ROS network according to the robot's
configuration. Using the "roscpp" library, it provides these Webots functions
mostly as ROS services and uses standard messages type to avoid dependencies on
third-party packages.

During simulation there can be multiple instances of robots or devices and other
Webots applications connected to the ROS network. Therefore the controller uses
a specific syntax to declare its services or topics on the network:
"[robot\_unique\_name]/[device\_name]/[service/topic\_name]"

"[robot\_unique\_name]": in order to avoid any misunderstanding between
different instances of the same robot, the name of the robot is followed by the
ID of the process and the IP address of the computer.

"[device\_name]": since the same function can refer to different devices, this
field show you which device it refers to.

"[service/topic\_name]": this field is equal or really close to the Webots
function it corresponds. For topics, it is followed by the sampling period. For
services, it is also the name of the corresponding srv file.

#### Using the Standard Controller

The controller is pre-compiled and you shouldn't edit it. All you have to do is
to load it on your robot; you will find it in the default list of controller. In
order to use it, you will have to build a ROS node that will communicates with
the robot using the different services available. Good examples of such ROS node
can be found inside Webots at
"WEBOTS\_MODULES\_PATH/projects/languages/ros/nodes". In this folder you will
find useful instructions to help you.

> **note**:
If you wants to access the controller from another machine and the roscore isn't
running on the same machine as Webots, you will need to edit the
ROS\_MASTER\_URI variable. This can be done by editing your environment
variables, adding the address in the controller arguments in Webots or with a
runtime.ini file in the controller directory. You must also be able to connect
to each of the computer in ssh in both ways. As ROS uses the hostname to find
other computer/devices on the network, you must had other computers' hostname
and the associated IP address to the known hosts of each computer. You can find
this list in a file named *hosts*. On Linux distribution, you can find it
directly at /etc/hosts; on Mac OS X, it is located at /private/etc/hosts; on
Windows, it is located at C:\Windows\System32\drivers\etc\hosts. On Windows and
Mac OS X, this a hidden path and you will need to search directly for this path.
The hosts file is usually protected and you will need administrator or root
right to edit it.

#### Custom Controller

The standard controller has been developed in order to work on every robot and
for general purpose. Sometimes, you may not be able to do what you want with
this controller or it would be too complicated. In this case, you can build your
own custom controller and ROS node.

It is possible to implement such a ROS node in C++ using the "roscpp" library.
However, in this case, you need to setup a build configuration to handle both
the "catkin\_make" from ROS and the "Makefile" from Webots to have the resulting
binary linked both against the Webots "libController" and the "roscpp" library.
An example of such an implementation is included in the Webots distribution (see
below).

This controller can also be implemented in Python by importing both ROS
libraries (roslib, rospy) and Webots libraries (controller) in a Webots robot or
supervisor controller.

#### Using the Custom Controller

A sample C++ ROS node running as a Webots controller is provided in the Webots
distribution for Linux. It is located in the Webots
"WEBOTS\_MODULES\_PATH/projects/languages/ros/custom" folder and contains a
world file named "joystick.wbt" and a controller named "joystick" which allows
the user to drive a simulated robot using a joystick through the ROS joy node.
This controller is a very simple example of a ROS node running as a Webots
controller. It could be used as a starting point to develop more complex
interfaces between Webots and ROS. The controller directory includes all the
"Makefile" machinery to call the build tools used by ROS and Webots to produce
the controller binary. The "ros" folder also includes a "README.txt" file with
detailed installation and usage instructions.

> **note**:
Following the instructions "README.md" is necessary to make the joystick example
work on your Linux system.

> In the [Tutorials](tutorials.md) chapter, you will find a section explaining how
to rebuild from scratch the joystick example.

