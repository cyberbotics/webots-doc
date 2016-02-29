## Python API

The following tables describe the Python classes and their methods.

%api "python_accelerometer"

|                                                                          |
| ------------------------------------------------------------------------ |
| from controller import Accelerometer                                     |
| class [Accelerometer](#accelerometer) ([Device](#python_device)) :       |
| &nbsp;&nbsp; def [enable](#wb_accelerometer_get_values)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_accelerometer_get_values)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_accelerometer_get_values)(self) |
| &nbsp;&nbsp; def [getValues](#wb_accelerometer_get_values)(self)         |

%end

%api "python_brake"

|                                                                                              |
| -------------------------------------------------------------------------------------------- |
| from controller import Brake                                                                 |
| class [Brake](#brake) ([Device](#python_device)) :                                           |
| &nbsp;&nbsp; def [setDampingConstant](#wb_brake_set_damping_constant)(self, dampingConstant) |
| &nbsp;&nbsp; def [getType](#wb_brake_set_damping_constant)(self)                             |

%end

%api "python_camera"

|                                                                                       |
| ------------------------------------------------------------------------------------- |
| from controller import Camera                                                         |
| class [Camera](#camera) ([Device](#python_device)) :                                  |
| &nbsp;&nbsp; COLOR, RANGE\_FINDER, BOTH                                               |
| &nbsp;&nbsp; def [enable](#wb_camera_enable)(self, ms)                                |
| &nbsp;&nbsp; def [disable](#wb_camera_enable)(self)                                   |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_camera_enable)(self)                         |
| &nbsp;&nbsp; def [getFov](#wb_camera_get_fov)(self)                                   |
| &nbsp;&nbsp; def [getMinFov](#wb_camera_get_fov)(self)                                |
| &nbsp;&nbsp; def [getMaxFov](#wb_camera_get_fov)(self)                                |
| &nbsp;&nbsp; def [setFov](#wb_camera_get_fov)(self, fov)                              |
| &nbsp;&nbsp; def [getFocalLength](#wb_camera_get_focal_length)(self)                  |
| &nbsp;&nbsp; def [getFocalDistance](#wb_camera_get_focal_length)(self)                |
| &nbsp;&nbsp; def [getMaxFocalDistance](#wb_camera_get_focal_length)(self)             |
| &nbsp;&nbsp; def [getMinFocalDistance](#wb_camera_get_focal_length)(self)             |
| &nbsp;&nbsp; def [setFocalDistance](#wb_camera_get_focal_length)(self, focalDistance) |
| &nbsp;&nbsp; def [getWidth](#wb_camera_get_width)(self)                               |
| &nbsp;&nbsp; def [getHeight](#wb_camera_get_width)(self)                              |
| &nbsp;&nbsp; def [getNear](#wb_camera_get_near)(self)                                 |
| &nbsp;&nbsp; def [getMaxRange](#wb_camera_get_range_image)(self)                      |
| &nbsp;&nbsp; def [getType](#wb_camera_get_type)(self)                                 |
| &nbsp;&nbsp; def [getImage](#wb_camera_get_image)(self)                               |
| &nbsp;&nbsp; def [getImageArray](#wb_camera_get_image)(self)                          |
| &nbsp;&nbsp; def [imageGetRed](#wb_camera_get_image)(image, width, x, y)              |
| &nbsp;&nbsp; imageGetRed = staticmethod(imageGetRed)                                  |
| &nbsp;&nbsp; def [imageGetGreen](#wb_camera_get_image)(image, width, x, y)            |
| &nbsp;&nbsp; imageGetGreen = staticmethod(imageGetGreen)                              |
| &nbsp;&nbsp; def [imageGetBlue](#wb_camera_get_image)(image, width, x, y)             |
| &nbsp;&nbsp; imageGetBlue = staticmethod(imageGetBlue)                                |
| &nbsp;&nbsp; def [imageGetGrey](#wb_camera_get_image)(image, width, x, y)             |
| &nbsp;&nbsp; imageGetGrey = staticmethod(imageGetGrey)                                |
| &nbsp;&nbsp; def [getRangeImage](#wb_camera_get_range_image)(self)                    |
| &nbsp;&nbsp; def [getRangeImageArray](#wb_camera_get_range_image)(self)               |
| &nbsp;&nbsp; def [rangeImageGetDepth](#wb_camera_get_range_image)(image, width, x, y) |
| &nbsp;&nbsp; rangeImageGetDepth = staticmethod(rangeImageGetDepth)                    |
| &nbsp;&nbsp; def [saveImage](#wb_camera_save_image)(self, filename, quality)          |

%end

%api "python_compass"

|                                                                    |
| ------------------------------------------------------------------ |
| from controller import Compass                                     |
| class [Compass](#compass) ([Device](#python_device)) :             |
| &nbsp;&nbsp; def [enable](#wb_compass_get_values)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_compass_get_values)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_compass_get_values)(self) |
| &nbsp;&nbsp; def [getValues](#wb_compass_get_values)(self)         |

%end

%api "python_connector"

|                                                                         |
| ----------------------------------------------------------------------- |
| from controller import Connector                                        |
| class [Connector](#connector) ([Device](#python_device)) :              |
| &nbsp;&nbsp; def [enablePresence](#wb_connector_get_presence)(self, ms) |
| &nbsp;&nbsp; def [disablePresence](#wb_connector_get_presence)(self)    |
| &nbsp;&nbsp; def [getPresence](#wb_connector_get_presence)(self)        |
| &nbsp;&nbsp; def [lock](#wb_connector_lock)(self)                       |
| &nbsp;&nbsp; def [unlock](#wb_connector_lock)(self)                     |

%end

%api "python_device"

|                                                                |
| -------------------------------------------------------------- |
| from controller import [Device](#device)                       |
| class Device :                                                 |
| &nbsp;&nbsp; def [getModel](#wb_device_get_model)(self)        |
| &nbsp;&nbsp; def [getName](#wb_device_get_name)(self)          |
| &nbsp;&nbsp; def [getNodeType](#wb_device_get_node_type)(self) |

%end

%api "python_differential_wheels"

|                                                                                             |
| ------------------------------------------------------------------------------------------- |
| from controller import DifferentialWheels                                                   |
| class [DifferentialWheels](#differentialwheels) ([Robot](#python_robot)) :                  |
| &nbsp;&nbsp; def [\_\_init\_\_](#wb_robot_step)(self)                                       |
| &nbsp;&nbsp; def [\_\_del\_\_](#wb_robot_step)(self)                                        |
| &nbsp;&nbsp; def [setSpeed](#wb_differential_wheels_set_speed)(self, left, right)           |
| &nbsp;&nbsp; def [getLeftSpeed](#wb_differential_wheels_set_speed)(self)                    |
| &nbsp;&nbsp; def [getRightSpeed](#wb_differential_wheels_set_speed)(self)                   |
| &nbsp;&nbsp; def [enableEncoders](#wb_differential_wheels_enable_encoders)(self, ms)        |
| &nbsp;&nbsp; def [disableEncoders](#wb_differential_wheels_enable_encoders)(self)           |
| &nbsp;&nbsp; def [getEncodersSamplingPeriod](#wb_differential_wheels_enable_encoders)(self) |
| &nbsp;&nbsp; def [getLeftEncoder](#wb_differential_wheels_get_left_encoder)(self)           |
| &nbsp;&nbsp; def [getRightEncoder](#wb_differential_wheels_get_left_encoder)(self)          |
| &nbsp;&nbsp; def [setEncoders](#wb_differential_wheels_get_left_encoder)(self, left, right) |
| &nbsp;&nbsp; def [getMaxSpeed](#wb_differential_wheels_get_max_speed)(self)                 |
| &nbsp;&nbsp; def [getSpeedUnit](#wb_differential_wheels_get_speed_unit)(self)               |

%end

%api "python_display"

|                                                                                         |
| --------------------------------------------------------------------------------------- |
| from controller import Display                                                          |
| class [Display](#display) ([Device](#python_device)) :                                  |
| &nbsp;&nbsp; RGB, RGBA, ARGB, BGRA                                                      |
| &nbsp;&nbsp; def [getWidth](#wb_display_get_width)(self)                                |
| &nbsp;&nbsp; def [getHeight](#wb_display_get_width)(self)                               |
| &nbsp;&nbsp; def [setColor](#wb_display_set_context)(self, color)                       |
| &nbsp;&nbsp; def [setAlpha](#wb_display_set_context)(self, alpha)                       |
| &nbsp;&nbsp; def [setOpacity](#wb_display_set_context)(self, opacity)                   |
| &nbsp;&nbsp; def [drawPixel](#wb_display_draw_primitive)(self, x1, y1)                  |
| &nbsp;&nbsp; def [drawLine](#wb_display_draw_primitive)(self, x1, y1, x2, y2)           |
| &nbsp;&nbsp; def [drawRectangle](#wb_display_draw_primitive)(self, x, y, width, height) |
| &nbsp;&nbsp; def [drawOval](#wb_display_draw_primitive)(self, cx, cy, a, b)             |
| &nbsp;&nbsp; def [drawPolygon](#wb_display_draw_primitive)(self, x, y)                  |
| &nbsp;&nbsp; def [drawText](#wb_display_draw_primitive)(self, txt, x, y)                |
| &nbsp;&nbsp; def [fillRectangle](#wb_display_draw_primitive)(self, x, y, width, height) |
| &nbsp;&nbsp; def [fillOval](#wb_display_draw_primitive)(self, cx, cy, a, b)             |
| &nbsp;&nbsp; def [fillPolygon](#wb_display_draw_primitive)(self, x, y)                  |
| &nbsp;&nbsp; def [imageCopy](#wb_display_image_functions)(self, x, y, width, height)    |
| &nbsp;&nbsp; def [imagePaste](#wb_display_image_functions)(self, ir, x, y)              |
| &nbsp;&nbsp; def [imageLoad](#wb_display_image_functions)(self, filename)               |
| &nbsp;&nbsp; def [imageNew](#wb_display_image_functions)(self, data, format)            |
| &nbsp;&nbsp; def [imageSave](#wb_display_image_functions)(self, ir, filename)           |
| &nbsp;&nbsp; def [imageDelete](#wb_display_image_functions)(self, ir)                   |

%end

%api "python_distance_sensor"

|                                                                           |
| ------------------------------------------------------------------------- |
| from controller import DistanceSensor                                     |
| class [DistanceSensor](#distancesensor) ([Device](#python_device)) :      |
| &nbsp;&nbsp; def [enable](#wb_distance_sensor_get_value)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_distance_sensor_get_value)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_distance_sensor_get_value)(self) |
| &nbsp;&nbsp; def [getValue](#wb_distance_sensor_get_value)(self)          |

%end

%api "python_emitter"

|                                                                       |
| --------------------------------------------------------------------- |
| from controller import Emitter                                        |
| class [Emitter](#emitter) ([Device](#python_device)) :                |
| &nbsp;&nbsp; CHANNEL\_BROADCAST                                       |
| &nbsp;&nbsp; def [send](#wb_emitter_send)(self, data)                 |
| &nbsp;&nbsp; def [getChannel](#wb_emitter_set_channel)(self)          |
| &nbsp;&nbsp; def [setChannel](#wb_emitter_set_channel)(self, channel) |
| &nbsp;&nbsp; def [getRange](#wb_emitter_set_range)(self)              |
| &nbsp;&nbsp; def [setRange](#wb_emitter_set_range)(self, range)       |
| &nbsp;&nbsp; def [getBufferSize](#wb_emitter_get_buffer_size)(self)   |

%end

%api "python_field"

|                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- |
| from controller import Field                                                                               |
| class Field :                                                                                              |
| &nbsp;&nbsp; SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F,                                         |
| &nbsp;&nbsp; SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF,                                            |
| &nbsp;&nbsp; MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR,                                        |
| &nbsp;&nbsp; MF\_STRING, MF\_NODE                                                                          |
| &nbsp;&nbsp; def [getType](#wb_supervisor_field_get)(self)                                                 |
| &nbsp;&nbsp; def [getTypeName](#wb_supervisor_field_get)(self)                                             |
| &nbsp;&nbsp; def [getCount](#wb_supervisor_field_get)(self)                                                |
| &nbsp;&nbsp; def [getSFBool](#wb_supervisor_field_get_sf_bool)(self)                                       |
| &nbsp;&nbsp; def [getSFInt32](#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFFloat](#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFVec2f](#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFVec3f](#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFRotation](#wb_supervisor_field_get_sf_bool)(self)                                   |
| &nbsp;&nbsp; def [getSFColor](#wb_supervisor_field_get_sf_bool)(self)                                      |
| &nbsp;&nbsp; def [getSFString](#wb_supervisor_field_get_sf_bool)(self)                                     |
| &nbsp;&nbsp; def [getSFNode](#wb_supervisor_field_get_sf_bool)(self)                                       |
| &nbsp;&nbsp; def [getMFBool](#wb_supervisor_field_get_sf_bool)(self, index)                                |
| &nbsp;&nbsp; def [getMFInt32](#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFFloat](#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFVec2f](#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFVec3f](#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFRotation](#wb_supervisor_field_get_sf_bool)(self, index)                            |
| &nbsp;&nbsp; def [getMFColor](#wb_supervisor_field_get_sf_bool)(self, index)                               |
| &nbsp;&nbsp; def [getMFString](#wb_supervisor_field_get_sf_bool)(self, index)                              |
| &nbsp;&nbsp; def [getMFNode](#wb_supervisor_field_get_sf_bool)(self, index)                                |
| &nbsp;&nbsp; def [setSFBool](#wb_supervisor_field_set_sf_bool)(self, value)                                |
| &nbsp;&nbsp; def [setSFInt32](#wb_supervisor_field_set_sf_bool)(self, value)                               |
| &nbsp;&nbsp; def [setSFFloat](#wb_supervisor_field_set_sf_bool)(self, value)                               |
| &nbsp;&nbsp; def [setSFVec2f](#wb_supervisor_field_set_sf_bool)(self, values)                              |
| &nbsp;&nbsp; def [setSFVec3f](#wb_supervisor_field_set_sf_bool)(self, values)                              |
| &nbsp;&nbsp; def [setSFRotation](#wb_supervisor_field_set_sf_bool)(self, values)                           |
| &nbsp;&nbsp; def [setSFColor](#wb_supervisor_field_set_sf_bool)(self, values)                              |
| &nbsp;&nbsp; def [setSFString](#wb_supervisor_field_set_sf_bool)(self, value)                              |
| &nbsp;&nbsp; def [setMFBool](#wb_supervisor_field_set_sf_bool)(self, index, value)                         |
| &nbsp;&nbsp; def [setMFInt32](#wb_supervisor_field_set_sf_bool)(self, index, value)                        |
| &nbsp;&nbsp; def [setMFFloat](#wb_supervisor_field_set_sf_bool)(self, index, value)                        |
| &nbsp;&nbsp; def [setMFVec2f](#wb_supervisor_field_set_sf_bool)(self, index, values)                       |
| &nbsp;&nbsp; def [setMFVec3f](#wb_supervisor_field_set_sf_bool)(self, index, values)                       |
| &nbsp;&nbsp; def [setMFRotation](#wb_supervisor_field_set_sf_bool)(self, index, values)                    |
| &nbsp;&nbsp; def [setMFColor](#wb_supervisor_field_set_sf_bool)(self, index, values)                       |
| &nbsp;&nbsp; def [setMFString](#wb_supervisor_field_set_sf_bool)(self, index, value)                       |
| &nbsp;&nbsp; def [importMFNode](#wb_supervisor_field_import_mf_node)(self, position, filename)             |
| &nbsp;&nbsp; def [importMFNodeFromString](#wb_supervisor_field_import_mf_node)(self, position, nodeString) |
| &nbsp;&nbsp; def [removeMFNode](#wb_supervisor_field_import_mf_node)(self, position)                       |

%end

%api "python_gps"

|                                                                |
| -------------------------------------------------------------- |
| from controller import GPS                                     |
| class [GPS](#gps) ([Device](#python_device)) :                 |
| &nbsp;&nbsp; def [enable](#wb_gps_get_values)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_gps_get_values)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_gps_get_values)(self) |
| &nbsp;&nbsp; def [getValues](#wb_gps_get_values)(self)         |

%end

%api "python_gyro"

|                                                                 |
| --------------------------------------------------------------- |
| from controller import Gyro                                     |
| class [Gyro](#gyro) ([Device](#python_device)) :                |
| &nbsp;&nbsp; def [enable](#wb_gyro_get_values)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_gyro_get_values)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_gyro_get_values)(self) |
| &nbsp;&nbsp; def [getValues](#wb_gyro_get_values)(self)         |

%end

%api "python_image_ref"

|                                 |
| ------------------------------- |
| from controller import ImageRef |
| class ImageRef :                |

%end

%api "python_inertial_unit"

|                                                                                  |
| -------------------------------------------------------------------------------- |
| from controller import InertialUnit                                              |
| class [InertialUnit](#inertialunit) ([Device](#python_device)) :                 |
| &nbsp;&nbsp; def [enable](#wb_inertial_unit_get_roll_pitch_yaw)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_inertial_unit_get_roll_pitch_yaw)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_inertial_unit_get_roll_pitch_yaw)(self) |
| &nbsp;&nbsp; def [getRollPitchYaw](#wb_inertial_unit_get_roll_pitch_yaw)(self)   |

%end

%api "python_led"

|                                                  |
| ------------------------------------------------ |
| from controller import LED                       |
| class [LED](#led) ([Device](#python_device)) :   |
| &nbsp;&nbsp; def [set](#wb_led_set)(self, state) |
| &nbsp;&nbsp; def [get](#wb_led_set)(self)        |

%end

%api "python_light_sensor"

|                                                                        |
| ---------------------------------------------------------------------- |
| from controller import LightSensor                                     |
| class [LightSensor](#lightsensor) ([Device](#python_device)) :         |
| &nbsp;&nbsp; def [enable](#wb_light_sensor_get_value)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_light_sensor_get_value)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_light_sensor_get_value)(self) |
| &nbsp;&nbsp; def [getValue](#wb_light_sensor_get_value)(self)          |

%end

%api "python_motion"

|                                                                  |
| ---------------------------------------------------------------- |
| from controller import Motion                                    |
| class [Motion](#motion) :                                        |
| &nbsp;&nbsp; def [\_\_init\_\_](#wbu_motion_new)(self, fileName) |
| &nbsp;&nbsp; def [\_\_del\_\_](#wbu_motion_new)(self)            |
| &nbsp;&nbsp; def [isValid](#wbu_motion_new)(self)                |
| &nbsp;&nbsp; def [play](#wbu_motion_play)(self)                  |
| &nbsp;&nbsp; def [stop](#wbu_motion_play)(self)                  |
| &nbsp;&nbsp; def [setLoop](#wbu_motion_play)(self, loop)         |
| &nbsp;&nbsp; def [setReverse](#wbu_motion_play)(self, reverse)   |
| &nbsp;&nbsp; def [isOver](#wbu_motion_is_over)(self)             |
| &nbsp;&nbsp; def [getDuration](#wbu_motion_is_over)(self)        |
| &nbsp;&nbsp; def [getTime](#wbu_motion_is_over)(self)            |
| &nbsp;&nbsp; def [setTime](#wbu_motion_is_over)(self, time)      |

%end

%api "python_motor"

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| from controller import Motor                                                              |
| class [Motor](#motor) ([Device](#python_device)) :                                        |
| &nbsp;&nbsp; ROTATIONAL, LINEAR                                                           |
| &nbsp;&nbsp; def [setPosition](#wb_motor_set_position)(self, position)                    |
| &nbsp;&nbsp; def [setVelocity](#wb_motor_set_position)(self, vel)                         |
| &nbsp;&nbsp; def [setAcceleration](#wb_motor_set_position)(self, force)                   |
| &nbsp;&nbsp; def [setAvailableForce](#wb_motor_set_position)(self, motor\_force)          |
| &nbsp;&nbsp; def [setAvailableTorque](#wb_motor_set_position)(self, motor\_torque)        |
| &nbsp;&nbsp; def [setControlPID](#wb_motor_set_position)(self, p, i, d)                   |
| &nbsp;&nbsp; def [getTargetPosition](#wb_motor_set_position)(self)                        |
| &nbsp;&nbsp; def [getMinPosition](#wb_motor_set_position)(self)                           |
| &nbsp;&nbsp; def [getMaxPosition](#wb_motor_set_position)(self)                           |
| &nbsp;&nbsp; def [getVelocity](#wb_motor_set_position)(self)                              |
| &nbsp;&nbsp; def [getMaxVelocity](#wb_motor_set_position)(self)                           |
| &nbsp;&nbsp; def [getAcceleration](#wb_motor_set_position)(self)                          |
| &nbsp;&nbsp; def [getAvailableForce](#wb_motor_set_position)(self)                        |
| &nbsp;&nbsp; def [getMaxForce](#wb_motor_set_position)(self)                              |
| &nbsp;&nbsp; def [getAvailableTorque](#wb_motor_set_position)(self)                       |
| &nbsp;&nbsp; double [getMaxTorque](#wb_motor_set_position)(self)                          |
| &nbsp;&nbsp; def [enableForceFeedback](#wb_motor_enable_force_feedback)(self, ms)         |
| &nbsp;&nbsp; def [disableForceFeedback](#wb_motor_enable_force_feedback)(self)            |
| &nbsp;&nbsp; def [getForceFeedbackSamplingPeriod](#wb_motor_enable_force_feedback)(self)  |
| &nbsp;&nbsp; def [getForceFeedback](#wb_motor_enable_force_feedback)(self)                |
| &nbsp;&nbsp; def [setForce](#wb_motor_set_force)(self, torque)                            |
| &nbsp;&nbsp; def [enableTorqueFeedback](#wb_motor_enable_force_feedback)(self, ms)        |
| &nbsp;&nbsp; def [disableTorqueFeedback](#wb_motor_enable_force_feedback)(self)           |
| &nbsp;&nbsp; def [getTorqueFeedbackSamplingPeriod](#wb_motor_enable_force_feedback)(self) |
| &nbsp;&nbsp; def [getTorqueFeedback](#wb_motor_enable_force_feedback)(self)               |
| &nbsp;&nbsp; def [setTorque](#wb_motor_set_force)(self, torque)                           |
| &nbsp;&nbsp; def [getType](#wb_motor_get_type)(self)                                      |

%end

%api "python_node"

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from controller import Node                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| class Node :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; NO\_NODE, ACCELEROMETER, APPEARANCE, BACKGROUND, BALL\_JOINT, BALL\_JOINT\_PARAMETERS, BOX, BRAKE, CAMERA, CAMERA\_FOCUS, CAMERA\_LENS\_DISTORTION, CAMERA\_ZOOM, CAPSULE, CHARGER, COLOR, COMPASS, CONE, CONNECTOR, CONTACT\_PROPERTIES, COORDINATE, CYLINDER, DAMPING, DIFFERENTIAL\_WHEELS, DIRECTIONAL\_LIGHT, DISPLAY, DISTANCE\_SENSOR, ELEVATION\_GRID, EMITTER, EXTRUSION, FLUID, FOG, GPS, GROUP, GYRO, HINGE\_2\_JOINT, HINGE\_2\_JOINT\_PARAMETERS, HINGE\_JOINT, HINGE\_JOINT\_PARAMETERS, IMAGE\_TEXTURE, IMMERSION\_PROPERTIES, INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, INERTIAL\_UNIT, JOINT\_PARAMETERS, LED, LIGHT\_SENSOR, LINEAR\_MOTOR, MATERIAL, MICROPHONE, PEN, PHYSICS, PLANE, POINT\_LIGHT, POSITION\_SENSOR, PROPELLER, RADIO, RECEIVER, ROBOT, ROTATIONAL\_MOTOR, SERVO, SHAPE, SLIDER\_JOINT, SLOT, SOLID, SOLID\_REFERENCE, SPEAKER, SPHERE, SPOT\_LIGHT, SUPERVISOR, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, TOUCH\_SENSOR, TRACK, TRACK\_WHEEL, TRANSFORM, VIEWPOINT, WORLD\_INFO |
| &nbsp;&nbsp; def [remove](#wb_supervisor_node_remove)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; def [getType](#wb_supervisor_node_get_type)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &nbsp;&nbsp; def [getId](#wb_supervisor_node_get_from_def)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp; def [getTypeName](#wb_supervisor_node_get_type)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| &nbsp;&nbsp; def [getBaseTypeName](#wb_supervisor_node_get_type)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; def [getField](#wb_supervisor_node_get_field)(self, fieldName)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; def [getParentNode](#wb_supervisor_node_get_from_def)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &nbsp;&nbsp; def [getPosition](#wb_supervisor_node_get_position)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; def [getOrientation](#wb_supervisor_node_get_position)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| &nbsp;&nbsp; def [getCenterOfMass](#wb_supervisor_node_get_center_of_mass)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp; def [getContactPoint](#wb_supervisor_node_get_contact_point)(self, index)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; def [getNumberOfContactPoints](#wb_supervisor_node_get_number_of_contact_points)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; def [getStaticBalance](#wb_supervisor_node_get_static_balance)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| &nbsp;&nbsp; def [getVelocity](#wb_supervisor_node_get_velocity)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; def [setVelocity](#wb_supervisor_node_get_velocity)(self, velocity)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp; def [resetPhysics](#wb_supervisor_node_reset_physics)(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

%end

%api "python_pen"

|                                                                             |
| --------------------------------------------------------------------------- |
| from controller import Pen                                                  |
| class [Pen](#pen) ([Device](#python_device)) :                              |
| &nbsp;&nbsp; def [write](#wb_pen_write)(self, write)                        |
| &nbsp;&nbsp; def [setInkColor](#wb_pen_set_ink_color)(self, color, density) |

%end

%api "python_position_sensor"

|                                                                           |
| ------------------------------------------------------------------------- |
| from controller import PositionSensor                                     |
| class [PositionSensor](#positionsensor) ([Device](#python_device)) :      |
| &nbsp;&nbsp; ANGULAR, LINEAR                                              |
| &nbsp;&nbsp; def [enable](#wb_position_sensor_get_value)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_position_sensor_get_value)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_position_sensor_get_value)(self) |
| &nbsp;&nbsp; def [getValue](#wb_position_sensor_get_value)(self)          |
| &nbsp;&nbsp; def [getType](#wb_position_sensor_get_value)(self)           |

%end

%api "python_receiver"

|                                                                                |
| ------------------------------------------------------------------------------ |
| from controller import Receiver                                                |
| class [Receiver](#receiver) ([Device](#python_device)) :                       |
| &nbsp;&nbsp; CHANNEL\_BROADCAST                                                |
| &nbsp;&nbsp; def [enable](#wb_receiver_enable)(self, ms)                       |
| &nbsp;&nbsp; def [disable](#wb_receiver_enable)(self)                          |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_receiver_enable)(self)                |
| &nbsp;&nbsp; def [getQueueLength](#wb_receiver_get_queue_length)(self)         |
| &nbsp;&nbsp; def [nextPacket](#wb_receiver_get_queue_length)(self)             |
| &nbsp;&nbsp; def [getData](#wb_receiver_get_data)(self)                        |
| &nbsp;&nbsp; def [getDataSize](#wb_receiver_get_data)(self)                    |
| &nbsp;&nbsp; def [getSignalStrength](#wb_receiver_get_signal_strength)(self)   |
| &nbsp;&nbsp; def [getEmitterDirection](#wb_receiver_get_signal_strength)(self) |
| &nbsp;&nbsp; def [setChannel](#wb_receiver_set_channel)(self, channel)         |
| &nbsp;&nbsp; def [getChannel](#wb_receiver_set_channel)(self)                  |

%end

%api "python_robot"

|                                                                                          |
| ---------------------------------------------------------------------------------------- |
| from controller import Robot                                                             |
| class [Robot](#robot) :                                                                  |
| &nbsp;&nbsp; MODE\_SIMULATION, MODE\_CROSS\_COMPILATION,                                 |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL                                                       |
| &nbsp;&nbsp; KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT, KEYBOARD\_UP,                |
| &nbsp;&nbsp; KEYBOARD\_RIGHT, KEYBOARD\_DOWN, KEYBOARD\_PAGEUP,                          |
| &nbsp;&nbsp; KEYBOARD\_PAGEDOWN, KEYBOARD\_NUMPAD\_HOME,                                 |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_LEFT, KEYBOARD\_NUMPAD\_UP,                               |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_RIGHT, KEYBOARD\_NUMPAD\_DOWN,                            |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_END, KEYBOARD\_KEY, KEYBOARD\_SHIFT,                      |
| &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT                                            |
| &nbsp;&nbsp; def [\_\_init\_\_](#wb_robot_step)(self)                                    |
| &nbsp;&nbsp; def [\_\_del\_\_](#wb_robot_step)(self)                                     |
| &nbsp;&nbsp; def [step](#wb_robot_step)(self, ms)                                        |
| &nbsp;&nbsp; def [getAccelerometer](#robotgetdevice)(self, name)                         |
| &nbsp;&nbsp; def [getBrake](#robotgetdevice)(self, name)                                 |
| &nbsp;&nbsp; def [getCamera](#robotgetdevice)(self, name)                                |
| &nbsp;&nbsp; def [getCompass](#robotgetdevice)(self, name)                               |
| &nbsp;&nbsp; def [getConnector](#robotgetdevice)(self, name)                             |
| &nbsp;&nbsp; def [getDisplay](#robotgetdevice)(self, name)                               |
| &nbsp;&nbsp; def [getDistanceSensor](#robotgetdevice)(self, name)                        |
| &nbsp;&nbsp; def [getEmitter](#robotgetdevice)(self, name)                               |
| &nbsp;&nbsp; def [getGPS](#robotgetdevice)(self, name)                                   |
| &nbsp;&nbsp; def [getGyro](#robotgetdevice)(self, name)                                  |
| &nbsp;&nbsp; def [getInertialUnit](#robotgetdevice)(self, name)                          |
| &nbsp;&nbsp; def [getLED](#robotgetdevice)(self, name)                                   |
| &nbsp;&nbsp; def [getLightSensor](#robotgetdevice)(self, name)                           |
| &nbsp;&nbsp; def [getMotor](#robotgetdevice)(self, name)                                 |
| &nbsp;&nbsp; def [getPen](#robotgetdevice)(self, name)                                   |
| &nbsp;&nbsp; def [getPositionSensor](#robotgetdevice)(self, name)                        |
| &nbsp;&nbsp; def [getReceiver](#robotgetdevice)(self, name)                              |
| &nbsp;&nbsp; def [getServo](#robotgetdevice)(self, name)                                 |
| &nbsp;&nbsp; def [getTouchSensor](#robotgetdevice)(self, name)                           |
| &nbsp;&nbsp; def [getNumberOfDevices](#wb_robot_get_device_by_index)(self)               |
| &nbsp;&nbsp; def [getDeviceByIndex](#wb_robot_get_device_by_index)(self, index)          |
| &nbsp;&nbsp; def [batterySensorEnable](#wb_robot_battery_sensor_enable)(self, ms)        |
| &nbsp;&nbsp; def [batterySensorDisable](#wb_robot_battery_sensor_enable)(self)           |
| &nbsp;&nbsp; def [batterySensorGetSamplingPeriod](#wb_robot_battery_sensor_enable)(self) |
| &nbsp;&nbsp; def [batterySensorGetValue](#wb_robot_battery_sensor_enable)(self)          |
| &nbsp;&nbsp; def [getBasicTimeStep](#wb_robot_get_basic_time_step)(self)                 |
| &nbsp;&nbsp; def [getMode](#wb_robot_get_mode)(self)                                     |
| &nbsp;&nbsp; def [getModel](#wb_robot_get_model)(self)                                   |
| &nbsp;&nbsp; def [getData](#wb_robot_get_data)(self)                                     |
| &nbsp;&nbsp; def [setData](#wb_robot_get_data)(self, data)                               |
| &nbsp;&nbsp; def [getName](#wb_robot_get_name)(self)                                     |
| &nbsp;&nbsp; def [getControllerName](#wb_robot_get_controller_name)(self)                |
| &nbsp;&nbsp; def [getControllerArguments](#wb_robot_get_controller_name)(self)           |
| &nbsp;&nbsp; def [getProjectPath](#wb_robot_get_project_path)(self)                      |
| &nbsp;&nbsp; def [getSynchronization](#wb_robot_get_synchronization)(self)               |
| &nbsp;&nbsp; def [getTime](#wb_robot_get_time)(self)                                     |
| &nbsp;&nbsp; def [getWorldPath](#wb_robot_get_world_path)(self)                          |
| &nbsp;&nbsp; def [keyboardEnable](#wb_robot_keyboard_enable)(self, ms)                   |
| &nbsp;&nbsp; def [keyboardDisable](#wb_robot_keyboard_enable)(self)                      |
| &nbsp;&nbsp; def [keyboardGetKey](#wb_robot_keyboard_enable)(self)                       |
| &nbsp;&nbsp; def [getType](#wb_robot_get_type)(self)                                     |

%end

%api "python_servo"

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| from controller import Servo                                                                        |
| class [Servo](#servo) ([Device](#python_device)) :                                                  |
| &nbsp;&nbsp; ROTATIONAL, LINEAR                                                                     |
| &nbsp;&nbsp; def [setPosition](#wb_servo_set_position)(self, position)                              |
| &nbsp;&nbsp; def [getTargetPosition](#wb_servo_set_position)(self)                                  |
| &nbsp;&nbsp; def [setVelocity](#wb_servo_set_position)(self, vel)                                   |
| &nbsp;&nbsp; def [setAcceleration](#wb_servo_set_position)(self, force)                             |
| &nbsp;&nbsp; def [setMotorForce](#wb_servo_set_position)(self, motor\_force)                        |
| &nbsp;&nbsp; def [setControlP](#wb_servo_set_position)(self, p)                                     |
| &nbsp;&nbsp; def [getMinPosition](#wb_servo_set_position)(self)                                     |
| &nbsp;&nbsp; def [getMaxPosition](#wb_servo_set_position)(self)                                     |
| &nbsp;&nbsp; def [enablePosition](#wb_servo_enable_position)(self, ms)                              |
| &nbsp;&nbsp; def [disablePosition](#wb_servo_enable_position)(self)                                 |
| &nbsp;&nbsp; def [getPositionSamplingPeriod](#wb_servo_enable_position)(self)                       |
| &nbsp;&nbsp; def [getPosition](#wb_servo_enable_position)(self)                                     |
| &nbsp;&nbsp; def [enableMotorForceFeedback](#wb_servo_enable_motor_force_feedback)(self, ms)        |
| &nbsp;&nbsp; def [disableMotorForceFeedback](#wb_servo_enable_motor_force_feedback)(self)           |
| &nbsp;&nbsp; def [getMotorForceFeedbackSamplingPeriod](#wb_servo_enable_motor_force_feedback)(self) |
| &nbsp;&nbsp; def [getMotorForceFeedback](#wb_servo_enable_motor_force_feedback)(self)               |
| &nbsp;&nbsp; def [setForce](#wb_servo_set_force)(self, force)                                       |
| &nbsp;&nbsp; def [getType](#wb_servo_get_type)(self)                                                |

%end

%api "python_supervisor"

|                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
| from controller import Supervisor                                                                                                              |
| class [Supervisor](#supervisor) ([Robot](#python_robot)) :                                                                                     |
| &nbsp;&nbsp; MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR              |
| &nbsp;&nbsp; def [\_\_init\_\_](#wb_robot_step)(self)                                                                                          |
| &nbsp;&nbsp; def [\_\_del\_\_](#wb_robot_step)(self)                                                                                           |
| &nbsp;&nbsp; def [exportImage](#wb_supervisor_export_image)(self, file, quality)                                                               |
| &nbsp;&nbsp; def [getRoot](#wb_supervisor_node_get_from_def)(self)                                                                             |
| &nbsp;&nbsp; def [getSelf](#wb_supervisor_node_get_from_def)(self)                                                                             |
| &nbsp;&nbsp; def [getFromDef](#wb_supervisor_node_get_from_def)(self, name)                                                                    |
| &nbsp;&nbsp; def [getFromId](#wb_supervisor_node_get_from_def)(self, id)                                                                       |
| &nbsp;&nbsp; def [setLabel](#wb_supervisor_set_label)(self, id, label, xpos, ypos, size, color, transparency)                                  |
| &nbsp;&nbsp; def [simulationQuit](#wb_supervisor_simulation_quit)(self, status)                                                                |
| &nbsp;&nbsp; def [simulationRevert](#wb_supervisor_simulation_revert)(self)                                                                    |
| &nbsp;&nbsp; def [simulationResetPhysics](#wb_supervisor_simulation_reset_physics)(self)                                                       |
| &nbsp;&nbsp; def [loadWorld](#wb_supervisor_load_world)(self, file)                                                                            |
| &nbsp;&nbsp; def [saveWorld](#wb_supervisor_load_world)(self)                                                                                  |
| &nbsp;&nbsp; def [saveWorld](#wb_supervisor_load_world)(self, file)                                                                            |
| &nbsp;&nbsp; def [movieStartRecording](#wb_supervisor_movie_start_recording)(self, file, width, height, codec, quality, acceleration, caption) |
| &nbsp;&nbsp; def [movieStopRecording](#wb_supervisor_movie_start_recording)(self)                                                              |
| &nbsp;&nbsp; def [movieGetStatus](#wb_supervisor_movie_start_recording)(self)                                                                  |
| &nbsp;&nbsp; def [animationStartRecording](#wb_supervisor_animation_start_recording)(self, file)                                               |
| &nbsp;&nbsp; def [animationStopRecording](#wb_supervisor_animation_start_recording)(self)                                                      |

%end

%api "python_touch_sensor"

|                                                                         |
| ----------------------------------------------------------------------- |
| from controller import TouchSensor                                      |
| class [TouchSensor](#touchsensor) ([Device](#python_device)) :          |
| &nbsp;&nbsp; BUMPER, FORCE, FORCE3D                                     |
| &nbsp;&nbsp; def [enable](#wb_touch_sensor_get_values)(self, ms)        |
| &nbsp;&nbsp; def [disable](#wb_touch_sensor_get_values)(self)           |
| &nbsp;&nbsp; def [getSamplingPeriod](#wb_touch_sensor_get_values)(self) |
| &nbsp;&nbsp; def [getValue](#wb_touch_sensor_get_values)(self)          |
| &nbsp;&nbsp; def [getValues](#wb_touch_sensor_get_values)(self)         |
| &nbsp;&nbsp; def [getType](#wb_touch_sensor_get_type)(self)             |

%end

