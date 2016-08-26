## Web Streaming

### Description

Webots can be used as a Web streaming server, i.e.,
to stream a simulation to several interactive 3D `HTML` pages,
as shown in the [figure bellow](web-streaming.md#screenshot-of-webots-streaming-server).

The mechanism is similar to the [web animation export](web-animation.md)
except that the `X3D` file and the animation are sent on the fly to the browser clients.

%figure "Screenshot of Webots streaming server"

![streaming-server-screenshot.png](images/streaming-server-screenshot.png)

%end


### How to stream a Webots Simulation

Start Webots with the streaming server using the `--stream` option.
Please refer to this [documentation](starting-webots.md#command-line-arguments)
to know the sub-options.

Open the streaming viewer page in your Web browser:

```
$(WEBOTS_HOME)/resources/web/streaming_viewer/index.html 
```

Use the buttons on the top of the page to connect to the Webots streaming server.

**Note**:
IP and ports between should match. The port should not be used by another application.


### Network settings

The Webots streaming server is simply  running on the local computer on a given port
(`1234` by default, but it can be modified from the [command line arguments](starting-webots.md#command-line-arguments)).
This port should not be used by another application.
In order to be visible from the outside network, 
the port should be open (e.g. on simple networks, this can be done by modifying the NAT settings of the router).
The firewall of the local computer may complain about this operation, in this case, please modify its settings.


### How to embed a Web Scene in your Website

Similarly to [this section](web-animation.md#how-to-embed-a-web-animation-in-your-website),
please refer to the streaming viewer page to embed a Webots stream in your Website.


### Limitations

The streaming server has the same limitations as the [Web animation](web-animation.md#limitations).
Except that adding and deleting objects from Webots is propagated to the clients.


### Technologies and Limitations

The data is sent to the clients using [WebSockets](https://www.websocket.org/).
`WebSockets` is supported in recent versions of Firefox, Chrome, Edge, Internet Explorer and Safari on
Mac OS X (see details on the [WebSockets website](https://www.websocket.org/)).

Moreover, please refer to [this section](web-animation.md#remarks-on-the-used-technologies-and-their-limitations).
