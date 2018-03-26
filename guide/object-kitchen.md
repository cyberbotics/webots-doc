# Fridge

%figure "Fridge model in Webots."

![Fridge](images/objects/fridge/Fridge/model.png)

%end

```
Fridge {
  SFVec3f translation 0 0 0
  SFRotation rotation 0 1 0 0
  SFString name "fridge"
  SFColor mainColor 1 1 1
  MFString mainTextureUrl [
    "textures/fridge_main.jpg"
  ]
  SFColor doorColor 1 1 1
  MFString doorTextureUrl [
    "textures/fridge_door.jpg"
  ]
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/fridge/protos/Fridge.proto"

### Fridge Description

A fridge with 2 doors (0.7 x 1.8 x 0.7 m).

# Breakfast

## BiscuitBox

%figure "BiscuitBox model in Webots."

![BiscuitBox](images/objects/breakfast/BiscuitBox/model.png)

%end

```
BiscuitBox {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "biscuit box"
  SFVec3f    size        0.24 0.04 0.08
  MFString   textureUrl  "textures/biscuit_box.jpg"
  SFFloat    mass        0.4
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/breakfast/protos/BiscuitBox.proto"

### BiscuitBox Description

A customizable (size, texture, etc.) biscuit box.

## CerealBox

%figure "CerealBox model in Webots."

![CerealBox](images/objects/breakfast/CerealBox/model.png)

%end

```
CerealBox {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "cereal box"
  SFVec3f    size        0.08 0.3 0.2
  MFString   textureUrl  "textures/cereal_box_2.jpg"
  SFFloat    mass        1
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/breakfast/protos/CerealBox.proto"

### CerealBox Description

A customizable (size, texture, etc.) cereal box.

## HoneyJar

%figure "HoneyJar model in Webots."

![HoneyJar](images/objects/breakfast/HoneyJar/model.png)

%end

```
HoneyJar {
  SFVec3f    translation    0 0 0
  SFRotation rotation       0 1 0 0
  SFString   name           "honey jar"
  MFString   textureLidUrl  "textures/bee_lid.jpg"
  SFFloat    mass           0.5
  SFColor    color          0.839216 0.572549 0.105882
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/breakfast/protos/HoneyJar.proto"

### HoneyJar Description

A honey jar.

## JamJar

%figure "JamJar model in Webots."

![JamJar](images/objects/breakfast/JamJar/model.png)

%end

```
JamJar {
  SFVec3f    translation   0 0 0
  SFRotation rotation      0 1 0 0
  SFString   name          "jam jar"
  MFString   textureLidUrl "textures/blue_jar_lid.jpg"
  SFFloat    mass          0.5
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/breakfast/protos/JamJar.proto"

### JamJar Description

A jam jar.

# Components

## HotPlate

%figure "HotPlate model in Webots."

![HotPlate](images/objects/components/HotPlate/model.png)

%end

```
HotPlate {
  SFVec3f    translation 0 0.71 0
  SFRotation rotation    0 1 0 0
  SFString   name        "hot plate"
  MFString   textureUrl  "textures/components.jpg"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/components/protos/HotPlate.proto"

### HotPlate Description

An hot plate.

## Sink

%figure "Sink model in Webots."

![Sink](images/objects/components/Sink/model.png)

%end

```
Sink {
  SFVec3f    translation 0 0.72 0
  SFRotation rotation    0 1 0 0
  SFString   name        "sink"
  MFString   textureUrl  "textures/components.jpg"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/components/protos/Sink.proto"

### Sink Description

A sink.

## Worktop

%figure "Worktop model in Webots."

![Worktop](images/objects/components/Worktop/model.png)

%end

```
Worktop {
  SFVec3f    translation   0 0.71 0
  SFRotation rotation      0 1 0 0
  SFString   name          "worktop"
  SFVec3f    size          0.44 0.06 0.7
  MFString   textureUrl    "textures/worktop.jpg"
  SFVec2f    tileSize      0.7 0.7
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/components/protos/Worktop.proto"

### Worktop Description

A customizable (size, texture, etc.) worktop.

# Oven

%figure "Oven model in Webots."

![Oven](images/objects/oven/Oven/model.png)

%end

```
Oven {
  SFVec3f translation 0 0.34 0
  SFRotation rotation 0 1 0 0
  SFString name "oven"
  SFColor mainColor 1 1 1
  MFString mainTextureUrl [
    "textures/oven.jpg"
  ]
  SFColor doorColor 1 1 1
  MFString doorTextureUrl [
    "textures/oven.jpg"
  ]
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/oven/protos/Oven.proto"

### Oven Description

An oven (0.5 x 0.68 x 0.44 m).

# Utensils

## Carafe

%figure "Carafe model in Webots."

![Carafe](images/objects/utensils/Carafe/model.png)

%end

```
Carafe {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "carafe"
  SFFloat    mass        1
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Carafe.proto"

### Carafe Description

A carafe.

## Cookware

%figure "Cookware model in Webots."

![Cookware](images/objects/utensils/Cookware/model.png)

%end

```
Cookware {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name       "cookware"
  SFColor    color      0.7 0.7 0.7
  SFFloat    mass       0.7
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Cookware.proto"

### Cookware Description

A cookware.

## Fork

%figure "Fork model in Webots."

![Fork](images/objects/utensils/Fork/model.png)

%end

```
Fork {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "fork"
  SFColor    color       0.55 0.55 0.55
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Fork.proto"

### Fork Description

A fork.

## Glass

%figure "Glass model in Webots."

![Glass](images/objects/utensils/Glass/model.png)

%end

```
Glass {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "glass"
  SFFloat    mass        0.17
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Glass.proto"

### Glass Description

A glass.

## Knife

%figure "Knife model in Webots."

![Knife](images/objects/utensils/Knife/model.png)

%end

```
Knife {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "knife"
  SFColor    color       0.55 0.55 0.55
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Knife.proto"

### Knife Description

A knife.

## Lid

%figure "Lid model in Webots."

![Lid](images/objects/utensils/Lid/model.png)

%end

```
Lid {
  SFVec3f    translation 0 0.068 0
  SFRotation rotation    0 1 0 0
  SFString   name        "lid"
  SFColor    color       0.7 0.7 0.7
  SFFloat    mass        0.19
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Lid.proto"

### Lid Description

A lid.

## Plate

%figure "Plate model in Webots."

![Plate](images/objects/utensils/Plate/model.png)

%end

```
Plate {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "plate"
  MFString   textureUrl  "textures/floral_plate.jpg"
  SFFloat    height      0.01
  SFFloat    radius      0.11
  SFFloat    mass        0.3
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Plate.proto"

### Plate Description

A customizable (dimensions, texture, etc. ) plate.

## Spoon

%figure "Spoon model in Webots."

![Spoon](images/objects/utensils/Spoon/model.png)

%end

```
Spoon {
  SFVec3f     translation 0 0 0
  SFRotation  rotation    0 1 0 0
  SFString    name        "spoon"
  SFColor     color       0.55 0.55 0.55
  SFString    type        "table"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Spoon.proto"

### Spoon Description

A spoon.

## Wineglass

%figure "Wineglass model in Webots."

![Wineglass](images/objects/utensils/Wineglass/model.png)

%end

```
Wineglass {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "wine glass"
  SFFloat    mass        0.2
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/Wineglass.proto"

### Wineglass Description

A wine glass.

## WoodenSpoon

%figure "WoodenSpoon model in Webots."

![WoodenSpoon](images/objects/utensils/WoodenSpoon/model.png)

%end

```
WoodenSpoon {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "wooden spoon"
  MFString   textureUrl  "textures/wooden_spoon.jpg"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/kitchen/utensils/protos/WoodenSpoon.proto"

### WoodenSpoon Description

A wooden spoon.

