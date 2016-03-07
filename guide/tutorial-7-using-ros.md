## Tutorial 7: Using ROS

This tutorial explains how to use the nodes from the `webots_ros` package
provided with Webots.

These examples were tested with ROS `jade`, `indigo`, `hydro` and `groovy`
distributions on Linux. There is no warranty they will work if you use a
different platform or an ancient distribution of ROS.

### Installing ROS

In order to use these nodes, you will first need to install the ROS framework.
To install the last version of ROS on Ubuntu use the following commands:

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net:80 --recv-key 0xB01FA116
sudo apt-get update
sudo apt-get install ros-jade-desktop-full
sudo apt-get install ros-jade-sensor-msgs
sudo rosdep init
rosdep update
```

For more information or to install it on another platform please reading
[http://wiki.ros.org/ROS/Installation](http://wiki.ros.org/ROS/Installation).
Unless you need older version for some other application, you should choose the
latest distribution (Jade Turtle).

> **note**:
If you never used the ROS framework before, it is strongly recommended to follow
some tutorials at:
[http://wiki.ros.org/ROS/Tutorials](http://wiki.ros.org/ROS/Tutorials). These
tutorials will also help you setting up your ROS environment and initializing
your catkin workspace.

### webots_ros package installation

If you haven't created any catkin workspace yet, you can create one with the
following commands:

```
mkdir -p catkin_ws/src
cd catkin_ws/src
catkin_init_workspace
```

Once your workspace is set, you have to copy the `webots_ros` folder located in
"projects/languages/ros" in the `src` folder of your catkin workspace. You will
also need to copy the list of the services and messages definitions of the
`webots_ros` package. Simply copy the `srv` and `msg` folders located in
"projects/default/controllers/ros/include" into the "webots\_ros" folder of your
catkin workspace.

The `webots_ros` package already contains a "CmakeList.txt" with build
instructions for the package. All you have to do, in order to build the package,
is to run:

```
cd catkin_ws
catkin_make
```

### Running the nodes

Now that you have built the package, you can run the example you want. You will
first have to launch the master node with the following command:

```
roscore
```

You can then start Webots and open the world of the example you want to run (the
example worlds are located in "projects/languages/ros/worlds"). When you start
the simulation the controller should connect to the master and the simulation
should start, waiting for instructions.

If the controller can't connect to the master node, it probably means the master
node doesn't use the standard `ROS_MASTER_URI`. You can check in the terminal in
which the master node was started what `ROS_MASTER_URI` is used and you can then
add the correct address in the controller arguments, in the environment
variables or in a runtime.ini file in the controller directory.

You can then start the ROS node corresponding to this example in a new terminal
using the following command:

```
rosrun webots_ros [node_name]
```

For example, if you opened the world
"projects/languages/ros/worlds/panoramic\_view\_recorder.wbt" you will have to
start the `panoramic_view_recorder` node with the following command:

```
rosrun webots_ros panoramic_view_recorder
```

> **note**:
The seed of the Webots random number generator is initialized at the beginning
of the simulation and not when the ROS nodes connect. Webots has to be running
so that the ROS nodes can connect. However, we cannot guarantee how long it will
run before the ROS nodes connect. Therefore, the sensor measurements and motor
commands will slightly differ from one run to another, due to the noise being
slightly different at the time of the connection of the ROS nodes. This may have
consequences on the behavior of the robots, thus making such simulations non
fully reproducible. You can use the '--synchronize' argument in order to make
sure that Webots will not run before the ROS node connects. This is useful to
make ROS-based simulation reproducible.

<!-- -->

> **note**:
If you want to use different computers for the ROS master, the Webots simulation
and/or the nodes, you must be able to connect to each of them with SSH in both
ways. The hostname and IP addresses of these computers should be listed in the
known hosts list of each computer and the `ROS_MASTER_URI` variable should be
adjusted accordingly.

### Creating new nodes

These examples only show a few possibilities for interfacing ROS and Webots, but
you can build your own nodes to connect with Webots.

The `robot_information_parser` node is the most basic one and is a good base to
start building your own node. The `complete_test` node doesn't show any
particular application but contains an almost exhaustive list of the Webots API
functions.

All the functions from the Webots API have their corresponding services or
topics. You can find in the `Reference Manual` the definitions of all the
services and topics associated with each device.

