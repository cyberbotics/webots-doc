## PBRAppearance

```
PBRAppearance {
  SFColor  baseColor            1 1 1             # any color
  SFNode   baseColorMap         NULL              # {ImageTexture, PROTO}
  SFFloat  transparency         0                 # [0, 1]
  SFFloat  roughness            0                 # [0, 1]
  SFNode   roughnessMap         NULL              # {ImageTexture, PROTO}
  SFFloat  metalness            1                 # [0, 1]
  SFNode   metalnessMap         NULL              # {ImageTexture, PROTO}
  SFNode   environmentMap       NULL              # {Cubemap, PROTO}
  SFFloat  IBLStrength          1                 # [0, inf)
  SFNode   normalMap            NULL              # {ImageTexture, PROTO}
  SFFloat  normalMapFactor      1                 # [0, inf)
  SFNode   occlusionMap         NULL              # {ImageTexture, PROTO}
  SFFloat  occlusionMapStrength 1                 # [0, inf)
  SFNode   textureTransform     NULL              # {TextureTransform, PROTO}
  SFString name                 "PBRAppearance"   # any string
}
```

### Description

The [PBRAppearance](#pbrappearance) node specifies the visual properties of a geometric node.
The value for each of the fields in this node may be NULL.
However, if the field is non-NULL, it shall contain one node of the appropriate type.


### Field Summary

- The `material` field, if specified, shall contain a [Material](material.md) node.
If the `material` field is NULL, lighting is off (all lights are ignored during the rendering of the object that references this [PBRAppearance](#pbrappearance)) and the unlit object color is (1,1,1).

- The `texture` field, if specified, shall contain an [ImageTexture](imagetexture.md) node.
If the `texture` node is NULL, the object that references this [PBRAppearance](#pbrappearance) is not textured.

- The `textureTransform` field, if specified, shall contain a [TextureTransform](texturetransform.md) node.
If the `textureTransform` is NULL, the `textureTransform` field has no effect.

- The `name` field specifies the pbrappearance name.
This is especially needed to uniquely identify the pbrappearance definition in MFNode fields supporting multiple [PBRAppearance](#pbrappearance) nodes.
In case of SFNode fields containing a single [PBRAppearance](#pbrappearance) node it is not necessary to define a unique name.
