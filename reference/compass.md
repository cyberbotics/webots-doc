## Compass

Derived from [Device](device.md) and [Solid](solid.md).

```
Compass {
  MFVec3f lookupTable [ ]    # lookup table
  SFBool  xAxis       TRUE   # {TRUE, FALSE}
  SFBool  yAxis       TRUE   # {TRUE, FALSE}
  SFBool  zAxis       TRUE   # {TRUE, FALSE}
  SFFloat resolution  -1     # {-1, [0, inf)}
}
```

### Description

A [Compass](#compass) node can be used to model a 1, 2 or 3-axis digital compass (magnetic sensor).
The [Compass](#compass) node returns a vector that indicates the direction of the *virtual north*.
The *virtual north* is specified by the `northDirection` field in the [WorldInfo](worldinfo.md) node.

### Field Summary

- `lookupTable`: This field optionally specifies a lookup table that can be used for mapping each vector component (between -1.0 and +1.0) to device specific output values.
By default the lookup table is empty and therefore no mapping is applied.
See the section on the [DistanceSensor](distancesensor.md#lookup-table) node for more explanation on how a `lookupTable` works.

- `xAxis, yAxis, zAxis`: Each of these boolean fields specifies if the computation should be enabled or disabled for the specified axis.
If one of these fields is set to FALSE, then the corresponding vector element will not be computed and it will return *NaN* (Not a Number).
For example if zAxis is FALSE, then the second element of the array returned by the `wb_compass_get_values` function will always return *NaN*.
The default is that all three axes are enabled (TRUE).
Modifying these fields makes it possible to choose between a single, dual or a three-axis digital compass and to specify which axes will be used.

- `resolution`: This field allows to define the resolution of the sensor, the resolution is the smallest change that it is able to measure.
Setting this field to -1 (default) means that the sensor has an 'infinite' resolution (it can measure any infinitesimal change).
This field accepts any value in the interval (0.0, inf).

### Compass Functions

**Name**

**wb\_compass\_enable**, **wb\_compass\_disable**, **wb\_compass\_get\_sampling\_period**, **wb\_compass\_get\_values** - *enable, disable and read the output values of the compass device*

{[C++](cpp-api.md#cpp_compass)}, {[Java](java-api.md#java_compass)}, {[Python](python-api.md#python_compass)}, {[Matlab](matlab-api.md#matlab_compass)}, {[ROS](ros-api.md)}

```c
#include <webots/compass.h>

void wb_compass_enable(WbDeviceTag tag, int sampling_period);
void wb_compass_disable(WbDeviceTag tag);
const double *wb_compass_get_values(WbDeviceTag tag);
int wb_compass_get_sampling_period(WbDeviceTag tag);
```

**Description**

The `wb_compass_enable` function turns on the [Compass](#compass) measurements.
The `sampling_period` argument specifies the sampling period of the sensor and is expressed in milliseconds.
Note that the first measurement will be available only after the first sampling period elapsed.

The `wb_compass_disable` function turns off the [Compass](#compass) device.

The `wb_compass_get_sampling_period` function returns the period given into the `wb_compass_enable` function, or 0 if the device is disabled.

The `wb_compass_get_values` function returns the current [Compass](#compass) measurement.
The returned vector indicates the direction of the *virtual north* in the coordinate system of the [Compass](#compass) device.
Here is the internal algorithm of the `wb_compass_get_values` function in pseudo-code:

```c
float[3] wb_compass_get_values() {
  float[3] n = getGlobalNorthDirection();
  n = rotateToCompassOrientation3D(n);
  n = normalizeVector3D(n);
  n[0] = applyLookupTable(n[0]);
  n[1] = applyLookupTable(n[1]);
  n[2] = applyLookupTable(n[2]);
  if (xAxis == FALSE) n[0] = 0.0;
  if (yAxis == FALSE) n[1] = 0.0;
  if (zAxis == FALSE) n[2] = 0.0;
  return n;
}
```

If the lookupTable is empty and all three xAxis, yAxis and zAxis fields are TRUE then the length of the returned vector is 1.0.

The values are returned as a 3D-vector, therefore only the indices 0, 1, and 2 are valid for accessing the vector.
Let's look at one example.
In Webots global coordinates system, the *xz*-plane represents the horizontal floor and the *y*-axis indicates the elevation.
The default value of the `northDirection` field is [ 1 0 0 ] and therefore the north direction is horizontal and aligned with the x-axis.
Now if the [Compass](#compass) node is in *upright* position, meaning that its y-axis is aligned with the global y-axis, then the bearing angle in degrees can be computed as follows:

```c
double get_bearing_in_degrees() {
  const double *north = wb_compass_get_values(tag);
  double rad = atan2(north[0], north[2]);
  double bearing = (rad - 1.5708) / M_PI * 180.0;
  if (bearing < 0.0)
    bearing = bearing + 360.0;
  return bearing;
}
```

> **Note** [C, C++]: The returned vector is a pointer to the internal values managed by the [Compass](#compass) node, therefore it is illegal to free this pointer.
Furthermore, note that the pointed values are only valid until the next call to the `wb_robot_step` or `Robot::step` functions.
If these values are needed for a longer period they must be copied.

<!-- -->

> **Note** [Python]: Ths `getValues` function returns the vector as a list containing three floats.
