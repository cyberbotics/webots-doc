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
"WEBOTS\_HOME\projects\robots\khr-2hv\controllers\khr2\khr2.vcproj" and
"WEBOTS\_HOME\projects\robots\khr-2hv\plugins\physics\khr2\physics.vcproj".
However in principle any C or C++ controller from Webots distribution can be
turned into a Visual C++ project.

### Configuration

When creating a Webots controller with Visual C++, it is necessary to specify
the path to Webots ".h" and/or ".hpp" files. It is also necessary to configure
the linker to use the "Controller.lib" import library from Webots distribution.
The "Controller.lib" files is needed to link with the "Controller.dll" file that
must be used by the controller in order to communicate with Webots.

The following procedure (Visual C++ 2008 Express) explains how to create a
Visual C++ controller for Webots. Note that the resulting ".exe" file must be
launched by Webots; it cannot be run from Visual C++.

1. Copy a Webots project from Webots distribution to your "Documents" folder, or
create an empty project directory using Webots menu: `Wizard / New Project
Directory...` Either way, the project directory must contain the "controllers"
and "worlds" subdirectories.

2. Start Visual C++ and select: `File / New / Project...` Then choose these
settings:

        Project type: General
        Template: Empty Project
        Name: MyController (for example)
        Location: C:\Users\MyName\Documents\MyProject\controllers (for example)

    Where "MyController" is the name of a new or already existing controller
    directory, and where "Location" must indicate the "controllers" subdirectory of
    your Webots project directory.

3. Then you can add a C or C++ source file to your project: Choose either: `Project
/ Add Existing Item` or `Project / Add New Item / C++ File (.cpp)`. In the
second case you can copy the content of one of the C/C++ examples of Webots
distribution.

    Note that if you copied C code from Webots examples to Visual C++, it is highly
    recommended to change the source file extension from .c to .cpp. The reason is
    that Webots examples are written for the gcc compiler which uses a more modern
    version of the C language than Visual C++. By changing the file extension to
    .cpp you will instruct Visual C++ to compile the file in C++ mode (/TP) which is
    more tolerant with gcc code. If you don't do it, you may run into error messages
    like these:

        MyController.c(24): error C2275: 'WbDeviceTag' : illegal use of
          this type as an expression
        MyController.c(24): error C2146: syntax error : missing ';' before
          identifier 'ir0'
        ...

4. Now we can set up the project configuration for Webots. Select the `Project /
Properties` menu. In the `Property Pages`, in the `Configuration Properties`,
enter following configuration:

        C/C++ > General > Additional Include Directories:
          C:\Program Files\Webots\include\controller\c

    This will tell Visual C++ where to find Webots C API (.h files).

    By default Visual C++ places the .exe file in a "Debug" or "Release"
    subdirectory. However order to be executed by Webots, the .exe file must be
    placed directly at the root of the "MyController" directory. So in this example
    the .exe should be there: "MyProject\controllers\MyController\MyController.exe".
    Consequently the linker output file should be configured like this:

        Linker > General > Output File: $(ProjectName).exe

    Now we need to tell Visual C++ to use the "Controller.lib" import library:

        Linker > Input > Additional Dependencies:
          Controller.lib
        Linker > General > Additional Library Directories:
          C:\Program Files\Webots\msys64\mingw64\lib\

5. If you want to use the C API, you should skip step 5 and go directly to step 6.
If you want to use the C++ API follow these instructions:

    In `Property Pages`, in the `Configuration Properties`, add the path to Webots
    .hpp files:

        C/C++ > General > Additional Include Directories:
          C:\Program Files\Webots\include\controller\c
          C:\Program Files\Webots\include\controller\cpp

    Now you should have the path to both the .h and the .hpp files.

    Then you need to add Webots C++ wrappers to your project. The C++ wrappers are
    .cpp files that implement the interface between the C++ API and the C API. You
    can proceed like this:

    In Visual C++, in the `Solution Explorer`: right-mouse-click on the `Sources
    Files` folder, then select `Add / New Filter`. This should create a `NewFilter1`
    subfolder in your `Sources Files` folder. Then select the `NewFilter1` and with
    the right-mouse-button: choose the `Add / Existing Item...` menu. In the file
    dialog, go to the "C:\Program Files\Webots\resources\languages\cpp" directory,
    then select all the .cpp files (but no other file) in that directory and hit the
    `Add` button. This should add the "Accelerometer.cpp, Camera.cpp, Compass.cpp",
    etc. source files to your project.

6. Now you should be able to build your controller with the `Build / Build
MyController` menu item (or the F7 key). This should generate the
"MyProject\controllers\MyController\MyController.exe" file.

7. Now we can switch to Webots in order to test the .exe controller. Start Webots
and verify that your robot is associated with the correct controller: In the
`Scene tree`, expand the robot node and check the `controller` field. It should
be: `controller "MyController"`. Otherwise you should change it: hit the `...`
(ellipsis) button, this opens a selection dialog. In the selection dialog choose
"MyController". Then hit the `Save` button in Webots main window. Finally you
can hit the `Run` button to start the simulation. At this point the simulation
should be using your Visual C++ controller.

8. If you want to debug your controller with Visual C++ you can *attach* the
debugger to the running controller process. Proceed like this: In Webots, hit
the `Pause` button then the `Revert` button. Then, in Visual C++, use the `Debug
/ Attach to Process...` menu. In the dialog choose the `MyController.exe_webots`
process. Still in Visual C++, you can now add breakpoints and watches in the
controller code. Then, in Webots, hit the `Run` button to resume the simulation.
Now the controller should pause when it reaches one of your breakpoints.
