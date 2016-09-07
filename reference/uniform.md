## Uniform

```
Uniform {
  SFString name  ""
  SFString type  ""
  SFString value ""
}
```

### Description

The [Uniform](#uniform) node specifies a uniform named variable.
Uniform variables are used to pass variables to the vertex or fragment shaders
defined in the same [ComposedShader](composedshader.md) node.

The `name` field indicates the uniform variable name.

The `type` field indicates the uniform variable data type.

The `value` field indicates the uniform variable value.


### Supported types

The uniform variables support the following data types:

| Uniform type | GLSL type   | Value example |
| ============ | =========== | ============= |
| "SFInt32"    | `sampler2D` | "2"           |
| "SFFloat"    | `float`     | "1.2"         |
| "SFVec2f"    | `vec2`      | "1.2 2.3"     |
| "SFVec3f"    | `vec3`      | "1.2 2.3 3.4" |
