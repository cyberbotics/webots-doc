# OpenStreetMap Importer

In order to ease the creation of new environments for automobile simulations, Webots worlds can be generated from OpenStreetMap maps using the importer script described here.

You can download an OpenStreetMap map of any part of the world from [www.openstreetmap.org/export](http://www.openstreetmap.org/export) (do not use more than a few square kilometers if you want to be able to run your simulation in real-time) and then save it as a Webots world file (e.g. `myMap.wbt`) using the importer script.

## Movie Presentation

![youtube video](https://www.youtube.com/watch?v=tPXHnp4bHrY&t)

## Dependencies

Follow [these instructions](../guide/using-python.md) to install Python.

Then install the Python `lxml`, `pyproj`, `shapely` and `webcolors` modules, as described below.

### Linux

```sh
sudo apt-get install python-pip
sudo pip install lxml pyproj shapely webcolors configparser
```

### macOS

```
pip install lxml pyproj shapely webcolors configparser --user
```

### Windows

As a prerequisite, `Microsoft Visual C++ Compiler for Python 2.7` (version `9.0` or higher) is required to build the `pyproj` dependency.
You can download it [from there](https://www.microsoft.com/en-us/download/details.aspx?id=44266).
If you are using Python 3.6 you will need [Microsoft Visual C++ Build Tools for Visual Studio 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15) instead.

Download the shapely wheel called [`Shapely‑<<version>>‑cp<<python_version>>‑cp<<python_version>>m‑win_amd64.whl`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely) and type in the [Windows Command Prompt](https://en.wikipedia.org/wiki/Cmd.exe):

```
%PYTHON_PATH%\Scripts\pip.exe install lxml
%PYTHON_PATH%\Scripts\pip.exe install pyproj
%PYTHON_PATH%\Scripts\pip.exe install webcolors
%PYTHON_PATH%\Scripts\pip.exe install configparser
%PYTHON_PATH%\Scripts\pip.exe install %HOME%\Downloads\Shapely‑<<version>>‑cp<<python_version>>‑cp<<python_version>>m‑win_amd64.whl
```

## How to Use the Importer

You should use the `importer.py` Python script to generate the `myMap.wbt` webots simulation world from the `myMap.osm` file:

```sh
cd $WEBOTS_HOME/resources/osm_importer
python importer.py --input=myMap.osm --output=myMap.wbt
```

Some extra folders such as `forest` can be generated in the target directory depending on the importer arguments.

Find [here](scenario-creation-tutorial.md) a detailed tutorial about an automobile scenario creation.

## Arguments

You can use several arguments with this script:

%figure "OpenStreetMap importer arguments"

| Argument               | Description                                                                                                                          | Default value                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| --input                | Specifies the OSM file to be converted                                                                                               | If not specified, the script tries to convert "map.osm"                   |
| --output               | Specifies the name of the generated world file                                                                                       | If not specified, the generated world is called "map.wbt"                 |
| --config-file          | Specifies which configuration file to use                                                                                            | If not specified, tries to use the configuration file called "config.ini" |
| --layer-height         | Defines the height of a layer (the 'layer' tag is ignored if set to 0)                                                               | A default value of 5.0 is used                                            |
| --no-forests           | Does not include the forests in the generated world                                                                                  | By default, forests are included                                          |
| --no-roads             | Does not include the roads in the generated world                                                                                    | By default, roads are included                                            |
| --no-areas             | Does not include the areas (water area, landuse, etc.) in the generated world                                                        | By default, areas are included                                            |
| --no-parking           | Does not include the parkings in the generated world                                                                                 | By default, parkings are included                                         |
| --no-trees             | Does not include the isolated trees in the generated world                                                                           | By default, isolated trees are included                                   |
| --no-barriers          | Does not include the barriers (fence, wall, etc.) in the generated world                                                             | By default, barriers are included                                         |
| --no-rivers            | Does not include the rivers in the generated world                                                                                   | By default, rivers are included                                           |
| --no-buildings         | Does not include the buildings in the generated world                                                                                | By default, buildings are included                                        |
| --no-intersection-road-lines | Does not generate road start and end lines at intersections                                                                    | By default, road start and end lines are generated at intersections       |
| --enable-3D            | Uses an external service to retrieve elevation information and use an `ElevationGrid` for the ground (requires an internet connexion)| By default, the ground of the generated world is flat                     |
| --disable-multipolygon-buildings | Does not generate buildings from multipolygon                                                                              | By default, buildings are generated from multipolygon                     |
| --projection           | Defines the projection parameters, the projection parameters should be defined following the [PROJ.4 rules](http://proj4.org/parameters.html), it should look like: `"+proj=robin +lon_0=2.3945 +lat_0=48.8365 +x_0=0.0725 +y_0=-5206258.932 +ellps=WGS84 +units=m +no_defs"`. Note that if you are not using the default projection, the GPS model of Webots may not match with the generated world. | By default, an empty string is used to define an UTM projection |
| --extract-projection   | Extracts the projection from the OSM file, displays it and exits.                                                                    | By default, this parameter is disabled.                                   |
| --removal-radius       | Specifies the radius (in meters) around each road waypoint beyond which any object is removed. It is possible to use the road.filter field of the [configuration file](a-typical-openstreetmap-importer-configuration-file.md) to specify which roads should be taken into account. | By default this feature is disabled (radius = 0.0).                       |
%end

In addition to these arguments, a configuration file can be used to define how to handle most of the OpenStreetMap entities.
A typical configuration file can be seen in [appendix](a-typical-openstreetmap-importer-configuration-file.md).

## Map Edition and Creation

If you want to edit a map exported from OpenStreetMap before converting it into a Webots world, we recommend using JOSM.
[JOSM](https://josm.openstreetmap.de) is an open source software written in Java.
It is very powerful and easy to use.
Using JOSM you can easily edit a map in order to add some elements, correct some parts, etc.

%figure "Left: the OSM file created in JOSM. Right: the resulting world open in Webots after conversion"

![osm_input.png](images/osm_input.png)
![osm_output.png](images/osm_output.png)

%end

In addition to editing map from OpenStreetmap, JOSM is also very convenient to create new environment from scratch.
You can see in the [previous picture](#left-the-osm-file-created-in-josm-right-the-resulting-world-open-in-webots-after-conversion) a map fully created in JOSM and then exported and opened in Webots.

## Graphical User Interface

To ease the use of this tool, a graphical interace has been created.
This grapical interface can easily be started from the last tab of the [robot window](robot-window.md).

%figure "The OpenStreetMap importer graphical user interface"

![osm_gui.png](images/osm_gui.png)

%end

As you can see on [previous picture](#the-openstreetmap-importer-graphical-user-interface), it is easy to set all the arguments of the script using the graphical user interface of the robot window.
Furthermore, using this graphical interface you can choose either to give an osm file as input or a map area using a latitude-longitude rectangle.
If you choose to use a latitude-longitude rectangle, it will take care to automatically download the corresponding osm file before launching the script (you will therefore require an internet connexion).
