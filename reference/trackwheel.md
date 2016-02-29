## TrackWheel

Derived from [Group](group.md#group).

```
TrackWheel {
  SFVec2f    position          0 0
  SFFloat    radius            0.1
  SFBool     inner             TRUE
}
```

### Description

The [TrackWheel](#trackwheel) node defines a wheel of a track system defined by
a [Track](track.md#track) node. The shape defined inside the `children` field of
the [TrackWheel](#trackwheel) node is automatically rotated along the z-axis
based on the speed of the parent [Track](track.md#track) node. Additionally this
node it is used by the parent [Track](track.md#track) node to compute the track
belt path used for geometries animation.

[TrackWheel](#trackwheel) node can only be inserted in the `children` field of a
[Track](track.md#track) node.

### Field Summary

- `position`: defines the position of the wheel on the x-y plane of the
[Track](track.md#track) node coordinate system.

    `radius`: defines the radius of the wheel.

    `inner`: defines if the wheel is inside the track belt.

