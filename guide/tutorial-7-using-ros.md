## Tutorial 7: Using ROS

This tutorial explains how to implement a Webots controller as a ROS node. This
process is exemplified by describing how we built the "joystick" controller
located in "WEBOTS\_MODULES\_PATH/projects/languages/ros/controllers/joystick".

> **note**:
We assume that you installed ROS groovy on your computer as explained in the
online ROS installation tutorial. As the ROS joy package is currently defined on
Linux only, you won't be able to compile this controller example on other
platforms.

### Creating a Webots project that contains a ROS package

The "joystick" controller is a Webots controller written in C++ and implemented
as a ROS node. It subscribes to the *joy/joy* topic of the "joy\_node" (see ROS
"joy" package) in order to listen to the joystick state. The relevant line in
"webots\_joystick\_node.cpp" is:

```
ros::Subscriber sub=nh.subscribe("joy", 10, joy_callback);
```

which prompts ten times per second the callback function *joycall\_back* to
transform the joystick sensed values into a robot motion command.

We now describe the actions to setup the controller directory
"WEBOTS\_MODULES\_PATH/projects/languages/ros/controllers/joystick" both on ROS
and Webots side (as provided in your Webots distribution). We are to recreate
the corresponding project based on its bare bones: the world file
"WEBOTS\_MODULES\_PATH/projects/languages/ros/worlds/joystick.wbt", the source
file
"WEBOTS\_MODULES\_PATH/projects/languages/ros/controller/catkin\_ws/src/webots\_joystick/src/webots\_joystick\_node.cpp"
and the ROS launcher file
"WEBOTS\_MODULES\_PATH/projects/languages/ros/controller/joy.launch". Note that
"joy.launch" is used in "webots\_joystick\_node.cpp" to launch the ROS node
"joy\_node" as child process:

```
  // launch the joy ROS node
      int roslaunch=fork();
      if (roslaunch==0) { // child process
        execlp("roslaunch","roslaunch","joy.launch",NULL);
        return 0;
      }
```

We will be done once we will have provided Webots with an executable file in
"WEBOTS\_MODULES\_PATH/projects/languages/ros/controllers/joystick" whose name
matches the controller directory name, i.e. "joystick" (which is also the name
specified in "joystick.wbt"). As we want this executable to be a ROS a node, we
will create and build a ROS package called "webots\_joystick" and copy the
resulting executable in
"WEBOTS\_MODULES\_PATH/projects/languages/ros/controllers/joystick".

Prior to package construction, we create and setup a *catkin* workspace from
which we will run most of the build process through the `catkin_make` command.

> **handson**:
Create a project directory called "my\_ros", with subdirectories "worlds" and
"controllers/joystick". Copy
"WEBOTS\_MODULES\_PATH/projects/languages/ros/worlds/joystick.wbt" into
"my\_ros/worlds". You can perform these actions by opening a terminal and
typing:

>     $ mkdir -p ~/my_ros/worlds
>     $ mkdir -p ~/my_ros/controllers/joystick
>     $ cp $WEBOTS_MODULES_PATH/projects/languages/ros/worlds/joystick.wbt ~/my_ros/worlds/

> Copy the file
"WEBOTS\_MODULES\_PATH/projects/languages/ros/controllers/joystick/joy.launch"
into "my\_ros/controllers/joystick":

>     $ cp $WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick/joy.launch ~/my_ros/controllers/joystick

<!-- -->

> **note**:
We will use catkin, the official ROS build system (see ROS tutorials for catkin
basics).

<!-- -->

> **handson**:
Create and init a catkin workspace. You can perform these actions through a
terminal by typing:

>     $ cd ~/my_ros/controllers/joystick
>     $ mkdir -p catkin_ws/src
>     $ cd catkin_ws/src
>     $ catkin_init_workspace

<!-- -->

> **handson**:
Install the joy package.

>     $ sudo apt-get install ros-groovy-joystick-drivers
>     $ rosdep install joy

<!-- -->

> **handson**:
Create a ROS package named "webots\_joystick" specifying dependency on "roscpp"
and "joy".

>     $ cd ~/my_ros/controllers/joystick/catkin_ws/src
>     $ catkin_create_pkg webots_joystick roscpp joy

<!-- -->

> **note**:
Calling `catkin_create_pkg` must have created the directory "webots\_joystick"
with the subdirectories "webots\_joystick/src" and "webots\_joystick/include"
plus two files: "webots\_joystick/CMakeLists.txt" and
"webots\_joystick/package.xml". The former is a CMake file that tells catkin how
to build the ROS package, the latter is a description of the package where you
can specify the package dependencies, the version number, the author name, the
maintainer name, etc.

<!-- -->

> **note**:
If you want to use the ROS command line tools (`roscd, rosls, rospack, ...`) to
navigate and get information about the created package then you need to call
`catkin_make` at the root of the catkin workspace and source the file
"devel/setup.bash":

        $ cd ~/my_ros/controllers/joystick/catkin_ws
        $ catkin_make
        $ source devel/setup.bash

> Now the output of the command `rospack find webots_joystick` should be

        ~/my_ros/controllers/joystick/catkin_ws/src/webots_joystick

    The information on package first level dependencies which are displayed after
    the `rospack depends1 webots_joystick` command should read as

        joy
        roscpp

<!-- -->

> **handson**:
Copy the original ".cpp" controller file into your package resource directory.

>     $ cd ~/my_ros/controllers/joystick/catkin_ws/src/webots_joystick/src
>     $ cp $WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick/catkin_ws/src/webots_joystick/src/webots_joystick_node.cpp .

<!-- -->

> **handson**:
In the file "webots\_joystick/CMakeLists.txt" uncomment the line

>     #add_executable(webots_joystick_node src/webots_joystick_node.cpp)

> and append the following lines

>     set(WEBOTS_HOME $ENV{WEBOTS_HOME})
>     add_definitions(-I${WEBOTS_HOME}/include/controller/cpp -I${WEBOTS_HOME}/include -Wall -I${WEBOTS_HOME}/include/controller/c -DLINUX)
>     find_library(CPP_CONTROLLER_LIBRARY CppController ${WEBOTS_HOME}/lib)
>     find_library(C_CONTROLLER_LIBRARY Controller ${WEBOTS_HOME}/lib)
>     target_link_libraries(webots_joystick_node ${catkin_LIBRARIES} ${C_CONTROLLER_LIBRARY} ${CPP_CONTROLLER_LIBRARY})

> These lines tell catkin where to find the Webots controller libraries and to
link the "webots\_joystick\_node" against them. (The comments indicate where to
paste these lines appropriately; the distributed CMakeLists.txt file shows you
the right places.)

<!-- -->

> **handson**:
Build the webots\_joystick package. Then copy the resulting ROS node executable
at the root of "controllers/joystick" and rename it appropriately.

>     $ cd ~/my_ros/controllers/joystick/catkin_ws
>     $ catkin_make
>     $ cp devel/lib/webots_joystick/webots_joystick_node ~/my_ros/controllers/joystick/joystick

<!-- -->

> **note**:
Calling `catkin_make` created the directories "catkin\_ws/build" and
"catkin\_ws/devel". You should source "catkin\_ws/devel/setup.bash" if you want
to use ROS built-in commands to manage the "webots\_joystick" package.

<!-- -->

> **handson**:
Have a look at the file
"WEBOTS\_MODULES\_PATH/projects/languages/ros/controllers/joystick/Makefile".
This file allows you to (re)compile the "joystick" controller from Webots build
editor (edit the source file in Webots build editor and hit the build button).
You may take inspiration from it when building other Webots-ROS projects.

<!-- -->

> **note**:
In case you need to configure your joystick, please refer to the ROS joy
tutorials.

### Conclusion

You should be able to run the "joystick" you just built as the original one
(open "~/my\_ros/worlds/joystick.wbt" and hit the play button). You hence
achieved a fully functional Webots controller implemented as a ROS node.
Exploring further Webots C/C++ and Python APIs will allow you to integrate
larger ROS frameworks.

