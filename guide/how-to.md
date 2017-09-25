## How To

This section gives various examples of complexe behaviors and/or
functionalities. The world files are located in the
"WEBOTS\_HOME/projects/samples/howto/world" directory, and their controllers in
the "WEBOTS\_HOME/projects/samples/howto/controllers" directory. For each, the
world file and its corresponding controller are named according to the behavior
they exemplify.

### binocular.wbt

**Keywords**: Stereovision, Stereoscopy, Camera

%figure "binocular"

![binocular.png](images/binocular.png)

%end

This example simply shows how to equip a robot with two `Camera`s for
stereovision. The example does not actually perform stereovision or any form of
computer vision.

### biped.wbt

**Keywords**: Humanoid robot, biped robot, power off, passive joint

%figure "biped"

![biped.png](images/biped.png)

%end

In this example, a biped robot stands up while his head rotates. After a few
seconds, all the motors are turned off and the robot collapses. This example
illustrates how to build a simple articulated robot and also how to turn off
motor power.

### force_control.wbt

**Keywords**: Force control, linear motor, spring and damper

%figure "force_control"

![force_control.png](images/force_control.png)

%end

This world shows two boxes connected by a `LinearMotor`. Here, the purpose is to
demonstrate the usage of the `wb_motor_set_force()` function to control a
`LinearMotor` with a user specified force. In this example,
`wb_motor_set_force()` is used to simulate the effect of a spring and a damper
between the two boxes. When the simulation starts, the motor force is used to
move the boxes apart. Then, the motor force is turned off and the boxes oscillate for
a while according to the spring and damping equations programmed in the
controller.

### inverted_pendulum.wbt

**Keywords**: Inverted pendulum, PID, LinearMotor

%figure "inverted_pendulum"

![inverted_pendulum.png](images/inverted_pendulum.png)

%end

In this example, a robot moves from left to right in order to keep an inverted
pendulum upright. This is known as the "Inverted Pendulum Problem", and it is
solved in our example by using a PID (Proportional Integral Differential)
controller.

### physics.wbt

**Keywords**: Physics plugin, OpenGL drawing, flying robot, Emitter, Receiver

%figure "physics"

![physics.png](images/physics.png)

%end

In this example, a robot flies using a physics plugin. This plugins is an
example of:

- how to access Webots objects in the physics plugin
- how to exchange information with the controller
- how to add custom forces
- how to move objects
- how to handle collisions
- how to draw objects using OpenGL

### supervisor.wbt

**Keywords**: Supervisor, DifferentialWheels, soccer, label, import node,
    restart simulation, screenshot, change controller

%figure "supervisor"

![supervisor.png](images/supervisor.png)

%end

This shows a simple soccer game with six robots and a referee. The `Supervisor`
code demonstrates the usage of several `Supervisor` functions. For example, the
`Supervisor` inserts a second ball to the simulation, changes its color, takes a
picture of the 3D view, restarts the simulation, etc. In addition the
`Supervisor` also plays the role of a soccer referee: it displays the current
score, places the players to their initial position when a goal is scored, etc.

### texture_change.wbt

**Keywords**: Supervisor, texture, `wb_supervisor_field_set_*()`, Camera

%figure "texture_change"

![texture_change.png](images/texture_change.png)

%end

In this example, a robot moves forward and backward in front of a large textured
panel. The robot watches the panel with its `Camera`. Meanwhile a `Supervisor`
switches the image displayed on the panel.
