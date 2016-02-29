## SolidReference

```
SolidReference {
  field  SFString  solidName  "" # name of an existing solid or <static environment>
}
```

### Description

A [SolidReference](#solidreference) can be used inside the `endPoint` field of a
[Joint](joint.md#joint) node to refer either to an existing
[Solid](solid.md#solid) or to the static environment. Mechanical loops can be
closed this way. The only constraint when referring to a [Solid](solid.md#solid)
is that both [Solid](solid.md#solid) and [Joint](joint.md#joint) must be
descendants of a common upper [Solid](solid.md#solid).

### Field Summary

- `solidName`: This field specifies either the static environment or the name of
an existing [Solid](solid.md#solid) node to be linked with the
[Joint](joint.md#joint)'s closest upper [Solid](solid.md#solid) node. Referring
to the [Joint](joint.md#joint) closest upper [Solid](solid.md#solid) node or to
a [Solid](solid.md#solid) node which has no common upper [Solid](solid.md#solid)
with the [Joint](joint.md#joint) is prohibited.

