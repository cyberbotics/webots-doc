## Group

```
Group {
  MFNode   children   []
}
```

Direct derived nodes: [Transform](reference/transform.md#transform).

A [Group](reference/group.md#group) node contains `children` nodes without
introducing a new transformation. It is equivalent to a
[Transform](reference/transform.md#transform) node containing an identity
transform.

A [Group](reference/group.md#group) node may not contain subsequent
[Solid](reference/solid.md#solid), device or robot nodes.

