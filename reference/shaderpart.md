## ShaderPart

```
ShaderPart {
  SFString type    "" # either "VERTEX" or "FRAGMENT"
  MFString content ""
}
```

### Description

The [ShaderPart](#shaderpart) node defines a GPU program to be used by a [ComposedShader](composedshader.md) node.

The `type` field indicates whether this object shall be compiled as a vertex program or a fragment GPU program.
It can be respectively either "VERTEX" or "FRAGMENT".

The `content` field contains the source code of the GPU program.


### GPU program supported type and version

For a maximal compatibility range, `GLSL version 120` has been chosen
as the only supported shading language for now.


### GLSL 120 documentation

GLSL learning is beyond the scope of this document, please refer to the following sources:

1. Official sources
    - [The OpenGL® Shading Language](https://www.opengl.org/registry/doc/GLSLangSpec.Full.1.20.8.pdf)
    - [OpenGL® Shading Language (GLSL) - Quick Reference Guide](http://mew.cx/glsl_quickref.pdf)
2. Tutorials
    - [Lighthouse3d.com](http://www.lighthouse3d.com/tutorials/glsl-12-tutorial/)
3. Books
    - [GLSL Essentials by Jacobo Rodríguez](https://www.amazon.com/GLSL-Essentials-Jacobo-Rodr%C3%ADguez/dp/1849698007)


### Variables

All the standard GLSL variables are accessible from the GPU program (gl_Vertex, gl_ModelViewMatrix, etc.).
Please refer to their documentation.

The links between the VRML fields and these variables are various.
Some of them are is described in the following table:

| VRML field(s)                                       | GLSL variable                                            |
| =================================================== | ======================================================== |
| `Material.ambientIntensity * Material.diffuseColor` | `gl_FrontMaterial.ambient.rgb`                           |
| `Material.diffuseColor`                             | `gl_FrontMaterial.diffuse.rgb`                           |
| `Material.emissiveColor`                            | `gl_FrontMaterial.emissive.rgb`                          |
| `Material.shininess`                                | `gl_FrontMaterial.shininess`                             |
| `Material.specularColor`                            | `gl_FrontMaterial.specular.rgb`                          |
| `sum(Light.ambientIntensity * Light.color)`         | `gl_LightModel.ambient`                                  |
| `Light.color * Light.intensity`                     | `gl_LightSource[X].diffuse`                              |
| `Light.on`                                          | *An unlit light is not present in the light list*        |
| `[Point/Spot]Light.attenuation`                     | `gl_LightSource[X].*attenuation`                         |
| `[Point/Spot]Light.location`                        | `gl_LightSource[X].position`                             |
| `[Point/Spot]Light.radius`                          | *Not available*                                          |
| `DirectionLight.direction`                          | *Most approaching value:* `gl_LightSource[X].halfVector` |


### Special preprocessor variables

- `NUMBER_OF_LIGHTS` is an integer containing the number of lights affecting the material.
This constant is particularly useful to loop over the lights.


### X3Dom export

**TODO**
