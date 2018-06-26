## Skin

Derived from [Device](device.md).

```
Skin {
  SFVec3f      translation   0 0 0
  SFRotation   rotation      0 1 0 0
  SFVec3f      scale         1 1 1
  SFString     name          "skin"
  SFString     model         ""
  MFNode       appearance    []
  MFNode       bones         []
  SFBool       castShadows   TRUE
}
```

### Description

The [Skin](#skin) node can be used to simulate soft mesh animation for example of a human or an animal.
The skin mesh is imported from a mesh file specified by the `model` name (either Ogre or FBX format),
but in order to be animated it has to be attached to a skeleton so that the rotation of the skeleton joints results in appropriate deformation of the skin mesh.

This node provides two alternative ways to define a skeleton.
The first method consists in providing the skeleton in the mesh file (in the case of Ogre, it stands in a separate skeleton file that must have the same name as the Ogre mesh file).
The second method consists in listing the [Solid](#solid.md) nodes corresponding to the mesh bones using the `bones` field.
If in the first case the resulting object animation will be purely graphical, when linking the [Skin](#skin) to an existing Webots skeleton made of [Solid](#solid.md) and [Joint](#joint.md) nodes it is possible to animate an dynamic object.

The XML files containing the skin mesh and skeleton can be generated using a 3D modeling software and then exporting them to Ogre format.
For example, the [Blender2OGRE](https://bitbucket.org/iboshkov/blender2ogre) plugin can be used to export the mesh and skeleton from [Blender](https://www.blender.org/) 3D modeling tool.
Then the exported ".mesh.xml" and ".skeleton.xml" XML file have to be converted to the corresponding ".mesh" and ".skeleton" binary files using the converter "$(WEBOTS\_HOME)/bin/ogre/OgreXMLConverter" in order to use it in Webots.

Other tools can be used for generating the characters to animate, for example human characters in the provided samples are generated using [MakeHuman](http://www.makehuman.org/).

#### Physically driven skin animation

If you want that the skin is animated based on the movements of a dynamic object then you have to specify skeleton by listing the [Solid](#solid.md) nodes corresponding to the skeleton bones in the `bones` field.
Each listed [Solid](#solid.md) bone have to be a child node of a [Joint](#joint.md).
Moreover the mesh bone structure and the [Solid](#solid.md)/[Joint](#joint.md) have to match.
In particular, this means that the number of mesh bones have to match with the number of joints and
that the [Solid](#solid.md) node names must be the same as the bone names specified in the mesh file.

#### Pure graphical skin animation

For a purely graphical skin animation the `bones` field doesn't have to be specified.
In this case the skeleton needed to animate the skin is loaded either from the file named "<modelName>.skeleton", where <modelName> corresponds to the `model` field value, and located in the same folder as the mesh file, or from the mesh FBX file, depending on what is provided.

### Field Summary

- The `translation` field defines the translation from the parent coordinate system to the children's coordinate system.

- The `rotation` field defines an arbitrary rotation of the children's coordinate system with respect to the parent coordinate system.
Please refer to [Transform](#transform.md) `rotation` field description for more information.

- The `scale` field specifies a possibly non-uniform scale of the mesh. Only positive values are permitted; non-positive values scale are automatically reset to 1.

- `name`: name of the skin device and used by wb_robot_get_device().

- `model`: name of the model to be imported.
For example, when using Ogre format, if the model name is "test_model", it import the binary mesh files "test_model.mesh" and "test_model.skeleton" placed in the "skins/test_model/" subdirectory, inside the current project directory.
The materials used by the imported mesh have to be defined in the `appearance` field.

- `appearance`: list of [Appearance](#appearance.md) nodes defining the materials used by the mesh defined in the `model` field.
In order to be correctly used, the `name` field of the child [Appearance](#appearance.md) node has to match the material name used in the mesh definition.
If multiple [Appearance](#appearance.md) nodes have the same `name` field value, the first one is used.

- The `bones` fields contains a list of [SolidReference](#solidreference.md) nodes that provide the information to attach a Webots skeleton made of [Solid](#solid.md) and [Joint](#joint.md) nodes.
In order to setup correctly the skeleton, the solids have to have the same names as specified in the skeleton.

- The `castShadows` field allows the user to turn on (TRUE) or off (FALSE) shadows casted by this shape. Note that if the mesh triangle count is very big, the casted shadows will be automatically disabled.

### Skin Functions

**Name**

**wb\_skin\_get\_bone\_count**, **wb\_skin\_get\_bone\_name** - *get the number and the names of bones in the skeleton of loaded skin model.*

{[C++](cpp-api.md#cpp_skin)}, {[Java](java-api.md#java_skin)}, {[Python](python-api.md#python_skin)}, {[Matlab](matlab-api.md#matlab_skin)}, {[ROS](ros-api.md)}

``` c
#include <webots/skin.h>

int wb_skin_get_bone_count(WbDeviceTag tag);
const char *wb_skin_get_bone_name(WbDeviceTag tag, int index);
```

**Description**

The function `wb_skin_get_bone_count` returns the total number of bones in the skeleton loaded by the [Skin](#skin) node.
The function `wb_skin_get_bone_name` returns the name of the bone at the specified index.
The bones are indexed starting from 0.

This two functions are available both if using a Webots skeleton or if the the skeleton is loaded from an Ogre XML file.
But if a Webots skeleton is used, then the bone count will correspond to the valid nodes specified in the `bones` field and the bone names will correspond to the referenced [Solid](#solid.md) names.

---

**Name**

**wb\_skin\_get\_bone\_orientation**, **wb\_skin\_get\_bone\_position,
  wb\_skin\_set\_bone\_orientation**, **wb\_skin\_set\_bone\_position** - *get or set the bone orientation and position.*

{[C++](cpp-api.md#cpp_skin)}, {[Java](java-api.md#java_skin)}, {[Python](python-api.md#python_skin)}, {[Matlab](matlab-api.md#matlab_skin)}, {[ROS](ros-api.md)}

``` c
#include <webots/skin.h>

void wb_skin_get_bone_orientation(WbDeviceTag tag, int index, bool absolute);
void wb_skin_get_bone_position(WbDeviceTag tag, int index, bool absolute);
void wb_skin_set_bone_orientation(WbDeviceTag tag, int index, const double rotation[4], bool absolute);
void wb_skin_set_bone_position(WbDeviceTag tag, int index, const double position[3], bool absolute);
```

**Description**

These functions set or return the skin's internal skeleton bone position and orientation.
Each bone is identified using an index value between 0 and the bones count returned by `wb_skin_get_bone_count`.
If the `absolute` argument is FALSE the orientation and position values are relative to the parent bone coordinate system.
Otherwise, if `absolute` is TRUE the orientation and position values are relative to the [Skin](#skin.md) node's coordinate system.

`wb_skin_set_bone_orientation` function sets the rotation of the skeleton bone to the specified axis-angle rotation value.
The rotation is specified as a double array, similar to `wb_supervisor_field_set_sf_rotation` [Supervisor](#supervisor.md) node.

`wb_skin_get_bone_orientation` function returns the axis-angle rotation of the skeleton bone
using the same format as in `wb_skin_set_bone_orientation`.

`wb_skin_set_bone_position` function sets the position of the skeleton bone.

`wb_skin_get_bone_position` function returns the position of the skeleton bone

> **note**:
The setter functions `wb_skin_set_bone_orientation` and `wb_skin_set_bone_position` are only available
if the `bones` field is not specified, i.e. if the object is purely graphical and the skin is not already
animated using the [Joint](#joint.md) nodes rotation.
