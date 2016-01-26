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

