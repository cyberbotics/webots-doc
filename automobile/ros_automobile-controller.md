## "ros_automobile" Controller

The `ros_automobile` controller provides an interface between ROS, the `libdriver` and `libcar` libraries.
In addition to the servies and topics available in the default ROS controller, additional services and topics are available with the `ros_automobile` controller.

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| [`/automobile/brake_intensity`](driver-library.md#wbu_driver_set_brake_intensity) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/current_speed`](driver-library.md#wbu_driver_get_current_speed) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/rpm`](driver-library.md#wbu_driver_get_rpm) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/steering_angle`](driver-library.md#wbu_driver_set_steering_angle) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/right_steering_angle`](car-library.md#wbu_car_get_right_steering_angle) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/left_steering_angle`](car-library.md#wbu_car_get_right_steering_angle) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/throttle`](driver-library.md#wbu_driver_set_throttle) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/front_right_wheel_encoder`](car-library.md#wbu_car_get_wheel_encoder)<br/>[`/automobile/front_left_wheel_encoder`](car-library.md#wbu_car_get_wheel_encoder)<br/>[`/automobile/rear_right_wheel_encoder`](car-library.md#wbu_car_get_wheel_encoder)<br/>[`/automobile/rear_left_wheel_encoder`](car-library.md#wbu_car_get_wheel_encoder) | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/front_right_wheel_speed`](car-library.md#wbu_car_get_wheel_encoder)<br/>[`/automobile/front_left_wheel_speed`](car-library.md#wbu_car_get_wheel_encoder)<br/>[`/automobile/rear_right_wheel_speed`](car-library.md#wbu_car_get_wheel_encoder)<br/>[`/automobile/rear_left_wheel_speed`](car-library.md#wbu_car_get_wheel_encoder)<br/> | `topic` | `webots_ros::Float64Stamped` | [`Header`](http://docs.ros.org/api/std_msgs/html/msg/Header.html) `header`<br/>`float64 data` |
| [`/automobile/enable_indicator_auto_disabling`](car-library.md#wbu_car_enable_indicator_auto_disabling) | `service` | `webots_ros::set_bool` | |
| [`/automobile/enable_limited_slip_differential`](car-library.md#wbu_car_enable_limited_slip_differential) | `service` | `webots_ros::set_bool` | |
| [`/automobile/get_antifog_light`](driver-library.md#wbu_driver_set_dipped_beams) | `service` | `webots_ros::get_bool` | |
| [`/automobile/get_backwards_light`](car-library.md#wbu_car_get_backwards_lights) | `service` | `webots_ros::get_bool` | |
| [`/automobile/get_brake_light`](car-library.md#wbu_car_get_backwards_lights) | `service` | `webots_ros::get_bool` | |
| [`/automobile/get_control_mode`](driver-library.md#wbu_driver_get_control_mode) | `service` | `webots_ros::get_int` | |
| [`/automobile/get_cruising_speed`](driver-library.md#wbu_driver_set_cruising_speed) | `service` | `webots_ros::get_float` | |
| [`/automobile/get_dimensions`](car-library.md#wbu_car_get_track_front) | `service` | `webots_ros::automobile_get_dimensions` | `uint8 ask`<br/>---<br/>`float64 trackFront`<br/>`float64 trackRear`<br/>`float64 wheelBase`<br/>`float64 frontWheelRadius`<br/>`float64 rearWheelRadius` |
| [`/automobile/get_dipped_beam`](driver-library.md#wbu_driver_set_dipped_beams) | `service` | `webots_ros::get_bool` | |
| [`/automobile/get_engine_type`](car-library.md#wbu_car_get_type) | `service` | `webots_ros::get_int` | |
| [`/automobile/get_gear`](driver-library.md#wbu_driver_set_gear) | `service` | `webots_ros::get_int` | |
| [`/automobile/get_gear_number`](driver-library.md#wbu_driver_set_gear) | `service` | `webots_ros::get_int` | |
| [`/automobile/get_hazard_flashers`](driver-library.md#wbu_driver_set_dipped_beams) | `service` | `webots_ros::get_bool` | |
| [`/automobile/get_indicator`](driver-library.md#wbu_driver_set_dipped_beams) | `service` | `webots_ros::get_bool` | |
| [`/automobile/get_indicator_period`](car-library.md#wbu_car_set_indicator_period) | `service` | `webots_ros::get_float` | |
| [`/automobile/get_type`](car-library.md#wbu_car_get_type) | `service` | `webots_ros::get_int` | |
| [`/automobile/get_wipers_mode`](driver-library.md#wbu_driver_set_wipers_mode) | `service` | `webots_ros::get_int` | |
| [`/automobile/set_antifog_light`](driver-library.md#wbu_driver_set_dipped_beams) | `service` | `webots_ros::set_bool` | |
| [`/automobile/set_brake_intensity`](driver-library.md#wbu_driver_set_brake_intensity) | `service` | `webots_ros::set_float` | |
| [`/automobile/set_cruising_speed`](driver-library.md#wbu_driver_set_cruising_speed) | `service` | `webots_ros::set_float` | |
| [`/automobile/set_dipped_beam`](driver-library.md#wbu_driver_set_dipped_beams) | `service` | `webots_ros::set_bool` | |
| [`/automobile/set_gear`](driver-library.md#wbu_driver_set_gear) | `service` | `webots_ros::set_int` | |
| [`/automobile/set_indicator`](driver-library.md#wbu_driver_set_indicator) | `service` | `webots_ros::set_bool` | |
| [`/automobile/set_indicator_period`](car-library.md#wbu_car_set_indicator_period) | `service` | `webots_ros::set_float` | |
| [`/automobile/set_hazard_flashers`](driver-library.md#wbu_driver_set_indicator) | `service` | `webots_ros::set_bool` | |
| [`/automobile/set_steering_angle`](driver-library.md#wbu_driver_set_steering_angle) | `service` | `webots_ros::set_float` | |
| [`/automobile/set_throttle`](driver-library.md#wbu_driver_set_throttle) | `service` | `webots_ros::set_float` | |
| [`/automobile/set_wipers_mode`](driver-library.md#wbu_driver_set_wipers_mode) | `service` | `webots_ros::set_int` | |

> **Note**: To enable synchronous simulation you will have to call the `/robot/time_step` service with a positive `step` argument.
Then each time this service is called a car step will be executed (set the `step` argument to 0 to disable synchronization).
