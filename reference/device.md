## Device

Abstract node, derived from [Solid](solid.md#solid).

```
Device {
}
```

### Description

This abstract node (not instanciable) represents a robot device (actuator and/or
sensor).

### Device Functions

<a name="wb_device_get_model">**Name**</a>

**wb\_device\_get\_model** - *returns the model string of the corresponding device*

{[C++](cpp-api.md#cpp_device)}, {[Java](java-api.md#java_device)}, {[Python](python-api.md#python_device)}, {[Matlab](matlab-api.md#matlab_device)}

``` c
#include <webots/device.h>

const char *wb_device_get_model(WbDeviceTag tag)
```

**Description**

`wb_device_get_model()` returns the model string of the device corresponding to
the WbDeviceTag given as parameter (`tag`).

This function returns NULL if the WbDeviceTag does not match a valid device, or
returns an empty string if the device is not a solid device (i.e. does not have
a `model` field)

---

<a name="wb_device_get_name">**Name**</a>

**wb\_device\_get\_name** - *convert WbDeviceTag to its corresponding device name*

{[C++](cpp-api.md#cpp_device)}, {[Java](java-api.md#java_device)}, {[Python](python-api.md#python_device)}, {[Matlab](matlab-api.md#matlab_device)}

``` c
#include <webots/device.h>

const char *wb_device_get_name(WbDeviceTag tag)
```

**Description**

`wb_device_get_name()` convert the WbDeviceTag given as parameter (`tag`) to its
corresponding name.

This function returns NULL if the WbDeviceTag does not match a valid device.

---

<a name="wb_device_get_node_type">**Name**</a>

**wb\_device\_get\_node\_type** - *convert WbDeviceTag to its corresponding WbNodeType*

{[C++](cpp-api.md#cpp_device)}, {[Java](java-api.md#java_device)}, {[Python](python-api.md#python_device)}, {[Matlab](matlab-api.md#matlab_device)}

``` c
#include <webots/device.h>

WbNodeType wb_device_get_node_type(WbDeviceTag tag)
```

**Description**

`wb_device_get_node_type()` convert the WbDeviceTag given as parameter (`tag`)
to its corresponding WbNodeType (cf. the [Supervisor](supervisor.md#supervisor)
API)

This function returns NULL if the WbDeviceTag does not match a valid device.

