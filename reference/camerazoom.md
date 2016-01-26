## CameraZoom


```
CameraZoom {
  SFFloat     maxFieldOfView 1.5 # (rad)
  SFFloat     minFieldOfView 0.5 # (rad)
}
```

### Description

The `CameraZoom` node allows the user to define a controllable zoom for a
`Camera` device. The `CameraZoom` node should be set in the `zoom` field of a
`Camera` node. The zoom level can be adjusted from the controller program using
the `wb_camera_set_fov()` function.

### Field Summary

