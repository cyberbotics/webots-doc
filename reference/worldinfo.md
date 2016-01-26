## WorldInfo


```
WorldInfo {
  SFString   title                          ""
  MFString   info                           []
  SFVec3f    gravity                        0 -9.81 0
  SFFloat    CFM                            0.00001  # [0,inf)
  SFFloat    ERP                            0.2      # [0,1]
  SFString   physics                        ""
  SFFloat    basicTimeStep                  32       # in ms
  SFFloat    FPS                            60
  SFInt32    optimalThreadCount             1        # maximum number of threads assigned to physics computation
  SFFloat    physicsDisableTime             1        # time after which the objects are disabled if they are idle
  SFFloat    physicsDisableLinearThreshold  0.01     # threshold determining if an object is idle or not
  SFFloat    physicsDisableAngularThreshold 0.01     # threshold determining if an object is idle or not
  SFNode     defaultDamping                 NULL     # default damping parameters
  SFFloat    inkEvaporation                 0        # make ground textures evaporate
  SFVec3f    northDirection                 1 0 0    # for compass and InertialUnit
  SFFloat    lineScale                      0.1      # control the length of every arbitrary-sized lines
  MFNode     contactProperties              []       # see ContactProperties node
}
```

The `WorldInfo` node provides general information on the simulated world:

