# Lights

## CeilingLight

%figure "CeilingLight model in Webots."

![CeilingLight](images/objects/lights/CeilingLight/model.png)

%end

```
CeilingLight {
   SFVec3f translation 0 2.4 0
   SFRotation rotation 0 1 0 0
   SFString name "ceiling light"
   SFColor bulbColor 1 1 1
   MFString bulbTextureUrl "textures/light_bulb.jpg"
   SFColor supportColor 1 1 1
   MFString supportTextureUrl "textures/light_support.jpg"
   SFFloat pointLightAmbientIntensity 0
   SFVec3f pointLightAttenuation 1 0 0
   SFColor pointLightColor 1 1 1
   SFFloat pointLightIntensity 1
   SFBool pointLightCastShadows FALSE
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/lights/protos/CeilingLight.proto"

### CeilingLight Description

A ceiling light (0.19 x 0.8 x 0.19 m).

## FloorLight

%figure "FloorLight model in Webots."

![FloorLight](images/objects/lights/FloorLight/model.png)

%end

```
FloorLight {
   SFVec3f translation 0 0 0
   SFRotation rotation 0 1 0 0
   SFString name "floor light"
   SFColor bulbColor 1 1 1
   MFString bulbTextureUrl "textures/light_bulb.jpg"
   SFColor supportColor 1 1 1
   MFString supportTextureUrl "textures/light_support.jpg"
   SFFloat pointLightAmbientIntensity 0
   SFVec3f pointLightAttenuation 1 0 0
   SFColor pointLightColor 1 1 1
   SFFloat pointLightIntensity 1
   SFBool pointLightCastShadows FALSE
   SFNode physics NULL
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/lights/protos/FloorLight.proto"

### FloorLight Description

A floor light (0.19 x 1.6 x 0.19 m).

