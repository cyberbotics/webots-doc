## Emitter

Derived from `Device`.


```
Emitter {
  SFString   type         "radio"  # or "serial" or "infra-red"
  SFFloat    range        -1       # -1 or positive
  SFFloat    maxRange     -1       # -1 or positive
  SFFloat    aperture     -1       # -1 or between 0 and 2*pi
  SFInt32    channel      0
  SFInt32    baudRate     -1       # -1 or positive
  SFInt32    byteSize     8        # 8 or more
  SFInt32    bufferSize   -1       # -1 or positive
}
```

### Description

The `Emitter` node is used to model radio, serial or infra-red emitters. An
`Emitter` node must be added to the children of a robot or a supervisor. Please
note that an emitter can send data but it cannot receive data. In order to
simulate a unidirectional communication between two robots, one robot must have
an `Emitter` while the other robot must have a `Receiver`. To simulate a
bidirectional communication between two robots, each robot needs to have both an
`Emitter` and a `Receiver`. Note that messages are never transmitted from one
robot to itself.

### Field Summary

### Emitter Functions

And here an example on how to send binary data with the C API:

