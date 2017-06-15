## SUMO exporter

In order to be able to simulate traffic on your simulation, it is required to
have a SUMO network file (`sumo.net.xml`).
The SUMO exporter can creates a SUMO network files from a Webots simulation.


## Dependencies

The SUMO exporter is using the `shapely` Python module.
Please refer to [these instructions](openstreetmap-importer.md#dependencies) to install it.


## Expectations on the Webots simulation

If the Webots simulation has been created from the OpenStreetMap importer,
then the export should be straight forward.

If it's not the case, you should pay attention on the use of the `Road` and
the `Crossroad` PROTOs. Indeed, their IDs should be unique, and the `Road.startCrossroad`,
the `Road.endCrossroad` and the `Crossroad.connectedRoadIDs` fields should be filled
correctly.


## How to use the exporter

You should use the `exporter.py` python script to generate the `sumo.nod.xml`,
the `sumo.edg.xml` and the `sumo.sumocfg` SUMO files.
These files can be used by SUMO `netconvert` to generate the `sumo.net.xml` file
from the `myMap.wbt` webots simulation world.

```sh
cd $WEBOTS_HOME/projects/automobile/resources/SUMO_exporter
mkdir myMap_net
python exporter.py --input=myMap.wbt --output=myMap_net
```


## Arguments

| Argument   | Description                                                       | Default value |
| ---------- | ----------------------------------------------------------------- | ------------- |
| `--input`  | Specifies the Webots .wbt file to open.                           | "file.wbt"    |
| `--output` | Specifies the directory where to generate the SUMO network files. | "."           |
