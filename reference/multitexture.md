## MultiTexture

```
MultiTexture {
  MFNode texture []   # {ImageTexture, ComposedCubeMapTexture, PROTO}
}
```

### Description

The [MultiTexture](#multitexture) node specifies the application of several individual textures to a 3D object to achieve a more complex visual effect.
[MultiTexture](#multitexture) can be used as a value for the texture field in an [Appearance](appearance.md) node.

It's particularly useful to pass several textures to a [ComposedShader](composedshader.md) node.

The `texture` field contains a list of texture nodes (i.e. [ImageTexture](imagetexture.md) and [ComposedCubeMapTexture](composedcubemaptexture.md)).
It may not contain another MultiTexture node.
