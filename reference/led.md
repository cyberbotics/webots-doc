## LED

Derived from [Device](#device).

```
LED {
  MFColor   color   [ 1 0 0 ]  # [0,1]
  SFBool    gradual FALSE      # for gradual color display and RBG LEDs
}
```

### Description

The [LED](#led) node is used to model a light emitting diode (LED). The light
produced by an LED can be used for debugging or informational purposes. The
resulted color is applied only on the first child of the [LED](#led) node. If
the first child is a [Shape](#shape) node, the `emissiveColor` field of its
[Material](#material) node is altered. If the first child is a [Light](#light)
node, its `color` field is altered. Otherwise, if the first child is a
[Group](#group) node, a recursive search is applied on this node in order to
find which color field must be modified, so every [Light](#light),
[Shape](#shape) and [Group](#group) node is altered according to the previous
rules.

### Field Summary

- `color`: This defines the colors of the LED device. When off, an LED is always
black. However, when on it may have different colors as specified by the LED
programming interface. By default, the `color` defines only one color (red), but
you can change this and add extra colors that could be selected from the LED
programming interface. However, the number of colors defined depends on the
value of the `gradual` field (see below).
- `gradual`: This defines the type of LED. If set to FALSE, the LED can take any
of the color values defined in the `color` list. If set to TRUE, then the
`color` list should either be empty or contain only one color value. If the
`color` list is empty, then the LED is an RGB LED and can take any color in the
R8G8B8 color space (16 million possibilities). If the `color` list contains a
single color, then the LED is monochromatic, and its intensity can be adjusted
between 0 (off) and 255 (maximum intensity).

### LED Functions

**Name** <a name="wb_led_set"/>

**wb\_led\_set**, **wb\_led\_get** - *turn an LED on or off and read its status*

{[C++](#cpp_led)}, {[Java](#java_led)}, {[Python](#python_led)}, {[Matlab](#matlab_led)}

``` c
#include <webots/led.h>

void wb_led_set(WbDeviceTag tag, int value)
int wb_led_get(WbDeviceTag tag)
```

**Description**

`wb_led_set()` switches an LED on or off, possibly changing its color. If the
`value` parameter is 0, the LED is turned off. Otherwise, it is turned on.

In the case of a non-gradual LED (`gradual` field set to FALSE), if the `value`
parameter is 1, the LED is turned on using the first color specified in the
`color` field of the corresponding [LED](#led) node. If the `value` parameter is
2, the LED is turned on using the second color specified in the `color` field of
the [LED](#led) node, and so on. The `value` parameter should not be greater
than the size of the `color` field of the corresponding [LED](#led) node.

In the case of a monochromatic LED (`gradual` field set to TRUE and `color`
field containing exactly one color), the `value` parameter indicates the
intensity of the LED in the range 0 (off) to 255 (maximum intensity).

In the case of an RGB LED (`gradual` field set to TRUE and `color` field
containing an empty list), the `value` parameter indicates the RGB color of the
LED in the range 0 (off or black) to 0xffffff (white). The format is R8G8B8: The
most significant 8 bits (left hand side) indicate the red level (between 0x00
and 0xff). Bits 8 to 15 indicate the green level and the least significant 8
bits (right hand side) indicate the blue level. For example, 0xff0000 is red,
0x00ff00 is green, 0x0000ff is blue, 0xffff00 is yellow, etc.

The `wb_led_get` function returns the value given as an argument of the last
`wb_led_set` function call.

