# Version R2018a Released

<p id="publish-data">By XXX - XXth XXX 2018</p>

---

Today we're happy to announce the release of Webots R2018a. This new release brings a ton of new features and improvements, coupled with the same dedicated patches addressing bugs and regressions. Listed below are some of the key features of this release (for a full list of changes please refer to the ChangeLog, found [here](https://www.cyberbotics.com/dvd/common/doc/webots/ChangeLog.html)).


## Improved Automobile Simulation Integration

The integration of the automobile simulation has been improved in Webots R2018a.

### Renaming of the 'automobile' folder has been renamed into 'vehicles'

You will therefore have to update your Makefile, in C, C++ and JAVA, the new `WEBOTS_AUTOMOBILE_PATH` should be set to:
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

### New model of trucks and two wheeled vehicles

In adition to the `Bus` PROTO two new model of trucks have been added:

%figure "Models of large vehicles"
![large vehicles](images/large_vehicles.png)
%end

Furthermore, a model of motorbike and a model of scooter have been added:

%figure "Models of two wheels vehicles"
![two wheels](images/two_wheels.png)
%end

All these new models are now used in the SUMo interface.

### Moved OSM_importer and SUMO_exporter

The OpenStreetmap importer and the SUMO exporter have both been moved in the `WEBOTS_HOME/resources` folder and renamed into `osm_importer` and `sumo_exporter` to make sure they can be easily used in other contexts than automobile simulations.

### SUMO interface as a default controller

The SUMO interface and PROTO have been moved in the `WEBOTS_HOME/projects/default` and can now be used in any project.
