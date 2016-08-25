## Web Streaming

### Description

Webots can be used as a Web streaming server, i.e.,
to stream a simulation to several interactive 3D `HTML` pages.

The mechanism is similar to the [web animation export](web-animation.md)
except that the `X3D` file and the animation are sent on the fly to the browser clients.

%figure "Screenshot of Webots used as a streaming server"

![streaming-server-screenshot.png](images/streaming-server-screenshot.png)

%end


### How to stream a Webots Simulation

**TODO: document**


### What can be streamed

**TODO: document**


### How to embed a Web Scene in your Website

**TODO: document**


### Limitations

**TODO: document**


### Technologies and Limitations

Please refer to [this section](web-animation.md#remarks-on-the-used-technologies-and-their-limitations).

The data is sent to the clients using [WebSockets](https://www.websocket.org/).
`WebSockets` is supported in recent versions of Firefox, Chrome, Edge, Internet Explorer and Safari on
Mac OS X (see details on the [WebSockets website](https://www.websocket.org/)).
