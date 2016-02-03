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

1. xyz_controller[.exe] (a binary executable)
2. xyz_controller.class (a Java bytecode class)
3. xyz_controller.jar (a Java .jar file)
4. xyz_controller.bsg (a Webots/BotStudio file)
5. xyz_controller.py (a Python script)
6. xyz_controller.m (a `MATLAB` script)

The first file that is found will be executed by Webots using the required
language interpreter (java, python, matlab). So the priority is defined by the
file extension, e.g. it won't be possible to execute "xyz_controller.m" if a
file named "xyz_controller.py" is also present in the same controller directory.
In the case that none of the above filenames exist or if the required language
interpreter is not found, an error message will be issued and Webots will start
the "void" controller instead.

