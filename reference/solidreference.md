## SolidReference

```
SolidReference {
  field  SFString  solidName  "" # name of an existing solid or <static environment>
}
```

### Description

A `SolidReference` can be used inside the `endPoint` field of a `Joint` node to
refer either to an existing `Solid` or to the static environment. Mechanical
loops can be closed this way. The only constraint when referring to a `Solid` is
that both `Solid` and `Joint` must be descendants of a common upper `Solid`.

### Field Summary

- `solidName`: This field specifies either the static environment or the name of
an existing `Solid` node to be linked with the `Joint`'s closest upper `Solid`
node. Referring to the `Joint` closest upper `Solid` node or to a `Solid` node
which has no common upper `Solid` with the `Joint` is prohibited.

