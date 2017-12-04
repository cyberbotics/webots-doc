## Using Python

### Introduction

The Python API has been generated from the C++ API by using SWIG. This implies
that their class hierarchy, their class names and their function names are
almost identical. The Python API is currently composed of a set of about 25
classes having about 200 public functions located in the module called
*controller*. The classes are either representations of a node of the scene tree
(such as Robot, LED, etc.) or utility classes (such as Motion, ImageRef,
etc.). A complete description of these functions can be found in the reference
guide while the instructions about the common way to program a Python controller
can be found in [this chapter](programming-fundamentals.md).

### Python Installation

#### Version

The Python API of Webots supports both Python 2.7 and Python 3.6.
On Ubuntu 16.04, it also supports Python 3.5 and on Ubuntu 14.04, it also support Python 3.4.

#### macOS and Linux Instructions

Most of the Linux distributions have Python already installed. macOS also
has Python installed by default. To check the current version of Python
installed on your system, you can type in a terminal:

```sh
$ python --version
```

Webots will start Python using the standard `python` command line. As a consequence, it will execute the first `python` binary found in the current PATH. Please refer to your operating system documentation to install and/or default to a different version of Python on the command line.

#### Windows Instructions

You should install the latest version of Python 2.7 (64 bit) or Python 3.6 (64 bit) from the official [Python website](https://www.python.org). Then, you have to modify your `PATH` environment variable to add the path to the python.exe binary which is located in the main `Python27` or `Python36` installation folder. To check this was done properly, you can open a DOS console (CMD.EXE) and type `python --version`. If it displays the Python version, then, everything is setup properly and you should be able to run the Python examples provided with Webots in the `WEBOTS_HOME/projects/languages/python/worlds/example.wbt` world file.

#### How to use another Python distribution

For advanced users and without guarantee, the Python controller library
can be recompiled to support other Python releases.

The source code is located in `WEBOTS_HOME/resources/languages/python`.
A SWIG script uses the C++ controller API to generate the Python API.

Install [SWIG](http://www.swig.org/), make sure that typing `python2.7` leads to
the expected Python installation, and recompile the Python API.

For example, on macOS, the Python Homebrew may be used by typing the following commands:

```sh
cd ${WEBOTS_HOME}
export PYTHON_VERSION=2.7
export PYTHON_PATH=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7
make clean -C resources/languages/python
make -C resources/languages/python
```

### Python Libraries

The `WEBOTS_HOME/projects/web/visual_tracking` sample simulation uses the Python [OpenCV](http://opencv.org/) and [NumPy](http://numpy.org/) packages.
So these packages have to be installed on the system in order to correctly run this simulation.
Using Python *pip*, the *NumPy* package is automatically installed with *opencv-python* package.

#### Linux

On Ubuntu 16.04, use the `pip` command to install OpenCV:
```sh
sudo apt-get install python-pip
sudo pip install opencv-python
```

On Ubuntu 14.04 OpenCV doesn't need to be installed because the Python OpenCV library is already included in the Ubuntu 14.04 tarball package.
*NumPy* can be installed with this command:
```sh
sudo apt-get install python-numpy
```

#### macOS

Open a Terminal and type:

```
pip install opencv-python --user
```

#### Windows

Open the DOS console (CMD.EXE) and type:
```
PYTHON_PATH\Scripts\pip.exe install opencv-python
```
where `PYTHON_PATH` is the path to the Python installation directory, for example `C:\Python36`.


### Use an alternative Python version

As described above, the Python libraries for Webots are precompiled with Python 2.7 and Python 3.6.
It is possible however to use another Python version by recompiling these libraries.
Such a task requires some knowledge in software installation, recompilation and Makefile.

The general idea is to walk through the following steps:

1. Install a new Python version and add the path to the new python binary in your PATH environment variable, so that you can execute `python --version` from a console with the correct version.
2. Get [SWIG](http://www.swig.org/download.html).
3. Recompile the Python wrapper located in this directory: `$WEBOTS_HOME/resources/languages/python` using its Makefile. You may check the above Makefile in `$WEBOTS_HOME/resources/languages/Makefile` to understand how to call the Python Makefile with different options.

Note: on Windows, you will need to install [MSYS2 for x86_64](http://www.msys2.org/) and run it in administrator mode to be able to modify files in `$WEBOTS_HOME`. From the MSYS2 console, you will need to install at least the following packages with the `pacman` command: `mingw-w65-x86_64_gcc` `make` and `swig`. Also, it is necessary to add `extern double hypot(double, double);` at the 3rd line of `$PYTHON_HOME\include\Python.h`.
