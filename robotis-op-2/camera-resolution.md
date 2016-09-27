## Camera resolution

In remote control, the camera's resolutions supported are not the same as in
cross-compilation, indeed they are smaller in order to not slow down too much
the communication speed between Webots and the robot. All the resolutions
available are specified in the [following table](#cameraremoteresolution).
Unlike from cross-compilation you do not have to specify the desired resolution
in any file, the resolution is automatically send to the robot from Webots. So
in order to adjust the resolution, just do the same way you would do it in the
simulation (by editing `cameraWidth` and `cameraHeight` fields of the DARwIn-OP
in the scene tree window).

%figure "Camera resolutions supported in remote-control"

| Width [pixel] | Height [pixel] |
| ------------- | -------------- |
| 320           | 240            |
| 160           | 120            |
| 80            | 80             |
| 40            | 60             |
| 20            | 40             |

%end

> **note**:
You do not need to choose a width and a height from the same line, any
combination of height and width is valid (for example, you can use a resolution
of 320x30).
