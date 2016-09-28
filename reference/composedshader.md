## ComposedShader

```
ComposedShader {
  vrmlField MFNode uniforms []
  vrmlField MFNode parts  []
}
```

### Description

The [ComposedShader](#composedshader) node defines a shader as a list of vertex or fragment programs and the uniforms passed to these programs.

The `parts` field is a list of [ShaderPart](shaderpart.md) nodes.
Generally a [ShaderPart](shaderpart.md) node of type "VERTEX" and another of type "FRAGMENT" are expected.
If several [ShaderPart](shaderpart.md) nodes of the same type are given, then only the first occurrence of each type is used.

The `uniforms` field is a list of [Uniform](uniform.md) nodes corresponding to the uniform variables passed to the [ShaderPart](shaderpart.md) programs.


### Limitations

Currently the [Shape](shape.md) nodes having a [ComposedShader](#composedshader) cannot receive shadows.


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
