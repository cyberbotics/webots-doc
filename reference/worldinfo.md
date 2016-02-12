## WorldInfo

```
WorldInfo {
  SFString   title                          ""
  MFString   info                           []
  SFVec3f    gravity                        0 -9.81 0
  SFFloat    CFM                            0.00001  # [0,inf)
  SFFloat    ERP                            0.2      # [0,1]
  SFString   physics                        ""
  SFFloat    basicTimeStep                  32       # in ms
  SFFloat    FPS                            60
  SFInt32    optimalThreadCount             1        # maximum number of threads assigned to physics computation
  SFFloat    physicsDisableTime             1        # time after which the objects are disabled if they are idle
  SFFloat    physicsDisableLinearThreshold  0.01     # threshold determining if an object is idle or not
  SFFloat    physicsDisableAngularThreshold 0.01     # threshold determining if an object is idle or not
  SFNode     defaultDamping                 NULL     # default damping parameters
  SFFloat    inkEvaporation                 0        # make ground textures evaporate
  SFVec3f    northDirection                 1 0 0    # for compass and InertialUnit
  SFFloat    lineScale                      0.1      # control the length of every arbitrary-sized lines
  MFNode     contactProperties              []       # see ContactProperties node
}
```

The [WorldInfo](worldinfo.md#worldinfo) node provides general information on the
simulated world:

- The `title` field should briefly describe the purpose of the world.
- The `info` field should give additional information, like the author who created
the world, the date of creation and a description of the purpose of the world.
Several character strings can be used.
- The `gravity` field defines the gravitational acceleration to be used in physics
simulation. The gravity is set by default to the gravity found on earth. You
should change it if you want to simulate rover robots on Mars, for example. The
gravity vector defines the orientation of the ground plane used by
[InertialUnit](inertialunit.md#inertialunit)s.
- The `ERP` field defines the *Error Reduction Parameter* use by ODE to manage
contacts joints. This applies by default to all contact joints, except those
whose contact properties are defined in a
[ContactProperties](contactproperties.md#contactproperties) node. The ERP
specifies what proportion of the contact joint error will be fixed during the
next simulation step. If ERP=0 then no correcting force is applied and the
bodies will eventually drift apart as the simulation proceeds. If ERP=1 then the
simulation will attempt to fix all joint error during the next time step.
However, setting ERP=1 is not recommended, as the joint error will not be
completely fixed due to various internal approximations. A value of ERP=0.1 to
0.8 is recommended (0.2 is the default).
- The `CFM` field defines the *Constraint Force Mixing* use by ODE to manage
contacts joints. This applies by default to all contact joints, except those
whose contact properties are defined in a
[ContactProperties](contactproperties.md#contactproperties) node. Along with the
ERP, the CFM controls the spongyness and springyness of the contact joint. If a
simulation includes heavy masses, then decreasing the CFM value for contacts
will prevent heavy objects from penetrating the ground. If CFM is set to zero,
the constraint will be hard. If CFM is set to a positive value, it will be
possible to violate the constraint by *pushing on it* (for example, for contact
constraints by forcing the two contacting objects together). In other words the
constraint will be soft, and the softness will increase as CFM increases. What
is actually happening here is that the constraint is allowed to be violated by
an amount proportional to CFM times the restoring force that is needed to
enforce the constraint (see ODE documentation for more details).
- The `physics` field refers to a physics plugin which allows the user to program
custom physics effects using the ODE API. See   for a description on how to set
up a physics plugin. This is especially useful for modeling hydrodynamic forces,
wind, non-uniform friction, etc.
- The `basicTimeStep` field defines the duration of the simulation step executed
by Webots. It is a floating point value expressed in milliseconds. The minimum
value for this field is 0.001, that is, one microsecond. Setting this field to a
high value will accelerate the simulation, but will decrease the accuracy and
the stability, especially for physics computations and collision detection. It
is usually recommended to tune this value in order to find a suitable
speed/accuracy trade-off.
- The `FPS` (frames per second) field represents the maximum rate at which the 3D
display of the main window is refreshed in `Real-time` and `Run` mode. It is
particularly usefull to limit the refresh rate, in order to speed up simulations
having a small `basicTimeStep` value.
- The `optimalThreadCount` defines the actual number of threads used for the
computation of the physics of the world. Note that the value of this field can
not be higher than the value set for `Number of threads` in the *Preferences*.
Changing the value of this field can have a non-negligeable impact on the speed
of the simulation. For simulations involving several robots physically
independent from each other, setting a value greater than 1 can significantly
improve the speed of simulation. In other cases, it may however reduce the
simulation speed due to the overhead of the multi-threading.
- The `physicsDisableTime` determines the amount of simulation time (in seconds)
before the idle solids are automatically disabled from the physics computation.
Set this to zero to disable solids as soon as they become idle. This field
matchs directly with the `dBodySetAutoDisableTime` ODE function. This feature
can improve significantly the speed of the simulation if the solids are static
most of the time. The solids are enabled again after any interaction (collision,
movement, ...).
- The `physicsDisableLinearThreshold` determines the solid's linear velocity
threshold (in meter/seconds) for automatic disabling. The body's linear velocity
magnitude must be less than this threshold for it to be considered idle. This
field is only useful if `physicsDisableTime` is bigger or equal to zero. This
field matchs directly with the `dBodySetAutoDisableLinearThreshold` ODE
function.
- The `physicsDisableAngularThreshold` determines the solid's angular velocity
threshold (in radian/seconds) for automatic disabling. The body's angular
velocity magnitude must be less than this threshold for it to be considered
idle. This field is only useful if `physicsDisableTime` is bigger or equal to
zero. This field matchs directly with the `dBodySetAutoDisableAngularThreshold`
ODE function.
- The `defaultDamping` field allows to specifiy a [Damping](damping.md#damping)
node that defines the default damping parameters that must be applied to each
[Solid](solid.md#solid) in the simulation.
- If the `inkEvaporation` field is set to a non-null value, the colors of the
ground textures will slowly turn to white. This is useful on a white-textured
ground in conjunction with a [Pen](pen.md#pen) device, in order to have the
track drawn by the [Pen](pen.md#pen) device disappear progressively. The
`inkEvaporation` field should be a positive floating point value defining the
speed of evaporation. This evaporation process is a computationally expensive
task, hence the ground textures are updated only every `WorldInfo.basicTimeStep`
* `WorldInfo.displayRefresh` milliseconds (even in fast mode). Also, it is
recommended to use ground textures with low resolution to speed up this process.
As with the pen device, the modified ground textures can be seen only through
infra-red distance sensors, and not through cameras (as the ground textures are
not updated on the controller side).
- The `northDirection` field is used to indicate the direction of the *virtual
north* and is used by [Compass](compass.md#compass) and
[InertialUnit](inertialunit.md#inertialunit) nodes.
- The `lineScale` field allows the user to control the size of the optionally
rendered arbitrary-sized lines or objects such as the connector and the hinge
axes, the local coordinate systems and centers of mass of solid nodes, the rays
of light sensors, the point light representations, the camera frustums, or the
offsets used for drawing bounding objects and the laser beam. Increasing the
`lineScale` value can help in case of depth fighting problems between the red
spot of a laser beam and the detected object. The value of this field is somehow
arbitrary, but setting this value equal to the average size of a robot
(expressed in meter) is likely to be a good initial choice.
- The `contactProperties` field allows to specifiy a number of
[ContactProperties](contactproperties.md#contactproperties) nodes that define
the behavior when [Solid](solid.md#solid) nodes collide.

