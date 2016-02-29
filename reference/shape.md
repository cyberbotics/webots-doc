## Shape

```
Shape {
  SFNode   appearance   NULL
  SFNode   geometry     NULL
}
```

The [Shape](#shape) node has two fields, `appearance` and `geometry`, which are
used to create rendered objects in the world. The `appearance` field contains an
[Appearance](appearance.md#appearance) node that specifies the visual attributes
(e.g., material and texture) to be applied to the geometry. The `geometry` field
contains a `Geometry` node: [Box](box.md#box), [Capsule](capsule.md#capsule),
[Cone](cone.md#cone), [Cylinder](cylinder.md#cylinder),
[ElevationGrid](elevationgrid.md#elevationgrid),
[IndexedFaceSet](indexedfaceset.md#indexedfaceset),
[IndexedLineSet](indexedlineset.md#indexedlineset), [Plane](plane.md#plane) or
[Sphere](sphere.md#sphere). The specified `Geometry` node is rendered with the
specified appearance nodes applied.

