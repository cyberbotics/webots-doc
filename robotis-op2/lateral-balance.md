## Lateral Balance

In simulation, in the `RobotisOp2GaitManager`, the lateral balance does not work as expected.
It is recommended to set `balance_hip_roll_gain` and `balance_ankle_roll_gain` to 0.0, this must be done in the 'config.ini' file associated with the controller.
