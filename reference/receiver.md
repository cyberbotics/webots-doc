## Receiver

Derived from `Device`.


```
Receiver {
  SFString  type                "radio"  # or "serial" or "infra-red"
  SFFloat   aperture            -1       # -1 or [0,2pi]
  SFInt32   channel             0        # [-1,inf)
  SFInt32   baudRate            -1       # -1 or [0,inf)
  SFInt32   byteSize            8        # [8,inf)
  SFInt32   bufferSize          -1       # -1 or [0,inf)
  SFFloat   signalStrengthNoise 0        # [0,inf)
  SFFloat   directionNoise      0        # [0,inf)
}
```

### Description

The `Receiver` node is used to model radio, serial or infra-red receivers. A
`Receiver` node must be added to the children of a robot or supervisor. Please
note that a `Receiver` can receive data but it cannot send it. In order to
achieve bidirectional communication, a robot needs to have both an `Emitter` and
a `Receiver` on board.

### Field Summary

### Receiver Functions

