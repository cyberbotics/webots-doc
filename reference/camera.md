## Camera

Derived from `Device`.


```
Camera {
  SFFloat    fieldOfView      0.7854
  SFInt32    width            64
  SFInt32    height           64
  SFString   type             "color"
  SFBool     spherical        FALSE
  SFFloat    near             0.01
  SFFloat    maxRange         1.0
  SFBool     antiAliasing     FALSE
  SFFloat    motionBlur       0.0
  SFFloat    colorNoise       0.0
  SFFloat    rangeNoise       0.0
  SFFloat    rangeResolution -1.0
  SFNode     lensDistortion   NULL
  SFNode     focus            NULL
  SFNode     zoom             NULL
  SFString   compositor       ""
}
```

### Description

The `Camera` node is used to model a robot's on-board camera or a range-finder.
The resulted image can be displayed on the 3D window. Depending on its setup,
the Camera node can model a linear camera, a lidar device, a Microsoft Kinect or
even a biological eye which is spherically distorted.

### Field Summary

- `fieldOfView`: horizontal field of view angle of the camera. The value ranges from *0* to pi radians. Since camera pixels are squares, the vertical field of view can be computed from the `width`, `height` and horizontal `fieldOfView`:*vertical FOV = fieldOfView * height / width*
- `width`: width of the image in pixels
- `height`: height of the image in pixels
- `type`: type of the camera: "color" or "range-finder". The camera types are described precisely in the corresponding subsection below.
- `spherical`: switch between a planar or a spherical projection. A spherical projection can be used for example to simulate a biological eye or a lidar device. More information on spherical projection in the corresponding subsection below.
- The `near` field defines the distance from the camera to the near clipping plane. This plane is parallel to the camera retina (i.e. projection plane). The near field determines the precision of the OpenGL depth buffer. A too small value produces depth fighting between overlaid polygons, resulting in random polygon overlaps. More information on frustums in the corresponding subsection below.
- The `maxRange` field is used only when the camera is a range-finder. In this case, `maxRange` defines the distance between the camera and the far clipping plane. The far clipping plane is not set to infinity. This field defines the maximum range that a range-finder can achieve and so the maximum possible value of the range image (in meter).
- The `antiAliasing` field switches on or off (the default) anti-aliasing effect on the camera images. Anti-aliasing is a technique that assigns pixel colors based on the fraction of the pixel's area that's covered by the primitives being rendered. Anti-aliasing makes graphics more smooth and pleasing to the eye by reducing aliasing artifacts. Aliasing artifacts can appear as jagged edges (or moiré patterns, strobing, etc.). Anti-aliasing will not be applied if it is not supported by the hardware.
- If the `motionBlur` field is greater than 0.0, the image is blurred by the motion of the camera or objects in the field of view. It means the image returned is a mix between the current view and the previous images returned by the camera. The value of this field represents the response time of the camera pixels in milliseconds, which is the amount of time a pixel takes to reach 99.5% of a new color value (the value of 99.5% was chosen since above this threshold it is not possible any more to detect color changes with a color component resolution of 8 bits). Of course smaller the time step is, better the effect is. Note that this feature is computationally expensive and can considerably reduce the simulation speed. Furthermore, it is useless to set a value smaller than the camera time step as it would not have any visible effect.
- If the `colorNoise` field is greater than 0.0, this adds a gaussian noise to each RGB channel of a color image. This field is useless in case of range-finder cameras. A value of 0.0 corresponds to remove the noise and thus saving computation time. A value of 1.0 corresponds to a gaussian noise having a standard derivation of 255 in the channel representation. More information on noise in the corresponding subsection below.
- If the `rangeNoise` field is greater than 0.0, this adds a gaussian noise to each depth value of a range-finder image. This field is useless in case of color cameras. A value of 0.0 corresponds to remove the noise and thus saving computation time. A value of 1.0 corresponds to a gaussian noise having a standard derivation of `maxRange` meters. More information on noise in the corresponding subsection below.
- `rangeResolution`: This field allows to define the depth resolution of the camera, the resolution is the smallest change that it is able to measure. Setting this field to -1 (default) means that the sensor has an 'infinite' resolution (it can measure any infinitesimal change). This field is used only when type is "range-finder" and accepts any value in the interval (0.0, inf).
- The `lensDistortion` field may contain a `CameraLensDistortion` node to specify the image distortion due to the camera lens.
- The `focus` field may contain a `CameraFocus` node to provide the camera device with a controllable focusing system. If this field is set to NULL, then no focus is available on the camera device.
- The `zoom` field may contain a `CameraZoom` node to provide the camera device with a controllable zoom system. If this field is set to NULL, then no zoom is available on the camera device.
- The `compositor` field specifies the name of a compositor to apply on the camera image. A compositor can be used to apply a shader in order to alter the original image returned by the camera, it runs on the graphic card and can therefore be very fast. Compositor is a technique provided by Ogre3d, you should respect the syntax defined by Ogre3d. Have a look at the [Ogre3d documentation](http://www.ogre3d.org/docs/manual/manual_29.html) for more information about compositors. Such a compositor can for example be used to simulate camera imperfections (e.g., lens distorion) or to run image processing directly on the graphic card (e.g., edge detection). Note that the compositor is applied at the end (i.e., after the addition of noise, etc.). The compositor resource files (compositor, material, shader, texture, etc.) should be located in a directory called `compositors` close to the world file. If the camera is contained in a PROTO file then the compositor files should be located in a directory called `compositors` close to the PROTO file. The internal compositor resource files of Webots can be used in any compositor, they are located in "WEBOTS_HOME/resources/ogre". Compositors can be added/removed at any time, even while the simulation is running. However, the compositor resource files are loaded at the same time as the world file. Therefore any modification to the compositor files will need a revert of the simulation to be taken into account.

### Camera Type

The camera type can be setup by the `type` field described above.

#### Color

The color camera allows to get color information from the OpenGL context of the
camera. This information can be get by the `wb_camera_get_image` function, while
the red, green and blue channels (RGB) can be extracted from the resulted image
by the `wb_camera_image_get_*`-like functions.

Internally when the camera is refreshed, an OpenGL context is created, and the
color or depth information is copied into the buffer which can be get throught
the `wb_camera_get_image` or the `wb_camera_get_range_image` functions. The
format of these buffers are respectively BGRA (32 bits) and float (16 bits). We
recommend to use the `wb_camera_image_get_*`-like functions to access the buffer
because the internal format could change.

#### Range-Finder

The range-finder camera allows to get depth information (in meters) from the
OpenGL context of the camera. This information is obtained through the
`wb_camera_get_range_image` function, while depth information can be extracted
from the returned image by using the `wb_camera_range_image_get_depth` function.

Internally when the camera is refreshed, an OpenGL context is created, and the
z-buffer is copied into a buffer of `float`. As the z-buffer contains scaled and
logarithmic values, an algorithm linearizes the buffer to metric values between
`near` and `maxRange`. This is the buffer which is accessible by the
`wb_camera_get_range_image` function.

Range-finder cannot see transparent objects. An object can be semi-transparent
either if its texture has an alpha channel, or if its `Material`.`transparency`
field is not equal to 1.

### Frustum

The frustum is the truncated pyramid defining what is visible from the camera.
Any 3D shape completely outside this frustum won't be rendered. Hence, shapes
located too close to the camera (standing between the camera and the near plane)
won't appear. It can be displayed with magenta lines by enabling the
`View|Optional Rendering|Show Camera Frustums` menu item. The `near` field
defines the position of the near clipping plane (x, y, -near). The `fieldOfView`
field defines the horizontal angle of the frustum. The `fieldOfView`, `width`
and `height` fields define the vertical angle of the frustum according to the
above formula.

Generally speaking there is no far clipping plane while this is common in other
OpenGL programs. In Webots, a camera can see as far as needed. Nevertheless, a
far clipping plane is artificially added in the case of range-finder cameras
(i.e. the resulted values are bounded by the `maxRange` field).

In the case of the spherical cameras, the frustum is quite different and
difficult to represent. In comparison with the frustum description above, the
near and the far planes are transformed to be sphere parts having their center
at the camera position, and the `fieldOfView` can be greater than Pi.

### Noise

It is possible to add quickly a white noise on the cameras by using the
`colorNoise` and the `rangeNoise` fields (applied respectively on the color
cameras and on the range-finder cameras). A value of `0.0` corresponds to an
image without noise. For each channel of the image and at each camera refresh, a
gaussian noise is computed and added to the channel. This gaussian noise has a
standard deviation corresponding to the noise field times the channel range. The
channel range is 256 for a color camera and `maxRange` for a range-finder
camera.

### Spherical projection

OpenGL is designed to have only planar projections. However spherical
projections are very useful for simulating a lidar, a camera pointing on a
curved mirror or a biological eye. Therefore we implemented a camera mode
rendering spherical projections. It can be enabled simply by switching on the
corresponding `spherical` field described above.

Internally, depending on the field of view, a spherical camera is implemented by
using between 1 to 6 OpenGL cameras oriented towards the faces of a cube (the
activated cameras are displayed by magenta squares when the `View|Optional
Rendering|Show Camera Frustums` menu item is enabled). Moreover an algorithm
computing the spherical projection is applied on the result of the subcameras.

So this mode is costly in terms of performance! Reducing the resolution of the
cameras and using a `fieldOfView` which minimizes the number of activated
cameras helps a lot to improve the performances if needed.

When the camera is spherical, the image returned by the `wb_camera_get_image` or
the `wb_camera_get_range_image` functions is a 2-dimensional array (s,t) in
spherical coordinates.

Let `hFov` be the horizontal field of view, and let `theta` be the angle in
radian between the `(0, 0, -z)` relative coordinate and the relative coordinate
of the target position along the `xz` plane relative to the camera, then `s=0`
corresponds to a `theta` angle of `-hFov/2`, `s=(width-1)/2` corresponds to a
`theta` angle of 0, and `s=width-1` corresponds to a `theta` angle of `hFov/2`.

Similarly, let `vFov` be the vertical field of view (defined just above), and
`phi` the angle in radian between the `(0, 0, -z)` relative coordinate and the
relative coordinate of the target position along the `xy` plane relative to the
camera, `t=0` corresponds to a `phi` angle of `-vFov/2`, `t=(height-1)/2`
corresponds to a `phi` angle of 0, and `t=height-1` corresponds to a `phi` angle
of `vFov/2`).

### Overlay Image

<center>
![Camera overlay image](png/camera_overlay.png)

####Camera overlay image
</center>

The camera image is shown by default on top of the 3D window with a magenta
border, see . The user can move this camera image at the desired position using
the mouse drag and drop and resize it by clicking on the icon at the bottom
right corner. Additionally a close button is available on the top right corner
to hide the image. Once the robot is selected, it is also possible to show or
hide the overlay images from the `Camera Devices` item in `Robot` menu.

It is also possible to show the camera image in an external window by double-
clicking on it. After doing it, the overlay disappears and the new window pops
up. Then, after closing the window, the overlay will be automatically restored.

### Camera Functions

