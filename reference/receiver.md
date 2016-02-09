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

- `type`: type of signal: "radio", "serial" or "infra-red". Signals of type
"radio" (the default) and "serial" are transmitted without taking obstacles into
account. Signals of type "infra-red," however, do take potential obstacles
between the emitter and the receiver into account. Any solid object (solid,
robots, etc ...) with a defined bounding object is a potential obstacle for an
"infra-red" communication. The structure of the emitting or receiving robot
itself will not block an "infra-red" transmission. Currently, there is no
implementation difference between the "radio" and "serial" types.
- `aperture`: opening angle of the reception cone (in radians); for "infra-red"
only. The receiver can only receive messages from emitters currently located
within its reception cone. The cone's apex is located at the origin ([0 0 0]) of
the receiver's coordinate system and the cone's axis coincides with the *z*-axis
of the receiver coordinate system (see  in ). An `aperture` of -1 (the default)
is considered to be infinite, meaning that a signal can be received from any
direction. For "radio" receivers, the `aperture` field is ignored.
- `channel`: reception channel. The value is an identification number for an
"infra-red" receiver or a frequency for a "radio" receiver. Normally, both
emitter and receiver must use the same channel in order to be able to
communicate. However, the special -1 channel number allows the receiver to
listen to all channels.
- `baudRate`: the baud rate is the communication speed expressed in bits per
second. It should be the same as the speed of the emitter. Currently, this field
is ignored.
- `byteSize`: the byte size is the number of bits used to represent one byte of
transmitted data (usually 8, but may be more if control bits are used). It
should be the same size as the emitter byte size. Currently, this field is
ignored.
- `bufferSize`: size (in bytes) of the reception buffer. The size of the received
data should not exceed the buffer size at any time, otherwise data may be lost.
A `bufferSize` of -1 (the default) is regarded as unlimited buffer size. If the
previous data have not been read when new data are received, the previous data
are lost.
- `signalStrengthNoise`: standard deviation of the gaussian noise added to the
signal strength returned by `wb_receiver_get_signal_strength`. The noise is
proportionnal to the signal strength, e.g., a `signalStrengthNoise` of 0.1 will
add a noise with a standard deviation of 0.1 for a signal strength of 1 and 0.2
for a signal strength of 2.
- `directionNoise`: standard deviation of the gaussian noise added to each of the
components of the direction returned by `wb_receiver_get_emitter_direction`. The
noise is not dependent on the distance between emitter-receiver.

### Receiver Functions

#### Description

`wb_receiver_enable()` starts the receiver listening for incoming data packets.
Data reception is activated in the background of the controller's loop at a rate
of once every `ms` milliseconds. Incoming data packet are appended to the tail
of the reception queue (see ). Incoming data packets will be discarded if the
receiver's buffer size (specified in the `Receiver` node) is exceeded. To avoid
buffer overflow, the data packets should be read at a high enough rate by the
controller program. The function `wb_receiver_disable()` stops the background
listening.

The `wb_receiver_get_sampling_period()` function returns the period given into
the `wb_receiver_enable()` function, or 0 if the device is disabled.

#### Description

The `wb_receiver_get_queue_length()` function returns the number of data packets
currently present in the receiver's queue (see ).

The `wb_receiver_next_packet()` function deletes the head packet. The next
packet in the queue, if any, becomes the new head packet. The user must copy
useful data from the head packet, before calling `wb_receiver_next_packet()`. It
is illegal to call `wb_receiver_next_packet()` when the queue is empty
(`wb_receiver_get_queue_length()` == 0). Here is a usage example:

``` c
while (wb_receiver_get_queue_length(tag) > 0) {
  const char *message = wb_receiver_get_data(tag);
  const double *dir = wb_receiver_get_emitter_direction(tag);
  double signal = wb_receiver_get_signal_strength(tag);
  printf("received: %s (signal=%g, dir=[%g %g %g])\n",
         message, signal, dir[0], dir[1], dir[2]);
  wb_receiver_next_packet(tag);
}
```

This example assumes that the data (*message*) was sent in the form of a null-
terminated string. The Emitter/Receiver API does not put any restriction on the
type of data that can be transmitted. Any user chosen format is suitable, as
long as emitters and receivers agree.

%figure "Receiver's packet queue"
![Receiver's packet queue](pdf/receiver_queue.pdf.png)
%end

- Packets will be received in the same order they were sent
- Packets will be transmitted atomically (no byte-wise fragmentation)

However, the Emitter/Receiver API does not guarantee a specific schedule for the
transmission. Sometimes several packets may be bundled and received together.
For example, imagine a simple setup where two robots have an `Emitter` and a
`Receiver` on board. If both robots use the same controller time step and each
one sends a packet at every time step, then the Receivers will receive, on
average, one data packet at each step, but they may sometimes get zero packets,
and sometimes two! Therefore it is recommend to write code that is tolerant to
variations in the transmission timing and that can deal with the eventuality of
receiving several or no packets at all during a particular time step. The
`wb_receiver_get_queue_length()` function should be used to check how many
packets are actually present in the `Receiver`'s queue. Making assumptions based
on timing will result in code that is not robust.

#### Description

The `wb_receiver_get_data()` function returns the data of the packet at the head
of the reception queue (see ). The returned data pointer is only valid until the
next call to the function `wb_receiver_next_packet()`. It is illegal to call
`wb_receiver_get_data()` when the queue is empty
(`wb_receiver_get_queue_length()` == 0). The `Receiver` node knows nothing about
that structure of the data being sent but its byte size. The emitting and
receiving code is responsible to agree on a specific format.

The `wb_receiver_get_data_size()` function returns the number of data bytes
present in the head packet of the reception queue. The *data size* is always
equal to the *size* argument of the corresponding `emitter_send_packet()` call.
It is illegal to call `wb_receiver_get_data_size()` when the queue is empty
(`wb_receiver_get_queue_length()` == 0).

#### Description

The `wb_receiver_get_signal_strength()` function operates on the head packet in
the receiver's queue (see ). It returns the simulated signal strength at the
time the packet was transmitted. This signal strength is equal to the inverse of
the distance between the emitter and the receiver squared. In other words, *s =
1 / r^2*, where *s* is the signal strength and *r* is the distance between
emitter and receiver. It is illegal to call this function if the receiver's
queue is empty (`wb_receiver_get_queue_length()` == 0).

The function `wb_receiver_get_emitter_direction()` also operates on the head
packet in the receiver's queue. It returns a normalized (length=1) vector that
indicates the direction of the emitter with respect to the receiver's coordinate
system. The three vector components indicate the *x, y *, and  *z*-directions of
the emitter, respectively. For example, if the emitter was exactly in front of
the receiver, then the vector would be [0 0 1]. In the usual orientation used
for 2D simulations (robots moving in the  *xz*-plane and the  *y *-axis oriented
upwards), a positive *x *-component indicates that the emitter is located to the
left of the receiver while a negative  *x *-component indicates that the emitter
is located to the right. The returned vector is valid only until the next call
to `wb_receiver_next_packet()`. It is illegal to call this function if the
receiver's queue is empty (`wb_receiver_get_queue_length()` == 0).

#### Description

The `wb_receiver_set_channel()` function allows a receiver to change its
reception channel. It modifies the `channel` field of the corresponding
`Receiver` node. Normally, a receiver can only receive data packets from
emitters that use the same channel. However, the special WB\_CHANNEL\_BROADCAST
value can be used to listen simultaneously to all channels.

The `wb_receiver_get_channel()` function returns the current channel number of
the receiver.

