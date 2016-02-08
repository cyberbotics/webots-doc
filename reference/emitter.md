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

- `type`: type of signals: "radio", "serial" or "infra-red". Signals of type
"radio" (the default) and "serial" are transmitted without taking obstacles into
account. Signals of type "infra-red," however, do take potential obstacles
between the emitter and the receiver into account. Any solid object (solid,
robots, etc ...) with a defined bounding object is a potential obstacle to an
"infra-red" communication. The structure of the emitting or receiving robot
itself will not block an "infra-red" transmission. Currently, there is no
implementation difference between the "radio" and "serial" types.
- `range`: radius of the emission sphere (in meters). A receiver can only receive
a message if it is located within the emission sphere. A value of -1 (the
default) for `range` is considered to be an infinite range.
- `maxRange`: defines the maximum value allowed for `range`. This field defines
the maximum value that can be set using `wb_emitter_set_range()`. A value of -1
(the default) for `maxRange` is considered to be infinite.
- `aperture` opening angle of the emission cone (in radians); for "infra-red"
only. The cone's apex is located at the origin ([0 0 0]) of the emitter's
coordinate system and the cone's axis coincides with the *z*-axis of the emitter
coordinate system. An "infra-red" emitter can only send data to receivers
currently located within its emission cone. An `aperture` of -1 (the default) is
considered to be infinite, meaning that the emitted signals are omni-
directional. For "radio" and "serial" emitters, this field is ignored.  See  for
an illustration of `range` and `aperture`.

%figure "Illustration of aperture and range for "infra-red" Emitter/Receiver"
![Illustration of aperture and range for "infra-red" Emitter/Receiver](pdf/emitter_receiver.pdf.png)
%end


- `channel`: transmission channel. This is an identification number for an "infra-
red" emitter or a frequency for a "radio" emitter. Normally a receiver must use
the same channel as an emitter to receive the emitted data. However, the special
channel -1 allows broadcasting messages on all channels. Channel 0 (the default)
is reserved for communicating with a physics plugin. For inter-robot
communication, please use positive channel numbers.
- `baudRate`: the baud rate is the communication speed expressed in number of bits
per second. A `baudRate` of -1 (the default) is regarded as infinite and causes
the data to be transmitted immediately (within one control step) from emitter to
receiver.
- `byteSize`: the byte size is the number of bits required to transmit one byte of
information. This is usually 8 (the default), but can be more if control bits
are used.
- `bufferSize`: specifies the size (in bytes) of the transmission buffer. The
total number of bytes in the packets enqueued in the emitter cannot exceed this
number. A `bufferSize` of -1 (the default) is regarded as unlimited buffer size.

### Emitter Functions

#### Description

The `wb_emitter_send()` function adds to the emitters's queue a packet of `size`
bytes located at the address indicated by `data`. The enqueued data packets will
then be sent to potential receivers (and removed from the emitter's queue) at
the rate specified by the `baudRate` field of the `Emitter` node. Note that a
packet will not be sent to its emitter robot. This function returns 1 if the
message was placed in the sending queue, 0 if the sending queue was full. The
queue is considered to be *full* when the sum of bytes of all the currently
enqueued packets exceeds the buffer size specified by the `bufferSize` field.
Note that a packet must have at least 1 byte.

The Emitter/Receiver API does not impose any particular format on the data being
transmitted. Any user chosen format is suitable, as long as the emitter and
receiver codes agree. The following example shows how to send a null-terminated
ascii string using the C API:

And here an example on how to send binary data with the C API:

#### Description

The `wb_emitter_set_channel()` function allows the controller to change the
transmission channel. This modifies the `channel` field of the corresponding
`Emitter` node. Normally, an emitter can send data only to receivers that use
the same channel. However, the special WB\_CHANNEL\_BROADCAST value can be used
for broadcasting to all channels. By switching the channel number an emitter can
selectively send data to different receivers. The `wb_emitter_get_channel()`
function returns the current channel number of the emitter.

#### Description

The `wb_emitter_set_range()` function allows the controller to change the
transmission range at run-time. Data packets can only reach receivers located
within the emitter's range. This function modifies the `range` field of the
corresponding `Emitter` node. If the specified `range` argument is larger than
the `maxRange` field of the `Emitter` node then the current range will be set to
`maxRange`. The `wb_emitter_get_range()` function returns the current emitter's
range. For both the `wb_emitter_set_range()` and `emitter_get_range()`
functions, a value of -1 indicates an infinite range.

#### Description

The `wb_emitter_get_buffer_size()` function returns the size (in bytes) of the
transmission buffer. This corresponds to the value specified by the `bufferSize`
field of the `Emitter` node. The buffer size indicates the maximum number of
data bytes that the emitter's queue can hold in total, if the size is -1, the
number of data bytes is not limited. When the buffer is full, calls to
`wb_emitter_send()` will fail and return 0.

