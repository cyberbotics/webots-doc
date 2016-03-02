## Shape

```
Shape {
  SFNode   appearance   NULL
  SFNode   geometry     NULL
}
```

The [Shape](#shape) node has two fields, `appearance` and `geometry`, which are
used to create rendered objects in the world. The `appearance` field contains an
[Appearance](appearance.md) node that specifies the visual attributes (e.g.,
material and texture) to be applied to the geometry. The `geometry` field
contains a `Geometry` node: [Box](box.md), [Capsule](capsule.md),
[Cone](cone.md), [Cylinder](cylinder.md), [ElevationGrid](elevationgrid.md),
[IndexedFaceSet](indexedfaceset.md), [IndexedLineSet](indexedlineset.md),
[Plane](plane.md) or [Sphere](sphere.md). The specified `Geometry` node is
rendered with the specified appearance nodes applied.

