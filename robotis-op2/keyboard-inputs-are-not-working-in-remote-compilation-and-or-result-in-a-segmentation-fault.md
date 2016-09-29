## Keyboard inputs are not working in remote compilation and/or result in a segmentation fault

Check that the keyboard window is open on the robot when enabling the
keyboard and be sure this window do not lost keyboard focus on the robot.

If you are starting the controller 'manually' by SSH, use the -X option when
starting SSH, and use the following command before to start the controller.

```sh
export DISPLAY=:0 ./my-controller
```
