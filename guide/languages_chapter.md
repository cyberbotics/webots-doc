# Language Setup

Webots controllers can be written in C/C++, Java, Python or `MATLAB`. This
chapter explains how to install the software development kits for the
programming language of your choice.

## Introduction

Webots can execute controllers written in compiled (C/C++, Java) or interpreted
(Python, `MATLAB`) languages. The compilation or interpretation process requires
extra software that must usually be installed separately. Only when using C/C++
on the Windows platform it is not necessary to install a separate C/C++
compiler; on this platform Webots comes with a pre-installed and preconfigured
copy of the MinGW C/C++ compiler. For any other language or platform the
software development tools must be installed separately. Note that Webots uses
very standard tools that may already be present in a standard installation.
Otherwise the instructions in this chapter will advise you about the
installation of your software development tools.

## Controller Start-up

The .wbt file contains the name of the controller that needs to be started for
each robot. The controller name is platform and language independent field; for
example when a controller name is specified as "xyz_controller" in the .wbt
file, this does not say anything about the controller's programming language or
platform. This is done deliberately to ensure the platform and programming
language independence of .wbt files.

So when Webots tries to start a controller it must first determine what
programming language is used by this controller. So, Webots looks in the
project's "controllers" directory for a subdirectory that matches the controller
name. Then, in this controller directory, it looks for a file that matches the
controller name. For example if the controller name is "xyz_controller", then
Webots looks for these files in the specified order, in the
"PROJECT_DIRECTORY/controllers/xyz_controller" directory.

The first file that is found will be executed by Webots using the required
language interpreter (java, python, matlab). So the priority is defined by the
file extension, e.g. it won't be possible to execute "xyz_controller.m" if a
file named "xyz_controller.py" is also present in the same controller directory.
In the case that none of the above filenames exist or if the required language
interpreter is not found, an error message will be issued and Webots will start
the "void" controller instead.

## Using C

### Introduction

The C API (Application Programming Interface) is composed of a set of about 200
C functions that can be used in C or C++ controller code. This is the low level
interface with the Webots simulator; all other APIs are built over the C API. A
majority of Webots controller examples are written in C, therefore the C API is
Webots de facto standard API. Although less represented in the controller
examples, the other APIs offer exactly the same functionality as the C API.

### C/C++ Compiler Installation

#### Windows Instructions

The Windows version of Webots comes with a pre-installed copy of the MinGW C/C++
compiler, so there is usually no need to install a separate compiler. The MinGW
compiler is a port of the GNU Compiler Collection (gcc) on the Windows platform.
The advantage of using the MinGW compiler will be the better portability of your
controller code. If you develop your code with MinGW it will be straightforward
to recompile it on the other Webots supported platforms: Mac OS X and Linux.
However, if you prefer using the Visual C++ compiler you will find instructions
`there`.

#### Mac OS X Instructions

In order to compile C/C++ controllers on the Mac, you will need to install Apple
Xcode. Xcode is a suite of tools, developed by Apple, for developing software
for Mac OS X. Xcode is free and can be downloaded from the Apple App Store.
Webots will need principally the `gcc` (GNU C Compiler) and `make` commands of
Xcode. To install these commands, start Xcode and go to Xcode menu, Preferences,
Downloads, Components and click `Install` for "Command Line Tools".

#### Linux Instructions

For compiling C controllers, Webots will need the GNU C Compiler and GNU Make
utility. On Linux, these tools are often pre-installed, otherwise you will need
to install them separately (*gcc* and *make* packages). For C++ you will also
need the GNU C++ Compiler (*g++* package). Optionally you can also install the
GNU Debugger (*gdb* package).

## Using C++

### Introduction

The C++ API is a wrapper of the C API described in the previous section. The
major part of the C functions has been wrapped in a function of a specific
class. It is currently composed of a set of about 25 classes having about 200
public functions. The classes are either representations of a node of the scene
tree (such as Robot, LED, etc.) or either utility classes (such as Motion,
ImageRef, etc.). A complete description of these functions can be found in the
reference guide while the instructions about the common way to program a C++
controller can be found in the .

### C++ Compiler Installation

Please refer to the instructions for the C Compiler installation `here`.

### Source Code of the C++ API

The source code of the C++ API is available in the Webots release. You may be
interested in looking through the directory containing the header files
("include/controllers/cpp") in order to get the precise definition of every
classes and functions although the reference guide offers a clean description of
the public functions. This directory is automatically included when the C++
controller is compiled.

For users who want to use a third-party development environment, it is useful to
know that the shared library ("CppController.dll, libCppController.so", or
"libCppController.dylib") is located in the "lib" subdirectory of your Webots
directory. This directory is automatically included when the C++ controller is
linked.

For advanced users who want to modify the C++ API, the C++ sources and the
Makefile are located in the "resources/languages/cpp" directory.

## Using Java

### Introduction

The Java API has been generated from the C++ API by using SWIG. That implies
that their class hierarchy, their class names and their function names are
almost identical. The Java API is currently composed of a set of about 25
classes having about 200 public functions located in the package called
*com.cyberbotics.webots.controller*. The classes are either representations of a
node of the scene tree (such as Robot, LED, etc.) or either utility classes
(such as Motion, ImageRef, etc.). A complete description of these functions can
be found in the reference guide while the instructions about the common way to
program a Java controller can be found in the .

### Java and Java Compiler Installation

In order to develop and run Java controllers for Webots it is necessary to have
the Java Development Kit (JDK) version 1.7.

#### Installation Instructions

The Java Development Kit (JDK) can be downloaded for free from the `Sun
Developer Network`. Make sure you choose the most recent release and the
Standard Edition (SE) of the JDK 7. For Windows, make also sure you have
selected the 64 bit version since webots is incompatible with the 32 bit
version. Then follow the installation instructions attending the package.

The `java` command is the Java Virtual Machine (JVM); it is used for executing
Java controllers in Webots. The `javac` command is the Java compiler; it is used
for compiling Java controllers in Webots text editor.

These commands should be accessible from a terminal. If it is not the case, this
can be done by modifying your *PATH* environment variable.

On Mac the JDK installer should do this automatically.

On Linux, you can set the *PATH* by adding this line to your "~/.bashrc" or
equivalent file.


```
$ export PATH=/usr/lib/jvm/java-XXXXXX/bin:$PATH
```

Where *java-XXXXXX* should correspond to the actual name of the installed JDK
package.

On Windows, the *PATH* variable must be set using the `Environment Variables`
dialog.

On Windows 7 and 8, this dialog can be opened like this: Choose `Start,
Settings, Control Panel, System and Security, System` and open `Advanced system
settings`. Select the `Advanced` tab and click on the `Environment Variables`
button.

In the dialog, in the `User variables for ...` section, look for a variable
named *PATH*. Add the "bin" path of the installed SDK to the right end of *PATH*
variables. If the *PATH* variable does not exist you should create it. A typical
value for *PATH* is:


```
C:\Program Files\Java\jdk-XXXXXXX\bin
```

Where *jdk-XXXXXX* stands for the actual name of the installed JDK package.

Then, you need to restart Webots so that the change is taken into account.

Note that the *PATH* can also be set globally for all users. On Linux this can
be achieved by adding it in the "/etc/profile" file. On Windows this can be
achieved by adding it to the *Path* variable in the `System variables` part of
the `Environment Variables` dialog.

#### Linux and OpenJDK Instructions

In alternative to Oracle JDK, on most popular Linux distribution is also
possible to directly install the open-source JDK from the system package
manager. Detailed information can be found on the `OpenJDK website`.

#### Troubleshooting the Java installation

If a Java controller fails to execute or compile, check that the `java`,
respectively the `javac` commands are reachable. You can verify this easily by
opening a Terminal (Linux and Mac OS X) or a Command Prompt (Windows) and typing
`java` or `javac`. If these commands are not reachable from the Terminal (or
Command Prompt) they will not be reachable by Webots. In this case check that
the JDK is installed and that your *PATH* variable is defined correctly as
explained above.

If you run into an error message that looks approximately like this: `Native
code library failed to load. See the chapter on Dynamic Linking Problems in the
SWIG Java documentation for help. java.lang.UnsatisfiedLinkError:
libJavaController.jnilib: no suitable image found.` this is due to a
32-bit/64-bit incompatibility between Java Virtual Machine (JVM) and Webots. On
Mac OS X this problem should disappear after you upgrade to a recent version of
Webots (6.3.0 or newer). On Windows, Webots is only compatible with 64-bit
versions of Java. On Linux (and Mac OS X) you should be able to solve this
problem by replacing the default "java" command string by "java -d32" or "java
-d64" in the dialog `Tools > Preferences > General > Java command`.

### Link with external jar files

When a Java controller is either compiled or executed, respectively the `java`
and the `javac` commands are executed with the `-classpath` option. This option
is filled internally with the location of the controller library, the location
of the current controller directory, and the content of the *CLASSPATH*
environment variable. In order to include third-party jar files, you should
define (or modify) this environment variable before running Webots (see the
previous section in order to know how to set an environment variable). Under
windows, the CLASSPATH seems like this,


```
$ set CLASSPATH=C:\Program Files\java\jdk\bin;relative\mylib.jar
```

while under Linux and Mac OS X, it seems like this:


```
$ export CLASSPATH=/usr/lib/jvm/java/bin:relative/mylib.jar
```

### Source Code of the Java API

The source code of the Java API is available in the Webots release. You may be
interested in looking through the directory containing the Java files
("resources/languages/java/SWIG_generated_files") in order to get the precise
definition of every classes and functions although these files have been
generated by SWIG and are difficult to read.

For users who want to use a third-party development environment, it can be
useful to know that the package of the Java API ("Controller.jar") is located in
the "lib" directory.

Advanced users may want to modify the Java API. They will need to modify the
SWIG script (controller.i), the java sources and the Makefile located in the
"resources/languages/java" directory.

## Using Python

### Introduction

The Python API has been generated from the C++ API by using SWIG. That implies
that their class hierarchy, their class names and their function names are
almost identical. The Python API is currently composed of a set of about 25
classes having about 200 public functions located in the module called
*controller*. The classes are either representations of a node of the scene tree
(such as Robot, LED, etc.) or either utility classes (such as Motion, ImageRef,
etc.). A complete description of these functions can be found in the reference
guide while the instructions about the common way to program a Python controller
can be found in .

### Python Installation

#### Version

The Python API of Webots is built with Python 2.7. Python 2.7 or earlier
versions are therefore recommended although more recent versions can work
without guarantee. Python 3 is not supported.

#### Mac OS X and Linux Instructions

Most of the Linux distribution have Python 2.7 already installed. Mac OS X also
has Python installed by default. To check the current version of Python
installed on your system, you can type in a terminal:


```
$ python --version
```

Webots will start Python using the `python2.7` command line. To check if this
command line is installed on your computer, you can type in a terminal:


```
$ python2.7 --version
```

More information is available from the `Python official web site`.

#### Windows Instructions

Webots comes with Python 2.7 64-bit pre-installed in the "msys64" folder.

### Source Code of the Python API

For advanced users who want to modify the Python API, the SWIG script
("controller.i"), and the Makefile are located in the
"resources/languages/python" directory while the generated library is located in
the "lib".

## Using MATLAB

### Introduction to 

`MATLAB` is a numerical computing environment and an interpreted programming
language. `MATLAB` allows easy matrix manipulation, plotting of functions and
data, implementation of algorithms and creation of user interfaces. You can get
more information on the official `MathWorks` web site. `MATLAB` is widely used
in robotics in particular for its *Image Processing, Neural Networks* and
*Genetics Algorithms* toolboxes. Webots allows to directly use `MATLAB` scripts
as robot controller programs for your simulations. Using the `MATLAB` interface,
it becomes easy to visualize controller or supervisor data, for example,
processed images, sensor readings, the performance of an optimization algorithm,
etc., while the simulation is running. In addition, it becomes possible to reuse
your existing `MATLAB` code directly in Webots.

### How to run the Examples?

If `MATLAB` is already installed, you can directly launch one of the `MATLAB`
examples. For doing that, start Webots and open the world file
"WEBOTS_MODULES_PATH/projects/languages/matlab/worlds/e-puck_matlab.wbt" or the
world file
"WEBOTS_MODULES_PATH/projects/robots/aldebaran/worlds/nao2_matlab.wbt" in your
Webots installation directory. Webots automatically starts `MATLAB` when it
detects an m-file in a controller directory. Note that the m-file must be named
after its directory in order to be identified as a controller file by Webots.
So, for example, if the directory is named "my_controller", then the controller
m-file must be named "my_controller/my_controller.m".

No special initialization code is necessary in the controller m-file. In fact
Webots calls an intermediate "launcher.m" file that sets up the Webots
controller environment and then calls the controller m-file. In particular the
"launcher.m" file loads the library for communicating with Webots and adds the
path to API m-files. The `MATLAB` API m-files are located in the "lib/matlab"
directory of Webots distribution. These are readable source files; please report
any problem, or possible improvement about these files.

In order to use `MATLAB` controllers in Webots, the `MATLAB` software must be
installed (`The MathWorks` license required).

Webots must be able to access the "matlab" executable (usually a script) in
order to run controller m-files. Webots looks for the *matlab* executable in
every directory of your *PATH* (or *Path* on Windows) environment variable. Note
that this is similar to calling `matlab` from a terminal (or *Command Prompt* on
Windows), therefore, if `MATLAB` can be started from a terminal then it can also
be started from Webots.

On Windows, the `MATLAB` installer will normally add `MATLAB`'s bin directories
to your *Path* environment variable, so usually Webots will be able to locate
`MATLAB` after a standard installation. However, in case it does not work,
please make sure that your *Path* contains this directory (or something slightly
different, according to your `MATLAB` version): `Path=C:\Program
Files\MATLAB\R2009b\bin`

On Linux, the `MATLAB` installer does normally suggest to add a symlink to the
"matlab" startup script in the "/usr/local/bin" directory. This is a good option
to make "matlab" globally accessible. Otherwise you can create the link at
anytime afterwards with this shell command (please change according to your
actual `MATLAB` installation directory and version): `$ sudo ln -s
/usr/local/MATLAB/R2014a/bin/matlab /usr/local/bin/matlab` Similarly, on Mac OS
X, if Webots is unable to find the "matlab" startup script then you should add a
symlink in "/usr/bin": `$ sudo ln -s /Applications/MATLAB_R2014a.app/bin/matlab
/usr/bin/matlab`

### Display information to Webots console

On Linux and Mac OS X, the Matlab output is redirected as is to the Webots
console. This means you can use all the Matlab display features (`disp()`,
`display()`, omitting the semicolon character at the end of a statement, etc.).

On Windows, the Matlab output is not redirected to the Webots console. The
`wb_console_print(text, stream)` function should be used to display some text in
the Webots console. The second argument (`stream`) can be either `WB_STDOUT` or
`WB_STDERR` depending on which stream you would like to write.

In order to create a cross-platform controller, it is recommended to use the
`wb_console_print(text, stream)` on every OS.

### Compatibility Issues

We recommend to use the latest Matlab version on an up-to-date operating system.

Note that 64-bit versions of Webots are not compatible with 32-bit versions of
`MATLAB`. Webots comes only in 64-bit flavour and therefore it can only inter-
operate with a 64 bit version of `MATLAB`.

On some platform the `MATLAB` interface needs `perl` and `gcc` to be installed
separately. These tools are required because `MATLAB`'s `loadlibrary()` function
will need to recompile Webots header files on the fly. According to `MATLAB`'s
documentation this will be the case on 64-bit systems, and hence we advice
64-bit Webots users (on Linux) to make sure that these packages are installed on
their systems.

On some Mac OS X systems the `MATLAB` interface will work only if you install
the Xcode development environment, because `gcc` is required. An error message
like this one, is a symptom of the above described problem: `error using ==>
calllib Method was not found.  error in ==> launcher at 66
calllib('libController','wb_robot_init');`

## Using ROS

### What is ROS?

`ROS` (Robot Operating System) is a framework for robot software development,
providing operating system-like functionality on top of a heterogenous computer
cluster. ROS was originally developed in 2007 by the Stanford Artificial
Intelligence Laboratory. As of 2008, development continues primarily at `Willow
Garage`.

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
"[robot_unique_name]/[device_name]/[service/topic_name]"

"[robot_unique_name]": in order to avoid any misunderstanding between different
instances of the same robot, the name of the robot is followed by the ID of the
process and the IP address of the computer.

"[device_name]": since the same function can refer to different devices, this
field show you which device it refers to.

"[service/topic_name]": this field is equal or really close to the Webots
function it corresponds. For topics, it is followed by the sampling period. For
services, it is also the name of the corresponding srv file.

#### Using the Standard Controller

The controller is pre-compiled and you shouldn't edit it. All you have to do is
to load it on your robot; you will find it in the default list of controller. In
order to use it, you will have to build a ROS node that will communicates with
the robot using the different services available. Good examples of such ROS node
can be found inside Webots at
"WEBOTS_MODULES_PATH/projects/languages/ros/webots_ros". In this folder you will
find useful instructions to help you.

#### Custom Controller

The standard controller has been developed in order to work on every robot and
for general purpose. Sometimes, you may not be able to do what you want with
this controller or it would be too complicated. In this case, you can build your
own custom controller and ROS node.

It is possible to implement such a ROS node in C++ using the "roscpp" library.
However, in this case, you need to setup a build configuration to handle both
the "catkin_make" from ROS and the "Makefile" from Webots to have the resulting
binary linked both against the Webots "libController" and the "roscpp" library.
An example of such an implementation is included in the Webots distribution (see
below).

This controller can also be implemented in Python by importing both ROS
libraries (roslib, rospy) and Webots libraries (controller) in a Webots robot or
supervisor controller.

#### Using the Custom Controller

A sample C++ ROS node running as a Webots controller is provided in the Webots
distribution for Linux. It is located in the Webots
"WEBOTS_MODULES_PATH/projects/languages/ros/custom" folder and contains a world
file named "joystick.wbt" and a controller named "joystick" which allows the
user to drive a simulated robot using a joystick through the ROS joy node. This
controller is a very simple example of a ROS node running as a Webots
controller. It could be used as a starting point to develop more complex
interfaces between Webots and ROS. The controller directory includes all the
"Makefile" machinery to call the build tools used by ROS and Webots to produce
the controller binary. The "ros" folder also includes a "README.txt" file with
detailed installation and usage instructions.

## Interfacing Webots to third party software with TCP/IP

### Overview

Webots offers programming APIs for following languages: C/C++, Java, Python and
`MATLAB`. It is also possible to interface Webots with other programming
languages of software packages, such as `Lisp`, `LabView`, etc. Such an
interface can be implemented through a TCP/IP protocol that you can define
yourself. Webots comes with an example of interfacing a simulated Khepera robot
via TCP/IP to any third party program able to read from and write to a TCP/IP
connection. This example world is called "khepera_tcpip.wbt", and can be found
in the "WEBOTS_MODULES_PATH/projects/robots/khepera/khepera1/worlds" directory
of Webots. The simulated Khepera robot is controlled by the "tcpip" controller
which is in the "controllers" directory of the same project. This small C
controller comes with full source code in "tcpip.c", so that you can modify it
to suit your needs. A client example is provided in "client.c". This client may
be used as a model to write a similar client using the programming language of
your third party software. This has already been implemented in `Lisp` and
`MATLAB` by some Webots users.

### Main advantages

There are several advantages of using such an interface. First, you can have
several simulated robots in the same world using several instances of the same
"tcpip" controller, each using a different TCP/IP port, thus allowing your third
party software to control several robots through several TCP/IP connections. To
allow the "tcpip" process to open a different port depending on the controlled
robot, you should give a different `name` to each robot and use the
`robot_get_name()` in the "tcpip" controller to retrieve this name and decide
which port to open for each robot.

The second advantage is that you can also control a real robot from your third
party software by simply implementing your library based on the given remote
control library. Switching to the remote control mode will redirect the
input/output to the real robot through the Inter-Process Communication (IPC). An
example of remote control is implemented for the e-puck robot in the file
"WEBOTS_MODULES_PATH/projects/robots/e-puck/worlds/e-puck.wbt" directory of
Webots.

The third advantage is that you can spread your controller programs over a
network of computers. This is especially useful if the controller programs
perform computationally expensive algorithms such as genetic algorithms or other
learning techniques.

Finally, you should set the controlled robot to synchronous or asynchronous mode
depending on whether or not you want the Webots simulator to wait for commands
from your controllers. In synchronous mode (with the `synchronization` field of
the robot equal to `TRUE`), the simulator will wait for commands from your
controllers. The controller step defined by the `robot_step` parameter of the
"tcpip" controller will be respected. In asynchronous mode (with the
`synchronization` field of the robot set to `FALSE`), the simulator will run as
fast as possible, without waiting for commands from your controllers. In the
latter case, you may want to run the simulation in real time mode so that robots
will behave like real robots controlled through an asynchronous connection.

### Limitations

The main drawback of TCP/IP interfacing is that if your robot has a camera
device, the protocol must send the images to the controller via TCP/IP, which
might be network intensive. Hence it is recommended to have a high speed
network, or use small resolution camera images, or compress the image data
before sending it to the controller. This overhead is negligible if you use a
low resolution camera such as the Khepera K213 (see example
"WEBOTS_MODULES_PATH/projects/robots/khepera/khepera1/worlds/khepera_k213.wbt").

