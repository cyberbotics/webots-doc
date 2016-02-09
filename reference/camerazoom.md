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

- The `maxFieldOfView` and the `minFieldOfView` fields define respectively the
maximum and minimum values for the field of view of the camera zoom (i.e.,
respectively the maxium and minimum zoom levels). Hence, they represent the
minimum and maximum values that can be passed to the `wb_camera_set_fov()`
function and they can be retrieved using the functions `wb_camera_get_min_fov()`
and `wb_camera_get_max_fov()`.

