## Light


```
Light {
  SFFloat   ambientIntensity   0        # [0,1]
  SFColor   color              1 1 1    # [0,1]
  SFFloat   intensity          1        # [0,1]
  SFBool    on                 TRUE
  SFBool    castShadows        FALSE
}
```

Direct derived nodes: `PointLight`, `SpotLight`, `DirectionalLight`.

### Description

The `Light` node is abstract: only derived nodes can be instantiated. Lights
have two purposes in Webots: (1) the are used to graphically illuminate objects
and (2) they determine the quantity of light perceived by `LightSensor` nodes.
Except for `castShadows`, every field of a `Light` node affects the light
measurements made by `LightSensor` nodes.

### Field Summary

