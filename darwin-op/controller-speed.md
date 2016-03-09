## Controller speed

Your controller is supposed to run at a speed of 1.0x whatever you chose to run
the simulation at run in `real-time` or `as fast as possible` mode. It can still
happen sometimes that the speed can not achieve a speed of 1.0x, especialy when
using the camera at high resolution, the mode `as fast as possible without
graphics` should resolve this problem.

If despite this you can not achieve a speed of 1.0x, it means that your
connection with the robot is to slow. You should consider reducing camera
resolution in order to increase the speed.

