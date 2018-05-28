## ROS API

The following tables describe the available ros messages and services for each device.

The `<device_name>` should be replaced by the actual name of the device and each services/topics names should be prepended with `<robot_unique_name>` (have a look at the [User Guide](../guide/using-ros.md#standard-controller) for more information about the value of `robot_unique_name`).

### Common Services

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

### Accelerometer

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/values` | `topic` | [`sensor_msgs::Imu`](http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) `orientation`<br/>`float64[9] orientation_covariance`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `angular_velocity`<br/>`float64[9] angular_velocity_covariance`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `linear_acceleration`<br/>`float64[9] linear_acceleration_covariance`<br/><br/>Note: only the linear_acceleration is filled in |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### Brake

| name | service/topic | data type |
| --- | --- | --- |
| `/<device_name>/set_damping_constant` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) |
| `/<device_name>/get_type` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) |

### Camera

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/image` | `topic` | [`sensor_msgs::Image`](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`uint32 height`<br/>`uint32 width`<br/>`string encoding`<br/>`uint8 is_bigendian`<br/>`uint32 step`<br/>`uint8[] data` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_info` | `service` | `webots_ros::camera_get_info` | `uint8 ask`<br/>`---`<br/>`uint32 width`<br/>`uint32 height`<br/>`float64 Fov`<br/>`float64 nearRange` |
| `/<device_name>/get_focus_info` | `service` | `webots_ros::camera_get_focus_info` | `uint8 ask`<br/>`---`<br/>`float64 focalLength`<br/>`float64 focalDistance`<br/>`float64 maxFocalDistance`<br/>`float64 minFocalDistance` |
| `/<device_name>/get_zoom_info` | `service` | `webots_ros::camera_get_zoom_info` | `uint8 ask`<br/>`---`<br/>`float64 minFov`<br/>`float64 maxFov` |
| `/<device_name>/save_image` | `service` | `webots_ros::save_image` | `string filename`<br/>`int32 quality`<br/>`---`<br/>`int8 success` |
| `/<device_name>/set_fov` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_focal_distance` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/has_recognition` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/<device_name>/recognition_enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/recognition_get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/recognition_objects` | `topic` | `webots_ros::RecognitionObject` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `relative_position`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) `relative_orientation`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `position_on_image`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `size_on_image`<br/>`int32 number_of_colors`<br/>`int32[] test`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html)[] `colors`<br/>`string model`<br/><br/>Note: the z value of position_on_image and size_on_image should be ignored |

### Compass

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/values` | `topic` | [`sensor_msgs::MagneticField`](http://docs.ros.org/api/sensor_msgs/html/msg/MagneticField.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `magnetic_field`<br/>`float64[9] magnetic_field_covariance`<br/> |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### Connector

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/presence` | `topic` | `webots_ros/Int8Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`int8 data` |
| `/<device_name>/presence_sensor/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/presence_sensor/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/lock` | `service` | [`webots_ros::set_bool`](ros-api.md#common-services) | |

### Device

| name | service/topic | data type |
| --- | --- | --- |
| `/<device_name>/get_model` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) |
| `/<device_name>/get_name` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) |
| `/<device_name>/get_node_type` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) |

### DifferentialWheels

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/differential_wheels/lwheel and /differential_wheels/rwheel` | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| `/differential_wheels/set_encoders` | `service` | [`webots_ros::set_float_array`](ros-api.md#common-services) | |
| `/differential_wheels_encoders/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/differential_wheels_encoders/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/differential_wheels/set_speed` | `service` | [`webots_ros::set_float_array`](ros-api.md#common-services) | |
| /differential_wheels/subscribe_twist_commands | `service` | `webots_ros::differential_wheels_subscribe_twist_commands` | `uint8 subscribe`<br/>`---`<br/>`int8 success`<br/><br/>Note: this `service` is used to subscribe to a `topic` called '/differential_wheels/twist_commands' which should send [`geometry_msgs::Twist`](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html) commands. |
| `/differential_wheels/get_max_speed` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/differential_wheels/get_speed` | `service` | `webots_ros::differential_wheels_get_speed` | `uint8 ask`<br/>`---`<br/>`float64 speed` |
| `/differential_wheels/get_speed_unit` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |

### Display

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/get_info` | `service` | `webots_ros::display_get_info` | `uint8 ask`<br/>`---`<br/>`uint32 width`<br/>`uint32 height` |
| `/<device_name>/set_color` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/set_alpha` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_opacity` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_font` | `service` | `webots_ros::display_set_font` | `string font`<br/>`int32 size`<br/>`uint8 antiAliasing`<br/>`---`<br/>`int8 success` |
| `/<device_name>/set_attach_camera` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/<device_name>/set_detach_camera` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/<device_name>/draw_pixel` | `service` | `webots_ros::display_draw_pixel` | `int32 x1`<br/>`int32 y1`<br/>`---`<br/>`int8 success` |
| `/<device_name>/draw_line` | `service` | `webots_ros::display_draw_line` | `int32 x1`<br/>`int32 y1`<br/>`int32 x2`<br/>`int32 y2`<br/>`---`<br/>`int8 success` |
| `/<device_name>/draw_rectangle` | `service` | `webots_ros::display_draw_rectangle` | `int32 x`<br/>`int32 y`<br/>`int32 width`<br/>`int32 height`<br/>`---`<br/>`int8 success` |
| `/<device_name>/draw_oval` | `service` | `webots_ros::display_draw_oval` | `int32 cx`<br/>`int32 cy`<br/>`int32 a`<br/>`int32 b`<br/>`---`<br/>`int8 success` |
| `/<device_name>/draw_polygon` | `service` | `webots_ros::display_draw_polygon` | `int32[] x`<br/>`int32[] y`<br/>`int32 size`<br/>`---`<br/>`int8 success` |
| `/<device_name>/draw_text` | `service` | `webots_ros::display_draw_text` | `string text`<br/>`int32 x`<br/>`int32 y`<br/>`---`<br/>`int8 success` |
| `/<device_name>/fill_rectangle` | `service` | `webots_ros::display_draw_rectangle` | `int32 x`<br/>`int32 y`<br/>`int32 width`<br/>`int32 height`<br/>`---`<br/>`int8 success` |
| `/<device_name>/fill_oval` | `service` | `webots_ros::display_draw_oval` | `int32 cx`<br/>`int32 cy`<br/>`int32 a`<br/>`int32 b`<br/>`---`<br/>`int8 success` |
| `/<device_name>/fill_polygon` | `service` | `webots_ros::display_draw_polygon` | `int32[] x`<br/>`int32[] y`<br/>`int32 size`<br/>`---`<br/>`int8 success` |
| `/<device_name>/image_new` | `service` | `webots_ros::display_image_new` | `int32 width`<br/>`int32 height`<br/>`char[] data`<br/>`int32 format`<br/>`---`<br/>`uint64 ir` |
| `/<device_name>/image_copy` | `service` | `webots_ros::display_image_copy` | `int32 x`<br/>`int32 y`<br/>`int32 width`<br/>`int32 height`<br/>`---`<br/>`uint64 ir` |
| `/<device_name>/image_paste` | `service` | `webots_ros::display_image_paste` | `uint64 ir`<br/>`int32 x`<br/>`int32 y`<br/>`uint8 blend`<br/>`---`<br/>`int8 success` |
| `/<device_name>/image_load` | `service` | `webots_ros::display_image_load` | `string filename`<br/>`---`<br/>`uint64 ir` |
| `/<device_name>/image_save` | `service` | `webots_ros::display_image_save` | `string filename`<br/>`uint64 ir`<br/>`---`<br/>`int8 success` |
| `/<device_name>/image_delete` | `service` | `webots_ros::display_image_delete` | `uint64 ir`<br/>`---`<br/>`int8 success` |

### DistanceSensor

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/value` | `topic` | [`sensor_msgs::Range`](http://docs.ros.org/api/sensor_msgs/html/msg/Range.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`uint8 ULTRASOUND=0`<br/>`uint8 INFRARED=1`<br/>`uint8 radiation_type`<br/>`float32 field_of_view`<br/>`float32 min_range`<br/>`float32 max_range`<br/>`float32 range` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_aperture` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_max_value` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_min_value` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_type` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### Emitter

| name | service/topic | data type |
| --- | --- | --- |
| `/<device_name>/send` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) |
| `/<device_name>/get_buffer_size` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) |
| `/<device_name>/get_channel` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) |
| `/<device_name>/get_range` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) |
| `/<device_name>/set_channel` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) |
| `/<device_name>/set_range` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) |

### GPS

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/values` | `topic` | [`sensor_msgs::NavSatFix`](http://docs.ros.org/api/sensor_msgs/html/msg/NavSatFix.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`sensor_msgs/NavSatStatus`](http://docs.ros.org/api/sensor_msgs/html/msg/NavSatStatus.html) `status`<br/>`float64 latitude`<br/>`float64 longitude`<br/>`float64 altitude`<br/>`float64[9] position_covariance`<br/>`uint8 COVARIANCE_TYPE_UNKNOWN=0`<br/>`uint8 COVARIANCE_TYPE_APPROXIMATED=1`<br/>`uint8 COVARIANCE_TYPE_DIAGONAL_KNOWN=2`<br/>`uint8 COVARIANCE_TYPE_KNOWN=3`<br/>`uint8 position_covariance_type`<br/><br/>Note: coordinates may be set locally (X-Y-Z) instead of globally (lat-long-alt) depending on the GPS coordinate system used. |
| `/<device_name>/speed` | `topic` | webots_ros::Float64Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_coordinate_system` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/decimal_degrees_to_degrees_minutes_seconds` | `service` | `webots_ros::gps_decimal_degrees_to_degrees_minutes_seconds` | `float32 decimalDegrees`<br/>`---`<br/>`string degreesMinutesSeconds` |

### Gyro

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/values` | `topic` | [`sensor_msgs::Imu`](http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) `orientation`<br/>`float64[9] orientation_covariance`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `angular_velocity`<br/>`float64[9] angular_velocity_covariance`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `linear_acceleration`<br/>`float64[9] linear_acceleration_covariance`<br/><br/>Note: only the angular_velocity is filled in |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### InertialUnit

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/roll_pitch_yaw` | `topic` | [`sensor_msgs::Imu`](http://docs.ros.org/api/sensor_msgs/html/msg/Imu.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) `orientation`<br/>`float64[9] orientation_covariance`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `angular_velocity`<br/>`float64[9] angular_velocity_covariance`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `linear_acceleration`<br/>`float64[9] linear_acceleration_covariance`<br/><br/>Note: only the orientation is filled in |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### Joystick

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/joystick/pressed_button` | `topic` | webots_ros::Int8Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`int8 data` |
| `/joystick/axis<X>` | `topic` | webots_ros::Int8Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`int8 data` |
| `/joystick/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/joystick/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/joystick/get_number_of_axes` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/joystick/is_connected` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/joystick/get_model` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/joystick/set_constant_force` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/joystick/set_constant_force_duration` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/joystick/set_auto_centering_gain` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/joystick/set_resistance_gain` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |

### Keyboard

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/keyboard/key` | `topic` | webots_ros::Int32Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`int32 data` |
| `/keyboard/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/keyboard/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### LED

| name | service/topic | data type |
| --- | --- | --- |
| `/<device_name>/set_led` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) |
| `/<device_name>/get_led` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) |

### Lidar

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/range_image` | `topic` | [`sensor_msgs::Image`](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`uint32 height`<br/>`uint32 width`<br/>`string encoding`<br/>`uint8 is_bigendian`<br/>`uint32 step`<br/>`uint8[] data` |
| `/<device_name>/point_cloud` | `topic` | [`sensor_msgs::PointCloud`](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`geometry_msgs/Point32[]`](http://docs.ros.org/api/geometry_msgs/html/msg/Point32.html) `points`<br/>[`sensor_msgs/ChannelFloat32[]`](http://docs.ros.org/api/sensor_msgs/html/msg/ChannelFloat32.html) `channels`<br/>Note: the first channel is filled with the corresponding layer id. |
| `/<device_name>/laser_scan/layer<X>` | `topic` | [`sensor_msgs::LaserScan`](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float32 angle_min`<br/>`float32 angle_max`<br/>`float32 angle_increment`<br/>`float32 time_increment`<br/>`float32 scan_time`<br/>`float32 range_min`<br/>`float32 range_max`<br/>`float32[] ranges`<br/>`float32[] intensities` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/enable_point_cloud` | `service` | [`webots_ros::set_bool`](ros-api.md#common-services) | |
| `/<device_name>/get_layer_point_cloud` | `service` | `webots_ros::lidar_get_layer_point_cloud` | `int32 layer`<br/>`---`<br/>[`sensor_msgs::PointCloud`](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud.html) pointCloud |
| `/<device_name>/get_layer_range_image` | `service` | `webots_ros::lidar_get_layer_range_image` | `int32 layer`<br/>`---`<br/>[`sensor_msgs::Image`](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html) image |
| `/<device_name>/get_frequency_info` | `service` | `webots_ros::lidar_get_frequency_info` | `uint8 ask`<br/>`---`<br/>`float64 frequency`<br/>`float64 minFrequency`<br/>`float64 maxFrequency` |
| `/<device_name>/get_info` | `service` | `webots_ros::lidar_get_info` | `uint8 ask`<br/>`---`<br/>`uint32 horizontalResolution`<br/>`uint32 numberOfLayers`<br/>`float64 fov`<br/>`float64 verticalFov`<br/>`float64 minRange`<br/>`float64 maxRange` |
| `/<device_name>/is_point_cloud_enabled` | `service` | `webots_ros::node_get_status` | `uint8 ask`<br/>`---`<br/>`uint8 status` |
| `/<device_name>/set_frequency` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |

### LightSensor

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/value` | `topic` | [`sensor_msgs::Illuminance`](http://docs.ros.org/api/sensor_msgs/html/msg/Illuminance.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 illuminance`<br/>`float64 variance` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### Motor

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/set_acceleration` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_velocity` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_force` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_torque` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_available_torque` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_available_force` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/set_control_pid` | `service` | `webots_ros::motor_set_control_pid` | `float64 controlp`<br/>`float64 controli`<br/>`float64 controld`<br/>`---`<br/>`int8 success` |
| `/<device_name>/set_position` | `service` | [`webots_ros::set_float`](ros-api.md#common-services) | |
| `/<device_name>/get_target_position` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_min_position` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_max_position` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_velocity` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_max_velocity` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_acceleration` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_type` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_available_torque` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_available_force` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_max_torque` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_max_force` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/torque_feedback` | `topic` | webots_ros::Float64Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| `/<device_name>/force_feedback` | `topic` | webots_ros::Float64Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| `/<device_name>/force_feedback_sensor/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/force_feedback_sensor/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### Mouse

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/mouse/key` | `topic` | webots_ros::Int32Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`int32 data` |
| `/mouse/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/mouse/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/mouse/get_state` | `service` | `webots_ros::sensor_get_state` | `uint8 ask`<br/>`---`<br/>`uint8 x`<br/>`uint8 y`<br/>`uint8 z`<br/>`float64 x`<br/>`float64 y`<br/>`float64 z` |

### Pen

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/write` | `service` | [`webots_ros::set_bool`](ros-api.md#common-services) | |
| `/<device_name>/set_ink_color` | `service` | `webots_ros::pen_set_ink_color` | `int32 color`<br/>`float64 density`<br/>`---`<br/>`int8 success` |

### PositionSensor

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/value` | `topic` | webots_ros::Float64Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_type` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |

### Radar

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/number_of_targets` | `topic` | webots_ros::Int8Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`int8 data` |
| `/<device_name>/targets` | `topic` | `webots_ros::RadarTarget` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 distance`<br/>`float64 receivedPower`<br/>`float64 speed`<br/>`float64 azimuth` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_max_range` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_min_range` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_vertical_fov` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_horizontal_fov` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |

### RangeFinder

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/range_image` | `topic` | [`sensor_msgs::Image`](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`uint32 height`<br/>`uint32 width`<br/>`string encoding`<br/>`uint8 is_bigendian`<br/>`uint32 step`<br/>`uint8[] data` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_info` | `service` | `webots_ros::range_finder_get_info` | `uint8 ask`<br/>`---`<br/>`uint32 width`<br/>`uint32 height`<br/>`float64 Fov`<br/>`float64 minRange`<br/>`float64 maxRange` |
| `/<device_name>/save_image` | `service` | `webots_ros::save_image` | `string filename`<br/>`int32 quality`<br/>`---`<br/>`int8 success` |

### Receiver

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/data` | `topic` | `webots_ros::StringStamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`string data` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/set_channel` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_channel` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_queue_length` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/next_packet` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/<device_name>/get_data_size` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_signal_strength` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/<device_name>/get_emitter_direction` | `service` | `webots_ros::receiver_get_emitter_direction` | `uint8 ask`<br/>`---`<br/>`float64[] direction` |

### Robot

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/battery_sensor/value` | `topic` | webots_ros::Float64Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| `/robot/time_step` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/robot/get_controller_name` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/robot/get_controller_arguments` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/robot/get_time` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/robot/get_model` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/robot/get_custom_data` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/robot/set_custom_data` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/robot/get_mode` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/robot/get_synchronization` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/robot/get_project_path` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/robot/get_world_path` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/robot/get_basic_time_step` | `service` | [`webots_ros::get_float`](ros-api.md#common-services) | |
| `/robot/get_number_of_devices` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/robot/get_type` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/robot/set_mode` | `service` | `webots_ros::robot_set_mode` | `char[] arg`<br/>`int32 mode`<br/>`---`<br/>`int8 success` |
| /robot/get_device_list | `service` | `webots_ros::robot_get_device_list` | `uint8 ask`<br/>`---`<br/>`string[] list` |
| `/robot/wwi_receive_text` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/robot/wwi_send_text` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |

### Speaker

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/play_sound` | `service` | `webots_ros::speaker_play_sound` | `string sound`<br/>`float64 volume`<br/>`float64 pitch`<br/>`float64 balance`<br/>`int8 loop`<br/>`---`<br/>`int8 success` |
| `/<device_name>/stop` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/<device_name>/get_engine` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/<device_name>/get_language` | `service` | [`webots_ros::get_string`](ros-api.md#common-services) | |
| `/<device_name>/set_engine` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/<device_name>/set_language` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/<device_name>/speak` | `service` | webots_ros::speaker\speak | `string text`<br/>`float64 volume`<br/>`---`<br/>`int8 success`<br/> |

### Supervisor

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/supervisor/simulation_quit` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/supervisor/simulation_revert` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/supervisor/simulation_reset_physics` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/supervisor/supervisor_simulation_get_mode` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/supervisor/supervisor_simulation_set_mode` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/supervisor/load_world` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/supervisor/save_world` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/supervisor/export_image` | `service` | `webots_ros::save_image` | `string filename`<br/>`int32 quality`<br/>`---`<br/>`int8 success` |
| `/supervisor/animation_start_recording` | `service` | [`webots_ros::set_string`](ros-api.md#common-services) | |
| `/supervisor/animation_stop_recording` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/supervisor/movie_start_recording` | `service` | `webots_ros::supervisor_movie_start_recording` | `string filename`<br/>`int32 width`<br/>`int32 height`<br/>`int32 codec`<br/>`int32 quality`<br/>`int32 acceleration`<br/>`uint8 caption`<br/>`---`<br/>`int8 success` |
| `/supervisor/movie_stop_recording` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/supervisor/movie_is_ready` | `service` | `webots_ros::node_get_status` | `uint8 ask`<br/>`---`<br/>`uint8 status` |
| `/supervisor/movie_failed` | `service` | `webots_ros::node_get_status` | `uint8 ask`<br/>`---`<br/>`uint8 status` |
| `/supervisor/set_label` | `service` | `webots_ros::supervisor_set_label` | `int32 id`<br/>`string label`<br/>`float64 xpos`<br/>`float64 ypos`<br/>`float64 size`<br/>`int32 color`<br/>`float64 transparency`<br/>`string font`<br/>`---`<br/>`int8 success` |
| `/supervisor/get_root` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/supervisor/get_self` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/supervisor/get_from_def` | `service` | `webots_ros::supervisor_get_from_def` | `string name`<br/>`---`<br/>`uint64 node` |
| `/supervisor/get_from_id` | `service` | `webots_ros::supervisor_get_from_id` | `int32 id`<br/>`---`<br/>`uint64 node` |
| `/supervisor/get_selected` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/supervisor/vitual_reality_headset_get_orientation` | `service` | `webots_ros::supervisor_virtual_reality_headset_get_orientation` | `uint8 ask`<br/>`---`<br/>[`geometry_msgs/Point`](http://docs.ros.org/api/geometry_msgs/html/msg/Point.html) position |
| `/supervisor/vitual_reality_headset_get_position` | `service` | `webots_ros::supervisor_virtual_reality_headset_get_position` | `uint8 ask`<br/>`---`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) orientation |
| `/supervisor/vitual_reality_headset_is_used` | `service` | [`webots_ros::get_bool`](ros-api.md#common-services) | |
| `/supervisor/node/get_id` | `service` | `webots_ros::node_get_id` | `uint64 node`<br/>`---`<br/>`int32 id` |
| `/supervisor/node/get_type` | `service` | `webots_ros::node_get_type` | `uint64 node`<br/>`---`<br/>`int32 type` |
| `/supervisor/node/get_type_name` | `service` | `webots_ros::node_get_name` | `uint64 node`<br/>`---`<br/>`string name` |
| `/supervisor/node/get_base_type_name` | `service` | `webots_ros::node_get_name` | `uint64 node`<br/>`---`<br/>`string name` |
| `/supervisor/node/get_def` | `service` | `webots_ros::node_get_name` | `uint64 node`<br/>`---`<br/>`string name` |
| `/supervisor/node/get_parent_node` | `service` | `webots_ros::node_get_parent_node` | `uint64 node`<br/>`---`<br/>`uint64 node` |
| `/supervisor/node/get_position` | `service` | `webots_ros::node_get_position` | `uint64 node`<br/>`---`<br/>[`geometry_msgs/Point`](http://docs.ros.org/api/geometry_msgs/html/msg/Point.html) position |
| `/supervisor/node/get_orientation` | `service` | `webots_ros::node_get_orientation` | `uint64 node`<br/>`---`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) orientation |
| `/supervisor/node/get_center_of_mass` | `service` | `webots_ros::node_get_center_of_mass` | `uint64 node`<br/>`---`<br/>[`geometry_msgs/Point`](http://docs.ros.org/api/geometry_msgs/html/msg/Point.html) centerOfMass |
| `/supervisor/node/get_number_of_contact_points` | `service` | `webots_ros::node_get_number_of_contact_points` | `uint64 node`<br/>`---`<br/>`int32 numberOfContactPoints` |
| `/supervisor/node/get_contact_point` | `service` | `webots_ros::node_get_contact_point` | `uint64 node`<br/>`int32 index`<br/>`---`<br/>[`geometry_msgs/Point`](http://docs.ros.org/api/geometry_msgs/html/msg/Point.html) point |
| `/supervisor/node/get_static_balance` | `service` | `webots_ros::node_get_static_balance` | `uint64 node`<br/>`---`<br/>`uint8 balance` |
| `/supervisor/node/get_velocity` | `service` | `webots_ros::node_get_velocity` | `uint64 node`<br/>`---`<br/>[`geometry_msgs/Twist`](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html) velocity |
| `/supervisor/node/set_velocity` | `service` | `webots_ros::node_set_velocity` | `uint64 node`<br/>[`geometry_msgs/Twist`](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html) `velocity`<br/>`---`<br/>`int32 success` |
| `/supervisor/node/get_field` | `service` | `webots_ros::node_get_field` | `uint64 node`<br/>`string fieldName`<br/>`---`<br/>`uint64 field` |
| `/supervisor/node/remove` | `service` | `webots_ros::node_remove` | `uint64 node`<br/>`---`<br/>`int8 success` |
| `/supervisor/node/reset_physics` | `service` | `webots_ros::node_reset_functions` | `uint64 node`<br/>`---`<br/>`int8 success` |
| `/supervisor/node/restart_controller` | `service` | `webots_ros::node_reset_functions` | `uint64 node`<br/>`---`<br/>`int8 success` |
| `/supervisor/node/set_visibility` | `service` | `webots_ros::node_hide_from_camera` | `uint64 node`<br/>`uint64 from`<br/>`uint8 visible`<br/>`---`<br/>`int8 success` |
| `/supervisor/field/get_type` | `service` | `webots_ros::field_get_type` | `uint64 node`<br/>`---`<br/>`int8 success` |
| `/supervisor/field/get_type_name` | `service` | `webots_ros::field_get_type_name` | `uint64 field`<br/>`---`<br/>`string name` |
| `/supervisor/field/get_count` | `service` | `webots_ros::field_get_count` | `uint64 field`<br/>`---`<br/>`int32 count` |
| `/supervisor/field/get_bool` | `service` | `webots_ros::field_get_bool` | `uint64 field`<br/>`int32 index`<br/>`---`<br/>`uint8 value` |
| `/supervisor/field/get_int32` | `service` | webots_ros::field_get_`int32 `| `uint64 field`<br/>`int32 index`<br/>`---`<br/>`int32 value` |
| `/supervisor/field/get_float` | `service` | `webots_ros::field_get_float` | `uint64 field`<br/>`int32 index`<br/>`---`<br/>`float64 value` |
| `/supervisor/field/get_vec2f` | `service` | webots_ros::field_get_vec2f | `uint64 field`<br/>`int32 index`<br/>`---`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `value`<br/><br/>Note: the 'z' coordinate should be ignored. |
| `/supervisor/field/get_vec3f` | `service` | webots_ros::field_get_vec3f | `uint64 field`<br/>`int32 index`<br/>`---`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) value |
| `/supervisor/field/get_rotation` | `service` | `webots_ros::field_get_rotation` | `uint64 field`<br/>`int32 index`<br/>`---`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) value |
| `/supervisor/field/get_color` | `service` | `webots_ros::field_get_color` | `uint64 field`<br/>`int32 index`<br/>`---`<br/>[`std_msgs/ColorRGBA`](http://docs.ros.org/api/std_msgs/html/msg/ColorRGBA.html) value |
| `/supervisor/field/get_string` | `service` | `webots_ros::field_get_string` | `uint64 field`<br/>`int32 index`<br/>`---`<br/>`string value` |
| `/supervisor/field/get_node` | `service` | `webots_ros::field_get_node` | `uint64 field`<br/>`int32 index`<br/>`---`<br/>`uint64 node` |
| `/supervisor/field/set_bool` | `service` | `webots_ros::field_set_bool` | `uint64 field`<br/>`int32 index`<br/>`uint8 value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/set_int32` | `service` | webots_ros::field_set_`int32 `| `uint64 field`<br/>`int32 index`<br/>`int32 value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/set_float` | `service` | `webots_ros::field_set_float` | `uint64 field`<br/>`int32 index`<br/>`float64 value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/set_vec2f` | `service` | webots_ros::field_set_vec2f | `uint64 field`<br/>`int32 index`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `value`<br/>`---`<br/>`int32 success`<br/><br/>Note: the 'z' coordinate is ignored. |
| `/supervisor/field/set_vec3f` | `service` | webots_ros::field_set_vec3f | `uint64 field`<br/>`int32 index`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/set_rotation` | `service` | `webots_ros::field_set_rotation` | `uint64 field`<br/>`int32 index`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) `value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/set_color` | `service` | `webots_ros::field_set_color` | `uint64 field`<br/>`int32 index`<br/>[`std_msgs/ColorRGBA`](http://docs.ros.org/api/std_msgs/html/msg/ColorRGBA.html) `value`<br/>`---`<br/>`int32 success`<br/><br/>Note: the 'a' component is ignored. |
| `/supervisor/field/set_string` | `service` | `webots_ros::field_set_string` | `uint64 field`<br/>`int32 index`<br/>`string value`<br/>`---`<br/>`int32 success`<br/> |
| `/supervisor/field/insert_bool` | `service` | `webots_ros::field_set_bool` | `uint64 field`<br/>`int32 index`<br/>`uint8 value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/insert_int32` | `service` | webots_ros::field_set_`int32 `| `uint64 field`<br/>`int32 index`<br/>`int32 value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/insert_float` | `service` | `webots_ros::field_set_float` | `uint64 field`<br/>`int32 index`<br/>`float64 value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/insert_vec2f` | `service` | webots_ros::field_set_vec2f | `uint64 field`<br/>`int32 index`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `value`<br/>`---`<br/>`int32 success`<br/><br/>Note: the 'z' coordinate is ignored. |
| `/supervisor/field/insert_vec3f` | `service` | webots_ros::field_set_vec3f | `uint64 field`<br/>`int32 index`<br/>[`geometry_msgs/Vector3`](http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html) `value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/insert_rotation` | `service` | `webots_ros::field_set_rotation` | `uint64 field`<br/>`int32 index`<br/>[`geometry_msgs/Quaternion`](http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html) `value`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/insert_color` | `service` | `webots_ros::field_set_color` | `uint64 field`<br/>`int32 index`<br/>[`std_msgs/ColorRGBA`](http://docs.ros.org/api/std_msgs/html/msg/ColorRGBA.html) `value`<br/>`---`<br/>`int32 success`<br/><br/>Note: the 'a' component is ignored. |
| `/supervisor/field/insert_string` | `service` | `webots_ros::field_set_string` | `uint64 field`<br/>`int32 index`<br/>`string value`<br/>`---`<br/>`int32 success`<br/> |
| `/supervisor/field/remove` | `service` | `webots_ros::field_remove` | `uint64 field`<br/>`int32 index`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/import_node` | `service` | `webots_ros::field_import_node` | `uint64 field`<br/>`int32 position`<br/>`string filename`<br/>`---`<br/>`int32 success` |
| `/supervisor/field/import_node_from_string` | `service` | `webots_ros::field_import_node_from_string` | `uint64 field`<br/>`int32 position`<br/>`string nodeString`<br/>`---`<br/>`int32 success` |

### TouchSensor

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| `/<device_name>/value` | `topic` | webots_ros::Float64Stamped | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| `/<device_name>/values` | `topic` | [`geometry_msgs::WrenchStamped`](http://docs.ros.org/api/geometry_msgs/html/msg/WrenchStamped.html) | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>[`Wrench`](http://docs.ros.org/api/geometry_msgs/html/msg/Wrench.html) wrench |
| `/<device_name>/value` | `topic` | `webots_ros::BoolStamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`bool data` |
| `/<device_name>/enable` | `service` | [`webots_ros::set_int`](ros-api.md#common-services) | |
| `/<device_name>/get_sampling_period` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
| `/<device_name>/get_type` | `service` | [`webots_ros::get_int`](ros-api.md#common-services) | |
