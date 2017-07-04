# Webots 8.6.0

Today we're happy to announce the release of Webots 8.6.0. This new release brings a ton of new features and improvements, coupled with the same dedicated patches addressing bugs and regressions. Listed below are some of the key features of this release (for a full list of changes please refer to the changelog (link will be added here)):

## Drive.

### OSM

With Webots 8.6.0 our automobile simulation tools are more advanced than ever. We've overhauled our OpenStreetMap importer to make modelling real-world road networks and districts in Webots as quick and easy as possible, in even more detail and more accurately than before. Here is a comparison between previously imported road structures and revamped import:

#### Before
![Master](https://cyberbotics.com/files/repository/files/8-6-0release/osm%20master.png)
#### After
![Master](https://cyberbotics.com/files/repository/files/8-6-0release/osm%20develop.png)

We have expanded our library of calibrated vehicles to include models from Lincoln and Range Rover, as well as improving and optimizing our existing car models. Traffic simulation workflow using our SUMO interface is now easier to use, thanks to our new SUMO exporter, letting you create a traffic network based on worlds brought in through the OSM importer.

### VR

Thanks to Valve introducing OpenVR, you can now experience Webots automobile simulations in VR, putting yourself in the driver's seat. 

#### (Image of David with HTC vive, racing wheel and stereo vision output on screen) (perhaps new camera?)

## New Nodes

### Smart Cameras

It is now possible to add object recognition directly to a Camera using the Recognition node:

![smart camera](https://cyberbotics.com/files/repository/files/8-6-0release/recognition.png)

The camera will return (in addition to the raw image) the list of recognized objects in the camera frame. Each object will be defined by its relative position, relative orientation, size, position and size on the image, color list and model name. It is also possible to configure the maximum detection range and maximum number of objects detected simultaneously.

### Muscles

You can now graphically represent the contraction and relaxation of an artificial muscle using the new Muscle node:

![Muscle](https://cyberbotics.com/files/repository/files/8-6-0release/muscle.gif)

These muscles are attached to an underlying LinearMotor or RotationalMotor node.
See the feature presentation [video](https://www.youtube.com/watch?v=pd0jD1TbJe4) for more details.

### Blinding Light

Attach lens flares to the Viewpoint or any robot camera to simulate glare from the sun:

![LensFlare](https://cyberbotics.com/files/repository/files/8-6-0release/lensflare.png)

## Interaction, Interaction, Interaction

This update also brings about numerous upgrades to user interaction. 

Now the Viewpoint movement speed and zoom is always relative to scene geometry. This means you can easily move around any world, big or small, with ease, from editing sensor positions on an E-puck to positioning buildings in a city simulation. 

We have also added a new feature that makes scene navigation even easier; with one click of button you can center the view on any object you have selected, near or far:  

![Move To Viewpoint](https://cyberbotics.com/files/repository/files/8-6-0release/viewpoint.gif)

Now, even if you wish to find a small object nearby, or locate a car that has driven several miles away, one click is all it takes.

You can now disable picking for objects in the scene for objects that are purely visual and are annoying to select by accident.

These are just some of the extra workflow improvements we are bringing with Webots 8.6.0.

## Better Visuals

We've put work into improving the visual quality of simulations with this update.

Jagged edges are a thing of the past as Multi-Sample Anti-Aliasing (MSAA) support is now enabled in Webots. MSAA smooths jagged edges of scene geometry for a nicer appearance:

![Jaggy](https://cyberbotics.com/files/repository/files/8-6-0release/msaa.png)

The default MSAA level is 2x, but via the preferences this can be increased to as much as 8x or disabled.

Textures can now be filtered using Anisotropic filtering techniques to avoid Moiré patterns and perspective Aliasing. Here is a checkerboard floor seen from far without and with Anisotropic Filtering enabled:

![grim](https://cyberbotics.com/files/repository/files/8-6-0release/moire-pattern.png)

## Extra Goodies

 - World loading time has been reduced by up to 50% on large worlds.

 - Users on Windows can now benefit from Microsoft text-to-speech technologies via the Speaker API.

 - The Supervisor API has been extended to perform various new actions, including restarting a robot's controller, getting mouse interactions, getting a node's DEF name, and interacting with the VR headset.

 - The Webots objects library has been further extended.

 - And many more improvements.
