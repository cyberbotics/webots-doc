## BallJointParameters


```
BallJointParameters {
  field SFVec3f anchor 0 0 0      # point at which the bodies are connected (m)
  field SFFloat springConstant  0 # uniform rotational spring constant (Nm)
  field SFFloat dampingConstant 0 # uniform rotational damping constant (Nms)
}
```

### Description

The `BallJointJointParameters` node can be used to specify the parameters of a
ball joint. It contains the anchor position, i.e. the coordinates of the point
where bodies under a ball joint constraints are kept attached. It can be used in
the jointParameters field of `BallJoint` only.

### Field Summary

- `anchor`: This field specifies the anchor position expressed in relative
coordinates with respect to the center of the closest upper `Solid`'s frame.
- `springConstant` and `dampingConstant`: These fields specify the uniform amount
of rotational spring and damping effect around each of the the frame axis of the
`BallJoint`'s closest upper `Solid` (see `Joint`'s `"Springs and Dampers"`
section for more information on these constants). This is can be useful to
simulate a retraction force that pulls the `BallJoint` solid `endPoint` back
towards its initial orientation.

