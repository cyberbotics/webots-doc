## Matlab API

The following tables describe the Matlab functions.

% `Accelerometer` :
---
`wb_accelerometer_enable`(tag, ms)
`wb_accelerometer_disable`(tag)
period = `wb_accelerometer_get_sampling_period`(tag)
[x y z] = `wb_accelerometer_get_values`(tag)


% `Brake` :
---
`wb_brake_set_damping_constant`(tag, dampingConstant)
type = `wb_brake_get_type`(tag)


% `Camera` :
---
WB_CAMERA_COLOR
WB_CAMERA_RANGE_FINDER
`wb_camera_enable`(tag, ms)
`wb_camera_disable`(tag)
period = `wb_camera_get_sampling_period`(tag)
fov = `wb_camera_get_fov`(tag)
fov = `wb_camera_get_min_fov`(tag)
fov = `wb_camera_get_max_fov`(tag)
`wb_camera_set_fov`(tag, fov)
fov = `wb_camera_get_focal_length`(tag)
fov = `wb_camera_get_focal_distance`(tag)
fov = `wb_camera_get_max_focal_distance`(tag)
fov = `wb_camera_get_min_focal_distance`(tag)
`wb_camera_set_focal_distance`(tag, focal_distance)
width = `wb_camera_get_width`(tag)
height = `wb_camera_get_height`(tag)
near = `wb_camera_get_near`(tag)
type = `wb_camera_get_type`(tag)
image = `wb_camera_get_image`(tag)
image = `wb_camera_get_range_image`(tag)
max_range = `wb_camera_get_max_range`(tag)
`wb_camera_save_image`(tag, 'filename', quality)


% `Compass` :
---
`wb_compass_enable`(tag, ms)
`wb_compass_disable`(tag)
period = `wb_compass_get_sampling_period`(tag)
[x y z] = `wb_compass_get_values`(tag)


% `Connector` :
---
`wb_connector_enable_presence`(tag, ms)
`wb_connector_disable_presence`(tag)
presence = `wb_connector_get_presence`(tag)
`wb_connector_lock`(tag)
`wb_connector_unlock`(tag)


% `Device` :
---
model = `wb_device_get_model`(tag)
name = `wb_device_get_name`(tag)
type = `wb_device_get_node_type`(tag)


% `DifferentialWheels` :
---
`wb_differential_wheels_set_speed`(left, right)
left = `wb_differential_wheels_get_left_speed`()
right = `wb_differential_wheels_get_right_speed`()
`wb_differential_wheels_enable_encoders`(ms)
`wb_differential_wheels_disable_encoders`()
period = `wb_differential_wheels_get_encoders_sampling_period`()
left = `wb_differential_wheels_get_left_encoder`()
right = `wb_differential_wheels_get_right_encoder`()
`wb_differential_wheels_set_encoders`(left, right)
max = `wb_differential_wheels_get_max_speed`()
unit = `wb_differential_wheels_get_speed_unit`()


% `Display` :
---
RGB
RGBA
ARGB
BGRA
width = `wb_display_get_width`(tag)
height = `wb_display_get_height`(tag)
`wb_display_set_color`(tag, [r g b])
`wb_display_set_alpha`(tag, alpha)
`wb_display_set_opacity`(tag, opacity)
`wb_display_draw_pixel`(tag, x, y)
`wb_display_draw_line`(tag, x1, y1, x2, y2)
`wb_display_draw_rectangle`(tag, x, y, width, height)
`wb_display_draw_oval`(tag, cx, cy, a, b)
`wb_display_draw_polygon`(tag, [x1 x2 ... xn], [y1 y2 ... yn])
`wb_display_draw_text`(tag, 'txt', x, y)
`wb_display_fill_rectangle`(tag, x, y, width, height)
`wb_display_fill_oval`(tag, cx, cy, a, b)
`wb_display_fill_polygon`(tag, [x1 x2 ... xn], [y1 y2 ... yn])
image = `wb_display_image_copy`(tag, x, y, width, height)
`wb_display_image_paste`(tag, image, x, y)
image = `wb_display_image_load`(tag, 'filename')
image = `wb_display_image_new`(tag, width, height, data ,format)
`wb_display_image_save`(tag, image, 'filename')
`wb_display_image_delete`(tag, image)


% `DistanceSensor` :
---
`wb_distance_sensor_enable`(tag, ms)
`wb_distance_sensor_disable`(tag)
period = `wb_distance_sensor_get_sampling_period`(tag)
value = `wb_distance_sensor_get_value`(tag)


% `Emitter` :
---
WB_CHANNEL_BROADCAST
`wb_emitter_send`(tag, data)
`wb_emitter_set_channel`(tag, channel)
channel = `wb_emitter_get_channel`(tag)
range = `wb_emitter_get_range`(tag)
`wb_emitter_set_range`(tag, range)
size = `wb_emitter_get_buffer_size`(tag)


% `GPS` :
---
`wb_gps_enable`(tag, ms)
`wb_gps_disable`(tag)
period = `wb_gps_get_sampling_period`(tag)
[x y z] = `wb_gps_get_values`(tag)


% `Gyro` :
---
`wb_gyro_enable`(tag, ms)
`wb_gyro_disable`(tag)
period = `wb_gyro_get_sampling_period`(tag)
[x y z] = `wb_gyro_get_values`(tag)


% `InertialUnit` :
---
`wb_inertial_unit_enable`(tag, ms)
`wb_inertial_unit_disable`(tag)
period = `wb_inertial_unit_get_sampling_period`(tag)
[roll pitch yaw] = `wb_inertial_unit_get_roll_pitch_yaw`(tag)


% `LED` :
---
`wb_led_set`(tag, state)
state = `wb_led_get`(tag)


% `LightSensor` :
---
`wb_light_sensor_enable`(tag, ms)
`wb_light_sensor_disable`(tag)
period = `wb_light_sensor_get_sampling_period`(tag)
value = `wb_light_sensor_get_value`(tag)


% `Motion` :
---
motion = `wbu_motion_new`('filename')
`wbu_motion_delete`(motion)
`wbu_motion_play`(motion)
`wbu_motion_stop`(motion)
`wbu_motion_set_loop`(motion, loop)
`wbu_motion_set_reverse`(motion, reverse)
over = `wbu_motion_is_over`(motion)
duration = `wbu_motion_get_duration`(motion)
time = `wbu_motion_get_time`(motion)
`wbu_motion_set_time`(motion, time)


% `Motor` :
---
WB_MOTOR_ROTATIONAL, WB_MOTOR_LINEAR
`wb_motor_set_position`(tag, position)
`wb_motor_set_velocity`(tag, vel)
`wb_motor_set_acceleration`(tag, acc)
`wb_motor_set_available_force`(tag, force)
`wb_motor_set_available_torque`(tag, torque)
`wb_motor_set_control_pid`(tag, p, i, d)
target = `wb_motor_get_target_position`(tag)
min = `wb_motor_get_min_position`(tag)
max = `wb_motor_get_max_position`(tag)
vel = `wb_motor_get_velocity`(tag)
vel = `wb_motor_get_max_velocity`(tag)
acc = `wb_motor_get_acceleration`(tag)
force = `wb_motor_get_available_force`(tag)
force = `wb_motor_get_max_force`(tag)
torque = `wb_motor_get_available_torque`(tag)
torque = `wb_motor_get_max_torque`(tag)
`wb_motor_enable_force_feedback`(tag, ms)
`wb_motor_disable_force_feedback`(tag)
period = `wb_motor_get_force_feedback_sampling_period`(tag)
force = `wb_motor_get_force_feedback`(tag)
`wb_motor_set_force`(tag, force)
`wb_motor_enable_torque_feedback`(tag, ms)
`wb_motor_disable_torque_feedback`(tag)
period = `wb_motor_get_torque_feedback_sampling_period`(tag)
force = `wb_motor_get_torque_feedback`(tag)
`wb_motor_set_torque`(tag, torque)
type = `wb_motor_get_type`(tag)


Node:
---
WB_NODE_NO_NODE, WB_NODE_APPEARANCE, WB_NODE_BACKGROUND,
WB_NODE_BOX, WB_NODE_COLOR, WB_NODE_CONE,
WB_NODE_COORDINATE,  WB_NODE_CYLINDER,
WB_NODE_DIRECTIONAL_LIGHT, WB_NODE_ELEVATION_GRID,
WB_NODE_EXTRUSION, WB_NODE_FOG, WB_NODE_GROUP,
WB_NODE_IMAGE_TEXTURE, WB_NODE_INDEXED_FACE_SET,
WB_NODE_INDEXED_LINE_SET, WB_NODE_MATERIAL,
WB_NODE_POINT_LIGHT,  WB_NODE_SHAPE, WB_NODE_SPHERE,
WB_NODE_SPOT_LIGHT, WB_NODE_SWITCH,
WB_NODE_TEXTURE_COORDINATE, WB_NODE_TEXTURE_TRANSFORM,
WB_NODE_TRANSFORM, WB_NODE_VIEWPOINT, WB_NODE_WORLD_INFO,
WB_NODE_CAPSULE, WB_NODE_PLANE, WB_NODE_ROBOT,
WB_NODE_SUPERVISOR, WB_NODE_DIFFERENTIAL_WHEELS,
WB_NODE_SOLID, WB_NODE_PHYSICS, WB_NODE_CAMERA_ZOOM,
WB_NODE_CHARGER, WB_NODE_DAMPING,
WB_NODE_CONTACT_PROPERTIES, WB_NODE_ACCELEROMETER, WB_NODE_BRAKE,
WB_NODE_CAMERA, WB_NODE_COMPASS, WB_NODE_CONNECTOR,
WB_NODE_DISPLAY, WB_NODE_DISTANCE_SENSOR, WB_NODE_EMITTER,
WB_NODE_GPS, WB_NODE_GYRO, WB_NODE_LED,
WB_NODE_LIGHT_SENSOR, WB_NODE_MICROPHONE, WB_NODE_MOTOR,
WB_NODE_PEN, WB_NODE_POSITION_SENSOR, WB_NODE_RADIO,
WB_NODE_RECEIVER, WB_NODE_SERVO, WB_NODE_SPEAKER,
WB_NODE_TOUCH_SENSOR


% `Pen` :
---
`wb_pen_write`(tag, write)
`wb_pen_set_ink_color`(tag, [r g b], density)


% `PositionSensor` :
---
WB_ANGULAR, WB_LINEAR
`wb_position_sensor_enable`(tag, ms)
`wb_position_sensor_disable`(tag)
period = `wb_position_sensor_get_sampling_period`(tag)
value = `wb_position_sensor_get_value`(tag)
type = `wb_position_sensor_get_type`(tag)


% `Receiver` :
---
WB_CHANNEL_BROADCAST
`wb_receiver_enable`(tag, ms)
`wb_receiver_disable`(tag)
period = `wb_receiver_get_sampling_period`(tag)
length = `wb_receiver_get_queue_length`(tag)
`wb_receiver_next_packet`(tag)
size = `wb_receiver_get_data_size`(tag)
data = `wb_receiver_get_data`(tag)
strength = `wb_receiver_get_signal_strength`(tag)
[x y z] = `wb_receiver_get_emitter_direction`(tag)
`wb_receiver_set_channel`(tag, channel)
channel = `wb_receiver_get_channel`(tag)


% `Robot` :
---
WB_MODE_SIMULATION,
WB_MODE_CROSS_COMPILATION,
WB_MODE_REMOTE_CONTROL
WB_ROBOT_KEYBOARD_END
WB_ROBOT_KEYBOARD_HOME
WB_ROBOT_KEYBOARD_LEFT
WB_ROBOT_KEYBOARD_UP
WB_ROBOT_KEYBOARD_RIGHT
WB_ROBOT_KEYBOARD_DOWN
WB_ROBOT_KEYBOARD_PAGEUP
WB_ROBOT_KEYBOARD_PAGEDOWN
WB_ROBOT_KEYBOARD_NUMPAD_HOME
WB_ROBOT_KEYBOARD_NUMPAD_LEFT
WB_ROBOT_KEYBOARD_NUMPAD_UP
WB_ROBOT_KEYBOARD_NUMPAD_RIGHT
WB_ROBOT_KEYBOARD_NUMPAD_DOWN
WB_ROBOT_KEYBOARD_NUMPAD_END
WB_ROBOT_KEYBOARD_KEY
WB_ROBOT_KEYBOARD_SHIFT
WB_ROBOT_KEYBOARD_CONTROL
WB_ROBOT_KEYBOARD_ALT
`wb_robot_step`(ms)
tag = `wb_robot_get_device`('name')
size = `wb_robot_get_number_of_devices`()
tag = `wb_robot_get_device_by_index`(index)
`wb_robot_battery_sensor_enable`(ms)
`wb_robot_battery_sensor_disable`()
period = `wb_robot_battery_sensor_get_sampling_period`()
value = `wb_robot_battery_sensor_get_value`()
step = `wb_robot_get_basic_time_step`()
mode = `wb_robot_get_mode`()
model = `wb_robot_get_model`()
data = `getData`()
`setData`('data')
name = `wb_robot_get_name`()
name = `wb_robot_get_controller_name`()
name = `wb_robot_get_controller_arguments`()
path = `wb_robot_get_project_path`()
sync = `wb_robot_get_synchronization`()
time = `wb_robot_get_time`()
path = `wb_robot_get_world_path`()
`wb_robot_keyboard_enable`(ms)
`wb_robot_keyboard_disable`()
key = `wb_robot_keyboard_get_key`()
type = `wb_robot_get_type`()


% `Servo` :
---
WB_SERVO_ROTATIONAL, WB_SERVO_LINEAR
`wb_servo_set_position`(tag, position)
target = `wb_servo_get_target_position`(tag)
`wb_servo_set_velocity`(tag, vel)
`wb_servo_set_acceleration`(tag, acc)
`wb_servo_set_motor_force`(tag, force)
`wb_servo_set_control_p`(tag, p)
min = `wb_servo_get_min_position`(tag)
max = `wb_servo_get_max_position`(tag)
`wb_servo_enable_position`(tag, ms)
`wb_servo_disable_position`(tag)
period = `wb_servo_get_position_sampling_period`(tag)
position = `wb_servo_get_position`(tag)
`wb_servo_enable_motor_force_feedback`(tag, ms)
`wb_servo_disable_motor_force_feedback`(tag)
period = `wb_servo_get_motor_force_feedback_sampling_period`(tag)
force = `wb_servo_get_motor_force_feedback`(tag)
`wb_servo_set_force`(tag, force)
type = `wb_servo_get_type`(tag)


% `Supervisor` :
---
WB_SF_BOOL, WB_SF_INT32, WB_SF_FLOAT, WB_SF_VEC2F,
WB_SF_VEC3F, WB_SF_ROTATION, WB_SF_COLOR, WB_SF_STRING,
WB_SF_NODE, WB_MF, WB_MF_INT32, WB_MF_FLOAT, B_MF_VEC2F,
WB_MF_VEC3F, WB_MF_COLOR, WB_MF_STRING, WB_MF_NODE
WB_SUPERVISOR_MOVIE_READY, WB_SUPERVISOR_MOVIE_RECORDING, WB_SUPERVISOR_MOVIE_SAVING, WB_SUPERVISOR_MOVIE_WRITE_ERROR, WB_SUPERVISOR_MOVIE_ENCODING_ERROR, WB_SUPERVISOR_MOVIE_SIMULATION_ERROR
`wb_supervisor_export_image`('filename', quality)
node = `wb_supervisor_node_get_root`()
node = `wb_supervisor_node_get_self`()
node = `wb_supervisor_node_get_from_def`('def')
node = `wb_supervisor_node_get_from_id`('id')
id = `wb_supervisor_node_get_id`(node)
node = `wb_supervisor_node_get_parent_node`(node)
`wb_supervisor_node_remove`(node)
`wb_supervisor_set_label`(id, 'text', x, y, size, [r g b], transparency)
`wb_supervisor_simulation_quit`(status)
`wb_supervisor_simulation_revert`()
`wb_supervisor_simulation_reset_physics`()
`wb_supervisor_load_world`('filename')
`wb_supervisor_save_world`()
`wb_supervisor_save_world`('filename')
`wb_supervisor_movie_start_recording`('filename', width, height, codec, quality,
acceleration, caption)
`wb_supervisor_movie_stop_recording`()
status = `wb_supervisor_movie_get_status`()
success = `wb_supervisor_animation_start_recording`('filename')
success = `wb_supervisor_animation_stop_recording`()
type = `wb_supervisor_field_get_type`(field)
name = `wb_supervisor_field_get_type_name`(field)
count = `wb_supervisor_field_get_count`(field)
b = `wb_supervisor_field_get_sf_bool`(field)
i = `wb_supervisor_field_get_sf_int32`(field)
f = `wb_supervisor_field_get_sf_float`(field)
[x y] = `wb_supervisor_field_get_sf_vec2f`(field)
[x y z] = `wb_supervisor_field_get_sf_vec3f`(field)
[x y z alpha] = `wb_supervisor_field_get_sf_rotation`(field)
[r g b] = `wb_supervisor_field_get_sf_color`(field)
s = `wb_supervisor_field_get_sf_string`(field)
node = `wb_supervisor_field_get_sf_node`(field)
b = `wb_supervisor_field_get_mf_bool`(field, index)
i = `wb_supervisor_field_get_mf_int32`(field, index)
f = `wb_supervisor_field_get_mf_float`(field, index)
[x y] = `wb_supervisor_field_get_mf_vec2f`(field, index)
[x y z] = `wb_supervisor_field_get_mf_vec3f`(field, index)
[x y z a] = `wb_supervisor_field_get_mf_rotation`(field, index)
[r g b] = `wb_supervisor_field_get_mf_color`(field, index)
s = `wb_supervisor_field_get_mf_string`(field, index)
node = `wb_supervisor_field_get_mf_node`(field, index)
`wb_supervisor_field_set_sf_bool`(field, value)
`wb_supervisor_field_set_sf_int32`(field, value)
`wb_supervisor_field_set_sf_float`(field, value)
`wb_supervisor_field_set_sf_vec2f`(field, [x y])
`wb_supervisor_field_set_sf_vec3f`(field, [x y z])
`wb_supervisor_field_set_sf_rotation`(field, [x y z alpha])
`wb_supervisor_field_set_sf_color`(field, [r g b])
`wb_supervisor_field_set_sf_string`(field, 'value')
`wb_supervisor_field_set_mf_bool`(field, index, value)
`wb_supervisor_field_set_mf_int32`(field, index, value)
`wb_supervisor_field_set_mf_float`(field, index, value)
`wb_supervisor_field_set_mf_vec2f`(field, index, [x y])
`wb_supervisor_field_set_mf_vec3f`(field, index, [x y z])
`wb_supervisor_field_set_mf_rotation`(field, index, [x y z a])
`wb_supervisor_field_set_mf_color`(field, index, [r g b])
`wb_supervisor_field_set_mf_string`(field, index, 'value')
`wb_supervisor_field_import_mf_node`(field, position, 'filename')
`wb_supervisor_field_import_mf_node_from_string`(field, position, 'node_string')
`wb_supervisor_field_remove_mf_node`(field, position)
type = `wb_supervisor_node_get_type`(node)
name = `wb_supervisor_node_get_type_name`(node)
name = `wb_supervisor_node_get_base_type_name`(node)
field = `wb_supervisor_node_get_field`(node, 'field_name')
position = `wb_supervisor_node_get_position`(node)
orientation = `wb_supervisor_node_get_orientation`(node)
com = `wb_supervisor_node_get_center_of_mass`(node)
contact_point = `wb_supervisor_node_get_contact_point`(node, index)
number_of_contacts = `wb_supervisor_node_get_number_of_contact_points`(index)
balance = `wb_supervisor_node_get_static_balance`(node)
velocity = `wb_supervisor_node_get_velocity`(node)
`wb_supervisor_node_set_velocity`(node, velocity)
`wb_supervisor_node_reset_physics`(node)


% `TouchSensor` :
---
WB_TOUCH_SENSOR_BUMPER, WB_TOUCH_SENSOR_FORCE,
WB_TOUCH_SENSOR_FORCE3D
`wb_touch_sensor_enable`(tag, ms)
`wb_touch_sensor_disable`(tag)
period = `wb_touch_sensor_get_sampling_period`(tag)
value = `wb_touch_sensor_get_value`(tag)
[x y z] = `wb_touch_sensor_get_values`(tag)
type = `wb_touch_sensor_get_type`(tag)


