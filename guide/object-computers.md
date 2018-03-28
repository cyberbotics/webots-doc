# Computers

## ComputerMouse

A computer mouse.

Derived from [Solid](../reference/solid.md).

%figure

![ComputerMouse](images/objects/computers/ComputerMouse/model.png)

%end

```
ComputerMouse {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "computer mouse"
  SFColor    topColor    0.71 0.71 0.71
  SFColor    bottomColor 0.056 0.056 0.056
  SFFloat    mass        0.1
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/computers/protos/ComputerMouse.proto"

### ComputerMouse Field Summary

- `topColor`: Defines the color of the top part of the mouse.
- `bottomColor`: Defines the color of the bottom part of the mouse.
- `mass`: Defines the mass of the mouse in kg.
## DesktopComputer

A computer tower.

Derived from [Solid](../reference/solid.md).

%figure

![DesktopComputer](images/objects/computers/DesktopComputer/model.png)

%end

```
DesktopComputer {
  SFVec3f    translation      0 0 0
  SFRotation rotation         0 1 0 0
  SFString   name             "desktop computer"
  SFColor    powerbuttonColor 0.252903 0.263813 0.266361
  SFFloat    mass             0
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/computers/protos/DesktopComputer.proto"

### DesktopComputer Field Summary

- `powerbuttonColor`: Defines the color of the computer power button.
- `mass`: Defines the mass of the computer in kg. A value smaller or equal to 0 remove the physics of the computer.
## Keyboard

A computer keyboard.

Derived from [Solid](../reference/solid.md).

%figure

![Keyboard](images/objects/computers/Keyboard/model.png)

%end

```
Keyboard {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "keyboard"
  SFColor    color       0.1 0.1 0.1
  SFFloat    mass        0
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/computers/protos/Keyboard.proto"

### Keyboard Field Summary

- `color`: Defines the color of the keyboard.
- `mass`: Defines the mass of the keyboard in kg. A value smaller or equal to 0 remove the physics of the keyboard.
## Laptop

A simple laptop.

Derived from [Solid](../reference/solid.md).

%figure

![Laptop](images/objects/computers/Laptop/model.png)

%end

```
Laptop {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "laptop"
  SFString   controller  "laptop_switch_on"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/computers/protos/Laptop.proto"

### Laptop Field Summary

- `controller`: Defines the controller of the laptop which can use the Display device to show images.
## Monitor

A computer monitor.

Derived from [Solid](../reference/solid.md).

%figure

![Monitor](images/objects/computers/Monitor/model.png)

%end

```
Monitor {
  SFVec3f    translation 0 0 0
  SFRotation rotation    0 1 0 0
  SFString   name        "monitor"
  SFColor    color       0.15 0.15 0.15
  SFFloat    mass        0
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/computers/protos/Monitor.proto"

### Monitor Field Summary

- `color`: Defines the color of the monitor.
- `mass`: Defines the mass of the monitor in kg. A value smaller or equal to 0 remove the physics of the monitor.
