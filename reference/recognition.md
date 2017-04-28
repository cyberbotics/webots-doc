## Recognition

```
Recognition {
  SFFloat  maxRange       100     # (m)
  SFInt32  maxObjects     -1      # maximum number of objects detected simultaneously
  SFBool   occlusion      TRUE    # should occlusions between the camera and the object be checked
  SFColor  frameColor     1 0 0   # color of the objects frame in the overlay
  SFInt32  frameThickness 1       # thickness of the objects frame in the overlay
}
```

### Description

The [Recognition](#recognition) node gives object recognition capability to the camera.
When a [Camera](camera.md) device has a [Recognition](#recognition) node in its `recognition` field, it is able to recognize which objects are present in the camera image. Only [Solids](solid.md) whose `recognitionColors` field is not empty can be recognized by the camera.

### Field Summary

- The `maxRange` field defines the maximum distance at which an object can be recognized. Objects farther than `maxRange` are not recognized.

- The `maxObjects` field defines the maximum number of objects detected by the camera. `-1` means no limit. If more objects than the limit are visible by the camera, only the `maxObjects` ones are recognized (ordered by pixel size).

- The `occlusion` field defines if occlusions between the camera and the object should be checked. Disabling the occlusions detection can save computational time and therefore speed up the simulation, but it can lead to recognized object that are not really visible to the camera.

- The `frameColor` field defines the color used to frame the objects recognized by the camera in its overlay.

- The `frameThickness` field defines the thickness of the frames in the camera overlay. 0 means no object frame in the camera overlay.
