## Group


```
Group {
  MFNode   children   []
}
```

Direct derived nodes: `Transform`.

A `Group` node contains `children` nodes without introducing a new
transformation. It is equivalent to a `Transform` node containing an identity
transform.

A `Group` node may not contain subsequent `Solid`, device or robot nodes.

