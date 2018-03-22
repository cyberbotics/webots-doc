# Components

## HotPlate

%figure "HotPlate"

![HotPlate-image](images/objects/components/HotPlate/model.png)

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

### Description

An hot plate

## Sink

%figure "Sink"

![Sink-image](images/objects/components/Sink/model.png)

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

### Description

A sink

## Worktop

%figure "Worktop"

![Worktop-image](images/objects/components/Worktop/model.png)

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

### Description

A customizable (size, texture, etc.) worktop

