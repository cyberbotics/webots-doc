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

