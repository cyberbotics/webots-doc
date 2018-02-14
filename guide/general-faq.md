## General FAQ

### What are the differences between Webots PRO, Webots EDU and Webots MOD?

Webots PRO provides a fully featured version of Webots intended for robotics research.
Webots EDU provides a special version of Webots well suited for education.
Webots MOD provides components tailored for specific uses of Webots, they include different models of robots with different programming interfaces.
The differences between Webots PRO, EDU and MOD are explained [here](http://www.cyberbotics.com/webots/).

### How can I report a bug in Webots?

If you can still start Webots, please report the bug by using Webots menu: `Help / Bug report...`.

If Webots cannot start any more, please report the bug here: [http://www.cyberbotics.com/bug](http://www.cyberbotics.com/bug).
Please include a precise description of the problem, the sequence of actions necessary to reproduce the problem.
Do also attach the world file and the controller programs necessary to reproduce it.

Before reporting a bug, please make sure that the problem is actually caused by Webots and not by your controller program.
For example, a crash of the controller process usually indicates a bug in the controller code, not in Webots.
This situation can be identified by these couple of symptoms:

1. Webots GUI is visible and responsive, but the simulation is blocked (simulation time stopped).
2. The controller process has vanished from the *Task Manager* (Windows) or is shows as *<defunct>* when using `ps -e` (Linux/Mac).

### Is it possible to use Visual C++ to compile my controllers?

Yes.
However, you will need to create your own project with all the necessary options.
You will find more detailed instructions on how to do that in [this section](using-visual-cpp-with-webots.md).
To create the import libraries (the "*.lib" files in Visual C++) from the "*.dll" files of the lib directory of Webots, please follow the instructions provided with the documentation of your compiler.
