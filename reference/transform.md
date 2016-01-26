## Transform

Derived from `Group`.


```
Transform {
  SFVec3f      translation   0 0 0     # 3D vector
  SFRotation   rotation      0 1 0 0   # 3D unit vector,angle (rad)
  SFVec3f      scale         1 1 1     # 3 real scaling factors
}
```

Direct derived nodes: `Solid`.

### Description

The `Transform` node is a grouping node that defines a coordinate system for its
children that is relative to the coordinate systems of its parent.

### Field Summary

