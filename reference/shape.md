## Shape

```
Shape {
  SFNode   appearance   NULL
  SFNode   geometry     NULL
}
```

The `Shape` node has two fields, `appearance` and `geometry`, which are used to
create rendered objects in the world. The `appearance` field contains an
`Appearance` node that specifies the visual attributes (e.g., material and
texture) to be applied to the geometry. The `geometry` field contains a
`Geometry` node: `Box`, `Capsule`, `Cone`, `Cylinder`, `ElevationGrid`,
`IndexedFaceSet`, `IndexedLineSet`, `Plane` or `Sphere`. The specified
`Geometry` node is rendered with the specified appearance nodes applied.

