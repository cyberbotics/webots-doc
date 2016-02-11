## GPS

Derived from [Device](reference/device.md#device).

```
GPS {
  SFString   type              "satellite"
  SFFloat    accuracy          0
  SFFloat    noiseCorrelation  0
  SFFloat    resolution       -1
}
```

### Description

The [GPS](reference/gps.md#gps) node is used to model a Global Positioning
Sensor (GPS) which can obtain information about its absolute position from the
controller program.

### Field Summary

- `type`: This field defines the type of GPS technology used like "satellite" or
"laser" (currently ignored).

- `accuracy`: This field defines the precision of the GPS, that is the standard
deviation (expressed in meter) of the gaussian noise added to the position.

- `noiseCorrelation`: If a more accurate gps noise model than the simple gaussian
noise is required, this field can be used to define the noise correlation level.
The noise model is then approximated by a gaussian-correlated phenomena, which
capture for example the drift phenomena present in GPS. The value should be
between 0 and 1 and represents how much the noise from 1 second ago influence
the current noise, 0 means no influence (i.e. no correlation) and 1 means that
the noise will be constant (noise fully correlated with the noise from one
second ago). Internally the correlation factor corresponding to the sensor time
step is computed and the current noise is estimated using a Gauss-Markov process
as described in .

%figure "Gauss-Markov process"
![Gauss-Markov process](pdf/gauss_markov.pdf.png)
%end

- `resolution`: This field allows to define the resolution of the sensor, the
resolution is the smallest change that it is able to measure. Setting this field
to -1 (default) means that the sensor has an 'infinite' resolution (it can
measure any infinitesimal change). This field accepts any value in the interval
(0.0, inf).

### GPS Functions

#### Name

**wb\_gps\_enable**, **wb\_gps\_disable**, **wb\_gps\_get\_sampling\_period**, **wb\_gps\_get\_values** - *enable, disable and read the GPS measurements*

{[C++](reference/cpp-api.md)}, {[Java](reference/java-api.md)}, {[Python](reference/python-api.md)}, {[Matlab](reference/matlab-api.md)}

``` c
#include <webots/gps.h>

void wb_gps_enable(WbDeviceTag tag, int ms)
void wb_gps_disable(WbDeviceTag tag)
int wb_gps_get_sampling_period(WbDeviceTag tag)
const double *wb_gps_get_values(WbDeviceTag tag)
```

#### Description

`wb_gps_enable()` allows the user to enable a GPS measurement each `ms`
milliseconds.

`wb_gps_disable()` turns the GPS off, saving computation time.

The `wb_gps_get_sampling_period()` function returns the period given into the
`wb_gps_enable()` function, or 0 if the device is disabled.

The `wb_gps_get_values()` function returns the current
[GPS](reference/gps.md#gps) measurement. The values are returned as a 3D-vector,
therefore only the indices 0, 1, and 2 are valid for accessing the vector. The
returned vector indicates the absolute position of the
[GPS](reference/gps.md#gps) device.

> **note** [C, C++]: The returned vector is a pointer to the internal values managed by the
[GPS](reference/gps.md#gps) node, therefore it is illegal to free this pointer.
Furthermore, note that the pointed values are only valid until the next call to
`wb_robot_step()` or `Robot::step()`. If these values are needed for a longer
period they must be copied.

> **note** [Python]: `getValues()` returns the 3D-vector as a list containing three floats.

