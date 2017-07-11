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
```
