## CameraFocus


```
CameraFocus {
  SFFloat  focalDistance     0  # Distance to the object we are focusing on (m)
  SFFloat  focalLength       0  # Focal length of the lens (m)
  SFFloat  maxFocalDistance  0  # (m)
  SFFloat  minFocalDistance  0  # (m)
}
```

### Description

The `CameraFocus` node allows the user to define a controllable focus for a
`Camera` device. The `CameraFocus` node should be set in the `focus` field of a
`Camera` node. The focal distance can be adjusted from the controller program
using the `wb_camera_set_focal_distance()` function.

### Field Summary

