## Procedural PROTO nodes

The expressive power of PROTO nodes can be significantly improved by extending
them using a scripting language. In this way, the PROTO node may contain
constants, mathematic expressions, loops, conditional expressions, randomness,
and so on.

### Scripting language

The used scripting language is `Lua`. Introducing and learning Lua is outside
the scope of this document. Please refer to the `Lua documentation` for
complementary information.

### Template Engine

A template engine is used to evaluate the PROTO according to the fields values
of the PROTO, before being loaded in Webots. The template engine used is `slt2`
(under the MIT license).

### Programming Facts

### Example


```

#VRML_SIM V8.1.0 utf8

PROTO SimpleStairs [
  field SFVec3f    translation 0 0 0
  field SFRotation rotation    0 1 0 0
  field SFInt32    nSteps      10
  field SFVec3f    stepSize    0.2 0.2 0.8
  field SFNode     appearance  NULL
]
{
  # template statements can be used from here
  %{
    -- a template statement can be written on several lines
    if fields.nSteps.value lt 1 then
      print('nSteps should be strictly positive')
    end
    
    -- print the path to this proto
    print(context.proto)
    
    if fields.stepSize.value ~= fields.stepSize.defaultValue then
      print('The step size used is not the default one')
    end

    -- print the first texture url of the ImageTexture node
    -- inside the Appearance node
    if fields.appearance.value and fields.appearance.value.fields.texture.value then
      -- The following test is true: fields.appearance.value.fields.texture.value.node_name == "ImageTexture"
      print (fields.appearance.value.fields.texture.value.url[0])
    end
  }%
  Solid {
    translation IS translation
    rotation IS rotation
    children [
      DEF SIMPLE_STAIRS_GROUP Group {
        children [
        %{ for i = 0, (fields.nSteps.value - 1) do }%
          %{ x = i * fields.stepSize.value.x }%
          %{ y = i * fields.stepSize.value.y + fields.stepSize.value.y / 2 }%
            Transform {
              translation %{=x}% %{=y}% 0
              children [
                Shape {
                  appearance IS appearance
                  geometry Box {
                    size IS stepSize
                  }
                }
              ]
            }
          %{ end }%
        ]
      }
    ]
    boundingObject USE SIMPLE_STAIRS_GROUP
  }
  # template statements can be used up to there
}
     
```

