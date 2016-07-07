## Skin

Derived from [Device](device.md).

```
Skin {
  SFVec3f      translation   0 0 0
  SFRotation   rotation      0 1 0 0
  SFVec3f      scale         1 1 1
  SFString     name          "skin"
  SFString     model         ""
  SFString     restPosePath  ""
  MFNode       bones         []
  SFBool       castShadows   TRUE
}
```

### Description

The [Skin](#skin) node can be used to model an animated character in the simulation world, for example, a human, or an animal.
The skin mesh is imported from Ogre XML files specified by the `model` name.
But in order to be animated it has to be attached to a skeleton so that the rotation of the skeleton joints results in appropriate deformation of the skin mesh.
This nodes provides two alternative ways to define a skeleton.
The first method consists in providing an Ogre XML Skeleton file that will having the same file name as the Ogre XML Mesh file.
Otherwise it is possible to list [Solid](#solid) noded corresponding to the mesh bones using the `bones` field.
If in the first case the resulting object animation will be purely graphical, when linking the [Skin](#skin) to an existing Webots skeleton made of [Solid](#solid) and [Joint](#joint) nodes it is possible to animate an dynamic object.

The XML files containing the skin mesh and skeleton model files can be generated using a 3D modeling software like Blender (TM) and using the plugin to export to Ogre. 
Makehuman (TM) is a tool for generating models of humans. The human characters in the provided samples are generated using Makehuman (TM).

#### Physically driven skin animation

If you want that the skin is animated based on the movements of a dynamic object then you have to specify skeleton by listing the [Solid](#solid) nodes corresponding to the skeleton bones in the `bones` field.
Each [Solid](#solid) bone have to be a child node of a [Joint](#joint).
Moreover mesh bone structure and the [Solid](#solid)/[Joint](#joint) have to match.
In particular this means that the number of mesh bones have to match with the number of joints.


#### Pure graphical skin animation

For a purely graphical skin animation the `bones` field doesn't have to be specified.
In this case the skeleton needed to animate the skin is expected to be loaded from a file named "<modelName>.skeleton.xml", where <modelName> corresponds to the `model` field value, and located in the same folder as the mesh and material files.

### Field Summary

- The `translation` field defines the translation from the parent coordinate system to the children's coordinate system.

- The `rotation` field defines an arbitrary rotation of the children's coordinate system with respect to the parent coordinate system.
Please refer to [Tranfsorm](#transform) `rotation` field description for more information.

- The `scale` field specifies a possibly non-uniform scale of the mesh. Only positive values are permitted; non-positive values scale are automatically reset to 1.

- `name`: name of the skin device and used by wb_robot_get_device().

- `model`: name of the model to be imported.
For example, if the model name is "test_model", it import the XML file "test_model.mesh.xml" and "test_model.material" placed in the "skins/test_model/" subdirectory, inside the current project directory. If the `bones` field is not defined it will also import "test_model.skeleton.xml".

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

- The `bones` fields contains a list of [SolidReference](#solid_reference) nodes that provide the information to attach a Webots skeleton made of [Solid](#solid) and [Joint](#joint) nodes.
In order to setup correctly the skeleton, the solid have to be listed in the same order as specified in the mesh file.
This means that if in the mesh file the thigh bone is referenced using the index number 3, then the [SolidReference](#solid_reference) linking to the tigh [Solid](#solid) has to inserted in the `bones` field at index 3 as well.

- The `castShadows` field allows the user to turn on (TRUE) or off (FALSE) shadows casted by this shape. Note that if the mesh triangle count is very big, the casted shadows will be automatically disabled.

### Skin Functions

**Name**

**wb\_skin\_get\_joint\_count**, **wb\_skin\_get\_joint\_name** - *get the number and the names of joints in the skeleton of loaded skin model.*

{[C++](cpp-api.md#cpp_skin)}, {[Java](java-api.md#java_skin)}, {[Python](python-api.md#python_skin)}, {[Matlab](matlab-api.md#matlab_skin)}, {[ROS](ros-api.md)}

``` c
#include <webots/skin.h>

int wb_skin_get_joint_count(WbDeviceTag tag);
const char *wb_skin_get_joint_name(WbDeviceTag tag, int index);
```

**Description**

The function `wb_skin_get_joint_count` returns the total number of joints in the skeleton loaded by the [Skin](#skin) node.
The function `wb_skin_get_joint_name` returns the name of the joint at the specified index.
The joints are indexed starting from 0.

This two functions are available both if using a Webots skeleton or a skeleton specified in an Ogre XML file.
But if a Webots skeleton is used, then the joint count will correspond to the valid nodes specified in the `bones` field and the joint names will correspond to the referenced [Solid](#solid) names.

---

**Name**

**wb\_skin\_set\_joint\_angle** - *set the joint angle.*

{[C++](cpp-api.md#cpp_skin)}, {[Java](java-api.md#java_skin)}, {[Python](python-api.md#python_skin)}, {[Matlab](matlab-api.md#matlab_skin)}, {[ROS](ros-api.md)}

``` c
#include <webots/skin.h>

void wb_character_set_joint_angle(WbDeviceTag tag, int index, const double rotation[4], bool absolute)
```

**Description**

This function sets the rotation of the joint to the specified axis-angle value.
The rotation is specified as a double array, similar to `wb_supervisor_field_set_sf_rotation` [Supervisor](#supervisor) node.
If the `absolute` argument is false the joint angle is set relative to the parent joint, otherwise the joint angle is set with respect to the absolute world frame.
The joints are indexed starting from 0.

This function is only available if the `bones` field is not specified, i.e. if the object is purely graphical and the skin is not already animated using the [Joint](#joint) node rotation.

> **note**:
Please look at the example in "WEBOTS\_HOME/projects/humans/skin_animation/" directory for further information.
