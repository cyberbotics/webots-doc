## Python API

The following tables describe the Python classes and their methods.

%api "python_accelerometer"

|                                                                                                 |
| ----------------------------------------------------------------------------------------------- |
| from controller import Accelerometer                                                            |
| class [Accelerometer](accelerometer.md#accelerometer) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; def [enable](accelerometer.md#wb_accelerometer_get_values)(self, ms)               |
| &nbsp;&nbsp; def [disable](accelerometer.md#wb_accelerometer_get_values)(self)                  |
| &nbsp;&nbsp; def [getSamplingPeriod](accelerometer.md#wb_accelerometer_get_values)(self)        |
| &nbsp;&nbsp; def [getValues](accelerometer.md#wb_accelerometer_get_values)(self)                |

%end

%api "python_brake"

|                                                                                                      |
| ---------------------------------------------------------------------------------------------------- |
| from controller import Brake                                                                         |
| class [Brake](brake.md#brake) ([Device](python-api.md#python_device)) :                              |
| &nbsp;&nbsp; def [setDampingConstant](brake.md#wb_brake_set_damping_constant)(self, dampingConstant) |
| &nbsp;&nbsp; def [getType](brake.md#wb_brake_set_damping_constant)(self)                             |

%end

%api "python_camera"

|                                                                                                |
| ---------------------------------------------------------------------------------------------- |
| from controller import Camera                                                                  |
| class [Camera](camera.md#camera) ([Device](python-api.md#python_device)) :                     |
| &nbsp;&nbsp; COLOR, RANGE\_FINDER, BOTH                                                        |
| &nbsp;&nbsp; def [enable](camera.md#wb_camera_enable)(self, ms)                                |
| &nbsp;&nbsp; def [disable](camera.md#wb_camera_enable)(self)                                   |
| &nbsp;&nbsp; def [getSamplingPeriod](camera.md#wb_camera_enable)(self)                         |
| &nbsp;&nbsp; def [getFov](camera.md#wb_camera_get_fov)(self)                                   |
| &nbsp;&nbsp; def [getMinFov](camera.md#wb_camera_get_fov)(self)                                |
| &nbsp;&nbsp; def [getMaxFov](camera.md#wb_camera_get_fov)(self)                                |
| &nbsp;&nbsp; def [setFov](camera.md#wb_camera_get_fov)(self, fov)                              |
| &nbsp;&nbsp; def [getFocalLength](camera.md#wb_camera_get_focal_length)(self)                  |
| &nbsp;&nbsp; def [getFocalDistance](camera.md#wb_camera_get_focal_length)(self)                |
| &nbsp;&nbsp; def [getMaxFocalDistance](camera.md#wb_camera_get_focal_length)(self)             |
| &nbsp;&nbsp; def [getMinFocalDistance](camera.md#wb_camera_get_focal_length)(self)             |
| &nbsp;&nbsp; def [setFocalDistance](camera.md#wb_camera_get_focal_length)(self, focalDistance) |
| &nbsp;&nbsp; def [getWidth](camera.md#wb_camera_get_width)(self)                               |
| &nbsp;&nbsp; def [getHeight](camera.md#wb_camera_get_width)(self)                              |
| &nbsp;&nbsp; def [getNear](camera.md#wb_camera_get_near)(self)                                 |
| &nbsp;&nbsp; def [getMaxRange](camera.md#wb_camera_get_range_image)(self)                      |
| &nbsp;&nbsp; def [getType](camera.md#wb_camera_get_type)(self)                                 |
| &nbsp;&nbsp; def [getImage](camera.md#wb_camera_get_image)(self)                               |
| &nbsp;&nbsp; def [getImageArray](camera.md#wb_camera_get_image)(self)                          |
| &nbsp;&nbsp; def [imageGetRed](camera.md#wb_camera_get_image)(image, width, x, y)              |
| &nbsp;&nbsp; imageGetRed = staticmethod(imageGetRed)                                           |
| &nbsp;&nbsp; def [imageGetGreen](camera.md#wb_camera_get_image)(image, width, x, y)            |
| &nbsp;&nbsp; imageGetGreen = staticmethod(imageGetGreen)                                       |
| &nbsp;&nbsp; def [imageGetBlue](camera.md#wb_camera_get_image)(image, width, x, y)             |
| &nbsp;&nbsp; imageGetBlue = staticmethod(imageGetBlue)                                         |
| &nbsp;&nbsp; def [imageGetGrey](camera.md#wb_camera_get_image)(image, width, x, y)             |
| &nbsp;&nbsp; imageGetGrey = staticmethod(imageGetGrey)                                         |
| &nbsp;&nbsp; def [getRangeImage](camera.md#wb_camera_get_range_image)(self)                    |
| &nbsp;&nbsp; def [getRangeImageArray](camera.md#wb_camera_get_range_image)(self)               |
| &nbsp;&nbsp; def [rangeImageGetDepth](camera.md#wb_camera_get_range_image)(image, width, x, y) |
| &nbsp;&nbsp; rangeImageGetDepth = staticmethod(rangeImageGetDepth)                             |
| &nbsp;&nbsp; def [saveImage](camera.md#wb_camera_save_image)(self, filename, quality)          |

%end

%api "python_compass"

|                                                                               |
| ----------------------------------------------------------------------------- |
| from controller import Compass                                                |
| class [Compass](compass.md#compass) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; def [enable](compass.md#wb_compass_get_values)(self, ms)         |
| &nbsp;&nbsp; def [disable](compass.md#wb_compass_get_values)(self)            |
| &nbsp;&nbsp; def [getSamplingPeriod](compass.md#wb_compass_get_values)(self)  |
| &nbsp;&nbsp; def [getValues](compass.md#wb_compass_get_values)(self)          |

%end

%api "python_connector"

|                                                                                     |
| ----------------------------------------------------------------------------------- |
| from controller import Connector                                                    |
| class [Connector](connector.md#connector) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; def [enablePresence](connector.md#wb_connector_get_presence)(self, ms) |
| &nbsp;&nbsp; def [disablePresence](connector.md#wb_connector_get_presence)(self)    |
| &nbsp;&nbsp; def [getPresence](connector.md#wb_connector_get_presence)(self)        |
| &nbsp;&nbsp; def [lock](connector.md#wb_connector_lock)(self)                       |
| &nbsp;&nbsp; def [unlock](connector.md#wb_connector_lock)(self)                     |

%end

%api "python_device"

|                                                                         |
| ----------------------------------------------------------------------- |
| from controller import [Device](device.md#device)                       |
| class Device :                                                          |
| &nbsp;&nbsp; def [getModel](device.md#wb_device_get_model)(self)        |
| &nbsp;&nbsp; def [getName](device.md#wb_device_get_name)(self)          |
| &nbsp;&nbsp; def [getNodeType](device.md#wb_device_get_node_type)(self) |

%end

%api "python_differential_wheels"

|                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------- |
| from controller import DifferentialWheels                                                                        |
| class [DifferentialWheels](differentialwheels.md#differentialwheels) ([Robot](python-api.md#python_robot)) :     |
| &nbsp;&nbsp; def [\_\_init\_\_](robot.md#wb_robot_step)(self)                                                    |
| &nbsp;&nbsp; def [\_\_del\_\_](robot.md#wb_robot_step)(self)                                                     |
| &nbsp;&nbsp; def [setSpeed](differentialwheels.md#wb_differential_wheels_set_speed)(self, left, right)           |
| &nbsp;&nbsp; def [getLeftSpeed](differentialwheels.md#wb_differential_wheels_set_speed)(self)                    |
| &nbsp;&nbsp; def [getRightSpeed](differentialwheels.md#wb_differential_wheels_set_speed)(self)                   |
| &nbsp;&nbsp; def [enableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)(self, ms)        |
| &nbsp;&nbsp; def [disableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)(self)           |
| &nbsp;&nbsp; def [getEncodersSamplingPeriod](differentialwheels.md#wb_differential_wheels_enable_encoders)(self) |
| &nbsp;&nbsp; def [getLeftEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)(self)           |
| &nbsp;&nbsp; def [getRightEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)(self)          |
| &nbsp;&nbsp; def [setEncoders](differentialwheels.md#wb_differential_wheels_get_left_encoder)(self, left, right) |
| &nbsp;&nbsp; def [getMaxSpeed](differentialwheels.md#wb_differential_wheels_get_max_speed)(self)                 |
| &nbsp;&nbsp; def [getSpeedUnit](differentialwheels.md#wb_differential_wheels_get_speed_unit)(self)               |

%end

%api "python_display"

|                                                                                                   |
| ------------------------------------------------------------------------------------------------- |
| from controller import Display                                                                    |
| class [Display](display.md#display) ([Device](python-api.md#python_device)) :                     |
| &nbsp;&nbsp; RGB, RGBA, ARGB, BGRA                                                                |
| &nbsp;&nbsp; def [getWidth](display.md#wb_display_get_width)(self)                                |
| &nbsp;&nbsp; def [getHeight](display.md#wb_display_get_width)(self)                               |
| &nbsp;&nbsp; def [setColor](display.md#wb_display_set_context)(self, color)                       |
| &nbsp;&nbsp; def [setAlpha](display.md#wb_display_set_context)(self, alpha)                       |
| &nbsp;&nbsp; def [setOpacity](display.md#wb_display_set_context)(self, opacity)                   |
| &nbsp;&nbsp; def [drawPixel](display.md#wb_display_draw_primitive)(self, x1, y1)                  |
| &nbsp;&nbsp; def [drawLine](display.md#wb_display_draw_primitive)(self, x1, y1, x2, y2)           |
| &nbsp;&nbsp; def [drawRectangle](display.md#wb_display_draw_primitive)(self, x, y, width, height) |
| &nbsp;&nbsp; def [drawOval](display.md#wb_display_draw_primitive)(self, cx, cy, a, b)             |
| &nbsp;&nbsp; def [drawPolygon](display.md#wb_display_draw_primitive)(self, x, y)                  |
| &nbsp;&nbsp; def [drawText](display.md#wb_display_draw_primitive)(self, txt, x, y)                |
| &nbsp;&nbsp; def [fillRectangle](display.md#wb_display_draw_primitive)(self, x, y, width, height) |
| &nbsp;&nbsp; def [fillOval](display.md#wb_display_draw_primitive)(self, cx, cy, a, b)             |
| &nbsp;&nbsp; def [fillPolygon](display.md#wb_display_draw_primitive)(self, x, y)                  |
| &nbsp;&nbsp; def [imageCopy](display.md#wb_display_image_functions)(self, x, y, width, height)    |
| &nbsp;&nbsp; def [imagePaste](display.md#wb_display_image_functions)(self, ir, x, y)              |
| &nbsp;&nbsp; def [imageLoad](display.md#wb_display_image_functions)(self, filename)               |
| &nbsp;&nbsp; def [imageNew](display.md#wb_display_image_functions)(self, data, format)            |
| &nbsp;&nbsp; def [imageSave](display.md#wb_display_image_functions)(self, ir, filename)           |
| &nbsp;&nbsp; def [imageDelete](display.md#wb_display_image_functions)(self, ir)                   |

%end

%api "python_distance_sensor"

|                                                                                                    |
| -------------------------------------------------------------------------------------------------- |
| from controller import DistanceSensor                                                              |
| class [DistanceSensor](distancesensor.md#distancesensor) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; def [enable](distancesensor.md#wb_distance_sensor_get_value)(self, ms)                |
| &nbsp;&nbsp; def [disable](distancesensor.md#wb_distance_sensor_get_value)(self)                   |
| &nbsp;&nbsp; def [getSamplingPeriod](distancesensor.md#wb_distance_sensor_get_value)(self)         |
| &nbsp;&nbsp; def [getValue](distancesensor.md#wb_distance_sensor_get_value)(self)                  |

%end

%api "python_emitter"

|                                                                                 |
| ------------------------------------------------------------------------------- |
| from controller import Emitter                                                  |
| class [Emitter](emitter.md#emitter) ([Device](python-api.md#python_device)) :   |
| &nbsp;&nbsp; CHANNEL\_BROADCAST                                                 |
| &nbsp;&nbsp; def [send](emitter.md#wb_emitter_send)(self, data)                 |
| &nbsp;&nbsp; def [getChannel](emitter.md#wb_emitter_set_channel)(self)          |
| &nbsp;&nbsp; def [setChannel](emitter.md#wb_emitter_set_channel)(self, channel) |
| &nbsp;&nbsp; def [getRange](emitter.md#wb_emitter_set_range)(self)              |
| &nbsp;&nbsp; def [setRange](emitter.md#wb_emitter_set_range)(self, range)       |
| &nbsp;&nbsp; def [getBufferSize](emitter.md#wb_emitter_get_buffer_size)(self)   |

%end

%api "python_field"

|                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- |
| from controller import Field                                                                                            |
| class Field :                                                                                                           |
| &nbsp;&nbsp; SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F,                                                      |
| &nbsp;&nbsp; SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF,                                                         |
| &nbsp;&nbsp; MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR,                                                     |
| &nbsp;&nbsp; MF\_STRING, MF\_NODE                                                                                       |
| &nbsp;&nbsp; def [getType](supervisor.md#wb_supervisor_field_get)(self)                                                 |
| &nbsp;&nbsp; def [getTypeName](supervisor.md#wb_supervisor_field_get)(self)                                             |
| &nbsp;&nbsp; def [getCount](supervisor.md#wb_supervisor_field_get)(self)                                                |
| &nbsp;&nbsp; def [getSFBool](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                       |
| &nbsp;&nbsp; def [getSFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                   |
| &nbsp;&nbsp; def [getSFColor](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFString](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                     |
| &nbsp;&nbsp; def [getSFNode](supervisor.md#wb_supervisor_field_get_sf_bool)(self)                                       |
| &nbsp;&nbsp; def [getMFBool](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                                |
| &nbsp;&nbsp; def [getMFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                            |
| &nbsp;&nbsp; def [getMFColor](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFString](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                              |
| &nbsp;&nbsp; def [getMFNode](supervisor.md#wb_supervisor_field_get_sf_bool)(self, index)                                |
| &nbsp;&nbsp; def [setSFBool](supervisor.md#wb_supervisor_field_set_sf_bool)(self, value)                                |
| &nbsp;&nbsp; def [setSFInt32](supervisor.md#wb_supervisor_field_set_sf_bool)(self, value)                               |
| &nbsp;&nbsp; def [setSFFloat](supervisor.md#wb_supervisor_field_set_sf_bool)(self, value)                               |
| &nbsp;&nbsp; def [setSFVec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(self, values)                              |
| &nbsp;&nbsp; def [setSFVec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(self, values)                              |
| &nbsp;&nbsp; def [setSFRotation](supervisor.md#wb_supervisor_field_set_sf_bool)(self, values)                           |
| &nbsp;&nbsp; def [setSFColor](supervisor.md#wb_supervisor_field_set_sf_bool)(self, values)                              |
| &nbsp;&nbsp; def [setSFString](supervisor.md#wb_supervisor_field_set_sf_bool)(self, value)                              |
| &nbsp;&nbsp; def [setMFBool](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, value)                         |
| &nbsp;&nbsp; def [setMFInt32](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, value)                        |
| &nbsp;&nbsp; def [setMFFloat](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, value)                        |
| &nbsp;&nbsp; def [setMFVec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, values)                       |
| &nbsp;&nbsp; def [setMFVec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, values)                       |
| &nbsp;&nbsp; def [setMFRotation](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, values)                    |
| &nbsp;&nbsp; def [setMFColor](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, values)                       |
| &nbsp;&nbsp; def [setMFString](supervisor.md#wb_supervisor_field_set_sf_bool)(self, index, value)                       |
| &nbsp;&nbsp; def [importMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(self, position, filename)             |
| &nbsp;&nbsp; def [importMFNodeFromString](supervisor.md#wb_supervisor_field_import_mf_node)(self, position, nodeString) |
| &nbsp;&nbsp; def [removeMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(self, position)                       |

%end

%api "python_gps"

|                                                                      |
| -------------------------------------------------------------------- |
| from controller import GPS                                           |
| class [GPS](gps.md#gps) ([Device](python-api.md#python_device)) :    |
| &nbsp;&nbsp; def [enable](gps.md#wb_gps_get_values)(self, ms)        |
| &nbsp;&nbsp; def [disable](gps.md#wb_gps_get_values)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](gps.md#wb_gps_get_values)(self) |
| &nbsp;&nbsp; def [getValues](gps.md#wb_gps_get_values)(self)         |

%end

%api "python_gyro"

|                                                                        |
| ---------------------------------------------------------------------- |
| from controller import Gyro                                            |
| class [Gyro](gyro.md#gyro) ([Device](python-api.md#python_device)) :   |
| &nbsp;&nbsp; def [enable](gyro.md#wb_gyro_get_values)(self, ms)        |
| &nbsp;&nbsp; def [disable](gyro.md#wb_gyro_get_values)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](gyro.md#wb_gyro_get_values)(self) |
| &nbsp;&nbsp; def [getValues](gyro.md#wb_gyro_get_values)(self)         |

%end

%api "python_image_ref"

|                                 |
| ------------------------------- |
| from controller import ImageRef |
| class ImageRef :                |

%end

%api "python_inertial_unit"

|                                                                                                 |
| ----------------------------------------------------------------------------------------------- |
| from controller import InertialUnit                                                             |
| class [InertialUnit](inertialunit.md#inertialunit) ([Device](python-api.md#python_device)) :    |
| &nbsp;&nbsp; def [enable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(self, ms)        |
| &nbsp;&nbsp; def [disable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(self) |
| &nbsp;&nbsp; def [getRollPitchYaw](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(self)   |

%end

%api "python_led"

|                                                                   |
| ----------------------------------------------------------------- |
| from controller import LED                                        |
| class [LED](led.md#led) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; def [set](led.md#wb_led_set)(self, state)            |
| &nbsp;&nbsp; def [get](led.md#wb_led_set)(self)                   |

%end

%api "python_light_sensor"

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| from controller import LightSensor                                                        |
| class [LightSensor](lightsensor.md#lightsensor) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; def [enable](lightsensor.md#wb_light_sensor_get_value)(self, ms)             |
| &nbsp;&nbsp; def [disable](lightsensor.md#wb_light_sensor_get_value)(self)                |
| &nbsp;&nbsp; def [getSamplingPeriod](lightsensor.md#wb_light_sensor_get_value)(self)      |
| &nbsp;&nbsp; def [getValue](lightsensor.md#wb_light_sensor_get_value)(self)               |

%end

%api "python_motion"

|                                                                           |
| ------------------------------------------------------------------------- |
| from controller import Motion                                             |
| class [Motion](motion.md#motion) :                                        |
| &nbsp;&nbsp; def [\_\_init\_\_](motion.md#wbu_motion_new)(self, fileName) |
| &nbsp;&nbsp; def [\_\_del\_\_](motion.md#wbu_motion_new)(self)            |
| &nbsp;&nbsp; def [isValid](motion.md#wbu_motion_new)(self)                |
| &nbsp;&nbsp; def [play](motion.md#wbu_motion_play)(self)                  |
| &nbsp;&nbsp; def [stop](motion.md#wbu_motion_play)(self)                  |
| &nbsp;&nbsp; def [setLoop](motion.md#wbu_motion_play)(self, loop)         |
| &nbsp;&nbsp; def [setReverse](motion.md#wbu_motion_play)(self, reverse)   |
| &nbsp;&nbsp; def [isOver](motion.md#wbu_motion_is_over)(self)             |
| &nbsp;&nbsp; def [getDuration](motion.md#wbu_motion_is_over)(self)        |
| &nbsp;&nbsp; def [getTime](motion.md#wbu_motion_is_over)(self)            |
| &nbsp;&nbsp; def [setTime](motion.md#wbu_motion_is_over)(self, time)      |

%end

%api "python_motor"

|                                                                                                   |
| ------------------------------------------------------------------------------------------------- |
| from controller import Motor                                                                      |
| class [Motor](motor.md#motor) ([Device](python-api.md#python_device)) :                           |
| &nbsp;&nbsp; ROTATIONAL, LINEAR                                                                   |
| &nbsp;&nbsp; def [setPosition](motor.md#wb_motor_set_position)(self, position)                    |
| &nbsp;&nbsp; def [setVelocity](motor.md#wb_motor_set_position)(self, vel)                         |
| &nbsp;&nbsp; def [setAcceleration](motor.md#wb_motor_set_position)(self, force)                   |
| &nbsp;&nbsp; def [setAvailableForce](motor.md#wb_motor_set_position)(self, motor\_force)          |
| &nbsp;&nbsp; def [setAvailableTorque](motor.md#wb_motor_set_position)(self, motor\_torque)        |
| &nbsp;&nbsp; def [setControlPID](motor.md#wb_motor_set_position)(self, p, i, d)                   |
| &nbsp;&nbsp; def [getTargetPosition](motor.md#wb_motor_set_position)(self)                        |
| &nbsp;&nbsp; def [getMinPosition](motor.md#wb_motor_set_position)(self)                           |
| &nbsp;&nbsp; def [getMaxPosition](motor.md#wb_motor_set_position)(self)                           |
| &nbsp;&nbsp; def [getVelocity](motor.md#wb_motor_set_position)(self)                              |
| &nbsp;&nbsp; def [getMaxVelocity](motor.md#wb_motor_set_position)(self)                           |
| &nbsp;&nbsp; def [getAcceleration](motor.md#wb_motor_set_position)(self)                          |
| &nbsp;&nbsp; def [getAvailableForce](motor.md#wb_motor_set_position)(self)                        |
| &nbsp;&nbsp; def [getMaxForce](motor.md#wb_motor_set_position)(self)                              |
| &nbsp;&nbsp; def [getAvailableTorque](motor.md#wb_motor_set_position)(self)                       |
| &nbsp;&nbsp; double [getMaxTorque](motor.md#wb_motor_set_position)(self)                          |
| &nbsp;&nbsp; def [enableForceFeedback](motor.md#wb_motor_enable_force_feedback)(self, ms)         |
| &nbsp;&nbsp; def [disableForceFeedback](motor.md#wb_motor_enable_force_feedback)(self)            |
| &nbsp;&nbsp; def [getForceFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)(self)  |
| &nbsp;&nbsp; def [getForceFeedback](motor.md#wb_motor_enable_force_feedback)(self)                |
| &nbsp;&nbsp; def [setForce](motor.md#wb_motor_set_force)(self, torque)                            |
| &nbsp;&nbsp; def [enableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)(self, ms)        |
| &nbsp;&nbsp; def [disableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)(self)           |
| &nbsp;&nbsp; def [getTorqueFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)(self) |
| &nbsp;&nbsp; def [getTorqueFeedback](motor.md#wb_motor_enable_force_feedback)(self)               |
| &nbsp;&nbsp; def [setTorque](motor.md#wb_motor_set_force)(self, torque)                           |
| &nbsp;&nbsp; def [getType](motor.md#wb_motor_get_type)(self)                                      |

%end

%api "python_node"

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from controller import Node                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| class Node :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; NO\_NODE, ACCELEROMETER, APPEARANCE, BACKGROUND, BALL\_JOINT, BALL\_JOINT\_PARAMETERS, BOX, BRAKE, CAMERA, CAMERA\_FOCUS, CAMERA\_LENS\_DISTORTION, CAMERA\_ZOOM, CAPSULE, CHARGER, COLOR, COMPASS, CONE, CONNECTOR, CONTACT\_PROPERTIES, COORDINATE, CYLINDER, DAMPING, DIFFERENTIAL\_WHEELS, DIRECTIONAL\_LIGHT, DISPLAY, DISTANCE\_SENSOR, ELEVATION\_GRID, EMITTER, EXTRUSION, FLUID, FOG, GPS, GROUP, GYRO, HINGE\_2\_JOINT, HINGE\_2\_JOINT\_PARAMETERS, HINGE\_JOINT, HINGE\_JOINT\_PARAMETERS, IMAGE\_TEXTURE, IMMERSION\_PROPERTIES, INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, INERTIAL\_UNIT, JOINT\_PARAMETERS, LED, LIGHT\_SENSOR, LINEAR\_MOTOR, MATERIAL, MICROPHONE, PEN, PHYSICS, PLANE, POINT\_LIGHT, POSITION\_SENSOR, PROPELLER, RADIO, RECEIVER, ROBOT, ROTATIONAL\_MOTOR, SERVO, SHAPE, SLIDER\_JOINT, SLOT, SOLID, SOLID\_REFERENCE, SPEAKER, SPHERE, SPOT\_LIGHT, SUPERVISOR, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, TOUCH\_SENSOR, TRACK, TRACK\_WHEEL, TRANSFORM, VIEWPOINT, WORLD\_INFO |
| &nbsp;&nbsp; def [remove](supervisor.md#wb_supervisor_node_remove)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &nbsp;&nbsp; def [getType](supervisor.md#wb_supervisor_node_get_type)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; def [getId](supervisor.md#wb_supervisor_node_get_from_def)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &nbsp;&nbsp; def [getTypeName](supervisor.md#wb_supervisor_node_get_type)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| &nbsp;&nbsp; def [getBaseTypeName](supervisor.md#wb_supervisor_node_get_type)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; def [getField](supervisor.md#wb_supervisor_node_get_field)(self, fieldName)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &nbsp;&nbsp; def [getParentNode](supervisor.md#wb_supervisor_node_get_from_def)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| &nbsp;&nbsp; def [getPosition](supervisor.md#wb_supervisor_node_get_position)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; def [getOrientation](supervisor.md#wb_supervisor_node_get_position)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; def [getCenterOfMass](supervisor.md#wb_supervisor_node_get_center_of_mass)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &nbsp;&nbsp; def [getContactPoint](supervisor.md#wb_supervisor_node_get_contact_point)(self, index)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; def [getNumberOfContactPoints](supervisor.md#wb_supervisor_node_get_number_of_contact_points)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp; def [getStaticBalance](supervisor.md#wb_supervisor_node_get_static_balance)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &nbsp;&nbsp; def [getVelocity](supervisor.md#wb_supervisor_node_get_velocity)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; def [setVelocity](supervisor.md#wb_supervisor_node_get_velocity)(self, velocity)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &nbsp;&nbsp; def [resetPhysics](supervisor.md#wb_supervisor_node_reset_physics)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

%end

%api "python_pen"

|                                                                                   |
| --------------------------------------------------------------------------------- |
| from controller import Pen                                                        |
| class [Pen](pen.md#pen) ([Device](python-api.md#python_device)) :                 |
| &nbsp;&nbsp; def [write](pen.md#wb_pen_write)(self, write)                        |
| &nbsp;&nbsp; def [setInkColor](pen.md#wb_pen_set_ink_color)(self, color, density) |

%end

%api "python_position_sensor"

|                                                                                                    |
| -------------------------------------------------------------------------------------------------- |
| from controller import PositionSensor                                                              |
| class [PositionSensor](positionsensor.md#positionsensor) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; ANGULAR, LINEAR                                                                       |
| &nbsp;&nbsp; def [enable](positionsensor.md#wb_position_sensor_get_value)(self, ms)                |
| &nbsp;&nbsp; def [disable](positionsensor.md#wb_position_sensor_get_value)(self)                   |
| &nbsp;&nbsp; def [getSamplingPeriod](positionsensor.md#wb_position_sensor_get_value)(self)         |
| &nbsp;&nbsp; def [getValue](positionsensor.md#wb_position_sensor_get_value)(self)                  |
| &nbsp;&nbsp; def [getType](positionsensor.md#wb_position_sensor_get_value)(self)                   |

%end

%api "python_receiver"

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| from controller import Receiver                                                           |
| class [Receiver](receiver.md#receiver) ([Device](python-api.md#python_device)) :          |
| &nbsp;&nbsp; CHANNEL\_BROADCAST                                                           |
| &nbsp;&nbsp; def [enable](receiver.md#wb_receiver_enable)(self, ms)                       |
| &nbsp;&nbsp; def [disable](receiver.md#wb_receiver_enable)(self)                          |
| &nbsp;&nbsp; def [getSamplingPeriod](receiver.md#wb_receiver_enable)(self)                |
| &nbsp;&nbsp; def [getQueueLength](receiver.md#wb_receiver_get_queue_length)(self)         |
| &nbsp;&nbsp; def [nextPacket](receiver.md#wb_receiver_get_queue_length)(self)             |
| &nbsp;&nbsp; def [getData](receiver.md#wb_receiver_get_data)(self)                        |
| &nbsp;&nbsp; def [getDataSize](receiver.md#wb_receiver_get_data)(self)                    |
| &nbsp;&nbsp; def [getSignalStrength](receiver.md#wb_receiver_get_signal_strength)(self)   |
| &nbsp;&nbsp; def [getEmitterDirection](receiver.md#wb_receiver_get_signal_strength)(self) |
| &nbsp;&nbsp; def [setChannel](receiver.md#wb_receiver_set_channel)(self, channel)         |
| &nbsp;&nbsp; def [getChannel](receiver.md#wb_receiver_set_channel)(self)                  |

%end

%api "python_robot"

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| from controller import Robot                                                                     |
| class [Robot](robot.md#robot) :                                                                  |
| &nbsp;&nbsp; MODE\_SIMULATION, MODE\_CROSS\_COMPILATION,                                         |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL                                                               |
| &nbsp;&nbsp; KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT, KEYBOARD\_UP,                        |
| &nbsp;&nbsp; KEYBOARD\_RIGHT, KEYBOARD\_DOWN, KEYBOARD\_PAGEUP,                                  |
| &nbsp;&nbsp; KEYBOARD\_PAGEDOWN, KEYBOARD\_NUMPAD\_HOME,                                         |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_LEFT, KEYBOARD\_NUMPAD\_UP,                                       |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_RIGHT, KEYBOARD\_NUMPAD\_DOWN,                                    |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_END, KEYBOARD\_KEY, KEYBOARD\_SHIFT,                              |
| &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT                                                    |
| &nbsp;&nbsp; def [\_\_init\_\_](robot.md#wb_robot_step)(self)                                    |
| &nbsp;&nbsp; def [\_\_del\_\_](robot.md#wb_robot_step)(self)                                     |
| &nbsp;&nbsp; def [step](robot.md#wb_robot_step)(self, ms)                                        |
| &nbsp;&nbsp; def [getAccelerometer](robot.md#robotgetdevice)(self, name)                         |
| &nbsp;&nbsp; def [getBrake](robot.md#robotgetdevice)(self, name)                                 |
| &nbsp;&nbsp; def [getCamera](robot.md#robotgetdevice)(self, name)                                |
| &nbsp;&nbsp; def [getCompass](robot.md#robotgetdevice)(self, name)                               |
| &nbsp;&nbsp; def [getConnector](robot.md#robotgetdevice)(self, name)                             |
| &nbsp;&nbsp; def [getDisplay](robot.md#robotgetdevice)(self, name)                               |
| &nbsp;&nbsp; def [getDistanceSensor](robot.md#robotgetdevice)(self, name)                        |
| &nbsp;&nbsp; def [getEmitter](robot.md#robotgetdevice)(self, name)                               |
| &nbsp;&nbsp; def [getGPS](robot.md#robotgetdevice)(self, name)                                   |
| &nbsp;&nbsp; def [getGyro](robot.md#robotgetdevice)(self, name)                                  |
| &nbsp;&nbsp; def [getInertialUnit](robot.md#robotgetdevice)(self, name)                          |
| &nbsp;&nbsp; def [getLED](robot.md#robotgetdevice)(self, name)                                   |
| &nbsp;&nbsp; def [getLightSensor](robot.md#robotgetdevice)(self, name)                           |
| &nbsp;&nbsp; def [getMotor](robot.md#robotgetdevice)(self, name)                                 |
| &nbsp;&nbsp; def [getPen](robot.md#robotgetdevice)(self, name)                                   |
| &nbsp;&nbsp; def [getPositionSensor](robot.md#robotgetdevice)(self, name)                        |
| &nbsp;&nbsp; def [getReceiver](robot.md#robotgetdevice)(self, name)                              |
| &nbsp;&nbsp; def [getServo](robot.md#robotgetdevice)(self, name)                                 |
| &nbsp;&nbsp; def [getTouchSensor](robot.md#robotgetdevice)(self, name)                           |
| &nbsp;&nbsp; def [getNumberOfDevices](robot.md#wb_robot_get_device_by_index)(self)               |
| &nbsp;&nbsp; def [getDeviceByIndex](robot.md#wb_robot_get_device_by_index)(self, index)          |
| &nbsp;&nbsp; def [batterySensorEnable](robot.md#wb_robot_battery_sensor_enable)(self, ms)        |
| &nbsp;&nbsp; def [batterySensorDisable](robot.md#wb_robot_battery_sensor_enable)(self)           |
| &nbsp;&nbsp; def [batterySensorGetSamplingPeriod](robot.md#wb_robot_battery_sensor_enable)(self) |
| &nbsp;&nbsp; def [batterySensorGetValue](robot.md#wb_robot_battery_sensor_enable)(self)          |
| &nbsp;&nbsp; def [getBasicTimeStep](robot.md#wb_robot_get_basic_time_step)(self)                 |
| &nbsp;&nbsp; def [getMode](robot.md#wb_robot_get_mode)(self)                                     |
| &nbsp;&nbsp; def [getModel](robot.md#wb_robot_get_model)(self)                                   |
| &nbsp;&nbsp; def [getData](robot.md#wb_robot_get_data)(self)                                     |
| &nbsp;&nbsp; def [setData](robot.md#wb_robot_get_data)(self, data)                               |
| &nbsp;&nbsp; def [getName](robot.md#wb_robot_get_name)(self)                                     |
| &nbsp;&nbsp; def [getControllerName](robot.md#wb_robot_get_controller_name)(self)                |
| &nbsp;&nbsp; def [getControllerArguments](robot.md#wb_robot_get_controller_name)(self)           |
| &nbsp;&nbsp; def [getProjectPath](robot.md#wb_robot_get_project_path)(self)                      |
| &nbsp;&nbsp; def [getSynchronization](robot.md#wb_robot_get_synchronization)(self)               |
| &nbsp;&nbsp; def [getTime](robot.md#wb_robot_get_time)(self)                                     |
| &nbsp;&nbsp; def [getWorldPath](robot.md#wb_robot_get_world_path)(self)                          |
| &nbsp;&nbsp; def [keyboardEnable](robot.md#wb_robot_keyboard_enable)(self, ms)                   |
| &nbsp;&nbsp; def [keyboardDisable](robot.md#wb_robot_keyboard_enable)(self)                      |
| &nbsp;&nbsp; def [keyboardGetKey](robot.md#wb_robot_keyboard_enable)(self)                       |
| &nbsp;&nbsp; def [getType](robot.md#wb_robot_get_type)(self)                                     |

%end

%api "python_servo"

|                                                                                                             |
| ----------------------------------------------------------------------------------------------------------- |
| from controller import Servo                                                                                |
| class [Servo](servo.md#servo) ([Device](python-api.md#python_device)) :                                     |
| &nbsp;&nbsp; ROTATIONAL, LINEAR                                                                             |
| &nbsp;&nbsp; def [setPosition](servo.md#wb_servo_set_position)(self, position)                              |
| &nbsp;&nbsp; def [getTargetPosition](servo.md#wb_servo_set_position)(self)                                  |
| &nbsp;&nbsp; def [setVelocity](servo.md#wb_servo_set_position)(self, vel)                                   |
| &nbsp;&nbsp; def [setAcceleration](servo.md#wb_servo_set_position)(self, force)                             |
| &nbsp;&nbsp; def [setMotorForce](servo.md#wb_servo_set_position)(self, motor\_force)                        |
| &nbsp;&nbsp; def [setControlP](servo.md#wb_servo_set_position)(self, p)                                     |
| &nbsp;&nbsp; def [getMinPosition](servo.md#wb_servo_set_position)(self)                                     |
| &nbsp;&nbsp; def [getMaxPosition](servo.md#wb_servo_set_position)(self)                                     |
| &nbsp;&nbsp; def [enablePosition](servo.md#wb_servo_enable_position)(self, ms)                              |
| &nbsp;&nbsp; def [disablePosition](servo.md#wb_servo_enable_position)(self)                                 |
| &nbsp;&nbsp; def [getPositionSamplingPeriod](servo.md#wb_servo_enable_position)(self)                       |
| &nbsp;&nbsp; def [getPosition](servo.md#wb_servo_enable_position)(self)                                     |
| &nbsp;&nbsp; def [enableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)(self, ms)        |
| &nbsp;&nbsp; def [disableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)(self)           |
| &nbsp;&nbsp; def [getMotorForceFeedbackSamplingPeriod](servo.md#wb_servo_enable_motor_force_feedback)(self) |
| &nbsp;&nbsp; def [getMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)(self)               |
| &nbsp;&nbsp; def [setForce](servo.md#wb_servo_set_force)(self, force)                                       |
| &nbsp;&nbsp; def [getType](servo.md#wb_servo_get_type)(self)                                                |

%end

%api "python_supervisor"

|                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from controller import Supervisor                                                                                                                           |
| class [Supervisor](supervisor.md#supervisor) ([Robot](python-api.md#python_robot)) :                                                                        |
| &nbsp;&nbsp; MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR                           |
| &nbsp;&nbsp; def [\_\_init\_\_](robot.md#wb_robot_step)(self)                                                                                               |
| &nbsp;&nbsp; def [\_\_del\_\_](robot.md#wb_robot_step)(self)                                                                                                |
| &nbsp;&nbsp; def [exportImage](supervisor.md#wb_supervisor_export_image)(self, file, quality)                                                               |
| &nbsp;&nbsp; def [getRoot](supervisor.md#wb_supervisor_node_get_from_def)(self)                                                                             |
| &nbsp;&nbsp; def [getSelf](supervisor.md#wb_supervisor_node_get_from_def)(self)                                                                             |
| &nbsp;&nbsp; def [getFromDef](supervisor.md#wb_supervisor_node_get_from_def)(self, name)                                                                    |
| &nbsp;&nbsp; def [getFromId](supervisor.md#wb_supervisor_node_get_from_def)(self, id)                                                                       |
| &nbsp;&nbsp; def [setLabel](supervisor.md#wb_supervisor_set_label)(self, id, label, xpos, ypos, size, color, transparency)                                  |
| &nbsp;&nbsp; def [simulationQuit](supervisor.md#wb_supervisor_simulation_quit)(self, status)                                                                |
| &nbsp;&nbsp; def [simulationRevert](supervisor.md#wb_supervisor_simulation_revert)(self)                                                                    |
| &nbsp;&nbsp; def [simulationResetPhysics](supervisor.md#wb_supervisor_simulation_reset_physics)(self)                                                       |
| &nbsp;&nbsp; def [loadWorld](supervisor.md#wb_supervisor_load_world)(self, file)                                                                            |
| &nbsp;&nbsp; def [saveWorld](supervisor.md#wb_supervisor_load_world)(self)                                                                                  |
| &nbsp;&nbsp; def [saveWorld](supervisor.md#wb_supervisor_load_world)(self, file)                                                                            |
| &nbsp;&nbsp; def [movieStartRecording](supervisor.md#wb_supervisor_movie_start_recording)(self, file, width, height, codec, quality, acceleration, caption) |
| &nbsp;&nbsp; def [movieStopRecording](supervisor.md#wb_supervisor_movie_start_recording)(self)                                                              |
| &nbsp;&nbsp; def [movieGetStatus](supervisor.md#wb_supervisor_movie_start_recording)(self)                                                                  |
| &nbsp;&nbsp; def [animationStartRecording](supervisor.md#wb_supervisor_animation_start_recording)(self, file)                                               |
| &nbsp;&nbsp; def [animationStopRecording](supervisor.md#wb_supervisor_animation_start_recording)(self)                                                      |

%end

%api "python_touch_sensor"

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| from controller import TouchSensor                                                        |
| class [TouchSensor](touchsensor.md#touchsensor) ([Device](python-api.md#python_device)) : |
| &nbsp;&nbsp; BUMPER, FORCE, FORCE3D                                                       |
| &nbsp;&nbsp; def [enable](touchsensor.md#wb_touch_sensor_get_values)(self, ms)            |
| &nbsp;&nbsp; def [disable](touchsensor.md#wb_touch_sensor_get_values)(self)               |
| &nbsp;&nbsp; def [getSamplingPeriod](touchsensor.md#wb_touch_sensor_get_values)(self)     |
| &nbsp;&nbsp; def [getValue](touchsensor.md#wb_touch_sensor_get_values)(self)              |
| &nbsp;&nbsp; def [getValues](touchsensor.md#wb_touch_sensor_get_values)(self)             |
| &nbsp;&nbsp; def [getType](touchsensor.md#wb_touch_sensor_get_type)(self)                 |

%end

