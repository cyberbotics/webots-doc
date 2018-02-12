## Environments Directory

This section shows some of the possible environments and objects available in Webots inside composed scenes.
Webots objects are modular and parametrizable, so other environments can be created simply, starting from these examples.
The world files for these examples are located in the "projects/sample/environments/worlds" directory.

Outdoor and urban environments located in the "projects/vehicles/worlds" and are not shown here.

In this directory, you will find the following world files :

### apartment.wbt

**Keywords**: Apartment, domestic environment, furniture

%figure "Screenshots of the apartment environment."

|                                            |                                            |
|--------------------------------------------|--------------------------------------------|
| ![apartment_a.png](images/apartment_a.png) | ![apartment_b.png](images/apartment_b.png) |
| ![apartment_c.png](images/apartment_c.png) | ![apartment_d.png](images/apartment_d.png) |

%end

This example shows a possible layout for some of the domestic objects included in Webots.
These objects are Webots PROTO nodes, and can be easily moved and resized to create other apartment layouts.
The kitchen and doors are interactive.
This means that a robot could open a drawer, leave an object inside it, and close it.
Light objects such as the books on the shelf or the fruits in the basket can be grabbed by a robot.
An e-puck robot patrols on the table and an iRobot Create robot cleans the ground.

### factory.wbt

**Keywords**: Factory, workbench, tools, industrial pipes, industrial stairs

%figure "Screenshots of the factory environment."

|                                        |                                        |
|----------------------------------------|----------------------------------------|
| ![factory_a.png](images/factory_a.png) | ![factory_b.png](images/factory_b.png) |

%end

This example shows a possible layout for some of the industrial objects included in Webots.
These objects are Webots PROTO nodes, and can be easily moved and resized to create other factory layouts.
The tools and valves are interactive.
This means that a robot could grab a hammer, or turn a valve handle.

### kitchen.wbt

**Keywords**: kitchen, utensil

![kitchen.png](images/kitchen.png) This example shows a kitchen created by using some of the domestic objects included in Webots.
These objects are Webots PROTO nodes, and can be easily moved and resized to create other kitchen layouts.
A robot can interact with the kitchen utensils, the glasses, the bottles, the plates, the pans or the food.
The shelves doors and drawers are also interactive.

### spinning\_top.wbt

**Keywords**: Spinner, chessboard, chess pieces, torque application

![spinning_top.png](images/spinning_top.png) This example shows rotating objects, in order to play with the torque application feature.
To apply a torque on the spinner, use the `Alt + mouse right click` sequence.
