## Matlab API

The following tables describe the Matlab functions.

%api "matlab_accelerometer"

| % [Accelerometer](accelerometer.md) :                                                                  |
| ------------------------------------------------------------------------------------------------------ |
| [wb\_accelerometer\_enable](accelerometer.md#wb_accelerometer_get_values)(tag, sampling_period)        |
| [wb\_accelerometer\_disable](accelerometer.md#wb_accelerometer_get_values)(tag)                        |
| period = [wb\_accelerometer\_get\_sampling\_period](accelerometer.md#wb_accelerometer_get_values)(tag) |
| [x y z] = [wb\_accelerometer\_get\_values](accelerometer.md#wb_accelerometer_get_values)(tag)          |

%end

%api "matlab_brake"

| % [Brake](brake.md) :                                                                             |
| ------------------------------------------------------------------------------------------------- |
| [wb\_brake\_set\_damping\_constant](brake.md#wb_brake_set_damping_constant)(tag, dampingConstant) |
| type = [wb\_brake\_get\_type](brake.md#wb_brake_set_damping_constant)(tag)                        |

%end

%api "matlab_camera"

| % [Camera](camera.md) :                                                                        |
| ---------------------------------------------------------------------------------------------- |
| [wb\_camera\_enable](camera.md#wb_camera_enable)(tag, sampling_period)                         |
| [wb\_camera\_disable](camera.md#wb_camera_enable)(tag)                                         |
| period = [wb\_camera\_get\_sampling\_period](camera.md#wb_camera_enable)(tag)                  |
| fov = [wb\_camera\_get\_fov](camera.md#wb_camera_get_fov)(tag)                                 |
| fov = [wb\_camera\_get\_min\_fov](camera.md#wb_camera_get_fov)(tag)                            |
| fov = [wb\_camera\_get\_max\_fov](camera.md#wb_camera_get_fov)(tag)                            |
| [wb\_camera\_set\_fov](camera.md#wb_camera_get_fov)(tag, fov)                                  |
| fov = [wb\_camera\_get\_focal\_length](camera.md#wb_camera_get_focal_length)(tag)              |
| fov = [wb\_camera\_get\_focal\_distance](camera.md#wb_camera_get_focal_length)(tag)            |
| fov = [wb\_camera\_get\_max\_focal\_distance](camera.md#wb_camera_get_focal_length)(tag)       |
| fov = [wb\_camera\_get\_min\_focal\_distance](camera.md#wb_camera_get_focal_length)(tag)       |
| [wb\_camera\_set\_focal\_distance](camera.md#wb_camera_get_focal_length)(tag, focal\_distance) |
| width = [wb\_camera\_get\_width](camera.md#wb_camera_get_width)(tag)                           |
| height = [wb\_camera\_get\_height](camera.md#wb_camera_get_width)(tag)                         |
| near = [wb\_camera\_get\_near](camera.md#wb_camera_get_near)(tag)                              |
| image = [wb\_camera\_get\_image](camera.md#wb_camera_get_image)(tag)                           |
| [wb\_camera\_save\_image](camera.md#wb_camera_save_image)(tag, 'filename', quality)            |
| [wb\_camera\_has\_recognition](camera.md#wb_camera_has_recognition)(tag)                       |
| [wb\_camera\_recognition\_disable](camera.md#wb_camera_has_recognition)(tag)                   |
| [wb\_camera\_recognition\_enable](camera.md#wb_camera_has_recognition)(tag, sampling_period)   |
| [wb\_camera\_recognition\_get\_number\_of\_objects](camera.md#wb_camera_has_recognition)(tag)  |
| [wb\_camera\_recognition\_get\_objects](camera.md#wb_camera_has_recognition)(tag)              |
| [wb\_camera\_recognition\_get\_sampling\_period](camera.md#wb_camera_has_recognition)(tag)     |

%end

%api "matlab_compass"

| % [Compass](compass.md) :                                                            |
| ------------------------------------------------------------------------------------ |
| [wb\_compass\_enable](compass.md#wb_compass_get_values)(tag, sampling_period)        |
| [wb\_compass\_disable](compass.md#wb_compass_get_values)(tag)                        |
| period = [wb\_compass\_get\_sampling\_period](compass.md#wb_compass_get_values)(tag) |
| [x y z] = [wb\_compass\_get\_values](compass.md#wb_compass_get_values)(tag)          |

%end

%api "matlab_connector"

| % [Connector](connector.md) :                                                                          |
| ------------------------------------------------------------------------------------------------------ |
| [wb\_connector\_enable\_presence](connector.md#wb_connector_get_presence)(tag, sampling_period)        |
| [wb\_connector\_disable\_presence](connector.md#wb_connector_get_presence)(tag)                        |
| period = [wb\_connector\_get\_presence\_sampling\_period](connector.md#wb_connector_get_presence)(tag) |
| presence = [wb\_connector\_get\_presence](connector.md#wb_connector_get_presence)(tag)                 |
| [wb\_connector\_lock](connector.md#wb_connector_lock)(tag)                                             |
| [wb\_connector\_unlock](connector.md#wb_connector_lock)(tag)                                           |

%end

%api "matlab_device"

| % [Device](device.md) :                                                      |
| ---------------------------------------------------------------------------- |
| model = [wb\_device\_get\_model](device.md#wb_device_get_model)(tag)         |
| name = [wb\_device\_get\_name](device.md#wb_device_get_name)(tag)            |
| type = [wb\_device\_get\_node\_type](device.md#wb_device_get_node_type)(tag) |

%end

%api "matlab_differential_wheels"

| % [DifferentialWheels](differentialwheels.md) :                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| [wb\_differential\_wheels\_set\_speed](differentialwheels.md#wb_differential_wheels_set_speed)(left, right)                          |
| left = [wb\_differential\_wheels\_get\_left\_speed](differentialwheels.md#wb_differential_wheels_set_speed)()                        |
| right = [wb\_differential\_wheels\_get\_right\_speed](differentialwheels.md#wb_differential_wheels_set_speed)()                      |
| [wb\_differential\_wheels\_enable\_encoders](differentialwheels.md#wb_differential_wheels_enable_encoders)(sampling_period)          |
| [wb\_differential\_wheels\_disable\_encoders](differentialwheels.md#wb_differential_wheels_enable_encoders)()                        |
| period = [wb\_differential\_wheels\_get\_encoders\_sampling\_period](differentialwheels.md#wb_differential_wheels_enable_encoders)() |
| left = [wb\_differential\_wheels\_get\_left\_encoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)()               |
| right = [wb\_differential\_wheels\_get\_right\_encoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)()             |
| [wb\_differential\_wheels\_set\_encoders](differentialwheels.md#wb_differential_wheels_get_left_encoder)(left, right)                |
| max = [wb\_differential\_wheels\_get\_max\_speed](differentialwheels.md#wb_differential_wheels_get_max_speed)()                      |
| unit = [wb\_differential\_wheels\_get\_speed\_unit](differentialwheels.md#wb_differential_wheels_get_speed_unit)()                   |

%end

%api "matlab_display"

| % [Display](display.md) :                                                                            |
| ---------------------------------------------------------------------------------------------------- |
| RGB                                                                                                  |
| RGBA                                                                                                 |
| ARGB                                                                                                 |
| BGRA                                                                                                 |
| width = [wb\_display\_get\_width](display.md#wb_display_get_width)(tag)                              |
| height = [wb\_display\_get\_height](display.md#wb_display_get_width)(tag)                            |
| [wb\_display\_set\_color](display.md#wb_display_set_color)(tag, [r g b])                             |
| [wb\_display\_set\_alpha](display.md#wb_display_set_color)(tag, alpha)                               |
| [wb\_display\_set\_opacity](display.md#wb_display_set_color)(tag, opacity)                           |
| [wb\_display\_set\_font](display.md#wb_display_set_color)(tag, font, size, anti_aliasing)            |
| [wb\_display\_attach\_camera](display.md#wb_display_attach_camera)(tag, camera_tag)                  |
| [wb\_display\_detach\_camera](display.md#wb_display_attach_camera)(tag)                              |
| [wb\_display\_draw\_pixel](display.md#wb_display_draw_pixel)(tag, x, y)                              |
| [wb\_display\_draw\_line](display.md#wb_display_draw_pixel)(tag, x1, y1, x2, y2)                     |
| [wb\_display\_draw\_rectangle](display.md#wb_display_draw_pixel)(tag, x, y, width, height)           |
| [wb\_display\_draw\_oval](display.md#wb_display_draw_pixel)(tag, cx, cy, a, b)                       |
| [wb\_display\_draw\_polygon](display.md#wb_display_draw_pixel)(tag, [x1 x2 ... xn], [y1 y2 ... yn])  |
| [wb\_display\_draw\_text](display.md#wb_display_draw_pixel)(tag, 'txt', x, y)                        |
| [wb\_display\_fill\_rectangle](display.md#wb_display_draw_pixel)(tag, x, y, width, height)           |
| [wb\_display\_fill\_oval](display.md#wb_display_draw_pixel)(tag, cx, cy, a, b)                       |
| [wb\_display\_fill\_polygon](display.md#wb_display_draw_pixel)(tag, [x1 x2 ... xn], [y1 y2 ... yn])  |
| image = [wb\_display\_image\_copy](display.md#wb_display_image_new)(tag, x, y, width, height)        |
| [wb\_display\_image\_paste](display.md#wb_display_image_new)(tag, image, x, y, blend)                |
| image = [wb\_display\_image\_load](display.md#wb_display_image_new)(tag, 'filename')                 |
| image = [wb\_display\_image\_new](display.md#wb_display_image_new)(tag, width, height, data ,format) |
| [wb\_display\_image\_save](display.md#wb_display_image_new)(tag, image, 'filename')                  |
| [wb\_display\_image\_delete](display.md#wb_display_image_new)(tag, image)                            |

%end

%api "matlab_distance_sensor"

| % [DistanceSensor](distancesensor.md) :                                                                       |
| ------------------------------------------------------------------------------------------------------------- |
| WB\_DISTANCE\_SENSOR\_GENERIC, WB\_DISTANCE\_SENSOR\_INFRA\_RED,                                              |
| WB\_DISTANCE\_SENSOR\_SONAR, WB\_DISTANCE\_SENSOR\_LASER                                                      |
| [wb\_distance\_sensor\_enable](distancesensor.md#wb_distance_sensor_get_value)(tag, sampling_period)          |
| [wb\_distance\_sensor\_disable](distancesensor.md#wb_distance_sensor_get_value)(tag)                          |
| period = [wb\_distance\_sensor\_get\_sampling\_period](distancesensor.md#wb_distance_sensor_get_value)(tag)   |
| value = [wb\_distance\_sensor\_get\_value](distancesensor.md#wb_distance_sensor_get_value)(tag)               |
| max\_range = [wb\_distance\_sensor\_get\_max\_range](distancesensor.md#wb_distance_sensor_get_max_range)(tag) |
| min\_range = [wb\_distance\_sensor\_get\_min\_range](distancesensor.md#wb_distance_sensor_get_max_range)(tag) |
| aperture = [wb\_distance\_sensor\_get\_aperture](distancesensor.md#wb_distance_sensor_get_max_range)(tag)     |
| type = [wb\_distance\_sensor\_get\_type](distancesensor.md#wb_distance_sensor_get_value)(tag)                 |

%end

%api "matlab_emitter"

| % [Emitter](emitter.md) :                                                           |
| ----------------------------------------------------------------------------------- |
| WB\_CHANNEL\_BROADCAST                                                              |
| [wb\_emitter\_send](emitter.md#wb_emitter_send)(tag, data)                          |
| [wb\_emitter\_set\_channel](emitter.md#wb_emitter_set_channel)(tag, channel)        |
| channel = [wb\_emitter\_get\_channel](emitter.md#wb_emitter_set_channel)(tag)       |
| range = [wb\_emitter\_get\_range](emitter.md#wb_emitter_set_range)(tag)             |
| [wb\_emitter\_set\_range](emitter.md#wb_emitter_set_range)(tag, range)              |
| size = [wb\_emitter\_get\_buffer\_size](emitter.md#wb_emitter_get_buffer_size)(tag) |

%end

%api "matlab_gps"

| % [GPS](gps.md) :                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------- |
| WB\_GPS\_LOCAL\_COORDINATE, WB\_GPS\_WGS84\_COORDINATE,                                                                                 |
| [wb\_gps\_enable](gps.md#wb_gps_get_values)(tag, sampling_period)                                                                       |
| [wb\_gps\_disable](gps.md#wb_gps_get_values)(tag)                                                                                       |
| period = [wb\_gps\_get\_sampling\_period](gps.md#wb_gps_get_values)(tag)                                                                |
| [x y z] = [wb\_gps\_get\_values](gps.md#wb_gps_get_values)(tag)                                                                         |
| speed = [wb\_gps\_get\_speed](gps.md#wb_gps_get_values)(tag)                                                                            |
| coordinate\_system = [wb\_gps\_get\_coordinate\_system](gps.md#wb_gps_get_coordinate_system)(tag)                                       |
| coordinate = [wb\_gps\_convert\_to\_degrees\_minutes\_seconds](gps.md#wb_gps_convert_to_degrees_minutes_seconds)(tag, decimal\_degrees) |

%end

%api "matlab_gyro"

| % [Gyro](gyro.md) :                                                         |
| --------------------------------------------------------------------------- |
| [wb\_gyro\_enable](gyro.md#wb_gyro_get_values)(tag, sampling_period)        |
| [wb\_gyro\_disable](gyro.md#wb_gyro_get_values)(tag)                        |
| period = [wb\_gyro\_get\_sampling\_period](gyro.md#wb_gyro_get_values)(tag) |
| [x y z] = [wb\_gyro\_get\_values](gyro.md#wb_gyro_get_values)(tag)          |

%end

%api "matlab_inertial_unit"

| % [InertialUnit](inertialunit.md) :                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------ |
| [wb\_inertial\_unit\_enable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag, sampling_period)                  |
| [wb\_inertial\_unit\_disable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag)                                  |
| period = [wb\_inertial\_unit\_get\_sampling\_period](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag)           |
| [roll pitch yaw] = [wb\_inertial\_unit\_get\_roll\_pitch\_yaw](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag) |

%end

%api "matlab_joystick"

| % [Joystick](joystick.md) :                                                                     |
| ----------------------------------------------------------------------------------------------- |
| [wb\_joystick\_enable](joystick.md#wb_joystick_enable)(sampling_period)                         |
| [wb\_joystick\_disable](joystick.md#wb_joystick_enable)()                                       |
| period = [wb\_joystick\_get\_sampling\_period](joystick.md#wb_joystick_enable)()                |
| connected = [wb_joystick_is_connected](joystick.md#wb_joystick_is_connected)()                  |
| axes_number = [wb_joystick_get_number_of_axes](joystick.md#wb_joystick_get_number_of_axes)()    |
| axis_value = [wb_joystick_get_axis_value](joystick.md#wb_joystick_get_number_of_axes)(axis)     |
| button = [wb_joystick_get_pressed_button](joystick.md#wb_joystick_get_pressed_button)()         |
| [wb_joystick_set_constant_force](joystick.md#wb_joystick_set_constant_force)(level)             |
| [wb_joystick_set_constant_force_duration](joystick.md#wb_joystick_set_constant_force)(duration) |
| [wb_joystick_set_auto_centering_gain](joystick.md#wb_joystick_set_constant_force)(gain)         |
| [wb_joystick_set_resistance_gain](joystick.md#wb_joystick_set_constant_force)(gain)             |

%end

%api "matlab_keyboard"

| % [Keyboard](keyboard.md) :                                                      |
| -------------------------------------------------------------------------------- |
| WB\_KEYBOARD\_END                                                                |
| WB\_KEYBOARD\_HOME                                                               |
| WB\_KEYBOARD\_LEFT                                                               |
| WB\_KEYBOARD\_UP                                                                 |
| WB\_KEYBOARD\_RIGHT                                                              |
| WB\_KEYBOARD\_DOWN                                                               |
| WB\_KEYBOARD\_PAGEUP                                                             |
| WB\_KEYBOARD\_PAGEDOWN                                                           |
| WB\_KEYBOARD\_NUMPAD\_HOME                                                       |
| WB\_KEYBOARD\_NUMPAD\_LEFT                                                       |
| WB\_KEYBOARD\_NUMPAD\_UP                                                         |
| WB\_KEYBOARD\_NUMPAD\_RIGHT                                                      |
| WB\_KEYBOARD\_NUMPAD\_DOWN                                                       |
| WB\_KEYBOARD\_NUMPAD\_END                                                        |
| WB\_KEYBOARD\_KEY                                                                |
| WB\_KEYBOARD\_SHIFT                                                              |
| WB\_KEYBOARD\_CONTROL                                                            |
| WB\_KEYBOARD\_ALT                                                                |
| [wb\_keyboard\_enable](keyboard.md#wb_keyboard_enable)(sampling_period)          |
| [wb\_keyboard\_disable](keyboard.md#wb_keyboard_enable)()                        |
| period = [wb\_keyboard\_get\_sampling\_period](keyboard.md#wb_keyboard_enable)() |
| key = [wb\_keyboard\_get\_key](keyboard.md#wb_keyboard_enable)()                 |

%end

%api "matlab_led"

| % [LED](led.md) :                              |
| ---------------------------------------------- |
| [wb\_led\_set](led.md#wb_led_set)(tag, state)  |
| state = [wb\_led\_get](led.md#wb_led_set)(tag) |

%end

%api "matlab_lidar"

| % [Lidar](lidar.md) :                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------- |
| &nbsp;&nbsp; [wb\_lidar\_enable](lidar.md#wb_lidar_enable)(tag, sampling_period);                                                 |
| &nbsp;&nbsp; [wb\_lidar\_enable\_point\_cloud](lidar.md#wb_lidar_enable_point_cloud)(tag);                                        |
| &nbsp;&nbsp; [wb\_lidar\_disable](lidar.md#wb_lidar_enable)(tag);                                                                 |
| &nbsp;&nbsp; [wb\_lidar\_disable\_point\_cloud](lidar.md#wb_lidar_enable_point_cloud)(tag);                                       |
| &nbsp;&nbsp; period = [wb\_lidar\_get\_sampling\_period](lidar.md#wb_lidar_enable)(tag);                                          |
| &nbsp;&nbsp; state = [wb\_lidar\_is\_point\_cloud\_enabled](lidar.md#wb_lidar_enable)(tag);                                       |
| &nbsp;&nbsp; range = [wb\_lidar\_get\_range\_image](lidar.md#wb_lidar_get_range_image)(tag);                                      |
| &nbsp;&nbsp; range = [wb\_lidar\_get\_layer\_range\_image](lidar.md#wb_lidar_get_range_image)(tag, layer);                        |
| &nbsp;&nbsp; points = [wb\_lidar\_get\_point\_cloud](lidar.md#wb_lidar_get_point_cloud)(tag);                                     |
| &nbsp;&nbsp; points = [wb\_lidar\_get\_layer\_point\_cloud](lidar.md#wb_lidar_get_point_cloud)(tag, layer);                       |
| &nbsp;&nbsp; number\_of\_points = [wb\_lidar\_get\_number\_of\_points](lidar.md#wb_lidar_get_point_cloud)(tag);                   |
| &nbsp;&nbsp; frequency = [wb\_lidar\_get\_frequency](lidar.md#wb_lidar_get_frequency)(tag);                                       |
| &nbsp;&nbsp; [wb\_lidar\_set\_frequency](lidar.md#wb_lidar_get_frequency)(tag, frequency);                                        |
| &nbsp;&nbsp; horizontal\_resolution = [wb\_lidar\_get\_horizontal\_resolution](lidar.md#wb_lidar_get_horizontal_resolution)(tag); |
| &nbsp;&nbsp; number\_of\_layers = [wb\_lidar\_get\_number\_of\_layers](lidar.md#wb_lidar_get_horizontal_resolution)(tag);         |
| &nbsp;&nbsp; min\_frequency = [wb\_lidar\_get\_min\_frequency](lidar.md#wb_lidar_get_min_frequency)(tag);                         |
| &nbsp;&nbsp; max\_frequency = [wb\_lidar\_get\_max\_frequency](lidar.md#wb_lidar_get_min_frequency)(tag);                         |
| &nbsp;&nbsp; fov = [wb\_lidar\_get\_fov](lidar.md#wb_lidar_get_fov)(tag);                                                         |
| &nbsp;&nbsp; vertical\_fov = [wb\_lidar\_get\_vertical\_fov](lidar.md#wb_lidar_get_fov)(tag);                                     |
| &nbsp;&nbsp; min\_range = [wb\_lidar\_get\_min\_range](lidar.md#wb_lidar_get_min_range)(tag);                                     |
| &nbsp;&nbsp; max\_range = [wb\_lidar\_get\_max\_range](lidar.md#wb_lidar_get_min_range)(tag);                                     |

%end

%api "matlab_light_sensor"

| % [LightSensor](lightsensor.md) :                                                                  |
| -------------------------------------------------------------------------------------------------- |
| [wb\_light\_sensor\_enable](lightsensor.md#wb_light_sensor_get_value)(tag, sampling_period)        |
| [wb\_light\_sensor\_disable](lightsensor.md#wb_light_sensor_get_value)(tag)                        |
| period = [wb\_light\_sensor\_get\_sampling\_period](lightsensor.md#wb_light_sensor_get_value)(tag) |
| value = [wb\_light\_sensor\_get\_value](lightsensor.md#wb_light_sensor_get_value)(tag)             |

%end

%api "matlab_motion"

| % [Motion](motion.md) :                                                       |
| ----------------------------------------------------------------------------- |
| motion = [wbu\_motion\_new](motion.md#wbu_motion_new)('filename')             |
| [wbu\_motion\_delete](motion.md#wbu_motion_new)(motion)                       |
| [wbu\_motion\_play](motion.md#wbu_motion_play)(motion)                        |
| [wbu\_motion\_stop](motion.md#wbu_motion_play)(motion)                        |
| [wbu\_motion\_set\_loop](motion.md#wbu_motion_play)(motion, loop)             |
| [wbu\_motion\_set\_reverse](motion.md#wbu_motion_play)(motion, reverse)       |
| over = [wbu\_motion\_is\_over](motion.md#wbu_motion_is_over)(motion)          |
| duration = [wbu\_motion\_get\_duration](motion.md#wbu_motion_is_over)(motion) |
| time = [wbu\_motion\_get\_time](motion.md#wbu_motion_is_over)(motion)         |
| [wbu\_motion\_set\_time](motion.md#wbu_motion_is_over)(motion, time)          |

%end

%api "matlab_motor"

| % [Motor](motor.md) :                                                                                       |
| ----------------------------------------------------------------------------------------------------------- |
| WB\_MOTOR\_ROTATIONAL, WB\_MOTOR\_LINEAR                                                                    |
| [wb\_motor\_set\_position](motor.md#wb_motor_set_position)(tag, position)                                   |
| [wb\_motor\_set\_velocity](motor.md#wb_motor_set_position)(tag, vel)                                        |
| [wb\_motor\_set\_acceleration](motor.md#wb_motor_set_position)(tag, acc)                                    |
| [wb\_motor\_set\_available\_force](motor.md#wb_motor_set_position)(tag, force)                              |
| [wb\_motor\_set\_available\_torque](motor.md#wb_motor_set_position)(tag, torque)                            |
| [wb\_motor\_set\_control\_pid](motor.md#wb_motor_set_position)(tag, p, i, d)                                |
| target = [wb\_motor\_get\_target\_position](motor.md#wb_motor_set_position)(tag)                            |
| min = [wb\_motor\_get\_min\_position](motor.md#wb_motor_set_position)(tag)                                  |
| max = [wb\_motor\_get\_max\_position](motor.md#wb_motor_set_position)(tag)                                  |
| vel = [wb\_motor\_get\_velocity](motor.md#wb_motor_set_position)(tag)                                       |
| vel = [wb\_motor\_get\_max\_velocity](motor.md#wb_motor_set_position)(tag)                                  |
| acc = [wb\_motor\_get\_acceleration](motor.md#wb_motor_set_position)(tag)                                   |
| force = [wb\_motor\_get\_available\_force](motor.md#wb_motor_set_position)(tag)                             |
| force = [wb\_motor\_get\_max\_force](motor.md#wb_motor_set_position)(tag)                                   |
| torque = [wb\_motor\_get\_available\_torque](motor.md#wb_motor_set_position)(tag)                           |
| torque = [wb\_motor\_get\_max\_torque](motor.md#wb_motor_set_position)(tag)                                 |
| [wb\_motor\_enable\_force\_feedback](motor.md#wb_motor_enable_force_feedback)(tag, sampling_period)         |
| [wb\_motor\_disable\_force\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                         |
| period = [wb\_motor\_get\_force\_feedback\_sampling\_period](motor.md#wb_motor_enable_force_feedback)(tag)  |
| force = [wb\_motor\_get\_force\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                     |
| [wb\_motor\_set\_force](motor.md#wb_motor_set_force)(tag, force)                                            |
| [wb\_motor\_enable\_torque\_feedback](motor.md#wb_motor_enable_force_feedback)(tag, sampling_period)        |
| [wb\_motor\_disable\_torque\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                        |
| period = [wb\_motor\_get\_torque\_feedback\_sampling\_period](motor.md#wb_motor_enable_force_feedback)(tag) |
| force = [wb\_motor\_get\_torque\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                    |
| [wb\_motor\_set\_torque](motor.md#wb_motor_set_force)(tag, torque)                                          |
| type = [wb\_motor\_get\_type](motor.md#wb_motor_get_type)(tag)                                              |

%end

%api "matlab_mouse"

| % [Mouse](mouse.md) :                                                   |
| ----------------------------------------------------------------------- |
| [wb\_mouse\_enable](mouse.md#wb_mouse_enable)(sampling_period)          |
| [wb\_mouse\_disable](mouse.md#wb_mouse_enable)()                        |
| period = [wb\_mouse\_get\_sampling\_period](mouse.md#wb_mouse_enable)() |
| state = [wb_mouse_get_state](mouse.md#wb_mouse_enable)()                |

%end

%api "matlab_node"

| Node:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| WB\_NODE\_NO\_NODE, WB\_NODE\_ACCELEROMETER, WB\_NODE\_APPEARANCE, WB\_NODE\_BACKGROUND, WB\_NODE\_BALL\_JOINT, WB\_NODE\_BALL\_JOINT\_PARAMETERS, WB\_NODE\_BOX, WB\_NODE\_BRAKE, WB\_NODE\_CAMERA, WB\_NODE\_CAPSULE, WB\_NODE\_CHARGER, WB\_NODE\_COLOR, WB\_NODE\_COMPASS, WB\_NODE\_CONE, WB\_NODE\_CONNECTOR, WB\_NODE\_CONTACT\_PROPERTIES, WB\_NODE\_COORDINATE, WB\_NODE\_CYLINDER, WB\_NODE\_DAMPING, WB\_NODE\_DIFFERENTIAL\_WHEELS, WB\_NODE\_DIRECTIONAL\_LIGHT, WB\_NODE\_DISPLAY, WB\_NODE\_DISTANCE\_SENSOR, WB\_NODE\_ELEVATION\_GRID, WB\_NODE\_EMITTER, WB\_NODE\_EXTRUSION, WB\_NODE\_FLUID, WB\_NODE\_FOCUS, WB\_NODE\_FOG, WB\_NODE\_GPS, WB\_NODE\_GROUP, WB\_NODE\_GYRO, WB\_NODE\_HINGE\_2\_JOINT, WB\_NODE\_HINGE\_2\_JOINT\_PARAMETERS, WB\_NODE\_HINGE\_JOINT, WB\_NODE\_HINGE\_JOINT\_PARAMETERS, WB\_NODE\_IMAGE\_TEXTURE, WB\_NODE\_IMMERSION\_PROPERTIES, WB\_NODE\_INDEXED\_FACE\_SET, WB\_NODE\_INDEXED\_LINE\_SET, WB\_NODE\_INERTIAL\_UNIT, WB\_NODE\_JOINT\_PARAMETERS, WB\_NODE\_LED, WB\_NODE\_LIDAR, WB\_NODE\_LIGHT\_SENSOR, WB\_NODE\_LINEAR\_MOTOR, WB\_NODE\_LENS\_DISTORTION, WB\_NODE\_MATERIAL, WB\_NODE\_MICROPHONE, WB\_NODE\_PEN, WB\_NODE\_PHYSICS, WB\_NODE\_PLANE, WB\_NODE\_POINT\_LIGHT, WB\_NODE\_POSITION\_SENSOR, WB\_NODE\_PROPELLER, WB\_NODE\_RADAR, WB\_NODE\_RADIO, WB\_NODE\_RANGE\_FINDER, WB\_NODE\_RECEIVER, WB\_NODE\_RECOGNITION, WB\_NODE\_ROBOT, WB\_NODE\_ROTATIONAL\_MOTOR, WB\_NODE\_SERVO, WB\_NODE\_SHAPE, WB\_NODE\_SLIDER\_JOINT, WB\_NODE\_SLOT, WB\_NODE\_SOLID, WB\_NODE\_SOLID\_REFERENCE, WB\_NODE\_SPEAKER, WB\_NODE\_SPHERE, WB\_NODE\_SPOT\_LIGHT, WB\_NODE\_SUPERVISOR, WB\_NODE\_SWITCH, WB\_NODE\_TEXTURE\_COORDINATE, WB\_NODE\_TEXTURE\_TRANSFORM, WB\_NODE\_TOUCH\_SENSOR, WB\_NODE\_TRACK, WB\_NODE\_TRACK\_WHEEL, WB\_NODE\_TRANSFORM, WB\_NODE\_VIEWPOINT, WB\_NODE\_WORLD\_INFO, WB\_NODE\_ZOOM |

%end

%api "matlab_pen"

| % [Pen](pen.md) :                                                              |
| ------------------------------------------------------------------------------ |
| [wb\_pen\_write](pen.md#wb_pen_write)(tag, write)                              |
| [wb\_pen\_set\_ink\_color](pen.md#wb_pen_set_ink_color)(tag, [r g b], density) |

%end

%api "matlab_position_sensor"

| % [PositionSensor](positionsensor.md) :                                                                     |
| ----------------------------------------------------------------------------------------------------------- |
| WB\_ANGULAR, WB\_LINEAR                                                                                     |
| [wb\_position\_sensor\_enable](positionsensor.md#wb_position_sensor_get_value)(tag, sampling_period)        |
| [wb\_position\_sensor\_disable](positionsensor.md#wb_position_sensor_get_value)(tag)                        |
| period = [wb\_position\_sensor\_get\_sampling\_period](positionsensor.md#wb_position_sensor_get_value)(tag) |
| value = [wb\_position\_sensor\_get\_value](positionsensor.md#wb_position_sensor_get_value)(tag)             |
| type = [wb\_position\_sensor\_get\_type](positionsensor.md#wb_position_sensor_get_value)(tag)               |

%end

%api "matlab_radar"

| % [Radar](radar.md) :                                                                                 |
| ----------------------------------------------------------------------------------------------------- |
| [wb\_radar\_enable](radar.md#wb_radar_enable)(tag, sampling_period)                                   |
| [wb\_radar\_disable](radar.md#wb_radar_enable)(tag)                                                   |
| period = [wb\_radar\_get\_sampling\_period](radar.md#wb_radar_enable)(tag)                            |
| targets\_number = [wb\_radar\_get\_number\_of\_targets](radar.md#wb_radar_get_number_of_targets)(tag) |
| targets = [wb\_radar\_get\_targets](radar.md#wb_radar_get_targets)(tag)                               |
| min\_range = [wb\_radar\_get\_min\_range](radar.md#wb_radar_get_min_range)(tag)                       |
| max\_range = [wb\_radar\_get\_max\_range](radar.md#wb_radar_get_min_range)(tag)                       |
| horizontal\_fov = [wb\_radar\_get\_horizontal\_fov](radar.md#wb_radar_get_horizontal_fov)(tag)        |
| vertical\_fov = [wb\_radar\_get\_vertical\_fov](radar.md#wb_radar_get_horizontal_fov)(tag)            |

%end

%api "matlab_range_finder"

| % [RangeFinder](rangefinder.md) :                                                                                  |
| ------------------------------------------------------------------------------------------------------------------ |
| [wb\_range\_finder\_enable](rangefinder.md#wb_range_finder_enable)(tag, sampling_period)                           |
| [wb\_range\_finder\_disable](rangefinder.md#wb_range_finder_enable)(tag)                                           |
| period = [wb\_range\_finder\_get\_sampling\_period](rangefinder.md#wb_range_finder_enable)(tag)                    |
| fov = [wb\_range\_finder\_get\_fov](rangefinder.md#wb_range_finder_get_fov)(tag)                                   |
| width = [wb\_range\_finder\_get\_width](rangefinder.md#wb_range_finder_get_width)(tag)                             |
| height = [wb\_range\_finder\_get\_height](rangefinder.md#wb_range_finder_get_width)(tag)                           |
| near = [wb\_range\_finder\_get\_min\_range](rangefinder.md#wb_range_finder_get_min_range)(tag)                     |
| max\_range = [wb\_range\_finder\_get\_max\_range](rangefinder.md#wb_range_finder_get_min_range)(tag)               |
| image = [wb\_range\_finder\_get\_range\_image](rangefinder.md#wb_range_finder_get_range_image)(tag)                |
| depth = [wb\_range\_finder\_image\_get\_depth](rangefinder.md#wb_range_finder_get_range_image)(image, width, x, y) |
| [wb\_range\_finder\_save\_image](rangefinder.md#wb_range_finder_save_image)(tag, 'filename', quality)              |

%end

%api "matlab_receiver"

| % [Receiver](receiver.md) :                                                                         |
| --------------------------------------------------------------------------------------------------- |
| WB\_CHANNEL\_BROADCAST                                                                              |
| [wb\_receiver\_enable](receiver.md#wb_receiver_enable)(tag, sampling_period)                        |
| [wb\_receiver\_disable](receiver.md#wb_receiver_enable)(tag)                                        |
| period = [wb\_receiver\_get\_sampling\_period](receiver.md#wb_receiver_enable)(tag)                 |
| length = [wb\_receiver\_get\_queue\_length](receiver.md#wb_receiver_get_queue_length)(tag)          |
| [wb\_receiver\_next\_packet](receiver.md#wb_receiver_get_queue_length)(tag)                         |
| size = [wb\_receiver\_get\_data\_size](receiver.md#wb_receiver_get_data)(tag)                       |
| data = [wb\_receiver\_get\_data](receiver.md#wb_receiver_get_data)(tag)                             |
| strength = [wb\_receiver\_get\_signal\_strength](receiver.md#wb_receiver_get_signal_strength)(tag)  |
| [x y z] = [wb\_receiver\_get\_emitter\_direction](receiver.md#wb_receiver_get_signal_strength)(tag) |
| [wb\_receiver\_set\_channel](receiver.md#wb_receiver_set_channel)(tag, channel)                     |
| channel = [wb\_receiver\_get\_channel](receiver.md#wb_receiver_set_channel)(tag)                    |

%end

%api "matlab_robot"

| % [Robot](robot.md) :                                                                                   |
| ------------------------------------------------------------------------------------------------------- |
| WB\_MODE\_SIMULATION,                                                                                   |
| WB\_MODE\_CROSS\_COMPILATION,                                                                           |
| WB\_MODE\_REMOTE\_CONTROL                                                                               |
| [wb\_robot\_step](robot.md#wb_robot_step)(sampling_period)                                              |
| tag = [wb\_robot\_get\_device](robot.md#wb_robot_get_device)('name')                                    |
| size = [wb\_robot\_get\_number\_of\_devices](robot.md#wb_robot_get_device_by_index)()                   |
| tag = [wb\_robot\_get\_device\_by\_index](robot.md#wb_robot_get_device_by_index)(index)                 |
| [wb\_robot\_battery\_sensor\_enable](robot.md#wb_robot_battery_sensor_enable)(sampling_period)          |
| [wb\_robot\_battery\_sensor\_disable](robot.md#wb_robot_battery_sensor_enable)()                        |
| period = [wb\_robot\_battery\_sensor\_get\_sampling\_period](robot.md#wb_robot_battery_sensor_enable)() |
| value = [wb\_robot\_battery\_sensor\_get\_value](robot.md#wb_robot_battery_sensor_enable)()             |
| step = [wb\_robot\_get\_basic\_time\_step](robot.md#wb_robot_get_basic_time_step)()                     |
| mode = [wb\_robot\_get\_mode](robot.md#wb_robot_get_mode)()                                             |
| model = [wb\_robot\_get\_model](robot.md#wb_robot_get_model)()                                          |
| data = [getData](robot.md#wb_robot_get_data)()                                                          |
| [setData](robot.md#wb_robot_get_data)('data')                                                           |
| name = [wb\_robot\_get\_name](robot.md#wb_robot_get_name)()                                             |
| name = [wb\_robot\_get\_controller\_name](robot.md#wb_robot_get_controller_name)()                      |
| name = [wb\_robot\_get\_controller\_arguments](robot.md#wb_robot_get_controller_name)()                 |
| path = [wb\_robot\_get\_project\_path](robot.md#wb_robot_get_project_path)()                            |
| sync = [wb\_robot\_get\_synchronization](robot.md#wb_robot_get_synchronization)()                       |
| time = [wb\_robot\_get\_time](robot.md#wb_robot_get_time)()                                             |
| path = [wb\_robot\_get\_world\_path](robot.md#wb_robot_get_world_path)()                                |
| type = [wb\_robot\_get\_type](robot.md#wb_robot_get_type)()                                             |

%end

%api "matlab_servo"

| % [Servo](servo.md) :                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- |
| WB\_SERVO\_ROTATIONAL, WB\_SERVO\_LINEAR                                                                                |
| [wb\_servo\_set\_position](servo.md#wb_servo_set_position)(tag, position)                                               |
| target = [wb\_servo\_get\_target\_position](servo.md#wb_servo_set_position)(tag)                                        |
| [wb\_servo\_set\_velocity](servo.md#wb_servo_set_position)(tag, vel)                                                    |
| [wb\_servo\_set\_acceleration](servo.md#wb_servo_set_position)(tag, acc)                                                |
| [wb\_servo\_set\_motor\_force](servo.md#wb_servo_set_position)(tag, force)                                              |
| [wb\_servo\_set\_control\_p](servo.md#wb_servo_set_position)(tag, p)                                                    |
| min = [wb\_servo\_get\_min\_position](servo.md#wb_servo_set_position)(tag)                                              |
| max = [wb\_servo\_get\_max\_position](servo.md#wb_servo_set_position)(tag)                                              |
| [wb\_servo\_enable\_position](servo.md#wb_servo_enable_position)(tag, sampling_period)                                  |
| [wb\_servo\_disable\_position](servo.md#wb_servo_enable_position)(tag)                                                  |
| period = [wb\_servo\_get\_position\_sampling\_period](servo.md#wb_servo_enable_position)(tag)                           |
| position = [wb\_servo\_get\_position](servo.md#wb_servo_enable_position)(tag)                                           |
| [wb\_servo\_enable\_motor\_force\_feedback](servo.md#wb_servo_enable_motor_force_feedback)(tag, sampling_period)        |
| [wb\_servo\_disable\_motor\_force\_feedback](servo.md#wb_servo_enable_motor_force_feedback)(tag)                        |
| period = [wb\_servo\_get\_motor\_force\_feedback\_sampling\_period](servo.md#wb_servo_enable_motor_force_feedback)(tag) |
| force = [wb\_servo\_get\_motor\_force\_feedback](servo.md#wb_servo_enable_motor_force_feedback)(tag)                    |
| [wb\_servo\_set\_force](servo.md#wb_servo_set_force)(tag, force)                                                        |
| type = [wb\_servo\_get\_type](servo.md#wb_servo_get_type)(tag)                                                          |

%end

%api "matlab_speaker"

| % [Speaker](speaker.md) :                                                                                   |
| ----------------------------------------------------------------------------------------------------------- |
| [wb_speaker_play_sound](speaker.md#wb_speaker_play_sound)(left, right, sound, volume, pitch, balance, loop) |
| [wb_speaker_stop](speaker.md#wb_speaker_stop)(tag, sound)                                                   |
| engine = [wb_speaker_get_engine](speaker.md#wb_speaker_get_engine)(tag)                                     |
| language = [wb_speaker_get_language](speaker.md#wb_speaker_get_language)(tag)                               |
| success = [wb_speaker_set_engine](speaker.md#wb_speaker_set_engine)(tag, language)                          |
| [wb_speaker_set_language](speaker.md#wb_speaker_set_language)(tag, language)                                |
| [wb_speaker_speak](speaker.md#wb_speaker_set_language)(tag, text, volume)                                   |

%end

%api "matlab_supervisor"

| % [Supervisor](supervisor.md) :                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WB\_SF\_BOOL, WB\_SF\_INT32, WB\_SF\_FLOAT, WB\_SF\_VEC2F,                                                                                                           |
| WB\_SF\_VEC3F, WB\_SF\_ROTATION, WB\_SF\_COLOR, WB\_SF\_STRING,                                                                                                      |
| WB\_SF\_NODE, WB\_MF, WB\_MF\_INT32, WB\_MF\_FLOAT, B\_MF\_VEC2F,                                                                                                    |
| WB\_MF\_VEC3F, WB\_MF\_COLOR, WB\_MF\_STRING, WB\_MF\_NODE                                                                                                           |
| WB\_SUPERVISOR\_SIMULATION\_MODE\_PAUSE, WB\_SUPERVISOR\_SIMULATION\_MODE\_REAL\_TIME, WB\_SUPERVISOR\_SIMULATION\_MODE\_RUN, WB\_SUPERVISOR\_SIMULATION\_MODE\_FAST |
| [wb\_supervisor\_export\_image](supervisor.md#wb_supervisor_export_image)('filename', quality)                                                                       |
| node = [wb\_supervisor\_node\_get\_root](supervisor.md#wb_supervisor_node_get_from_def)()                                                                            |
| node = [wb\_supervisor\_node\_get\_self](supervisor.md#wb_supervisor_node_get_from_def)()                                                                            |
| node = [wb\_supervisor\_node\_get\_from\_def](supervisor.md#wb_supervisor_node_get_from_def)('def')                                                                  |
| s  = [wb\_supervisor\_node\_get\_def](supervisor.md#wb_supervisor_node_get_def)(node)                                                                                |
| node = [wb\_supervisor\_node\_get\_from\_id](supervisor.md#wb_supervisor_node_get_from_def)('id')                                                                    |
| id = [wb\_supervisor\_node\_get\_id](supervisor.md#wb_supervisor_node_get_from_def)(node)                                                                            |
| node = [wb\_supervisor\_node\_get\_parent\_node](supervisor.md#wb_supervisor_node_get_from_def)(node)                                                                |
| [wb\_supervisor\_node\_remove](supervisor.md#wb_supervisor_node_get_from_def)(node)                                                                                  |
| [wb\_supervisor\_set\_label](supervisor.md#wb_supervisor_set_label)(id, 'text', x, y, size, [r g b], transparency)                                                   |
| [wb\_supervisor\_simulation\_quit](supervisor.md#wb_supervisor_simulation_quit)(status)                                                                              |
| [wb\_supervisor\_simulation\_revert](supervisor.md#wb_supervisor_simulation_revert)()                                                                                |
| [wb\_supervisor\_simulation\_reset\_physics](supervisor.md#wb_supervisor_simulation_reset_physics)()                                                                 |
| mode = [wb\_supervisor\_simulation\_get\_mode](supervisor.md#wb_supervisor_simulation_set_mode)()                                                                    |
| [wb\_supervisor\_simulation\_set\_mode](supervisor.md#wb_supervisor_simulation_set_mode)(mode)                                                                       |
| [wb\_supervisor\_load\_world](supervisor.md#wb_supervisor_load_world)('filename')                                                                                    |
| [wb\_supervisor\_save\_world](supervisor.md#wb_supervisor_load_world)()                                                                                              |
| [wb\_supervisor\_save\_world](supervisor.md#wb_supervisor_load_world)('filename')                                                                                    |
| [wb\_supervisor\_movie\_start\_recording](supervisor.md#wb_supervisor_movie_start_recording)('filename', width, height, codec, quality,                              |
| acceleration, caption)                                                                                                                                               |
| [wb\_supervisor\_movie\_stop\_recording](supervisor.md#wb_supervisor_movie_start_recording)()                                                                        |
| status = [wb\_supervisor\_movie\_is\_ready](supervisor.md#wb_supervisor_movie_start_recording)()                                                                     |
| status = [wb\_supervisor\_movie\_failed](supervisor.md#wb_supervisor_movie_start_recording)()                                                                        |
| success = [wb\_supervisor\_animation\_start\_recording](supervisor.md#wb_supervisor_animation_start_recording)('filename')                                           |
| success = [wb\_supervisor\_animation\_stop\_recording](supervisor.md#wb_supervisor_animation_start_recording)()                                                      |
| type = [wb\_supervisor\_field\_get\_type](supervisor.md#wb_supervisor_field_get_type)(field)                                                                         |
| name = [wb\_supervisor\_field\_get\_type\_name](supervisor.md#wb_supervisor_field_get_type)(field)                                                                   |
| count = [wb\_supervisor\_field\_get\_count](supervisor.md#wb_supervisor_field_get_type)(field)                                                                       |
| b = [wb\_supervisor\_field\_get\_sf\_bool](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                     |
| i = [wb\_supervisor\_field\_get\_sf\_int32](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                    |
| f = [wb\_supervisor\_field\_get\_sf\_float](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                    |
| [x y] = [wb\_supervisor\_field\_get\_sf\_vec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                |
| [x y z] = [wb\_supervisor\_field\_get\_sf\_vec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                              |
| [x y z alpha] = [wb\_supervisor\_field\_get\_sf\_rotation](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                     |
| [r g b] = [wb\_supervisor\_field\_get\_sf\_color](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                              |
| s = [wb\_supervisor\_field\_get\_sf\_string](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                   |
| node = [wb\_supervisor\_field\_get\_sf\_node](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                  |
| b = [wb\_supervisor\_field\_get\_mf\_bool](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                              |
| i = [wb\_supervisor\_field\_get\_mf\_int32](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                             |
| f = [wb\_supervisor\_field\_get\_mf\_float](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                             |
| [x y] = [wb\_supervisor\_field\_get\_mf\_vec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                         |
| [x y z] = [wb\_supervisor\_field\_get\_mf\_vec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                       |
| [x y z a] = [wb\_supervisor\_field\_get\_mf\_rotation](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                  |
| [r g b] = [wb\_supervisor\_field\_get\_mf\_color](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                       |
| s = [wb\_supervisor\_field\_get\_mf\_string](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                            |
| node = [wb\_supervisor\_field\_get\_mf\_node](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                           |
| [wb\_supervisor\_field\_set\_sf\_bool](supervisor.md#wb_supervisor_field_set_sf_bool)(field, value)                                                                  |
| [wb\_supervisor\_field\_set\_sf\_int32](supervisor.md#wb_supervisor_field_set_sf_bool)(field, value)                                                                 |
| [wb\_supervisor\_field\_set\_sf\_float](supervisor.md#wb_supervisor_field_set_sf_bool)(field, value)                                                                 |
| [wb\_supervisor\_field\_set\_sf\_vec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [x y])                                                                 |
| [wb\_supervisor\_field\_set\_sf\_vec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [x y z])                                                               |
| [wb\_supervisor\_field\_set\_sf\_rotation](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [x y z alpha])                                                      |
| [wb\_supervisor\_field\_set\_sf\_color](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [r g b])                                                               |
| [wb\_supervisor\_field\_set\_sf\_string](supervisor.md#wb_supervisor_field_set_sf_bool)(field, 'value')                                                              |
| [wb\_supervisor\_field\_set\_mf\_bool](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, value)                                                           |
| [wb\_supervisor\_field\_set\_mf\_int32](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, value)                                                          |
| [wb\_supervisor\_field\_set\_mf\_float](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, value)                                                          |
| [wb\_supervisor\_field\_set\_mf\_vec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [x y])                                                          |
| [wb\_supervisor\_field\_set\_mf\_vec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [x y z])                                                        |
| [wb\_supervisor\_field\_set\_mf\_rotation](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [x y z a])                                                   |
| [wb\_supervisor\_field\_set\_mf\_color](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [r g b])                                                        |
| [wb\_supervisor\_field\_set\_mf\_string](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, 'value')                                                       |
| [wb\_supervisor\_field\_import\_mf\_node](supervisor.md#wb_supervisor_field_import_mf_node)(field, position, 'filename')                                             |
| [wb\_supervisor\_field\_import\_mf\_node\_from\_string](supervisor.md#wb_supervisor_field_import_mf_node)(field, position, 'node\_string')                           |
| [wb\_supervisor\_field\_remove\_mf\_node](supervisor.md#wb_supervisor_field_import_mf_node)(field, position)                                                         |
| type = [wb\_supervisor\_node\_get\_type](supervisor.md#wb_supervisor_node_get_type)(node)                                                                            |
| name = [wb\_supervisor\_node\_get\_type\_name](supervisor.md#wb_supervisor_node_get_type)(node)                                                                      |
| name = [wb\_supervisor\_node\_get\_base\_type\_name](supervisor.md#wb_supervisor_node_get_type)(node)                                                                |
| field = [wb\_supervisor\_node\_get\_field](supervisor.md#wb_supervisor_node_get_field)(node, 'field\_name')                                                          |
| position = [wb\_supervisor\_node\_get\_position](supervisor.md#wb_supervisor_node_get_position)(node)                                                                |
| orientation = [wb\_supervisor\_node\_get\_orientation](supervisor.md#wb_supervisor_node_get_position)(node)                                                          |
| com = [wb\_supervisor\_node\_get\_center\_of\_mass](supervisor.md#wb_supervisor_node_get_center_of_mass)(node)                                                       |
| contact\_point = [wb\_supervisor\_node\_get\_contact\_point](supervisor.md#wb_supervisor_node_get_contact_point)(node, index)                                        |
| number\_of\_contacts = [wb\_supervisor\_node\_get\_number\_of\_contact\_points](supervisor.md#wb_supervisor_node_get_number_of_contact_points)(index)                |
| balance = [wb\_supervisor\_node\_get\_static\_balance](supervisor.md#wb_supervisor_node_get_static_balance)(node)                                                    |
| velocity = [wb\_supervisor\_node\_get\_velocity](supervisor.md#wb_supervisor_node_get_velocity)(node)                                                                |
| [wb\_supervisor\_node\_set\_velocity](supervisor.md#wb_supervisor_node_get_velocity)(node, velocity)                                                                 |
| [wb\_supervisor\_node\_reset\_physics](supervisor.md#wb_supervisor_node_reset_physics)(node)                                                                         |
| [wb\_supervisor\_node\_restart\_controller](supervisor.md#wb_supervisor_node_restart_controller)(node)                                                                   |
| [wb\_supervisor\_node\_set\_visibility](supervisor.md#wb_supervisor_node_set_visibility)(node, from, visible)                                                        |

%end

%api "matlab_touch_sensor"

| % [TouchSensor](touchsensor.md) :                                                                   |
| --------------------------------------------------------------------------------------------------- |
| WB\_TOUCH\_SENSOR\_BUMPER, WB\_TOUCH\_SENSOR\_FORCE,                                                |
| WB\_TOUCH\_SENSOR\_FORCE3D                                                                          |
| [wb\_touch\_sensor\_enable](touchsensor.md#wb_touch_sensor_get_values)(tag, sampling_period)        |
| [wb\_touch\_sensor\_disable](touchsensor.md#wb_touch_sensor_get_values)(tag)                        |
| period = [wb\_touch\_sensor\_get\_sampling\_period](touchsensor.md#wb_touch_sensor_get_values)(tag) |
| value = [wb\_touch\_sensor\_get\_value](touchsensor.md#wb_touch_sensor_get_values)(tag)             |
| [x y z] = [wb\_touch\_sensor\_get\_values](touchsensor.md#wb_touch_sensor_get_values)(tag)          |
| type = [wb\_touch\_sensor\_get\_type](touchsensor.md#wb_touch_sensor_get_type)(tag)                 |

%end
