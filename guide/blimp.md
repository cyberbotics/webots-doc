## LIS Blimp

%figure "Blimp model in Webots"

![model.png](images/robots/blimp/model.png)

%end

The "Blimp" robot is a Zeppelin-like aerial robot developed by the [EPFL LIS laboratory](https://lis.epfl.ch/).

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/epfl/lis/worlds".

### blimp\_lis.wbt

![blimp.png](images/robots/blimp/blimp.wbt.png) This is an example of the flying blimp robot developed at the Laboratory of Intelligent Systems (LIS) at EPFL.
You can use your keyboard, or a joystick to control the blimp's motion across the room.
Use the up, down, right, left, page up, page down and space (reset) keys.
Various `Transform` and `IndexedFaceSet` nodes are used to model the room using textures and transparency.
A *physics plugin* is used to add thrust and other forces to the simulation.

> **Note**:
`Fluid` and `Propeller` nodes are now recommended to create flying robots.
