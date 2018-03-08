## Sphero's BB-8

%figure "BB-8 model in Webots"

![model.png](images/robots/bb8/model.png)

%end

The [Sphero's BB-8](https://www.sphero.com/starwars/bb8) is an articulated robot composed of a spherical body and an hemispherical head.
A wheeled robot is embedded inside the spherical body.

The Webots model is implemented at a high-level of abstraction; the wheeled robot inside the spherical body is not modeled, but the body and head are linked by two rotational joints (pitch and yaw), and one joint allows head rotation.
The robot size are customizable using the BB-8 PROTO fields.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/sphero/worlds".

#### bb-8.wbt

![bb-8.wbt.png](images/robots/bb8/bb-8.wbt.png) This simulation shows the BB-8 moving on a sandy uneven terrain.
When starting up, the robot moves randomly.
You can disable the auto-pilot mode and control the robot (please refer to the corresponding instructions in the Webots console).
