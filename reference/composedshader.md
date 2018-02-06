> **Note**: This node is experimental, i.e. its long-term support is not guaranteed.

## ComposedShader

```
ComposedShader {
  MFNode uniforms    [ ]
  MFNode parts       [ ]
  SFBool transparent FALSE
}
```

### Description

The [ComposedShader](#composedshader) node defines a shader as a list of vertex or fragment programs and the uniforms passed to these programs.

The `parts` field is a list of [ShaderPart](shaderpart.md) nodes.
Generally a [ShaderPart](shaderpart.md) node of type "VERTEX" and another of type "FRAGMENT" are expected.
If several [ShaderPart](shaderpart.md) nodes of the same type are given, then only the first occurrence of each type is used.

The `uniforms` field is a list of [Uniform](uniform.md) nodes corresponding to the uniform variables passed to the [ShaderPart](shaderpart.md) programs.

Webots provides a set of useful uniforms that can be invoked within a shader program and for which there is no need to add a [Uniform](uniform.md) field.
To use them, simply declare them as `uniform` in your shader.
For example, if you wish to perform calculations in world space, declare `uniform vec4 worldMatrix` and use the `worldMatrix` variable to transform elements from model to world space.

Here is a list of supported variables:

| type | name              | description                                                 |
|------|-------------------|-------------------------------------------------------------|
| mat4 | viewMatrix        | The matrix transformation from world space to camera space. |
| mat4 | viewMatrixInverse | The inverse transformation of viewMatrix.                   |
| mat4 | worldMatrix       | The matrix transformation from model space to world space.  |

The `transparent` field indicates if the shader will use the alpha channel.
If it is set to `FALSE` then the alpha channel will be ignored, and the [Shape](shape.md) node containing the [ComposedShader](#composedshader) will be rendered in the rendering queue of the opaque objects.
If it is set to `TRUE` then the alpha channel will be used, and the container [Shape](shape.md) node will be rendered in the rendering queue of the transparent objects.

### Limitations

- The [Shape](shape.md) nodes containing a [ComposedShader](#composedshader) node cannot receive shadows.
- The [Shape](shape.md) nodes containing a transparent [ComposedShader](#composedshader) node cannot cast shadows.

### Example

The following example is a shader blending two textures together and multiplying the result by the Material.diffuseColor field:

```
Shape {
  appearance Appearance {
    material Material {
      diffuseColor 0.9 0.7 0.9
    }
    texture MultiTexture {
      texture [
        ImageTexture {
          url [
            "textures/tagged_wall.jpg"
          ]
        }
        ImageTexture {
          url [
            "textures/stone.jpg"
          ]
        }
      ]
    }
    shaders [
      ComposedShader {
        uniforms [
          Uniform {
            name "myMixFactor"
            type "SFFloat"
            value "0.7"
          }
          Uniform {
            name "myTextureA"
            type "SFInt32"
            value "0"
          }
          Uniform {
            name "myTextureB"
            type "SFInt32"
            value "1"
          }
        ]
        parts [
          ShaderPart {
            type "VERTEX"
            content [
              "#version 120"
              ""
              "void main() {"
              "  gl_TexCoord[0] = gl_TextureMatrix[0] * gl_MultiTexCoord0;"
              "  gl_Position = ftransform();"
              "}"
            ]
          }
          ShaderPart {
            type "FRAGMENT"
            content [
              "#version 120"
              ""
              "uniform float myMixFactor;"
              "uniform sampler2D myTextureA;"
              "uniform sampler2D myTextureB;"
              ""
              "void main() {"
              "  vec4 textureColorA = texture2D(myTextureA, gl_TexCoord[0].st);"
              "  vec4 textureColorB = texture2D(myTextureB, gl_TexCoord[0].st);"
              "  vec4 materialColor = gl_FrontMaterial.diffuse;"
              "  gl_FragColor = materialColor * mix(textureColorA, textureColorB, myMixFactor);"
              "}"
            ]
          }
        ]
      }
    ]
  }
  geometry Cylinder {
  }
}
```
