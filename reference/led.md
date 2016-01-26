## LED

Derived from `Device`.


```
LED {
  MFColor   color   [ 1 0 0 ]  # [0,1]
  SFBool    gradual FALSE      # for gradual color display and RBG LEDs
}
```

### Description

The `LED` node is used to model a light emitting diode (LED). The light produced
by an LED can be used for debugging or informational purposes. The resulted
color is applied only on the first child of the `LED` node. If the first child
is a `Shape` node, the `emissiveColor` field of its `Material` node is altered.
If the first child is a `Light` node, its `color` field is altered. Otherwise,
if the first child is a `Group` node, a recursive search is applied on this node
in order to find which color field must be modified, so every `Light`, `Shape`
and `Group` node is altered according to the previous rules.

### Field Summary

### LED Functions

