## Material


```
Material {
  SFFloat   ambientIntensity   0.2          # [0,1]
  SFColor   diffuseColor       0.8 0.8 0.8  # [0,1]
  SFColor   emissiveColor      0 0 0        # [0,1]
  SFFloat   shininess          0.2          # [0,1]
  SFColor   specularColor      0 0 0        # [0,1]
  SFFloat   transparency       0            # [0,1]
}
```

### Description

The `Material` node specifies surface material properties for associated
geometry nodes and is used by the VRML97 lighting equations during rendering.
The fields in the `Material` node determine how light reflects off an object to
create color.

### Field Summary

