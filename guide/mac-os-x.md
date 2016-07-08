## Mac OS X

### MATLAB and robot plugins

The controllers and the robot plugins (e.g. the robot windows) are sharing the
same process. Generally this mechanism is works well, but some instabilities
(crashes and warnings) may occur when a robot uses a MATLAB controller and a
robot window at the same time. This is due to some conflicts between the Qt
libraries used by MATLAB and the one used by Webots.
