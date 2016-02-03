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

- `lookupTable`: This field optionally specifies a lookup table that can be used for mapping each vector component (between -1.0 and +1.0) to device specific output values. With the lookup table it is also possible to add noise and to define min and max output values. By default the lookup table is empty and therefore no mapping is applied.
- `xAxis, yAxis, zAxis`: Each of these boolean fields specifies if the computation should be enabled or disabled for the specified axis. If one of these fields is set to FALSE, then the corresponding vector element will not be computed and it will return *NaN* (Not a Number). For example if zAxis is FALSE, then calling wb_compass_get_values()[2] will always return *NaN*. The default is that all three axes are enabled (TRUE). Modifying these fields makes it possible to choose between a single, dual or a three-axis digital compass and to specify which axes will be used.
- `resolution`: This field allows to define the resolution of the sensor, the resolution is the smallest change that it is able to measure. Setting this field to -1 (default) means that the sensor has an 'infinite' resolution (it can measure any infinitesimal change). This field accepts any value in the interval (0.0, inf).

### Compass Functions

