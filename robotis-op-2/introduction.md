## Introduction

The Robotis OP2 (or formally ROBOTIS OP2) is an open source miniature humanoid
robot platform with advanced computational power.
It is developed and manufactured by ROBOTIS (a Korean robot manufacturer) in
collaboration with the University of Pennsylvania.

>**Note**:
The previous model was named DARwIn-OP. It means _**D**ynamic **A**nthropomorphic **R**obot **w**ith
**In**telligence**-O**pen **P**latform_.

The Robotis OP2 is mainly used by universities and research centers for
educational and research purposes. It has a total of 20 degrees of freedoms:

- Two in the head ;
- Three in each arm ;
- Six in each leg.

This robot is available at a fairly low price and is based on open source
components (both hardware and software). It has been used in the RoboCup
international competition with some success.

The Robotis OP2 robot has been fully integrated into Webots in collaboration with
ROBOTIS. By using Robotis OP2 in conjunction with Webots you will have following
 benefits compared to a direct use of ROBOTIS API on the robot:

- **Simulation**: You will be able to test your controller in simulation, without
any risk of damaging the robot. You will also be able to run automatically a lot
of different simulations in a very small amount of time (to tune up parameters
for example), which would be impossible to do with the real robot.
- **Remote compilation**: When your controller is doing fine in simulation, you will
be able to send, compile and run it on the real robot, without changing anything to your
code, just by pressing a button in the robot window.
- **Remote control**: To debug or understand your controller's behavior, you will be
able to see in real time all sensor and actuator states on your
computer screen. This is available both in simulation and on the real robot.
Here again, this is done in just one click. You will also be able to run your
controller on the computer, but instead of sending commands to and reading
sensor data from the simulated robot, it sends commands to and reads sensor data
from the real robot.
- **Ease of use**: Webots greatly simplifies the programming of the robot. Indeed,
Webots API is simple to understand and to use thanks to examples and documentation.
