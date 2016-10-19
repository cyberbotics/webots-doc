## BVH Utility Functions

**Name**

**wbu\_bvh\_read\_file**, **wbu\_bvh\_cleanup** - *obtaining and releasing a BVH file handle.*

{[C++](cpp-api.md#cpp_bvh)}, {[Java](java-api.md#java_bvh)}, {[Python](python-api.md#python_bvh)}, {[Matlab](matlab-api.md#matlab_bvh)}, {[ROS](ros-api.md)}

``` c
#include <webots/utils/bvh_reader.h>

WbBvhDataRef wbu_bvh_read_file(const char *filename);
void wbu_bvh_cleanup(WbBvhDataRef motion);
```

**Description**

The function `wbu_bvh_read_file` parses the hierarchical skeleton data and motion data in the specified BVH file.
The `filename` can be specified either with an absolute path or a path relative to the controller directory.
The function returns a `WbBvhDataRef` object, which is a reference to the data read from the BVH file.
This object is null if there is an error in reading the BVH file, for example when the file is corrupt or the path is incorrect.

The `wbu_bvh_cleanup` function frees all the memory associated with the `WbBvhDataRef` object.
After this function is called the corresponding `WbBvhDataRef` object can no longer be used.

 > **note** [C++, Java, Python]:
 In object-oriented languages there is no `wbu_bvh_cleanup()` function because it is automatically called by the destructor.

---

**Name**

**wbu\_bvh\_get\_joint\_count**, **wbu\_bvh\_get\_joint\_name**, **wbu\_bvh\_get\_frame\_count**, **wbu\_bvh\_set\_scale** - *query number of joints, joint names, and number of frames in the BVH file, and set scale for translation data.*

{[C++](cpp-api.md#cpp_bvh)}, {[Java](java-api.md#java_bvh)}, {[Python](python-api.md#python_bvh)}, {[Matlab](matlab-api.md#matlab_bvh)}

``` c
#include <webots/utils/bvh_reader.h>

int wbu_bvh_get_joint_count(WbBvhDataRef ref);
const char* wbu_bvh_get_joint_name(WbBvhDataRef ref, int joint_index);
int wbu_bvh_get_frame_count(WbBvhDataRef ref);
void wbu_bvh_set_scale(WbBvhDataRef ref, double scale);
```

**Description**

The function `wbu_bvh_get_joint_count` returns the number of joints defined in the loaded BVH file.


The function `wbu_bvh_get_joint_name` returns the name of the joint indexed by the number `joint_index` in the loaded BVH file.

The function `wbu_bvh_get_frame_count` returns the number of frames of motion data in the loaded BVH file. Each frame corresponds to one entry of time-series data.


The function `wbu_bvh_set_scale()` sets the scale factor, which is used to scale the translation data form the BVH animation file. The scale factor is 1.0 by default. Note that this value does not affect the rotation data.

---

**Name**

**wbu\_bvh\_step**, **wbu\_bvh\_goto\_frame**, **wbu\_bvh\_reset** -
*read next frame, read a specific frame, or jump to first frame.*

{[C++](cpp-api.md#cpp_bvh)}, {[Java](java-api.md#java_bvh)}, {[Python](python-api.md#python_bvh)}, {[Matlab](matlab-api.md#matlab_bvh)}

``` c
#include <webots/utils/bvh_reader.h>

bool wbu_bvh_step(WbBvhDataRef ref);
bool wbu_bvh_goto_frame(WbBvhDataRef ref, int frame_number);
bool wbu_bvh_reset(WbBvhDataRef ref);
```

**Description**

The function `wbu_bvh_step` reads the joint angles and translation data in the next frame.
This function is typically called at the beginning of the main loop.
If the current frame is the last frame in the BVH file, calling this function reads the first frame again.
Returns true on success.

The function `wbu_bvh_goto_frame` reads a specific frame, whose index is the argument `frame_number`. Returns true on success.
Note that if the argument `frame_number` is greater than the number of frames in the file, it leads to an error, and the function returns false.


The function `wbu_bvh_reset` jumps to the first frame.
Returns true on success.

``` c
void main() {
  WbBvhDataRef ref = wbu_bvh_read_file(filename);
  do {
    wbu_bvh_step(ref);

    // Read the joint angles and do something
  } while (condition);
}

```

---

**Name**

**wbu\_bvh\_get\_joint\_rotation**, **wbu\_bvh\_get\_root\_translation** -
*get the joint rotation for a specific joint and the BVH object translation.*

{[C++](cpp-api.md#cpp_bvh)}, {[Java](java-api.md#java_bvh)}, {[Python](python-api.md#python_bvh)}, {[Matlab](matlab-api.md#matlab_bvh)}

``` c
#include <webots/utils/bvh_reader.h>

double *wbu_bvh_get_joint_rotation(WbBvhDataRef ref, int joint_index);
double *wbu_bvh_get_root_translation(WbBvhDataRef ref);
```

**Description**

The function `wbu_bvh_get_joint_rotation` returns the rotation of the joint specified by `joint_index`.
The rotation is returned as an array of double.
The function `wbu_bvh_get_root_translation` returns the translation of the BVH object.
The translation is returned as an array of double.
This is typically used to set the translation of the [Skin](#skin) node that is being animated by this BVH file.
The values can wither be used directly, or scaled using the `wbu_bvh_set_scale` function.

``` c   
void main() {
  WbBvhDataRef ref = wbu_bvh_read_file(filename);
  int i = 0;
  do {
    wbu_bvh_step(ref);
    for(i=0; i &lt joint_count; ++i){
      double *rotation = wbu_bvh_get_joint_rotation(ref, i);
      double axis_x = rotation[0];
      double axis_y = rotation[1];
      double axis_z = rotation[2];
      double angle  = rotation[3];
      // Do something with the joint angles
    }
    double *position = wbu_bvh_get_root_translation(ref);
    double x = position[0];
    double y = position[1];
    double z = position[2];
    // Do something with the translation
  } while (condition);
}
```

---

**Name**

**wbu\_bvh\_adapt\_skeleton** -
*adapt the skeleton specified in the BVH file to be able to re-target the BVH motion data for animating of a [Skin](#skin) node.*

{[C++](cpp-api.md#cpp_bvh)}, {[Java](java-api.md#java_bvh)}, {[Python](python-api.md#python_bvh)}, {[Matlab](matlab-api.md#matlab_bvh)}

``` c
#include <webots/utils/bvh_reader.h>

void wbu_bvh_adapt_skeleton(WbBvhDataRef ref, int num_joints, const char** joint_name_list);
```

**Description**

The `wbu_bvh_adapt_skeleton` adapts the skeleton defined in the BVH file to be able to re-target the BVH motion data to the [Skin](#skin) Node.
This is necessary because the skeleton of the [Skin](#skin) node will generally be different from the skeleton defined in the BVH file.
The difference can be in the joint hierarchy and in the number of joints.
Therefore, firstly, the extra joints in the BVH file must be removed.
Further, since the joint rotations are specified as relative to parent joints, they must be recomputed in case a joint is removed.
This computation is done by this function.

The arguments to this function are the number of bones and the list of bones names in the [Skin](#skin) node.
They can be obtained by calling the functions `wb_skin_get_bone_count` and `wb_skin_get_bone_name`.
Note that if the nomenclature of the joints in the [Skin](#skin) node is different from that of the BVH file, the names have to be manually translated.
Please refer to the advanced sample project in "WEBOTS\_HOME/projects/humans/skin_animation/" directory for an example of how this is done.
