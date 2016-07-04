## A typical OpenstreetMap importer configuration file

```ini
  # BUILDINGS DEFAULTS SETTINGS #

  [building]
  ignore: FALSE
  floorHeight: 3
  floorNumber: 3

  [building_house]
  ignore: FALSE
  floorHeight: 3
  floorNumber: 2

  [building_apartments]
  ignore: FALSE
  floorHeight: 3
  floorNumber: 4

  [building_residential]
  ignore: FALSE
  floorHeight: 3.2
  floorNumber: 6

  # WATERWAY DEFAULTS SETTINGS #

  [waterway]
  ignore: TRUE

  [waterway_river]
  ignore: FALSE
  width: 2

  [waterway_stream]
  ignore: FALSE
  width: 2

  # ROUNDABOUT DEFAULTS SETTINGS #

  [roundabout]
  ignore: FALSE
  laneWidth: 4
  laneNumber: 1

  [roundabout_primary]
  ignore: FALSE
  laneWidth: 3.5
  laneNumber: 2

  # AREA DEFAULTS SETTINGS #

  [area]
  ignore: TRUE

  [area_farmland]
  ignore: FALSE
  texture: textures/dry_grass.jpg

  [area_farm]
  ignore: FALSE
  texture: textures/dry_grass.jpg

  [area_water]
  ignore: FALSE
  blueComponent: 1

  [area_forest]
  ignore: FALSE
  greenComponent: 1
  transparency: 0.7
  density: 0.1

  # ROAD DEFAULTS SETTINGS #

  [road]
  ignore: TRUE

  [road_motorway]
  ignore: FALSE
  border: FALSE
  # this is for oneway
  laneNumber: 3
  laneWidth: 3.5

  [road_motorway_link]
  ignore: FALSE
  border: FALSE
  laneNumber: 1
  laneWidth: 4

  [road_trunk]
  ignore: FALSE
  border: FALSE
  # this is for oneway
  laneNumber: 2
  laneWidth: 3

  [road_trunk_link]
  ignore: FALSE
  border: FALSE
  laneNumber: 1
  laneWidth: 4

  [road_primary]
  ignore: FALSE
  border: FALSE
  laneNumber: 2
  laneWidth: 3.5

  [road_secondary]
  ignore: FALSE
  laneNumber: 2
  laneWidth: 3.5

  [road_tertiary]
  ignore: FALSE
  laneNumber: 1
  laneWidth: 4

  [road_residential]
  ignore: FALSE
  laneNumber: 1
  laneWidth: 4
  texture: "textures/road_no_border_line.jpg"

  [road_unclassified]
  ignore: FALSE
  laneNumber: 1
  laneWidth: 4
  texture: "textures/road_no_border_line.jpg"

  [road_service]
  ignore: FALSE
  border: FALSE
  laneNumber: 1
  laneWidth: 4
  texture: "textures/road_no_border_line.jpg"
```
