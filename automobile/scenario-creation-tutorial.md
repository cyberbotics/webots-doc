## Scenario creation tutorial

This small tutorial explains step-by-step how to create a scenario inspired from a real world map and then add traffic using SUMO.
This tutorial has been written for `linux` and `macOS` because of the use of the terminal.
The same can be achieved on `Windows` converting the commands accordingly.


### Creation of the Webots project directory

```sh
export WBT_PROJECT_PATH=/your/webots/project/path  # define here your project path
mkdir -p $WBT_PROJECT_PATH/worlds/map_net
```


### Download the OpenStreetMap map

We will use a part of the OpenStreetMap map to generate the Webots world file. To download the map go to the [OpenStreetMap website](https://www.openstreetmap.org/export). From there you can select the part of the map you want and download it:

%figure "Export a part of map from OpenStreetMap"
![osm_export.png](images/osm_export.png)
%end


### Get the map projection

Get the map projection parameters which will be reuse them to generate the SUMO network file.

```
cd $WEBOTS_HOME/projects/automobile/resources/OSM_importer
$ python importer.py --input=/path/to/map.osm --extract-projection
+proj=utm +north +zone=32 +lon_0=6.505000 +lat_0=46.511000 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```


### Generate the SUMO network files

We can also use the previously downloaded map to generate the SUMO network file. You need to use the [netconvert](http://sumo.dlr.de/wiki/NETCONVERT) utility for this:

```sh
cd $WEBOTS_HOME/projects/automobile/resources/sumo
export PATH=$PATH:$(pwd)/lib  # on linux only
./netconvert --osm-files /path/to/map.osm -o $WBT_PROJECT_PATH/worlds/map_net/sumo.net.xml --geometry.remove --roundabouts.guess --ramps.guess --junctions.join --tls.guess-signals --tls.discard-simple --tls.join --proj "+proj=utm +north +zone=32 +lon_0=6.505000 +lat_0=46.511000 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"
```

> **Note**:
Reuse the projection for the `--proj` option.

Both the [OpenStreetMap importer](openstreetmap-importer.md) and [netconvert](http://sumo.dlr.de/wiki/NETCONVERT) will center the map, but it can happen that the centering is not perfectly matched and results in an offset between the Webots world and the SUMO network. To fix this problem, simply open the `sumo.net.xml` in a text editor and look for the line starting by `<location netOffset=` (it should be at the beginning of the file). You will need to change the value of the `netOffset` field, the new value (for each component) should be the previous value additioned to the value of `x_offset_value` and `y_offset_value` displayed by the [OpenStreetMap importer](openstreetmap-importer.md).

You can then generate the route file, SUMO provides several ways to generate route files. You may for example generate a [flow file](http://sumo.dlr.de/wiki/Definition_of_Vehicles,_Vehicle_Types,_and_Routes) and then use [duarouter](http://sumo.dlr.de/wiki/DUAROUTER) to generate the route file for you:

```sh
./duarouter --flows $WBT_PROJECT_PATH/worlds/map_net/sumo.flow.xml --net-file $WBT_PROJECT_PATH/worlds/map_net/sumo.net.xml --output-file $WBT_PROJECT_PATH/worlds/map_net/sumo.rou.xml
```

Finally you need to write the [SUMO configuration file](http://sumo.dlr.de/wiki/SUMO-GUI#Configuration_Files), the file should be called `$WBT_PROJECT_PATH/worlds/map_net/sumo.sumocfg` and looks like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/sumoConfiguration.xsd">
    <input>
        <net-file value="sumo.net.xml"/>
        <route-files value="sumo.rou.xml"/>
    </input>
    <time>
        <begin value="0"/>
    </time>
    <report>
        <verbose value="true"/>
        <no-step-log value="true"/>
    </report>
</configuration>
```


### Add the SUMO interface

Now that you have all the required files, you can open the generated world in Webots and add the `SumoInterface` PROTO (or a `Supervisor` node and associate the `sumo_supervisor` controller to it). Since the network files are already generated, you need to set the `useNetconvert` field to FALSE (or use the `--noNetconvert` option) and set in the `networkfiles` field (or use the `--d or --directory` option) the path to the directory where the SUMO network files are located.


### Generate the Webots world

As explained in the [OpenStreetMap importer](openstreetmap-importer.md) section, you should use the previously downloaded map to generate the Webots world.

> **Note**:
It is strongly recommended to not use the 3D feature of the [OpenStreetMap importer](openstreetmap-importer.md) otherwise it will not be possible to add traffic using SUMO.

```sh
cd $(WEBOTS_HOME)/projects/automobile/resources/OSM_importer
python importer.py --inputFile=$WBT_PROJECT_PATH/worlds/map_net/myMap.osm --sumoNetworkFile=$WBT_PROJECT_PATH/worlds/map_net/sumo.net.xml --outputFile=$WBT_PROJECT_PATH/worlds/map.wbt
```

> **Node**:
The `map.wbt` base name and the `map_net` directory prefix should match.

You should be able to open the generated world file directly in Webots:

%figure "resulting world generated by the importer"
![osm_tutorial_import1.png](images/osm_tutorial_import1.png)

![osm_tutorial_import2.png](images/osm_tutorial_import2.png)
%end
