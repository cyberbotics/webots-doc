## TrackWheel

Derived from `Group`.


```
TrackWheel {
  SFVec2f    position          0 0
  SFFloat    radius            0.1
  SFBool     inner             TRUE
}
```

### Description

The `TrackWheel` node defines a wheel of a track system defined by a `Track`
node. The shape defined inside the `children` field of the `TrackWheel` node is
automatically rotated along the z-axis based on the speed of the parent `Track`
node. Additionally this node it is used by the parent `Track` node to compute
the track belt path used for geometries animation.

`TrackWheel` node can only be inserted in the `children` field of a `Track`
node.

### Field Summary

- `position`: defines the position of the wheel on the x-y plane of the `Track` node coordinate system.`radius`: defines the radius of the wheel.`inner`: defines if the wheel is inside the track belt.

