> **Note**: This node is experimental, i.e. its long-term support is not guaranteed.

## Uniform

```
Uniform {
  SFString name  ""   # any string
  SFString type  ""   # any string
  SFString value ""   # any string
}
```

### Description

The [Uniform](#uniform) node specifies a uniform named variable.
Uniform variables are used to pass variables to the vertex or fragment shaders defined in the same [ComposedShader](composedshader.md) node.

The `name` field indicates the uniform variable name.

The `type` field indicates the uniform variable data type.

The `value` field indicates the uniform variable value.

### Supported Data Types

The uniform variables support the following data types:

| Uniform type | GLSL type   | Value example |
| ============ | =========== | ============= |
| "SFInt32"    | `sampler2D` | "2"           |
| "SFFloat"    | `float`     | "1.2"         |
| "SFVec2f"    | `vec2`      | "1.2 2.3"     |
| "SFVec3f"    | `vec3`      | "1.2 2.3 3.4" |
