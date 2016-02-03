## Robot

Derived from `Solid`.


```
Robot {
  SFString   controller        "void"
  SFString   controllerArgs    ""
  SFString   data              ""
  SFBool     synchronization   TRUE
  MFFloat    battery           []
  SFFloat    cpuConsumption    0   # [0,inf)
  SFBool     selfCollision     FALSE
  SFBool     showRobotWindow   FALSE
  SFString   robotWindow       ""
  SFString   remoteControl     ""
}
```

Direct derived nodes: `DifferentialWheels`, `Supervisor`.

### Description

The `Robot` node can be used as basis for building a robot, e.g., an articulated
robot, a humanoid robot, a wheeled robot... If you want to build a two-wheels
robot with differential-drive you should also consider the `DifferentialWheels`
node. If you would like to build a robot with supervisor capabilities use the
`Supervisor` node instead (Webots PRO license required).

### Field Summary

- `controller`: name of the controller program that the simulator must use to control the robot. This program is located in a directory whose name is equal to the field's value. This directory is in turn located in the "controllers" subdirectory of the current project directory. For example, if the field value is "my_controller" then the controller program should be located in "my_project/controllers/my_controller/my_controller[.exe]". The ".exe" extension is added on the Windows platforms only.
- `controllerArgs`: string containing the arguments (separated by space characters) to be passed to the `main()` function of the C/C++ controller program or the `main()` method of the Java controller program.
- `data`: this field may contain any user data, for example parameters corresponding to the configuration of the robot. It can be read from the robot controller using the `wb_robot_get_data()` function and can be written using the `wb_robot_set_data()` function. It may also be used as a convenience for communicating between a robot and a supervisor without implementing a Receiver / Emitter system: The supervisor can read and write in this field using the generic supervisor functions for accessing fields.
- `synchronization`: if the value is `TRUE` (default value), the simulator is synchronized with the controller; if the value is `FALSE`, the simulator runs as fast as possible, without waiting for the controller. The `wb_robot_get_synchronization()` function can be used to read the value of this field from a controller program.
- `battery`: this field should contain three values: the first one corresponds to the present energy level of the robot in Joules (*J*), the second is the maximum energy the robot can hold in Joules, and the third is the energy recharge speed in Watts (*[W]=[J]/[s]*). The simulator updates the first value, while the other two remain constant. *Important:* when the current energy value reaches zero, the corresponding controller process terminates and the simulated robot stops all motion.Note: *[J]=[V].[A].[s] and [J]=[V].[A.h]/3600*
- `cpuConsumption`: power consumption of the CPU (central processing unit) of the robot in Watts.
- `selfCollision`: setting this field to TRUE will enable the detection of collisions within the robot and apply the corresponding contact forces, so that the robot limbs cannot cross each other (provided that they have a `Physics` node). This is useful for complex articulated robots for which the controller doesn't prevent inner collisions. Enabling self collision is, however, likely to decrease the simulation speed, as more collisions will be generated during the simulation. Note that only collisions between non-consecutive solids will be detected. For consecutive solids, e.g., two solids attached to each other with a joint, no collision detection is performed, even if the self collision is enabled. The reason is that this type of collision detection is usually not wanted by the user, because a very accurate design of the bounding objects of the solids would be required. To prevent two consecutive solid nodes from penetrating each other, the `minStop` and `maxStop` fields of the corresponding joint node should be adjusted accordingly. Here is an example of a robot leg with self collision enabled: `Thigh (solid) | Knee (joint) | Leg (solid) | Ankle (joint) | Foot (solid)` In this example, no collision is detected between the "Thigh" and the "Leg" solids because they are consecutive, e.g., directly joined by the "Knee". In the same way no collision detection takes place between the "Leg" and the "Foot" solids because they are also consecutive, e.g., directly joined by the "Ankle". However, collisions may be detected between the "Thigh" and the "Foot" solids, because they are non-consecutive, e.g., they are attached to each other through an intermediate solid ("Leg"). In such an example, it is probably a good idea to set `minStop` and `maxStop` values for the "Knee" and "Ankle" joints.
- `showRobotWindow`: defines whether the robot window should be shown at the startup of the controller. If yes, the related entry point function of the robot window controller plugin (`wbw_show()`) is called as soon as the controller is initialized.
- `robotWindow`: defines the path of the robot window controller plugin used to display the robot window. If the `robotWindow` field is empty, the default generic robot window is loaded. The search algorithm works as following: Let $(VALUE) be the value of the `robotWindow` field, let $(EXT) be the shared library file extension of the OS (".so", ".dll" or ".dylib"), let $(PREFIX) be the shared library file prefix of the OS ("" on windows and "lib" on other OS), let $(PROJECT) be the current project path, let $(WEBOTS) be the webots installation path, and let $(...) be a recursive search, then the first existing file will be used as absolute path:$(PROJECT)/plugins/robot_windows/$(VALUE)/$(PREFIX)$(VALUE)$(EXT)$(WEBOTS)/resources/$(...)/plugins/robot_windows/$(VALUE)/$(PREFIX)$(VALUE)$(EXT)
- `remoteControl`: defines the path of the remote-control controller plugin used to remote control the real robot. The search algorithm is identical to the one used for the robotWindow field, except that the subdirectory of `plugins` is `remote_controls` rather than `robot_windows`.

### Synchronous versus Asynchronous controllers

The `synchronization` field specifies if a robot controller must be synchronized
with the simulator or not.

If `synchronization` is `TRUE` (the default), the simulator will wait for the
controller's `wb_robot_step()` whenever necessary to keep the simulation and the
controller synchronized. So for example if the simulation step
(`WorldInfo.basicTimeStep`) is 16 ms and the control step (`wb_robot_step()`) is
64 ms, then Webots will always execute precisely 4 simulation steps during one
control step. After the 4th simulation step, Webots will wait for the
controller's next control step (call to `wb_robot_step(64)`).

If `synchronization` is `FALSE`, the simulator will run as fast a possible
without waiting for the control step. So for example, with the same simulation
step (16 ms) and control step (64 ms) as before, if the simulator has finished
the 4th simulation step but the controller has not yet reached the call to
`wb_robot_step(64)`, then Webots will not wait; instead it will continue the
simulation using the latest actuation commands. Hence, if `synchronization` is
`FALSE`, the number of simulation steps that are executed during a control step
may vary; this will depend on the current simulator and controller speeds and on
the current CPU load, and hence the outcome of the simulation may also vary.
Note that if the number of simulation steps per control step varies, this will
appear as a variations of the "speed of the physics" in the controller's point
of view, and this will appear as a variation of the robot's reaction speed in
the user's point of view.

So generally the `synchronization` field should be set to `TRUE` when robust
control is required. For example if a motion (or ".motion file") was designed in
synchronous mode then it may appear completely different in asynchronous mode.
The asynchronous mode is currently used only for the robot competitions, because
in this case it is necessary to limit the CPU time allocated to each
participating controller. Note that it is also possible to combine synchronous
and asynchronous controllers, e.g., for the robot competitions generally the
`Supervisor` controller is synchronous while the contestants controllers are
asynchronous. Asynchronous controllers may also be recommended for networked
simulations involving several robots distributed over a computer network with an
unpredictable delay (like the Internet).

### Robot Functions

