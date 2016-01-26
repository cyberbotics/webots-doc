## ImmersionProperties


```
ImmersionProperties {
  field SFString   fluidName       ""
  field SFString   referenceArea   "immersed area"
  field SFVec3f    dragForceCoefficients  0 0 0 # dimensionless coefficient ranging in [0, infinity)
  field SFVec3f    dragTorqueCoefficients  0 0 0 # dimensionless coefficients ranging in [0, infinity)
  field SFFloat    viscousResistanceForceCoefficient  0 # (Ns/m) ranges in [0, infinity)
  field SFFloat    viscousResistanceTorqueCoefficient  0 # (Nm/s ) ranges in [0, infinity)
}
```

### Description

An `ImmersionProperties` node is used inside the `immersionProperties` field of
a `Solid` node to specify its dynamical interactions with one or more `Fluid`
nodes.

### ImmersionProperties Fields

