## Buildings

%figure "One of the available buildings"

![bungalow_style_house.png](images/bungalow_style_house.png)

%end

The following PROTOs of buildings are available to add in your worlds:

- Auditorium
- BigGlassTower
- BuildingUnderConstruction
- BungalowStyleHouse
- CommercialBuilding
- CyberboticsTower
- HollowBuilding
- Hotel
- ModernHouse
- Museum
- ResidentialBuilding
- SimpleTwoFloorsHouse
- TheThreeTowers
- UBuilding

### Generic building

In addition to those PROTOs of buildings, the `GenericBuilding` PROTO represent
a highly customizable building and can be used to model a large variety of
buildings.

%figure "An example of GenericBuilding with the default parameters"

![building.png](images/building.png)

%end

```
GenericBuilding {
     SFFloat     floorHeight            3
     SFInt32     floorNumber            3
     MFVec2f     corners                [10 10, 10 -10, -10 -10, -10 10 ]
     SFString    wallType               "building2"
     SFString    roofType               "tiled"
     SFString    roofShape              "pyramidal roof"
     SFBool      snowOnRoof             FALSE
     SFFloat     roofHeight             3
     SFBool      enableBoundingObject   TRUE
 }
```

#### GenericBuilding Field Summary

- `floorHeight`: Defines the height of one floor.
- `floorNumber`: Defines the number of floors (excluding roof).
- `corners`: Defines the geometry of the building (2D ground footprint of the
building).
- `wallType`: Defines the texture to be used for the walls.
- `roofType`: Defines the texture to be used for the roof. Supported types are
`tiled`, `gravel` and `slate`.
- `roofShape`: Defines the geometry of the roof. Supported geometry are `flat
roof` and `pyramidal roof`.
- `snowOnRoof`: Defines if snow should be added on top of the roof.
- `roofHeight`: Defines the height of the roof (used only in the case of pyramidal
roof).
- `enableBoundingObject`: Defines if the building should have a bounding object.

### Other city objects

In addition to buildings, other PROTO nodes are available representing objects
normally found in a city environment:

- BusStop
- Fence
- Fountain

%figure "The BusStop PROTO"

![bus_stop.png](images/bus_stop.png)

%end
