## Send a controller to the robot

To test your controller on the real robot press the following button:

%figure "Send icon"

![Send icon](png/send.png)

%end

Webots will then connect to the robot, if any error appears during the
connection, the reason will be shown. If it is the first time you connect the
robot with Webots, Webots will install all the files needed on the robot. This
can take some time and some step are longer than other, so be patient please,
this happens only on the first connection, the next ones will be shorter. You
can also see in real time what is appening in the `DARwIn-OP console`. Webots
will also stop the auto start of the demo program at the startup of the robot,
but don't worry the program is not suppressed and the auto start can easily be
reinstalled (explanation follows).

Then the controller code itself is sent to the robot. The whole controller
directory is sent to the robot, so please put all the files needed by your
controller in the same directory. The controller itself is then compiled for the
robot and you can see the compilation in the `DARwIn-OP console`. If the
compilation succeeds and the robot is close to the [start
position](#start-position-of-the-robot-the-robot-is-sit-down-same-start-position-as-in-simulation)
the controller will be initialized (head and eyes LED in red) and then started
(head and eyes LED in green).

%figure "Start position of the robot. The robot is sit down (same start position as in simulation)"

![Start position of the robot. The robot is sit down (same start position as in simulation)](png/start_position.png)

%end

It is recommended when testing a new controller whose behavior is not very
certain to hold the robot by its handle.

To stop the controller press the following button:

%figure "Stop button"

![Stop button](png/stop.png)

%end

This will stop the controller and clean all files previously sent to the robot.
You can also stop the controller by pressing the right button at the back of the
robot. This will not entirely stop the controller but will at least avoid the
robot from moving. It will also release the torque of all the servos.

