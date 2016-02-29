## Group

```
Group {
  MFNode   children   []
}
```

Direct derived nodes: [Transform](transform.md#transform).

A [Group](group.md#group) node contains `children` nodes without introducing a
new transformation. It is equivalent to a [Transform](transform.md#transform)
node containing an identity transform.

A [Group](group.md#group) node may not contain subsequent
[Solid](solid.md#solid), device or robot nodes.

