## SolidReference

```
SolidReference {
  field  SFString  solidName  "" # name of an existing solid or <static environment>
}
```

### Description

A [SolidReference](#solidreference) can be used inside the `endPoint` field of a
[Joint](#joint) node to refer either to an existing [Solid](#solid) or to the
static environment. Mechanical loops can be closed this way. The only constraint
when referring to a [Solid](#solid) is that both [Solid](#solid) and
[Joint](#joint) must be descendants of a common upper [Solid](#solid).

### Field Summary

- `solidName`: This field specifies either the static environment or the name of
an existing [Solid](#solid) node to be linked with the [Joint](#joint)'s closest
upper [Solid](#solid) node. Referring to the [Joint](#joint) closest upper
[Solid](#solid) node or to a [Solid](#solid) node which has no common upper
[Solid](#solid) with the [Joint](#joint) is prohibited.

