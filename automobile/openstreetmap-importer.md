## OpenStreetMap importer

In order to ease the creation of new environments for automobile simulations,
Webots worlds can be generated from OpenStreetMap maps using the importer script
described here.

You can download an OpenStreetMap map of any part of the world from
[www.openstreetmap.org/export](http://www.openstreetmap.org/export) (do not use
more than a few kilometers square if you want to be able to run your simulation
in real-time). And then convert it using the script.

Additionally a SUMO road network file should be provided to the importer in order
to generate the roads.
This file can be generated from the same input OpenStreetMap map using the SUMO
`netconvert` tool (embedded in Webots).
Typically, the `sumo.net.xml` file can be created the following way:

```sh
cd $WEBOTS_HOME/projects/automobile/resources/sumo
export PATH=$PATH:$(pwd)/lib
./netconvert --osm-files map.osm -o sumo.net.xml
```

The script is written in Python. A typical usage is:

```sh
cd $WEBOTS_HOME/projects/automobile/resources/OSM_importer
python importer.py --inputFile=myMap.osm --sumoNetworkFile=sumo.net.xml --outputFile=myWorld.wbt
```

This command will create the file called `myWorld.wbt` and if there is some
forest in the map, it will generate a `forest` folder too. This `forest` folder
contains the [forest files](nature.md#forest) of the forests present in the
world.

A detailed tutorial about an automobile scenario creation
can be found in [this section](scenario-creation-tutorial.md).

You can use several arguments with this script:

%figure "OpenStreetMap importer arguments"

| Argument               | Description                                                                                                                          | Default value                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| --input                | Specifies the OSM file to be converted                                                                                               | If not specified, the script tries to convert "map.osm"                   |
| --sumoNetworkFile      | Specifies a SUMO network which is used to generate roads.                                                                            | If not specified, the script tries to open "sumo.net.xml"                 |
| --output               | Specifies the name of the generated world file                                                                                       | If not specified, the generated world is called "map.wbt"                 |
| --config-file          | Specifies which configuration file to use                                                                                            | If not specified, tries to use the configuration file called "config.ini" |
| --spline-subdivision   | Defines the spline subdivision used for roads, rivers, etc.                                                                          | A default value of 0 is used                                              |
| --layer-height         | Defines the height of a layer (the 'layer' tag is ignored if set to 0)                                                               | A default value of 5.0 is used                                            |
| --no-forests           | Does not include the forests in the generated world                                                                                  | By default, forests are included                                          |
| --no-roads             | Does not include the roads in the generated world                                                                                    | By default, roads are included                                            |
| --no-areas             | Does not include the areas (water area, landuse, etc.) in the generated world                                                        | By default, areas are included                                            |
| --no-trees             | Does not include the isolated trees in the generated world                                                                           | By default, isolated trees are included                                   |
| --no-barriers          | Does not include the barriers (fence, wall, etc.) in the generated world                                                             | By default, barriers are included                                         |
| --no-rivers            | Does not include the rivers in the generated world                                                                                   | By default, rivers are included                                           |
| --no-buildings         | Does not include the buildings in the generated world                                                                                | By default, buildings are included                                        |
| --no-intersection-road-lines | Does not generate road start and end lines at intersections                                                                    | By default, road start and end lines are generated at intersections       |
| --enable-3D            | Uses an external service to retrieve elevation information and use an `ElevationGrid` for the ground (requires an internet connexion)| By default, the ground of the generated world is flat                     |
| --disable-multipolygon-buildings | Does not generate buildings from multipolygon                                                                              | By default, buildings are generated from multipolygon                     |
| --projection           | Defines the projection parameters, the projection parameters should be defined following the PROJ.4 rules (https://trac.osgeo.org/proj/wiki/GenParms). Note that if you are not using the default projection, the GPS model of Webots may not match with the generated world. | By default, an empty string is used to define an UTM projection |
| --extract-projection   | Extracts the projection from the OSM file, displays it and exits.                                                                    | By default, this option is disabled.                                      |

%end

In addition to these arguments, a configuration file can be used to define how
to handle most of the OpenStreetMap entities. A typical configuration file can
be seen in [appendix](a-typical-openstreetmap-importer-configuration-file.md).

### Map edition and creation

If you want to edit a map exported from OpenStreetMap before converting it into
a Webots world, we recommend using JOSM. [JOSM](https://josm.openstreetmap.de)
is an open source software written in Java. It is very powerful and easy to use.
Using JOSM you can easily edit a map in order to add some elements, correct some
parts, etc.

%figure "Left: the OSM file created in JOSM. Right: the resulting world open in Webots after conversion"

![osm_input.png](images/osm_input.png)
![osm_output.png](images/osm_output.png)

%end

In addition to editing map from OpenStreetmap, JOSM is also very convenient to
create new environment from scratch. You can see in the [previous
picture](#left-the-osm-file-created-in-josm-right-the-resulting-world-open-in-webots-after-conversion)
a map fully created in JOSM and then exported and opened in Webots.

### Graphical user interface

To ease the use of this tool, a graphical interace has been created. This
grapical interface can easily be started from the last tab of the [robot
window](robot-window.md).

%figure "The OpenStreetMap importer graphical user interface"

![osm_gui.png](images/osm_gui.png)

%end

As you can see on [previous
picture](#the-openstreetmap-importer-graphical-user-interface) , it is easy to
set all the arguments of the script using the graphical user interface of the
robot window. Furthermore, using this graphical interface you can choose either
to give an osm file as input or a map area using a latitude-longitude rectangle.
If you choose to use a latitude-longitude rectangle, it will take care
to automatically download the corresponding osm file before launching the script
(you will therefore require an internet connexion).
