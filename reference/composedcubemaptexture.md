## ComposedCubeMapTexture

```
ComposedCubeMapTexture {
  vrmlField SFNode right   NULL
  vrmlField SFNode left    NULL
  vrmlField SFNode top     NULL
  vrmlField SFNode bottom  NULL
  vrmlField SFNode front   NULL
  vrmlField SFNode back    NULL
}
```

### Description

The [ComposedCubeMapTexture](#composedcubemaptexture) node defines a cubic texture used for environment mapping.

Each of the six fields takes a texture corresponding to the side of the environment. For instance `right` takes the texture displayed on the side of the cube along the +X direction. Accordingly we have the following order, with the Z-axis pointing outwards: right:+X (0), left:-X (1), top:+Y (2), bottom:-Y (3), front:+Z (4), back:-Z (5).

The [ComposedCubeMapTexture](#composedcubemaptexture) is typically used together with a [ComposedShader](composedshader.md). It can be set to an Appearance's texture field on its own, or in conjunction with other textures inside a [MultiTexture](multitexture.md) node.


### Example

The following is an example of an environment mapping shader:

```
Shape {
  appearance Appearance {
    material Material {
    }
    texture ComposedCubeMapTexture {
      right ImageTexture {
        url [
          "textures/noon_cloudy_empty_right.jpg"
        ]
      }
      left ImageTexture {
        url [
          "textures/noon_cloudy_empty_left.jpg"
        ]
      }
      top ImageTexture {
        url [
          "textures/noon_cloudy_empty_top.jpg"
        ]
      }
      bottom ImageTexture {
        url [
          "textures/noon_cloudy_empty_bottom.jpg"
        ]
      }
      front ImageTexture {
        url [
          "textures/noon_cloudy_empty_front.jpg"
        ]
      }
      back ImageTexture {
        url [
          "textures/noon_cloudy_empty_back.jpg"
        ]
      }
    }
    shaders [
      ComposedShader {
        uniforms [
          Uniform {
            name "texCube"
            type "SFInt32"
            value "0"
          }
        ]
        parts [
          ShaderPart {
            type "VERTEX"
            content [
              "#version 120"
              ""
              "varying vec3 N;"
              "varying vec3 E;"
              ""
              "void main() {"
              "  E = gl_Vertex.xyz - vec3(gl_ModelViewMatrixInverse * vec4(0.,0.,0.,1.));"
              "  N = gl_Normal;"
              "  gl_Position = ftransform();"
              "}"
            ]
          }
          ShaderPart {
            type "FRAGMENT"
            content [
              "#version 120"
              ""
              "uniform samplerCube texCube;"
              ""
              "varying vec3 N;"
              "varying vec3 E;"
              ""
              "void main() {"
              "  vec3 eye = normalize(E);"
              "  vec3 n = normalize(N);"
              ""
              "  vec3 cubeCoord = reflect(eye, n);"
              ""
              "  gl_FragColor = vec4(textureCube(texCube, cubeCoord).rgb, 1.0);"
              "}"
            ]
          }
        ]
      }
    ]
  }
  geometry TeapotMesh {
  }
}
```