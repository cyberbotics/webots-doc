## Tutorial 7: Using ROS

This tutorial explains how to implement a Webots controller as a ROS node. This
process is exemplified by describing how we built the "joystick" controller
located in "WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick".

### Creating a Webots project that contains a ROS package


The "joystick" controller is a Webots controller written in C++ and implemented as a ROS node. It subscribes to the *joy/joy*
topic of the "joy_node" (see ROS "joy" package) in order to listen to the joystick state. The relevant line in "webots_joystick_node.cpp" is:

```
ros::Subscriber sub=nh.subscribe("joy", 10, joy_callback);
```
which prompts ten times per second
the callback function *joycall_back* to transform the joystick sensed values into a robot motion command.


We now describe the actions to setup the controller directory
"WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick" both on ROS
and Webots side (as provided in your Webots distribution). We are to recreate
the corresponding project based on its bare bones: the world file
"WEBOTS_MODULES_PATH/projects/languages/ros/worlds/joystick.wbt", the source
file "WEBOTS_MODULES_PATH/projects/languages/ros/controller/catkin_ws/src/webots
_joystick/src/webots_joystick_node.cpp" and the ROS launcher file
"WEBOTS_MODULES_PATH/projects/languages/ros/controller/joy.launch". Note that
"joy.launch" is used in "webots_joystick_node.cpp" to launch the ROS node
"joy_node" as child process:


```
  // launch the joy ROS node
      int roslaunch=fork();
      if (roslaunch==0) { // child process
        execlp("roslaunch","roslaunch","joy.launch",NULL);
        return 0;
      }
    
```

We will be done once we will have provided Webots with an executable file in
"WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick" whose name
matches the controller directory name, i.e. "joystick" (which is also the name
specified in "joystick.wbt"). As we want this executable to be a ROS a node, we
will create and build a ROS package called "webots_joystick" and copy the
resulting executable in
"WEBOTS_MODULES_PATH/projects/languages/ros/controllers/joystick".

Prior to package construction, we create and setup a *catkin* workspace from
which we will run most of the build process through the `catkin_make` command.

### Conclusion

You should be able to run the "joystick" you just built as the original one
(open "~/my_ros/worlds/joystick.wbt" and hit the play button). You hence
achieved a fully functional Webots controller implemented as a ROS node.
Exploring further Webots C/C++ and Python APIs will allow you to integrate
larger ROS frameworks.

