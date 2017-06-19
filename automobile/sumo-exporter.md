## SUMO exporter

In order to be able to simulate traffic in your simulation, it is required to
have a SUMO network file (`sumo.net.xml`).
The SUMO exporter can create SUMO network files from a Webots simulation.


## Dependencies

The SUMO exporter is using the `shapely` Python module.
Please refer to [these instructions](openstreetmap-importer.md#dependencies) to install it.


## Expectations on the Webots simulation

If the Webots simulation has been created from the OpenStreetMap importer,
then the export should be straight forward.

If it's not the case, you should pay attention on the use of the `Road` and
the `Crossroad` PROTOs. Indeed, their IDs should be unique, and the `Road.startJunction`,
the `Road.endJunction` and the `Crossroad.connectedRoadIDs` fields should be filled
correctly.


## How to use the exporter

You should use the `exporter.py` python script to generate the `sumo.nod.xml`,
`sumo.edg.xml` and `sumo.sumocfg` SUMO files.
These files can be used by SUMO `netconvert` to generate the `sumo.net.xml` file
from the `myMap.wbt` webots simulation world.

```sh
cd $WEBOTS_HOME/projects/automobile/resources/SUMO_exporter
mkdir myMap_net
python exporter.py --input=myMap.wbt --output=myMap_net
$WEBOTS_HOME/projects/automobile/resources/sumo/bin/netconvert --node-files=myMap_net/sumo.nod.xml --edge-files=myMap_net/sumo.edg.xml --output-file=myMap_net/sumo.net.xml
```


## Arguments

| Argument   | Description                                                       | Default value |
| ---------- | ----------------------------------------------------------------- | ------------- |
| `--input`  | Specifies the Webots .wbt file to open.                           | "file.wbt"    |
| `--output` | Specifies the directory where to generate the SUMO network files. | "."           |
