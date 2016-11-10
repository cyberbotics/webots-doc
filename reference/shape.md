## Shape

```
Shape {
  SFNode   appearance   NULL
  SFNode   geometry     NULL
  SFBool   castShadows  TRUE
}
```

### Description

The [Shape](#shape) node is used to create rendered objects in the world.
Visible objects are constituted by a geometry and an appearance.

### Field Summary

- The `appearance` field contains an [Appearance](appearance.md) node that
specifies the visual attributes (e.g., material and texture) to be applied to
the geometry.

- The `geometry` field contains a `Geometry` node: [Box](box.md),
[Capsule](capsule.md), [Cone](cone.md), [Cylinder](cylinder.md),
[ElevationGrid](elevationgrid.md), [IndexedFaceSet](indexedfaceset.md),
[IndexedLineSet](indexedlineset.md), [Plane](plane.md) or [Sphere](sphere.md).
The specified `Geometry` node is rendered with the specified appearance nodes
applied.

- The `castShadows` field allows the user to turn on (TRUE) or off (FALSE) shadows
casted by this shape.

> **Note**:
Objects cast shadows only if the world contains at least one [Light](light.md)
node with `castShadows` field set to TRUE and if shadows are not disabled in the
application preferences.
