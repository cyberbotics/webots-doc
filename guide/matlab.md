## Matlab

The `MATLAB` API for Webots is very similar to the C API. The functions names
are identical, only the type and number of parameters differs slightly in some
cases. The `MATLAB` functions and prototypes are described in Webots Reference
Manual. Note that unlike with the C API, there are no `wb_robot_init()` and
`wb_robot_cleanup()` functions in the `MATLAB`  API. The necessary
initialization and cleanup are automatically carried out respectively before
entering and after leaving the controller code.

If the `MATLAB` code uses graphics, it is necessary to call the `drawnow`
command somewhere in the control loop in order to flush the graphics.

Here is a simple `MATLAB` controller example:

```
% uncomment the next two lines to use the
```



### Using the 

In order to avoid cluttering the desktop with too many windows, Webots starts
`MATLAB` with the *-nodesktop* option. The *-nodesktop* option starts `MATLAB`
without user interface and therefore it keeps the memory usage low which is
useful in particular for multi-robot experiments. If you would like to use the
`MATLAB` desktop to interact with your controller you just need to add these two
`MATLAB` commands somewhere at the beginning of your controller m-file:


```
desktop;
keyboard;
```

The `desktop` command brings up the `MATLAB` desktop. The `keyboard` stops the
execution of the controller and gives control to the keyboard (`K>>` prompt).
Then `MATLAB` opens your controller m-file in its editor and indicates that the
execution is stopped at the `keyboard` command. After that, the controller
m-file can be debugged interactively, i.e., it is possible to continue the
execution step-by-step, set break points, watch variable, etc. While debugging,
the current values of the controller variables are shown in the `MATLAB`
workspace. It is possible to *continue* the execution of the controller by
typing `return` at the `K>>` prompt. Finally the execution of the controller can
be terminated with `Ctrl-C` key combination.

Once the controller is terminated, the connection with Webots remains active.
Therefore it becomes possible to issue Webots commands directly at the `MATLAB`
prompt, for example you can interactively issue commands to query the sensors,
etc.:


```
>> wb_differential_wheels_set_speed(600, 600);
>> wb_robot_step(1000);
>> wb_gps_get_values(gps)

ans =

    0.0001    0.0030   -0.6425
>> |
```

It is possible to use additional `keyboard` statements in various places in your
".m" controller. So each time `MATLAB` will run into a `keyboard` statement, it
will return control to the `K>>` prompt where you will be able to debug
interactively.

At this point, it is also possible to restart the controller by calling its
m-file from `MATLAB` prompt. Note that this will restart the controller only,
not the whole simulation, so the current robot and motor positions will be
preserved. If you want to restart the whole simulation you need to use the
`Revert` button as usual.

