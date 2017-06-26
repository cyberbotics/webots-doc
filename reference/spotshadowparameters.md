## SpotShadowParameters

Derived from [Shadowparameters](shadowparameters.md).

```
SpotShadowParameters {
  field  SFInt32  shadowMapSize           1024      # Size of the square shadow texture side [32;4096].
  field  SFFloat  near                    0.1       # Light frustum near clipping plane.
  field  SFFloat  far                     1000      # Light frustum far clipping plane.
  field  SFFloat  softness                0.2       # Shadow penumbra size.
  field  SFBool   fsaa                    FALSE     # Toggle supersampling anti-alisasing to reduce staircase edge effects.
  field  SFFloat  varianceLowerBound      0.000002  # Lower bound on the shadow map variance to reduce numerical inaccuracies.
  field  SFFloat  lightBleedingReduction  0.2       # Percentage of light bleeding reduction. Using a value of 1.0 falls back to hard edged shadows.
}
```
