## Lidar

Derived from [Device](device.md).

```
Lidar {
  SFFloat    tiltAngle                0.0
  SFInt32    horizontalResolution     512
  SFFloat    fieldOfView              1.5708
  SFFloat    verticalFieldOfView      0.2
  SFInt32    numberOfLayers           4
  SFFloat    minRange                 0.01
  SFFloat    maxRange                 1.0
  SFString   type                     "fixed"
  SFBool     spherical                TRUE
  SFFloat    noise                    0.0
  SFFloat    resolution              -1.0
  SFFloat    defaultFrequency         10
  SFFloat    minFrequency             1
  SFFloat    maxFrequency             25
  SFNode     rotatingHead             NULL
  SFString   compositor               ""
}
```

### Description

The [Lidar](#lidar) node is used to model a robot's on-board lidar
(laser-scanner).

The lidar measures depth information (in meters) from an OpenGL rendering, like
the [RangeFinder](rangefinder.md) node does. Whereas a
[RangeFinder](rangefinder.md) node is used to simulate a depth camera (like for
example a Kinect), the [Lidar](#lidar) node is used to simulate laser scans. The
main difference is that for the [RangeFinder](rangefinder.md) node the vertical
field of view is imposed by the size (width and height) of the image (because of
the constraint of square pixels) and not in the case of the [Lidar](#lidar) node
where lines of pixels (laser scan) are extracted from the depth buffer.

Lidar cannot see semi-transparent objects. An object can be semi-transparent
either if its texture has an alpha channel, or if its
[Material](material.md).`transparency` field is not equal to 1.

By default the [Lidar](#lidar) node outputs the depth values in an array, the
depth values are order from left to right and from the top to the bottom layer
(like a [RangeFinder](rangefinder.md) node does). Complementary the point cloud
mode can be enabled thanks to the
[wb\_lidar\_enable\_point\_cloud](#wb_lidar_enable) function. It is then
possible to call the [wb\_lidar\_get\_point\_cloud](#wb_lidar_get_point_cloud)
to get the lidar output as a point cloud (array of points). Be aware that the
point cloud mode is computationally expensive and can therefore slow-down the
simulation speed.

#### WbLidarPoint

A point of the lidar point cloud is defined by the following structure

``` c
typedef struct {
  float x;
  float y;
  float z;
  int layer_id;
  float time;
} WbLidarPoint;
```

The X, Y and Z coordinates are relative to the [Lidar](#lidar) node origin. The
`layer_id` field specifies to which layer this point belongs to (from 0 to
`numberOfLayers` - 1) and the `time` field specifies the exact time at which the
point was acquired. With lidar devices, all the points are not acquired at the
exact same time but rather sequentially.

### Field Summary

- The `tiltAngle` field defines the tilt angle of the sensor (rotation around the
X axis of to the [Lidar](#lidar) node).
- The `horizontalResolution` field defines the number of points returned by
layers.
- The `fieldOfView` field defines the horizontal field of view angle of the lidar.
The value ranges from *0* to π radians.
- The `verticalFieldOfView` field defines the vertical repartition of the layers
(angle between first and last layer).
- The `NumberOfLayers` field defines the number of layers (number of lasers).
- The `minRange` field defines the minimum range of the lidar (objects closer to
the lidar than the minimum range are not seen from the lidar).
- The `maxRange` field defines the distance between the lidar and the far clipping
plane of the OpenGL view frustum. This field defines the maximum range that the
lidar can achieve and so the maximum possible value of the range image (in
meter).
- The `type` field should either be 'fixed' or 'rotating', it defines if the lidar
has a rotating or fixed head.
- The `spherical` field switches between a planar or a spherical projection. It is
highly recommended to use the spherical projection in case of fixed-head lidar.
More information on spherical projections is provided in the [spherical
projection](camera.md#spherical-projection) section of the [Camera](camera.md)
node.
- If the `noise` field is greater than 0.0, a gaussian noise is added to each
depth value of a lidar image. A value of 0.0 corresponds to no noise and thus
saves computation time. A value of 1.0 corresponds to a gaussian noise having a
standard derivation of `maxRange` meters.
- The `resolution` field defines the depth resolution of the lidar, that is the
smallest depth difference that it is able to measure. Setting this field to -1
(default) corresponds to an 'infinite' resolution (it can measure any
infinitesimal change). This field accepts any value in the interval (0.0, inf).
- The `defaultFrequency` field defines the default rotation frequency (defined in
Hz) of the head if the `type` field is set to 'rotating'. The value of this
field should be smaller or equal to the value of the `maxFrequency` field and
bigger or equal to the value of the `minFrequency` field.
- The `minFrequency` field defines the minimum rotation frequency (defined in Hz)
of the head if the `type` field is set to 'rotating'.
- The `maxFrequency` field defines the maximum rotation frequency (defined in Hz)
of the head if the `type` field is set to 'rotating'.
- A node can be inserted in the `rotatingHead` field to define the rotating head
of the lidar.
- The `compositor` field specifies the name of a compositor to apply on the depth
image. More information on compositors is provided in the
[compositor](camera.md) field description of the [Camera](camera.md) node.

> **note**:
The fields `NumberOfLayers`, `verticalFieldOfView`, `horizontalResolution` and
`fieldOfView` should respect the following constraint in order to be able to
simulate the lidar:

        NumberOfLayers < verticalFieldOfView * horizontalResolution / fieldOfView

    In case of 'rotating' lidar, the `fieldOfView` term in the constraint is
    replaced by `2 * π`.

### Lidar Functions

<a name="wb_lidar_enable">**Name**</a>

**wb\_lidar\_enable**, **wb\_lidar\_disable**, **wb\_lidar\_get\_sampling\_period** - *enable and disable lidar updates*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

void wb_lidar_enable(WbDeviceTag tag, int ms)
void wb_lidar_disable(WbDeviceTag tag)
int wb_lidar_get_sampling_period(WbDeviceTag tag)
```

**Description**

`wb_lidar_enable()` allows the user to enable a lidar update each `ms`
milliseconds.

`wb_lidar_disable()` turns the lidar off, saving computation time.

The `wb_lidar_get_sampling_period()` function returns the period given into the
`wb_lidar_enable()` function, or 0 if the device is disabled.

---

<a name="wb_lidar_enable_point_cloud">**Name**</a>

**wb\_lidar\_enable\_point\_cloud**, **wb\_lidar\_disable\_point\_cloud**, **wb\_lidar\_is\_point\_cloud\_enabled** - *enable and disable lidar point cloud mode*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

void wb_lidar_enable_point_cloud(WbDeviceTag tag)
void wb_lidar_disable_point_cloud(WbDeviceTag tag)
bool wb_lidar_is_point_cloud_enabled(WbDeviceTag tag)
```

**Description**

`wb_lidar_enable_point_cloud()` allows the user to enable the lidar point cloud
update, the point cloud array is the updated with the same sampling period as
the range image.

`wb_lidar_disable_point_cloud()` allows the user to disable the lidar point
cloud update.

The `wb_lidar_is_point_cloud_enabled()` function returns true if the point cloud
update is enabled or false otherwise.

---

<a name="wb_lidar_get_range_image">**Name**</a>

**wb\_lidar\_get\_range\_image**, **wb\_lidar\_get\_layer\_range\_image** - *get the range image and range image associate with a specific layer*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

const float *wb_lidar_get_range_image(WbDeviceTag tag)
const float *wb_lidar_get_layer_range_image(WbDeviceTag tag, int layer)
```

**Description**

The `wb_lidar_get_range_image()` function allows the user to read the contents
of the last range image grabbed by a lidar. The range image is computed using
the depth buffer produced by the OpenGL rendering. The range image is coded as
an array of single precision floating point values corresponding to the range
value of each pixel of the image. The precision of the lidar values decreases
when the objects are located farther from the near clipping plane. Pixels are
stored in scan lines running from left to right and from first to last layer.
The memory chunk returned by this function shall not be freed, as it is managed
by the lidar internally. The size in bytes of the range image can be computed as
follows:

`size` = `lidar_horizontal_resolution` * `lidar_number_of_layers` *
sizeof(float)

Attempting to read outside the bounds of this memory chunk will cause an error.

The `wb_lidar_get_layer_range_image()` function is a convenient way of getting
directly the sub range image associated with one layer.

> **note** [Python]:
The Lidar class has two methods for getting the lidar image. The
`getRangeImage()` returns a one-dimensional list of floats, while the
`getRangeImageArray()` returns a two-dimensional list of floats. Their content
are identical but their handling is of course different.

---

<a name="wb_lidar_get_point_cloud">**Name**</a>

**wb\_lidar\_get\_point\_cloud**, **wb\_lidar\_get\_layer\_point\_cloud**, **wb\_lidar\_get\_number\_of\_points** - *get the points array, points array associate with a specific layer and total number of point*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

const WbLidarPoint *wb_lidar_get_point_cloud(WbDeviceTag tag)
const WbLidarPoint *wb_lidar_get_layer_range_image(WbDeviceTag tag, int layer)
int wb_lidar_get_number_of_points(WbDeviceTag tag)
```

**Description**

The `wb_lidar_get_point_cloud()` returns the pointer to the point cloud array,
each point consists of a [WbLidarPoint](#wblidarpoint). The memory chunk
returned by this function shall not be freed, as it is managed by the lidar
internally. The size in bytes of the point cloud can be computed as follows:

`size` = `lidar_number_of_points` * sizeof(WbLidarPoint)

Attempting to read outside the bounds of this memory chunk will cause an error.

The `wb_lidar_get_layer_point_cloud()` function is a convenient way of getting
directly the sub point cloud associated with one layer.

The `wb_lidar_get_number_of_points()` function returns the total number of
points contained in the point cloud (each layer is assumed to have the same
number of points associated to).

---

<a name="wb_lidar_get_frequency">**Name**</a>

**wb\_lidar\_get\_frequency**, **wb\_lidar\_set\_frequency** - *set and get the rotating frequency*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

double wb_lidar_get_frequency(WbDeviceTag tag)
void wb_lidar_set_frequency(WbDeviceTag tag, double frequency)
```

**Description**

The `wb_lidar_get_frequency()` returns the current rotating frequency of the
lidar head (in case of rotating lidar).

The `wb_lidar_set_frequency()` sets the current rotating frequency of the lidar
head (in case of rotating lidar). The `frequency` argument should be in the
range [minFrequency; maxFrequency].

---

<a name="wb_lidar_get_horizontal_resolution">**Name**</a>

**wb\_lidar\_get\_horizontal\_resolution**, **wb\_lidar\_get\_number\_of\_layers** - *get the horizontal resolution and layer number*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

int wb_lidar_get_horizontal_resolution(WbDeviceTag tag)
int wb_lidar_get_number_of_layers(WbDeviceTag tag)
```

**Description**

The `wb_lidar_get_horizontal_resolution()` returns the horizontal resolution of
the lidar.

The `wb_lidar_get_number_of_layers()` returns the number of layers of the lidar.

---

<a name="wb_lidar_get_min_frequency">**Name**</a>

**wb\_lidar\_get\_min\_frequency**, **wb\_lidar\_get\_max\_frequency** - *get the minimum and maximum rotating frequency*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

double wb_lidar_get_min_frequency(WbDeviceTag tag)
double wb_lidar_get_max_frequency(WbDeviceTag tag)
```

**Description**

The `wb_lidar_get_min_frequency()` and `wb_lidar_get_max_frequency()` functions
return respectively the minimum and maximum allowed rotating frequency of the
head of the lidar (in case of rotating lidar).

---

<a name="wb_lidar_get_fov">**Name**</a>

**wb\_lidar\_get\_fov**, **wb\_lidar\_get\_vertical\_fov** - *get the horizontal and vertical field of view of the lidar*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

double wb_lidar_get_fov(WbDeviceTag tag)
int wb_lidar_get_vertical_fov(WbDeviceTag tag)
```

**Description**

The `wb_lidar_get_fov()` returns the horizontal field of view of the lidar.

The `wb_lidar_get_vertical_fov()` returns the vertical field of view of the
lidar.

---

<a name="wb_lidar_get_min_range">**Name**</a>

**wb\_lidar\_get\_min\_range**, **wb\_lidar\_get\_max\_range** - *get the minimum and maximum range*

{[C++](cpp-api.md#cpp_lidar)}, {[Java](java-api.md#java_lidar)}, {[Python](python-api.md#python_lidar)}, {[Matlab](matlab-api.md#matlab_lidar)}, {[ROS](ros-api.md)}

``` c
#include <webots/lidar.h>

double wb_lidar_get_min_range(WbDeviceTag tag)
double wb_lidar_get_max_range(WbDeviceTag tag)
```

**Description**

The `wb_lidar_get_min_range()` and `wb_lidar_get_max_range()` functions return
respectively the minimum and maximum range of the lidar.

