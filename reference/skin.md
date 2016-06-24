## Skin

Derived from [Device](device.md).

```
Skin {
  SFVec3f      translation   0 0 0
  SFRotation   rotation      0 1 0 0
  SFString     name          "skin"
  SFString     model         ""
}
```

### Description

The [Skin](#skin) node can be used to model an animated character in the simulation world, for example, a human, or an animal.
There are two aspects of the node: a skin mesh and a skeleton.
The skin mesh is attached to the skeleton, and the rotation of the skeleton joints results in appropriate deformation of the skin mesh.
The [Skin](#skin) node imports skin mesh and its associated skeleton from XML files, placed inside a folder with the same name as the XML file names, within the "skins" subdirectory of the current project directory.
Such XML files of models of characters (skin mesh and skeleton) can be generated using a 3D modeling software like Blender (TM).
Makehuman (TM) is a tool for generating models of humans. The human characters in the provided samples are generated using Makehuman (TM).
The [Skin](#skin) can be animated by changing the rotation of its joints as a function of time.

### Field Summary

- The `translation` field defines the translation from the parent coordinate system to the children's coordinate system.

- The `rotation` field defines an arbitrary rotation of the children's coordinate system with respect to the parent coordinate system.
Please refer to [Tranfsorm](#transform) `rotation` field description for more information.

- `name`: name of the model to be imported.
For example, if the model name is "test_model", it imports the XML files "test_model.skeleton.xml", "test_model.mesh.xml" and "test_model.material" placed in the "skins/test_model/" subdirectory, inside the current project directory.

- `restPosePath`: path to a file containing the rest pose of the skin model.
Rest pose is the pose the object should have if all the rotations are set to zero.
In other words, this is the initial reference pose relative to which all rotations are specified.
This is needed when we want to re-target pose data from another source and animate the character.
For example, this source could be a motion file.
In that case, the rest pose of this character node and the rest pose defined in the motion file must be similar.
This field may be an absolute path, or a path relative to current project directory.
The rest pose is specified in a text file in the format shown below.
Thefirst number is the joint id, as specified in the .skeleton file.
The next four numbers represent a quaternion, with its elements in the order [w, x, y, z].
It is not necessary to specify rest pose for all joints.
No rest pose is set for those joints which are not present in the rest pose file.
```
2: 0.98477, 0.173642, 0.00151535, -0.00859396
3: 0.98477, 0.173642, -0.00151535, 0.00859396
5: 0.976296, 0.21644, 0, 0     
```

### Skin Functions

**Name**

**wb\_skin\_get\_joint\_count**, **wb\_skin\_get\_joint\_name** - *get the number and the names of joints in the skeleton of loaded skin model.*

{[C++](cpp-api.md#cpp_skin)}, {[Java](java-api.md#java_skin)}, {[Python](python-api.md#python_skin)}, {[Matlab](matlab-api.md#matlab_skin)}, {[ROS](ros-api.md)}

``` c
#include <webots/skin.h>

int wb_skin_get_joint_count(WbDeviceTag tag)
const char *wb_skin_get_joint_name(WbDeviceTag tag, int index)
```

**Description**

The function `wb_skin_get_joint_count` returns the total number of joints in the skeleton loaded by the [Skin](#skin) node.
The joints are indexed starting from 0.

---

**Name**

**wb\_skin\_set\_joint\_angle\_relative**, **wb\_skin\_set\_joint\_angle\_absolute** -
*set the joint angle, either relative to parent joint or in the absolute world coordinate frame.*

{[C++](cpp-api.md#cpp_skin)}, {[Java](java-api.md#java_skin)}, {[Python](python-api.md#python_skin)}, {[Matlab](matlab-api.md#matlab_skin)}, {[ROS](ros-api.md)}

``` c
#include <webots/skin.h>

void wb_character_set_joint_angle_relative(WbDeviceTag tag, const double rotation[4])
void wb_character_set_joint_angle_absolute(WbDeviceTag tag, const double rotation[4])
```

**Description**

These functions set the rotation of the joint to the specified axis-angle value.
The rotation is specified as a double array, similar to `wb_supervisor_field_set_sf_rotation` [Supervisor](#supervisor) node.

The function `wb_character_set_joint_angle_relative` sets the joint angle relative to the parent joint.
The function `wb_character_set_joint_angle_absolute` sets the joint angle with respect to the absolute world frame.

> **note**:
Please look at the example in "WEBOTS\_HOME/projects/humans/skin_animation/" directory for further information.
