## BioRob GhostDog

%figure "GhostDog model in Webots"

![model.png](images/robots/ghostdog/model.png)

%end

The "GhostDog" robot is a dog-like robot developed by the [EPFL BioRob laboratory](https://biorob.epfl.ch/).

It is a quadruped robot made of active hip joints and passive knee joints (using springs and dampers).
Each knee is made of two embedded HingeJoint nodes, one active and one passive, sharing the same rotation axis.
The passive HingeJoint simulates the spring and damping.
The active HingeJoint is not actuated in the followin demo but it could be used for controlling the knee joints.

### Samples

You will find the following sample in this folder: "WEBOTS\_HOME/projects/robots/epfl/biorob/worlds".

#### ghostdog.wbt

![ghostdog.png](images/robots/ghostdog/ghostdog.wbt.png) This example shows the GhostDog which gallops.
The keyboard can be used to control the robot's direction and to change the amplitude of the galloping motion.
