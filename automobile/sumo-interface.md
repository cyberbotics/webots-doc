## SUMO interface

An interface with a microscopic traffic simulator called `SUMO` (Simulation of
Urban MObility) has been developed using a `Supervisor` node. The advantage of
interfacing SUMO with Webots is that it allows to easily generate traffic using
a large number of vehicles in real-time. This interface is written in python in
a supervisor controller and uses  [TraCI](http://sumo.dlr.de/wiki/TraCI) to
communicate with SUMO.

In order to use this interface a few rules need to be observed. First, a
`Supervisor` node has to be added to the simulation and should use the
`sumo_supervisor` controller. Then a folder called `worldName_net` should be
present close to the world file. This folder should contains the usual files
defining a network in SUMO (.edg.xml, .nod.xml, .rou.xml, etc.) and the
configuration files (.netccfg and .sumocfg).

Then the interface will automatically start SUMO and run it in synchronization
with Webots time. Each time a new vehicle enter the SUMO simulation, it will be
created in Webots too and its position and orientation will be continually
updated. The vehicle DEF name is set to `SUMO_VEHICLEX`, with `X` being the vehicle number (starting from 0). If some vehicles whose DEF name is `SUMO_VEHICLEX` are already present in the world at the simulation start, then the interface will automatically use them before creating new vehicles, this can be useful to avoid real-time addition of vehicles (which can make the simulation speed drop for a very short time). If some vehicles whose DEF name is `WEBOTS_VEHICLEX` (with `X` being the vehicle number starting from 0) are present in the simulation, the interface will automatically add them and update their position and orientation in SUMO in order to close the loop.

If the SUMO abstract vehicle class (vClass vehicle attribute, refer to SUMO documentation for more information about this attribute) of the vehicle is `passenger` (default), one of the available car PROTOs will be randomly selected and created in Webots. If the abstract vehicle class of the vehicle is `bus` Webots will use the `Bus` PROTO.

If the simulation contains traffic lights, the name of the
corresponding `LEDs` node of these traffic lights in Webots should respect the
following syntax: `trafficLightID_trafficLightIndex_r/y/g`. If the `LEDs` names
are respected, the state of the traffic light will be automatically updated in
Webots from SUMO by the interface.

A few arguments can be passed to the `sumo_supervisor` controller using the
field `controllerArgs` in order to customize the behavior of the interface:

%figure "sumo_supervisor arguments"

| Argument              | Description                                                                                                                          | Default value                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| --no-gui                 | Runs the command-line version of SUMO                                                                                                | By default, the GUI version of SUMO is launched                                                  |
| --verbose                | Prints SUMO outputs in Webots console                                                                                                | SUMO outputs are lost                                                                            |
| --step                   | Specifies the time step of SUMO in milliseconds                                                                                      | By default, a time step of 200ms is used                                                         |
| --no-netconvert          | Does not run netconvert before launching SUMO                                                                                        | By default, netconvert is run before launching SUMO. It is required to disable netconvert if the *.net.xml file is already available (for example when importing it from OpenStreetMap)          |
| --disable-traffic-lights | Does not update traffic light states in Webots                                                                                       | By default, traffic light states are updated in Webots                                           |
| --max-vehicles           | Specifies the maximum number of vehicles included in Webots                                                                          | By default, a maximum of 100 vehicles are included in Webots                                     |
| --rotate-wheels          | Updates the orientation of the wheels of the vehicles in Webots                                                                      | By default, the wheels orientation is not updated                                                |
| --radius                 | Specifies the visibility radius of the vehicles in meters (only vehicles closer to the viewpoint than this radius will be displayed) | By default, the visibility radius is equal to -1 which means that all the vehicles are displayed |
| --enable-height          | Specifies if height information should be extracted from the edge name                                                               | By default, all the vehicles are in the plane defined by y = 0                                   |
| --d or --directory       | Specifies the directory where are located the SUMO network files                                                                     | By default the files should be located close to the world in a directory called `worldName_net`  |
| --p --port               | Specifies which port SUMO and the interface should use to communicate                                                                | By default, the port 8873 is used                                                                |
| --s --seed               | Specifies the seed of the SUMO random number generator (0 for the '--random' option of SUMO)                                         | By default, a seed of 1 is used                                                                  |
| --use-display            | Specifies if the GUI view of SUMO should be displayed in a Webots display (only working in GUI mode, and the Supervisor must have a display named 'sumo display')                                         | By default, the GUI view is not displayed  |
| --display-refresh-rate   | Specifies the refresh rate of the SUMO display, expressed in milliseconds (no effect if the SUMO display is not activated)           | By default, a refresh rate of 1000ms is used                                                                  |
| --display-zoom           | Specifies the initial zoom of the SUMO display in Webots (1.0 means no scaling)                                                      | By default, no scaling is performed                                                                  |
| --display-fit-size       | Specifies if the image should be resized to fit the SUMO display size or not                                                         | By default, the image is not resized                                                                  |

%end

In addition to these arguments, the plugin mechanism can be used to extend the
interface. The plugin should be written in python, be in the same folder than
the SUMO network files, and should implement the `SumoSupervisorPlugin` class
with the two following entry-point functions:

```python
class SumoSupervisorPlugin:
  def __init__(self, supervisor, traci, net):
    # TODO

  def run(self, ms):
    # TODO
```

The first function is called at initialization of the interface, the arguments
are: the `Supervisor` itself, the traci class in order to get information about
the traci context and the net class to get information about the network. The
second one is called at each SUMO step and the argument is the time step.

Such a plugin can be used for example to change traffic light state in SUMO.

> **note**:
Currently version 0.26 of SUMO is distributed with Webots.


### SumoInterface PROTO

Instead of adding a `Supervisor` node and assigning the `sumo_supervisor` controller to it, you can simply add the `SumoInterface` PROTO node which provides a simpler interface to change the arguments of the controller and does not require you to copy the `sumo_supervisor` controller in the `controllers` directory of your project.
