## IndexedLineSet


```
IndexedLineSet {
  SFNode    coord        NULL
  MFInt32   coordIndex   []    # [-1,inf)
}
```

The `IndexedLineSet` node represents a 3D geometry formed by constructing
polylines from 3D vertices specified in the `coord` field. `IndexedLineSet` uses
the indices in its `coordIndex` field to specify the polylines by connecting
vertices from the `coord` field. An index of "-1" indicates that the current
polyline has ended and the next one begins. The last polyline may be (but does
not have to be) followed by a "-1". `IndexedLineSet` is specified in the local
coordinate system and is affected by the transformations of its ancestors.

The `coord` field specifies the 3D vertices of the line set and contains a
`Coordinate` node.

`IndexedLineSet`s are not lit, are not texture-mapped and they do not cast or
receive shadows. `IndexedLineSet`s cannot be use for collision detection
(boundingObject).

