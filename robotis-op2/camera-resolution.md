## Camera resolution

In remote control, supported camera resolutions are not the same as in remote compilation.
Indeed they are smaller in order to not slow down too much the communication speed between Webots and the robot.
All available resolutions are specified in the [following table](#cameraremoteresolution).
Unlike from remote compilation you do not have to specify the desired resolution in any file, the resolution is automatically sent to the robot from Webots.
So in order to adjust the resolution, just do the same way you would do it in the simulation (by editing `cameraWidth` and `cameraHeight` fields of the ROBOTIS OP2 in the scene tree window).

%figure "Camera resolutions supported in remote-control"

| Width [pixels] | Height [pixels] |
| ------------- | -------------- |
| 320           | 240            |
| 160           | 120            |
| 80            | 80             |
| 40            | 60             |
| 20            | 40             |

%end

> **Note**: You do not need to choose a width and a height from the same line, any combination of height and width is valid (for example, you can use a resolution of 320x30).
