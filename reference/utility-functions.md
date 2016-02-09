## Utility Functions

This section describes utility functions that are available to the physics
plugin. They are not callback functions, but functions that you can call from
your callback functions.

### dWebotsGetBodyFromDEF()

This function looks for a `Solid` node with the specified name and returns the
corresponding dBodyID. The returned dBodyID is an ODE object that represent a
rigid body with properties such as mass, velocity, inertia, etc. The dBodyID
object can then be used with all the available ODE `dBody*()` functions (see ODE
documentation). For example it is possible to add a force to the body with
`dBodyAddForce()`, etc. The prototype of this function is:

```
dBodyID dWebotsGetBodyFromDEF(const char *DEF);
```

where DEF is the DEF name of the requested `Solid` node.

It is possible to use dots (.) as scoping operator in the DEF parameter. Dots
can be used when looking for a specific node path in the node hierarchy. For
example:

```
dBodyID head_pitch_body = dWebotsGetBodyFromDEF("BLUE_PLAYER_1.HeadYaw.HeadPitch");
```

means that we are searching for a `Solid` node named "HeadPitch" inside a node
named "HeadYaw", inside a node named "BLUE\_PLAYER\_1". Note that each dot (.)
can be substituted by any number of named or unnamed nodes, so in other words it
is not necessary to fully specify the path.

This function returns NULL if there is no `Solid` (or derived) node with the
specified DEF name. It will also return NULL if the `physics` field of the
`Solid` node is undefined (NULL) or if the `Solid` have been *merged* with an
ancestor. Solid merging happens between rigidly linked solids with non NULL
`physics` fields, see `Physics`'s "Implicit solid merging and joints" for more
details. This function searches the Scene Tree recursively, therefore it is
recommended to store the result rather than calling it at each step. It is
highly recommended to test for NULL returned values, because passing a NULL
dBodyID to an ODE function is illegal and will crash the plugin and Webots.

### dWebotsGetGeomFromDEF()

This function looks for a `Solid` node with the specified name and returns the
corresponding dGeomID. A dGeomID is an ODE object that represents a geometrical
shape such as a sphere, a cylinder, a box, etc., or a coordinate system
transformation. The dGeomID returned by Webots corresponds to the boundingObject
of the `Solid`. The dGeomID object can then be used with all the available ODE
`dGeom*()` functions (see ODE documentation). The prototype of this function is:

```
dGeomID dWebotsGetGeomFromDEF(const char *DEF);
```

where DEF is the DEF name of the requested `Solid` node.

It is possible to use dots (.) as scoping operator in the DEF parameter, see
above. This function returns NULL if there is no `Solid` (or derived) node with
the specified DEF name. It will also return NULL if the `boundingObject` field
of the `Solid` node is undefined (NULL). This function searches the Scene Tree
recursively therefore it is recommended to store the result rather than calling
it at each step. It is highly recommended to test for NULL returned values,
because passing a NULL dGeomID to an ODE function is illegal and will crash the
plugin and Webots.

Using the returned dGeomID, it is also possible to obtain the corresponding
dBodyID object using ODE's `dGeomGetBody()` function. This is an alternative to
calling the `dWebotsGetGeomFromDEF()` function described above.

Note that this function returns only the top level dGeomID of the
boundingObject, but the boundingObject can be made of a whole hierarchy of
dGeomIDs. Therefore it is risky to make assumptions about the type of the
returned dGeomID. It is safer to use ODE functions to query the actual type. For
example this function may return a "transform geom" (dGeomTransformClass) or a
"space geom" (dSimpleSpaceClass) if this is required to represent the structure
of the boundingObject.

### dWebotsGetContactJointGroup()

This function allows you to retrieve the contact joint group where to create the
contacts. It is typically called inside the `webots_physics_collide()` function.
Remark that this group may change during the time and should be retrieved at
each `webots_physics_collide()` call.

### dGeomSetDynamicFlag(dGeomID geom)

This function switches on the dynamic flag of a given ODE geometry (given by the
`geom` argument).

By default the ODE geometries linked with an ODE body are dynamic, meaning that
they can pass from one to another cluster in the case of the multi-threaded
version of ODE. On the other hand, an ODE geometry without any ODE body is
static, meaning it is available in every cluster.

There are some cases where one wants to have a dynamic ODE geometry even if it
is not linked with an ODE body. This is the puropose of this function. Typically
the ODE rays (which don't have bodies) are more efficient if defined as dynamic
geometries.

### dWebotsSend() and dWebotsReceive()

It is often useful to communicate information between your physics plugin and
your robot (or Supervisor) controllers. This is especially useful if your
physics plugin implements some sensors (like accelerometers, force feedback
sensors, etc.) and needs to send the sensor measurement to the robot controller.
It is also useful if your physics plugin implements some actuators (like an
Akermann drive model), and needs to receive motor commands from a robot
controller.

The physics plugin API provides the `dWebotsSend()` function to send messages to
robot controllers and the `dWebotsReceive()` function to receive messages from
robot controllers. In order to receive messages from the physics plugin, a robot
has to contain a `Receiver` node set to an appropriate channel (see Reference
Manual) and with a `baudRate` set to -1 (for infinite communication speed).
Messages are sent from the physics plugin using the `dWebotsSend()` function,
and received through the receiver API as if they were sent by an `Emitter` node
with an infinite range and baud rate. Similarly, in order to send messages to
the physics plugin, a robot has to contain an `Emitter` node set to `channel` 0
(as the physics plugin only receives data sent on this channel). The `range` and
`baudRate` fields of the `Emitter` node should be set to -1 (infinite). Messages
are sent to the physics plugin using the standard `Emitter` API functions. They
are received by the physics plugin through the `dWebotsReceive()` function.

```
void dWebotsSend(int channel,const void *buffer,int size);
void *dWebotsReceive(int *size);
```

The `dWebotsSend()` function sends `size` bytes of data contained in `buffer`
over the specified communication `channel`.

The `dWebotsReceive()` function receives any data sent on channel 0. If no data
was sent, it returns NULL; otherwise it returns a pointer to a buffer containing
the received data. If `size` is non-NULL, it is set to the number of bytes of
data available in the returned buffer. If multiple messages are sent to the
physics plugin at the same time step, then they will be concatenated.

> **note**: Pay attention when managing multiple concatenated string messages, because every
message will terminate with the null character `\0` preventing the correct copy
and display of the returned data. The following example shows how to split
concatenated string messages:

>     int dataSize;
>     char *data = (char *)dWebotsReceive(&dataSize);
>     if (dataSize > 0) {
>       char *msg = new char[dataSize];
>       int count = 1, i = 0, j = 0;
>       for ( ; i < dataSize; ++i) {
>         char c = data[i];
>         if (c == '\0') {
>           msg[j] = c;
>           // process message
>           dWebotsConsolePrintf("Received message %d: %s\n", count, msg);
>           // reset for next string
>           ++count;
>           j = 0;
>         } else {
>           msg[j] = c;
>           ++j;
>         }
>       }
>     }

### dWebotsGetTime()

This function returns the current simulation time in milliseconds [ms] as a
double precision floating point value. This corresponds to the time displayed in
the bottom right corner of the main Webots window.

```
double dWebotsGetTime(void);
```

### dWebotsConsolePrintf()

This function prints a line of formatted text to the Webots console. The format
argument is the same as the standard C `printf()` function, i.e., the format
string may contain format characters defining conversion specifiers, and
optional extra arguments should match these conversion specifiers. A prefix and
a '\n' (new line) character will automatically be added to each line. A '\f'
(form feed) character can optionally be used for clearing up the console.

```
void dWebotsConsolePrintf(const char *format, ...);
```

