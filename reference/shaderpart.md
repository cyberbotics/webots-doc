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

For a maximal compatibility range, `GLSL version 120` has been chosen
as the only supported shading language for now.


### GLSL 120 documentation

GLSL learning is beyond the scope of this document, please refer to the following sources:

1. Official sources
    - [The OpenGL® Shading Language](https://www.opengl.org/registry/doc/GLSLangSpec.Full.1.20.8.pdf)
    - [OpenGL® Shading Language (GLSL) - Quick Reference Guide](http://mew.cx/glsl_quickref.pdf)
2. Tutorials
    - [Lighthouse3d.com](http://www.lighthouse3d.com/tutorials/glsl-12-tutorial/)
3. Books
    - [GLSL Essentials by Jacobo Rodríguez](https://www.amazon.com/GLSL-Essentials-Jacobo-Rodr%C3%ADguez/dp/1849698007)


### Variables

**TODO**


### Special variables

**TODO**


### X3Dom export

**TODO**
