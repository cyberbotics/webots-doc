## Group

```
Group {
  MFNode   children   []
}
```

Direct derived nodes: [Transform](transform.md).

A [Group](#group) node contains `children` nodes without introducing a new
transformation. It is equivalent to a [Transform](transform.md) node containing
an identity transform.

A [Group](#group) node may not contain subsequent [Solid](solid.md), device or
robot nodes.

