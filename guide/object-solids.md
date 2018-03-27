# Solids

## SolidBox

Derived from [Solid](../reference/solid.md)

%figure "A box object implemented at the Solid-node level.
The box has similar properties as the VRML Box node in term of axis and fields.
The UV-mapping is defined in a metric way (the textures are not deformed - the reference is the longest edge).
The subdivision field allows to divide the faces into multiple quads (useful mainly for simple renderings).
"

![SolidBox](images/objects/solids/SolidBox/model.png)

%end

```
SolidBox {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "box"
  SFVec3f    size            2 2 2                                                                                             
  SFInt32    subdivision     8                                                                                                 
  SFString   contactMaterial "default"                                                                                         
  SFNode     appearance      Appearance { material Material { } texture ImageTexture { url [ "textures/tagged_wall.jpg" ] } }  
  SFNode     physics         NULL                                                                                              
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/solids/protos/SolidBox.proto"

### SolidBox Field Summary

- `size`: Defines the size of the box.

- `subdivision`: Defines the number of polygons used to represent the box and so its resolution.

- `contactMaterial`: Is equivalent to the `contactMaterial` field of the [Solid](../reference/solid.md) node.

- `appearance`: Defines the appearance of the box.

- `physics`: Is equivalent to the `physics` field of the [Solid](../reference/solid.md) node.

## SolidPipe

Derived from [Solid](../reference/solid.md)

%figure "A pipe object implemented at the Solid-node level.
Graphically, the SolidPipe is an IndexedFaceSet.
Physically, the SolidPipe is a set of N boxes, where N is the subdivision field.
The 'accuracy' field defines how much boxes position can differ on y axis: a 0 value represents an error-free model but it will slow down the simulation.
"

![SolidPipe](images/objects/solids/SolidPipe/model.png)

%end

```
SolidPipe {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "pipe"
  SFFloat    height          2                                                                                                 
  SFFloat    radius          1                                                                                                 
  SFFloat    thickness       0.1                                                                                               
  SFInt32    subdivision     24                                                                                                
  SFFloat    accuracy        0.0001                                                                                            
  SFString   contactMaterial "default"                                                                                         
  SFNode     appearance      Appearance { material Material { } texture ImageTexture { url [ "textures/tagged_wall.jpg" ] } }  
  SFNode     physics         NULL                                                                                              
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/solids/protos/SolidPipe.proto"

### SolidPipe Field Summary

- `height`: Defines the height of the pipe.

- `radius`: Defines the radius of the pipe.

- `thickness`: Defines the thickness of the pipe.

- `subdivision`: Defines the number of polygons used to represent the pipe and so its resolution.

- `accuracy`: Defines how much boxes position can differ on y axis: a 0 value represents an error-free model but it will slow down the simulation.

- `contactMaterial`: Is equivalent to the `contactMaterial` field of the [Solid](../reference/solid.md) node.

- `appearance`: Defines the appearance of the box.

- `physics`: Is equivalent to the `physics` field of the [Solid](../reference/solid.md) node.

## SolidRoundedBox

Derived from [Solid](../reference/solid.md)

%figure "A box object with rounded corners and edges implemented at the Solid-node level.
The box has similar properties as the VRML Box node in term of axis and fields.
"

![SolidRoundedBox](images/objects/solids/SolidRoundedBox/model.png)

%end

```
SolidRoundedBox {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "rounded box"
  SFVec3f    size            2 2 2                                                                                             
  SFFloat    borderRadius    0.5                                                                                               
  SFInt32    subdivision     24                                                                                                
  SFString   contactMaterial "default"                                                                                         
  SFNode     appearance      Appearance { material Material { } texture ImageTexture { url [ "textures/tagged_wall.jpg" ] } }  
  SFNode     physics         NULL                                                                                              
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/solids/protos/SolidRoundedBox.proto"

### SolidRoundedBox Field Summary

- `size`: Defines the size of the box.

- `borderRadius`: Defines the radius of the box borders.

- `subdivision`: Defines the number of polygons used to represent the box and so its resolution.

- `contactMaterial`: Is equivalent to the `contactMaterial` field of the [Solid](../reference/solid.md) node.

- `appearance`: Defines the appearance of the box.

- `physics`: Is equivalent to the `physics` field of the [Solid](../reference/solid.md) node.

## SolidTorus

Derived from [Solid](../reference/solid.md)

%figure "A torus object implemented at the Solid-node level.
Graphically, the SolidTorus is defined as an IndexedFaceSet.
Physically, the SolidTorus is defined as a set of N spheres, where N is the subdivision field.
"

![SolidTorus](images/objects/solids/SolidTorus/model.png)

%end

```
SolidTorus {
  SFVec3f    translation     0 0 0
  SFRotation rotation        0 1 0 0
  SFString   name            "torus"
  SFFloat    majorRadius     2                                                                                                 
  SFFloat    minorRadius     1                                                                                                 
  SFInt32    subdivision     24                                                                                                
  SFString   contactMaterial "default"                                                                                         
  SFNode     appearance      Appearance { material Material { } texture ImageTexture { url [ "textures/tagged_wall.jpg" ] } }  
  SFNode     physics         NULL                                                                                              
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/solids/protos/SolidTorus.proto"

### SolidTorus Field Summary

- `majorRadius`: Defines the major radius of the torus.

- `minorRadius`: Defines the minor radius of the torus.

- `subdivision`: Defines the number of polygons used to represent the torus and so its resolution.

- `contactMaterial`: Is equivalent to the `contactMaterial` field of the [Solid](../reference/solid.md) node.

- `appearance`: Defines the appearance of the torus.

- `physics`: Is equivalent to the `physics` field of the [Solid](../reference/solid.md) node.

