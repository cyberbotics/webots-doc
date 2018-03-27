# Plants

## BunchOfSunFlowers

Five sun flowers into a pot (0.17 x 0.95 x 0.17 m).

Derived from [Solid](../reference/solid.md).

%figure

![BunchOfSunFlowers](images/objects/plants/BunchOfSunFlowers/model.png)

%end

```
BunchOfSunFlowers {
  SFVec3f    translation            0 0 0
  SFRotation rotation               0 1 0 0
  SFString   name                   "bunch of sunflowers"
  SFColor    potAndSteamsColor      1 1 1
  MFString   potAndSteamsTextureUrl "textures/bunch_of_sun_flowers_pot_and_steams.jpg"
  SFColor    flowerColor            1 1 1
  MFString   flowerTextureUrl       "textures/bunch_of_sun_flowers_flower.png"
  SFColor    leavesColor            1 1 1
  MFString   leavesTextureUrl       "textures/bunch_of_sun_flowers_leaves.png"
  SFNode     physics                NULL
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/plants/protos/BunchOfSunFlowers.proto"

### BunchOfSunFlowers Field Summary

- `potAndSteamsColor`: Defines the color of the pot and the steams.

- `potAndSteamsTextureUrl`: Defines the textures used for the pot and the steams.

- `flowerColor`: Defines the color of the flowers.

- `flowerTextureUrl`: Defines the textures used for the flowers.

- `leavesColor`: Defines the color of the leaves.

- `leavesTextureUrl`: Defines the textures used for the leaves.

- `physics`: Is equivalent to the `physics` field of the [Solid](../reference/solid.md) node.

## PottedTree

A potted tree (0.3 x 1.3 x 0.3 m).

Derived from [Solid](../reference/solid.md).

%figure

![PottedTree](images/objects/plants/PottedTree/model.png)

%end

```
PottedTree {
  SFVec3f    translation          0 0 0
  SFRotation rotation             0 1 0 0
  SFString   name                 "potted tree"
  SFColor    potAndTreeColor      1 1 1
  MFString   potAndTreeTextureUrl "textures/potted_tree_pot_and_tree.jpg"
  SFColor    leavesColor          1 1 1
  MFString   leavesTextureUrl     "textures/potted_tree_leaves.png"
  SFNode     physics              NULL
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/plants/protos/PottedTree.proto"

### PottedTree Field Summary

- `potAndTreeColor`: Defines the color of the pot and the three.

- `potAndTreeTextureUrl`: Defines the textures used for of the pot and the three.

- `leavesColor`: Defines the color of the leaves.

- `leavesTextureUrl`: Defines the textures used for of the leaves.

- `physics`: Is equivalent to the `physics` field of the [Solid](../reference/solid.md) node.

