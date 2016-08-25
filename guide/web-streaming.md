## Web Streaming

### Purpose

Webots can be used as a web streaming server, i.e., to send the graphical information of a 3D scene to several
web browsers (used as clients), and to stream scene modifications (such as the moving objects positions, etc.),
as shown in [the figure above](#screenshot-of-webots-used-as-a-streaming-server).

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

To render the scene in a Web browser, Webots is using the same technologies as to render a web scene
(cf. [limitations](web-scene.md#remarks-on-the-used-technologies-and-their-limitations)).
To stream the scene modifications, Webots is using websockets.
Websockets are present on the majority of recent web browsers.
