## Damping

```
Damping {
    SFFloat   linear        0.2     # [0,1]
    SFFloat   angular       0.2     # [0,1]
}
```

### Description

A `Damping` node can be used to slow down a body (a `Solid` node with
`Physics`). The speed of each body is reduced by the specified amount (between
0.0 and 1.0) every second. A value of 0.0 means "no slowing down" and value of
1.0 means a "complete stop", a value of 0.1 means that the speed should be
decreased by 10 percent every second. Note that the behavior of this value on
the solid speeds is nonlinear: a linear damping of 0.99 is far to affect the
solids speeds as a linear damping of 1.0. A damped body will possibly come to
rest and become disabled depending on the values specified in `WorldInfo`.
Damping does not add any force in the simulation, it directly affects the
velocity of the body. The damping effect is applied after all forces have been
applied to the bodies. Damping can be used to reduce simulation instability.

> **note**: When several rigidly linked `Solid`s are merged (see `Physics`'s `solid merging`
section) damping values of the aggregate body are averaged over the volumes of
all `Solid` components. The volume of a `Solid` is the sum of the volumes of the
geometries found in its `boundingObject`; overlaps are not handled.

The `linear` field indicates the amount of damping that must be applied to the
body's linear motion. The `angular` field indicates the amount of damping that
must be applied to the body's angular motion. The linear damping can be used,
e.g., to slow down a vehicule by simulating air or water friction. The angular
damping can be used, e.g., to slow down the rotation of a rolling ball or the
spin of a coin. Note that the damping is applied regardless of the shape of the
object, so damping cannot be used to model complex fluid dynamics (use
`ImmersionProperties` and `Fluid` nodes instead).

A `Damping` node can be specified in the `defaultDamping` field of the
`WorldInfo` node; in this case it defines the default damping parameters that
must be applied to every body in the simulation. A `Damping` node can be
specified in the `damping` field of a `Physics` node; in this case it defines
the damping parameters that must be applied to the `Solid` that contains the
`Physics` node. The damping specified in a `Physics` node overrides the default
damping.

