# Backgrounds

## TexturedBackground

```
TexturedBackground {
  SFString texture "noon_sunny_empty"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/backgrounds/protos/TexturedBackground.proto"

### Description

Background textured with a skybox

Supported values for the "texture" field:

- dawn_cloudy_empty
- morning_cloudy_empty
- noon_cloudy_empty
- noon_cloudy_mountains
- noon_stormy_empty
- noon_sunny_empty
- noon_sunny_garden
- twilight_cloudy_empty

## TexturedBackgroundLight

```
TexturedBackgroundLight {
  SFString texture "noon_sunny_empty"
  SFBool castShadows TRUE
  SFBool castLensFlares FALSE
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto"

### Description

Light matching with the TexturedBackground

Supported values for the "texture" field:

- dawn_cloudy_empty
- morning_cloudy_empty
- noon_cloudy_empty
- noon_cloudy_mountains
- noon_stormy_empty
- noon_sunny_empty
- noon_sunny_garden
- twilight_cloudy_empty

