## Preferences

The Webots preferences can be modified by a dialog box which can be open from
the `Webots / Preferences` menu item on Mac, and from the `Tools / Preferences`
menu item on the other operating systems.

The dialog box is separated into tabs. Each of the following subsection
corresponds to one of these tabs.

### General

The `General` tab contains various preferences about the application.

- The `Language` option allows you to choose the language of Webots user interface
(restart needed).
- The `Startup mode` allows you to choose the state of the simulation when Webots
is started (pause, realtime, run, fast; see the `Simulation` menu).
- The `Editor font` defines the font to be used in Webots text editor and in the
Console. It is recommended to select a fixed width font for better source code
display. The default value of this preference is "Consolas,10" on Windows,
"Courier,14" on Mac and "Monospace" on linux.
- The `Number of threads` defines how many threads can be created by Webots at
maximum. The recommended value matches with the number of logical cores of the
computer processor. It may be interesting to reduce this value in some specific
cases, for example when another process requires intensively other cores. For
now this value affects only the physical engine speed, and the controller
compilation speed. Note that this is the maximum number of threads allowed, but
the actual number of threads used is the one defined in the `optimalThreadCount`
field of the `WorldInfo` node.
- The `Warnings: Display save warning only for scene tree edit` checkbox prevents Webots from displaying any warning dialog window when you quit, revert or load a new world after the current world was modified by either changing the viewpoint, dragging, rotating, applying a force or applying a torque to an object. It will however still display a warning if the world was modified from the scene tree.
- The `Update policy: Check for Webots updates on startup` checkbox allows Webots to check if a new version is available for download at every startup. If available, a dialog window will inform you about it.

### OpenGL

The `OpenGL` tab contains preferences about setting the 3D rendering abilities.
The initial parameters of these settings may vary from one computer to another
depending on the GPU OpenGL abilities.

- The `RTT preferred mode` option allows you to modify the method used to create
the Camera device images. The methods are sorted from the most efficient one to
the least efficient one.

- The `Main 3D view anti-aliasing` option allows you to enable Multisample Anti-Aliasing
on the 3D scene in Webots. This option can lead to reduced performance, but it improves 
graphical fidelity significantly. It is disabled by default on systems that do not meet 
our minimum requirements. Note that this option does not apply to any Camera rendering, 
this is managed by the `Disable camera anti-aliasing` setting in the same tab of the preferences dialog.

- The `Disable shadows` option allows you to disable completely the shadows in the
3D view and in the Camera rendering, whatever the values of the
*Light.castShadows* fields.

    The global performances can be improved by disabling this feature, but on the
    other hand the rendering is more difficult to understand, and less pretty.

- The `Disable shader` option allows you to use the regular OpenGL shading model,
instead of a custom shading. This custom shading model computes the light
effects on the 3D objects per pixel instead of per vertex, resulting in a much
smoother rendering. It may be interesting to disbale this feature on old GPU if
the shaders are not well supported.

- The `Disable camera anti-aliasing` option allows you to bypass all the
*Camera.antialiasing* fields and to disable this feature. We observed that some
hardware doesn't support the OpenGL feature about anti-aliasing when rendering
into a texture (RTT).
