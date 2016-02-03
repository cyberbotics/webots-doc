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

- `color`: This defines the colors of the LED device. When off, an LED is always black. However, when on it may have different colors as specified by the LED programming interface. By default, the `color` defines only one color (red), but you can change this and add extra colors that could be selected from the LED programming interface. However, the number of colors defined depends on the value of the `gradual` field (see below).
- `gradual`: This defines the type of LED. If set to FALSE, the LED can take any of the color values defined in the `color` list. If set to TRUE, then the `color` list should either be empty or contain only one color value. If the `color` list is empty, then the LED is an RGB LED and can take any color in the R8G8B8 color space (16 million possibilities). If the `color` list contains a single color, then the LED is monochromatic, and its intensity can be adjusted between 0 (off) and 255 (maximum intensity).

### LED Functions

