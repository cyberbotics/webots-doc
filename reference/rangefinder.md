## RangeFinder

Derived from [Device](device.md).

```
RangeFinder {
  SFFloat    fieldOfView      0.7854
  SFInt32    width            64
  SFInt32    height           64
  SFBool     spherical        FALSE
  SFFloat    minRange         0.01
  SFFloat    maxRange         1.0
  SFFloat    motionBlur       0.0
  SFFloat    noise            0.0
  SFFloat    resolution      -1.0
  SFNode     lens             NULL
  SFString   compositor       ""
}
```

### Description

The [RangeFinder](#rangefinder) node is used to model a robot's on-board
range-finder (depth camera). The resulting image can be displayed on the 3D
window.

The range-finder measures depth information (in meters) from an OpenGL
rendering. Each time a range-finder is refreshed, an OpenGL rendering is
computed, and the z-buffer is copied into a buffer of `float`. As the z-buffer
contains scaled and logarithmic values, an algorithm linearizes the buffer to
metric values between `minRange` and `maxRange`. This is the buffer which is
accessible by the `wb_range_finder_get_range_image` function.

Range-finder cannot see semi-transparent objects. An object can be
semi-transparent either if its texture has an alpha channel, or if its
[Material](material.md).`transparency` field is not equal to 1.

### Field Summary

- `fieldOfView`: horizontal field of view angle of the range-finder. The value
ranges from *0* to π radians. Since range-finder pixels are squares, the
vertical field of view can be computed from the `width`, `height` and horizontal
`fieldOfView`:

    *vertical FOV = fieldOfView * height / width*

- `width`: width of the image in pixels

- `height`: height of the image in pixels

- `spherical`: switch between a planar or a spherical projection. A spherical
projection can be used for example to simulate a lidar device. More information
on spherical projections is provided in the [spherical
projection](camera.md#spherical-projection) section of the [Camera](camera.md)
node.

- The `minRange` field defines the distance from the range-finder to the near
clipping plane of the OpenGL view frustum. This plane is parallel to the
range-finder retina (i.e., projection plane). The minRange field determines the
precision of the OpenGL depth buffer. A too small value produces depth fighting
between overlaid polygons, resulting in random polygon overlaps. More
information about the frustrum is provided in the [frustum](camera.md#frustum)
section of the [Camera](camera.md) node.

- The `maxRange` defines the distance between the range-finder and the far
clipping plane of the OpenGL view frustum. This field defines the maximum range
that a range-finder can achieve and so the maximum possible value of the range
image (in meter).

- If the `motionBlur` field is greater than 0.0, the image is blurred by the
motion of the range-finder or objects in the field of view. More information on
motion blur is provided in the [motionBlur](camera.md) field description of the
[Camera](camera.md) node.

- If the `noise` field is greater than 0.0, a gaussian noise is added to each
depth value of a range-finder image. A value of 0.0 corresponds to no noise and
thus saves computation time. A value of 1.0 corresponds to a gaussian noise
having a standard derivation of `maxRange` meters.

- `resolution`: This field defines the depth resolution of the range-finder, that
is the smallest depth difference that it is able to measure. Setting this field
to -1 (default) corresponds to an 'infinite' resolution (it can measure any
infinitesimal change). This field is accepts any value in the interval (0.0,
inf).

- The `lens` field may contain a [Lens](lens.md) node to specify the image
distortion due to the lens geometry.

- The `compositor` field specifies the name of a compositor to apply on the depth
image. More information on compositors is provided in the
[compositor](camera.md) field description of the [Camera](camera.md) node.

### Overlay Image

%figure "RangeFinder overlay image"

![range_finder_overlay.png](images/range_finder_overlay.png)

%end

The range-finder image is shown by default on top of the 3D window with a yellow
border, see [this figure](#rangefinder-overlay-image). The user can move this
range-finder image at the desired position using the mouse drag and drop and
resize it by clicking on the icon at the bottom right corner. Additionally a
close button is available on the top right corner to hide the image. Once the
robot is selected, it is also possible to show or hide the overlay images from
the `RangeFinder Devices` item in `Robot` menu.

It is also possible to show the range-finder image in an external window by
double-clicking on it. After doing it, the overlay disappears and a new window
pops up. Then, after closing the window, the overlay will be automatically
restored.

### RangeFinder Functions

<a name="wb_range_finder_enable">**Name**</a>

**wb\_range\_finder\_enable**, **wb\_range\_finder\_disable**, **wb\_range\_finder\_get\_sampling\_period** - *enable and disable range-finder updates*

{[C++](cpp-api.md#cpp_range_finder)}, {[Java](java-api.md#java_range_finder)}, {[Python](python-api.md#python_range_finder)}, {[Matlab](matlab-api.md#matlab_range_finder)}, {[ROS](ros-api.md)}

``` c
#include <webots/range_finder.h>

void wb_range_finder_enable(WbDeviceTag tag, int ms)
void wb_range_finder_disable(WbDeviceTag tag)
int wb_range_finder_get_sampling_period(WbDeviceTag tag)
```

**Description**

`wb_range_finder_enable()` allows the user to enable a range-finder update each
`ms` milliseconds.

`wb_range_finder_disable()` turns the range-finder off, saving computation time.

The `wb_range_finder_get_sampling_period()` function returns the period given
into the `wb_range_finder_enable()` function, or 0 if the device is disabled.

---

<a name="wb_range_finder_get_fov">**Name**</a>

**wb\_range\_finder\_get\_fov** - *get field of view for a range-finder*

{[C++](cpp-api.md#cpp_range_finder)}, {[Java](java-api.md#java_range_finder)}, {[Python](python-api.md#python_range_finder)}, {[Matlab](matlab-api.md#matlab_range_finder)}, {[ROS](ros-api.md)}

``` c
#include <webots/range_finder.h>

double wb_range_finder_get_fov(WbDeviceTag tag)
```

**Description**

These functions allow the controller to get the value of the field of view (fov)
of a range-finder.

---

<a name="wb_range_finder_get_width">**Name**</a>

**wb\_range\_finder\_get\_width**, **wb\_range\_finder\_get\_height** - *get the size of the range-finder image*

{[C++](cpp-api.md#cpp_range_finder)}, {[Java](java-api.md#java_range_finder)}, {[Python](python-api.md#python_range_finder)}, {[Matlab](matlab-api.md#matlab_range_finder)}, {[ROS](ros-api.md)}

``` c
#include <webots/range_finder.h>

int wb_range_finder_get_width(WbDeviceTag tag)
int wb_range_finder_get_height(WbDeviceTag tag)
```

**Description**

These functions return the width and height of a range-finder image as defined
in the corresponding [RangeFinder](#rangefinder) node.

---

<a name="wb_range_finder_get_min_range">**Name**</a>

**wb\_range\_finder\_get\_min\_range**, **wb\_range\_finder\_get\_max\_range** - *get the minimum and maximum range of the range-finder device*

{[C++](cpp-api.md#cpp_range_finder)}, {[Java](java-api.md#java_range_finder)}, {[Python](python-api.md#python_range_finder)}, {[Matlab](matlab-api.md#matlab_range_finder)}, {[ROS](ros-api.md)}

``` c
#include <webots/range_finder.h>

double wb_range_finder_get_min_range(WbDeviceTag tag)
double wb_range_finder_get_max_range(WbDeviceTag tag)
```

**Description**

These functions return the minRange and maxRange parameters of a range-finder
device as defined in the corresponding [RangeFinder](#rangefinder) node.

---

<a name="wb_range_finder_get_range_image">**Name**</a>

**wb\_range\_finder\_get\_range\_image**, **wb\_range\_finder\_image\_get\_depth** - *get the range image and range data from a range-finder*

{[C++](cpp-api.md#cpp_range_finder)}, {[Java](java-api.md#java_range_finder)}, {[Python](python-api.md#python_range_finder)}, {[Matlab](matlab-api.md#matlab_range_finder)}, {[ROS](ros-api.md)}

``` c
#include <webots/range_finder.h>

const float *wb_range_finder_get_range_image(WbDeviceTag tag)
float wb_range_finder_image_get_depth(const float *range_image, int width, int x, int y)
```

**Description**

The `wb_range_finder_get_range_image()` macro allows the user to read the
contents of the last range image grabbed by a range-finder. The range image is
computed using the depth buffer produced by the OpenGL rendering. Each pixel
corresponds to the distance expressed in meter from the object to the plane
defined by the equation *z = 0* within the coordinates system of the
range-finder. The bounds of the range image is determined by the near clipping
plane (defined by the `minRange` field) and the far clipping plane (defined by
the `maxRange` field). The range image is coded as an array of single precision
floating point values corresponding to the range value of each pixel of the
image. The precision of the range-finder values decreases when the objects are
located farther from the near clipping plane. Pixels are stored in scan lines
running from left to right and from top to bottom. The memory chunk returned by
this function shall not be freed, as it is managed by the range-finder
internally. The size in bytes of the range image can be computed as follows:

`size` = `range_finder_width` * `range_finder_height` * sizeof(float)

Attempting to read outside the bounds of this memory chunk will cause an error.

The `wb_range_finder_image_get_depth()` macro is a convenient way to access a
range value, directly from its pixel coordinates. The `range_finder_width`
parameter can be obtained from the `wb_range_finder_get_width()` function. The
`x` and `y` parameters are the coordinates of the pixel in the image.

> **note** [Python]:
The RangeFinder class has two methods for getting the range-finder image. The
`getRangeImage()` returns a one-dimensional list of floats, while the
`getRangeImageArray()` returns a two-dimensional list of floats. Their content
are identical but their handling is of course different.

---

<a name="wb_range_finder_save_image">**Name**</a>

**wb\_range\_finder\_save\_image** - *save a range-finder image in either PNG or JPEG format*

{[C++](cpp-api.md#cpp_range_finder)}, {[Java](java-api.md#java_range_finder)}, {[Python](python-api.md#python_range_finder)}, {[Matlab](matlab-api.md#matlab_range_finder)}, {[ROS](ros-api.md)}

``` c
#include <webots/range_finder.h>

int wb_range_finder_save_image(WbDeviceTag tag, const char *filename, int quality)
```

**Description**

The `wb_range_finder_save_image()` function allows the user to save a `tag`
image which was previously obtained with the `wb_range_finder_get_image()`
function. The image is saved in a file in either PNG or JPEG format. The image
format is specified by the `filename` parameter. If `filename` is terminated by
`.png`, the image format is PNG. If `filename` is terminated by `.jpg` or
`.jpeg`, the image format is JPEG. Other image formats are not supported. The
`quality` parameter is useful only for JPEG images. It defines the JPEG quality
of the saved image. The `quality` parameter should be in the range 1 (worst
quality) to 100 (best quality). Low quality JPEG files will use less disk space.
For PNG images, the `quality` parameter is ignored.

The return value of the `wb_range_finder_save_image()` is 0 in case of success.
It is -1 in case of failure (unable to open the specified file or unrecognized
image file extension).

