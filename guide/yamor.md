## Biorob Yamor

%figure "Yamor model in Webots"

![model.png](images/robots/yamor/model.png)

%end

TODO: description.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/epfl/biorob/worlds".

#### yamor.wbt

![yamor.wbt.png](images/robots/yamor/yamor.wbt.png) In this example, eight "Yamor" robot modules attach and detach to and from each other using `Connector` devices.
Connector devices are used to simulate the mechanical connections of docking systems.
In this example, the robot modules go through a sequence of loops and worm-like configurations while changing their mode of locomotion.
All modules use the same controller code, but their actual module behavior is chosen according to the name of the module.
