## Compass

Derived from `Device`.


```
Compass {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute x-axis
  SFBool     yAxis          TRUE  # compute y-axis
  SFBool     zAxis          TRUE  # compute z-axis
  SFFloat    resolution     -1
}
```

### Description

A `Compass` node can be used to model a 1, 2 or 3-axis digital compass (magnetic
sensor). The `Compass` node returns a vector that indicates the direction of the
*virtual north*. The *virtual north* is specified by the `northDirection` field
in the `WorldInfo` node.

### Field Summary

### Compass Functions

