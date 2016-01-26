## General bugs

### Intel GMA graphics cards

Webots should run on any fairly recent computer equipped with a nVidia or ATI
graphics card and up-to-date graphics drivers. Webots is not guaranteed to work
with Intel GMA graphics cards: it may crash or exhibit display bugs. Upgrading
to the latest versions of the Intel graphics driver may help resolve such
problems (without any guarantee). Graphics drivers from Intel may be obtained
from the `Intel download center web site`. Linux graphics drivers from Intel may
be obtained from the `Intel Linux Graphics web site`.

### Virtualization

Because it highly relies on OpenGL, Webots may not work properly in virtualized
environments (such as VMWare or VirtualBox) which often lack a good OpenGL
support. Hence, Webots may exhibit some display bugs, run very slowly or crash
in such environments.

### Collision detection

Although collision detection works well generally well, `Cylinder-Cylinder`,
`Cylinder-Capsule`, `IndexedFaceSet-IndexedFaceSet` and `IndexedFaceSet-
Cylinder` collision detection may occasionaly yield wrong contact points.
Sometimes the contact points may be slightly off the shape, therefore causing
unrealistic reaction forces to be applied to the objects. Other times there are
too few contact points, therefore causing vibration or instabilities.

### Orientation dependent friction

Although the friction model of ODE is very accurate, the true friction cone is
approximated by a linearized version which can introduce some orientation
specific artifacts. It is for example possible that an object slips more easily
on another object in some direction than in some other, even if the friction
coefficients are set to be symmetric. However, in most of the cases it is
possible to get rid of these effects by tuning correctly the friction
parameters.

