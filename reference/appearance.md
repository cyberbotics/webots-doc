## Appearance

```
Appearance {
  SFNode   material           NULL
  SFNode   texture            NULL
  SFNode   textureTransform   NULL
  SFString name               "appearance"
}
```

### Description

The [Appearance](#appearance) node specifies the visual properties of a
geometric node. The value for each of the fields in this node may be NULL.
However, if the field is non-NULL, it shall contain one node of the appropriate
type.

### Field Summary

- The `material` field, if specified, shall contain a [Material](material.md)
node. If the `material` field is NULL or unspecified, lighting is off (all
lights are ignored during rendering of the object that references this
[Appearance](#appearance)) and the unlit object color is (1,1,1).

- The `texture` field, if specified, shall contain an
[ImageTexture](imagetexture.md) node. If the `texture` node is NULL or the
`texture` field is unspecified, the object that references this
[Appearance](#appearance) is not textured.

- The `textureTransform` field, if specified, shall contain a
[TextureTransform](texturetransform.md) node. If the `textureTransform` is NULL
or unspecified, the `textureTransform` field has no effect.

- The `name` field specifies appearance name.
This is especially needed to uniquely identify the appearance definition in MFNode fields supporting multiple Appearance nodes.
In case of SFNode fields containing a single Appearance node it is not necessary to define a unique name.
