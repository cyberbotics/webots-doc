# Known Bugs

This chapter lists the bugs known by Cyberbotics. They are not planned to be
resolved on the short term but possible workarounds are explained.

## General bugs

### Intel GMA graphics cards

Webots should run on any fairly recent computer equipped with a nVidia or ATI
graphics card and up-to-date graphics drivers. Webots is not guaranteed to work
with Intel GMA graphics cards: it may crash or exhibit display bugs. Upgrading
to the latest versions of the Intel graphics driver may help resolve such
problems (without any guarantee). Graphics drivers from Intel may be obtained
from the `Intel download center web site`. Linux graphics drivers from Intel may
be obtained from the `Intel Linux Graphics web site`.

### Virtualization

Because it highly relies on OpenGL, Webots may not work properly in virtualized
environments (such as VMWare or VirtualBox) which often lack a good OpenGL
support. Hence, Webots may exhibit some display bugs, run very slowly or crash
in such environments.

### Collision detection

Although collision detection works well generally well, `Cylinder-Cylinder`,
`Cylinder-Capsule`, `IndexedFaceSet-IndexedFaceSet` and `IndexedFaceSet-
Cylinder` collision detection may occasionaly yield wrong contact points.
Sometimes the contact points may be slightly off the shape, therefore causing
unrealistic reaction forces to be applied to the objects. Other times there are
too few contact points, therefore causing vibration or instabilities.

### Orientation dependent friction

Although the friction model of ODE is very accurate, the true friction cone is
approximated by a linearized version which can introduce some orientation
specific artifacts. It is for example possible that an object slips more easily
on another object in some direction than in some other, even if the friction
coefficients are set to be symmetric. However, in most of the cases it is
possible to get rid of these effects by tuning correctly the friction
parameters.

## Mac OS X

### Matlab and robot plugins

The controllers and the robot plugins (e.g. the robot windows) are sharing the
same process. Generally this mechanism is working well, but some instabilities
(crashes and warnings) may occur when a robot uses a Matlab controller and a
robot window at the same time. This is due to some conflicts between the Qt
libraries used by Matlab and the one used by Webots.

## Linux

### Window refresh

It may happen that the main window of Webots is not refreshed properly and
appears blank at startup or upon resize or maximization. This is caused by a
conflict between the Compiz window manager and OpenGL. Simply disabling Compiz
should fix such a problem. This can be achieved on Ubuntu Linux from the System
menu: `Preferences > Appearance > Visual Effects > None`.

### ssh -x

There are known issues about running Webots over a `ssh -x` (x-tunneling)
connection. This problem is not specific to Webots but to most GLX (OpenGL on
the X Window system) applications that use complex OpenGL graphics. We think
this is caused by incomplete or defective implementation of the GLX support in
the graphics drivers on Linux. It may help to run the `ssh -x` tunnel across two
computers with the same graphics hardware, e.g., both nVidia or both ATI. It
also usually works to use Mesa OpenGL on both sides of the `ssh -x` tunnel,
however this solution is extremely slow.

