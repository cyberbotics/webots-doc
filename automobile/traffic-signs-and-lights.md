## Traffic signs and lights

In addition to the `PedestrianCrossing` and `TrafficCone` PROTO nodes, a set of traffic signs and lights is provided.

All of those traffic signs and lights can either be mounted on the `Pole` or `TrafficLightBigPole` PROTO models.
The first one is a simple cylindrical pole on which one element can be mounted.
On the second bigger one, a maximum of three elements can be mounted.

### Traffic lights

%figure "a traffic light"

![traffic_light.png](images/traffic_light.png)

%end

Two kinds of traffic lights are available, they both have 3 `LEDs` and can therefore be controlled if inserted in a `Robot` node.
For both of them, the shape of the light can either be a full circle or an arrow (defined in the `lamp_geometry` field).

- `TrafficLight`: Normal traffic light with 3 colors.
- `TrafficLightHorizontal`: Normal traffic light with 3 colors but with horizontal
sun-protector.

In addition to the traffic lights, the `StreetLight` PROTO can be used to light some part of the road in nightly environments.

%figure "The StreetLight PROTO"

![street_light.png](images/street_light.png)

%end

### Traffic signs

%figure "Various traffic signs"

![order_sign.png](images/order_sign.png)
![speed_sign.png](images/speed_sign.png)
![caution_sign.png](images/caution_sign.png)
![yield_sign.png](images/yield_sign.png)
![sign_pole.png](images/sign_pole.png)

%end

A total of 6 traffic signs are available.
They represent the various sizes and shapes usually used for traffic signs:

- `CautionSign`: Diamond sign usually used for warnings.
- `ExitSign`: Big rectangular sign used for example for highway exits.
- `OrderSign`: Circular sign usually used for interdictions.
- `SpeedLimitSign`: Rectangular sign usually used for speed limits.
- `StopSign`: Octagonal sign usually used for stop.
- `YieldSign`: Triangular sign usually used for yield.
- `SignPole`: Arrow shaped sign usually used to indicate a direction. The text and its properties are implemented as fields.

A complete set of textures is available with those traffic signs and can easily be applied using the `signBoards` field.
The signs are fully customizable as their size, color and number of `signBoards` are implemented as independent fields.

### Highway signs

%figure "Highway poles with one or two stands"

![HighwayPole1.png](images/HighwayPole1.png)
![HighwayPole2.png](images/HighwayPole2.png)

%end

`HighwayPole` is usually used to indicate directions or general information on highways.
It can support, on either one or two stands, multiple signs using the different sign fields.
Just like `HighwaySign`, `HighwayPole` is fully customizable as its size, color and number of signs and stands are implemented as independent fields.
