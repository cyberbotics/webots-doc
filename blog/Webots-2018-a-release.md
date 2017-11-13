# Version R2018a Released

<p id="publish-data">By XXX - XXth XXX 2018</p>

---

Today we're happy to announce the release of Webots R2018a. This new release brings a ton of new features and improvements, coupled with the same dedicated patches addressing bugs and regressions. Listed below are some of the key features of this release (for a full list of changes please refer to the ChangeLog, found [here](https://www.cyberbotics.com/dvd/common/doc/webots/ChangeLog.html)).


## Improved Automobile Simulation Integration

Automobile simulation tools have been largely integrated into the default Webots resources.

### Renamed Automobile Folder

The 'automobile' folder has been renamed into 'vehicles'.
You will therefore have to update your Makefile: for C, C++ and JAVA, the new `WEBOTS_AUTOMOBILE_PATH` should be set to:
```
$(WEBOTS_HOME)/projects/vehicles/libraries
```
instead of:
```
$(WEBOTS_HOME)/projects/automobile/libraries
```

Similarly in python, the library path should be set to:
```
os.environ.get("WEBOTS_HOME") + "/projects/vehicles/libraries/python"
```
instead of:
```
os.environ.get("WEBOTS_HOME") + "/projects/automobile/libraries/python"
```

Furthermore, vehicles are now organized by brand.

### New Truck & Two-Wheeled Models

In addition to the `Bus` PROTO two new models of trucks have been added:

%figure "Models of large vehicles"
![large vehicles](images/large_vehicles.png)
%end

Furthermore, a model of a motorbike and a model of a scooter have been added:

%figure "Models of two wheels vehicles"
![two wheels](images/two_wheels.png)
%end

All these new models are now used in the SUMO interface.

### Moved OSM\_importer and SUMO\_exporter

The [OpenStreetmap](https://www.openstreetmap.org) importer and the [SUMO](http://sumo.dlr.de/wiki/Simulation_of_Urban_MObility_-_Wiki) exporter have both been moved to the `WEBOTS_HOME/resources` folder and renamed to `osm_importer` and `sumo_exporter` to make sure they can be easily used in other contexts than automobile simulations.

### SUMO Interface as Default Controller

The SUMO interface and PROTO have been moved to `WEBOTS_HOME/projects/default` and can now be used in any project.
