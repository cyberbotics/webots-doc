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

- `type`: type of signal: "radio", "serial" or "infra-red". Signals of type "radio" (the default) and "serial" are transmitted without taking obstacles into account. Signals of type "infra-red," however, do take potential obstacles between the emitter and the receiver into account. Any solid object (solid, robots, etc ...) with a defined bounding object is a potential obstacle for an "infra-red" communication. The structure of the emitting or receiving robot itself will not block an "infra-red" transmission. Currently, there is no implementation difference between the "radio" and "serial" types.
- `aperture`: opening angle of the reception cone (in radians); for "infra-red" only. The receiver can only receive messages from emitters currently located within its reception cone. The cone's apex is located at the origin ([0 0 0]) of the receiver's coordinate system and the cone's axis coincides with the *z*-axis of the receiver coordinate system (see in ). An `aperture` of -1 (the default) is considered to be infinite, meaning that a signal can be received from any direction. For "radio" receivers, the `aperture` field is ignored.
- `channel`: reception channel. The value is an identification number for an "infra-red" receiver or a frequency for a "radio" receiver. Normally, both emitter and receiver must use the same channel in order to be able to communicate. However, the special -1 channel number allows the receiver to listen to all channels.
- `baudRate`: the baud rate is the communication speed expressed in bits per second. It should be the same as the speed of the emitter. Currently, this field is ignored.
- `byteSize`: the byte size is the number of bits used to represent one byte of transmitted data (usually 8, but may be more if control bits are used). It should be the same size as the emitter byte size. Currently, this field is ignored.
- `bufferSize`: size (in bytes) of the reception buffer. The size of the received data should not exceed the buffer size at any time, otherwise data may be lost. A `bufferSize` of -1 (the default) is regarded as unlimited buffer size. If the previous data have not been read when new data are received, the previous data are lost.
- `signalStrengthNoise`: standard deviation of the gaussian noise added to the signal strength returned by `wb_receiver_get_signal_strength`. The noise is proportionnal to the signal strength, e.g., a `signalStrengthNoise` of 0.1 will add a noise with a standard deviation of 0.1 for a signal strength of 1 and 0.2 for a signal strength of 2.
- `directionNoise`: standard deviation of the gaussian noise added to each of the components of the direction returned by `wb_receiver_get_emitter_direction`. The noise is not dependent on the distance between emitter-receiver.

### Receiver Functions

