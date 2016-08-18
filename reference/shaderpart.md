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

**TODO**

### Special variables

**TODO**

### X3Dom export

**TODO**
