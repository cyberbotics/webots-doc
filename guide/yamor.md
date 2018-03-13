## BioRob Yamor

%figure "Yamor model in Webots"

![model.png](images/robots/yamor/model.png)

%end

The "Yamor" robot is a modular robot developed by the [EPFL BioRob laboratory](https://biorob.epfl.ch/).

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/epfl/biorob/worlds".

#### yamor.wbt

![yamor.wbt.png](images/robots/yamor/yamor.wbt.png) In this example, eight Yamor robot "modules" attach to and detach from each other using `Connector` devices.
Connector devices are used to simulate the mechanical connections of docking systems.
Each module is controlled by an instance of the same robot controller, which can only connect or disconnect from another module and move its rotational motor.
From these simple behaviors, a global behavior emerges.
The resulting robot (composed of all the modules) moves forward as a worm.
From times to times, a module is dropped, showing the robustness of the locomotion behavior of such a system. 
