## Motion

**Name**

**wbu\_motion\_new**, **wbu\_motion\_delete** - *obtaining and releasing a motion file handle*

{[C++](cpp-api.md#cpp_motion)}, {[Java](java-api.md#java_motion)}, {[Python](python-api.md#python_motion)}, {[Matlab](matlab-api.md#matlab_motion)}

``` c
#include <webots/utils/motion.h>

WbMotionRef wbu_motion_new(const char *filename)
void wbu_motion_delete(WbMotionRef motion)
```

**Description**

The `wbu_motion_new()` function allows to read a motion file specified by the
`filename` parameter. The `filename` can be specified either with an absolute
path or a path relative to the controller directory. If the file can be read, if
its syntax is correct and if it contains at least one pose and one joint
position, then `wbu_motion_new()` returns a `WbMotionRef` that can be used as
parameter in further `wbu_motion_*()` calls. If an error occurred, an error
message is printed to Webots' console, and `NULL` is returned. Motions are
created in *stopped mode*, `wbu_motion_play()` must be called to start the
playback.

The `wbu_motion_delete()` function frees all the memory associated with the
`WbMotionRef`. This `WbMotionRef` can no longer be used afterwards.

> **note** [C++, Java, Python]:
The constructor and destructor of the Motion class are used instead of
`wbu_motion_new()` and `wbu_motion_delete()`. In these languages, an error
condition can be detected by calling the `isValid()` function after the
constructor. If `isValid()` yields `false` then the `Motion` object should be
explicitly deleted. See example below.

```c++
Motion *walk = new Motion(filename);
if (! walk->isValid()) {
  cerr << "could not load file: " << filename << endl;
  delete walk;
}
```

**See also**

[wbu\_motion\_play](#wbu_motion_play)

---

**Name**

**wbu\_motion\_play**, **wbu\_motion\_stop**, **wbu\_motion\_set\_loop**, **wbu\_motion\_set\_reverse** - *Controlling motion files playback*

{[C++](cpp-api.md#cpp_motion)}, {[Java](java-api.md#java_motion)}, {[Python](python-api.md#python_motion)}, {[Matlab](matlab-api.md#matlab_motion)}

``` c
#include <webots/utils/motion.h>

void wbu_motion_play(WbMotionRef motion)
void wbu_motion_stop(WbMotionRefmotion)
void wbu_motion_set_loop(WbMotionRef motion, bool loop)
void wbu_motion_set_reverse(WbMotionRefmotion, bool reverse)
```

**Description**

The `wbu_motion_play()` starts the playback of the specified motion. This
function registers the motion to the playback system, but the effective playback
happens in the background and is activated as a side effect of calling the
`wb_robot_step()` function. If you want to play a file and wait for its
termination you can do it with this simple function:

```c
void my_motion_play_sync(WbMotionRef motion)
{
  wbu_motion_play(motion);
  do {
    wb_robot_step(TIME_STEP);
  }
  while (! wbu_motion_is_over(motion));
}
```

Several motion files can be played simultaneously by the same robot, however if
two motion files have common joints, the behavior is undefined.

Note that the steps of the `wb_robot_step()` function and the pose intervals in
the motion file can differ. In this case Webot computes intermediate joint
positions by linear interpolation.

The `wbu_motion_stop()` interrupts the playback of the specified motion but
preserves the current position. After interruption the playback can be resumed
with `wbu_motion_play()`.

The `wbu_motion_set_loop()` sets the *loop mode* of the specified motion. If the
*loop mode* is `true`, the motion repeats when it reaches either the end or the
beginning (*reverse mode*) of the file. The *loop mode* can be used, for
example, to let a robot repeat a series of steps in a walking sequence. Note
that the loop mode can be changed while the motion is playing.

The `wbu_motion_set_reverse()` sets the *reverse mode* of the specified motion.
If the *reverse mode* is `true`, the motion file plays backwards. For example,
by using the *reverse mode*, it may be possible to turn a forwards walking
motion into a backwards walking motion. The *reverse mode* can be changed while
the motion is playing, in this case, the motion will go back from its current
position.

By default, the *loop mode* and *reverse mode* of motions are `false`.

**See also**

[wbu\_motion\_new](#wbu_motion_new)

---

**Name**

**wbu\_motion\_is\_over**, **wbu\_motion\_get\_duration**, **wbu\_motion\_get\_time**, **wbu\_motion\_set\_time** - *controlling the playback position*

{[C++](cpp-api.md#cpp_motion)}, {[Java](java-api.md#java_motion)}, {[Python](python-api.md#python_motion)}, {[Matlab](matlab-api.md#matlab_motion)}

``` c
#include <webots/utils/motion.h>

bool wbu_motion_is_over(WbMotionRef motion)
int wbu_motion_get_duration(WbMotionRefmotion)
int wbu_motion_get_time(WbMotionRef motion, bool loop)
void wbu_motion_set_time(WbMotionRefmotion, int ms)
```

**Description**

The `wbu_motion_is_over()` function returns `true` when the playback position
has reached the end of the motion file. That is when the last pose has been sent
to the [Motor](motor.md) nodes using the `wb_motor_set_position()` function. But
this does not mean that the motors have yet reached the specified positions;
they may be slow or blocked by obstacles, robots, walls, the floor, etc. If the
motion is in *loop mode*, this function returns always `false`. Note that
`wbu_motion_is_over()` depends on the *reverse mode*. `wbu_motion_is_over()`
returns `true` when *reverse mode* is `true` and the playback position is at the
beginning of the file or when *reverse mode* is `false` and the playback
position is at the end of the file.

The `wbu_motion_get_duration()` function returns the total duration of the
motion file in milliseconds.

The `wbu_motion_get_time()` function returns the current playback position in
milliseconds.

The `wbu_motion_set_time()` function allows to change the playback position.
This enables, for example, to skip forward or backward. Note that, the position
can be changed whether the motion is playing or stopped. The minimum value is 0
(beginning of the motion), and the maximum value is the value returned by the
`wbu_motion_get_duration()` function (end of the motion).

**See also**

[wbu\_motion\_play](#wbu_motion_play)
