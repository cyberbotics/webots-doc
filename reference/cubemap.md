## Cubemap

```
Cubemap {
  SFString  textureBaseName ""                 # any string
  SFString  directory       "textures/cubic"   # any string
}
```

### Description

The [Cubemap](#cubemap) node is a multi-purpose utility node for loading cubic textures.
In the case of the [Background](background.md) node,[Cubemap](#cubemap) nodes are used to create the world's skybox.
In the case of the [PBRAppearance](pbrappearance.md) node, they are used as part of the Image-Based Lighting stage of the Physically-Based Rendering pipeline, to generate realistic reflections and environmental ambient lighting.



### Field Summary

The `textureBaseName` field specifies the base name for the texture, without any suffix to designate the face of the cube to which it belongs, nor the file extension.

The `directory` field specifies the directory from which textures will be located and loaded.

In order to be easy and practical to use, URLs are forged using the two fields of the node.
Consequently, there is a strict pattern to follow for naming textures for each face.

The algorithm for loading faces can be described with the following pseudocode:

```cpp
textureSuffixes = {"_right", "_left", "_top", "_bottom", "_front", "_back"};

for (i = 0; i < 6; ++i) {
  textureUrl = directory + "/" + textureBaseName + textureSuffixes[i] + extension;
  loadImage(textureUrl);
}

```
Where `extension` will be either `.jpg` or `.png` and is automatically selected by the loading algorithm depending on what files it finds.

For example, the `textureBaseName` "noon\_sunny\_empty" and `directory` "textures/cubic" will generate these URLs:

```
textures/cubic/noon_sunny_empty_right.jpg
textures/cubic/noon_sunny_empty_left.jpg
textures/cubic/noon_sunny_empty_top.jpg
textures/cubic/noon_sunny_empty_bottom.jpg
textures/cubic/noon_sunny_empty_front.jpg
textures/cubic/noon_sunny_empty_back.jpg
```

then these textures are loaded according to the same image loading rules as the `url` field of the [ImageTexture](imagetexture.md#search-rule-of-the-texture-path) node.
