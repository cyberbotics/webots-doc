## Shape

```
Shape {
  SFNode   appearance   NULL
  SFNode   geometry     NULL
}
```

The [Shape](#shape) node has two fields, `appearance` and `geometry`, which are
used to create rendered objects in the world. The `appearance` field contains an
[Appearance](#appearance) node that specifies the visual attributes (e.g.,
material and texture) to be applied to the geometry. The `geometry` field
contains a `Geometry` node: [Box](#box), [Capsule](#capsule), [Cone](#cone),
[Cylinder](#cylinder), [ElevationGrid](#elevationgrid),
[IndexedFaceSet](#indexedfaceset), [IndexedLineSet](#indexedlineset),
[Plane](#plane) or [Sphere](#sphere). The specified `Geometry` node is rendered
with the specified appearance nodes applied.

