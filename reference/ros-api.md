## ROS API

### Common Services

The following table describes the ROS services shared between the Webots devices.

| `service` name | `service` definition |
| --- | --- |
| `get_bool` | `bool ask`<br/>`---`<br/>`bool success` |
| `get_float` | `bool ask`<br/>`---`<br/>`float64 value` |
| `get_int` | `bool ask`<br/>`---`<br/>`int32 value` |
| `get_string` | `bool ask`<br/>`---`<br/>`string value` |
| `set_bool` | `bool success`<br/>`---`<br/>`bool success` |
| `set_float` | `float64 value`<br/>`---`<br/>`bool success` |
| `set_float_array` | `float64[] values`<br/>`---`<br/>`bool success` |
| `set_int` | `int32 value`<br/>`---`<br/>`bool success` |
| `set_string` | `string value`<br/>`---`<br/>`bool success` |
