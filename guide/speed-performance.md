## Speed/Performance

### Why is Webots slow on my computer?

You should verify your graphics driver installation.
Please find instructions in [this section](verifying-your-graphics-driver-installation.md).

If you are using a laptop computer, please check the power options and make sure you are using the high performance power plan.

On Ubuntu (or other Linux) we also recommend to disable all visual effects.
Depending on the graphics hardware, there may be a huge performance drop of the rendering system (up to 10x) when the visual effects are on.
You can easily disable the operating system's visual effects using some tools like *Compiz Config Settings Manager* or *Unity Tweak Tool*.

### How can I change the speed of the simulation?

There are several ways to increase the simulation speed:

1. Use the `Run` button (Webots PRO only).
This button runs the simulation as fast as possible using all the available CPU power.
Otherwise, using the `Real-Time` running mode, Webots may not be using all the available CPU power in order to obtain a simulation speed that is close to the speed of the real world's phenomena.
2. Use the `Fast` button (Webots PRO only).
This button runs the simulation as fast as possible using all the available CPU power.
In this mode the simulation speed is increased further by leaving out the graphics rendering, hence the 3d window is black.
3. Increase the value of `WorldInfo.basicTimeStep`.
This field sets the granularity of the physics simulation.
With a higher `WorldInfo.basicTimeStep`, the simulation becomes faster but less accurate.
With a lower `WorldInfo.basicTimeStep`, the simulation becomes slower but more accurate.
There is an additional restriction: `WorldInfo.basicTimeStep` must be chosen such as to be an integer divisor of the *control step* which is the value passed as parameter to the `wb_robot_step` (or equivalent) function.
4. Decrease the value of `WorldInfo.FPS`.
This field represents the maximum rate at which the 3D display of the main windows is refreshed.
With a lower value, the simulation becomes faster but more flickering.
With a higher value, the simulation becomes slower but less flickering.
5. Try changing the value of `WorldInfo.optimalThreadCount`.
This field specifies how many threads are used to simulate the physics of the world.
Depending on the world you can get a better performance by reducing or increasing this value.
In general it is better to have a low number of threads for simple worlds and a bigger number of threads for complex worlds that include several robots physically independent from each other.
6. Disable unnecessary shadows.
Webots uses a lot of CPU/GPU power to compute how and where the objects shadows are cast.
But shadows are irrelevant for most simulation unless they should explicitly be seen by Cameras.
Unnecessary shadows can be disabled by unchecking the `castShadows` field of light nodes: `PointLight, SpotLight`, or `DirectionalLight`.
7. Simplify your simulation by removing unnecessary objects.
In particular, try to minimize the number of `Physics` nodes.
Avoid using a `Solid` nodes when a `Transform` or a `Shape` would do the trick.
8. Simplify the `boundingObject`s to increase the speed of the collision detection.
Replace complex primitives, like `Cylinder, IndexedFaceSet` and `ElevationGrid` by simpler primitives, like `Sphere, Capsule, Box` and `Plane`.
Avoid using a composition of primitives (in a `Group` or a `Transform`) when a single primitive would do the trick.
