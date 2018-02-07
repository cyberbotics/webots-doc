> **Note**: This node is experimental, i.e. its long-term support is not guaranteed.

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

For a maximal compatibility range, `GLSL version 120` has been chosen as the only supported shading language for now.

### GLSL 120 documentation

The GLSL documentation is available from following sources:

1. Official sources
    - [The OpenGL® Shading Language](https://www.opengl.org/registry/doc/GLSLangSpec.Full.1.20.8.pdf)
    - [OpenGL® Shading Language (GLSL) - Quick Reference Guide](http://mew.cx/glsl_quickref.pdf)
2. Tutorials
    - [Lighthouse3d.com](http://www.lighthouse3d.com/tutorials/glsl-12-tutorial/)
3. Books
    - [GLSL Essentials by Jacobo Rodríguez](https://www.amazon.com/GLSL-Essentials-Jacobo-Rodr%C3%ADguez/dp/1849698007)

### Variables

All the standard GLSL variables are accessible from the GPU program (`gl_Vertex`, `gl_ModelViewMatrix`, etc.).
Please refer to their documentation.

The links between the VRML97 fields and these variables are various.
Some of them are described in the following table:

| VRML97 field(s)                                      | GLSL variable                                                   |
| ---------------------------------------------------- | --------------------------------------------------------------- |
| `Material.ambientIntensity * Material.diffuseColor`  | `gl_FrontMaterial.ambient.rgb`                                  |
| `Material.diffuseColor`                              | `gl_FrontMaterial.diffuse.rgb`                                  |
| `Material.emissiveColor`                             | `gl_FrontMaterial.emissive.rgb`                                 |
| `Material.shininess`                                 | `gl_FrontMaterial.shininess / 128.0`                            |
| `Material.specularColor`                             | `gl_FrontMaterial.specular.rgb`                                 |
| `sum(Light.ambientIntensity * Light.color)`          | `gl_LightModel.ambient`                                         |
| `Light.color * Light.intensity`                      | `gl_LightSource[X].diffuse`                                     |
| `Light.on`                                           | *An unlit light is simply not in the light list*                |
| `[Point/Spot/Directional]Light` (type determination) | `gl_LightSource[X].position.w` + `gl_LightSource[i].spotCutoff` |
| `[Point/Spot]Light.attenuation`                      | `gl_LightSource[X].*attenuation`                                |
| `[Point/Spot]Light.location`                         | `gl_LightSource[X].position`                                    |
| `[Point/Spot]Light.radius`                           | *Not available*                                                 |
| `DirectionalLight.direction`                         | `gl_LightSource[X].position`                                    |

### Special preprocessor variables

- `NUMBER_OF_LIGHTS` is an integer containing the number of lights affecting the material.
This constant is particularly useful to loop over the lights.
- `FOG_TYPE` is an integer matching with the current fog type:
    - `0` stands for no fog
    - `1` stands for an exponential fog
    - `2` stands for an exponential2 fog
    - `3` stands for a linear fog

### X3DOM export

When exporting the GLSL shader to X3DOM, the shader is converted from `GLSL v120` to the `X3DOM` shaders (`WebGL` shaders with custom variables).
Generally this automatic conversion is working fine, however if you suspect a wrong behavior, please write a bug report to help us improving the conversion function.

#### Known differences

- **Lights order**: In Webots the lights list is sorted by the distance between the lights and the target object,
while in `X3DOM` the list is simply sorted by the Light node definition order.
So it's recommended to deal the lights in a generic way.
