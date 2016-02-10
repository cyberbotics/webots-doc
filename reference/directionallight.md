## DirectionalLight

Derived from [Light](reference/light.md#light).

```
DirectionalLight {
  SFVec3f   direction   0 0 -1   # (-inf,inf)
}
```

### Description

The [DirectionalLight](reference/directionallight.md#directionallight) node
defines a directional light source that illuminates along rays parallel to a
given 3-dimensional vector. Unlike
[PointLight](reference/pointlight.md#pointlight), rays cast by
[DirectionalLight](reference/directionallight.md#directionallight) nodes do not
attenuate with distance.

### Field Summary

- The `direction` field specifies the direction vector of the illumination
emanating from the light source in the global coordinate system. Light is
emitted along parallel rays from an infinite distance away. The `direction`
field is taken into account when computing the quantity of light received by a
[LightSensor](reference/lightsensor.md#lightsensor).

