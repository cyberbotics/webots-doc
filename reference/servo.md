## Servo

Derived from `Device`.


```
Servo {
  SFString   type             "rotational"
  SFFloat    maxVelocity      10      # (0,inf)
  SFFloat    maxForce         10      # [0,inf)
  SFFloat    controlP         10      # (0,inf)
  SFFloat    acceleration     -1      # -1 or (0,inf)
  SFFloat    position         0
  SFFloat    minPosition      0       # (-inf,0]
  SFFloat    maxPosition      0       # [0,inf)
  SFFloat    minStop          0       # [-pi,0]
  SFFloat    maxStop          0       # [0,pi]
  SFFloat    springConstant   0       # [0,inf)
  SFFloat    dampingConstant  0       # [0,inf)
  SFFloat    staticFriction   0       # [0,inf)
}
```

### Description

A `Servo` node is used to add a joint (1 degree of freedom (DOF)) in a
mechanical simulation. The joint can be active or passive; it is placed between
the parent and children nodes (".wbt" hierarchy) of the `Servo` and therefore it
allows the children to move with respect to the parent. The `Servo` can be of
type "rotational" or "linear". A "rotational" `Servo` is used to simulate a
rotating motion, like an electric motor or a hinge. A "linear" `Servo` is used
to simulate a sliding motion, like a linear motor, a piston, a
hydraulic/pneumatic cylinder, a spring, or a damper.

### Field Summary

### Units

Rotational servos units are expressed in *radians* while linear servos units are
expressed in *meters*. See :

 | Rotational | Linear
--- | --- | ---
Position | rad (radians) | m (meters)
Velocity | rad/s (radians / second) | m/s (meters / second)
Acceleration | rad/s^2 (radians / second^2) | m/s^2 (meters / second^2)
Torque/Force | N*m (Newtons * meters) | N (Newtons)

### Initial Transformation and Position

The `Servo` node inherits the `translation` and `rotation` fields from the
`Transform` node. These two fields represent the initial coordinate system
transformation between the `Servo` parent and children.

In a "rotational" `Servo`, these fields have the following meaning: The
`translation` field specifies the translation of the axis of rotation. The
`rotation` field specifies the orientation of the axis of rotation. See .

![Rotational servo](pdf/rotational_servo.pdf)

**Rotational servo**

In a "linear" `Servo`, these fields have the following meaning: The
`translation` field specifies the translation of the sliding axis. The
`rotation` field specifies the direction of the sliding axis. See .

![Linear servo](pdf/linear_servo.pdf)

**Linear servo**

The `position` field represents the current angle difference (in radians) or the
current distance (in meters) with respect to the initial `translation` and
`rotation` of the `Servo`. If `position` field is zero then the `Servo` is at
its initial `translation` and `rotation`. For example if we have a "rotational"
`Servo` and the value of the `position` field is 1.5708, this means that this
`Servo` is 90 degrees from its initial rotation. The values passed to the
`wb_servo_set_position()` function are specified with respect to the position
zero. The values of the `minPosition`, `maxPosition`, `minStop` and `maxStop`
fields are also defined with respect to the position zero.

### Position Control

The standard way of operating a `Servo` is to control the position directly
(*position control*). The user specifies a target position using the
`wb_servo_set_position()` function, then the P-controller takes into account the
desired velocity, acceleration and motor force in order to move the servo to the
target position. See .

In Webots, position control is carried out in three stages, as depicted in . The
first stage is performed by the user-specified controller (1) that decides which
position, velocity, acceleration and motor force must be used. The second stage
is performed by the servo P-controller (2) that computes the current velocity of
the servo `V`. Finally, the third stage (3) is carried out by the physics
simulator (ODE joint motors).

![Servo control](pdf/servo_control.pdf)

**Servo control**

At each simulation step, the P-controller (2) recomputes the current velocity
*Vc* according to the following algorithm: `Vc = P * (Pt - Pc); if (abs(Vc) >
Vd) Vc = sign(Vc) * Vd; if (A != -1) { a = (Vc - Vp) / ts; if (abs(a) > A) a =
sign(a) * A; Vc = Vp + a * ts; }` where  `V` is the current servo velocity in
rad/s or m/s, `P` is the P-control parameter specified in `controlP` field or
set with `wb_servo_set_control_p()`, `P` is the *target position* of the servo
set by the function `wb_servo_set_position()`, `P` is the current servo position
as reflected by the `position` field, `V` is the desired velocity as specified
by the `maxVelocity` field (default) or set with `wb_servo_set_velocity()`, `a`
is the acceleration required to reach *Vc* in one time step, `V` is the motor
velocity of the previous time step, `t` is the duration of the simulation time
step as specified by the `basicTimeStep` field of the `WorldInfo` node
(converted in seconds), and `A` is the acceleration of the servo motor as
specified by the `acceleration` field (default) or set with
`wb_servo_set_acceleration()`.

### Velocity Control

The servos can also be used with *velocity control* instead of *position
control*. This is obtained with two function calls: first the
`wb_servo_set_position()` function must be called with `INFINITY` as a position
parameter, then the desired velocity, which may be positive or negative, must be
specified by calling the `wb_servo_set_velocity()` function. This will initiate
a continuous servo motion at the desired speed, while taking into account the
specified acceleration and motor force. Example: `wb_servo_set_position(servo,
INFINITY); wb_servo_set_velocity(servo, 6.28);  // 1 rotation per second`
`INFINITY` is a C macro corresponding to the IEEE 754 floating point standard.
It is implemented in the C99 specifications as well as in C++. In Java, this
value is defined as `Double.POSITIVE_INFINITY`. In Python, you should use
`float('inf')`. Finally, in Matlab you should use the `inf` constant.

### Force Control

The position/velocity control described above are performed by the Webots
P-controller and ODE's joint motor implementation (see ODE documentation). As an
alternative, Webots does also allow the user to directly specify the amount of
torque/force that must be applied by a `Servo`. This is achieved with the
`wb_servo_set_force()` function which specifies the desired amount of
torque/forces and switches off the P-controller and motor force. A subsequent
call to `wb_servo_set_position()` restores the original *position control*. Some
care must be taken when using *force control*. Indeed the torque/force specified
with `wb_servo_set_force()` is applied to the `Servo` continuously. Hence the
`Servo` will infinitely accelerate its rotational or linear motion and
eventually *explode* unless a functional force control algorithm is used.

 | position control | velocity control | force control
--- | --- | --- | --- | ---
uses P-controller | yes | no | no
wb_servo_set_position() | * specifies the desired position | should be set to INFINITY | switches to position/velocity control
wb_servo_set_velocity() | specifies the max velocity | * specifies the desired velocity | is ignored
wb_servo_set_acceleration() | specifies the max acceleration | specifies the max acceleration | is ignored
wb_servo_set_motor_force() | specifies the available force | specifies the available force | specifies the max force
wb_servo_set_force() | switches to force control | switches to force control | * specifies the desired force

### Servo Limits

The `position` field is a scalar value that represents the current servo
"rotational" or "linear" position. For a rotational servo, `position` represents
the difference (in radians) between the initial and the current angle of its
rotation field. For a linear servo, `position` represents the distance (in
meters) between the servo's initial and current translation (`translation`
field).

The `minPosition` and `maxPosition` fields define the *soft limits* of the
servo. Soft limits specify the *software* boundaries beyond which the
P-controller will not attempt to move. If the controller calls
`wb_servo_set_position()` with a target position that exceeds the soft limits,
the desired target position will be clipped in order to fit into the soft limit
range. Since the initial position of the servo is always zero, `minPosition`
must always be negative or zero, and `maxPosition` must always be positive or
zero. When both `minPosition` and `maxPosition` are zero (the default), the soft
limits are deactivated. Note that the soft limits can be overstepped when an
external force which exceeds the motor force is applied to the servo. For
example, it is possible that the weight of a robot exceeds the motor force that
is required to hold it up.

The `minStop` and `maxStop` fields define the *hard limits* of the servo. Hard
limits represent physical (or mechanical) bounds that cannot be overrun by any
force. Hard limits can be used, for example, to simulate both end caps of a
hydraulic or pneumatic piston or to restrict the range of rotation of a hinge.
The value of `minStop` must be in the range [-pi, 0] and `maxStop` must be in
the range [0, pi]. When both `minStop` and `maxStop` are zero (the default), the
hard limits are deactivated. The servo hard limits use ODE joint stops (for more
information see the ODE documentation on `dParamLoStop` and `dParamHiStop`).

Finally, note that when both soft and hard limits are activated, the range of
the soft limits must be included in the range of the hard limits, such that
`minStop lt= minValue` and `maxStopgt= maxValue`.

### Springs and Dampers

The `springConstant` field specifies the value of the spring constant (or spring
stiffness), usually denoted as `K`. The `springConstant` must be positive or
zero. If the `springConstant` is zero (the default), no spring torque/force will
be applied to the servo. If the `springConstant` is greater than zero, then a
spring force will be computed and applied to the servo in addition to the other
forces (i.e., motor force, damping force). The spring force is calculated
according to Hooke's law: `F = -Kx`, where `K` is the `springConstant` and `x`
is the current servo position as represented by the `position` field. Therefore,
the spring force is computed so as to be proportional to the current servo
position, and to move the servo back to its initial position. When designing a
robot model that uses springs, it is important to remember that the spring's
resting position for each servo will correspond to the initial position of the
servo.

The `dampingConstant` field specifies the value of the servo damping constant.
The value of `dampingConstant` must be positive or zero. If `dampingConstant` is
zero (the default), no damping torque/force will be added to the servo. If
`dampingConstant` is greater than zero, a damping torque/force will be applied
to the servo in addition to the other forces (i.e., motor force, spring force).
This damping torque/force is proportional to the effective servo velocity: `F =
-Bv`, where `B` is the damping constant, and `v = dx/dt` is the effective servo
velocity computed by the physics simulator.

![Mechanical Diagram of a Servo](pdf/servo_mechanics.pdf)

**Mechanical Diagram of a Servo**

As you can see in (see  ), a `Servo` creates a joint between two masses `m` and
`m`. `m` is defined by the `Physics` node in the parent of the `Servo`. The mass
`m` is defined by the `Physics` node of the `Servo`. The value `x` corresponds
to the initial translation of the `Servo` defined by the `translation` field.
The position `x` corresponds to the current position of the `Servo` defined by
the `position` field.

### Servo Forces

Altogether, three different forces can be applied to a `Servo`: the motor force,
the spring force and the damping force. These three forces are applied in
parallel and can be switched on and off independently (by default only the motor
force is on). For example, to turn off the motor force and obtain a passive
`Servo`, you can set the `maxForce` field to zero.

Force | motor force | spring force | damping force
--- | --- | --- | ---
Turned on when: | maxForce gt 0 | springConstant gt 0 | dampingConstant gt 0
Turned off when: | maxForce = 0 | springConstant = 0 | dampingConstant = 0
regular motor (the default) | on | off | off
regular spring amp damper | off | on | on
damper (without spring) | off | off | on
motor with friction | on | off | on
spring without any friction | off | on | off

To obtain a spring amp damper element, you can set `maxForce` to zero and
`springConstant` and `dampingConstant` to non-zero values. A pure spring is
obtained when both `maxForce` and `dampingConstant` but not `springConstant` are
set to zero. However in this case the spring may oscillate forever because
Webots will not simulate the air friction. So it is usually wise to associate
some damping to every spring.

### Friction

The friction applied on the `Servo` to slow down its velocity is computed as the
maximum between the `maxForce` and the `staticFriction` values. The static
friction is particularily useful to add a friction for a passive `Servo`.

### Serial Servos

Each instance of a `Servo` simulates a mechanical system with optional motor,
spring and damping elements, mounted in parallel. Sometimes it is necessary to
have such elements mounted serially. With Webot, serially mounted elements must
be modeled by having `Servo` nodes used as children of other `Servo` nodes. For
example if you wish to have a system where a motor controls the resting position
of a spring, then you will need two `Servo` nodes, as depicted in . In this
example, the parent `Servo` will have a motor force (maxForce gt 0) and the
child `Servo` will have spring and damping forces (`springConstant` gt 0 and
`dampingConstant` gt 0).

![Example of serial connection of two Servo nodes](pdf/servo_serial.pdf)

**Example of serial connection of two Servo nodes**

This is equivalent to this ".wbt" code, where, as you can notice, *Servo2* is a
child of *Servo1*:


```
DEF Servo1 Servo {
  ...
  children [
    DEF Servo2 Servo {
      ...
      children [
        ...
      ]
      boundingObject ...
      physics Physics {
        mass {m2}
      }
      maxForce 0
      springConstant {K}
      dampingConstant {B}
    }
  ]
  boundingObject ...
  physics Physics {
    mass {m1}
  }
  maxForce {M}
  springConstant 0
  dampingConstant 0
}
```

Note that it is necessary to specify the `Physics` and the `boundingObject` of
*Servo1*. This adds the extra body `m` in the simulation, between the motor and
the spring and damper.

### Simulating Overlayed Joint Axes

Sometimes it is necessary to simulate a joint with two or three independent but
overlayed rotation axes (e.g., a shoulder joint with a *pitch* axis and a *roll*
axis). As usually with Webots, each axis must be implemented as a separate
`Servo` node. So for two axes you need two `Servo` nodes, for three axes you
need three `Servo` nodes, etc.

With overlayed axes (or very close axes) the mass and the shape of the body
located between these axes is often unknown or negligible. However, Webots
requires all the intermediate `boundingObject` and `physics` fields to be
defined. So the trick is to use dummy values for these fields. Usually the dummy
`boundingObject` can be specified as a `Sphere` with a radius of 1 millimeter. A
`Sphere` is the preferred choice because this is the cheapest shape for the
collision detection. And the `physics` field can use a `Physics` node with
default values.

This is better explained with an example. Let's assume that we want to build a
pan/tilt robot head. For this we need two independent (and perpendicular)
rotation axes: *pan* and *tilt*. Now let's assume that these axes cross each
other but we don't know anything about the shape and the mass of the body that
links the two axes. Then this can be modeled like this:


```
DEF PAN Servo {
  ...
  children [
    DEF TILT Servo {
      translation 0 0 0  # overlayed
      children [
        DEF HEAD_TRANS Transform {
          # head shape
        }
        # head devices
      ]
      boundingObject USE HEAD_TRANS
      physics Physics {
      }
    }
  ]
  boundingObject DEF DUMMY_BO Sphere {
    radius 0.001
  }
  physics DEF DUMMY_PHYSICS Physics {
  }
}
```

Please note the dummy `Physics` and the 1 millimeter `Sphere` as dummy
`boundingObject`.

### Servo Functions

