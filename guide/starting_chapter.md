# Getting Started with Webots

This chapter gives an overview of Webots windows and menus.

## Introduction to Webots

### What is Webots?

Webots is a professional mobile robot simulation software package. It offers a
rapid prototyping environment, that allows the user to create 3D virtual worlds
with physics properties such as mass, joints, friction coefficients, etc. The
user can add simple passive objects or active objects called mobile robots.
These robots can have different locomotion schemes (wheeled robots, legged
robots, or flying robots). Moreover, they may be equipped with a number of
sensor and actuator devices, such as distance sensors, drive wheels, cameras,
motors, touch sensors, emitters, receivers, etc. Finally, the user can program
each robot individually to exhibit the desired behavior. Webots contains a large
number of robot models and controller program examples to help users get
started.

Webots also contains a number of interfaces to real mobile robots, so that once
your simulated robot behaves as expected, you can transfer its control program
to a real robot like e-puck, DARwIn-OP, Nao, etc. Adding new interfaces is
possible through the related sytem.

### What can I do with Webots?

Webots is well suited for research and educational projects related to mobile
robotics. Many mobile robotics projects have relied on Webots for years in the
following areas:

### What do I need to know to use Webots?

You will need a minimal amount of technical knowledge to develop your own
simulations:

### Webots simulation

A Webots simulation is composed of following items:

### What is a world?

A world, in Webots, is a 3D description of the properties of robots and of their
environment. It contains a description of every object: position, orientation,
geometry, appearance (like color or brightness), physical properties, type of
object, etc. Worlds are organized as hierarchical structures where objects can
contain other objects (like in VRML97). For example, a robot can contain two
wheels, a distance sensor and a joint which itself contains a camera, etc. A
world file doesn't contain the controller code of the robots; it only specifies
the name of the controller that is required for each robot. Worlds are saved in
".wbt" files. The ".wbt" files are stored in the "worlds" subdirectory of each
Webots project.

### What is a controller?

A controller is a computer program that controls a robot specified in a world
file. Controllers can be written in any of the programming languages supported
by Webots: C, C++, Java, Python or `MATLAB`. When a simulation starts, Webots
launches the specified controllers, each as a separate process, and it
associates the controller processes with the simulated robots. Note that several
robots can use the same controller code, however a distinct process will be
launched for each robot.

Some programming languages need to be compiled (C and C++) other languages need
to be interpreted (Python and `MATLAB`) and some need to be both compiled and
interpreted (Java). For example, C and C++ controllers are compiled to platform-
dependent binary executables (for example ".exe" under Windows). Python and
`MATLAB` controllers are interpreted by the corresponding run-time systems
(which must be installed). Java controller need to be compiled to byte code
(".class" files or ".jar") and then interpreted by a Java Virtual Machine.

The source files and binary files of each controller are stored together in a
controller directory. A controller directory is placed in the "controllers"
subdirectory of each Webots project.

### What is a Supervisor?

The Supervisor is a privileged type of Robot that can execute operations that
can normally only be carried out by a human operator and not by a real robot.
The Supervisor is normally associated with a controller program that can also be
written in any of the above mentioned programming languages. However in contrast
with a regular Robot controller, the Supervisor controller will have access to
privileged operations. The privileged operations include simulation control, for
example, moving the robots to a random position, making a video capture of the
simulation, etc.

## Starting Webots

The first time you start Webots it will open the "Welcome to Webots!" menu with
a list of possible starting points.

### Linux

Open a terminal and type `webots` to launch Webots.

### Mac OS X

Open the directory in which you installed the Webots package and double-click on
the Webots icon.

### Windows

On Windows 10 and Windows 7, open the `Start` menu, go to the `Program Files >
Cyberbotics` menu and click on the `Webots
webots_major_version.webots_minor_version.webots_bugfix_version` menu item.

On Windows 8, open the `Start` screen, scroll to the screen's right until
spotting the Cyberbotics section and click on the `Webots` icon.

### Command Line Arguments

Following command line options are available when starting Webots from a
Terminal (Linux/Mac) or a Command Prompt (Windows): `SYNOPSIS: webots [options]
[worldfile] OPTIONS: --minimize                  minimize Webots window on
startup --mode=ltmodegt               choose startup mode (overrides application
preferences) argument ltmodegt must be one of: pause, realtime, run or fast
(Webots PRO is required to use: --mode==run or --mode=fast) --help
display this help message and exit --sysinfo                   display
information of the system and exit --version                   display version
information and exit --uuid                      display the UUID of the
computer and exit --stdout                    redirect the controller stdout to
the terminal --stderr                    redirect the controller stderr to the
terminal --disable-modules-download  skip the check for module updates --force-
modules-download    automatically download module updates (if any) at startup
--start-streaming-server    starts the Webots streaming server (Webots PRO is
required) [="key[=value];..."]         parameters may be given as an option:
port=1234 : starts the streaming server on port 1234 monitorActivity : prints a
dot '.' on stdout every 5 seconds disableStandardStreamsRedirection : disables
the streaming of the standard output and error streams --log-performance="ltfile
pathgt[,ltsteps countgt]" measure the performance of Webots and log it in the
specified ltfile pathgt file. ltsteps countgt is an optional integer value that
specifies how many steps are analyzed. If '--sysinfo' is also set then the
system information are printed in the log file.`

The optional `worldfile` argument specifies the name of a .wbt file to open. If
it is not specified, Webots attempts to open the most recently opened file.

The `--minimize` option is used to minimize (iconize) Webots window on startup.
This also skips the splash screen and the eventual Welcome Dialog. This option
can be used to avoid cluttering the screen with windows when automatically
launching Webots from scripts. Note that Webots PRO does automatically enable
the `Fast` mode when `--minimize` is specified.

The `--mode=ltmodegt` option can be used to start Webots in the specified
execution mode. The four possible execution modes are: `pause`, `realtime`,
`run` and `fast`; they correspond to the simulation control buttons of Webots'
graphical user interface. This option overrides, but does not modify, the
startup mode saved in Webots' preferences. For example, type `webots
--mode=pause filename.wbt` to start Webots in `pause` mode. Note that `run` and
`fast` modes are only available in Webots PRO.

The `--sysinfo` option displays misc information about the current system on the
standard output stream and quits Webots.

The `--stdout` and `--stderr` options have the effect of redirecting Webots
console output to the calling terminal or process. For example, this can be used
to redirect the controllers output to a file or to pipe it to a shell command.
`--stdout` redirects the *stdout* stream of the controllers, while `--stderr`
redirects the *stderr* stream. Note that the *stderr* stream may also contain
Webots error or warning messages.

The `--disable-modules-download` option disables the download of new modules and
therefore prevents the `Webots Update Manager` window from poping up. The
`--force-modules-download` will instead force the automatic download of new
modules (if available) without asking the user. Both options are mutually
exclusive.

The `--start-streaming-server` option starts the Webots streaming server. An
option can be given to change the default parameters of the streaming server.
This option is a string containing a list of parameter keys and their values
separated by semicolons. The supported options are described in .

For example, the following command will start Webots with the streaming server
enabled on the TCP port '1234': `webots --start-streaming-server="port:1234"`

## The User Interface

Webots GUI is composed of four principal windows: the *3D window* that displays
and allows to interact with the 3D simulation, the *Scene tree* which is a
hierarchical representation of the current world, the *Text editor* that allows
to edit source code, and finally, the *Console* that displays both compilation
and controller outputs.

![Webots GUI](png/main_window.png)
**Webots GUI**

The GUI has nine menus: `File, Edit, View, Simulation, Build, Robot, Tools,
Wizards` and `Help`.

### File Menu

The `File` menu allows you to perform usual file operations: loading, saving,
etc.

The `New World` menu item (and button) opens a new world in the simulation
window containing only an `ElevationGrid`, displayed as a chessboard of 10 x 10
squares on a surface of 1 m x 1 m.

The `Open World...` menu item (and button) opens a file selection dialog that
allows you to choose a ".wbt" file to load.

The `Open Recent World` menu item gives the possibility of reopening a ".wbt"
file that was opened recently by choosing it from the list displayed in the
submenu.

The `Open Sample World` menu item opens a dialog listing all the available
sample worlds where it is possible to search for a specific ".wbt" file to load
by entering the file name or part of it in the search field.

The `Save World` menu item (and button) saves the current world using the
current filename (the filename that appears at the top of the main window). On
each `Save` the content of the ".wbt" file is overwritten and no backup copies
are created by Webots, therefore you should use this button carefully and
eventually do safety copies manually.

The `Save World As...` menu item (and button) saves the current world with a new
filename entered by the user. Note that a ".wbt" file should always be saved in
a Webots project directory, and in the "worlds" subdirectory, otherwise it will
not be possible to reopen the file.

The `Revert World` menu item (and button) reloads the current world from the
saved version and restarts the simulation from the beginning.

The `New Text File` menu item (and button) opens an empty text file in the text
editor.

The `Open Text File...` menu item (and button) opens a file selection dialog
that allows you to choose a text file (for example a ".java" file) to load.

The `Save Text File` menu item (and button) saves the current text file.

The `Save Text File As...` menu item (and button) saves the current text file
with a new filename entered by the user.

The `Save All Text Files` menu item saves all the opened and unsaved text files.

The `Revert Text File` menu item (and button) reloads the text file from the
saved version.

The `Print Preview...` menu item opens a window allowing you to manage the page
layout in order to print files from the text editor.

The `Print...` menu item opens a window allowing you to print the current file
of the text editor.

The `Import VRML 2.0...` menu item adds VRML97 objects at the end of the scene
tree. These objects come from a VRML97 file you must specify. This feature is
useful for importing complex shapes that were modeled in a 3D modelling program,
then exported to VRML97 (or VRML 2.0). Most 3D modelling software, like 3D
Studio Max, Maya, AutoCAD, Pro Engineer, AC3D, or Art Of Illusion, include the
VRML97 (or VRML 2.0) export feature. Be aware that Webots cannot import files in
VRML 1.0 format. Once imported, these objects appear as `Group`, `Transform` or
`Shape` nodes at the bottom of the scene tree. You can then either turn these
objects into Webots nodes (like `Solid`, `DifferentialWheels`, etc.) or cut and
paste them into the `children` list of existing Webots nodes.

The `Export VRML 2.0...` item allows you to save the currently loaded world as a
".wrl" file, conforming to the VRML97 standard. Such a file can, in turn, be
opened with any VRML97 viewer and most 3D modeling software.

The `Take Screenshot...` item allows you to take a screenshot of the current
view in Webots. It opens a file dialog to save the current view as a PNG or JPG
image.

The `Make Movie...` item allows you to create MPEG movies (Linux and Mac OS X)
or AVI movies (Windows). Once the movie recording is started, this item is
changed in `Stop Movie...`. During the recording, it is possible to the change
the running mode and pause the simulation. However, frames are only captured
during Webots steps and not when the simulation is paused.

The `Export HTML5 Model...` item allows you to export the current world as an
interactive 3D ".html" file, using the X3DOM web standard, based on WebGL. This
is especially useful for publishing Webots-created worlds on the Web. X3DOM is
supported in recent versions of Firefox, Chrome, Internet Explorer and Safari on
Mac OS X (see details on the `X3DOM web site`).

The `Make HTML5 Animation...` item allows you to record a simulation as a 3D
animation and publish it on a HTML5 web page. The result is similar to a movie
with playback controls, except that you can change the viewpoint at any time.
Several files are generated: an X3D file containing the 3D scene, a JSON file
containing the animation data and a HTML5 file displaying the result using X3DOM
and jQuery. Once the animation recording is started, this item is changed to
`Stop HTML5 Animation...` and can be used to stop the animation recording.

The `Quit Webots` terminates the current simulation and closes Webots.

### Edit Menu

The `Edit` menu provides usual text edition functions to manipulate files opened
in the *Text editor*, such as Copy, Paste, Cut, etc.

### View Menu

The `View` menu allows to control the viewing in the simulation window.

The `Follow Object` menu item allows to switch between a fixed (static)
viewpoint and a viewpoint that follows a mobile object (usually a robot). If you
want the viewpoint to follow an object, first you need to select the object with
the mouse and then check the `Follow Object` menu item. Note that the `Follow
Object` state is saved in the ".wbt" file.

The `Restore Viewpoint` item restores the viewpoint's position and orientation
to their initial settings when the file was loaded or reverted. This feature is
handy when you get lost while navigating in the scene, and want to return to the
original viewpoint.

The `Fullscreen` item enables and disables displaying the 3D window on the
entire screen.

The `Projection` radio button group allows to choose between the `Perspective
Projection` (default) and the `Orthographic Projection` mode for Webots
simulation window. The *perspective* mode corresponds to a natural projection:
in which the farther an object is from the viewer, the smaller it appears in the
image. With the *orthographic* projection, the distance from the viewer does not
affect how large an object appears. Furthermore, with the *orthographic* mode,
lines which are parallel in the model are drawn parallel on the screen,
therefore this projection is sometimes useful during the modelling phase. No
shadows are rendered in the *orthographic* mode.

The `Rendering` radio button group allows to choose between the `Plain
Rendering` (default) and the `Wireframe` modes for Webots simulation window. In
*plain rendering* mode, the objects are rendered with their geometrical faces,
materials, colors and textures, in the same way they are usually seen by an eye
or a camera. In *wireframe rendering* mode, only the segments of the renderable
primitives are rendered. This mode can be useful to debug your meshes. If the
*wireframe rendering* mode and the `View > Optional Rendering > Show All
Bounding Objects` toggle button are both activated, then only bounding objects
are drawn (not the renderable primitives). This can be used to debug a problem
with the collision detection.

Finally, the `Optional Rendering` submenu allows to display, or to hide,
supplementary information. These rendering are displayed only in the main
rendering and hide in the robot camera. They are used to understand better the
behavior of the simulation.

The `Show Coordinate System` allows to display, or to hide, the global
coordinate system at the bottom right corner of the 3D window as red, green and
blue arrows representing the x, y and z axes respectively.

The `Show All Bounding Objects` allows to display, or to hide, all the bounding
objects (defined in the *boundingObject* fields of every *Solid* node). Bounding
objects are represented by white lines. These lines turn rose when a collision
occurs and blue when the solid is idle, i.e., it comes to rest and it doesn't
interact with any other active solid.

The `Show Contact Points` allows to display, or to hide, the contact points
generated by the collision detection engine. Contact points that do not generate
a corresponding contact force are not shown. A contact force is generated only
for objects simulated with physics (`Physics` node required). A step is required
for taking this operation into account.

The `Show Connector axes` allows to display, or to hide, the connector axes. The
rotation alignments are depicted in black while the y and z axes respectively in
green and blue.

The `Show Joint axes` allows to display, or to hide, the joint axes. The joint
axes are represented by black lines.

The `Show Camera frustums` allows to display, or to hide, the OpenGL culling
frustum for every camera in the scene, using a magenta wire frame. The OpenGL
culling frustum is a truncated pyramid corresponding to the field of view of a
camera. The back of the pyramid is not represented because the far plane is set
to infinity. More information about this concept is available in the OpenGL
documentation.

The `Show Distance Sensor rays` allows to display, or to hide, the rays casted
by the distance sensor devices. These rays are drawn as red lines (which become
green beyond collision points). Their length corresponds to the maximum range of
the device.

The `Show Light Sensor rays` allows to display, or to hide, the rays casted by
the light sensor devices. These rays are drawn as yellow lines.

The `Show Lights` allows to display, or to hide, the lights (including
PointLights and SpotLights). DirectionalLights aren't represented. PointLights
and SpotLights are represented by a colored circle surrounded by a flare.

The `Show Pen Painting Rays` allows to display, or to hide, the rays in which
the pen devices paint. These rays are drawn as violet lines if painting is
enabled, otherwise as gray lines.

The `Show Center Of Mass and Support Polygon` allows to display, or to hide,
both the global center of mass of a selected solid (with non NULL `Physics`
node) and its support polygon. By support polygon we mean the projection of the
convex hull of the solid's contact points on the horizontal plane which contains
the lowest one. In addition, the projection of the center of mass in the latter
plane is rendered in green if it lies inside the support polygon (static
equilibrium), red otherwise. This rendering option can be activated only for
solids with no other solid at their top.

If the `Disable selection` option is enabled, it prevents you from changing the
selected solid node when clicking on the 3D window. This is particularly useful
during the modeling phase, when you want to change the viewpoint without
modifying the visible and selected fields in the scene tree.

### Simulation Menu

The `Simulation` menu is used to control the execution of the simulation.

The `Pause` menu item (and button) pauses the simulation.

The `Step` menu item (and button) executes one basic time step of simulation.
The duration of this step is defined in the `basicTimeStep` field of the
`WorldInfo` node, and can be adjusted in the scene tree window to suit your
needs.

The `Real-time` menu item (and button) runs the simulation at real-time until it
is interrupted by `Pause` or `Step`. In run mode, the 3D display of the scene is
refreshed every *n* basic time steps, where *n* is defined in the
`displayRefresh` field of the `WorldInfo` node.

The `Run` menu item (and button) is like `Real-time`, except that it runs as
fast as possible (Webots PRO only).

The `Fast` menu item (and button) is like `Run`, except that no graphical
rendering is performed (Webots PRO only). As the graphical rendering is disabled
(black screen) this allows for a faster simulation and therefore this is well
suited for cpu-intensive simulations (genetic algorithms, vision, learning,
etc.).

### Build Menu

The `Build` menu provides the functionality to compile (or cross-compile)
controller code. The build menu is described in more details `here`.

### Robot Menu

The `Robot` menu provides actions specific to `Robot` nodes. Some actions of
this menu are active only when a robot is selected in the 3D window or when
there is only one robot in the simulation:

The `Edit Controller` menu item opens the source file of the controller of the
selected robot.

The `Camera Devices` submenu contains the list of all the camera devices of the
selected robot and lets the user show or hide single camera overlay images by
checking or unchecking the corresponding item. Camera overlays differ from the
display overlays because of their magenta border. Note that if the `Hide All
Camera Overlays` item is checked, then the camera device overlays will not be
visible in the 3D view independently from the status of `Camera Devices` menu
items. A `Camera Devices` menu  item is disabled if the overlay's texture is
shown in an external window by double-clicking on it.

The `Display Devices` submenu contains the list of all the display devices of
the selected robot and lets the user show or hide single display overlay images
by checking or unchecking the corresponding item. Display overlays differ from
the camera overlays because of their cyan border. Note that if the `Hide All
Display Overlays` item is checked, then the display device overlays will not be
visible in the 3D view independently from the status of `Display Devices` menu
items. A `Display Devices` menu item is disabled if the overlay's texture is
shown in an external window by double-clicking on it.

On the other hand the following items are always active and apply to all the
robot in the world:

The `Hide All Camera Overlays` option hides all the camera devices overlays in
the 3D view independently from the specific robot's device option set in `Camera
Devices` submenu.

The `Hide All Display Overlays` option hides all the display devices overlays in
the 3D view independently from the specific robot's device option set in
`Display Devices` submenu.

### Tools Menu

The `Tools` menu allows you to open various Webots windows.

The `3D View` menu item shows or hides the

The `Scene Tree` menu item opens the

The `Scene Tree` menu item opens the `Scene Tree` window in which you can edit
the virtual world. Alternatively it is also possible to double-click on some of
the objects in the main window: this automatically opens the Scene Tree with the
corresponding object selected.

The `Text Editor` menu item opens the Webots text editor. This editor can be
used for editing and compiling controller source code.

The `Console` menu item opens the Webots Console, which is a read-only console
that is used to display Webots error messages and controller outputs.

The `Restore Layout` menu item restores the factory layout of the panes of the
main window.

The `Clear Console` menu item clears the console.

The `Edit Physics Plugin` menu item opens the source code of the physics plugin
in the text editor.

The `License Manager...` item opens the `Webots License Manager` window that
allows you to see which license modules are in use and optionally to transfer
some license modules to your local computer for off-line use. Please note that
the transfer of license modules may be limited by your local license
administrator: It may not be possible to transfer some modules to your local
computer or only for a limited duration depending on the configuration defined
by your local license administrator. Please ask your local license administrator
in case of problem.

The `Preferences` item pops up a window described in `this section`.

### Wizards Menu

The `Wizards` menu makes it easier to create new projects and new controllers.

The `New Project Directory...` menu item first prompts you to choose a
filesystem location and then it creates a project directory. A project directory
contains several subdirectories that are used to store the files related to a
particular Webots project, i.e. world files, controller files, data files,
plugins, etc. Webots remembers the current project directory and automatically
opens and saves any type of file from the corresponding subdirectory of the
current project directory.

The `New Robot Controller...` menu item allows you to create a new controller
program. You will first be prompted to choose between a C, C++, Java, Python or
`MATLAB` controller. Then, Webots will ask you to enter the name of your
controller and finally it will create all the necessary files (including a
template source code file) in your current project directory.

The `New Physics Plugin...` menu item will let you create a new physics plugin
for your project. Webots asks you to choose a programming language (C or C++)
and a name for the new physics plugin. Then it creates a directory, a template
source code file and a Makefile in your current project.

### Help menu

In the `Help` menu, the `About...` item opens the `About...` window that
displays the license information.

The `Webots Guided Tour...` menu item starts a guided tour that demonstrates
Webots capabilies through a series of examples.

The `OpenGL Information...` menu item gives you information about your current
OpenGL hardware and driver. It can be used to diagnose rendering problems.

The remaining menu items bring up various information as indicated, in the form
of HTML pages, PDF documents, etc.

### Main toolbar

The main toolbar contains items for editing the world and the speedometer (see
subsection ), other than shortcuts to items of the `File`, `Simulation` and
`View` menus. Edit actions always apply on the selected object, that is
highlighted both in the 3D window and in the Scene Tree.

`Hide/Show Scene Tree`: shows or hides the Scene Tree and resizes the 3D window
consequently.

`Cut`: Cuts the selected object.

`Copy`: Copies the selected object.

`Paste`: Pastes the copied or cut object.

Note that the first three nodes of the Scene Tree (`WorldInfo, Viewpoint,` and
`Background`) cannot be cut, copied or pasted. One single instance of each of
these nodes must be present in every Webots world, and in that precise order.

`Add`: Adds a node or an object. For nodes, this triggers a dialog that will let
you choose a node type from a list. The new node is created with default values
that can be modified afterwards. You can only insert a node suitable for the
corresponding field. The dialog also gives the possibility to load a previously
exported node by clicking on the `Import...` button. Further information about
how to export a node are available `here`.

`Delete`: Deletes the selected object.

### Speedometer and Virtual Time

A speedometer (see ) indicates the speed of the simulation on your computer. It
is displayed on the main toolbar, and indicates how fast the simulation runs
compared to real time. In other words, it represents the speed of the virtual
time. If the value of the speedometer is 2, it means that your computer
simulation is running twice as fast as the corresponding real robots would. This
information is valid both in `Run` mode and `Fast` mode.

![Speedometer](png/speedometer.png)
**Speedometer**

To the left of the speedometer, the *virtual time* is displayed using following
format:

*H:MM:SS:MMM*

where *H* is the number of hours (may be several digits), *MM* is the number of
minutes, *SS* is the number of seconds, and *MMM* is the number of milliseconds
(see ). If the speedometer value is greater than one, the virtual time is
progressing faster than real time.

The basic time step for simulation can be set in the `basicTimeStep` field of
the `WorldInfo` node in the scene tree window. It is expressed in virtual time
milliseconds. The value of this time step defines the length of the time step
executed during the `Step` mode. This step is multiplied by the `displayRefresh`
field of the same `WorldInfo` node to define how frequently the display is
refreshed.

## The 3D Window

### Selecting an object

A single mouse click allows to select a solid object. The bounding object of a
selected solid is represented by white lines. These lines turn rose if the solid
is colliding with another one and blue when the solid is idle, i.e., it comes to
rest and it doesn't interact with any other active solid. Selecting a robot
enables the `Show Robot Window` item in the `Tools` menu. Double-clicking on a
solid object opens the Robot Window and if it was closed, the Scene Tree.

If an object has a solid subpart, then it is also possible to select only this
subpart by clicking on it once the whole object is already selected, or by
clicking on it while holding down the Alt key. Linux users should also hold down
the Control key (Ctrl) together with the Alt key.

### Navigation in the scene

Dragging the mouse while pressing a mouse button moves the camera of the 3D
window.

### Moving a solid object

Currently Webots provides two different ways to move solid objects: axis-aligned
handles and keyboard shortcuts.

#### Axis-aligned handles

When a solid object is selected, some arrow-shaped handles appear in the 3D
window (see ). These handles can be used to translate and rotate the object
along the corresponding axis. For moving the object you can simply click on the
handle and drag it to the desired position. A label will show the currect
relative translation or rotation during the movement, as shown in .

If the Control key (Ctrl), the handles for resizing the solid object will be
displayed instead of translation and rotation handles. These resize handles can
also be enabled from the Field Editor.

![Axis-aligned handles to move solid objects](png/manipulators.png)
**Axis-aligned handles to move solid objects**

![Labels displaying relative translation and rotation when moving objects with handles](png/manipulators_label.png)
**Labels displaying relative translation and rotation when moving objects with handles**

#### Translation using keyboard shurtcuts

### Applying a force to a solid object with physics

To apply a force to an object, place the mouse pointer where the force will
apply, hold down the Alt key and left mouse button together while dragging the
mouse. Linux users should also hold down the Control key (Ctrl) together with
the Alt key. This way your are drawing a 3D-vector whose end is located in the
plane parallel to the view which passes through the point of application. The
intensity of the applied force is directly proportional to the cube of the
length of this vector.

### Applying a torque to a solid object with physics

To apply a torque to an object, place the mouse pointer on it, hold down the Alt
key and right mouse button together while dragging the mouse. Linux users should
also hold down the Control key (Ctrl) together with the Alt key. Also, Mac OS X
users with a one-button mouse should hold down the Control key (Ctrl) to emulate
the right mouse button. This way your are drawing a 3D-vector with origin the
center of mass and whose end is located in the plane parallel to the view which
passes through this center. The object is prompted to turn around the vector
direction, the intensity of the applied torque being directly proportional to
the product of the mass by the length of the 3D-vector.

### Moving and resizing Overlays

By default for each Camera and Display device, an overlay showing the recorded
or displayed image is visible in the 3D view. The device type is indicated by
the border color: magenta for Camera devices and cyan for Display devices, see .
This overlay can be moved to the desired position on the view by clicking on it
and dragging the mouse. In order to resize the overlay the user has to click on
the icon located at the bottom right corner and drag the mouse, during this
action the original not scaled image size will be indicated using darker areas,
as depicted in Additionally a close button is available on the top right corner
to hide the overlay. Once the robot is selected, it is also possible to show or
hide the overlay images from the `Camera Devices` and `Display Devices` items in
`Robot` menu.

![Camera and Display overlays](png/overlay.png)
**Camera and Display overlays**

![Camera overlay resizing](png/overlay_resize.png)
**Camera overlay resizing**

### Show Camera and Display images in separate window

Overlay images can also be displayed outside the 3D window, see . When double-
clicking with the left mouse button on the overlay, a new external window
displaying the device image is created and the overlay in the 3D window is
disabled. It is possible to restore the 3D window overlay simply by closing the
window.

![Camera and Display image window](png/rendering_device_window.png)
**Camera and Display image window**

## The Scene Tree

As seen in the previous section, to access to the Scene Tree Window you can
either choose `Scene Tree` in the `Tools` menu, or press the `Show Scene Tree`
button in the main toolbar. The scene tree contains the information that
describes a simulated world, including robots and environment, and its graphical
representation. The scene tree of Webots is structured like a VRML97 file. It is
composed of a list of nodes, each containing fields. Fields can contain values
(text strings, numerical values) or other nodes.

This section describes the user interface of the Scene Tree, gives an overview
of the VRML97 nodes and Webots nodes.

![Scene Tree Window](png/scene_tree1.png)
**Scene Tree Window**

### Field Editor

Nodes can be expanded with a double-click. When a field is selected, its value
can be edited at the bottom of the Scene Tree. All changes will be immediately
reflected in the 3D window. The following buttons are available int the field
editor section:

`Reset`: Resets a field to its default value.

`Help`: Context sensitive help for the currently selected node.

Additionally, when a node is selected, other actions are available as shown in :

![Webots node editor](png/field_editor.png)
**Webots node editor**

`Tranform to`: Allow to change the type of the selected node by chosing the
target type from a given list of suitable types. This action is not available
for all node's types.

`Export...`: Exports nodes that can then be imported in other worlds.

`Source`: Displayed only when a PROTO node is selected, opens the corresponding
PROTO definition file in the text editor.

`Result`: Displayed only when a procedural PROTO node is selected, opens the
PROTO definition file generated by the template engine in the text editor.

`Show resize handles`: Displays the handles for resizing and scaling the
selected node from the 3D Window. This option is disabled for PROTO nodes and
only displayed for Geometry nodes and nodes derived from Transform.

## Preferences

The Webots preferences can be modified by a dialog box which can be open from
the `Webots > Preferences` menu item on Mac, and from the `Tools > Preferences`
menu item on the other operating systems.

The dialog box is separated into tabs. Each of the following subsection
corresponds to one of this tab.

### General

The `General` tab contains misc preferences about the application.

### OpenGL

The `OpenGL` tab contains preferences about setting the 3D rendering abilities.
The initial parameters of these settings may vary from one computer to another
depending on the GPU OpenGL abilities.

## Citing Webots

If you write a scientific paper or describe your project involving Webots on a
web page, we will greatly appreciate if you can add a reference to Webots. For
example by explicitly mentioning Cyberbotics' web site or by referencing a
journal paper that describes Webots. To make this simpler, we provide here some
citation examples, including BibTex entries that you can use in your own
documents.

### Citing Cyberbotics' web site

*This project uses * `Webots`*, a commercial mobile robot simulation software
developed by Cyberbotics Ltd.*

*This project uses Webots (http://www.cyberbotics.com), a commercial mobile
robot simulation software developed by Cyberbotics Ltd.*

The BibTex reference entry may look odd, as it is very different from a standard
paper citation and we want the specified fields to appear in the normal plain
citation mode of LaTeX.


```
@MISC{Webots,
  AUTHOR = {Webots},
  TITLE  = {http://www.cyberbotics.com},
  NOTE   = {Commercial Mobile Robot Simulation Software},
  EDITOR = {Cyberbotics Ltd.},
  URL    = {http://www.cyberbotics.com}
}
```

Once compiled with LaTeX, it should display as follows:

*References*

* [1] Webots. http://www.cyberbotics.com. Commercial Mobile Robot Simulation
Software.*

### Citing a reference journal paper about Webots

A reference paper was published in the International Journal of Advanced
Robotics Systems. Here is the BibTex entry:


```

  @ARTICLE{Webots04,
  AUTHOR  = {Michel, O.},
  TITLE   = {Webots: Professional Mobile Robot Simulation},
  JOURNAL = {Journal of Advanced Robotics Systems},
  YEAR    = {2004},
  VOLUME  = {1},
  NUMBER  = {1},
  PAGES   = {39--42},
  URL     = {http://www.ars-journal.com/International-Journal-of-
             Advanced-Robotic-Systems/Volume-1/39-42.pdf}
}
 
```

