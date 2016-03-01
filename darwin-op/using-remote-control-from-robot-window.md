## Using remote-control from robot-window

To use remote-control, open the robot window, go to the `Transfer` tab, as for
cross-compilation you have to set the connection settings (the settings been the
same as for cross-compilation, see previous chapter for more information). To
start the remote control, stop and revert your simulation, put your robot in the
[stable
position](send-a-controller-to-the-robot.md#start-position-of-the-robot-the-robot-is-sit-down-same-start-position-as-in-simulation).
Then press the following button:

%figure "remote-control button"

![remote-control button](images/remote.png)

%end

A small window (similar of the one from the [following
picture](#this-small-window-asks-you-to-wait-until-remote-control-has-started)})
will appear and ask you to wait until the remote-control has been started. When
this window disappears and the eyes of the robot switch from red to green, the
remote-control has been sucessfully started. You can now easily start and stop
your controller in remote-control mode by using the run and stop button of
Webots (see chapter \textit{Examples} for more details). Warning: if you revert
the simulation it will stop the remote-control mode. In order to stop the
remote-control (without reverting) simply press the stop button of the remote
control (it has the same aspect from the one of the
[cross-compilation](send-a-controller-to-the-robot.md#stop-button) ).

%figure "This small window asks you to wait until remote-control has started"

![This small window asks you to wait until remote-control has started](images/waitWindow.png)

%end

When the controller runs in remote-control mode, you can see in the other tabs
of the robot window the values of the sensors of the real robot in real-time.

