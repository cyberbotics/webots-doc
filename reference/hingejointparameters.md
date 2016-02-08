## HingeJointParameters

Derived from `JointParameters`.


```
HingeJointParameters {
  field SFVec3f anchor                    0 0 0 # for the rotation axis (m)
  # the following field have different default values than the parent class
  field SFVec3f axis                      1 0 0 # rotation axis
  field SFFloat suspensionSpringConstant  0     # linear spring constant along the suspension axis (Ns/m)
  field SFFloat suspensionDampingConstant 0     # linear damping constant along the suspension axis (Ns/m)
  field SFVec3f suspensionAxis            1 0 0 # direction of the suspension axis
}

```

### Description

The `HingeJointParameters` node can be used to specify the hinge rotation axis
and various joint parameters (e.g., angular position, stop angles, spring and
damping constants etc.) related to this rotation axis.

### Field Summary

- `anchor`: This field specifies the anchor position, i.e. a point through which
the hinge axis passes. Together with the `axis` field inherited from the
`JointParameters` node, the `anchor` field determines the hinge rotation axis in
a unique way. It is expressed in relative coordinates with respect to the the
closest upper `Solid`'s frame.
- `suspensionSpringConstant`: This field specifies the suspension spring constant
along the suspension axis.
- `suspensionDampingConstant`: This field specifies the suspension damping
constant along the suspension axis.
- `suspensionAxis`: This field specifies the direction of the suspension axis.

The `suspensionSpringConstant` and `suspensionDampingConstant` fields can be
used to add a linear spring and/or damping behavior *along* the axis defined in
`suspensionAxis`. These fields are described in more detail in
`JointParameters`'s Springs and Dampers" section.

