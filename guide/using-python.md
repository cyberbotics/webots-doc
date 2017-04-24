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

#### Mac OS X and Linux Instructions

Most of the Linux distributions have Python 2.7 already installed. Mac OS X also
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

The sample simulation `WEBOTS_HOME/projects/web/visual_tracking` use the Python [OpenCV](http://opencv.org/) library.
So this library has to be installed on the system in order to correctly run the simulation.

#### Linux

On Ubuntu 16.04, use the `pip` command to install OpenCV:
```
sudo pip install opencv-python
```

On older Ubuntu versions, it can be installed using the the APT package `python-opencv` for example by typing the following command in a terminal:
```
sudo apt-get install python-opencv
```

#### macOS

Since macOS El Capitan, open a Terminal and type:

```
pip install opencv-python --user
```

On older macOS versions, type:

```
pip install opencv-python
```


#### Windows

Open the DOS console (CMD.EXE) and type:
```
PYTHON_PATH\Scripts\pip.exe install opencv-python
```
where `PYTHON_PATH` is the path to the Python installation directory, for example `C:\Python27`.
