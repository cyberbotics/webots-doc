# Street Furniture

## Bench

%figure "Bench"

![Bench](images/street_furniture/Bench/model.png)

%end

```
Bench {
  SFVec3f    translation          0 0 0
  SFRotation rotation             0 1 0 0
  SFString   name                 "bench"
  SFColor    metalColor           0.17 0.17 0.17
  SFColor    woodColor            0.25 0.17 0.12
  MFColor    recognitionColors    [0.17 0.17 0.17, 0.25 0.17 0.12]
}
```

### Description

A bench.

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/Bench.proto'.

## BusStop

%figure "BusStop"

![BusStop](images/street_furniture/BusStop/model.png)

%end

```
BusStop {
  SFVec3f     translation                 0 0 0
  SFRotation  rotation                    0 1 0 0
  SFString    name                        "bus stop"
  SFBool      bench                       TRUE
  SFNode      appearance                  Appearance { material Material { diffuseColor 0.3 0.45 0.33 } }
  MFString    internalAdvertisingTexture  [ "textures/cocacola_advertising.jpg" ]
  MFString    externalAdvertisingTexture  [ "textures/cocacola_advertising.jpg" ]
  SFBool      advertisingLightOn          TRUE
}
```

### Description

Simple bus stop with customizable appearance and an optional bench
based on the blender model of Ringbarkis (http://www.blendswap.com/blends/view/66783)
Sponsored by the CTI project RO2IVSim (http://transport.epfl.ch/simulator-for-mobile-robots-and-intelligent-vehicles)

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/BusStop.proto'.

## EmergencyPhone

%figure "EmergencyPhone"

![EmergencyPhone](images/street_furniture/EmergencyPhone/model.png)

%end

```
EmergencyPhone {
  SFVec3f    translation          0 0 0
  SFRotation rotation             0 1 0 0
  SFString   name                 "emergency phone"
  SFColor    poleColor            1 0.44 0
  MFColor    recognitionColors    [1 0.44 0]
}
```

### Description

An emergency phone.

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/EmergencyPhone.proto'.

## FireHydrant

%figure "FireHydrant"

![FireHydrant](images/street_furniture/FireHydrant/model.png)

%end

```
FireHydrant {
  SFVec3f translation 0 0 0
  SFRotation rotation 0 1 0 0
  SFString name "fire hydrant"
  SFNode appearance Appearance { material Material { diffuseColor 0.643 0 0 specularColor 0.473 0.027 0.027} }
}
```

### Description

A fire hydrant.

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/FireHydrant.proto'.

## Fountain

%figure "Fountain"

![Fountain](images/street_furniture/Fountain/model.png)

%end

```
Fountain {
  SFVec3f     translation            0 0 0
  SFRotation  rotation               0 1 0 0
  SFString    name                   "fountain"
  SFFloat     height                 1.5
  SFFloat     radius                 1
  SFInt32     sudivision             16
}
```

### Description

Simple fountain

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/Fountain.proto'.

## PublicBin

%figure "PublicBin"

![PublicBin](images/street_furniture/PublicBin/model.png)

%end

```
PublicBin {
  SFVec3f    translation          0 0 0
  SFRotation rotation             0 1 0 0
  SFString   name                 "public bin"
  SFColor    color                0.27 0.27 0.27
  MFColor    recognitionColors    [0.27 0.27 0.27]
}
```

### Description

A public bin.

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/PublicBin.proto'.

## PublicToilet

%figure "PublicToilet"

![PublicToilet](images/street_furniture/PublicToilet/model.png)

%end

```
PublicToilet {
  SFVec3f     translation         0 0 0
  SFRotation  rotation            0 1 0 0
  SFString    name                "public toilet"
  SFFloat     height              3.2
  SFFloat     length              3.5
  SFFloat     width               2.1
  SFColor     mainColor           0.4 0.4 0.4
  SFColor     secondaryColor      0.5 0.5 0.5
  SFColor     mainTopColor        0.22 0.22 0.22
  SFColor     secondaryTopColor   1 0.95 0.33
  SFColor     windowColor         0.8 1 0.93
  SFString    text                "TOILET"
  SFFloat     textScale           80
  MFString    backDisplayTexture  "textures/webots_billboard.jpg"
  SFBool      backDisplayLight    FALSE
  MFNode      frontDisplay        [ AdvertisingBoard {
  frontTexture ["textures/webots_billboard.jpg"]
  backTexture []
  displayBackLight FALSE
  displayWidth 0.90
  displayHeight 1.35
  frameThickness 0.1
  } ]
}
```

### Description

Resizable public toilet with two different displays.

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/PublicToilet.proto'.

## TrashBin

%figure "TrashBin"

![TrashBin](images/street_furniture/TrashBin/model.png)

%end

```
TrashBin {
  SFVec3f    translation          0 0 0
  SFRotation rotation             0 1 0 0
  SFString   name                 "trash bin"
  SFColor    coverColor           0.1 0.1 0.1
  SFColor    binColor             0.08 0.46 0
  MFColor    recognitionColors    [0.1 0.1 0.1, 0.08 0.46 0]
}
```

### Description

A trash bin.

> **Note**: The PROTO file of this object is located at 'projects/objects/street_furniture/protos/TrashBin.proto'.
