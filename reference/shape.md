## Shape

```
Shape {
  SFNode   appearance   NULL
  SFNode   geometry     NULL
}
```

The [Shape](reference/shape.md#shape) node has two fields, `appearance` and
`geometry`, which are used to create rendered objects in the world. The
`appearance` field contains an [Appearance](reference/appearance.md#appearance)
node that specifies the visual attributes (e.g., material and texture) to be
applied to the geometry. The `geometry` field contains a `Geometry` node:
[Box](reference/box.md#box), [Capsule](reference/capsule.md#capsule),
[Cone](reference/cone.md#cone), [Cylinder](reference/cylinder.md#cylinder),
[ElevationGrid](reference/elevationgrid.md#elevationgrid),
[IndexedFaceSet](reference/indexedfaceset.md#indexedfaceset),
[IndexedLineSet](reference/indexedlineset.md#indexedlineset),
[Plane](reference/plane.md#plane) or [Sphere](reference/sphere.md#sphere). The
specified `Geometry` node is rendered with the specified appearance nodes
applied.

