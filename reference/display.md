## Display

Derived from `Device`.


```
Display {
  SFInt32    width          64
  SFInt32    height         64
}
```

### Description

The `Display` node allows to handle a 2D pixel array using simple API functions,
and render it into a 2D overlay on the 3D view, into a 2D texture of any `Shape`
node, or both. It can model an embedded screen or it can display any graphical
information such as graphs, text, robot trajectory, filtered camera images and
so on.

If the first child of the `Display` node is or contains (recursive search if the
first node is a `Group`) a `Shape` node having a `ImageTexture`, then the
internal texture of the(se) `ImageTexture` node(s) is replaced by the texture of
the `Display`.

### Field Summary

- `width`: width of the display in pixels
- `height`: height of the display in pixels

### Coordinates system

Internally, the `Display` image is stored in a 2D pixel array. The RGBA value
(4x8 bits) of a pixel is dislayed in the status bar (the bar at the bottom of
the console window) when the mouse hovers over the pixel in the `Display`. The
2D array has a fixed size defined by the `width` and `height` fields. The (0,0)
coordinate corresponds to the top left pixel, while the (`width`-1,`height`-1)
coordinate corresponds to the bottom right pixel.

### Command stack

Each function call of the `Display` device API (except for
`wb_display_get_width()` and `wb_display_get_height()`) is storing a specific
command into an internal stack. This command stack is sent to Webots during the
next call of the `wb_robot_step()` function, using a FIFO scheme (First In,
First Out), so that commands are executed in the same order as the corresponding
function calls.

### Context

The `Display` device has among other things two kinds of functions; the
contextual ones which allow to set the current state of the display, and the
drawing ones which allow to draw specific primitives. The behavior of the
drawing functions depends on the display context. For example, in order to draw
two red lines, the `wb_display_set_color` contextual function must be called for
setting the display's internal color to red before calling twice the
`wb_display_draw_line` drawing function to draw the two lines.

### Overlay Image

<center>
![Display overlay image](png/display_overlay.png)

####Display overlay image
</center>

The display image is shown by default on top of the 3D window with a cyan
border, see . The user can move this display image at the desired position using
the mouse drag and drop and resize it by clicking on the icon at the bottom
right corner. Additionally a close button is available on the top right corner
to hide the image. Once the robot is selected, it is also possible to show or
hide the overlay image from the `Display Devices` item in `Robot` menu.

It is also possible to show the display image in an external window by double-
clicking on it. After doing it, the overlay disappears and the new window pops
up. Then, after closing the window, the overlay will be automatically restored.

### Display Functions

