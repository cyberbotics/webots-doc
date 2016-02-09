## GPS

Derived from `Device`.

```
GPS {
  SFString   type              "satellite"
  SFFloat    accuracy          0
  SFFloat    noiseCorrelation  0
  SFFloat    resolution       -1
}
```

### Description

The `GPS` node is used to model a Global Positioning Sensor (GPS) which can
obtain information about its absolute position from the controller program.

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

#### Description

`wb_gps_enable()` allows the user to enable a GPS measurement each `ms`
milliseconds.

`wb_gps_disable()` turns the GPS off, saving computation time.

The `wb_gps_get_sampling_period()` function returns the period given into the
`wb_gps_enable()` function, or 0 if the device is disabled.

The `wb_gps_get_values()` function returns the current `GPS` measurement. The
values are returned as a 3D-vector, therefore only the indices 0, 1, and 2 are
valid for accessing the vector. The returned vector indicates the absolute
position of the `GPS` device.

