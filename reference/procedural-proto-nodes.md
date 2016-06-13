## Procedural PROTO nodes

The expressive power of PROTO nodes can be significantly improved by extending
them using a scripting language. In this way, the PROTO node may contain
constants, mathematic expressions, loops, conditional expressions, randomness,
and so on.

### Scripting language

The used scripting language is [Lua](http://www.lua.org). Introducing and
learning Lua is outside the scope of this document. Please refer to the [Lua
documentation](http://www.lua.org/docs.html) for complementary information.

### Template Engine

A template engine is used to evaluate the PROTO according to the fields values
of the PROTO, before being loaded in Webots. The template engine used is
[slt2](https://github.com/henix/slt2) (under the MIT license).

### Programming Facts

- Using the template statements is exclusively allowed inside the content scope of
the PROTO (cf. example).
- A template statement is encapsulated inside the "%{" and the "}%" tokens and can
be written on several lines.
- Adding an "=" just after the opening token ("%{=") allows to evaluate a
statement.
- The fields are accessible into a global Lua dictionary named "fields". The
dictionary keys matches the PROTO's fields names. Each entry of this dictionary
is a sub-dictionary with two keys named "value" and "defaultValue", the first
one contains the current state of the field and the second one contains its the
default state. The conversion between the VRML types and the Lua types is
detailed in [this table](#vrml-type-to-lua-type-conversion).
- As shown in [this table](#vrml-type-to-lua-type-conversion), the conversion of a
VRML node is a Lua dictionary. This dictionary contains the following keys:
"node\_name" containing the VRML node name, "fields" which is a dictionary
containing the Lua representation of the VRML node fields, and "super" which can
contains the super PROTO node (the node above in the hierarchy) if existing.
This dictionary is equal to `nil` if the VRML node is not defined (`NULL`). For
example, in the SimpleStairs example below, the `fields.appearance.node_name`
key contains the `'Appearance'` string.
- The `context` dictionary provides contextual information about the PROTO. Table
[this table](#content-of-the-context-dictionary) shows the available information
and its corresponding keys.
- The VRML comment ("#") prevails over the Lua statements.
- The following Lua modules are availble directly: base, table, io, os, string,
math, debug, package.
- The LUA\_PATH environment variable can be modified (before running Webots) to
include external Lua modules.
- Lua standard output and error streams are redirected on the Webots console
(written respectively in regular and in red colors). This allows developers to
use the Lua regular functions to write on these streams.

%figure "VRML type to Lua type conversion"

| VRML type  | Lua type                                              |
| ---------- | ----------------------------------------------------- |
| SFBool     | boolean                                               |
| SFInt32    | number                                                |
| SFFloat    | number                                                |
| SFString   | string                                                |
| SFVec2f    | dictionary (keys = "x" and "y")                       |
| SFVec3f    | dictionary (keys = "x", "y" and "z")                  |
| SFRotation | dictionary (keys = "x", "y", "z" and "a")             |
| SFColor    | dictionary (keys = "r", "g" and "b")                  |
| SFNode     | dictionary (keys = "node\_name", "fields"[, "super"]) |
| MF*        | array (indexes = multiple value positions)            |

%end

%figure "Content of the context dictionary"

| Key             | Value                                                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| world           | absolute path to the current world file (including file name and extension)                                                          |
| proto           | absolute path to the current PROTO file (including file name and extension)                                                          |
| project\_path   | absolute path to the current project directory                                                                                       |
| webots\_version | dictionary representing the version of Webots with which the PROTO is currently used (dictionary keys: major, minor and maintenance) |
| webots\_home    | absolute path to the Webots installation directory                                                                                   |

%end

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
    if fields.nSteps.value < 1 then
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
