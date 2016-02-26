## Matlab API

The following tables describe the Matlab functions.

<a name="matlab_accelerometer"/>

| % [Accelerometer](accelerometer.md#accelerometer) :                                                    |
| ------------------------------------------------------------------------------------------------------ |
| [wb\_accelerometer\_enable](accelerometer.md#wb_accelerometer_get_values)(tag, ms)                     |
| [wb\_accelerometer\_disable](accelerometer.md#wb_accelerometer_get_values)(tag)                        |
| period = [wb\_accelerometer\_get\_sampling\_period](accelerometer.md#wb_accelerometer_get_values)(tag) |
| [x y z] = [wb\_accelerometer\_get\_values](accelerometer.md#wb_accelerometer_get_values)(tag)          |

<a name="matlab_brake"/>

| % [Brake](brake.md#brake) :                                                                       |
| ------------------------------------------------------------------------------------------------- |
| [wb\_brake\_set\_damping\_constant](brake.md#wb_brake_set_damping_constant)(tag, dampingConstant) |
| type = [wb\_brake\_get\_type](brake.md#wb_brake_set_damping_constant)(tag)                        |

<a name="matlab_camera"/>

| % [Camera](camera.md#camera) :                                                                 |
| ---------------------------------------------------------------------------------------------- |
| WB\_CAMERA\_COLOR                                                                              |
| WB\_CAMERA\_RANGE\_FINDER                                                                      |
| [wb\_camera\_enable](camera.md#wb_camera_enable)(tag, ms)                                      |
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
| type = [wb\_camera\_get\_type](camera.md#wb_camera_get_type)(tag)                              |
| image = [wb\_camera\_get\_image](camera.md#wb_camera_get_image)(tag)                           |
| image = [wb\_camera\_get\_range\_image](camera.md#wb_camera_get_range_image)(tag)              |
| max\_range = [wb\_camera\_get\_max\_range](camera.md#wb_camera_get_range_image)(tag)           |
| [wb\_camera\_save\_image](camera.md#wb_camera_save_image)(tag, 'filename', quality)            |

<a name="matlab_compass"/>

| % [Compass](compass.md#compass) :                                                    |
| ------------------------------------------------------------------------------------ |
| [wb\_compass\_enable](compass.md#wb_compass_get_values)(tag, ms)                     |
| [wb\_compass\_disable](compass.md#wb_compass_get_values)(tag)                        |
| period = [wb\_compass\_get\_sampling\_period](compass.md#wb_compass_get_values)(tag) |
| [x y z] = [wb\_compass\_get\_values](compass.md#wb_compass_get_values)(tag)          |

<a name="matlab_connector"/>

| % [Connector](connector.md#connector) :                                                |
| -------------------------------------------------------------------------------------- |
| [wb\_connector\_enable\_presence](connector.md#wb_connector_get_presence)(tag, ms)     |
| [wb\_connector\_disable\_presence](connector.md#wb_connector_get_presence)(tag)        |
| presence = [wb\_connector\_get\_presence](connector.md#wb_connector_get_presence)(tag) |
| [wb\_connector\_lock](connector.md#wb_connector_lock)(tag)                             |
| [wb\_connector\_unlock](connector.md#wb_connector_lock)(tag)                           |

<a name="matlab_device"/>

| % [Device](device.md#device) :                                               |
| ---------------------------------------------------------------------------- |
| model = [wb\_device\_get\_model](device.md#wb_device_get_model)(tag)         |
| name = [wb\_device\_get\_name](device.md#wb_device_get_name)(tag)            |
| type = [wb\_device\_get\_node\_type](device.md#wb_device_get_node_type)(tag) |

<a name="matlab_differential_wheels"/>

| % [DifferentialWheels](differentialwheels.md#differentialwheels) :                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| [wb\_differential\_wheels\_set\_speed](differentialwheels.md#wb_differential_wheels_set_speed)(left, right)                          |
| left = [wb\_differential\_wheels\_get\_left\_speed](differentialwheels.md#wb_differential_wheels_set_speed)()                        |
| right = [wb\_differential\_wheels\_get\_right\_speed](differentialwheels.md#wb_differential_wheels_set_speed)()                      |
| [wb\_differential\_wheels\_enable\_encoders](differentialwheels.md#wb_differential_wheels_enable_encoders)(ms)                       |
| [wb\_differential\_wheels\_disable\_encoders](differentialwheels.md#wb_differential_wheels_enable_encoders)()                        |
| period = [wb\_differential\_wheels\_get\_encoders\_sampling\_period](differentialwheels.md#wb_differential_wheels_enable_encoders)() |
| left = [wb\_differential\_wheels\_get\_left\_encoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)()               |
| right = [wb\_differential\_wheels\_get\_right\_encoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)()             |
| [wb\_differential\_wheels\_set\_encoders](differentialwheels.md#wb_differential_wheels_get_left_encoder)(left, right)                |
| max = [wb\_differential\_wheels\_get\_max\_speed](differentialwheels.md#wb_differential_wheels_get_max_speed)()                      |
| unit = [wb\_differential\_wheels\_get\_speed\_unit](differentialwheels.md#wb_differential_wheels_get_speed_unit)()                   |

<a name="matlab_display"/>

| % [Display](display.md#display) :                                                                          |
| ---------------------------------------------------------------------------------------------------------- |
| RGB                                                                                                        |
| RGBA                                                                                                       |
| ARGB                                                                                                       |
| BGRA                                                                                                       |
| width = [wb\_display\_get\_width](display.md#wb_display_get_width)(tag)                                    |
| height = [wb\_display\_get\_height](display.md#wb_display_get_width)(tag)                                  |
| [wb\_display\_set\_color](display.md#wb_display_set_context)(tag, [r g b])                                 |
| [wb\_display\_set\_alpha](display.md#wb_display_set_context)(tag, alpha)                                   |
| [wb\_display\_set\_opacity](display.md#wb_display_set_context)(tag, opacity)                               |
| [wb\_display\_draw\_pixel](display.md#wb_display_draw_primitive)(tag, x, y)                                |
| [wb\_display\_draw\_line](display.md#wb_display_draw_primitive)(tag, x1, y1, x2, y2)                       |
| [wb\_display\_draw\_rectangle](display.md#wb_display_draw_primitive)(tag, x, y, width, height)             |
| [wb\_display\_draw\_oval](display.md#wb_display_draw_primitive)(tag, cx, cy, a, b)                         |
| [wb\_display\_draw\_polygon](display.md#wb_display_draw_primitive)(tag, [x1 x2 ... xn], [y1 y2 ... yn])    |
| [wb\_display\_draw\_text](display.md#wb_display_draw_primitive)(tag, 'txt', x, y)                          |
| [wb\_display\_fill\_rectangle](display.md#wb_display_draw_primitive)(tag, x, y, width, height)             |
| [wb\_display\_fill\_oval](display.md#wb_display_draw_primitive)(tag, cx, cy, a, b)                         |
| [wb\_display\_fill\_polygon](display.md#wb_display_draw_primitive)(tag, [x1 x2 ... xn], [y1 y2 ... yn])    |
| image = [wb\_display\_image\_copy](display.md#wb_display_image_functions)(tag, x, y, width, height)        |
| [wb\_display\_image\_paste](display.md#wb_display_image_functions)(tag, image, x, y)                       |
| image = [wb\_display\_image\_load](display.md#wb_display_image_functions)(tag, 'filename')                 |
| image = [wb\_display\_image\_new](display.md#wb_display_image_functions)(tag, width, height, data ,format) |
| [wb\_display\_image\_save](display.md#wb_display_image_functions)(tag, image, 'filename')                  |
| [wb\_display\_image\_delete](display.md#wb_display_image_functions)(tag, image)                            |

<a name="matlab_distance_sensor"/>

| % [DistanceSensor](distancesensor.md#distancesensor) :                                                      |
| ----------------------------------------------------------------------------------------------------------- |
| [wb\_distance\_sensor\_enable](distancesensor.md#wb_distance_sensor_get_value)(tag, ms)                     |
| [wb\_distance\_sensor\_disable](distancesensor.md#wb_distance_sensor_get_value)(tag)                        |
| period = [wb\_distance\_sensor\_get\_sampling\_period](distancesensor.md#wb_distance_sensor_get_value)(tag) |
| value = [wb\_distance\_sensor\_get\_value](distancesensor.md#wb_distance_sensor_get_value)(tag)             |

<a name="matlab_emitter"/>

| % [Emitter](emitter.md#emitter) :                                                   |
| ----------------------------------------------------------------------------------- |
| WB\_CHANNEL\_BROADCAST                                                              |
| [wb\_emitter\_send](emitter.md#wb_emitter_send)(tag, data)                          |
| [wb\_emitter\_set\_channel](emitter.md#wb_emitter_set_channel)(tag, channel)        |
| channel = [wb\_emitter\_get\_channel](emitter.md#wb_emitter_set_channel)(tag)       |
| range = [wb\_emitter\_get\_range](emitter.md#wb_emitter_set_range)(tag)             |
| [wb\_emitter\_set\_range](emitter.md#wb_emitter_set_range)(tag, range)              |
| size = [wb\_emitter\_get\_buffer\_size](emitter.md#wb_emitter_get_buffer_size)(tag) |

<a name="matlab_gps"/>

| % [GPS](gps.md#gps) :                                                    |
| ------------------------------------------------------------------------ |
| [wb\_gps\_enable](gps.md#wb_gps_get_values)(tag, ms)                     |
| [wb\_gps\_disable](gps.md#wb_gps_get_values)(tag)                        |
| period = [wb\_gps\_get\_sampling\_period](gps.md#wb_gps_get_values)(tag) |
| [x y z] = [wb\_gps\_get\_values](gps.md#wb_gps_get_values)(tag)          |

<a name="matlab_gyro"/>

| % [Gyro](gyro.md#gyro) :                                                    |
| --------------------------------------------------------------------------- |
| [wb\_gyro\_enable](gyro.md#wb_gyro_get_values)(tag, ms)                     |
| [wb\_gyro\_disable](gyro.md#wb_gyro_get_values)(tag)                        |
| period = [wb\_gyro\_get\_sampling\_period](gyro.md#wb_gyro_get_values)(tag) |
| [x y z] = [wb\_gyro\_get\_values](gyro.md#wb_gyro_get_values)(tag)          |

<a name="matlab_inertial_unit"/>

| % [InertialUnit](inertialunit.md#inertialunit) :                                                                         |
| ------------------------------------------------------------------------------------------------------------------------ |
| [wb\_inertial\_unit\_enable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag, ms)                               |
| [wb\_inertial\_unit\_disable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag)                                  |
| period = [wb\_inertial\_unit\_get\_sampling\_period](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag)           |
| [roll pitch yaw] = [wb\_inertial\_unit\_get\_roll\_pitch\_yaw](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(tag) |

<a name="matlab_led"/>

| % [LED](led.md#led) :                          |
| ---------------------------------------------- |
| [wb\_led\_set](led.md#wb_led_set)(tag, state)  |
| state = [wb\_led\_get](led.md#wb_led_set)(tag) |

<a name="matlab_light_sensor"/>

| % [LightSensor](lightsensor.md#lightsensor) :                                                      |
| -------------------------------------------------------------------------------------------------- |
| [wb\_light\_sensor\_enable](lightsensor.md#wb_light_sensor_get_value)(tag, ms)                     |
| [wb\_light\_sensor\_disable](lightsensor.md#wb_light_sensor_get_value)(tag)                        |
| period = [wb\_light\_sensor\_get\_sampling\_period](lightsensor.md#wb_light_sensor_get_value)(tag) |
| value = [wb\_light\_sensor\_get\_value](lightsensor.md#wb_light_sensor_get_value)(tag)             |

<a name="matlab_motion"/>

| % [Motion](motion.md#motion) :                                                |
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

<a name="matlab_motor"/>

| % [Motor](motor.md#motor) :                                                                                 |
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
| [wb\_motor\_enable\_force\_feedback](motor.md#wb_motor_enable_force_feedback)(tag, ms)                      |
| [wb\_motor\_disable\_force\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                         |
| period = [wb\_motor\_get\_force\_feedback\_sampling\_period](motor.md#wb_motor_enable_force_feedback)(tag)  |
| force = [wb\_motor\_get\_force\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                     |
| [wb\_motor\_set\_force](motor.md#wb_motor_set_force)(tag, force)                                            |
| [wb\_motor\_enable\_torque\_feedback](motor.md#wb_motor_enable_force_feedback)(tag, ms)                     |
| [wb\_motor\_disable\_torque\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                        |
| period = [wb\_motor\_get\_torque\_feedback\_sampling\_period](motor.md#wb_motor_enable_force_feedback)(tag) |
| force = [wb\_motor\_get\_torque\_feedback](motor.md#wb_motor_enable_force_feedback)(tag)                    |
| [wb\_motor\_set\_torque](motor.md#wb_motor_set_force)(tag, torque)                                          |
| type = [wb\_motor\_get\_type](motor.md#wb_motor_get_type)(tag)                                              |

<a name="matlab_node"/>

| Node:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WB\_NODE\_NO\_NODE, WB\_NODE\_ACCELEROMETER, WB\_NODE\_APPEARANCE, WB\_NODE\_BACKGROUND, WB\_NODE\_BALL\_JOINT, WB\_NODE\_BALL\_JOINT\_PARAMETERS, WB\_NODE\_BOX, WB\_NODE\_BRAKE, WB\_NODE\_CAMERA, WB\_NODE\_CAMERA\_FOCUS, WB\_NODE\_CAMERA\_LENS\_DISTORTION, WB\_NODE\_CAMERA\_ZOOM, WB\_NODE\_CAPSULE, WB\_NODE\_CHARGER, WB\_NODE\_COLOR, WB\_NODE\_COMPASS, WB\_NODE\_CONE, WB\_NODE\_CONNECTOR, WB\_NODE\_CONTACT\_PROPERTIES, WB\_NODE\_COORDINATE, WB\_NODE\_CYLINDER, WB\_NODE\_DAMPING, WB\_NODE\_DIFFERENTIAL\_WHEELS, WB\_NODE\_DIRECTIONAL\_LIGHT, WB\_NODE\_DISPLAY, WB\_NODE\_DISTANCE\_SENSOR, WB\_NODE\_ELEVATION\_GRID, WB\_NODE\_EMITTER, WB\_NODE\_EXTRUSION, WB\_NODE\_FLUID, WB\_NODE\_FOG, WB\_NODE\_GPS, WB\_NODE\_GROUP, WB\_NODE\_GYRO, WB\_NODE\_HINGE\_2\_JOINT, WB\_NODE\_HINGE\_2\_JOINT\_PARAMETERS, WB\_NODE\_HINGE\_JOINT, WB\_NODE\_HINGE\_JOINT\_PARAMETERS, WB\_NODE\_IMAGE\_TEXTURE, WB\_NODE\_IMMERSION\_PROPERTIES, WB\_NODE\_INDEXED\_FACE\_SET, WB\_NODE\_INDEXED\_LINE\_SET, WB\_NODE\_INERTIAL\_UNIT, WB\_NODE\_JOINT\_PARAMETERS, WB\_NODE\_LED, WB\_NODE\_LIGHT\_SENSOR, WB\_NODE\_LINEAR\_MOTOR, WB\_NODE\_MATERIAL, WB\_NODE\_MICROPHONE, WB\_NODE\_PEN, WB\_NODE\_PHYSICS, WB\_NODE\_PLANE, WB\_NODE\_POINT\_LIGHT, WB\_NODE\_POSITION\_SENSOR, WB\_NODE\_PROPELLER, WB\_NODE\_RADIO, WB\_NODE\_RECEIVER, WB\_NODE\_ROBOT, WB\_NODE\_ROTATIONAL\_MOTOR, WB\_NODE\_SERVO, WB\_NODE\_SHAPE, WB\_NODE\_SLIDER\_JOINT, WB\_NODE\_SLOT, WB\_NODE\_SOLID, WB\_NODE\_SOLID\_REFERENCE, WB\_NODE\_SPEAKER, WB\_NODE\_SPHERE, WB\_NODE\_SPOT\_LIGHT, WB\_NODE\_SUPERVISOR, WB\_NODE\_SWITCH, WB\_NODE\_TEXTURE\_COORDINATE, WB\_NODE\_TEXTURE\_TRANSFORM, WB\_NODE\_TOUCH\_SENSOR, WB\_NODE\_TRACK, WB\_NODE\_TRACK\_WHEEL, WB\_NODE\_TRANSFORM, WB\_NODE\_VIEWPOINT, WB\_NODE\_WORLD\_INFO |

<a name="matlab_pen"/>

| % [Pen](pen.md#pen) :                                                          |
| ------------------------------------------------------------------------------ |
| [wb\_pen\_write](pen.md#wb_pen_write)(tag, write)                              |
| [wb\_pen\_set\_ink\_color](pen.md#wb_pen_set_ink_color)(tag, [r g b], density) |

<a name="matlab_position_sensor"/>

| % [PositionSensor](positionsensor.md#positionsensor) :                                                      |
| ----------------------------------------------------------------------------------------------------------- |
| WB\_ANGULAR, WB\_LINEAR                                                                                     |
| [wb\_position\_sensor\_enable](positionsensor.md#wb_position_sensor_get_value)(tag, ms)                     |
| [wb\_position\_sensor\_disable](positionsensor.md#wb_position_sensor_get_value)(tag)                        |
| period = [wb\_position\_sensor\_get\_sampling\_period](positionsensor.md#wb_position_sensor_get_value)(tag) |
| value = [wb\_position\_sensor\_get\_value](positionsensor.md#wb_position_sensor_get_value)(tag)             |
| type = [wb\_position\_sensor\_get\_type](positionsensor.md#wb_position_sensor_get_value)(tag)               |

<a name="matlab_receiver"/>

| % [Receiver](receiver.md#receiver) :                                                                |
| --------------------------------------------------------------------------------------------------- |
| WB\_CHANNEL\_BROADCAST                                                                              |
| [wb\_receiver\_enable](receiver.md#wb_receiver_enable)(tag, ms)                                     |
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

<a name="matlab_robot"/>

| % [Robot](robot.md#robot) :                                                                             |
| ------------------------------------------------------------------------------------------------------- |
| WB\_MODE\_SIMULATION,                                                                                   |
| WB\_MODE\_CROSS\_COMPILATION,                                                                           |
| WB\_MODE\_REMOTE\_CONTROL                                                                               |
| WB\_ROBOT\_KEYBOARD\_END                                                                                |
| WB\_ROBOT\_KEYBOARD\_HOME                                                                               |
| WB\_ROBOT\_KEYBOARD\_LEFT                                                                               |
| WB\_ROBOT\_KEYBOARD\_UP                                                                                 |
| WB\_ROBOT\_KEYBOARD\_RIGHT                                                                              |
| WB\_ROBOT\_KEYBOARD\_DOWN                                                                               |
| WB\_ROBOT\_KEYBOARD\_PAGEUP                                                                             |
| WB\_ROBOT\_KEYBOARD\_PAGEDOWN                                                                           |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_HOME                                                                       |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_LEFT                                                                       |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_UP                                                                         |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_RIGHT                                                                      |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_DOWN                                                                       |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_END                                                                        |
| WB\_ROBOT\_KEYBOARD\_KEY                                                                                |
| WB\_ROBOT\_KEYBOARD\_SHIFT                                                                              |
| WB\_ROBOT\_KEYBOARD\_CONTROL                                                                            |
| WB\_ROBOT\_KEYBOARD\_ALT                                                                                |
| [wb\_robot\_step](robot.md#wb_robot_step)(ms)                                                           |
| tag = [wb\_robot\_get\_device](robot.md#wb_robot_get_device)('name')                                    |
| size = [wb\_robot\_get\_number\_of\_devices](robot.md#wb_robot_get_device_by_index)()                   |
| tag = [wb\_robot\_get\_device\_by\_index](robot.md#wb_robot_get_device_by_index)(index)                 |
| [wb\_robot\_battery\_sensor\_enable](robot.md#wb_robot_battery_sensor_enable)(ms)                       |
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
| [wb\_robot\_keyboard\_enable](robot.md#wb_robot_keyboard_enable)(ms)                                    |
| [wb\_robot\_keyboard\_disable](robot.md#wb_robot_keyboard_enable)()                                     |
| key = [wb\_robot\_keyboard\_get\_key](robot.md#wb_robot_keyboard_enable)()                              |
| type = [wb\_robot\_get\_type](robot.md#wb_robot_get_type)()                                             |

<a name="matlab_servo"/>

| % [Servo](servo.md#servo) :                                                                                             |
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
| [wb\_servo\_enable\_position](servo.md#wb_servo_enable_position)(tag, ms)                                               |
| [wb\_servo\_disable\_position](servo.md#wb_servo_enable_position)(tag)                                                  |
| period = [wb\_servo\_get\_position\_sampling\_period](servo.md#wb_servo_enable_position)(tag)                           |
| position = [wb\_servo\_get\_position](servo.md#wb_servo_enable_position)(tag)                                           |
| [wb\_servo\_enable\_motor\_force\_feedback](servo.md#wb_servo_enable_motor_force_feedback)(tag, ms)                     |
| [wb\_servo\_disable\_motor\_force\_feedback](servo.md#wb_servo_enable_motor_force_feedback)(tag)                        |
| period = [wb\_servo\_get\_motor\_force\_feedback\_sampling\_period](servo.md#wb_servo_enable_motor_force_feedback)(tag) |
| force = [wb\_servo\_get\_motor\_force\_feedback](servo.md#wb_servo_enable_motor_force_feedback)(tag)                    |
| [wb\_servo\_set\_force](servo.md#wb_servo_set_force)(tag, force)                                                        |
| type = [wb\_servo\_get\_type](servo.md#wb_servo_get_type)(tag)                                                          |

<a name="matlab_supervisor"/>

| % [Supervisor](supervisor.md#supervisor) :                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WB\_SF\_BOOL, WB\_SF\_INT32, WB\_SF\_FLOAT, WB\_SF\_VEC2F,                                                                                                                                                           |
| WB\_SF\_VEC3F, WB\_SF\_ROTATION, WB\_SF\_COLOR, WB\_SF\_STRING,                                                                                                                                                      |
| WB\_SF\_NODE, WB\_MF, WB\_MF\_INT32, WB\_MF\_FLOAT, B\_MF\_VEC2F,                                                                                                                                                    |
| WB\_MF\_VEC3F, WB\_MF\_COLOR, WB\_MF\_STRING, WB\_MF\_NODE                                                                                                                                                           |
| WB\_SUPERVISOR\_MOVIE\_READY, WB\_SUPERVISOR\_MOVIE\_RECORDING, WB\_SUPERVISOR\_MOVIE\_SAVING, WB\_SUPERVISOR\_MOVIE\_WRITE\_ERROR, WB\_SUPERVISOR\_MOVIE\_ENCODING\_ERROR, WB\_SUPERVISOR\_MOVIE\_SIMULATION\_ERROR |
| [wb\_supervisor\_export\_image](supervisor.md#wb_supervisor_export_image)('filename', quality)                                                                                                                       |
| node = [wb\_supervisor\_node\_get\_root](supervisor.md#wb_supervisor_node_get_from_def)()                                                                                                                            |
| node = [wb\_supervisor\_node\_get\_self](supervisor.md#wb_supervisor_node_get_from_def)()                                                                                                                            |
| node = [wb\_supervisor\_node\_get\_from\_def](supervisor.md#wb_supervisor_node_get_from_def)('def')                                                                                                                  |
| node = [wb\_supervisor\_node\_get\_from\_id](supervisor.md#wb_supervisor_node_get_from_def)('id')                                                                                                                    |
| id = [wb\_supervisor\_node\_get\_id](supervisor.md#wb_supervisor_node_get_from_def)(node)                                                                                                                            |
| node = [wb\_supervisor\_node\_get\_parent\_node](supervisor.md#wb_supervisor_node_get_from_def)(node)                                                                                                                |
| [wb\_supervisor\_node\_remove](supervisor.md#wb_supervisor_node_get_from_def)(node)                                                                                                                                  |
| [wb\_supervisor\_set\_label](supervisor.md#wb_supervisor_set_label)(id, 'text', x, y, size, [r g b], transparency)                                                                                                   |
| [wb\_supervisor\_simulation\_quit](supervisor.md#wb_supervisor_simulation_quit)(status)                                                                                                                              |
| [wb\_supervisor\_simulation\_revert](supervisor.md#wb_supervisor_simulation_revert)()                                                                                                                                |
| [wb\_supervisor\_simulation\_reset\_physics](supervisor.md#wb_supervisor_simulation_reset_physics)()                                                                                                                 |
| [wb\_supervisor\_load\_world](supervisor.md#wb_supervisor_load_world)('filename')                                                                                                                                    |
| [wb\_supervisor\_save\_world](supervisor.md#wb_supervisor_load_world)()                                                                                                                                              |
| [wb\_supervisor\_save\_world](supervisor.md#wb_supervisor_load_world)('filename')                                                                                                                                    |
| [wb\_supervisor\_movie\_start\_recording](supervisor.md#wb_supervisor_movie_start_recording)('filename', width, height, codec, quality,                                                                              |
| acceleration, caption)                                                                                                                                                                                               |
| [wb\_supervisor\_movie\_stop\_recording](supervisor.md#wb_supervisor_movie_start_recording)()                                                                                                                        |
| status = [wb\_supervisor\_movie\_get\_status](supervisor.md#wb_supervisor_movie_start_recording)()                                                                                                                   |
| success = [wb\_supervisor\_animation\_start\_recording](supervisor.md#wb_supervisor_animation_start_recording)('filename')                                                                                           |
| success = [wb\_supervisor\_animation\_stop\_recording](supervisor.md#wb_supervisor_animation_start_recording)()                                                                                                      |
| type = [wb\_supervisor\_field\_get\_type](supervisor.md#wb_supervisor_field_get)(field)                                                                                                                              |
| name = [wb\_supervisor\_field\_get\_type\_name](supervisor.md#wb_supervisor_field_get)(field)                                                                                                                        |
| count = [wb\_supervisor\_field\_get\_count](supervisor.md#wb_supervisor_field_get)(field)                                                                                                                            |
| b = [wb\_supervisor\_field\_get\_sf\_bool](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                                     |
| i = [wb\_supervisor\_field\_get\_sf\_int32](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                                    |
| f = [wb\_supervisor\_field\_get\_sf\_float](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                                    |
| [x y] = [wb\_supervisor\_field\_get\_sf\_vec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                                |
| [x y z] = [wb\_supervisor\_field\_get\_sf\_vec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                              |
| [x y z alpha] = [wb\_supervisor\_field\_get\_sf\_rotation](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                     |
| [r g b] = [wb\_supervisor\_field\_get\_sf\_color](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                              |
| s = [wb\_supervisor\_field\_get\_sf\_string](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                                   |
| node = [wb\_supervisor\_field\_get\_sf\_node](supervisor.md#wb_supervisor_field_get_sf_bool)(field)                                                                                                                  |
| b = [wb\_supervisor\_field\_get\_mf\_bool](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                              |
| i = [wb\_supervisor\_field\_get\_mf\_int32](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                             |
| f = [wb\_supervisor\_field\_get\_mf\_float](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                             |
| [x y] = [wb\_supervisor\_field\_get\_mf\_vec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                         |
| [x y z] = [wb\_supervisor\_field\_get\_mf\_vec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                       |
| [x y z a] = [wb\_supervisor\_field\_get\_mf\_rotation](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                  |
| [r g b] = [wb\_supervisor\_field\_get\_mf\_color](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                       |
| s = [wb\_supervisor\_field\_get\_mf\_string](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                            |
| node = [wb\_supervisor\_field\_get\_mf\_node](supervisor.md#wb_supervisor_field_get_sf_bool)(field, index)                                                                                                           |
| [wb\_supervisor\_field\_set\_sf\_bool](supervisor.md#wb_supervisor_field_set_sf_bool)(field, value)                                                                                                                  |
| [wb\_supervisor\_field\_set\_sf\_int32](supervisor.md#wb_supervisor_field_set_sf_bool)(field, value)                                                                                                                 |
| [wb\_supervisor\_field\_set\_sf\_float](supervisor.md#wb_supervisor_field_set_sf_bool)(field, value)                                                                                                                 |
| [wb\_supervisor\_field\_set\_sf\_vec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [x y])                                                                                                                 |
| [wb\_supervisor\_field\_set\_sf\_vec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [x y z])                                                                                                               |
| [wb\_supervisor\_field\_set\_sf\_rotation](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [x y z alpha])                                                                                                      |
| [wb\_supervisor\_field\_set\_sf\_color](supervisor.md#wb_supervisor_field_set_sf_bool)(field, [r g b])                                                                                                               |
| [wb\_supervisor\_field\_set\_sf\_string](supervisor.md#wb_supervisor_field_set_sf_bool)(field, 'value')                                                                                                              |
| [wb\_supervisor\_field\_set\_mf\_bool](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, value)                                                                                                           |
| [wb\_supervisor\_field\_set\_mf\_int32](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, value)                                                                                                          |
| [wb\_supervisor\_field\_set\_mf\_float](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, value)                                                                                                          |
| [wb\_supervisor\_field\_set\_mf\_vec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [x y])                                                                                                          |
| [wb\_supervisor\_field\_set\_mf\_vec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [x y z])                                                                                                        |
| [wb\_supervisor\_field\_set\_mf\_rotation](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [x y z a])                                                                                                   |
| [wb\_supervisor\_field\_set\_mf\_color](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, [r g b])                                                                                                        |
| [wb\_supervisor\_field\_set\_mf\_string](supervisor.md#wb_supervisor_field_set_sf_bool)(field, index, 'value')                                                                                                       |
| [wb\_supervisor\_field\_import\_mf\_node](supervisor.md#wb_supervisor_field_import_mf_node)(field, position, 'filename')                                                                                             |
| [wb\_supervisor\_field\_import\_mf\_node\_from\_string](supervisor.md#wb_supervisor_field_import_mf_node)(field, position, 'node\_string')                                                                           |
| [wb\_supervisor\_field\_remove\_mf\_node](supervisor.md#wb_supervisor_field_import_mf_node)(field, position)                                                                                                         |
| type = [wb\_supervisor\_node\_get\_type](supervisor.md#wb_supervisor_node_get_type)(node)                                                                                                                            |
| name = [wb\_supervisor\_node\_get\_type\_name](supervisor.md#wb_supervisor_node_get_type)(node)                                                                                                                      |
| name = [wb\_supervisor\_node\_get\_base\_type\_name](supervisor.md#wb_supervisor_node_get_type)(node)                                                                                                                |
| field = [wb\_supervisor\_node\_get\_field](supervisor.md#wb_supervisor_node_get_field)(node, 'field\_name')                                                                                                          |
| position = [wb\_supervisor\_node\_get\_position](supervisor.md#wb_supervisor_node_get_position)(node)                                                                                                                |
| orientation = [wb\_supervisor\_node\_get\_orientation](supervisor.md#wb_supervisor_node_get_position)(node)                                                                                                          |
| com = [wb\_supervisor\_node\_get\_center\_of\_mass](supervisor.md#wb_supervisor_node_get_center_of_mass)(node)                                                                                                       |
| contact\_point = [wb\_supervisor\_node\_get\_contact\_point](supervisor.md#wb_supervisor_node_get_contact_point)(node, index)                                                                                        |
| number\_of\_contacts = [wb\_supervisor\_node\_get\_number\_of\_contact\_points](supervisor.md#wb_supervisor_node_get_number_of_contact_points)(index)                                                                |
| balance = [wb\_supervisor\_node\_get\_static\_balance](supervisor.md#wb_supervisor_node_get_static_balance)(node)                                                                                                    |
| velocity = [wb\_supervisor\_node\_get\_velocity](supervisor.md#wb_supervisor_node_get_velocity)(node)                                                                                                                |
| [wb\_supervisor\_node\_set\_velocity](supervisor.md#wb_supervisor_node_get_velocity)(node, velocity)                                                                                                                 |
| [wb\_supervisor\_node\_reset\_physics](supervisor.md#wb_supervisor_node_reset_physics)(node)                                                                                                                         |

<a name="matlab_touch_sensor"/>

| % [TouchSensor](touchsensor.md#touchsensor) :                                                       |
| --------------------------------------------------------------------------------------------------- |
| WB\_TOUCH\_SENSOR\_BUMPER, WB\_TOUCH\_SENSOR\_FORCE,                                                |
| WB\_TOUCH\_SENSOR\_FORCE3D                                                                          |
| [wb\_touch\_sensor\_enable](touchsensor.md#wb_touch_sensor_get_values)(tag, ms)                     |
| [wb\_touch\_sensor\_disable](touchsensor.md#wb_touch_sensor_get_values)(tag)                        |
| period = [wb\_touch\_sensor\_get\_sampling\_period](touchsensor.md#wb_touch_sensor_get_values)(tag) |
| value = [wb\_touch\_sensor\_get\_value](touchsensor.md#wb_touch_sensor_get_values)(tag)             |
| [x y z] = [wb\_touch\_sensor\_get\_values](touchsensor.md#wb_touch_sensor_get_values)(tag)          |
| type = [wb\_touch\_sensor\_get\_type](touchsensor.md#wb_touch_sensor_get_type)(tag)                 |

