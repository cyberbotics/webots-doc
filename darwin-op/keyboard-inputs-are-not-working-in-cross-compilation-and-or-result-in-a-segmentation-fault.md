## Keyboard inputs are not working in cross-compilation and/or result in a segmentation fault

Check that the keyboard window is oppened on the robot when enabling the
keyboard and be sure to not unfocus the keyboard window on the robot.

If you are starting the controller 'manually' by SSH, use the -X option when
starting SSH, and use the command 'export DISPLAY=:0' before to start the
controller.
