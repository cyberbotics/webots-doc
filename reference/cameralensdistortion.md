## CameraLensDistortion


```
CameraLensDistortion {
  SFVec2f  center                  0.5 0.5
  SFVec2f  radialCoefficients      0 0
  SFVec2f  tangentialCoefficients  0 0
}
```

### Description

The `CameraLensDistortion` node allows the user to simulate the camera image
distortion due to the camera lens. A Brown's distortion model with two
coefficients both for the radial and tangential distortions is used to simulate
image distortion.

### Field Summary

