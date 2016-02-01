## General FAQ

### What are the differences between Webots PRO, Webots EDU and other Webots modules?

Webots PRO provides a fully featured version of Webots intended for robotics
research. Webots EDU provides a special version of Webots well suited for
education. Webots modules are components tailored for specific uses of Webots,
they include different models of robots, objects, environments, programming
interfaces, libraries, etc. Users can purchase only the modules they need
separately. The differences between Webots modules are explained
[here](http://www.cyberbotics.com/webots/).

### How can I report a bug in Webots?

If you can still start Webots, please report the bug by using Webots menu: `Help
> Bug report...`.

If Webots cannot start any more, please report the bug there:
[http://www.cyberbotics.com/bug](http://www.cyberbotics.com/bug). Please include
a precise description of the problem, the sequence of actions necessary to
reproduce the problem. Do also attach the world file and the controller programs
necessary to reproduce it.

Before reporting a bug, please make sure that the problem is actually caused by
Webots and not by your controller program. For example, a crash of the
controller process usually indicates a bug in the controller code, not in
Webots. This situation can be identified with these two symptoms:

### Is it possible to use Visual C++ to compile my controllers?

Yes. However, you will need to create your own project with all the necessary
options. You will find more detailed instructions on how to do that in . To
create the import libraries (the "*.lib" files in Visual C++) from the "*.dll"
files of the lib directory of Webots, please follow the instructions provided
with the documentation of your compiler.

