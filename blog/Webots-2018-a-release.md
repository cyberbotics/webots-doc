# Version R2018a Released

<p id="publish-data">By XXX - XXth XXX 2018</p>

---

Today we're happy to announce the release of Webots R2018a. This new release brings a ton of new features and improvements, coupled with the same dedicated patches addressing bugs and regressions. Listed below are some of the key features of this release (for a full list of changes please refer to the ChangeLog, found [here](https://www.cyberbotics.com/dvd/common/doc/webots/ChangeLog.html)).


## Enhanced Viewpoint Movement

### Line It Up Just Right

Take better screenshots and record better videos of your robot by aligning the viewpoint on one of the six world axes, using the new Change tool:

%figure "New Change View Menu"
![viewpoint menu](https://raw.githubusercontent.com/omichel/webots-doc/update-blog-post-for-animated-views/blog/images/viewpoint%20menu.png)
%end

### Smooth

Now, all automated Viewpoint movement is animated, when resetting the viewpoint, moving the viewpoint to an object, or moving to any of the six default views:

![youtube video](https://www.youtube.com/watch?v=S0k0cJb_Mus)

---

## Improved Automobile Simulation Integration

The integration of the automobile simulation has been improved in Webots R2018a.

### The 'automobile' folder has been renamed into 'vehicles'

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

Furthemore, vehicles are now prganized by brand.

### New model of trucks and two wheeled vehicles

In adition to the `Bus` PROTO two new model of trucks have been added:

%figure "Models of large vehicles"
![large vehicles](images/large_vehicles.png)
%end

Furthermore, a model of motorbike and a model of scooter have been added:

%figure "Models of two wheels vehicles"
![two wheels](images/two_wheels.png)
%end

All these new models are now used in the SUMO interface.

### Moved OSM\_importer and SUMO\_exporter

The [OpenStreetmap](https://www.openstreetmap.org) importer and the [SUMO](http://sumo.dlr.de/wiki/Simulation_of_Urban_MObility_-_Wiki) exporter have both been moved in the `WEBOTS_HOME/resources` folder and renamed into `osm_importer` and `sumo_exporter` to make sure they can be easily used in other contexts than automobile simulations.

### SUMO interface as a default controller

The SUMO interface and PROTO have been moved in the `WEBOTS_HOME/projects/default` and can now be used in any project.
