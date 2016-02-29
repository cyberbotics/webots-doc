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
can be found in [this chapter](#programming-fundamentals).

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

More information is available from the [Python official web
site](http://www.python.org/).

#### Windows Instructions

Webots comes with Python 2.7 64-bit pre-installed in the "msys64" folder.

### Source Code of the Python API

For advanced users who want to modify the Python API, the SWIG script
("controller.i"), and the Makefile are located in the
"resources/languages/python" directory while the generated library is located in
the "lib".

