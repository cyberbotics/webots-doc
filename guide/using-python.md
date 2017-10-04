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

The Python API of Webots is built with Python 2.7. Python 2.7 or earlier
versions are therefore recommended although more recent versions can work
without guarantee. Python 3 is not supported.

#### macOS and Linux Instructions

Most of the Linux distributions have Python 2.7 already installed. macOS also
has Python installed by default. To check the current version of Python
installed on your system, you can type in a terminal:

```sh
$ python --version
```

Webots will start Python using the `python2.7` command line. To check if this
command line is installed on your computer, you can type in a terminal:

```sh
$ python2.7 --version
```

#### Windows Instructions

You should install the latest version of Python 2.7 (64 bit) from the official [Python website](https://www.python.org). Then, you have to modify your `PATH` environment variable to add the path to the python.exe binary which is located in the main `Python27` installation folder. To check this was done properly, you can open a DOS console (CMD.EXE) and type `python --version`. If it displays the Python version, then, everything is setup properly and you should be able to run the Python examples provided with Webots (in the `WEBOTS_HOME/projects/languages/python/worlds/example.wbt`)

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

#### Linux

On Ubuntu 16.04, use the `pip` command to install OpenCV:
```sh
sudo apt-get install python-pip
sudo pip install opencv-python numpy
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
PYTHON_PATH\Scripts\pip.exe install opencv-python numpy
```
where `PYTHON_PATH` is the path to the Python installation directory, for example `C:\Python27`.


### Use an alternative Python version

As described above, the Python libraries for Webots are precompiled with Python 2.7.
It is possible to use another Python version such as Python 3 or macOS brew Python,
by recompiling these libraries.
This documentation is generic and may not cover all the cases.
This task requires advanced knowledge in operating systems management.

The general idea is to complete the following tasks:

1. Install the new Python version.
2. Get [SWIG](http://www.swig.org/download.html).
3. Recompile this directory: `$WEBOTS_HOME/resources/languages/python`


#### Example: build the Webots libraries for Python 3.6 under Windows

1. Uninstall any Python installation.
2. Download and install [Python 3.6 for x86_64](https://www.python.org/downloads/):
    - Extend your system `PATH` environment variable to add the
    `C:\Users\$USER\AppData\Local\Programs\Python\Python36` directory.
    - Add `extern double hypot(double, double);` at the 3rd line of
    `C:\Users\$USER\AppData\Local\Programs\Python\Python36\include\Python.h`
3. Download, install and run [MSYS2 for x86_64](http://www.msys2.org/).
4. You should either start the MSYS2 console in administrator mode (right click on the MSYS2.exe icon and select Run as administrator) or
enable the user write rights at least for these folders:
    - `/C/Program\ Files/Webots/resources/languages/python`
    - `/C/Program\ Files/Webots/lib/python`
5. From the MSYS2 terminal, type:

```shell
# Update and install gcc and make
pacman -Syuu
pacman -S mingw-w64-x86_64-gcc make swig

# Setup and compile Webots library for Python 3.6
export PYTHON_VERSION=3.6
export PYTHON_HOME=/C/Users/$USER/AppData/Local/Programs/Python/Python36
cd /C/Program\ Files/Webots/resources/languages/python
make
```

8. Foreach Python 3.6 controller, create a `runtime.ini` file containing:

```ini
[python]
COMMAND = python
```
