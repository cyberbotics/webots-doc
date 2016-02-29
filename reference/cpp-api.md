## C++ API

The following tables describe the C++ classes and their methods.

%api "cpp_accelerometer"

|                                                                               |
| ----------------------------------------------------------------------------- |
| #include `<`webots/Accelerometer.hpp`>`                                       |
| class [Accelerometer](#accelerometer) : public [Device](#cpp_device) {        |
| &nbsp;&nbsp; virtual void [enable](#wb_accelerometer_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](#wb_accelerometer_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_accelerometer_get_values)();         |
| &nbsp;&nbsp; const double *[getValues](#wb_accelerometer_get_values)() const; |
| };                                                                            |

%end

%api "cpp_brake"

|                                                                                                       |
| ----------------------------------------------------------------------------------------------------- |
| #include `<`webots/Brake.hpp`>`                                                                       |
| class [Brake](#brake) : public [Device](#cpp_device) {                                                |
| &nbsp;&nbsp; void [setDampingConstant](#wb_brake_set_damping_constant)(double dampingConstant) const; |
| &nbsp;&nbsp; int [getType](#wb_brake_set_damping_constant)() const;                                   |
| };                                                                                                    |

%end

%api "cpp_camera"

|                                                                                                      |
| ---------------------------------------------------------------------------------------------------- |
| #include `<`webots/Camera.hpp`>`                                                                     |
| class [Camera](#camera) : public [Device](#cpp_device) {                                             |
| &nbsp;&nbsp; enum {COLOR, RANGE\_FINDER, BOTH};                                                      |
| &nbsp;&nbsp; virtual void [enable](#wb_camera_enable)(int ms);                                       |
| &nbsp;&nbsp; virtual void [disable](#wb_camera_enable)();                                            |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_camera_enable)();                                           |
| &nbsp;&nbsp; double [getFov](#wb_camera_get_fov)() const;                                            |
| &nbsp;&nbsp; double [getMinFov](#wb_camera_get_fov)() const;                                         |
| &nbsp;&nbsp; double [getMaxFov](#wb_camera_get_fov)() const;                                         |
| &nbsp;&nbsp; virtual void [setFov](#wb_camera_get_fov)(double fov);                                  |
| &nbsp;&nbsp; double [getFocalLength](#wb_camera_get_focal_length)() const;                           |
| &nbsp;&nbsp; double [getFocalDistance](#wb_camera_get_focal_length)() const;                         |
| &nbsp;&nbsp; double [getMaxFocalDistance](#wb_camera_get_focal_length)() const;                      |
| &nbsp;&nbsp; double [getMinFocalDistance](#wb_camera_get_focal_length)() const;                      |
| &nbsp;&nbsp; virtual void [setFocalDistance](#wb_camera_get_focal_length)(double focalDistance);     |
| &nbsp;&nbsp; int [getWidth](#wb_camera_get_width)() const;                                           |
| &nbsp;&nbsp; int [getHeight](#wb_camera_get_width)() const;                                          |
| &nbsp;&nbsp; double [getNear](#wb_camera_get_near)() const;                                          |
| &nbsp;&nbsp; double [getMaxRange](#wb_camera_get_range_image)() const;                               |
| &nbsp;&nbsp; int [getType](#wb_camera_get_type)() const;                                             |
| &nbsp;&nbsp; const unsigned char *[getImage](#wb_camera_get_image)() const;                          |
| &nbsp;&nbsp; static unsigned char [imageGetRed](#wb_camera_get_image)(const unsigned char *image,    |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                   |
| &nbsp;&nbsp; static unsigned char [imageGetGreen](#wb_camera_get_image)(const unsigned char *image,  |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                   |
| &nbsp;&nbsp; static unsigned char [imageGetBlue](#wb_camera_get_image)(const unsigned char *image,   |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                   |
| &nbsp;&nbsp; static unsigned char [imageGetGrey](#wb_camera_get_image)(const unsigned char *image,   |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                   |
| &nbsp;&nbsp; const float *[getRangeImage](#wb_camera_get_range_image)() const;                       |
| &nbsp;&nbsp; static float [rangeImageGetDepth](#wb_camera_get_range_image)(const float *image,       |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                   |
| &nbsp;&nbsp; int [saveImage](#wb_camera_save_image)(const std::string &filename, int quality) const; |
| };                                                                                                   |

%end

%api "cpp_compass"

|                                                                         |
| ----------------------------------------------------------------------- |
| #include `<`webots/Compass.hpp`>`                                       |
| class [Compass](#compass) : public [Device](#cpp_device) {              |
| &nbsp;&nbsp; virtual void [enable](#wb_compass_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](#wb_compass_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_compass_get_values)();         |
| &nbsp;&nbsp; const double *[getValues](#wb_compass_get_values)() const; |
| };                                                                      |

%end

%api "cpp_connector"

|                                                                                 |
| ------------------------------------------------------------------------------- |
| #include `<`webots/Connector.hpp`>`                                             |
| class [Connector](#connector) : public [Device](#cpp_device) {                  |
| &nbsp;&nbsp; virtual void [enablePresence](#wb_connector_get_presence)(int ms); |
| &nbsp;&nbsp; virtual void [disablePresence](#wb_connector_get_presence)();      |
| &nbsp;&nbsp; int [getPresence](#wb_connector_get_presence)() const;             |
| &nbsp;&nbsp; virtual void [lock](#wb_connector_lock)();                         |
| &nbsp;&nbsp; virtual void [unlock](#wb_connector_lock)();                       |
| };                                                                              |

%end

%api "cpp_device"

|                                                                           |
| ------------------------------------------------------------------------- |
| #include `<`webots/Device.hpp`>`                                          |
| class [Device](#device) {                                                 |
| &nbsp;&nbsp; const std::string &[getModel](#wb_device_get_model)() const; |
| &nbsp;&nbsp; const std::string &[getName](#wb_device_get_name)() const;   |
| &nbsp;&nbsp; int [getNodeType](#wb_device_get_node_type)() const;         |
| };                                                                        |

%end

%api "cpp_differential_wheels"

|                                                                                                               |
| ------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/DifferentialWheels.hpp`>`                                                                  |
| class [DifferentialWheels](#differentialwheels) : public [Robot](#cpp_robot) {                                |
| &nbsp;&nbsp; [DifferentialWheels](#wb_robot_step)();                                                          |
| &nbsp;&nbsp; virtual [~DifferentialWheels](#wb_robot_step)();                                                 |
| &nbsp;&nbsp; virtual void [setSpeed](#wb_differential_wheels_set_speed)(double left, double right);           |
| &nbsp;&nbsp; double [getLeftSpeed](#wb_differential_wheels_set_speed)() const;                                |
| &nbsp;&nbsp; double [getRightSpeed](#wb_differential_wheels_set_speed)() const;                               |
| &nbsp;&nbsp; virtual void [enableEncoders](#wb_differential_wheels_enable_encoders)(int ms);                  |
| &nbsp;&nbsp; virtual void [disableEncoders](#wb_differential_wheels_enable_encoders)();                       |
| &nbsp;&nbsp; int [getEncodersSamplingPeriod](#wb_differential_wheels_enable_encoders)();                      |
| &nbsp;&nbsp; double [getLeftEncoder](#wb_differential_wheels_get_left_encoder)() const;                       |
| &nbsp;&nbsp; double [getRightEncoder](#wb_differential_wheels_get_left_encoder)() const;                      |
| &nbsp;&nbsp; virtual void [setEncoders](#wb_differential_wheels_get_left_encoder)(double left, double right); |
| &nbsp;&nbsp; double [getMaxSpeed](#wb_differential_wheels_get_max_speed)() const;                             |
| &nbsp;&nbsp; double [getSpeedUnit](#wb_differential_wheels_get_speed_unit)() const;                           |
| };                                                                                                            |

%end

%api "cpp_display"

|                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Display.hpp`>`                                                                                                            |
| class [Display](#display) : public [Device](#cpp_device) {                                                                                   |
| &nbsp;&nbsp; enum {RGB, RGBA, ARGB, BGRA};                                                                                                   |
| &nbsp;&nbsp; int [getWidth](#wb_display_get_width)() const;                                                                                  |
| &nbsp;&nbsp; int [getHeight](#wb_display_get_width)() const;                                                                                 |
| &nbsp;&nbsp; virtual void [setColor](#wb_display_set_context)(int color);                                                                    |
| &nbsp;&nbsp; virtual void [setAlpha](#wb_display_set_context)(double alpha);                                                                 |
| &nbsp;&nbsp; virtual void [setOpacity](#wb_display_set_context)(double opacity);                                                             |
| &nbsp;&nbsp; virtual void [drawPixel](#wb_display_draw_primitive)(int x1, int y1);                                                           |
| &nbsp;&nbsp; virtual void [drawLine](#wb_display_draw_primitive)(int x1, int y1, int x2, int y2);                                            |
| &nbsp;&nbsp; virtual void [drawRectangle](#wb_display_draw_primitive)(int x, int y, int width, int height);                                  |
| &nbsp;&nbsp; virtual void [drawOval](#wb_display_draw_primitive)(int cx, int cy, int a, int b);                                              |
| &nbsp;&nbsp; virtual void [drawPolygon](#wb_display_draw_primitive)(const int *x, const int *y, int size);                                   |
| &nbsp;&nbsp; virtual void [drawText](#wb_display_draw_primitive)(const std::string &txt, int x, int y);                                      |
| &nbsp;&nbsp; virtual void [fillRectangle](#wb_display_draw_primitive)(int x, int y, int width, int height);                                  |
| &nbsp;&nbsp; virtual void [fillOval](#wb_display_draw_primitive)(int cx, int cy, int a, int b);                                              |
| &nbsp;&nbsp; virtual void [fillPolygon](#wb_display_draw_primitive)(const int *x, const int *y, int size);                                   |
| &nbsp;&nbsp; [ImageRef](#cpp_image_ref) *[imageCopy](#wb_display_image_functions)(int x, int y, int width, int height) const;                |
| &nbsp;&nbsp; virtual void [imagePaste](#wb_display_image_functions)([ImageRef](#cpp_image_ref) *ir, int x, int y);                           |
| &nbsp;&nbsp; [ImageRef](#cpp_image_ref) *[imageLoad](#wb_display_image_functions)(const std::string &filename) const;                        |
| &nbsp;&nbsp; [ImageRef](#cpp_image_ref) *[imageNew](#wb_display_image_functions)(int width, int height, const void *data, int format) const; |
| &nbsp;&nbsp; void [imageSave](#wb_display_image_functions)([ImageRef](#cpp_image_ref) *ir, const std::string &filename) const;               |
| &nbsp;&nbsp; void [imageDelete](#wb_display_image_functions)([ImageRef](#cpp_image_ref) *ir) const;                                          |
| };                                                                                                                                           |

%end

%api "cpp_distance_sensor"

|                                                                            |
| -------------------------------------------------------------------------- |
| #include `<`webots/DistanceSensor.hpp`>`                                   |
| class [DistanceSensor](#distancesensor) : public [Device](#cpp_device) {   |
| &nbsp;&nbsp; virtual void [enable](#wb_distance_sensor_get_value)(int ms); |
| &nbsp;&nbsp; virtual void [disable](#wb_distance_sensor_get_value)();      |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_distance_sensor_get_value)();     |
| &nbsp;&nbsp; double [getValue](#wb_distance_sensor_get_value)() const;     |
| };                                                                         |

%end

%api "cpp_emitter"

|                                                                                |
| ------------------------------------------------------------------------------ |
| #include `<`webots/Emitter.hpp`>`                                              |
| class [Emitter](#emitter) : public [Device](#cpp_device) {                     |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};                                        |
| &nbsp;&nbsp; virtual int [send](#wb_emitter_send)(const void *data, int size); |
| &nbsp;&nbsp; int [getChannel](#wb_emitter_set_channel)() const;                |
| &nbsp;&nbsp; virtual void [setChannel](#wb_emitter_set_channel)(int channel);  |
| &nbsp;&nbsp; double [getRange](#wb_emitter_set_range)() const;                 |
| &nbsp;&nbsp; virtual void [setRange](#wb_emitter_set_range)(double range);     |
| &nbsp;&nbsp; int [getBufferSize](#wb_emitter_get_buffer_size)() const;         |
| };                                                                             |

%end

%api "cpp_field"

|                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Field.hpp`>`                                                                                                                                                                             |
| class Field {                                                                                                                                                                                               |
| &nbsp;&nbsp; enum { SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, MF\_STRING, MF\_NODE }; |
| &nbsp;&nbsp; int [getType](#wb_supervisor_field_get)() const;                                                                                                                                               |
| &nbsp;&nbsp; std::string [getTypeName](#wb_supervisor_field_get)() const;                                                                                                                                   |
| &nbsp;&nbsp; int [getCount](#wb_supervisor_field_get)() const;                                                                                                                                              |
| &nbsp;&nbsp; bool [getSFBool](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                                    |
| &nbsp;&nbsp; int [getSFInt32](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                                    |
| &nbsp;&nbsp; double [getSFFloat](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                                 |
| &nbsp;&nbsp; const double *[getSFVec2f](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                          |
| &nbsp;&nbsp; const double *[getSFVec3f](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                          |
| &nbsp;&nbsp; const double *[getSFRotation](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                       |
| &nbsp;&nbsp; const double *[getSFColor](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                          |
| &nbsp;&nbsp; std::string [getSFString](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                           |
| &nbsp;&nbsp; [Node](#cpp_node) *[getSFNode](#wb_supervisor_field_get_sf_bool)() const;                                                                                                                      |
| &nbsp;&nbsp; bool [getMFBool](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                                           |
| &nbsp;&nbsp; int [getMFInt32](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                                           |
| &nbsp;&nbsp; double [getMFFloat](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                                        |
| &nbsp;&nbsp; const double *[getMFVec2f](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                                 |
| &nbsp;&nbsp; const double *[getMFVec3f](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                                 |
| &nbsp;&nbsp; const double *[getMFRotation](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                              |
| &nbsp;&nbsp; const double *[getMFColor](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                                 |
| &nbsp;&nbsp; std::string [getMFString](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                                  |
| &nbsp;&nbsp; [Node](#cpp_node) *[getMFNode](#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                             |
| &nbsp;&nbsp; void [setSFBool](#wb_supervisor_field_set_sf_bool)(bool value);                                                                                                                                |
| &nbsp;&nbsp; void [setSFInt32](#wb_supervisor_field_set_sf_bool)(int value);                                                                                                                                |
| &nbsp;&nbsp; void [setSFFloat](#wb_supervisor_field_set_sf_bool)(double value);                                                                                                                             |
| &nbsp;&nbsp; void [setSFVec2f](#wb_supervisor_field_set_sf_bool)(const double values[2]);                                                                                                                   |
| &nbsp;&nbsp; void [setSFVec3f](#wb_supervisor_field_set_sf_bool)(const double values[3]);                                                                                                                   |
| &nbsp;&nbsp; void [setSFRotation](#wb_supervisor_field_set_sf_bool)(const double values[4]);                                                                                                                |
| &nbsp;&nbsp; void [setSFColor](#wb_supervisor_field_set_sf_bool)(const double values[3]);                                                                                                                   |
| &nbsp;&nbsp; void [setSFString](#wb_supervisor_field_set_sf_bool)(const std::string &value);                                                                                                                |
| &nbsp;&nbsp; void [setMFBool](#wb_supervisor_field_set_sf_bool)(int index, bool value);                                                                                                                     |
| &nbsp;&nbsp; void [setMFInt32](#wb_supervisor_field_set_sf_bool)(int index, int value);                                                                                                                     |
| &nbsp;&nbsp; void [setMFFloat](#wb_supervisor_field_set_sf_bool)(int index, double value);                                                                                                                  |
| &nbsp;&nbsp; void [setMFVec2f](#wb_supervisor_field_set_sf_bool)(int index, const double values[2]);                                                                                                        |
| &nbsp;&nbsp; void [setMFVec3f](#wb_supervisor_field_set_sf_bool)(int index, const double values[3]);                                                                                                        |
| &nbsp;&nbsp; void [setMFRotation](#wb_supervisor_field_set_sf_bool)(int index, const double values[4]);                                                                                                     |
| &nbsp;&nbsp; void [setMFColor](#wb_supervisor_field_set_sf_bool)(int index, const double values[3]);                                                                                                        |
| &nbsp;&nbsp; void [setMFString](#wb_supervisor_field_set_sf_bool)(int index, const std::string &value);                                                                                                     |
| &nbsp;&nbsp; void [importMFNode](#wb_supervisor_field_import_mf_node)(int position, const std::string &filename);                                                                                           |
| &nbsp;&nbsp; void [importMFNodeFromString](#wb_supervisor_field_import_mf_node)(int position, const std::string &nodeString);                                                                               |
| &nbsp;&nbsp; void [removeMFNode](#wb_supervisor_field_import_mf_node)(int position);                                                                                                                        |
| };                                                                                                                                                                                                          |

%end

%api "cpp_gps"

|                                                                     |
| ------------------------------------------------------------------- |
| #include `<`webots/GPS.hpp`>`                                       |
| class [GPS](#gps) : public [Device](#cpp_device) {                  |
| &nbsp;&nbsp; virtual void [enable](#wb_gps_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](#wb_gps_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_gps_get_values)();         |
| &nbsp;&nbsp; const double *[getValues](#wb_gps_get_values)() const; |
| };                                                                  |

%end

%api "cpp_gyro"

|                                                                      |
| -------------------------------------------------------------------- |
| #include `<`webots/Gyro.hpp`>`                                       |
| class [Gyro](#gyro) : public [Device](#cpp_device) {                 |
| &nbsp;&nbsp; virtual void [enable](#wb_gyro_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](#wb_gyro_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_gyro_get_values)();         |
| &nbsp;&nbsp; const double *[getValues](#wb_gyro_get_values)() const; |
| };                                                                   |

%end

%api "cpp_image_ref"

|                                    |
| ---------------------------------- |
| #include `<`webots/ImageRef.hpp`>` |
| class ImageRef {                   |
| };                                 |

%end

%api "cpp_inertial_unit"

|                                                                                             |
| ------------------------------------------------------------------------------------------- |
| #include `<`webots/InertialUnit.hpp`>`                                                      |
| class [InertialUnit](#inertialunit) : public [Device](#cpp_device) {                        |
| &nbsp;&nbsp; virtual void [enable](#wb_inertial_unit_get_roll_pitch_yaw)(int ms);           |
| &nbsp;&nbsp; virtual void [disable](#wb_inertial_unit_get_roll_pitch_yaw)();                |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_inertial_unit_get_roll_pitch_yaw)();               |
| &nbsp;&nbsp; const double *[getRollPitchYaw](#wb_inertial_unit_get_roll_pitch_yaw)() const; |
| };                                                                                          |

%end

%api "cpp_led"

|                                                          |
| -------------------------------------------------------- |
| #include `<`webots/LED.hpp`>`                            |
| class [LED](#led) : public [Device](#cpp_device) {       |
| &nbsp;&nbsp; virtual void [set](#wb_led_set)(int value); |
| &nbsp;&nbsp; int [get](#wb_led_set)() const;             |
| };                                                       |

%end

%api "cpp_light_sensor"

|                                                                         |
| ----------------------------------------------------------------------- |
| #include `<`webots/LightSensor.hpp`>`                                   |
| class [LightSensor](#lightsensor) : public [Device](#cpp_device) {      |
| &nbsp;&nbsp; virtual void [enable](#wb_light_sensor_get_value)(int ms); |
| &nbsp;&nbsp; virtual void [disable](#wb_light_sensor_get_value)();      |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_light_sensor_get_value)();     |
| &nbsp;&nbsp; double [getValue](#wb_light_sensor_get_value)() const;     |
| };                                                                      |

%end

%api "cpp_motion"

|                                                                         |
| ----------------------------------------------------------------------- |
| #include `<`webots/utils/Motion.hpp`>`                                  |
| class [Motion](#motion) {                                               |
| &nbsp;&nbsp; [Motion](#wbu_motion_new)(const std::string &fileName);    |
| &nbsp;&nbsp; virtual [~Motion](#wbu_motion_new)();                      |
| &nbsp;&nbsp; bool [isValid](#wbu_motion_new)() const;                   |
| &nbsp;&nbsp; virtual void [play](#wbu_motion_play)();                   |
| &nbsp;&nbsp; virtual void [stop](#wbu_motion_play)();                   |
| &nbsp;&nbsp; virtual void [setLoop](#wbu_motion_play)(bool loop);       |
| &nbsp;&nbsp; virtual void [setReverse](#wbu_motion_play)(bool reverse); |
| &nbsp;&nbsp; bool [isOver](#wbu_motion_is_over)() const;                |
| &nbsp;&nbsp; int [getDuration](#wbu_motion_is_over)() const;            |
| &nbsp;&nbsp; int [getTime](#wbu_motion_is_over)() const;                |
| &nbsp;&nbsp; virtual void [setTime](#wbu_motion_is_over)(int time);     |
| };                                                                      |

%end

%api "cpp_motor"

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| #include `<`webots/Motor.hpp`>`                                                                  |
| class [Motor](#motor) : public [Device](#cpp_device) {                                           |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};                                                          |
| &nbsp;&nbsp; virtual void [setPosition](#wb_motor_set_position)(double position);                |
| &nbsp;&nbsp; virtual void [setVelocity](#wb_motor_set_position)(double vel);                     |
| &nbsp;&nbsp; virtual void [setAcceleration](#wb_motor_set_position)(double force);               |
| &nbsp;&nbsp; virtual void [setAvailableForce](#wb_motor_set_position)(double motor\_force);      |
| &nbsp;&nbsp; virtual void [setAvailableTorque](#wb_motor_set_position)(double motor\_torque);    |
| &nbsp;&nbsp; virtual void [setControlPID](#wb_motor_set_position)(double p, double i, double d); |
| &nbsp;&nbsp; double [getTargetPosition](#wb_motor_set_position)(double position) const;          |
| &nbsp;&nbsp; double [getMinPosition](#wb_motor_set_position)() const;                            |
| &nbsp;&nbsp; double [getMaxPosition](#wb_motor_set_position)() const;                            |
| &nbsp;&nbsp; double [getVelocity](#wb_motor_set_position)() const;                               |
| &nbsp;&nbsp; double [getMaxVelocity](#wb_motor_set_position)() const;                            |
| &nbsp;&nbsp; double [getAcceleration](#wb_motor_set_position)() const;                           |
| &nbsp;&nbsp; double [getAvailableForce](#wb_motor_set_position)() const;                         |
| &nbsp;&nbsp; double [getMaxForce](#wb_motor_set_position)() const;                               |
| &nbsp;&nbsp; double [getAvailableTorque](#wb_motor_set_position)() const;                        |
| &nbsp;&nbsp; double [getMaxTorque](#wb_motor_set_position)() const;                              |
| &nbsp;&nbsp; virtual void [enableForceFeedback](#wb_motor_enable_force_feedback)(int ms);        |
| &nbsp;&nbsp; virtual void [disableForceFeedback](#wb_motor_enable_force_feedback)();             |
| &nbsp;&nbsp; int [getForceFeedbackSamplingPeriod](#wb_motor_enable_force_feedback)();            |
| &nbsp;&nbsp; double [getForceFeedback](#wb_motor_enable_force_feedback)() const;                 |
| &nbsp;&nbsp; virtual void [setForce](#wb_motor_set_force)(double force);                         |
| &nbsp;&nbsp; virtual void [enableTorqueFeedback](#wb_motor_enable_force_feedback)(int ms);       |
| &nbsp;&nbsp; virtual void [disableTorqueFeedback](#wb_motor_enable_force_feedback)();            |
| &nbsp;&nbsp; int [getTorqueFeedbackSamplingPeriod](#wb_motor_enable_force_feedback)();           |
| &nbsp;&nbsp; double [getTorqueFeedback](#wb_motor_enable_force_feedback)() const;                |
| &nbsp;&nbsp; virtual void [setTorque](#wb_motor_set_force)(double torque);                       |
| &nbsp;&nbsp; int [getType](#wb_motor_get_type)() const;                                          |
| };                                                                                               |

%end

%api "cpp_node"

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Node.hpp`>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| class Node {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| &nbsp;&nbsp; enum { NO\_NODE, ACCELEROMETER, APPEARANCE, BACKGROUND, BALL\_JOINT, BALL\_JOINT\_PARAMETERS, BOX, BRAKE, CAMERA, CAMERA\_FOCUS, CAMERA\_LENS\_DISTORTION, CAMERA\_ZOOM, CAPSULE, CHARGER, COLOR, COMPASS, CONE, CONNECTOR, CONTACT\_PROPERTIES, COORDINATE, CYLINDER, DAMPING, DIFFERENTIAL\_WHEELS, DIRECTIONAL\_LIGHT, DISPLAY, DISTANCE\_SENSOR, ELEVATION\_GRID, EMITTER, EXTRUSION, FLUID, FOG, GPS, GROUP, GYRO, HINGE\_2\_JOINT, HINGE\_2\_JOINT\_PARAMETERS, HINGE\_JOINT, HINGE\_JOINT\_PARAMETERS, IMAGE\_TEXTURE, IMMERSION\_PROPERTIES, INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, INERTIAL\_UNIT, JOINT\_PARAMETERS, LED, LIGHT\_SENSOR, LINEAR\_MOTOR, MATERIAL, MICROPHONE, PEN, PHYSICS, PLANE, POINT\_LIGHT, POSITION\_SENSOR, PROPELLER, RADIO, RECEIVER, ROBOT, ROTATIONAL\_MOTOR, SERVO, SHAPE, SLIDER\_JOINT, SLOT, SOLID, SOLID\_REFERENCE, SPEAKER, SPHERE, SPOT\_LIGHT, SUPERVISOR, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, TOUCH\_SENSOR, TRACK, TRACK\_WHEEL, TRANSFORM, VIEWPOINT, WORLD\_INFO }; |
| &nbsp;&nbsp; virtual void [remove](#wb_supervisor_node_remove)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &nbsp;&nbsp; int [getId](#wb_supervisor_node_get_from_def)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| &nbsp;&nbsp; int [getType](#wb_supervisor_node_get_type)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &nbsp;&nbsp; std::string [getTypeName](#wb_supervisor_node_get_type)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; std::string [getBaseTypeName](#wb_supervisor_node_get_type)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &nbsp;&nbsp; Node *[getParentNode](#wb_supervisor_node_get_from_def)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; [Field](#cpp_field) *[getField](#wb_supervisor_node_get_field)(const std::string &fieldName) const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; const double *[getPosition](#wb_supervisor_node_get_position)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| &nbsp;&nbsp; const double *[getOrientation](#wb_supervisor_node_get_position)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; const double *[getCenterOfMass](#wb_supervisor_node_get_center_of_mass)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; const double *[getContactPoint](#wb_supervisor_node_get_contact_point)(int index) const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; int [getNumberOfContactPoints](#wb_supervisor_node_get_number_of_contact_points)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; bool [getStaticBalance](#wb_supervisor_node_get_static_balance)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; const double * [getVelocity](#wb_supervisor_node_get_velocity)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| &nbsp;&nbsp; void [setVelocity](#wb_supervisor_node_get_velocity)(const double velocity[6]);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| &nbsp;&nbsp; void [resetPhysics](#wb_supervisor_node_reset_physics)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| };                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

%end

%api "cpp_pen"

|                                                                                            |
| ------------------------------------------------------------------------------------------ |
| #include `<`webots/Pen.hpp`>`                                                              |
| class [Pen](#pen) : public [Device](#cpp_device) {                                         |
| &nbsp;&nbsp; virtual void [write](#wb_pen_write)(bool write);                              |
| &nbsp;&nbsp; virtual void [setInkColor](#wb_pen_set_ink_color)(int color, double density); |
| };                                                                                         |

%end

%api "cpp_position_sensor"

|                                                                            |
| -------------------------------------------------------------------------- |
| #include `<`webots/PositionSensor.hpp`>`                                   |
| class [PositionSensor](#positionsensor) : public [Device](#cpp_device) {   |
| &nbsp;&nbsp; enum {ANGULAR, LINEAR};                                       |
| &nbsp;&nbsp; virtual void [enable](#wb_position_sensor_get_value)(int ms); |
| &nbsp;&nbsp; virtual void [disable](#wb_position_sensor_get_value)();      |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_position_sensor_get_value)();     |
| &nbsp;&nbsp; double [getValue](#wb_position_sensor_get_value)() const;     |
| &nbsp;&nbsp; int [getType](#wb_position_sensor_get_value)() const;         |
| };                                                                         |

%end

%api "cpp_receiver"

|                                                                                             |
| ------------------------------------------------------------------------------------------- |
| #include `<`webots/Receiver.hpp`>`                                                          |
| class [Receiver](#receiver) : public [Device](#cpp_device) {                                |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};                                                     |
| &nbsp;&nbsp; virtual void [enable](#wb_receiver_enable)(int ms);                            |
| &nbsp;&nbsp; virtual void [disable](#wb_receiver_enable)();                                 |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_receiver_enable)();                                |
| &nbsp;&nbsp; int [getQueueLength](#wb_receiver_get_queue_length)() const;                   |
| &nbsp;&nbsp; virtual void [nextPacket](#wb_receiver_get_queue_length)();                    |
| &nbsp;&nbsp; const void *[getData](#wb_receiver_get_data)() const;                          |
| &nbsp;&nbsp; int [getDataSize](#wb_receiver_get_data)() const;                              |
| &nbsp;&nbsp; double [getSignalStrength](#wb_receiver_get_signal_strength)() const;          |
| &nbsp;&nbsp; const double *[getEmitterDirection](#wb_receiver_get_signal_strength)() const; |
| &nbsp;&nbsp; virtual void [setChannel](#wb_receiver_set_channel)(int channel);              |
| &nbsp;&nbsp; int [getChannel](#wb_receiver_set_channel)() const;                            |
| };                                                                                          |

%end

%api "cpp_robot"

|                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Robot.hpp`>`                                                                                     |
| class [Robot](#robot) {                                                                                             |
| &nbsp;&nbsp; enum {MODE\_SIMULATION, MODE\_CROSS\_COMPILATION,                                                      |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL};                                                                                |
| &nbsp;&nbsp; enum {KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT,                                                   |
| &nbsp;&nbsp; KEYBOARD\_UP, KEYBOARD\_RIGHT, KEYBOARD\_DOWN,                                                         |
| &nbsp;&nbsp; KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN,                                                                  |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT,                                                        |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT,                                                         |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END,                                                         |
| &nbsp;&nbsp; KEYBOARD\_KEY, KEYBOARD\_SHIFT, KEYBOARD\_CONTROL,                                                     |
| &nbsp;&nbsp; KEYBOARD\_ALT};                                                                                        |
| &nbsp;&nbsp; [Robot](#wb_robot_step)();                                                                             |
| &nbsp;&nbsp; virtual [~Robot](#wb_robot_step)();                                                                    |
| &nbsp;&nbsp; virtual int [step](#wb_robot_step)(int ms);                                                            |
| &nbsp;&nbsp; [Accelerometer](#cpp_accelerometer) *[getAccelerometer](#robotgetdevice)(const std::string &name);     |
| &nbsp;&nbsp; [Brake](#cpp_brake) *[getBrake](#robotgetdevice)(const std::string &name);                             |
| &nbsp;&nbsp; [Camera](#cpp_camera) *[getCamera](#robotgetdevice)(const std::string &name);                          |
| &nbsp;&nbsp; [Compass](#cpp_compass) *[getCompass](#robotgetdevice)(const std::string &name);                       |
| &nbsp;&nbsp; [Connector](#cpp_connector) *[getConnector](#robotgetdevice)(const std::string &name);                 |
| &nbsp;&nbsp; [Display](#cpp_display) *[getDisplay](#robotgetdevice)(const std::string &name);                       |
| &nbsp;&nbsp; [DistanceSensor](#cpp_distance_sensor) *[getDistanceSensor](#robotgetdevice)(const std::string &name); |
| &nbsp;&nbsp; [Emitter](#cpp_emitter) *[getEmitter](#robotgetdevice)(const std::string &name);                       |
| &nbsp;&nbsp; [GPS](#cpp_gps) *[getGPS](#robotgetdevice)(const std::string &name);                                   |
| &nbsp;&nbsp; [Gyro](#cpp_gyro) *[getGyro](#robotgetdevice)(const std::string &name);                                |
| &nbsp;&nbsp; [InertialUnit](#cpp_inertial_unit) *[getInertialUnit](#robotgetdevice)(const std::string &name);       |
| &nbsp;&nbsp; [LED](#cpp_led) *[getLED](#robotgetdevice)(const std::string &name);                                   |
| &nbsp;&nbsp; [LightSensor](#cpp_light_sensor) *[getLightSensor](#robotgetdevice)(const std::string &name);          |
| &nbsp;&nbsp; [Motor](#cpp_motor) *[getMotor](#robotgetdevice)(const std::string &name);                             |
| &nbsp;&nbsp; [Pen](#cpp_pen) *[getPen](#robotgetdevice)(const std::string &name);                                   |
| &nbsp;&nbsp; [PositionSensor](#cpp_position_sensor) *[getPositionSensor](#robotgetdevice)(const std::string &name); |
| &nbsp;&nbsp; [Receiver](#cpp_receiver) *[getReceiver](#robotgetdevice)(const std::string &name);                    |
| &nbsp;&nbsp; [Servo](#cpp_servo) *[getServo](#robotgetdevice)(const std::string &name);                             |
| &nbsp;&nbsp; [TouchSensor](#cpp_touch_sensor) *[getTouchSensor](#robotgetdevice)(const std::string &name);          |
| &nbsp;&nbsp; int [getNumberOfDevices](#wb_robot_get_device_by_index)();                                             |
| &nbsp;&nbsp; [Device](#cpp_device) *[getDeviceByIndex](#wb_robot_get_device_by_index)(int index);                   |
| &nbsp;&nbsp; virtual void [batterySensorEnable](#wb_robot_battery_sensor_enable)(int ms);                           |
| &nbsp;&nbsp; virtual void [batterySensorDisable](#wb_robot_battery_sensor_enable)();                                |
| &nbsp;&nbsp; int [batterySensorGetSamplingPeriod](#wb_robot_battery_sensor_enable)();                               |
| &nbsp;&nbsp; double [batterySensorGetValue](#wb_robot_battery_sensor_enable)() const;                               |
| &nbsp;&nbsp; double [getBasicTimeStep](#wb_robot_get_basic_time_step)() const;                                      |
| &nbsp;&nbsp; int [getMode](#wb_robot_get_mode)() const;                                                             |
| &nbsp;&nbsp; std::string [getModel](#wb_robot_get_model)() const;                                                   |
| &nbsp;&nbsp; std::string [getData](#wb_robot_get_data)() const;                                                     |
| &nbsp;&nbsp; void [setData](#wb_robot_get_data)(const std::string &data);                                           |
| &nbsp;&nbsp; std::string [getName](#wb_robot_get_name)() const;                                                     |
| &nbsp;&nbsp; std::string [getControllerName](#wb_robot_get_controller_name)() const;                                |
| &nbsp;&nbsp; std::string [getControllerArguments](#wb_robot_get_controller_name)() const;                           |
| &nbsp;&nbsp; std::string [getProjectPath](#wb_robot_get_project_path)() const;                                      |
| &nbsp;&nbsp; bool [getSynchronization](#wb_robot_get_synchronization)() const;                                      |
| &nbsp;&nbsp; double [getTime](#wb_robot_get_time)() const;                                                          |
| &nbsp;&nbsp; std::string [getWorldPath](#wb_robot_get_world_path)() const;                                          |
| &nbsp;&nbsp; virtual void [keyboardEnable](#wb_robot_keyboard_enable)(int ms);                                      |
| &nbsp;&nbsp; virtual void [keyboardDisable](#wb_robot_keyboard_enable)();                                           |
| &nbsp;&nbsp; int [keyboardGetKey](#wb_robot_keyboard_enable)() const;                                               |
| &nbsp;&nbsp; int [getType](#wb_robot_get_type)() const;                                                             |
| &nbsp;&nbsp; void *[robotWindowCustomFunction](#wb_robot_window_custom_function)(void *arg);                        |
| };                                                                                                                  |

%end

%api "cpp_servo"

|                                                                                                      |
| ---------------------------------------------------------------------------------------------------- |
| #include `<`webots/Servo.hpp`>`                                                                      |
| class [Servo](#servo) : public [Device](#cpp_device) {                                               |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};                                                              |
| &nbsp;&nbsp; virtual void [setPosition](#wb_servo_set_position)(double position);                    |
| &nbsp;&nbsp; virtual void [setVelocity](#wb_servo_set_position)(double vel);                         |
| &nbsp;&nbsp; virtual void [setAcceleration](#wb_servo_set_position)(double force);                   |
| &nbsp;&nbsp; virtual void [setMotorForce](#wb_servo_set_position)(double motor\_force);              |
| &nbsp;&nbsp; virtual void [setControlP](#wb_servo_set_position)(double p);                           |
| &nbsp;&nbsp; double [getTargetPosition](#wb_servo_set_position)(double position) const;              |
| &nbsp;&nbsp; double [getMinPosition](#wb_servo_set_position)() const;                                |
| &nbsp;&nbsp; double [getMaxPosition](#wb_servo_set_position)() const;                                |
| &nbsp;&nbsp; virtual void [enablePosition](#wb_servo_enable_position)(int ms);                       |
| &nbsp;&nbsp; virtual void [disablePosition](#wb_servo_enable_position)();                            |
| &nbsp;&nbsp; int [getPositionSamplingPeriod](#wb_servo_enable_position)();                           |
| &nbsp;&nbsp; double [getPosition](#wb_servo_enable_position)() const;                                |
| &nbsp;&nbsp; virtual void [enableMotorForceFeedback](#wb_servo_enable_motor_force_feedback)(int ms); |
| &nbsp;&nbsp; virtual void [disableMotorForceFeedback](#wb_servo_enable_motor_force_feedback)();      |
| &nbsp;&nbsp; int [getMotorForceFeedbackSamplingPeriod](#wb_servo_enable_motor_force_feedback)();     |
| &nbsp;&nbsp; double [getMotorForceFeedback](#wb_servo_enable_motor_force_feedback)() const;          |
| &nbsp;&nbsp; virtual void [setForce](#wb_servo_set_force)(double force);                             |
| &nbsp;&nbsp; int [getType](#wb_servo_get_type)() const;                                              |
| };                                                                                                   |

%end

%api "cpp_supervisor"

|                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Supervisor.hpp`>`                                                                                                                          |
| class [Supervisor](#supervisor) : public [Robot](#cpp_robot) {                                                                                                |
| &nbsp;&nbsp; enum {MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR};                     |
| &nbsp;&nbsp; [Supervisor](#wb_robot_step)();                                                                                                                  |
| &nbsp;&nbsp; virtual [~Supervisor](#wb_robot_step)();                                                                                                         |
| &nbsp;&nbsp; void [exportImage](#wb_supervisor_export_image)(const std::string &file, int quality) const;                                                     |
| &nbsp;&nbsp; [Node](#cpp_node) *[getRoot](#wb_supervisor_node_get_from_def)();                                                                                |
| &nbsp;&nbsp; [Node](#cpp_node) *[getSelf](#wb_supervisor_node_get_from_def)();                                                                                |
| &nbsp;&nbsp; [Node](#cpp_node) *[getFromDef](#wb_supervisor_node_get_from_def)(const std::string &name);                                                      |
| &nbsp;&nbsp; [Node](#cpp_node) *[getFromId](#wb_supervisor_node_get_from_def)(int id);                                                                        |
| &nbsp;&nbsp; virtual void [setLabel](#wb_supervisor_set_label)(int id, const std::string &label, double xpos, double ypos,                                    |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency);                                                                                        |
| &nbsp;&nbsp; virtual void [simulationQuit](#wb_supervisor_simulation_quit)(int status);                                                                       |
| &nbsp;&nbsp; virtual void [simulationRevert](#wb_supervisor_simulation_revert)();                                                                             |
| &nbsp;&nbsp; virtual void [simulationResetPhysics](#wb_supervisor_simulation_reset_physics)();                                                                |
| &nbsp;&nbsp; virtual void [loadWorld](#wb_supervisor_load_world)(const std::string &file);                                                                    |
| &nbsp;&nbsp; virtual void [saveWorld](#wb_supervisor_load_world)();                                                                                           |
| &nbsp;&nbsp; virtual void [saveWorld](#wb_supervisor_load_world)(const std::string &file);                                                                    |
| &nbsp;&nbsp; virtual void [movieStartRecording](#wb_supervisor_movie_start_recording)(const std::string &file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp; int acceleration, bool caption) const;                                                                                                           |
| &nbsp;&nbsp; virtual void [movieStopRecording](#wb_supervisor_movie_start_recording)();                                                                       |
| &nbsp;&nbsp; int [movieGetStatus](#wb_supervisor_movie_start_recording)() const;                                                                              |
| &nbsp;&nbsp; virtual bool [animationStartRecording](#wb_supervisor_animation_start_recording)(const std::string &file);                                       |
| &nbsp;&nbsp; virtual bool [animationStopRecording](#wb_supervisor_animation_start_recording)();                                                               |
| };                                                                                                                                                            |

%end

%api "cpp_touch_sensor"

|                                                                              |
| ---------------------------------------------------------------------------- |
| #include `<`webots/TouchSensor.hpp`>`                                        |
| class [TouchSensor](#touchsensor) : public [Device](#cpp_device) {           |
| &nbsp;&nbsp; enum {BUMPER, FORCE, FORCE3D};                                  |
| &nbsp;&nbsp; virtual void [enable](#wb_touch_sensor_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](#wb_touch_sensor_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_touch_sensor_get_values)();         |
| &nbsp;&nbsp; double [getValue](#wb_touch_sensor_get_values)() const;         |
| &nbsp;&nbsp; const double *[getValues](#wb_touch_sensor_get_values)() const; |
| &nbsp;&nbsp; int [getType](#wb_touch_sensor_get_type)() const;               |
| };                                                                           |

%end

