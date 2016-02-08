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
"WEBOTS\_MODULES\_PATH\projects\robots\khr-2hv\controllers\khr2\khr2.vcproj" and
"WEBOTS\_MODULES\_PATH\projects\robots\khr-
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

