## LightSensor

Derived from `Device`.


```
LightSensor {
  MFVec3f     lookupTable   [ 0 0 0, 1 1000 0 ]
  SFColor     colorFilter   1 1 1    # [0,1]
  SFBool      occlusion     FALSE
  SFFloat     resolution    -1
}
```

### Description

`LightSensor` nodes are used to model photo-transistors, photo-diodes or any
type of device that measures the irradiance of light in a given direction.
*Irradiance* represents the radiant power incident on a surface in Watts per
square meter (W/m^2), and is sometimes called *intensity*. The simulated
irradiance is computed by adding the irradiance contributed by every light
source (`DirectionalLight`, `SpotLight` and `PointLight`) in the world. Then the
total irradiance is multiplied by a color filter and fed into a lookup table
that returns the corresponding user-defined value.

The irradiance contribution of each light source is divided into *direct* and
*ambient* contributions. The direct contribution depends on the `position` and
the `orientation` of the sensor, the `location` and the `direction` of the light
sources and (optionally) on the possible occlusion of the light sources. The
ambient contribution ignores the possible occlusions, and it is not affected by
the `orientation` of the sensor nor by the `direction` of a light source. The
direct and ambient contributions of `PointLight`s and `SpotLight`s are
attenuated according to the distance between the sensor and the light, according
to specified attenuation coefficients. The light radiated by a
`DirectionalLight` is not attenuated. See also `DirectionalLight`, `SpotLight`
and `PointLight` node descriptions.

Note that the Webots lighting model does not take reflected light nor object
colors into account.

### Field Summary

- `lookupTable`: this table allows Webots to map simulated irradiance values to user-defined sensor output values and to specify a noise level. The first column contains the input irradiance values in W/m^2. The second column represents the corresponding sensor output values in user-defined units. The third column specifies the level of noise in percent of the corresponding output value. See the section on the `DistanceSensor` node for more explanation on how a `lookupTable` works.
- `colorFilter`: specifies an RGB filter that can be used to approximate a physical color filter or spectral response. The total RGB irradiance is multiplied by this filter (see formula below) in order to obtain a scalar irradiance value *E* that is then used as the input to the lookup table. The `colorFilter` field can, for example, be used to selectively detect light sources according to color.
- `occlusion`: specifies whether or not obstacles between the sensor and light sources should be taken into account in the calculation of irradiance. If the `occlusion` field is FALSE (the default), all potential obstacles (Walls, other Robots, etc.) are ignored and Webots behaves as if they were transparent. If the `occlusion` field is TRUE, Webots will detect which light sources are occluded (from the sensor's viewpoint) and it will ignore their direct contributions. Note that the `occlusion` flag affects only the *direct* light measurement, not the *ambient* light which is always added in. By default, the `occlusion` field is disabled because the occlusion detection is computationally expensive and should be avoided whenever possible. For example, in a setup where it is obvious that there will never be an obstacle between a particular sensor and the various light sources, the `occlusion` flag can be set to FALSE.
- `resolution`: This field allows to define the resolution of the sensor, the resolution is the smallest change that it is able to measure. Setting this field to -1 (default) means that the sensor has an 'infinite' resolution (it can measure any infinitesimal change). This field accepts any value in the interval (0.0, inf).

Before being interpolated by the `lookupTable`, the total irradiance `E` [W/m^2]
seen by a sensor is computed according to the equation shown in :

<center>
![Light sensor irradiance formula](pdf/light_intensity.pdf)

####Light sensor irradiance formula
</center>

The `F` vector corresponds to the sensor's `colorFilter` field, `n` is the total
number of lights in the simulation, `on[i]` corresponds to the `on` field of
light `i` (TRUE=1, FALSE=0), the `C[i]` vector is the `color` field of light
`i`, and `I` is the `ambientIntensity` field of light `i`.  The value `att[i]`
is the attenuation of light `i`, and is calculated as shown in .

<center>
![Light attenuation](pdf/light_attenuation.pdf)

####Light attenuation
</center>

Variables `a` and `a` correspond to the `attenuation` field of light `i`, and
`d` is the distance between the sensor and the light. There is no attenuation
for `DirectionalLight`s. `I` is the direct irradiance contributed by light `i`,
and is calculated as shown in .

<center>
![Direct irradiance](pdf/direct_light.pdf)

####Direct irradiance
</center>

Finally, `spot[i]` is a factor used only in case of a `SpotLight`, and that
depends on its `cutOffAngle` and `beamWidth` fields, and is calculated as shown
in , where the `alpha` angle corresponds to the angle between `-L` and the
`direction` vector of the `SpotLight`.

<center>
![SpotLight factor](pdf/spot_light.pdf)

####SpotLight factor
</center>

The value `I[i]` corresponds to the *intensity* field of light `i`, and `N` is
the normal axis (*x*-axis) of the sensor (see ). In the case of a `PointLight`,
`L` is the sensor-to-light-source vector. In the case of a `DirectionalLight`,
`L` corresponds to the negative of the light's `direction` field. The *
operation is a modified dot product: if dot lt 0, then 0, otherwise, dot
product. Hence, each light source contributes to the irradiance of a sensor
according to the cosine of the angle between the `N` and the `L` vectors, as
shown in the figure. The contribution is zero if the light source is located
behind the sensor. This is derived from the physical fact that a photo-sensitive
device is usually built as a surface of semiconductor material and therefore,
the closer the angle of incidence is to perpendicular, the more photons will
actually hit the surface and excite the device. When a light source is parallel
to (or behind) the semiconductor surface, no photons actually reach the surface.

<center>
![The irradiance (E) depends on the angle (phi) between the](pdf/light_sensor.pdf)

####The irradiance (E) depends on the angle (phi) between the
</center>

The "occlusion" condition is true if the light source is hidden by one or more
obstacles. More precisely, "occlusion" is true if (1) the `occlusion` field of
the sensor is set to TRUE and (2) there is an obstacle in the line of sight
between the sensor and the light source. Note that `DirectionalLight` nodes
don't have *location* fields; in this case Webots checks for obstacles between
the sensor and an imaginary point located 1000m away in the direction opposite
to the one indicated by the `direction` field of this `DirectionalLight`.

Like any other type of collision detection in Webots, the `LightSensor`
occlusion detection is based on the `boundingObjects` of `Solid` nodes (or
derived nodes). Therefore, even if it has a visible geometric structure, a
`Solid` node cannot produce any occlusion if its `boundingObject` is not
specified.

### LightSensor Functions

