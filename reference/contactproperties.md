## ContactProperties


```
ContactProperties {
  SFString   material1           "default"
  SFString   material2           "default"
  MFFloat    coulombFriction     1          # [0,inf)
  SFVec2f    frictionRotation    0 0
  SFFloat    bounce              0.5        # [0,1]
  SFFloat    bounceVelocity      0.01       # (m/s)
  MFFloat    forceDependentSlip  0
  SFFloat    softERP             0.2
  SFFloat    softCFM             0.001
}
```

### Description

`ContactProperties` nodes define the contact properties to use in case of
contact between `Solid` nodes (or any node derived from `Solid`).
`ContactProperties` nodes are placed in the `contactProperties` field of the
`WorldInfo` node. Each `ContactProperties` node specifies the name of two
*materials* for which these `ContactProperties` are valid.

When two `Solid` nodes collide, a matching `ContactProperties` node is searched
in the `WorldInfo`.`contactProperties` field. A `ContactProperties` node will
match if its `material1` and `material2` fields correspond (in any order) to the
the `contactMaterial` fields of the two colliding `Solid`s. The values of the
first matching `ContactProperties` are applied to the contact. If no matching
node is found, default values are used. The default values are the same as those
indicated above.

### Field Summary

