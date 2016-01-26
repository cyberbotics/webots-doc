## Accelerometer

Derived from `Device`.


```
Accelerometer {
  MFVec3f    lookupTable    []    # interpolation
  SFBool     xAxis          TRUE  # compute x-axis
  SFBool     yAxis          TRUE  # compute y-axis
  SFBool     zAxis          TRUE  # compute z-axis
  SFFloat    resolution     -1
}
```

### Description

The `Accelerometer` node can be used to model accelerometer devices such as
those commonly found in mobile electronics, robots and game input devices. The
`Accelerometer` node measures acceleration and gravity induced reaction forces
over 1, 2 or 3 axes. It can be used for example to detect fall, the up/down
direction, etc.

### Field Summary

### Accelerometer Functions

