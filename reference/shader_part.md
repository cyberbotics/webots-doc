## ShaderPart

```
ShaderPart {
  SFString type    "" # either "VERTEX" or "FRAGMENT"
  MFString content ""
}
```

### Description

The [ShaderPart](#shaderpart) node specifies a GPU program.

The `type` field indicates whether this object shall be compiled as a vertex shader or a fragment shader.
It can be respectively either "VERTEX" or "FRAGMENT".

The `content` field contains the source code of the GPU program.
