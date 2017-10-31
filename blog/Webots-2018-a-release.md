# Version R2018a Released

<p id="publish-data">By XXX - XXth XXX 2018</p>

---

Today we're happy to announce the release of Webots R2018a. This new release brings a ton of new features and improvements, coupled with the same dedicated patches addressing bugs and regressions. Listed below are some of the key features of this release (for a full list of changes please refer to the ChangeLog, found [here](https://www.cyberbotics.com/dvd/common/doc/webots/ChangeLog.html)).


## Improved automobile simulation integration

The integration of the automobile simulation has been improved in Webots R2018a.

### New location for car PROTO files and libraries

The car PROTO files, libraries and associated worlds have been moved into `WEBOTS_HOME/projects/robots/cars`.
You will therefore have to update your Makefile, in C, C++ and JAVA, the new `WEBOTS_AUTOMOBILE_PATH` should be set to `$(WEBOTS_HOME)/projects/robots/cars/libraries` instead of `$(WEBOTS_HOME)/projects/automobile/libraries`.
Similarly in python, the library path should be set to `os.environ.get("WEBOTS_HOME") + "/projects/robots/cars/libraries/python"` instead of `os.environ.get("WEBOTS_HOME") + "/projects/automobile/libraries/python"`.

### New large vehicle models

Some new large vehicle models have been added in `/projects/robots/large_vehicles`:

%figure "Models of large vehicles"
![large vehicles](images/large_vehicles.png)
%end

### Moved OSM_importer and SUMO_exporter

The OpenStreetmap importer and the SUMO exporter have both been moved in the `WEBOTS_HOME/resources` folder to make sure they can be easily used in other contexts than automobile simulations.

### SUMO interface as a default controller

The SUMO interface and PROTO have been moved in the `WEBOTS_HOME/projects/default` and can now be used in any project.

### Static vehicle models

The static vehicle models (either used by SUMO interface or for non-moving parked vehicles) have been moved in `WEBOTS_HOME/projects/objects/vehicles`. Furthermore, models of two wheels vehicles have been added:

%figure "Models of two wheels vehicles"
![two wheels](images/two_wheels.png)
%end
