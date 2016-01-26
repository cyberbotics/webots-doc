## SolidReference


```
SolidReference {
  field  SFString  solidName  "" # name of an existing solid or ltstatic environmentgt
}
```

### Description

A `SolidReference` can be used inside the `endPoint` field of a `Joint` node to
refer either to an existing `Solid` or to the static environment. Mechanical
loops can be closed this way. The only constraint when referring to a `Solid` is
that both `Solid` and `Joint` must be descendants of a common upper `Solid`.

### Field Summary

