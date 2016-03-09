## Verifying your graphics driver installation

### Supported graphics cards

Webots officially supports only recent nVidia and ATI graphics adapters. So it
is recommended to run Webots on computers equipped with such graphics adapters
and up-to-date drivers provided by the card manufacturer (i.e., nVidia or ATI).
Such drivers are often bundled with the operating system (Windows, Linux and Mac
OS X), but in some case, it may be necessary to fetch it from the web site of
the card manufacturer.

### Unsupported graphics cards

Webots may nevertheless work with other graphics adapters, in particular the
Intel graphics adapters. However this is unsupported and may work or not,
without any guarantee. Some users reported success with some Intel graphics
cards after installing the latest version of the driver. Graphics drivers from
Intel may be obtained from the [Intel download center web
site](http://downloadcenter.intel.com). Linux graphics drivers from Intel may be
obtained from the [Intel Linux Graphics web
site](http://intellinuxgraphics.org). If some graphical bugs subsist, changing
the "RTT prefered mode" from the Webots OpenGL Preferences from "Framebuffer
Object" to "Pixelbuffer Object" or "Direct Copy" may fix the problems. However,
this may also impact the 3D performance.

### Upgrading your graphics driver

On Linux and Windows, you should make sure that the latest graphics driver is
installed. On the Mac the latest graphics driver are automatically installed by
the *Software Update*, so Mac users are not concerned by this section. Note that
Webots can run up to 10x slower without appropriate driver. Updating your driver
may also solve various problems, i.e., odd graphics rendering or Webots crashes.

#### Upgrading the GPU driver on Linux

On Linux, use this command to check if a hardware accelerated driver is
installed:

```
$ glxinfo | grep OpenGL
```

If the output contains the string "NVIDIA", "ATI", or "Intel", this indicates
that a hardware driver is currently installed:

```
$ glxinfo | grep OpenGL
OpenGL vendor string: NVIDIA Corporation
OpenGL renderer string: GeForce 8500 GT/PCI/SSE2
OpenGL version string: 3.0.0 NVIDIA 180.44
...
```

If you read "Mesa", "Software Rasterizer" or "GDI Generic", this indicates that
the hardware driver is currently not installed and that your computer is
currently using a slow software emulation of OpenGL:

```
$ glxinfo | grep OpenGL
OpenGL vendor string: Mesa project: www.mesa3d.org
OpenGL renderer string: Mesa GLX Indirect
OpenGL version string: 1.4 (1.5 Mesa 6.5.2)
...
```

In this case you should definitely install the hardware driver.

On Ubuntu the driver can usually be installed automatically from the `Additional
Drivers` tab of the `Software & Update` window. Otherwise you can find out what
graphics hardware is installed on your computer by using this command:

```
$ lspci | grep VGA
01:00.0 VGA compatible controller: nVidia Corporation GeForce 8500 GT (rev a1)
```

Then you can normally download the appropriate driver from the graphics hardware
manufacturer's website: [http://www.nvidia.com](http://www.nvidia.com) for an
nVidia card or [http://www.amd.com](http://www.amd.com) for a ATI graphics card.
Please follow the manufacturer's instructions for the installation.

#### Upgrading the GPU driver on Windows

1. Right-click on `My Computer`.
2. Select `Properties`.
3. Click on the `Device Manager` tab.
4. Click on the plus sign to the left of `Display adapters`. The name of the driver
appears. Make a note of it.
5. Go to the web site of your card manufacturer:
[http://www.nvidia.com](http://www.nvidia.com) for an nVidia card or
[http://www.amd.com](http://www.amd.com) for a ATI graphics card.
6. Download the driver corresponding to your graphics card.
7. Follow the instructions from the manufacturer to install the driver.

### Hardware acceleration tips

#### Linux: disable desktop effects

Depending on the graphics hardware, there may be a huge performance drop of the
rendering system (up to 10x) when *compiz* desktop effects are on. Also these
visual effects may cause some display bug where the main window of Webots is not
properly refreshed. Hence, on Ubuntu (or other Linux) we recommend to deactivate
the desktop effects. You can easily disable them using some tools like *Compiz
Config Settings Manager* or *Unity Twerk Tool*.

