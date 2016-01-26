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

