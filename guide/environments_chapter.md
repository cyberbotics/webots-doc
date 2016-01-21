# Development Environments

This chapter indicates how to use the built-in development environment or third-
party environments for developing Webots controllers.

## Webots Built-in Editor

Webots source code editor is a multi-tab text editor specially adapted for
developing Webots controllers. It is usually recommended to use this editor as
it makes the compilation straightforward. The editor features syntax
highlighting for Webots supported language (C/C++, Java, Python and `MATLAB`)
and auto-completion for Webots C API.

![Webots Text Editor](png/text_editor.png)
**Webots Text Editor**

### Compiling with the Source Code Editor

The Source Code Editor can be used to compile C/C++ or Java source files into
binary executable or bytecode (Java) files that can be executed in a simulation.
The compilation output is printed to Webots console; errors and warnings appear
in red. If you double-click an error message, Webots will highlight the
corresponding source line in the editor.

Note that, for compiling source code it is necessary to have the appropriate
development tools installed. You will find information on the development tools
`here`.

In the following, the possible compilation actions are listed. Some of them are
only accessible in the `Build` menu, whereas `Build` and `Clean` actions have a
shortcut in the Text Editor toolbar.

Builds the whole project by invoking `make` in the selected file's directory.
With C/C++, the `Build` button compiles and links the whole project into an
executable file. C/C++ source file dependencies are automatically generated and
updated when necessary. With Java, the `Build` button compiles the whole project
into bytecode (.class files).

The `Clean` button invokes `make clean` to delete the intermediate compilation
files in the current file's directory. The source files remain untouched.

The `Make JAR file` menu item rebuilds the whole project and packs all the
.class in a ".jar". This is a convenience function that can be used to pack a
complete controller prior to uploading it to one of our online contest website.

The `Cross-compile` menu item allows to cross-compile the current text editor's
file. Note that a specific Makefile is required in the controller's directory
for performing this operation. For an e-puck robot, this Makefile must be named
"Makefile.e-puck".

The `Cross-compilation clean` menu item allows you to clean the cross-
compilation files. Note that a specific Makefile is required in the controller's
directory for performing this operation. For an e-puck robot, this Makefile must
be named "Makefile.e-puck".

## The standard File Hierarchy of a Project

Some rules have to be followed in order to create a project which can be used by
Webots. This section describes the file hierarchy of a simple project.

### The Root Directory of a Project

The root directory of a project contains at least a directory called "worlds"
containing a single world file. But several other directories are often
required:

### The Project Files

The project files contain information about the GUI (such as the perspective).
These files are hidden. Each world file can have one project file. If the world
file is named "myWorldFile.wbt", its project file is named
".myWorldFile.wbproj". This file is written by Webots when a world is correctly
closed. Removing it allows you to retrieve the default perspective.

### The "controllers" Directory

This directory contains the controllers. Each controller is defined in a
directory. A controller is referenced by the name of the directory. Here is an
example of the controllers directory having one simple controller written in C
which can be edited and executed.


```

controllers/
controllers/simple_controller/
controllers/simple_controller/Makefile
controllers/simple_controller/simple_controller.c
controllers/simple_controller/simple_controller[.exe]
    
```

## Compiling Controllers in a Terminal

It is possible to compile Webots controllers in a terminal instead of the built-
in editor. In this case you need to define the `WEBOTS_HOME` environment
variable and make it point to Webots installation directory. The `WEBOTS_HOME`
variable is used to locate Webots header files and libraries in the Makefiles.
Setting an environment variable depends on the platform (and shell), here are
some examples:

### Mac OS X and Linux

These examples assume that Webots is installed in the default directory. On
Linux, type this: `$ export WEBOTS_HOME=/usr/local/webots` or add this line to
your "~/.bash_profile" file. On Mac OS X, type this: `$ export
WEBOTS_HOME=/Applications/Webots` or add this line to your "~/.profile" file.

Once `WEBOTS_HOME` is defined, you should be able to compile in a terminal, with
the `make` command. Like with the editor buttons, it is possible to build the
whole project, or only a single binary file, e.g.:


```
$ make
$ make clean
$ make my_robot.class
$ make my_robot.o
```

### Windows

On Windows you must use the MSYS terminal to compile the controllers. MSYS is a
UNIX-like terminal that can be used to invoke MinGW commands. It can be
downloaded from `http://sourceforge.net`. You will also need to add the "bin"
directory of MinGW to your *PATH* environment variable. MinGW is located in the
"mingw" subdirectory of Webots distribution. When set correctly, the environment
variable should be like this:


```
WEBOTS_HOME=C:\Program Files\Webots
PATH=C:\program Files\Webots\mingw\bin;C:\...
```

Once MSYS is installed and the environment variables are defined, you should be
able to compile controllers by invoking `mingw32-make` in the MSYS terminal,
e.g.:


```
$ mingw32-make
$ mingw32-make clean
$ mingw32-make my_robot.class
$ mingw32-make my_robot.o
```

## Using Webots Makefiles

### What are Makefiles

The compilation of Webots C/C++ and Java controllers can be configured in the
provided Makefiles. A controller's Makefile is a configuration file used by the
`make` utility and that optionally specifies a list of source files and how they
will be compiled and linked to create the executable program.

Note that Python and `MATLAB` are interpreted languages and therefore they don't
need Makefiles. So if you are using any of these programming languages or Visual
C++ then you can ignore this section.

When using C/C++ or Java, the presence of a Makefile in the controller directory
is necessary. If the Makefile is missing Webots will automatically propose to
create one. This Makefile can be modified with a text editor; its purpose is to
define project specific variables and to include the global "Makefile.include"
file. The global "Makefile.include" file is stored in "WEBOTS_HOME/resources/"
directory; it contains the effective build rules and may vary with the Webots
version. Note that Webots Makefiles are platform and language independent.

### Controller with Several Source Files (C/C++)

If a controller requires several C/C++ source files they need to be specified in
the Makefile. The name of each source file must be listed, using one of these
variables:

Every source file specified using these variables, will be added to the
controller build. In addition dependency files will be automatically generated
by the `make` command in order to minimize the build. Note that these variables
should not be used in any language other than C or C++.

For example, if a controller has several ".c" source files, then this can be
specified like this in the controller's Makefile: `C_SOURCES = my_controller.c
my_second_file.c my_third_file.c` If a project has several ".cpp" source files,
then this can be specified like this: `CXX_SOURCES = my_controller.cpp
my_second_file.cpp my_third_file.cc` Important: the build rules require that one
of the source files in the list must correspond to the controller name (i.e.
controller directory name), e.g. if the controller directory is "my_controller"
then the list must contain either "my_controller.c, my_controller.cpp" or
"my_controller.cc" accordingly.

### Using the Compiler and Linker Flags (C/C++)

These two variables can be used to pass flags to the gcc compiler or linker.

#### Adding an External Library (C/C++)

Webots C/C++ controllers are regular binary executable files that can easily be
compiled and linked with external libraries. To add an external library it is
only necessary to specify the path to the header files, and the path and name of
the library in the controller's Makefile. For example the `-I`*dir* flag can be
used to add a directory to search for include files. The LIBRARIES variable can
be used to pass flags to the linker. For example the `-L`*dir* flag can be used
to add a directory to search for static or dynamic libraries, and the `-l` flag
can be used to specify the name of a library that needs to be linked with the
controller.

For example, let's assume that you would like to add an external library called
*XYZLib*. And let's assume that the library's header files and ".dll" file are
located like this (Windows): `C:\Users\YourName\XYZLib\include\XYZLib.h
C:\Users\YourName\XYZLib\lib\XYZLib.dll` Then here is how this should be
specified in the Makefile: `INCLUDE = -I"C:\Users\YourName\XYZLib\include"
LIBRARIES = -L"C:\Users\YourName\XYZLib\lib" -lXYZLib` The first line tells gcc
where to look for the *#includeltXYZLib.hgt* file. The second line tells gcc to
link the executable controller with the "XYZLib.dll" and where that ".dll" can
be found. Note that this would be similar on Linux and Mac OS X, you would just
need to use UNIX-compatible paths instead. If more external libraries are
required, it is always possible to use additional `-I, -L` and `-l` flags. For
more information on these flags, please refer to the `gcc` man page.

#### Using Webots C API in a C++ Controller

Normally, C++ controllers use Webots C++ API. The C++ API is a set of C++
classes provided by C++ header files, e.g. `#include ltwebots/Robot.hppgt`. If
you prefer, C++ controllers can use Webots C API instead. The C API is a set of
C functions starting with the `wb` prefix and provided by C header files, e.g.
`#include ltwebots/robot.hgt`. To use the C API in a C++ controller you need to
add this line in your controller Makefile: `USE_C_API = true`

#### Adding Debug Information

If you need to debug your controller, you need to recompile it with the `debug`
target from a terminal: `make debug` This will instruct gcc to add debugging
information so that the executable can be debugged using gcc.

## Debugging C/C++ Controllers

### Controller processes

In the Webots environment, the Webots application and each robot C/C++
controller are executed in distinct operating system processes. For example,
when the "soccer.wbt" world is executed, there is a total of eight processes in
memory; one for Webots, six for the six player robots, and one for the
supervisor. To debug a C/C++ controller with Visual C++, please see `here.`

When a controller process performs an illegal instruction, it is terminated by
the operating system while the Webots process and the other controller processes
remain active. Although Webots is still active, the simulation blocks because it
waits for data from the terminated controller. So if you come across a situation
where your simulation stops unexpectedly, but the Webots GUI is still
responsive, this usually indicates the crash of a controller. This can easily be
confirmed by listing the active processes at this moment: For example on Linux,
type:


```
$ ps -e
...
12751 pts/1    00:00:16 webots
13294 pts/1    00:00:00 soccer_player
13296 pts/1    00:00:00 soccer_player
13297 pts/1    00:00:00 soccer_player
13298 pts/1    00:00:00 soccer_player
13299 pts/1    00:00:00 soccer_player
13300 pts/1    00:00:00 soccer_player
13301 pts/1    00:00:00 soccer_supervisor ltdefunctgt
...
```

On Mac OS X, use rather `ps -x` and on Windows use the *Task Manager* for this.
If one of your robot controllers is missing in the list (or appearing as
*ltdefunctgt*) this confirms that it has crashed and therefore blocked the
simulation. In this example the "soccer_supervisor" has crashed. Note that the
crash of a controller is almost certainly caused by an error in the controller
code, because an error in Webots would have caused Webots to crash. Fortunately,
the GNU debugger (`gdb`) can usually help finding the reason of the crash. The
following example assumes that there is a problem with the "soccer_supervisor"
controller and indicates how to proceed with the debugging.

### Using the GNU debugger with a controller

The first step is to recompile the controller code with the *-g* flag, in order
to add debugging information to the executable file. This can be achieved by
adding this line to the controller's Makefile:


```
CFLAGS = -g
```

Then you must recompile the controller, either by using the `Clean` and `Build`
buttons of the Webots text editor or directly in a terminal:


```
$ make clean
$ make
...
```

Note that, the *-g* flag should now appear in the compilation line. Once you
have recompiled the controller, hit the `Pause` and `Revert` buttons. This
pauses the simulation and reloads the freshly compiled versions of the
controller. Now find the process ID (PID) of the "soccer_supervisor" process,
using `ps -e` (Linux) or `ps -x` (Mac OS X), or using the *Task Manager*
(Windows). The PID is in the left-most column of output of `ps` as shown above.
Then open a terminal and start the debugger by typing:


```
$ gdb
...
(gdb) attach PID
...
(gdb) cont
Continuing.
```

Where PID stands for the PID of the "soccer_supervisor" process. The `attach`
command will attach the debugger to the "soccer_supervisor" process and
interrupt its execution. Then the `cont` command will instruct the debugger to
resume the execution of the process. (On Windows you will need to install the
"gdb.exe" file separately and use an MSYS console to achieve this.)

Then hit the `Run` button to start the simulation and let it run until the
controller crashes again. The controller's execution can be interrupted at any
time (Ctrl-C), in order to query variables, set up break points, etc. When the
crash occurs, `gdb` prints a diagnostic message similar to this:


```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1208314144 (LWP 16448)]
0x00cd6dd5 in _IO_str_overflow_internal () from /lib/tls/libc.so.6
```

This indicates the location of the problem. You can examine the call stack more
precisely by using the `where` command of `gdb`. For example type:


```
(gdb) where
#0 0x00cd6dd5 in _IO_str_overflow_internal() from /lib/tls/libc.so.6
#1 0x00cd596f in _IO_default_xsputn_internal() from /lib/tls/libc.so.6
#2 0x00cca9c1 in _IO_padn_internal() from /lib/tls/libc.so.6
#3 0x00cb17ea in vfprintf() from /lib/tls/libc.so.6
#4 0x00ccb9cb in vsprintf() from /lib/tls/libc.so.6
#5 0x00cb8d4b in sprintf() from /lib/tls/libc.so.6
#6 0x08048972 in run(ms=0) at soccer_supervisor.c:106
#7 0x08048b0a in main() at soccer_supervisor.c:140
```

By examining carefully the call stack you can locate the source of the error. In
this example we will assume that the `sprintf()` function is OK, because it is
in a system library. Therefore it seems that the problem is caused by an illegal
use of the `sprintf()` function in the `run()` function. The line 106 of the
source file "soccer_supervisor.c" must be examined closely. While the controller
is still in memory you can query the values of some variables in order to
understand what happened. For example, you can use the `frame` and `print`
commands:


```
(gdb) frame 6
#6  0x08048953 in run (ms=0) at soccer_supervisor.c:106
106         sprintf(time_string, "%02d:%02d", (int) (time / 60),
 (int) time % 60);
(gdb) print time_string
$1 = 0x0
```

The `frame` command instructs the debugger to select the specified stack frame,
and the `print` command prints the current value of an expression. In this
simple example we clearly see that the problem is caused by a NULL (0x0)
*time_string* argument passed to the `sprintf()` function. The next steps are
to: fix the problem, recompile the controller and revert the simulation to give
it another try. Once it works correctly you can remove the *-g* flag from the
Makefile.

## Using Visual C++ with Webots

### Introduction

Microsoft Visual C++ is an integrated development environment (IDE) for C/C++
available on the Windows platform. On Windows, Visual C++ is a possible
alternative to using Webots built-in gcc (MinGW) compiler. Visual C++ can be
used to develop controllers using Webots C or C++ API. The developer must choose
one of these two APIs as they cannot be used together in controller code. The C
API is composed of ".h" files that contains flat C functions that can be used in
C or C++ controllers. The C++ API is composed of ".hpp" files that contain C++
classes and methods that can be used in C++ controllers only.

Two Visual C++ projects examples are included in Webots distribution:
"WEBOTS_MODULES_PATH\projects\robots\khr-2hv\controllers\khr2\khr2.vcproj" and
"WEBOTS_MODULES_PATH\projects\robots\khr-
2hv\plugins\physics\khr2\physics.vcproj". However in principle any C or C++
controller from Webots distribution can be turned into a Visual C++ project.

### Configuration

When creating a Webots controller with Visual C++, it is necessary to specify
the path to Webots ".h" and/or ".hpp" files. It is also necessary to configure
the linker to use the "Controller.lib" import library from Webots distribution.
The "Controller.lib" files is needed to link with the "Controller.dll" file that
must be used by the controller in order to communicate with Webots.

The following procedure (Visual C++ 2008 Express) explains how to create a
Visual C++ controller for Webots. Note that the resulting ".exe" file must be
launched by Webots; it cannot be run from Visual C++.

## Starting Webots Remotely (ssh)

Webots can be started on a remote computer, by using `ssh` (or a similar)
command. However, Webots will work only if it can get a X11 connection to a
X-server running locally (on the same computer). It is currently not possible to
redirect Webots graphical output to another computer.

### Using the ssh command

Here is the usual way to start from computer A, a Webots instance that will run
on computer B: `$ ssh myname@computerB.org $ export DISPLAY=:0.0 $ webots
--mode=fast --stdout --stderr myworld.wbt` The first line logs onto computer B.
The 2nd line sets the DISPLAY variable to the display 0 (and screen 0) of
computer B. This will indicate to all X11 applications (including Webots) that
they needs to connect to the X-server running on the local computer: computer B
in this case. This step is necessary because the DISPLAY variable is usually not
set in an `ssh` session.

The last line starts Webots: the *--mode=fast* option enables the *Fast*
simulation mode, which is available only with Webots PRO. The *--mode=fast*
option makes the simulation run as fast as possible, without graphical
rendering, which is fine because the graphical output won't be visible anyway
from computer A. Options *--stdout* and *--stderr* are used to redirect Webots'
output to the standard streams instead of Webots console, otherwise the output
would not be visible on computer A.

At this point, Webots will start only if a X-server with proper authorizations
is running on computer B. To ensure that this is the case, the simplest solution
is to have an open login session on computer B, i.e., to have logged in using
the login screen of computer B, and not having logged out. Unless configured
differently, the `ssh` login and the screen login session must belong to the
same user, otherwise the X-server will reject the connection. Note that the
`xhost +` command can be used to grant access to the X-server to another user.
For security reasons, the screen of the open session on computer B can be locked
(e.g. with a screen-saver): this won't affect the running X-server.

### Terminating the ssh session

A little problem with the above approach is that closing the `ssh` session will
kill the remote jobs, including Webots. Fortunately it is easy to overcome this
problem by starting the Webots as a background job and redirecting its output to
a file: `$ ssh myname@computerB.org $ export DISPLAY=:0.0 $ webots --mode=fast
--stdout --stderr myworld.wbt ampgt out.txt amp $ exit` The ampgt sign redirects
into a text file the output that would otherwise appear in the `ssh` terminal.
The amp sign starts Webots as a background job: so the user can safely exit the
`ssh` session, while Webots keeps running.

In this case the decision to terminate the job is usually made in the Supervisor
code according to simulation specific criteria. The
`wb_supervisor_simulation_quit()` function can be used to automatically
terminate Webots when the job is over.

## Transfer to your own robot

In mobile robot simulation, it is often useful to transfer the results onto real
mobile robots. Webots was designed with this transfer capability in mind. The
simulation is as realistic as possible, and the programming interface can be
ported or interfaced to existing, real robots. Webots already comprises transfer
systems for a number of existing robots including `e-puck`, `DARwIn-OP`,
`Khepera` and `Hemisson`. This section explains how to develop your own transfer
system to your own mobile robot.

Since the simulation is only an approximation of the physics of the real robot,
some tuning is always necessary when developing a transfer mechanism for a real
robot. This tuning will affect the simulated model so that it better matches the
behavior of the real robot.

### Remote control

#### Overview

Often, the easiest way to transfer your control program to a real robot is to
develop a remote control system. In this case, your control program runs on the
computer, but instead of sending commands to and reading sensor data from the
simulated robot, it sends commands to and reads sensor data from the real robot.
Developing such a remote control system can be achieved in a very simple way by
writing your own implementation of the Webots API functions as a small library.
For example, you will probably have to implement the
`wb_differential_wheels_set_speed()` function to send a specific command to the
real robot with the wheel speeds as an argument. This command can be sent to the
real robot via the serial port of the PC, or any other PC-robot interface you
have. You will probably need to make some unit conversions, since your robot may
not use the same units of measurement as the ones used in Webots. The same
applies for reading sensor values from the real robot.

#### Developing a remote control plugin

Webots already provides some facilities to implement a remote control library
and in particular it is possible to develop it as a controller plugin. Once set
in the corresponding field of the Robot node, this remote control plugin will be
executed automatically when running the controller. Implementation details are
described in .

#### Special functions

The `wb_robot_init()` function must be the first called function. It performs
the controller library's initialization.

The `wb_robot_step()` function should be called repeatedly (typically in an
infinite loop). It requests that the simulator performs a simulation step of ms
milliseconds; that is, to advance the simulation by this amount of time.

The `wb_robot_cleanup()` function should be called at the end of a program in
order to leave the controller cleanly.

#### Running your real robot

Once linked with your own remote control plugin, you can control your real robot
by running the simulation in Webots. It might be useful to also add a robot
window plugin (see ) to graphically display specific sensor values, motor
commands or a stop button.

Such a remote control system is designed to be implemented in C/C++ as explained
in ; however, it can also be implemented other programming languages creating a
wrapper.

### Cross-compilation

#### Overview

Developing a cross-compilation system will allow you to recompile your Webots
controller for the embedded processor of your own real robot. Hence, the source
code you wrote for the Webots simulation will be executed on the real robot
itself, and there is no need to have a permanent PC connection with the robot as
with the remote control system. This is only possible if the processor on your
robot can be programmed respectively in C, C++, Java or Python. It is not
possible for a processor that can be programmed only in assembler or another
specific language. Webots includes the source code of such a cross-compilation
system for the e-puck and the Hemisson robot. Samples are located in the
"WEBOTS_MODULES_PATH/projects/robots" directory.

#### Developing a custom library

Unlike the remote control system, the cross-compilation system requires that the
source code of your Webots controller be recompiled using the cross-compilation
tools specific to your own robot. You will also need to rewrite the Webots
include files to be specific to your own robot. In simple cases, you can just
rewrite the Webots include files you need, as in the "hemisson" example. In more
complex cases, you will also need to write some C source files to be used as a
replacement for the Webots "Controller" library, but running on the real robot.
You should then recompile your Webots controller with your robot cross-
compilation system and link it with your robot library. The resulting file
should be uploaded onto the real robot for local execution.

#### Examples

Webots support cross-compilation for several existing commercial robots. For the
`e-puck` robot, this system is fully integrated in Webots and needs no
modification in the code. For the `Hemisson` robot, this system needs a few
include files to replace the Webots API include files. For the `Khepera` robot,
a specific C library is used in addition to specific include files.

### Interpreted language

In some cases, it may be better to implement an interpreted language system.
This is useful if your real robot already uses an interpreted language, like
Basic or a graph based control language. In this case, the transfer is very easy
since you can directly transfer the code of your program that will be
interpreted to the real robot. The most difficult part may be to develop a
language interpreter in C or Java to be used by your Webots controller for
controlling the simulated robot. Such an interpreted language system was
developed for the `Hemisson` robot with the `BotStudio` system.

