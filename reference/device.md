## Device

Abstract node, derived from [Solid](reference/solid.md#solid).

```
Device {
}
```

### Description

This abstract node (not instanciable) represents a robot device (actuator and/or
sensor).

### Device Functions

#### Name

**wb\_device\_get\_model** - *returns the model string of the corresponding device*

{[C++](reference/cpp-api.md)}, {[Java](reference/java-api.md)}, {[Python](reference/python-api.md)}, {[Matlab](reference/matlab-api.md)}

``` c
#include <webots/device.h>

const char *wb_device_get_model(WbDeviceTag tag)
```

#### Description

`wb_device_get_model()` returns the model string of the device corresponding to
the WbDeviceTag given as parameter (`tag`).

This function returns NULL if the WbDeviceTag does not match a valid device, or
returns an empty string if the device is not a solid device (i.e. does not have
a `model` field)

---

#### Name

**wb\_device\_get\_name** - *convert WbDeviceTag to its corresponding device name*

{[C++](reference/cpp-api.md)}, {[Java](reference/java-api.md)}, {[Python](reference/python-api.md)}, {[Matlab](reference/matlab-api.md)}

``` c
#include <webots/device.h>

const char *wb_device_get_name(WbDeviceTag tag)
```

#### Description

`wb_device_get_name()` convert the WbDeviceTag given as parameter (`tag`) to its
corresponding name.

This function returns NULL if the WbDeviceTag does not match a valid device.

---

#### Name

**wb\_device\_get\_node\_type** - *convert WbDeviceTag to its corresponding WbNodeType*

{[C++](reference/cpp-api.md)}, {[Java](reference/java-api.md)}, {[Python](reference/python-api.md)}, {[Matlab](reference/matlab-api.md)}

``` c
#include <webots/device.h>

WbNodeType wb_device_get_node_type(WbDeviceTag tag)
```

#### Description

`wb_device_get_node_type()` convert the WbDeviceTag given as parameter (`tag`)
to its corresponding WbNodeType (cf. the
[Supervisor](reference/supervisor.md#supervisor) API)

This function returns NULL if the WbDeviceTag does not match a valid device.

