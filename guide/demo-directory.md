## Demo Directory

This section provides a list of interesting worlds that broadly illustrate Webots capabilities.
Several of these examples have stemmed from research or teaching projects.
You will find the corresponding ".wbt" files in the "WEBOTS\_HOME/projects/samples/demos/worlds" directory, and their controller source code in the "WEBOTS\_HOME/projects/samples/demos/controllers" directory.
For each demo, the world file and its corresponding controller have the same name.

### anaglyph.wbt

**Keywords**: Stereoscopic camera, anachrome red/cyan filters

![anaglyph.png](images/samples/anaglyph.png) This example demonstrates the merge of two `Camera` images into one, in order to create an [anaglyph image](https://en.wikipedia.org/wiki/Anaglyph_3D).
A stereoscopic camera is mounted on a `iRobot Create` robot.
At each step, both `Camera` images are merged into a `Display` device, one is filtered in red, and the other one is filtered in cyan.
This produces an anaglyph 3D image that can be seen with low cost red/cyan 3D glassed.

### blimp\_lis.wbt

**Keywords**: Flying robot, physics plugin, keyboard, joystick

![blimp_lis.png](images/samples/blimp_lis.png) This is an example of the flying blimp robot developed at the Laboratory of Intelligent Systems (LIS) at EPFL.
You can use your keyboard, or a joystick to control the blimp's motion across the room.
Use the up, down, right, left, page up, page down and space (reset) keys.
Various `Transform` and `IndexedFaceSet` nodes are used to model the room using textures and transparency.
A *physics plugin* is used to add thrust and other forces to the simulation.

> **Note**:
`Fluid` and `Propeller` nodes are now recommended to create flying robots.

### gantry.wbt

**Keywords**: Gantry robot, gripper, Hanoi towers, linear motors, recursive algorithm

![gantry.png](images/samples/gantry.png) In this example, a gantry robot plays "Towers of Hanoi" by stacking three colored boxes.
The gantry robot is modeled using a combination of `LinearMotor` and `RotationalMotor` devices.
A recursive algorithm is used to solve the Hanoi Towers problem.

### ghostdog.wbt

**Keywords**: Quadruped, legged robot, dog robot, passive joint, spring and damper

![ghostdog.png](images/samples/ghostdog.png) This example shows a galloping quadruped robot made of active hip joints and passive knee joints (using springs and dampers).
The keyboard can be used to control the robot's direction and to change the amplitude of the galloping motion.
Each knee is made of two embedded HingeJoint nodes, one active and one passive, sharing the same rotation axis.
The passive HingeJoint simulates the spring and damping.
The active HingeJoint is not actuated in this demo but it could be used for controlling the knee joints.

### hexapod.wbt

**Keywords**: Legged robot, alternating tripod gait, linear motor

![hexapod.png](images/samples/hexapod.png) In this example, an insect-shaped robot is made of a combination of `LinearMotor` and `RotationalMotor` devices.
The robot moves using an alternating tripod gait.

### humanoid.wbt

**Keywords**: Humanoid, QRIO robot

![humanoid.png](images/samples/humanoid.png) In this example, a humanoid robot performs endless gymnastic movements.

### moon.wbt

**Keywords**: differential wheels, Koala, keyboard, texture

![moon.png](images/samples/moon.png) In this example, two Koala robots (K-Team) circle on a moon-like surface.
You can modify their trajectories with the arrow keys on your keyboard.
The moon-like scenery is made of `IndexedFaceSet` nodes.
Both robots use the same controller code.

### salamander.wbt

**Keywords**: Salamander robot, swimming robot, amphibious robot, legged robot, physics plugin, buoyancy

![salamander.png](images/samples/salamander.png) A salamander-shaped robot walks down a slope and reaches a pool where it starts to swim.
The controller uses two different types of locomotion: it walks on the ground and swims in the water.
This demo simulates propulsive forces caused by the undulations of the body and the resistance caused by the robot's shape.
In addition, the buoyancy of the robot's body is also simulated using Archimedes' principle.

### soccer.wbt

**Keywords**: Soccer, Supervisor, differential wheels, label

![soccer.png](images/samples/soccer.png) In this example, two teams of simple robots play soccer.
A `Supervisor` is used as the referee; it counts the goals and displays the current score and the remaining time in the 3D view.
This example shows how a `Supervisor` can be used to read and change the position of objects.

### sojourner.wbt

**Keywords**: Sojourner, Passive joint, planetary exploration robot, keyboard, IndexedFaceSet

![sojourner.png](images/samples/sojourner.png) This is a realistic model of the "Sojourner" Mars exploration robot (NASA).
A large obstacle is placed in front of the robot so that it is possible to observe how the robot manages to climb over it.
The keyboard can be used to control the robot's motion.

### stewart\_platform.wbt

**Keywords**: Stewart platform, linear motion, physics plugin, ball joint, universal joint

![stewart_platform.png](images/samples/stewart_platform.png) This is an example of a *Stewart platform*.
A Stewart platform is a kind of parallel manipulator that uses an octahedral assembly of linear actuators.
It has six degrees of freedom (*x*, *y*, *z*, pitch, roll, and yaw).
In this example, the Stewart platform is loaded with a few stacked boxes, then the platform moves and the boxes stumble apart.
This simulation attaches both ends of the linear actuators (hydraulic pistons) to the lower and the upper parts of the Stewart platform.

### uneven\_terrain.wbt

**Keywords**: ElevationGrid, uneven terrain

![uneven_terrain.png](images/samples/uneven_terrain.png) This example demonstrates the creation of an uneven terrain based on the `ElevationGrid` primitive.
In this world, a six-wheeled robots with rotational suspensions is moving along a predefined path (composed of a list of `GPS` coordinates).
To do so, it uses its `GPS` and `Compass` sensors.

### yamor.wbt

**Keywords**: Connector, modular robots, self-reconfiguring robot

![yamor.png](images/samples/yamor.png) In this example, eight "Yamor" robot modules attach and detach to and from each other using `Connector` devices.
Connector devices are used to simulate the mechanical connections of docking systems.
In this example, the robot modules go through a sequence of loops and worm-like configurations while changing their mode of locomotion.
All modules use the same controller code, but their actual module behavior is chosen according to the name of the module.
