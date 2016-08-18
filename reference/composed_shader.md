## ComposedShader

```
ComposedShader {
  vrmlField MFNode fields []
  vrmlField MFNode parts  []
}
```

### Description

The [ComposedShader](#composedshader) node defines a shader as a list of vertex or fragment programs and the fields passed to these programs.

The `parts` type is a list of [ShaderPart](shaderpart.md) nodes.
Generally a [ShaderPart](shaderpart.md) node of type "VERTEX" and another of type "FRAGMENT" are expected.
If several [ShaderPart](shaderpart.md) node of the same type are given, then only the last ones are used.

The `fields` type is a list of [Uniform](uniform.md) nodes corresponding to the uniform variables passed to the [ShaderPart](shaderpart.md) programs.

### Example

**TODO**

### Limitations

**TODO**
