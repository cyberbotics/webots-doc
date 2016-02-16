## C++ API

The following tables describe the C++ classes and their methods.

<a name="cpp_accelerometer"/>

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| #include `<`webots/Accelerometer.hpp`>`                                                          |
| class [Accelerometer](accelerometer.md#accelerometer) : public [Device](cpp-api.md#cpp_device) { |
| &nbsp;&nbsp; virtual void [enable](accelerometer.md#wb_accelerometer_get_values)(int ms);        |
| &nbsp;&nbsp; virtual void [disable](accelerometer.md#wb_accelerometer_get_values)();             |
| &nbsp;&nbsp; int [getSamplingPeriod](accelerometer.md#wb_accelerometer_get_values)();            |
| &nbsp;&nbsp; const double *[getValues](accelerometer.md#wb_accelerometer_get_values)() const;    |
| };                                                                                               |

<a name="cpp_brake"/>

|                                                                                                               |
| ------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Brake.hpp`>`                                                                               |
| class [Brake](brake.md#brake) : public [Device](cpp-api.md#cpp_device) {                                      |
| &nbsp;&nbsp; void [setDampingConstant](brake.md#wb_brake_set_damping_constant)(double dampingConstant) const; |
| &nbsp;&nbsp; int [getType](brake.md#wb_brake_set_damping_constant)() const;                                   |
| };                                                                                                            |

<a name="cpp_camera"/>

|                                                                                                               |
| ------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Camera.hpp`>`                                                                              |
| class [Camera](camera.md#camera) : public [Device](cpp-api.md#cpp_device) {                                   |
| &nbsp;&nbsp; enum {COLOR, RANGE\_FINDER, BOTH};                                                               |
| &nbsp;&nbsp; virtual void [enable](camera.md#wb_camera_enable)(int ms);                                       |
| &nbsp;&nbsp; virtual void [disable](camera.md#wb_camera_enable)();                                            |
| &nbsp;&nbsp; int [getSamplingPeriod](camera.md#wb_camera_enable)();                                           |
| &nbsp;&nbsp; double [getFov](camera.md#wb_camera_get_fov)() const;                                            |
| &nbsp;&nbsp; double [getMinFov](camera.md#wb_camera_get_fov)() const;                                         |
| &nbsp;&nbsp; double [getMaxFov](camera.md#wb_camera_get_fov)() const;                                         |
| &nbsp;&nbsp; virtual void [setFov](camera.md#wb_camera_get_fov)(double fov);                                  |
| &nbsp;&nbsp; double [getFocalLength](camera.md#wb_camera_get_focal_length)() const;                           |
| &nbsp;&nbsp; double [getFocalDistance](camera.md#wb_camera_get_focal_length)() const;                         |
| &nbsp;&nbsp; double [getMaxFocalDistance](camera.md#wb_camera_get_focal_length)() const;                      |
| &nbsp;&nbsp; double [getMinFocalDistance](camera.md#wb_camera_get_focal_length)() const;                      |
| &nbsp;&nbsp; virtual void [setFocalDistance](camera.md#wb_camera_get_focal_length)(double focalDistance);     |
| &nbsp;&nbsp; int [getWidth](camera.md#wb_camera_get_width)() const;                                           |
| &nbsp;&nbsp; int [getHeight](camera.md#wb_camera_get_width)() const;                                          |
| &nbsp;&nbsp; double [getNear](camera.md#wb_camera_get_near)() const;                                          |
| &nbsp;&nbsp; double [getMaxRange](camera.md#wb_camera_get_range_image)() const;                               |
| &nbsp;&nbsp; int [getType](camera.md#wb_camera_get_type)() const;                                             |
| &nbsp;&nbsp; const unsigned char *[getImage](camera.md#wb_camera_get_image)() const;                          |
| &nbsp;&nbsp; static unsigned char [imageGetRed](camera.md#wb_camera_get_image)(const unsigned char *image,    |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                            |
| &nbsp;&nbsp; static unsigned char [imageGetGreen](camera.md#wb_camera_get_image)(const unsigned char *image,  |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                            |
| &nbsp;&nbsp; static unsigned char [imageGetBlue](camera.md#wb_camera_get_image)(const unsigned char *image,   |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                            |
| &nbsp;&nbsp; static unsigned char [imageGetGrey](camera.md#wb_camera_get_image)(const unsigned char *image,   |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                            |
| &nbsp;&nbsp; const float *[getRangeImage](camera.md#wb_camera_get_range_image)() const;                       |
| &nbsp;&nbsp; static float [rangeImageGetDepth](camera.md#wb_camera_get_range_image)(const float *image,       |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                            |
| &nbsp;&nbsp; int [saveImage](camera.md#wb_camera_save_image)(const std::string &filename, int quality) const; |
| };                                                                                                            |

<a name="cpp_compass"/>

|                                                                                   |
| --------------------------------------------------------------------------------- |
| #include `<`webots/Compass.hpp`>`                                                 |
| class [Compass](compass.md#compass) : public [Device](cpp-api.md#cpp_device) {    |
| &nbsp;&nbsp; virtual void [enable](compass.md#wb_compass_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](compass.md#wb_compass_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](compass.md#wb_compass_get_values)();         |
| &nbsp;&nbsp; const double *[getValues](compass.md#wb_compass_get_values)() const; |
| };                                                                                |

<a name="cpp_connector"/>

|                                                                                             |
| ------------------------------------------------------------------------------------------- |
| #include `<`webots/Connector.hpp`>`                                                         |
| class [Connector](connector.md#connector) : public [Device](cpp-api.md#cpp_device) {        |
| &nbsp;&nbsp; virtual void [enablePresence](connector.md#wb_connector_get_presence)(int ms); |
| &nbsp;&nbsp; virtual void [disablePresence](connector.md#wb_connector_get_presence)();      |
| &nbsp;&nbsp; int [getPresence](connector.md#wb_connector_get_presence)() const;             |
| &nbsp;&nbsp; virtual void [lock](connector.md#wb_connector_lock)();                         |
| &nbsp;&nbsp; virtual void [unlock](connector.md#wb_connector_lock)();                       |
| };                                                                                          |

<a name="cpp_device"/>

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| #include `<`webots/Device.hpp`>`                                                   |
| class [Device](device.md#device) {                                                 |
| &nbsp;&nbsp; const std::string &[getModel](device.md#wb_device_get_model)() const; |
| &nbsp;&nbsp; const std::string &[getName](device.md#wb_device_get_name)() const;   |
| &nbsp;&nbsp; int [getNodeType](device.md#wb_device_get_node_type)() const;         |
| };                                                                                 |

<a name="cpp_differential_wheels"/>

|                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/DifferentialWheels.hpp`>`                                                                                       |
| class [DifferentialWheels](differentialwheels.md#differentialwheels) : public [Robot](cpp-api.md#cpp_robot) {                      |
| &nbsp;&nbsp; [DifferentialWheels](robot.md#wb_robot_step)();                                                                       |
| &nbsp;&nbsp; virtual [~DifferentialWheels](robot.md#wb_robot_step)();                                                              |
| &nbsp;&nbsp; virtual void [setSpeed](differentialwheels.md#wb_differential_wheels_set_speed)(double left, double right);           |
| &nbsp;&nbsp; double [getLeftSpeed](differentialwheels.md#wb_differential_wheels_set_speed)() const;                                |
| &nbsp;&nbsp; double [getRightSpeed](differentialwheels.md#wb_differential_wheels_set_speed)() const;                               |
| &nbsp;&nbsp; virtual void [enableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)(int ms);                  |
| &nbsp;&nbsp; virtual void [disableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)();                       |
| &nbsp;&nbsp; int [getEncodersSamplingPeriod](differentialwheels.md#wb_differential_wheels_enable_encoders)();                      |
| &nbsp;&nbsp; double [getLeftEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)() const;                       |
| &nbsp;&nbsp; double [getRightEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)() const;                      |
| &nbsp;&nbsp; virtual void [setEncoders](differentialwheels.md#wb_differential_wheels_get_left_encoder)(double left, double right); |
| &nbsp;&nbsp; double [getMaxSpeed](differentialwheels.md#wb_differential_wheels_get_max_speed)() const;                             |
| &nbsp;&nbsp; double [getSpeedUnit](differentialwheels.md#wb_differential_wheels_get_speed_unit)() const;                           |
| };                                                                                                                                 |

<a name="cpp_display"/>

|                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Display.hpp`>`                                                                                                                                |
| class [Display](display.md#display) : public [Device](cpp-api.md#cpp_device) {                                                                                   |
| &nbsp;&nbsp; enum {RGB, RGBA, ARGB, BGRA};                                                                                                                       |
| &nbsp;&nbsp; int [getWidth](display.md#wb_display_get_width)() const;                                                                                            |
| &nbsp;&nbsp; int [getHeight](display.md#wb_display_get_width)() const;                                                                                           |
| &nbsp;&nbsp; virtual void [setColor](display.md#wb_display_set_context)(int color);                                                                              |
| &nbsp;&nbsp; virtual void [setAlpha](display.md#wb_display_set_context)(double alpha);                                                                           |
| &nbsp;&nbsp; virtual void [setOpacity](display.md#wb_display_set_context)(double opacity);                                                                       |
| &nbsp;&nbsp; virtual void [drawPixel](display.md#wb_display_draw_primitive)(int x1, int y1);                                                                     |
| &nbsp;&nbsp; virtual void [drawLine](display.md#wb_display_draw_primitive)(int x1, int y1, int x2, int y2);                                                      |
| &nbsp;&nbsp; virtual void [drawRectangle](display.md#wb_display_draw_primitive)(int x, int y, int width, int height);                                            |
| &nbsp;&nbsp; virtual void [drawOval](display.md#wb_display_draw_primitive)(int cx, int cy, int a, int b);                                                        |
| &nbsp;&nbsp; virtual void [drawPolygon](display.md#wb_display_draw_primitive)(const int *x, const int *y, int size);                                             |
| &nbsp;&nbsp; virtual void [drawText](display.md#wb_display_draw_primitive)(const std::string &txt, int x, int y);                                                |
| &nbsp;&nbsp; virtual void [fillRectangle](display.md#wb_display_draw_primitive)(int x, int y, int width, int height);                                            |
| &nbsp;&nbsp; virtual void [fillOval](display.md#wb_display_draw_primitive)(int cx, int cy, int a, int b);                                                        |
| &nbsp;&nbsp; virtual void [fillPolygon](display.md#wb_display_draw_primitive)(const int *x, const int *y, int size);                                             |
| &nbsp;&nbsp; [ImageRef](cpp-api.md#cpp_image_ref) *[imageCopy](display.md#wb_display_image_functions)(int x, int y, int width, int height) const;                |
| &nbsp;&nbsp; virtual void [imagePaste](display.md#wb_display_image_functions)([ImageRef](cpp-api.md#cpp_image_ref) *ir, int x, int y);                           |
| &nbsp;&nbsp; [ImageRef](cpp-api.md#cpp_image_ref) *[imageLoad](display.md#wb_display_image_functions)(const std::string &filename) const;                        |
| &nbsp;&nbsp; [ImageRef](cpp-api.md#cpp_image_ref) *[imageNew](display.md#wb_display_image_functions)(int width, int height, const void *data, int format) const; |
| &nbsp;&nbsp; void [imageSave](display.md#wb_display_image_functions)([ImageRef](cpp-api.md#cpp_image_ref) *ir, const std::string &filename) const;               |
| &nbsp;&nbsp; void [imageDelete](display.md#wb_display_image_functions)([ImageRef](cpp-api.md#cpp_image_ref) *ir) const;                                          |
| };                                                                                                                                                               |

<a name="cpp_distance_sensor"/>

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| #include `<`webots/DistanceSensor.hpp`>`                                                            |
| class [DistanceSensor](distancesensor.md#distancesensor) : public [Device](cpp-api.md#cpp_device) { |
| &nbsp;&nbsp; virtual void [enable](distancesensor.md#wb_distance_sensor_get_value)(int ms);         |
| &nbsp;&nbsp; virtual void [disable](distancesensor.md#wb_distance_sensor_get_value)();              |
| &nbsp;&nbsp; int [getSamplingPeriod](distancesensor.md#wb_distance_sensor_get_value)();             |
| &nbsp;&nbsp; double [getValue](distancesensor.md#wb_distance_sensor_get_value)() const;             |
| };                                                                                                  |

<a name="cpp_emitter"/>

|                                                                                          |
| ---------------------------------------------------------------------------------------- |
| #include `<`webots/Emitter.hpp`>`                                                        |
| class [Emitter](emitter.md#emitter) : public [Device](cpp-api.md#cpp_device) {           |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};                                                  |
| &nbsp;&nbsp; virtual int [send](emitter.md#wb_emitter_send)(const void *data, int size); |
| &nbsp;&nbsp; int [getChannel](emitter.md#wb_emitter_set_channel)() const;                |
| &nbsp;&nbsp; virtual void [setChannel](emitter.md#wb_emitter_set_channel)(int channel);  |
| &nbsp;&nbsp; double [getRange](emitter.md#wb_emitter_set_range)() const;                 |
| &nbsp;&nbsp; virtual void [setRange](emitter.md#wb_emitter_set_range)(double range);     |
| &nbsp;&nbsp; int [getBufferSize](emitter.md#wb_emitter_get_buffer_size)() const;         |
| };                                                                                       |

<a name="cpp_field"/>

|                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Field.hpp`>`                                                                                                                                                                             |
| class Field {                                                                                                                                                                                               |
| &nbsp;&nbsp; enum { SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, MF\_STRING, MF\_NODE }; |
| &nbsp;&nbsp; int [getType](supervisor.md#wb_supervisor_field_get)() const;                                                                                                                                  |
| &nbsp;&nbsp; std::string [getTypeName](supervisor.md#wb_supervisor_field_get)() const;                                                                                                                      |
| &nbsp;&nbsp; int [getCount](supervisor.md#wb_supervisor_field_get)() const;                                                                                                                                 |
| &nbsp;&nbsp; bool [getSFBool](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                                       |
| &nbsp;&nbsp; int [getSFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                                       |
| &nbsp;&nbsp; double [getSFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                                    |
| &nbsp;&nbsp; const double *[getSFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                             |
| &nbsp;&nbsp; const double *[getSFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                             |
| &nbsp;&nbsp; const double *[getSFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                          |
| &nbsp;&nbsp; const double *[getSFColor](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                             |
| &nbsp;&nbsp; std::string [getSFString](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                              |
| &nbsp;&nbsp; [Node](cpp-api.md#cpp_node) *[getSFNode](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                               |
| &nbsp;&nbsp; bool [getMFBool](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                              |
| &nbsp;&nbsp; int [getMFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                              |
| &nbsp;&nbsp; double [getMFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                           |
| &nbsp;&nbsp; const double *[getMFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                    |
| &nbsp;&nbsp; const double *[getMFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                    |
| &nbsp;&nbsp; const double *[getMFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                 |
| &nbsp;&nbsp; const double *[getMFColor](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                    |
| &nbsp;&nbsp; std::string [getMFString](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                     |
| &nbsp;&nbsp; [Node](cpp-api.md#cpp_node) *[getMFNode](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                      |
| &nbsp;&nbsp; void [setSFBool](supervisor.md#wb_supervisor_field_set_sf_bool)(bool value);                                                                                                                   |
| &nbsp;&nbsp; void [setSFInt32](supervisor.md#wb_supervisor_field_set_sf_bool)(int value);                                                                                                                   |
| &nbsp;&nbsp; void [setSFFloat](supervisor.md#wb_supervisor_field_set_sf_bool)(double value);                                                                                                                |
| &nbsp;&nbsp; void [setSFVec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(const double values[2]);                                                                                                      |
| &nbsp;&nbsp; void [setSFVec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(const double values[3]);                                                                                                      |
| &nbsp;&nbsp; void [setSFRotation](supervisor.md#wb_supervisor_field_set_sf_bool)(const double values[4]);                                                                                                   |
| &nbsp;&nbsp; void [setSFColor](supervisor.md#wb_supervisor_field_set_sf_bool)(const double values[3]);                                                                                                      |
| &nbsp;&nbsp; void [setSFString](supervisor.md#wb_supervisor_field_set_sf_bool)(const std::string &value);                                                                                                   |
| &nbsp;&nbsp; void [setMFBool](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, bool value);                                                                                                        |
| &nbsp;&nbsp; void [setMFInt32](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, int value);                                                                                                        |
| &nbsp;&nbsp; void [setMFFloat](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, double value);                                                                                                     |
| &nbsp;&nbsp; void [setMFVec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, const double values[2]);                                                                                           |
| &nbsp;&nbsp; void [setMFVec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, const double values[3]);                                                                                           |
| &nbsp;&nbsp; void [setMFRotation](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, const double values[4]);                                                                                        |
| &nbsp;&nbsp; void [setMFColor](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, const double values[3]);                                                                                           |
| &nbsp;&nbsp; void [setMFString](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, const std::string &value);                                                                                        |
| &nbsp;&nbsp; void [importMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(int position, const std::string &filename);                                                                              |
| &nbsp;&nbsp; void [importMFNodeFromString](supervisor.md#wb_supervisor_field_import_mf_node)(int position, const std::string &nodeString);                                                                  |
| &nbsp;&nbsp; void [removeMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(int position);                                                                                                           |
| };                                                                                                                                                                                                          |

<a name="cpp_gps"/>

|                                                                           |
| ------------------------------------------------------------------------- |
| #include `<`webots/GPS.hpp`>`                                             |
| class [GPS](gps.md#gps) : public [Device](cpp-api.md#cpp_device) {        |
| &nbsp;&nbsp; virtual void [enable](gps.md#wb_gps_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](gps.md#wb_gps_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](gps.md#wb_gps_get_values)();         |
| &nbsp;&nbsp; const double *[getValues](gps.md#wb_gps_get_values)() const; |
| };                                                                        |

<a name="cpp_gyro"/>

|                                                                             |
| --------------------------------------------------------------------------- |
| #include `<`webots/Gyro.hpp`>`                                              |
| class [Gyro](gyro.md#gyro) : public [Device](cpp-api.md#cpp_device) {       |
| &nbsp;&nbsp; virtual void [enable](gyro.md#wb_gyro_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](gyro.md#wb_gyro_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](gyro.md#wb_gyro_get_values)();         |
| &nbsp;&nbsp; const double *[getValues](gyro.md#wb_gyro_get_values)() const; |
| };                                                                          |

<a name="cpp_image_ref"/>

|                                    |
| ---------------------------------- |
| #include `<`webots/ImageRef.hpp`>` |
| class ImageRef {                   |
| };                                 |

<a name="cpp_inertial_unit"/>

|                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- |
| #include `<`webots/InertialUnit.hpp`>`                                                                     |
| class [InertialUnit](inertialunit.md#inertialunit) : public [Device](cpp-api.md#cpp_device) {              |
| &nbsp;&nbsp; virtual void [enable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(int ms);           |
| &nbsp;&nbsp; virtual void [disable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)();                |
| &nbsp;&nbsp; int [getSamplingPeriod](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)();               |
| &nbsp;&nbsp; const double *[getRollPitchYaw](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)() const; |
| };                                                                                                         |

<a name="cpp_led"/>

|                                                                    |
| ------------------------------------------------------------------ |
| #include `<`webots/LED.hpp`>`                                      |
| class [LED](led.md#led) : public [Device](cpp-api.md#cpp_device) { |
| &nbsp;&nbsp; virtual void [set](led.md#wb_led_set)(int value);     |
| &nbsp;&nbsp; int [get](led.md#wb_led_set)() const;                 |
| };                                                                 |

<a name="cpp_light_sensor"/>

|                                                                                            |
| ------------------------------------------------------------------------------------------ |
| #include `<`webots/LightSensor.hpp`>`                                                      |
| class [LightSensor](lightsensor.md#lightsensor) : public [Device](cpp-api.md#cpp_device) { |
| &nbsp;&nbsp; virtual void [enable](lightsensor.md#wb_light_sensor_get_value)(int ms);      |
| &nbsp;&nbsp; virtual void [disable](lightsensor.md#wb_light_sensor_get_value)();           |
| &nbsp;&nbsp; int [getSamplingPeriod](lightsensor.md#wb_light_sensor_get_value)();          |
| &nbsp;&nbsp; double [getValue](lightsensor.md#wb_light_sensor_get_value)() const;          |
| };                                                                                         |

<a name="cpp_motion"/>

|                                                                                  |
| -------------------------------------------------------------------------------- |
| #include `<`webots/utils/Motion.hpp`>`                                           |
| class [Motion](motion.md#motion) {                                               |
| &nbsp;&nbsp; [Motion](motion.md#wbu_motion_new)(const std::string &fileName);    |
| &nbsp;&nbsp; virtual [~Motion](motion.md#wbu_motion_new)();                      |
| &nbsp;&nbsp; bool [isValid](motion.md#wbu_motion_new)() const;                   |
| &nbsp;&nbsp; virtual void [play](motion.md#wbu_motion_play)();                   |
| &nbsp;&nbsp; virtual void [stop](motion.md#wbu_motion_play)();                   |
| &nbsp;&nbsp; virtual void [setLoop](motion.md#wbu_motion_play)(bool loop);       |
| &nbsp;&nbsp; virtual void [setReverse](motion.md#wbu_motion_play)(bool reverse); |
| &nbsp;&nbsp; bool [isOver](motion.md#wbu_motion_is_over)() const;                |
| &nbsp;&nbsp; int [getDuration](motion.md#wbu_motion_is_over)() const;            |
| &nbsp;&nbsp; int [getTime](motion.md#wbu_motion_is_over)() const;                |
| &nbsp;&nbsp; virtual void [setTime](motion.md#wbu_motion_is_over)(int time);     |
| };                                                                               |

<a name="cpp_motor"/>

|                                                                                                          |
| -------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Motor.hpp`>`                                                                          |
| class [Motor](motor.md#motor) : public [Device](cpp-api.md#cpp_device) {                                 |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};                                                                  |
| &nbsp;&nbsp; virtual void [setPosition](motor.md#wb_motor_set_position)(double position);                |
| &nbsp;&nbsp; virtual void [setVelocity](motor.md#wb_motor_set_position)(double vel);                     |
| &nbsp;&nbsp; virtual void [setAcceleration](motor.md#wb_motor_set_position)(double force);               |
| &nbsp;&nbsp; virtual void [setAvailableForce](motor.md#wb_motor_set_position)(double motor\_force);      |
| &nbsp;&nbsp; virtual void [setAvailableTorque](motor.md#wb_motor_set_position)(double motor\_torque);    |
| &nbsp;&nbsp; virtual void [setControlPID](motor.md#wb_motor_set_position)(double p, double i, double d); |
| &nbsp;&nbsp; double [getTargetPosition](motor.md#wb_motor_set_position)(double position) const;          |
| &nbsp;&nbsp; double [getMinPosition](motor.md#wb_motor_set_position)() const;                            |
| &nbsp;&nbsp; double [getMaxPosition](motor.md#wb_motor_set_position)() const;                            |
| &nbsp;&nbsp; double [getVelocity](motor.md#wb_motor_set_position)() const;                               |
| &nbsp;&nbsp; double [getMaxVelocity](motor.md#wb_motor_set_position)() const;                            |
| &nbsp;&nbsp; double [getAcceleration](motor.md#wb_motor_set_position)() const;                           |
| &nbsp;&nbsp; double [getAvailableForce](motor.md#wb_motor_set_position)() const;                         |
| &nbsp;&nbsp; double [getMaxForce](motor.md#wb_motor_set_position)() const;                               |
| &nbsp;&nbsp; double [getAvailableTorque](motor.md#wb_motor_set_position)() const;                        |
| &nbsp;&nbsp; double [getMaxTorque](motor.md#wb_motor_set_position)() const;                              |
| &nbsp;&nbsp; virtual void [enableForceFeedback](motor.md#wb_motor_enable_force_feedback)(int ms);        |
| &nbsp;&nbsp; virtual void [disableForceFeedback](motor.md#wb_motor_enable_force_feedback)();             |
| &nbsp;&nbsp; int [getForceFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)();            |
| &nbsp;&nbsp; double [getForceFeedback](motor.md#wb_motor_enable_force_feedback)() const;                 |
| &nbsp;&nbsp; virtual void [setForce](motor.md#wb_motor_set_force)(double force);                         |
| &nbsp;&nbsp; virtual void [enableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)(int ms);       |
| &nbsp;&nbsp; virtual void [disableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)();            |
| &nbsp;&nbsp; int [getTorqueFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)();           |
| &nbsp;&nbsp; double [getTorqueFeedback](motor.md#wb_motor_enable_force_feedback)() const;                |
| &nbsp;&nbsp; virtual void [setTorque](motor.md#wb_motor_set_force)(double torque);                       |
| &nbsp;&nbsp; int [getType](motor.md#wb_motor_get_type)() const;                                          |
| };                                                                                                       |

<a name="cpp_node"/>

|                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Node.hpp`>`                                                                                                          |
| class Node {                                                                                                                            |
| &nbsp;&nbsp; enum { NO\_NODE, APPEARANCE, BACKGROUND, BOX, COLOR, CONE,                                                                 |
| &nbsp;&nbsp; COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT, ELEVATION\_GRID,                                                                 |
| &nbsp;&nbsp; EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE, INDEXED\_FACE\_SET,                                                                 |
| &nbsp;&nbsp; INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT, SHAPE, SPHERE,                                                                 |
| &nbsp;&nbsp; SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM,                                                              |
| &nbsp;&nbsp; TRANSFORM, VIEWPOINT, WORLD\_INFO, CAPSULE, PLANE, ROBOT,                                                                  |
| &nbsp;&nbsp; SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID, PHYSICS, CAMERA\_ZOOM,                                                            |
| &nbsp;&nbsp; CHARGER, DAMPING, CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE,                                                               |
| &nbsp;&nbsp; CAMERA, COMPASS, CONNECTOR, DISPLAY, DISTANCE\_SENSOR,                                                                     |
| &nbsp;&nbsp; EMITTER, GPS,GYRO, LED, LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN,                                                             |
| &nbsp;&nbsp; POSITION\_SENSOR, RADIO, RECEIVER, SERVO, SPEAKER,                                                                         |
| &nbsp;&nbsp; TOUCH\_SENSOR };                                                                                                           |
| &nbsp;&nbsp; virtual void [remove](supervisor.md#wb_supervisor_node_remove)();                                                          |
| &nbsp;&nbsp; int [getId](supervisor.md#wb_supervisor_node_get_from_def)() const;                                                        |
| &nbsp;&nbsp; int [getType](supervisor.md#wb_supervisor_node_get_type)() const;                                                          |
| &nbsp;&nbsp; std::string [getTypeName](supervisor.md#wb_supervisor_node_get_type)() const;                                              |
| &nbsp;&nbsp; std::string [getBaseTypeName](supervisor.md#wb_supervisor_node_get_type)() const;                                          |
| &nbsp;&nbsp; Node *[getParentNode](supervisor.md#wb_supervisor_node_get_from_def)() const;                                              |
| &nbsp;&nbsp; [Field](cpp-api.md#cpp_field) *[getField](supervisor.md#wb_supervisor_node_get_field)(const std::string &fieldName) const; |
| &nbsp;&nbsp; const double *[getPosition](supervisor.md#wb_supervisor_node_get_position)() const;                                        |
| &nbsp;&nbsp; const double *[getOrientation](supervisor.md#wb_supervisor_node_get_position)() const;                                     |
| &nbsp;&nbsp; const double *[getCenterOfMass](supervisor.md#wb_supervisor_node_get_center_of_mass)() const;                              |
| &nbsp;&nbsp; const double *[getContactPoint](supervisor.md#wb_supervisor_node_get_contact_point)(int index) const;                      |
| &nbsp;&nbsp; int [getNumberOfContactPoints](supervisor.md#wb_supervisor_node_get_number_of_contact_points)() const;                     |
| &nbsp;&nbsp; bool [getStaticBalance](supervisor.md#wb_supervisor_node_get_static_balance)() const;                                      |
| &nbsp;&nbsp; const double * [getVelocity](supervisor.md#wb_supervisor_node_get_velocity)() const;                                       |
| &nbsp;&nbsp; void [setVelocity](supervisor.md#wb_supervisor_node_get_velocity)(const double velocity[6]);                               |
| &nbsp;&nbsp; void [resetPhysics](supervisor.md#wb_supervisor_node_reset_physics)();                                                     |
| };                                                                                                                                      |

<a name="cpp_pen"/>

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| #include `<`webots/Pen.hpp`>`                                                                    |
| class [Pen](pen.md#pen) : public [Device](cpp-api.md#cpp_device) {                               |
| &nbsp;&nbsp; virtual void [write](pen.md#wb_pen_write)(bool write);                              |
| &nbsp;&nbsp; virtual void [setInkColor](pen.md#wb_pen_set_ink_color)(int color, double density); |
| };                                                                                               |

<a name="cpp_position_sensor"/>

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| #include `<`webots/PositionSensor.hpp`>`                                                            |
| class [PositionSensor](positionsensor.md#positionsensor) : public [Device](cpp-api.md#cpp_device) { |
| &nbsp;&nbsp; enum {ANGULAR, LINEAR};                                                                |
| &nbsp;&nbsp; virtual void [enable](positionsensor.md#wb_position_sensor_get_value)(int ms);         |
| &nbsp;&nbsp; virtual void [disable](positionsensor.md#wb_position_sensor_get_value)();              |
| &nbsp;&nbsp; int [getSamplingPeriod](positionsensor.md#wb_position_sensor_get_value)();             |
| &nbsp;&nbsp; double [getValue](positionsensor.md#wb_position_sensor_get_value)() const;             |
| &nbsp;&nbsp; int [getType](positionsensor.md#wb_position_sensor_get_value)() const;                 |
| };                                                                                                  |

<a name="cpp_receiver"/>

|                                                                                                        |
| ------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Receiver.hpp`>`                                                                     |
| class [Receiver](receiver.md#receiver) : public [Device](cpp-api.md#cpp_device) {                      |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};                                                                |
| &nbsp;&nbsp; virtual void [enable](receiver.md#wb_receiver_enable)(int ms);                            |
| &nbsp;&nbsp; virtual void [disable](receiver.md#wb_receiver_enable)();                                 |
| &nbsp;&nbsp; int [getSamplingPeriod](receiver.md#wb_receiver_enable)();                                |
| &nbsp;&nbsp; int [getQueueLength](receiver.md#wb_receiver_get_queue_length)() const;                   |
| &nbsp;&nbsp; virtual void [nextPacket](receiver.md#wb_receiver_get_queue_length)();                    |
| &nbsp;&nbsp; const void *[getData](receiver.md#wb_receiver_get_data)() const;                          |
| &nbsp;&nbsp; int [getDataSize](receiver.md#wb_receiver_get_data)() const;                              |
| &nbsp;&nbsp; double [getSignalStrength](receiver.md#wb_receiver_get_signal_strength)() const;          |
| &nbsp;&nbsp; const double *[getEmitterDirection](receiver.md#wb_receiver_get_signal_strength)() const; |
| &nbsp;&nbsp; virtual void [setChannel](receiver.md#wb_receiver_set_channel)(int channel);              |
| &nbsp;&nbsp; int [getChannel](receiver.md#wb_receiver_set_channel)() const;                            |
| };                                                                                                     |

<a name="cpp_robot"/>

|                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Robot.hpp`>`                                                                                                       |
| class [Robot](robot.md#robot) {                                                                                                       |
| &nbsp;&nbsp; enum {MODE\_SIMULATION, MODE\_CROSS\_COMPILATION,                                                                        |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL};                                                                                                  |
| &nbsp;&nbsp; enum {KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT,                                                                     |
| &nbsp;&nbsp; KEYBOARD\_UP, KEYBOARD\_RIGHT, KEYBOARD\_DOWN,                                                                           |
| &nbsp;&nbsp; KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN,                                                                                    |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT,                                                                          |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT,                                                                           |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END,                                                                           |
| &nbsp;&nbsp; KEYBOARD\_KEY, KEYBOARD\_SHIFT, KEYBOARD\_CONTROL,                                                                       |
| &nbsp;&nbsp; KEYBOARD\_ALT};                                                                                                          |
| &nbsp;&nbsp; [Robot](robot.md#wb_robot_step)();                                                                                       |
| &nbsp;&nbsp; virtual [~Robot](robot.md#wb_robot_step)();                                                                              |
| &nbsp;&nbsp; virtual int [step](robot.md#wb_robot_step)(int ms);                                                                      |
| &nbsp;&nbsp; [Accelerometer](cpp-api.md#cpp_accelerometer) *[getAccelerometer](robot.md#robotgetdevice)(const std::string &name);     |
| &nbsp;&nbsp; [Brake](cpp-api.md#cpp_brake) *[getBrake](robot.md#robotgetdevice)(const std::string &name);                             |
| &nbsp;&nbsp; [Camera](cpp-api.md#cpp_camera) *[getCamera](robot.md#robotgetdevice)(const std::string &name);                          |
| &nbsp;&nbsp; [Compass](cpp-api.md#cpp_compass) *[getCompass](robot.md#robotgetdevice)(const std::string &name);                       |
| &nbsp;&nbsp; [Connector](cpp-api.md#cpp_connector) *[getConnector](robot.md#robotgetdevice)(const std::string &name);                 |
| &nbsp;&nbsp; [Display](cpp-api.md#cpp_display) *[getDisplay](robot.md#robotgetdevice)(const std::string &name);                       |
| &nbsp;&nbsp; [DistanceSensor](cpp-api.md#cpp_distance_sensor) *[getDistanceSensor](robot.md#robotgetdevice)(const std::string &name); |
| &nbsp;&nbsp; [Emitter](cpp-api.md#cpp_emitter) *[getEmitter](robot.md#robotgetdevice)(const std::string &name);                       |
| &nbsp;&nbsp; [GPS](cpp-api.md#cpp_gps) *[getGPS](robot.md#robotgetdevice)(const std::string &name);                                   |
| &nbsp;&nbsp; [Gyro](cpp-api.md#cpp_gyro) *[getGyro](robot.md#robotgetdevice)(const std::string &name);                                |
| &nbsp;&nbsp; [InertialUnit](cpp-api.md#cpp_inertial_unit) *[getInertialUnit](robot.md#robotgetdevice)(const std::string &name);       |
| &nbsp;&nbsp; [LED](cpp-api.md#cpp_led) *[getLED](robot.md#robotgetdevice)(const std::string &name);                                   |
| &nbsp;&nbsp; [LightSensor](cpp-api.md#cpp_light_sensor) *[getLightSensor](robot.md#robotgetdevice)(const std::string &name);          |
| &nbsp;&nbsp; [Motor](cpp-api.md#cpp_motor) *[getMotor](robot.md#robotgetdevice)(const std::string &name);                             |
| &nbsp;&nbsp; [Pen](cpp-api.md#cpp_pen) *[getPen](robot.md#robotgetdevice)(const std::string &name);                                   |
| &nbsp;&nbsp; [PositionSensor](cpp-api.md#cpp_position_sensor) *[getPositionSensor](robot.md#robotgetdevice)(const std::string &name); |
| &nbsp;&nbsp; [Receiver](cpp-api.md#cpp_receiver) *[getReceiver](robot.md#robotgetdevice)(const std::string &name);                    |
| &nbsp;&nbsp; [Servo](cpp-api.md#cpp_servo) *[getServo](robot.md#robotgetdevice)(const std::string &name);                             |
| &nbsp;&nbsp; [TouchSensor](cpp-api.md#cpp_touch_sensor) *[getTouchSensor](robot.md#robotgetdevice)(const std::string &name);          |
| &nbsp;&nbsp; int [getNumberOfDevices](robot.md#wb_robot_get_device_by_index)();                                                       |
| &nbsp;&nbsp; [Device](cpp-api.md#cpp_device) *[getDeviceByIndex](robot.md#wb_robot_get_device_by_index)(int index);                   |
| &nbsp;&nbsp; virtual void [batterySensorEnable](robot.md#wb_robot_battery_sensor_enable)(int ms);                                     |
| &nbsp;&nbsp; virtual void [batterySensorDisable](robot.md#wb_robot_battery_sensor_enable)();                                          |
| &nbsp;&nbsp; int [batterySensorGetSamplingPeriod](robot.md#wb_robot_battery_sensor_enable)();                                         |
| &nbsp;&nbsp; double [batterySensorGetValue](robot.md#wb_robot_battery_sensor_enable)() const;                                         |
| &nbsp;&nbsp; double [getBasicTimeStep](robot.md#wb_robot_get_basic_time_step)() const;                                                |
| &nbsp;&nbsp; int [getMode](robot.md#wb_robot_get_mode)() const;                                                                       |
| &nbsp;&nbsp; std::string [getModel](robot.md#wb_robot_get_model)() const;                                                             |
| &nbsp;&nbsp; std::string [getData](robot.md#wb_robot_get_data)() const;                                                               |
| &nbsp;&nbsp; void [setData](robot.md#wb_robot_get_data)(const std::string &data);                                                     |
| &nbsp;&nbsp; std::string [getName](robot.md#wb_robot_get_name)() const;                                                               |
| &nbsp;&nbsp; std::string [getControllerName](robot.md#wb_robot_get_controller_name)() const;                                          |
| &nbsp;&nbsp; std::string [getControllerArguments](robot.md#wb_robot_get_controller_name)() const;                                     |
| &nbsp;&nbsp; std::string [getProjectPath](robot.md#wb_robot_get_project_path)() const;                                                |
| &nbsp;&nbsp; bool [getSynchronization](robot.md#wb_robot_get_synchronization)() const;                                                |
| &nbsp;&nbsp; double [getTime](robot.md#wb_robot_get_time)() const;                                                                    |
| &nbsp;&nbsp; std::string [getWorldPath](robot.md#wb_robot_get_world_path)() const;                                                    |
| &nbsp;&nbsp; virtual void [keyboardEnable](robot.md#wb_robot_keyboard_enable)(int ms);                                                |
| &nbsp;&nbsp; virtual void [keyboardDisable](robot.md#wb_robot_keyboard_enable)();                                                     |
| &nbsp;&nbsp; int [keyboardGetKey](robot.md#wb_robot_keyboard_enable)() const;                                                         |
| &nbsp;&nbsp; int [getType](robot.md#wb_robot_get_type)() const;                                                                       |
| &nbsp;&nbsp; void *[robotWindowCustomFunction](robot.md#wb_robot_window_custom_function)(void *arg);                                  |
| };                                                                                                                                    |

<a name="cpp_servo"/>

|                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Servo.hpp`>`                                                                              |
| class [Servo](servo.md#servo) : public [Device](cpp-api.md#cpp_device) {                                     |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};                                                                      |
| &nbsp;&nbsp; virtual void [setPosition](servo.md#wb_servo_set_position)(double position);                    |
| &nbsp;&nbsp; virtual void [setVelocity](servo.md#wb_servo_set_position)(double vel);                         |
| &nbsp;&nbsp; virtual void [setAcceleration](servo.md#wb_servo_set_position)(double force);                   |
| &nbsp;&nbsp; virtual void [setMotorForce](servo.md#wb_servo_set_position)(double motor\_force);              |
| &nbsp;&nbsp; virtual void [setControlP](servo.md#wb_servo_set_position)(double p);                           |
| &nbsp;&nbsp; double [getTargetPosition](servo.md#wb_servo_set_position)(double position) const;              |
| &nbsp;&nbsp; double [getMinPosition](servo.md#wb_servo_set_position)() const;                                |
| &nbsp;&nbsp; double [getMaxPosition](servo.md#wb_servo_set_position)() const;                                |
| &nbsp;&nbsp; virtual void [enablePosition](servo.md#wb_servo_enable_position)(int ms);                       |
| &nbsp;&nbsp; virtual void [disablePosition](servo.md#wb_servo_enable_position)();                            |
| &nbsp;&nbsp; int [getPositionSamplingPeriod](servo.md#wb_servo_enable_position)();                           |
| &nbsp;&nbsp; double [getPosition](servo.md#wb_servo_enable_position)() const;                                |
| &nbsp;&nbsp; virtual void [enableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)(int ms); |
| &nbsp;&nbsp; virtual void [disableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)();      |
| &nbsp;&nbsp; int [getMotorForceFeedbackSamplingPeriod](servo.md#wb_servo_enable_motor_force_feedback)();     |
| &nbsp;&nbsp; double [getMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)() const;          |
| &nbsp;&nbsp; virtual void [setForce](servo.md#wb_servo_set_force)(double force);                             |
| &nbsp;&nbsp; int [getType](servo.md#wb_servo_get_type)() const;                                              |
| };                                                                                                           |

<a name="cpp_supervisor"/>

|                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Supervisor.hpp`>`                                                                                                                                       |
| class [Supervisor](supervisor.md#supervisor) : public [Robot](cpp-api.md#cpp_robot) {                                                                                      |
| &nbsp;&nbsp; enum {MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR};                                  |
| &nbsp;&nbsp; [Supervisor](robot.md#wb_robot_step)();                                                                                                                       |
| &nbsp;&nbsp; virtual [~Supervisor](robot.md#wb_robot_step)();                                                                                                              |
| &nbsp;&nbsp; void [exportImage](supervisor.md#wb_supervisor_export_image)(const std::string &file, int quality) const;                                                     |
| &nbsp;&nbsp; [Node](cpp-api.md#cpp_node) *[getRoot](supervisor.md#wb_supervisor_node_get_from_def)();                                                                      |
| &nbsp;&nbsp; [Node](cpp-api.md#cpp_node) *[getSelf](supervisor.md#wb_supervisor_node_get_from_def)();                                                                      |
| &nbsp;&nbsp; [Node](cpp-api.md#cpp_node) *[getFromDef](supervisor.md#wb_supervisor_node_get_from_def)(const std::string &name);                                            |
| &nbsp;&nbsp; [Node](cpp-api.md#cpp_node) *[getFromId](supervisor.md#wb_supervisor_node_get_from_def)(int id);                                                              |
| &nbsp;&nbsp; virtual void [setLabel](supervisor.md#wb_supervisor_set_label)(int id, const std::string &label, double xpos, double ypos,                                    |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency);                                                                                                     |
| &nbsp;&nbsp; virtual void [simulationQuit](supervisor.md#wb_supervisor_simulation_quit)(int status);                                                                       |
| &nbsp;&nbsp; virtual void [simulationRevert](supervisor.md#wb_supervisor_simulation_revert)();                                                                             |
| &nbsp;&nbsp; virtual void [simulationResetPhysics](supervisor.md#wb_supervisor_simulation_reset_physics)();                                                                |
| &nbsp;&nbsp; virtual void [loadWorld](supervisor.md#wb_supervisor_load_world)(const std::string &file);                                                                    |
| &nbsp;&nbsp; virtual void [saveWorld](supervisor.md#wb_supervisor_load_world)();                                                                                           |
| &nbsp;&nbsp; virtual void [saveWorld](supervisor.md#wb_supervisor_load_world)(const std::string &file);                                                                    |
| &nbsp;&nbsp; virtual void [movieStartRecording](supervisor.md#wb_supervisor_movie_start_recording)(const std::string &file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp; int acceleration, bool caption) const;                                                                                                                        |
| &nbsp;&nbsp; virtual void [movieStopRecording](supervisor.md#wb_supervisor_movie_start_recording)();                                                                       |
| &nbsp;&nbsp; int [movieGetStatus](supervisor.md#wb_supervisor_movie_start_recording)() const;                                                                              |
| &nbsp;&nbsp; virtual bool [animationStartRecording](supervisor.md#wb_supervisor_animation_start_recording)(const std::string &file);                                       |
| &nbsp;&nbsp; virtual bool [animationStopRecording](supervisor.md#wb_supervisor_animation_start_recording)();                                                               |
| };                                                                                                                                                                         |

<a name="cpp_touch_sensor"/>

|                                                                                            |
| ------------------------------------------------------------------------------------------ |
| #include `<`webots/TouchSensor.hpp`>`                                                      |
| class [TouchSensor](touchsensor.md#touchsensor) : public [Device](cpp-api.md#cpp_device) { |
| &nbsp;&nbsp; enum {BUMPER, FORCE, FORCE3D};                                                |
| &nbsp;&nbsp; virtual void [enable](touchsensor.md#wb_touch_sensor_get_values)(int ms);     |
| &nbsp;&nbsp; virtual void [disable](touchsensor.md#wb_touch_sensor_get_values)();          |
| &nbsp;&nbsp; int [getSamplingPeriod](touchsensor.md#wb_touch_sensor_get_values)();         |
| &nbsp;&nbsp; double [getValue](touchsensor.md#wb_touch_sensor_get_values)() const;         |
| &nbsp;&nbsp; const double *[getValues](touchsensor.md#wb_touch_sensor_get_values)() const; |
| &nbsp;&nbsp; int [getType](touchsensor.md#wb_touch_sensor_get_type)() const;               |
| };                                                                                         |

