## Matlab API

The following tables describe the Matlab functions.

| % `Accelerometer` : |
| --- |
| `wb_accelerometer_enable`(tag, ms) |
| `wb_accelerometer_disable`(tag) |
| period = `wb_accelerometer_get_sampling_period`(tag) |
| [x y z] = `wb_accelerometer_get_values`(tag) |



| % `Brake` : |
| --- |
| `wb_brake_set_damping_constant`(tag, dampingConstant) |
| type = `wb_brake_get_type`(tag) |



| % `Camera` : |
| --- |
| WB\_CAMERA\_COLOR |
| WB\_CAMERA\_RANGE\_FINDER |
| `wb_camera_enable`(tag, ms) |
| `wb_camera_disable`(tag) |
| period = `wb_camera_get_sampling_period`(tag) |
| fov = `wb_camera_get_fov`(tag) |
| fov = `wb_camera_get_min_fov`(tag) |
| fov = `wb_camera_get_max_fov`(tag) |
| `wb_camera_set_fov`(tag, fov) |
| fov = `wb_camera_get_focal_length`(tag) |
| fov = `wb_camera_get_focal_distance`(tag) |
| fov = `wb_camera_get_max_focal_distance`(tag) |
| fov = `wb_camera_get_min_focal_distance`(tag) |
| `wb_camera_set_focal_distance`(tag, focal\_distance) |
| width = `wb_camera_get_width`(tag) |
| height = `wb_camera_get_height`(tag) |
| near = `wb_camera_get_near`(tag) |
| type = `wb_camera_get_type`(tag) |
| image = `wb_camera_get_image`(tag) |
| image = `wb_camera_get_range_image`(tag) |
| max\_range = `wb_camera_get_max_range`(tag) |
| `wb_camera_save_image`(tag, 'filename', quality) |



| % `Compass` : |
| --- |
| `wb_compass_enable`(tag, ms) |
| `wb_compass_disable`(tag) |
| period = `wb_compass_get_sampling_period`(tag) |
| [x y z] = `wb_compass_get_values`(tag) |



| % `Connector` : |
| --- |
| `wb_connector_enable_presence`(tag, ms) |
| `wb_connector_disable_presence`(tag) |
| presence = `wb_connector_get_presence`(tag) |
| `wb_connector_lock`(tag) |
| `wb_connector_unlock`(tag) |



| % `Device` : |
| --- |
| model = `wb_device_get_model`(tag) |
| name = `wb_device_get_name`(tag) |
| type = `wb_device_get_node_type`(tag) |



| % `DifferentialWheels` : |
| --- |
| `wb_differential_wheels_set_speed`(left, right) |
| left = `wb_differential_wheels_get_left_speed`() |
| right = `wb_differential_wheels_get_right_speed`() |
| `wb_differential_wheels_enable_encoders`(ms) |
| `wb_differential_wheels_disable_encoders`() |
| period = `wb_differential_wheels_get_encoders_sampling_period`() |
| left = `wb_differential_wheels_get_left_encoder`() |
| right = `wb_differential_wheels_get_right_encoder`() |
| `wb_differential_wheels_set_encoders`(left, right) |
| max = `wb_differential_wheels_get_max_speed`() |
| unit = `wb_differential_wheels_get_speed_unit`() |



| % `Display` : |
| --- |
| RGB |
| RGBA |
| ARGB |
| BGRA |
| width = `wb_display_get_width`(tag) |
| height = `wb_display_get_height`(tag) |
| `wb_display_set_color`(tag, [r g b]) |
| `wb_display_set_alpha`(tag, alpha) |
| `wb_display_set_opacity`(tag, opacity) |
| `wb_display_draw_pixel`(tag, x, y) |
| `wb_display_draw_line`(tag, x1, y1, x2, y2) |
| `wb_display_draw_rectangle`(tag, x, y, width, height) |
| `wb_display_draw_oval`(tag, cx, cy, a, b) |
| `wb_display_draw_polygon`(tag, [x1 x2 ... xn], [y1 y2 ... yn]) |
| `wb_display_draw_text`(tag, 'txt', x, y) |
| `wb_display_fill_rectangle`(tag, x, y, width, height) |
| `wb_display_fill_oval`(tag, cx, cy, a, b) |
| `wb_display_fill_polygon`(tag, [x1 x2 ... xn], [y1 y2 ... yn]) |
| image = `wb_display_image_copy`(tag, x, y, width, height) |
| `wb_display_image_paste`(tag, image, x, y) |
| image = `wb_display_image_load`(tag, 'filename') |
| image = `wb_display_image_new`(tag, width, height, data ,format) |
| `wb_display_image_save`(tag, image, 'filename') |
| `wb_display_image_delete`(tag, image) |



| % `DistanceSensor` : |
| --- |
| `wb_distance_sensor_enable`(tag, ms) |
| `wb_distance_sensor_disable`(tag) |
| period = `wb_distance_sensor_get_sampling_period`(tag) |
| value = `wb_distance_sensor_get_value`(tag) |



| % `Emitter` : |
| --- |
| WB\_CHANNEL\_BROADCAST |
| `wb_emitter_send`(tag, data) |
| `wb_emitter_set_channel`(tag, channel) |
| channel = `wb_emitter_get_channel`(tag) |
| range = `wb_emitter_get_range`(tag) |
| `wb_emitter_set_range`(tag, range) |
| size = `wb_emitter_get_buffer_size`(tag) |



| % `GPS` : |
| --- |
| `wb_gps_enable`(tag, ms) |
| `wb_gps_disable`(tag) |
| period = `wb_gps_get_sampling_period`(tag) |
| [x y z] = `wb_gps_get_values`(tag) |



| % `Gyro` : |
| --- |
| `wb_gyro_enable`(tag, ms) |
| `wb_gyro_disable`(tag) |
| period = `wb_gyro_get_sampling_period`(tag) |
| [x y z] = `wb_gyro_get_values`(tag) |



| % `InertialUnit` : |
| --- |
| `wb_inertial_unit_enable`(tag, ms) |
| `wb_inertial_unit_disable`(tag) |
| period = `wb_inertial_unit_get_sampling_period`(tag) |
| [roll pitch yaw] = `wb_inertial_unit_get_roll_pitch_yaw`(tag) |



| % `LED` : |
| --- |
| `wb_led_set`(tag, state) |
| state = `wb_led_get`(tag) |



| % `LightSensor` : |
| --- |
| `wb_light_sensor_enable`(tag, ms) |
| `wb_light_sensor_disable`(tag) |
| period = `wb_light_sensor_get_sampling_period`(tag) |
| value = `wb_light_sensor_get_value`(tag) |



| % `Motion` : |
| --- |
| motion = `wbu_motion_new`('filename') |
| `wbu_motion_delete`(motion) |
| `wbu_motion_play`(motion) |
| `wbu_motion_stop`(motion) |
| `wbu_motion_set_loop`(motion, loop) |
| `wbu_motion_set_reverse`(motion, reverse) |
| over = `wbu_motion_is_over`(motion) |
| duration = `wbu_motion_get_duration`(motion) |
| time = `wbu_motion_get_time`(motion) |
| `wbu_motion_set_time`(motion, time) |



| % `Motor` : |
| --- |
| WB\_MOTOR\_ROTATIONAL, WB\_MOTOR\_LINEAR |
| `wb_motor_set_position`(tag, position) |
| `wb_motor_set_velocity`(tag, vel) |
| `wb_motor_set_acceleration`(tag, acc) |
| `wb_motor_set_available_force`(tag, force) |
| `wb_motor_set_available_torque`(tag, torque) |
| `wb_motor_set_control_pid`(tag, p, i, d) |
| target = `wb_motor_get_target_position`(tag) |
| min = `wb_motor_get_min_position`(tag) |
| max = `wb_motor_get_max_position`(tag) |
| vel = `wb_motor_get_velocity`(tag) |
| vel = `wb_motor_get_max_velocity`(tag) |
| acc = `wb_motor_get_acceleration`(tag) |
| force = `wb_motor_get_available_force`(tag) |
| force = `wb_motor_get_max_force`(tag) |
| torque = `wb_motor_get_available_torque`(tag) |
| torque = `wb_motor_get_max_torque`(tag) |
| `wb_motor_enable_force_feedback`(tag, ms) |
| `wb_motor_disable_force_feedback`(tag) |
| period = `wb_motor_get_force_feedback_sampling_period`(tag) |
| force = `wb_motor_get_force_feedback`(tag) |
| `wb_motor_set_force`(tag, force) |
| `wb_motor_enable_torque_feedback`(tag, ms) |
| `wb_motor_disable_torque_feedback`(tag) |
| period = `wb_motor_get_torque_feedback_sampling_period`(tag) |
| force = `wb_motor_get_torque_feedback`(tag) |
| `wb_motor_set_torque`(tag, torque) |
| type = `wb_motor_get_type`(tag) |



| Node: |
| --- |
| WB\_NODE\_NO\_NODE, WB\_NODE\_APPEARANCE, WB\_NODE\_BACKGROUND, |
| WB\_NODE\_BOX, WB\_NODE\_COLOR, WB\_NODE\_CONE, |
| WB\_NODE\_COORDINATE,  WB\_NODE\_CYLINDER, |
| WB\_NODE\_DIRECTIONAL\_LIGHT, WB\_NODE\_ELEVATION\_GRID, |
| WB\_NODE\_EXTRUSION, WB\_NODE\_FOG, WB\_NODE\_GROUP, |
| WB\_NODE\_IMAGE\_TEXTURE, WB\_NODE\_INDEXED\_FACE\_SET, |
| WB\_NODE\_INDEXED\_LINE\_SET, WB\_NODE\_MATERIAL, |
| WB\_NODE\_POINT\_LIGHT,  WB\_NODE\_SHAPE, WB\_NODE\_SPHERE, |
| WB\_NODE\_SPOT\_LIGHT, WB\_NODE\_SWITCH, |
| WB\_NODE\_TEXTURE\_COORDINATE, WB\_NODE\_TEXTURE\_TRANSFORM, |
| WB\_NODE\_TRANSFORM, WB\_NODE\_VIEWPOINT, WB\_NODE\_WORLD\_INFO, |
| WB\_NODE\_CAPSULE, WB\_NODE\_PLANE, WB\_NODE\_ROBOT, |
| WB\_NODE\_SUPERVISOR, WB\_NODE\_DIFFERENTIAL\_WHEELS, |
| WB\_NODE\_SOLID, WB\_NODE\_PHYSICS, WB\_NODE\_CAMERA\_ZOOM, |
| WB\_NODE\_CHARGER, WB\_NODE\_DAMPING, |
| WB\_NODE\_CONTACT\_PROPERTIES, WB\_NODE\_ACCELEROMETER, WB\_NODE\_BRAKE, |
| WB\_NODE\_CAMERA, WB\_NODE\_COMPASS, WB\_NODE\_CONNECTOR, |
| WB\_NODE\_DISPLAY, WB\_NODE\_DISTANCE\_SENSOR, WB\_NODE\_EMITTER, |
| WB\_NODE\_GPS, WB\_NODE\_GYRO, WB\_NODE\_LED, |
| WB\_NODE\_LIGHT\_SENSOR, WB\_NODE\_MICROPHONE, WB\_NODE\_MOTOR, |
| WB\_NODE\_PEN, WB\_NODE\_POSITION\_SENSOR, WB\_NODE\_RADIO, |
| WB\_NODE\_RECEIVER, WB\_NODE\_SERVO, WB\_NODE\_SPEAKER, |
| WB\_NODE\_TOUCH\_SENSOR |



| % `Pen` : |
| --- |
| `wb_pen_write`(tag, write) |
| `wb_pen_set_ink_color`(tag, [r g b], density) |



| % `PositionSensor` : |
| --- |
| WB\_ANGULAR, WB\_LINEAR |
| `wb_position_sensor_enable`(tag, ms) |
| `wb_position_sensor_disable`(tag) |
| period = `wb_position_sensor_get_sampling_period`(tag) |
| value = `wb_position_sensor_get_value`(tag) |
| type = `wb_position_sensor_get_type`(tag) |



| % `Receiver` : |
| --- |
| WB\_CHANNEL\_BROADCAST |
| `wb_receiver_enable`(tag, ms) |
| `wb_receiver_disable`(tag) |
| period = `wb_receiver_get_sampling_period`(tag) |
| length = `wb_receiver_get_queue_length`(tag) |
| `wb_receiver_next_packet`(tag) |
| size = `wb_receiver_get_data_size`(tag) |
| data = `wb_receiver_get_data`(tag) |
| strength = `wb_receiver_get_signal_strength`(tag) |
| [x y z] = `wb_receiver_get_emitter_direction`(tag) |
| `wb_receiver_set_channel`(tag, channel) |
| channel = `wb_receiver_get_channel`(tag) |



| % `Robot` : |
| --- |
| WB\_MODE\_SIMULATION, |
| WB\_MODE\_CROSS\_COMPILATION, |
| WB\_MODE\_REMOTE\_CONTROL |
| WB\_ROBOT\_KEYBOARD\_END |
| WB\_ROBOT\_KEYBOARD\_HOME |
| WB\_ROBOT\_KEYBOARD\_LEFT |
| WB\_ROBOT\_KEYBOARD\_UP |
| WB\_ROBOT\_KEYBOARD\_RIGHT |
| WB\_ROBOT\_KEYBOARD\_DOWN |
| WB\_ROBOT\_KEYBOARD\_PAGEUP |
| WB\_ROBOT\_KEYBOARD\_PAGEDOWN |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_HOME |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_LEFT |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_UP |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_RIGHT |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_DOWN |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_END |
| WB\_ROBOT\_KEYBOARD\_KEY |
| WB\_ROBOT\_KEYBOARD\_SHIFT |
| WB\_ROBOT\_KEYBOARD\_CONTROL |
| WB\_ROBOT\_KEYBOARD\_ALT |
| `wb_robot_step`(ms) |
| tag = `wb_robot_get_device`('name') |
| size = `wb_robot_get_number_of_devices`() |
| tag = `wb_robot_get_device_by_index`(index) |
| `wb_robot_battery_sensor_enable`(ms) |
| `wb_robot_battery_sensor_disable`() |
| period = `wb_robot_battery_sensor_get_sampling_period`() |
| value = `wb_robot_battery_sensor_get_value`() |
| step = `wb_robot_get_basic_time_step`() |
| mode = `wb_robot_get_mode`() |
| model = `wb_robot_get_model`() |
| data = `getData`() |
| `setData`('data') |
| name = `wb_robot_get_name`() |
| name = `wb_robot_get_controller_name`() |
| name = `wb_robot_get_controller_arguments`() |
| path = `wb_robot_get_project_path`() |
| sync = `wb_robot_get_synchronization`() |
| time = `wb_robot_get_time`() |
| path = `wb_robot_get_world_path`() |
| `wb_robot_keyboard_enable`(ms) |
| `wb_robot_keyboard_disable`() |
| key = `wb_robot_keyboard_get_key`() |
| type = `wb_robot_get_type`() |



| % `Servo` : |
| --- |
| WB\_SERVO\_ROTATIONAL, WB\_SERVO\_LINEAR |
| `wb_servo_set_position`(tag, position) |
| target = `wb_servo_get_target_position`(tag) |
| `wb_servo_set_velocity`(tag, vel) |
| `wb_servo_set_acceleration`(tag, acc) |
| `wb_servo_set_motor_force`(tag, force) |
| `wb_servo_set_control_p`(tag, p) |
| min = `wb_servo_get_min_position`(tag) |
| max = `wb_servo_get_max_position`(tag) |
| `wb_servo_enable_position`(tag, ms) |
| `wb_servo_disable_position`(tag) |
| period = `wb_servo_get_position_sampling_period`(tag) |
| position = `wb_servo_get_position`(tag) |
| `wb_servo_enable_motor_force_feedback`(tag, ms) |
| `wb_servo_disable_motor_force_feedback`(tag) |
| period = `wb_servo_get_motor_force_feedback_sampling_period`(tag) |
| force = `wb_servo_get_motor_force_feedback`(tag) |
| `wb_servo_set_force`(tag, force) |
| type = `wb_servo_get_type`(tag) |



| % `Supervisor` : |
| --- |
| WB\_SF\_BOOL, WB\_SF\_INT32, WB\_SF\_FLOAT, WB\_SF\_VEC2F, |
| WB\_SF\_VEC3F, WB\_SF\_ROTATION, WB\_SF\_COLOR, WB\_SF\_STRING, |
| WB\_SF\_NODE, WB\_MF, WB\_MF\_INT32, WB\_MF\_FLOAT, B\_MF\_VEC2F, |
| WB\_MF\_VEC3F, WB\_MF\_COLOR, WB\_MF\_STRING, WB\_MF\_NODE |
| WB\_SUPERVISOR\_MOVIE\_READY, WB\_SUPERVISOR\_MOVIE\_RECORDING,
WB\_SUPERVISOR\_MOVIE\_SAVING, WB\_SUPERVISOR\_MOVIE\_WRITE\_ERROR,
WB\_SUPERVISOR\_MOVIE\_ENCODING\_ERROR, WB\_SUPERVISOR\_MOVIE\_SIMULATION\_ERROR |
| `wb_supervisor_export_image`('filename', quality) |
| node = `wb_supervisor_node_get_root`() |
| node = `wb_supervisor_node_get_self`() |
| node = `wb_supervisor_node_get_from_def`('def') |
| node = `wb_supervisor_node_get_from_id`('id') |
| id = `wb_supervisor_node_get_id`(node) |
| node = `wb_supervisor_node_get_parent_node`(node) |
| `wb_supervisor_node_remove`(node) |
| `wb_supervisor_set_label`(id, 'text', x, y, size, [r g b], transparency) |
| `wb_supervisor_simulation_quit`(status) |
| `wb_supervisor_simulation_revert`() |
| `wb_supervisor_simulation_reset_physics`() |
| `wb_supervisor_load_world`('filename') |
| `wb_supervisor_save_world`() |
| `wb_supervisor_save_world`('filename') |
| `wb_supervisor_movie_start_recording`('filename', width, height, codec, quality, |
| acceleration, caption) |
| `wb_supervisor_movie_stop_recording`() |
| status = `wb_supervisor_movie_get_status`() |
| success = `wb_supervisor_animation_start_recording`('filename') |
| success = `wb_supervisor_animation_stop_recording`() |
| type = `wb_supervisor_field_get_type`(field) |
| name = `wb_supervisor_field_get_type_name`(field) |
| count = `wb_supervisor_field_get_count`(field) |
| b = `wb_supervisor_field_get_sf_bool`(field) |
| i = `wb_supervisor_field_get_sf_int32`(field) |
| f = `wb_supervisor_field_get_sf_float`(field) |
| [x y] = `wb_supervisor_field_get_sf_vec2f`(field) |
| [x y z] = `wb_supervisor_field_get_sf_vec3f`(field) |
| [x y z alpha] = `wb_supervisor_field_get_sf_rotation`(field) |
| [r g b] = `wb_supervisor_field_get_sf_color`(field) |
| s = `wb_supervisor_field_get_sf_string`(field) |
| node = `wb_supervisor_field_get_sf_node`(field) |
| b = `wb_supervisor_field_get_mf_bool`(field, index) |
| i = `wb_supervisor_field_get_mf_int32`(field, index) |
| f = `wb_supervisor_field_get_mf_float`(field, index) |
| [x y] = `wb_supervisor_field_get_mf_vec2f`(field, index) |
| [x y z] = `wb_supervisor_field_get_mf_vec3f`(field, index) |
| [x y z a] = `wb_supervisor_field_get_mf_rotation`(field, index) |
| [r g b] = `wb_supervisor_field_get_mf_color`(field, index) |
| s = `wb_supervisor_field_get_mf_string`(field, index) |
| node = `wb_supervisor_field_get_mf_node`(field, index) |
| `wb_supervisor_field_set_sf_bool`(field, value) |
| `wb_supervisor_field_set_sf_int32`(field, value) |
| `wb_supervisor_field_set_sf_float`(field, value) |
| `wb_supervisor_field_set_sf_vec2f`(field, [x y]) |
| `wb_supervisor_field_set_sf_vec3f`(field, [x y z]) |
| `wb_supervisor_field_set_sf_rotation`(field, [x y z alpha]) |
| `wb_supervisor_field_set_sf_color`(field, [r g b]) |
| `wb_supervisor_field_set_sf_string`(field, 'value') |
| `wb_supervisor_field_set_mf_bool`(field, index, value) |
| `wb_supervisor_field_set_mf_int32`(field, index, value) |
| `wb_supervisor_field_set_mf_float`(field, index, value) |
| `wb_supervisor_field_set_mf_vec2f`(field, index, [x y]) |
| `wb_supervisor_field_set_mf_vec3f`(field, index, [x y z]) |
| `wb_supervisor_field_set_mf_rotation`(field, index, [x y z a]) |
| `wb_supervisor_field_set_mf_color`(field, index, [r g b]) |
| `wb_supervisor_field_set_mf_string`(field, index, 'value') |
| `wb_supervisor_field_import_mf_node`(field, position, 'filename') |
| `wb_supervisor_field_import_mf_node_from_string`(field, position,
'node\_string') |
| `wb_supervisor_field_remove_mf_node`(field, position) |
| type = `wb_supervisor_node_get_type`(node) |
| name = `wb_supervisor_node_get_type_name`(node) |
| name = `wb_supervisor_node_get_base_type_name`(node) |
| field = `wb_supervisor_node_get_field`(node, 'field\_name') |
| position = `wb_supervisor_node_get_position`(node) |
| orientation = `wb_supervisor_node_get_orientation`(node) |
| com = `wb_supervisor_node_get_center_of_mass`(node) |
| contact\_point = `wb_supervisor_node_get_contact_point`(node, index) |
| number\_of\_contacts = `wb_supervisor_node_get_number_of_contact_points`(index) |
| balance = `wb_supervisor_node_get_static_balance`(node) |
| velocity = `wb_supervisor_node_get_velocity`(node) |
| `wb_supervisor_node_set_velocity`(node, velocity) |
| `wb_supervisor_node_reset_physics`(node) |



| % `TouchSensor` : |
| --- |
| WB\_TOUCH\_SENSOR\_BUMPER, WB\_TOUCH\_SENSOR\_FORCE, |
| WB\_TOUCH\_SENSOR\_FORCE3D |
| `wb_touch_sensor_enable`(tag, ms) |
| `wb_touch_sensor_disable`(tag) |
| period = `wb_touch_sensor_get_sampling_period`(tag) |
| value = `wb_touch_sensor_get_value`(tag) |
| [x y z] = `wb_touch_sensor_get_values`(tag) |
| type = `wb_touch_sensor_get_type`(tag) |



