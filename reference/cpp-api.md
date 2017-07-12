## C++ API

The following tables describe the C++ classes and their methods.

%api "cpp_accelerometer"

|                                                                                                        |
| ------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Accelerometer.hpp`>`                                                                |
| class [Accelerometer](accelerometer.md) : public [Device](#cpp_device) {                               |
| &nbsp;&nbsp; virtual void [enable](accelerometer.md#wb_accelerometer_get_values)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](accelerometer.md#wb_accelerometer_get_values)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](accelerometer.md#wb_accelerometer_get_values)();                  |
| &nbsp;&nbsp; const double *[getValues](accelerometer.md#wb_accelerometer_get_values)() const;          |
| };                                                                                                     |

%end

%api "cpp_brake"

|                                                                                                               |
| ------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Brake.hpp`>`                                                                               |
| class [Brake](brake.md) : public [Device](#cpp_device) {                                                      |
| &nbsp;&nbsp; void [setDampingConstant](brake.md#wb_brake_set_damping_constant)(double dampingConstant) const; |
| &nbsp;&nbsp; int [getType](brake.md#wb_brake_set_damping_constant)() const;                                   |
| };                                                                                                            |

%end

%api "cpp_camera"

|                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Camera.hpp`>`                                                                                   |
| class [Camera](camera.md) : public [Device](#cpp_device) {                                                         |
| &nbsp;&nbsp; virtual void [enable](camera.md#wb_camera_enable)(int sampling_period);                               |
| &nbsp;&nbsp; virtual void [disable](camera.md#wb_camera_enable)();                                                 |
| &nbsp;&nbsp; int [getSamplingPeriod](camera.md#wb_camera_enable)();                                                |
| &nbsp;&nbsp; double [getFov](camera.md#wb_camera_get_fov)() const;                                                 |
| &nbsp;&nbsp; double [getMinFov](camera.md#wb_camera_get_fov)() const;                                              |
| &nbsp;&nbsp; double [getMaxFov](camera.md#wb_camera_get_fov)() const;                                              |
| &nbsp;&nbsp; virtual void [setFov](camera.md#wb_camera_get_fov)(double fov);                                       |
| &nbsp;&nbsp; double [getFocalLength](camera.md#wb_camera_get_focal_length)() const;                                |
| &nbsp;&nbsp; double [getFocalDistance](camera.md#wb_camera_get_focal_length)() const;                              |
| &nbsp;&nbsp; double [getMaxFocalDistance](camera.md#wb_camera_get_focal_length)() const;                           |
| &nbsp;&nbsp; double [getMinFocalDistance](camera.md#wb_camera_get_focal_length)() const;                           |
| &nbsp;&nbsp; virtual void [setFocalDistance](camera.md#wb_camera_get_focal_length)(double focalDistance);          |
| &nbsp;&nbsp; int [getWidth](camera.md#wb_camera_get_width)() const;                                                |
| &nbsp;&nbsp; int [getHeight](camera.md#wb_camera_get_width)() const;                                               |
| &nbsp;&nbsp; double [getNear](camera.md#wb_camera_get_near)() const;                                               |
| &nbsp;&nbsp; const unsigned char *[getImage](camera.md#wb_camera_get_image)() const;                               |
| &nbsp;&nbsp; static unsigned char [imageGetRed](camera.md#wb_camera_get_image)(const unsigned char *image,         |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                                 |
| &nbsp;&nbsp; static unsigned char [imageGetGreen](camera.md#wb_camera_get_image)(const unsigned char *image,       |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                                 |
| &nbsp;&nbsp; static unsigned char [imageGetBlue](camera.md#wb_camera_get_image)(const unsigned char *image,        |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                                 |
| &nbsp;&nbsp; static unsigned char [imageGetGray](camera.md#wb_camera_get_image)(const unsigned char *image,        |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                                 |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                                 |
| &nbsp;&nbsp; int [saveImage](camera.md#wb_camera_save_image)(const std::string &filename, int quality) const;      |
| &nbsp;&nbsp; bool [hasRecognition](camera.md#wb_camera_has_recognition)() const;                                   |
| &nbsp;&nbsp; void [recognitionEnable](camera.md#wb_camera_has_recognition)(int samplingPeriod);                    |
| &nbsp;&nbsp; void [recognitionDisable](camera.md#wb_camera_has_recognition)();                                     |
| &nbsp;&nbsp; int [getRecognitionSamplingPeriod](camera.md#wb_camera_has_recognition)() const;                      |
| &nbsp;&nbsp; int [getRecognitionNumberOfObjects](camera.md#wb_camera_has_recognition)() const;                     |
| &nbsp;&nbsp; const CameraRecognitionObject *[getRecognitionObjects](camera.md#wb_camera_has_recognition)() const;  |
| };                                                                                                                 |

%end

%api "cpp_compass"

|                                                                                            |
| ------------------------------------------------------------------------------------------ |
| #include `<`webots/Compass.hpp`>`                                                          |
| class [Compass](compass.md) : public [Device](#cpp_device) {                               |
| &nbsp;&nbsp; virtual void [enable](compass.md#wb_compass_get_values)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](compass.md#wb_compass_get_values)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](compass.md#wb_compass_get_values)();                  |
| &nbsp;&nbsp; const double *[getValues](compass.md#wb_compass_get_values)() const;          |
| };                                                                                         |

%end

%api "cpp_connector"

|                                                                                                          |
| -------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Connector.hpp`>`                                                                      |
| class [Connector](connector.md) : public [Device](#cpp_device) {                                         |
| &nbsp;&nbsp; virtual void [enablePresence](connector.md#wb_connector_get_presence)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disablePresence](connector.md#wb_connector_get_presence)();                   |
| &nbsp;&nbsp; int [getPresenceSamplingPeriod](connector.md#wb_connector_get_presence)() const;            |
| &nbsp;&nbsp; int [getPresence](connector.md#wb_connector_get_presence)() const;                          |
| &nbsp;&nbsp; virtual void [lock](connector.md#wb_connector_lock)();                                      |
| &nbsp;&nbsp; virtual void [unlock](connector.md#wb_connector_lock)();                                    |
| };                                                                                                       |

%end

%api "cpp_device"

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| #include `<`webots/Device.hpp`>`                                                   |
| class [Device](device.md) {                                                        |
| &nbsp;&nbsp; const std::string &[getModel](device.md#wb_device_get_model)() const; |
| &nbsp;&nbsp; const std::string &[getName](device.md#wb_device_get_name)() const;   |
| &nbsp;&nbsp; int [getNodeType](device.md#wb_device_get_node_type)() const;         |
| };                                                                                 |

%end

%api "cpp_differential_wheels"

|                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/DifferentialWheels.hpp`>`                                                                                       |
| class [DifferentialWheels](differentialwheels.md) : public [Robot](#cpp_robot) {                                                   |
| &nbsp;&nbsp; [DifferentialWheels](robot.md#wb_robot_step)();                                                                       |
| &nbsp;&nbsp; virtual [~DifferentialWheels](robot.md#wb_robot_step)();                                                              |
| &nbsp;&nbsp; virtual void [setSpeed](differentialwheels.md#wb_differential_wheels_set_speed)(double left, double right);           |
| &nbsp;&nbsp; double [getLeftSpeed](differentialwheels.md#wb_differential_wheels_set_speed)() const;                                |
| &nbsp;&nbsp; double [getRightSpeed](differentialwheels.md#wb_differential_wheels_set_speed)() const;                               |
| &nbsp;&nbsp; virtual void [enableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)(int sampling_period);     |
| &nbsp;&nbsp; virtual void [disableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)();                       |
| &nbsp;&nbsp; int [getEncodersSamplingPeriod](differentialwheels.md#wb_differential_wheels_enable_encoders)();                      |
| &nbsp;&nbsp; double [getLeftEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)() const;                       |
| &nbsp;&nbsp; double [getRightEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)() const;                      |
| &nbsp;&nbsp; virtual void [setEncoders](differentialwheels.md#wb_differential_wheels_get_left_encoder)(double left, double right); |
| &nbsp;&nbsp; double [getMaxSpeed](differentialwheels.md#wb_differential_wheels_get_max_speed)() const;                             |
| &nbsp;&nbsp; double [getSpeedUnit](differentialwheels.md#wb_differential_wheels_get_speed_unit)() const;                           |
| };                                                                                                                                 |

%end

%api "cpp_display"

|                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Display.hpp`>`                                                                                                                          |
| class [Display](display.md) : public [Device](#cpp_device) {                                                                                               |
| &nbsp;&nbsp; enum {RGB, RGBA, ARGB, BGRA};                                                                                                                 |
| &nbsp;&nbsp; int [getWidth](display.md#wb_display_get_width)() const;                                                                                      |
| &nbsp;&nbsp; int [getHeight](display.md#wb_display_get_width)() const;                                                                                     |
| &nbsp;&nbsp; virtual void [setColor](display.md#wb_display_set_color)(int color);                                                                          |
| &nbsp;&nbsp; virtual void [setAlpha](display.md#wb_display_set_color)(double alpha);                                                                       |
| &nbsp;&nbsp; virtual void [setOpacity](display.md#wb_display_set_color)(double opacity);                                                                   |
| &nbsp;&nbsp; virtual void [setFont](display.md#wb_display_set_color)(const std::string &font, int size, bool antiAliasing);                                |
| &nbsp;&nbsp; virtual void [attachCamera](display.md#wb_display_attach_camera)(Camera *camera);                                                             |
| &nbsp;&nbsp; virtual void [detachCamera](display.md#wb_display_attach_camera)();                                                                           |
| &nbsp;&nbsp; virtual void [drawPixel](display.md#wb_display_draw_pixel)(int x1, int y1);                                                                   |
| &nbsp;&nbsp; virtual void [drawLine](display.md#wb_display_draw_pixel)(int x1, int y1, int x2, int y2);                                                    |
| &nbsp;&nbsp; virtual void [drawRectangle](display.md#wb_display_draw_pixel)(int x, int y, int width, int height);                                          |
| &nbsp;&nbsp; virtual void [drawOval](display.md#wb_display_draw_pixel)(int cx, int cy, int a, int b);                                                      |
| &nbsp;&nbsp; virtual void [drawPolygon](display.md#wb_display_draw_pixel)(const int *x, const int *y, int size);                                           |
| &nbsp;&nbsp; virtual void [drawText](display.md#wb_display_draw_pixel)(const std::string &txt, int x, int y);                                              |
| &nbsp;&nbsp; virtual void [fillRectangle](display.md#wb_display_draw_pixel)(int x, int y, int width, int height);                                          |
| &nbsp;&nbsp; virtual void [fillOval](display.md#wb_display_draw_pixel)(int cx, int cy, int a, int b);                                                      |
| &nbsp;&nbsp; virtual void [fillPolygon](display.md#wb_display_draw_pixel)(const int *x, const int *y, int size);                                           |
| &nbsp;&nbsp; [ImageRef](#cpp_image_ref) *[imageCopy](display.md#wb_display_image_new)(int x, int y, int width, int height) const;                          |
| &nbsp;&nbsp; virtual void [imagePaste](display.md#wb_display_image_new)([ImageRef](#cpp_image_ref) *ir, int x, int y, blend=false);                        |
| &nbsp;&nbsp; [ImageRef](#cpp_image_ref) *[imageLoad](display.md#wb_display_image_new)(const std::string &filename) const;                                  |
| &nbsp;&nbsp; [ImageRef](#cpp_image_ref) *[imageNew](display.md#wb_display_image_new)(int width, int height, const void *data, int format) const;           |
| &nbsp;&nbsp; void [imageSave](display.md#wb_display_image_new)([ImageRef](#cpp_image_ref) *ir, const std::string &filename) const;                         |
| &nbsp;&nbsp; void [imageDelete](display.md#wb_display_image_new)([ImageRef](#cpp_image_ref) *ir) const;                                                    |
| };                                                                                                                                                         |

%end

%api "cpp_distance_sensor"

|                                                                                                          |
| -------------------------------------------------------------------------------------------------------- |
| #include `<`webots/DistanceSensor.hpp`>`                                                                 |
| class [DistanceSensor](distancesensor.md) : public [Device](#cpp_device) {                               |
| &nbsp;&nbsp; enum {GENERIC, INFRA\_RED, SONAR, LASER};                                                   |
| &nbsp;&nbsp; virtual void [enable](distancesensor.md#wb_distance_sensor_get_value)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](distancesensor.md#wb_distance_sensor_get_value)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](distancesensor.md#wb_distance_sensor_get_value)();                  |
| &nbsp;&nbsp; double [getValue](distancesensor.md#wb_distance_sensor_get_value)() const;                  |
| &nbsp;&nbsp; double [getMaxRange](distancesensor.md#wb_distance_sensor_get_max_range)() const;           |
| &nbsp;&nbsp; double [getMinRange](distancesensor.md#wb_distance_sensor_get_max_range)() const;           |
| &nbsp;&nbsp; double [getAperture](distancesensor.md#wb_distance_sensor_get_max_range)() const;           |
| &nbsp;&nbsp; int [getType](distancesensor.md#wb_distance_sensor_get_type)() const;                       |
| };                                                                                                       |

%end

%api "cpp_emitter"

|                                                                                          |
| ---------------------------------------------------------------------------------------- |
| #include `<`webots/Emitter.hpp`>`                                                        |
| class [Emitter](emitter.md) : public [Device](#cpp_device) {                             |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};                                                  |
| &nbsp;&nbsp; virtual int [send](emitter.md#wb_emitter_send)(const void *data, int size); |
| &nbsp;&nbsp; int [getChannel](emitter.md#wb_emitter_set_channel)() const;                |
| &nbsp;&nbsp; virtual void [setChannel](emitter.md#wb_emitter_set_channel)(int channel);  |
| &nbsp;&nbsp; double [getRange](emitter.md#wb_emitter_set_range)() const;                 |
| &nbsp;&nbsp; virtual void [setRange](emitter.md#wb_emitter_set_range)(double range);     |
| &nbsp;&nbsp; int [getBufferSize](emitter.md#wb_emitter_get_buffer_size)() const;         |
| };                                                                                       |

%end

%api "cpp_field"

|                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Field.hpp`>`                                                                                                                                                                             |
| class Field {                                                                                                                                                                                               |
| &nbsp;&nbsp; enum { SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, MF\_STRING, MF\_NODE }; |
| &nbsp;&nbsp; int [getType](supervisor.md#wb_supervisor_field_get_type)() const;                                                                                                                             |
| &nbsp;&nbsp; std::string [getTypeName](supervisor.md#wb_supervisor_field_get_type)() const;                                                                                                                 |
| &nbsp;&nbsp; int [getCount](supervisor.md#wb_supervisor_field_get_type)() const;                                                                                                                            |
| &nbsp;&nbsp; bool [getSFBool](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                                       |
| &nbsp;&nbsp; int [getSFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                                       |
| &nbsp;&nbsp; double [getSFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                                    |
| &nbsp;&nbsp; const double *[getSFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                             |
| &nbsp;&nbsp; const double *[getSFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                             |
| &nbsp;&nbsp; const double *[getSFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                          |
| &nbsp;&nbsp; const double *[getSFColor](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                             |
| &nbsp;&nbsp; std::string [getSFString](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                              |
| &nbsp;&nbsp; [Node](#cpp_node) *[getSFNode](supervisor.md#wb_supervisor_field_get_sf_bool)() const;                                                                                                         |
| &nbsp;&nbsp; bool [getMFBool](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                              |
| &nbsp;&nbsp; int [getMFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                              |
| &nbsp;&nbsp; double [getMFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                           |
| &nbsp;&nbsp; const double *[getMFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                    |
| &nbsp;&nbsp; const double *[getMFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                    |
| &nbsp;&nbsp; const double *[getMFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                 |
| &nbsp;&nbsp; const double *[getMFColor](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                    |
| &nbsp;&nbsp; std::string [getMFString](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                     |
| &nbsp;&nbsp; [Node](#cpp_node) *[getMFNode](supervisor.md#wb_supervisor_field_get_sf_bool)(int index) const;                                                                                                |
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
| &nbsp;&nbsp; void [insertMFBool](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, bool value);                                                                                                  |
| &nbsp;&nbsp; void [insertMFInt32](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, int value);                                                                                                  |
| &nbsp;&nbsp; void [insertMFFloat](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, double value);                                                                                               |
| &nbsp;&nbsp; void [insertMFVec2f](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, const double values[2]);                                                                                     |
| &nbsp;&nbsp; void [insertMFVec3f](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, const double values[3]);                                                                                     |
| &nbsp;&nbsp; void [insertMFRotation](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, const double values[4]);                                                                                  |
| &nbsp;&nbsp; void [insertMFColor](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, const double values[3]);                                                                                     |
| &nbsp;&nbsp; void [insertMFString](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index, const std::string &value);                                                                                  |
| &nbsp;&nbsp; void [removeMFBool](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                              |
| &nbsp;&nbsp; void [removeMFInt32](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                             |
| &nbsp;&nbsp; void [removeMFFloat](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                             |
| &nbsp;&nbsp; void [removeMFVec2f](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                             |
| &nbsp;&nbsp; void [removeMFVec3f](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                             |
| &nbsp;&nbsp; void [removeMFRotation](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                          |
| &nbsp;&nbsp; void [removeMFColor](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                             |
| &nbsp;&nbsp; void [removeMFString](supervisor.md#wb_supervisor_field_insert_mf_bool)(int index);                                                                                                            |
| &nbsp;&nbsp; void [importMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(int position, const std::string &filename);                                                                              |
| &nbsp;&nbsp; void [importMFNodeFromString](supervisor.md#wb_supervisor_field_import_mf_node)(int position, const std::string &nodeString);                                                                  |
| &nbsp;&nbsp; void [removeMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(int position);                                                                                                           |
| };                                                                                                                                                                                                          |

%end

%api "cpp_gps"

|                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/GPS.hpp`>`                                                                                                             |
| class [GPS](gps.md) : public [Device](#cpp_device) {                                                                                      |
| &nbsp;&nbsp; enum {LOCAL, WGS84};                                                                                                         |
| &nbsp;&nbsp; virtual void [enable](gps.md#wb_gps_get_values)(int sampling_period);                                                        |
| &nbsp;&nbsp; virtual void [disable](gps.md#wb_gps_get_values)();                                                                          |
| &nbsp;&nbsp; int [getSamplingPeriod](gps.md#wb_gps_get_values)();                                                                         |
| &nbsp;&nbsp; const double *[getValues](gps.md#wb_gps_get_values)() const;                                                                 |
| &nbsp;&nbsp; const double [getSpeed](gps.md#wb_gps_get_values)() const;                                                                   |
| &nbsp;&nbsp; const int [getCoordinateSystem](gps.md#wb_gps_get_coordinate_system)() const;                                                |
| &nbsp;&nbsp; static std::string [convertToDegreesMinutesSeconds](gps.md#wb_gps_convert_to_degrees_minutes_seconds)(double decimalDegree); |
| };                                                                                                                                        |

%end

%api "cpp_gyro"

|                                                                                      |
| ------------------------------------------------------------------------------------ |
| #include `<`webots/Gyro.hpp`>`                                                       |
| class [Gyro](gyro.md) : public [Device](#cpp_device) {                               |
| &nbsp;&nbsp; virtual void [enable](gyro.md#wb_gyro_get_values)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](gyro.md#wb_gyro_get_values)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](gyro.md#wb_gyro_get_values)();                  |
| &nbsp;&nbsp; const double *[getValues](gyro.md#wb_gyro_get_values)() const;          |
| };                                                                                   |

%end

%api "cpp_image_ref"

|                                    |
| ---------------------------------- |
| #include `<`webots/ImageRef.hpp`>` |
| class ImageRef {                   |
| };                                 |

%end

%api "cpp_inertial_unit"

|                                                                                                               |
| ------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/InertialUnit.hpp`>`                                                                        |
| class [InertialUnit](inertialunit.md) : public [Device](#cpp_device) {                                        |
| &nbsp;&nbsp; virtual void [enable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)();                  |
| &nbsp;&nbsp; const double *[getRollPitchYaw](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)() const;    |
| };                                                                                                            |

%end

%api "cpp_joystick"

|                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Joystick.hpp`>`                                                                           |
| class [Joystick](joystick.md) {                                                                              |
| &nbsp;&nbsp; virtual void [enable](joystick.md#wb_joystick_enable)(int sampling_period);                     |
| &nbsp;&nbsp; virtual void [disable](joystick.md#wb_joystick_enable)();                                       |
| &nbsp;&nbsp; int [getSamplingPeriod](joystick.md#wb_joystick_enable)();                                      |
| &nbsp;&nbsp; bool [isConnected](joystick.md#wb_joystick_is_connected)() const;                               |
| &nbsp;&nbsp; int [getNumberOfAxes](joystick.md#wb_joystick_get_number_of_axes)() const;                      |
| &nbsp;&nbsp; int [getAxisValue](joystick.md#wb_joystick_get_number_of_axes)(int axis) const;                 |
| &nbsp;&nbsp; int [getPressedButton](joystick.md#wb_joystick_get_pressed_button)() const;                     |
| &nbsp;&nbsp; void [setConstantForce](joystick.md#wb_joystick_set_constant_force)(int level);                 |
| &nbsp;&nbsp; void [setConstantForceDuration](joystick.md#wb_joystick_set_constant_force)(double duration);   |
| &nbsp;&nbsp; void [setAutoCenteringGain](joystick.md#wb_joystick_set_constant_force)(double gain);           |
| &nbsp;&nbsp; void [setResistanceGain](joystick.md#wb_joystick_set_constant_force)(double gain);              |
| };                                                                                                           |

%end

%api "cpp_keyboard"

|                                                                                          |
| ---------------------------------------------------------------------------------------- |
| #include `<`webots/Keyboard.hpp`>`                                                       |
| class [Keyboard](keyboard.md) {                                                          |
| &nbsp;&nbsp; enum {END, HOME, LEFT, UP, RIGHT, DOWN,                                     |
| &nbsp;&nbsp; PAGEUP, PAGEDOWN, NUMPAD\_HOME, NUMPAD\_LEFT,                               |
| &nbsp;&nbsp; NUMPAD\_UP, NUMPAD\_RIGHT, NUMPAD\_DOWN, NUMPAD\_END,                       |
| &nbsp;&nbsp; KEY, SHIFT, CONTROL, ALT};                                                  |
| &nbsp;&nbsp; virtual void [enable](keyboard.md#wb_keyboard_enable)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](keyboard.md#wb_keyboard_enable)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](keyboard.md#wb_keyboard_enable)();                  |
| &nbsp;&nbsp; int [getKey](keyboard.md#wb_keyboard_enable)() const;                       |
| };                                                                                       |

%end

%api "cpp_led"

|                                                                |
| -------------------------------------------------------------- |
| #include `<`webots/LED.hpp`>`                                  |
| class [LED](led.md) : public [Device](#cpp_device) {           |
| &nbsp;&nbsp; virtual void [set](led.md#wb_led_set)(int value); |
| &nbsp;&nbsp; int [get](led.md#wb_led_set)() const;             |
| };                                                             |

%end

%api "cpp_lidar"

|                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Lidar.hpp`>`                                                                                                      |
| class [Lidar](lidar.md) : public [Device](#cpp_device) {                                                                             |
| &nbsp;&nbsp; virtual void [enable](lidar.md#wb_lidar_enable)(int sampling_period);                                                   |
| &nbsp;&nbsp; void [enablePointCloud](lidar.md#wb_lidar_enable_point_cloud)();                                                        |
| &nbsp;&nbsp; virtual void [disable](lidar.md#wb_lidar_enable)();                                                                     |
| &nbsp;&nbsp; void [disablePointCloud](lidar.md#wb_lidar_enable_point_cloud)();                                                       |
| &nbsp;&nbsp; int [getSamplingPeriod](lidar.md#wb_lidar_enable)() const;                                                              |
| &nbsp;&nbsp; bool [isPointCloudEnabled](lidar.md#wb_lidar_enable_point_cloud)();                                                     |
| &nbsp;&nbsp; const float * [getRangeImage](lidar.md#wb_lidar_get_range_image)() const;                                               |
| &nbsp;&nbsp; const float * [getLayerRangeImage](lidar.md#wb_lidar_get_range_image)(int layer) const;                                 |
| &nbsp;&nbsp; const [LidarPoint](lidar.md#wblidarpoint) * [getPointCloud](lidar.md#wb_lidar_get_point_cloud)() const;                 |
| &nbsp;&nbsp; const [LidarPoint](lidar.md#wblidarpoint) * [getLayerPointCloud](lidar.md#wb_lidar_get_point_cloud)(int layer) const;   |
| &nbsp;&nbsp; int [getNumberOfPoints](lidar.md#wb_lidar_get_point_cloud)() const;                                                     |
| &nbsp;&nbsp; double [getFrequency](lidar.md#wb_lidar_get_frequency)() const;                                                         |
| &nbsp;&nbsp; void [setFrequency](lidar.md#wb_lidar_get_frequency)(double frequency);                                                 |
| &nbsp;&nbsp; int [getHorizontalResolution](lidar.md#wb_lidar_get_horizontal_resolution)() const;                                     |
| &nbsp;&nbsp; int [getNumberOfLayers](lidar.md#wb_lidar_get_horizontal_resolution)() const;                                           |
| &nbsp;&nbsp; double [getMinFrequency](lidar.md#wb_lidar_get_min_frequency)() const;                                                  |
| &nbsp;&nbsp; double [getMaxFrequency](lidar.md#wb_lidar_get_min_frequency)() const;                                                  |
| &nbsp;&nbsp; double [getFov](lidar.md#wb_lidar_get_fov)() const;                                                                     |
| &nbsp;&nbsp; double [getVerticalFov](lidar.md#wb_lidar_get_fov)() const;                                                             |
| &nbsp;&nbsp; double [getMinRange](lidar.md#wb_lidar_get_min_range)() const;                                                          |
| &nbsp;&nbsp; double [getMaxRange](lidar.md#wb_lidar_get_min_range)() const;                                                          |
| };                                                                                                                                   |

%end

%api "cpp_light_sensor"

|                                                                                                    |
| -------------------------------------------------------------------------------------------------- |
| #include `<`webots/LightSensor.hpp`>`                                                              |
| class [LightSensor](lightsensor.md) : public [Device](#cpp_device) {                               |
| &nbsp;&nbsp; virtual void [enable](lightsensor.md#wb_light_sensor_get_value)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](lightsensor.md#wb_light_sensor_get_value)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](lightsensor.md#wb_light_sensor_get_value)();                  |
| &nbsp;&nbsp; double [getValue](lightsensor.md#wb_light_sensor_get_value)() const;                  |
| };                                                                                                 |

%end

%api "cpp_motion"

|                                                                                  |
| -------------------------------------------------------------------------------- |
| #include `<`webots/utils/Motion.hpp`>`                                           |
| class [Motion](motion.md) {                                                      |
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

%end

%api "cpp_motor"

|                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Motor.hpp`>`                                                                                 |
| class [Motor](motor.md) : public [Device](#cpp_device) {                                                        |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};                                                                         |
| &nbsp;&nbsp; virtual void [setPosition](motor.md#wb_motor_set_position)(double position);                       |
| &nbsp;&nbsp; virtual void [setVelocity](motor.md#wb_motor_set_position)(double vel);                            |
| &nbsp;&nbsp; virtual void [setAcceleration](motor.md#wb_motor_set_position)(double force);                      |
| &nbsp;&nbsp; virtual void [setAvailableForce](motor.md#wb_motor_set_position)(double motor\_force);             |
| &nbsp;&nbsp; virtual void [setAvailableTorque](motor.md#wb_motor_set_position)(double motor\_torque);           |
| &nbsp;&nbsp; virtual void [setControlPID](motor.md#wb_motor_set_position)(double p, double i, double d);        |
| &nbsp;&nbsp; double [getTargetPosition](motor.md#wb_motor_set_position)(double position) const;                 |
| &nbsp;&nbsp; double [getMinPosition](motor.md#wb_motor_set_position)() const;                                   |
| &nbsp;&nbsp; double [getMaxPosition](motor.md#wb_motor_set_position)() const;                                   |
| &nbsp;&nbsp; double [getVelocity](motor.md#wb_motor_set_position)() const;                                      |
| &nbsp;&nbsp; double [getMaxVelocity](motor.md#wb_motor_set_position)() const;                                   |
| &nbsp;&nbsp; double [getAcceleration](motor.md#wb_motor_set_position)() const;                                  |
| &nbsp;&nbsp; double [getAvailableForce](motor.md#wb_motor_set_position)() const;                                |
| &nbsp;&nbsp; double [getMaxForce](motor.md#wb_motor_set_position)() const;                                      |
| &nbsp;&nbsp; double [getMaxTorque](motor.md#wb_motor_set_position)() const;                                     |
| &nbsp;&nbsp; double [getAvailableTorque](motor.md#wb_motor_set_position)() const;                               |
| &nbsp;&nbsp; virtual void [enableForceFeedback](motor.md#wb_motor_enable_force_feedback)(int sampling_period);  |
| &nbsp;&nbsp; virtual void [disableForceFeedback](motor.md#wb_motor_enable_force_feedback)();                    |
| &nbsp;&nbsp; int [getForceFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)();                   |
| &nbsp;&nbsp; double [getForceFeedback](motor.md#wb_motor_enable_force_feedback)() const;                        |
| &nbsp;&nbsp; virtual void [setForce](motor.md#wb_motor_set_force)(double force);                                |
| &nbsp;&nbsp; virtual void [enableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)();                   |
| &nbsp;&nbsp; int [getTorqueFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)();                  |
| &nbsp;&nbsp; double [getTorqueFeedback](motor.md#wb_motor_enable_force_feedback)() const;                       |
| &nbsp;&nbsp; virtual void [setTorque](motor.md#wb_motor_set_force)(double torque);                              |
| &nbsp;&nbsp; int [getType](motor.md#wb_motor_get_type)() const;                                                 |
| };                                                                                                              |

%end

%api "cpp_mouse"

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| #include `<`webots/Mouse.hpp`>`                                                                  |
| class [Mouse](mouse.md) {                                                                        |
| &nbsp;&nbsp; virtual void [enable](mouse.md#wb_mouse_enable)(int sampling_period);               |
| &nbsp;&nbsp; virtual void [disable](mouse.md#wb_mouse_enable)();                                 |
| &nbsp;&nbsp; int [getSamplingPeriod](mouse.md#wb_mouse_enable)();                                |
| &nbsp;&nbsp; [MouseState](mouse.md#wbmousestate) [getState](mouse.md#wb_mouse_enable)() const;   |
| };                                                                                               |

%end

%api "cpp_node"

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Node.hpp`>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| class Node {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &nbsp;&nbsp; enum { NO\_NODE, ACCELEROMETER, APPEARANCE, BACKGROUND, BALL\_JOINT, BALL\_JOINT\_PARAMETERS, BOX, BRAKE, CAMERA, CAPSULE, CHARGER, COLOR, COMPASS, CONE, CONNECTOR, CONTACT\_PROPERTIES, COORDINATE, CYLINDER, DAMPING, DIFFERENTIAL\_WHEELS, DIRECTIONAL\_LIGHT, DISPLAY, DISTANCE\_SENSOR, ELEVATION\_GRID, EMITTER, EXTRUSION, FOCUS, FLUID, FOG, GPS, GROUP, GYRO, HINGE\_2\_JOINT, HINGE\_2\_JOINT\_PARAMETERS, HINGE\_JOINT, HINGE\_JOINT\_PARAMETERS, IMAGE\_TEXTURE, IMMERSION\_PROPERTIES, INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, INERTIAL\_UNIT, JOINT\_PARAMETERS, LED, LENS\_DISTORTION, LIDAR, LIGHT\_SENSOR, LINEAR\_MOTOR, MATERIAL, MICROPHONE, PEN, PHYSICS, PLANE, POINT\_LIGHT, POSITION\_SENSOR, PROPELLER, RADAR, RADIO, RANGE\_FINDER, RECEIVER, RECOGNITION, ROBOT, ROTATIONAL\_MOTOR, SERVO, SHAPE, SLIDER\_JOINT, SLOT, SOLID, SOLID\_REFERENCE, SPEAKER, SPHERE, SPOT\_LIGHT, SUPERVISOR, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, TOUCH\_SENSOR, TRACK, TRACK\_WHEEL, TRANSFORM, VIEWPOINT, WORLD\_INFO, ZOOM }; |
| &nbsp;&nbsp; virtual void [remove](supervisor.md#wb_supervisor_node_remove)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| &nbsp;&nbsp; int [getId](supervisor.md#wb_supervisor_node_get_from_def)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| &nbsp;&nbsp; int [getType](supervisor.md#wb_supervisor_node_get_type)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| &nbsp;&nbsp; std::string [getTypeName](supervisor.md#wb_supervisor_node_get_type)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                   
| &nbsp;&nbsp; std::string [getBaseTypeName](supervisor.md#wb_supervisor_node_get_type)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| &nbsp;&nbsp; std::string [getDef](supervisor.md#wb_supervisor_node_get_def)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; Node *[getParentNode](supervisor.md#wb_supervisor_node_get_from_def)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; [Field](#cpp_field) *[getField](supervisor.md#wb_supervisor_node_get_field)(const std::string &fieldName) const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &nbsp;&nbsp; const double *[getPosition](supervisor.md#wb_supervisor_node_get_position)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| &nbsp;&nbsp; const double *[getOrientation](supervisor.md#wb_supervisor_node_get_position)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; const double *[getCenterOfMass](supervisor.md#wb_supervisor_node_get_center_of_mass)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; const double *[getContactPoint](supervisor.md#wb_supervisor_node_get_contact_point)(int index) const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; int [getNumberOfContactPoints](supervisor.md#wb_supervisor_node_get_number_of_contact_points)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; bool [getStaticBalance](supervisor.md#wb_supervisor_node_get_static_balance)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; const double * [getVelocity](supervisor.md#wb_supervisor_node_get_velocity)() const;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| &nbsp;&nbsp; void [setVelocity](supervisor.md#wb_supervisor_node_get_velocity)(const double velocity[6]);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| &nbsp;&nbsp; void [resetPhysics](supervisor.md#wb_supervisor_node_reset_physics)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; void [restartController](supervisor.md#wb_supervisor_node_restart_controller)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; void [setVisibility](supervisor.md#wb_supervisor_node_set_visibility)(Node *from, bool visible);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| };                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

%end

%api "cpp_pen"

|                                                                                                  |
| ------------------------------------------------------------------------------------------------ |
| #include `<`webots/Pen.hpp`>`                                                                    |
| class [Pen](pen.md) : public [Device](#cpp_device) {                                             |
| &nbsp;&nbsp; virtual void [write](pen.md#wb_pen_write)(bool write);                              |
| &nbsp;&nbsp; virtual void [setInkColor](pen.md#wb_pen_set_ink_color)(int color, double density); |
| };                                                                                               |

%end

%api "cpp_position_sensor"

|                                                                                                          |
| -------------------------------------------------------------------------------------------------------- |
| #include `<`webots/PositionSensor.hpp`>`                                                                 |
| class [PositionSensor](positionsensor.md) : public [Device](#cpp_device) {                               |
| &nbsp;&nbsp; enum {ANGULAR, LINEAR};                                                                     |
| &nbsp;&nbsp; virtual void [enable](positionsensor.md#wb_position_sensor_get_value)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](positionsensor.md#wb_position_sensor_get_value)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](positionsensor.md#wb_position_sensor_get_value)();                  |
| &nbsp;&nbsp; double [getValue](positionsensor.md#wb_position_sensor_get_value)() const;                  |
| &nbsp;&nbsp; int [getType](positionsensor.md#wb_position_sensor_get_value)() const;                      |
| };                                                                                                       |

%end

%api "cpp_radar"

|                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Radar.hpp`>`                                                                                |
| class [Radar](radar.md) : public [Device](#cpp_device) {                                                       |
| &nbsp;&nbsp; virtual void [enable](radar.md#wb_radar_enable)(int sampling_period);                             |
| &nbsp;&nbsp; virtual void [disable](radar.md#wb_radar_enable)();                                               |
| &nbsp;&nbsp; int [getSamplingPeriod](radar.md#wb_radar_enable)();                                              |
| &nbsp;&nbsp; int [getNumberOfTargets](radar.md#wb_radar_get_number_of_targets)() const;                        |
| &nbsp;&nbsp; const [RadarTarget](radar.md#wbradartarget) *[getTargets](radar.md#wb_radar_get_targets)() const; |
| &nbsp;&nbsp; double [getMinRange](radar.md#wb_radar_get_min_range)() const;                                    |
| &nbsp;&nbsp; double [getMaxRange](radar.md#wb_radar_get_min_range)() const;                                    |
| &nbsp;&nbsp; double [getHorizontalFov](radar.md#wb_radar_get_horizontal_fov)() const;                          |
| &nbsp;&nbsp; double [getVerticalFov](radar.md#wb_radar_get_horizontal_fov)() const;                            |
| };                                                                                                             |

%end

%api "cpp_range_finder"

|                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/RangeFinder.hpp`>`                                                                                      |
| class [RangeFinder](rangefinder.md) : public [Device](#cpp_device) {                                                       |
| &nbsp;&nbsp; virtual void [enable](rangefinder.md#wb_range_finder_enable)(int sampling_period);                            |
| &nbsp;&nbsp; virtual void [disable](rangefinder.md#wb_range_finder_enable)();                                              |
| &nbsp;&nbsp; int [getSamplingPeriod](rangefinder.md#wb_range_finder_enable)();                                             |
| &nbsp;&nbsp; double [getFov](rangefinder.md#wb_range_finder_get_fov)() const;                                              |
| &nbsp;&nbsp; int [getWidth](rangefinder.md#wb_range_finder_get_width)() const;                                             |
| &nbsp;&nbsp; int [getHeight](rangefinder.md#wb_range_finder_get_width)() const;                                            |
| &nbsp;&nbsp; double [getMinRange](rangefinder.md#wb_range_finder_get_min_range)() const;                                   |
| &nbsp;&nbsp; double [getMaxRange](rangefinder.md#wb_range_finder_get_min_range)() const;                                   |
| &nbsp;&nbsp; const unsigned char *[getRangeImage](rangefinder.md#wb_range_finder_get_range_image)() const;                 |
| &nbsp;&nbsp; static unsigned char [rangeImageGetDepth](rangefinder.md#wb_range_finder_get_range_image)(const float *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                                         |
| &nbsp;&nbsp; int [saveImage](rangefinder.md#wb_range_finder_save_image)(const std::string &filename, int quality) const;   |
| };                                                                                                                         |

%end

%api "cpp_receiver"

|                                                                                                        |
| ------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Receiver.hpp`>`                                                                     |
| class [Receiver](receiver.md) : public [Device](#cpp_device) {                                         |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};                                                                |
| &nbsp;&nbsp; virtual void [enable](receiver.md#wb_receiver_enable)(int sampling_period);               |
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

%end

%api "cpp_robot"

|                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Robot.hpp`>`                                                                                                            |
| class [Robot](robot.md) {                                                                                                                  |
| &nbsp;&nbsp; enum {MODE\_SIMULATION, MODE\_CROSS\_COMPILATION,                                                                             |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL};                                                                                                       |
| &nbsp;&nbsp; [Robot](robot.md#wb_robot_step)();                                                                                            |
| &nbsp;&nbsp; virtual [~Robot](robot.md#wb_robot_step)();                                                                                   |
| &nbsp;&nbsp; virtual int [step](robot.md#wb_robot_step)(int sampling_period);                                                              |
| &nbsp;&nbsp; [Accelerometer](#cpp_accelerometer) *[getAccelerometer](robot.md#wb_robot_get_device)(const std::string &name);               |
| &nbsp;&nbsp; [Brake](#cpp_brake) *[getBrake](robot.md#wb_robot_get_device)(const std::string &name);                                       |
| &nbsp;&nbsp; [Camera](#cpp_camera) *[getCamera](robot.md#wb_robot_get_device)(const std::string &name);                                    |
| &nbsp;&nbsp; [Compass](#cpp_compass) *[getCompass](robot.md#wb_robot_get_device)(const std::string &name);                                 |
| &nbsp;&nbsp; [Connector](#cpp_connector) *[getConnector](robot.md#wb_robot_get_device)(const std::string &name);                           |
| &nbsp;&nbsp; [Display](#cpp_display) *[getDisplay](robot.md#wb_robot_get_device)(const std::string &name);                                 |
| &nbsp;&nbsp; [DistanceSensor](#cpp_distance_sensor) *[getDistanceSensor](robot.md#wb_robot_get_device)(const std::string &name);           |
| &nbsp;&nbsp; [Emitter](#cpp_emitter) *[getEmitter](robot.md#wb_robot_get_device)(const std::string &name);                                 |
| &nbsp;&nbsp; [GPS](#cpp_gps) *[getGPS](robot.md#wb_robot_get_device)(const std::string &name);                                             |
| &nbsp;&nbsp; [Gyro](#cpp_gyro) *[getGyro](robot.md#wb_robot_get_device)(const std::string &name);                                          |
| &nbsp;&nbsp; [InertialUnit](#cpp_inertial_unit) *[getInertialUnit](robot.md#wb_robot_get_device)(const std::string &name);                 |
| &nbsp;&nbsp; [Joystick](#cpp_joystick) *getJoystick();                                                                                     |
| &nbsp;&nbsp; [Keyboard](#cpp_keyboard) *getKeyboard();                                                                                     |
| &nbsp;&nbsp; [LED](#cpp_led) *[getLED](robot.md#wb_robot_get_device)(const std::string &name);                                             |
| &nbsp;&nbsp; [Lidar](#cpp_lidar) *[getLidar](robot.md#wb_robot_get_device)(const std::string &name);                                       |
| &nbsp;&nbsp; [LightSensor](#cpp_light_sensor) *[getLightSensor](robot.md#wb_robot_get_device)(const std::string &name);                    |
| &nbsp;&nbsp; [Motor](#cpp_motor) *[getMotor](robot.md#wb_robot_get_device)(const std::string &name);                                       |
| &nbsp;&nbsp; [Mouse](#cpp_mouse) *getMouse();                                                                                              |
| &nbsp;&nbsp; [Pen](#cpp_pen) *[getPen](robot.md#wb_robot_get_device)(const std::string &name);                                             |
| &nbsp;&nbsp; [PositionSensor](#cpp_position_sensor) *[getPositionSensor](robot.md#wb_robot_get_device)(const std::string &name);           |
| &nbsp;&nbsp; [Radar](#cpp_radar) *[getRadar](robot.md#wb_robot_get_device)(const std::string &name);                                       |
| &nbsp;&nbsp; [RangeFinder](#cpp_range_finder) *[getRangeFinder](robot.md#wb_robot_get_device)(const std::string &name);                    |
| &nbsp;&nbsp; [Receiver](#cpp_receiver) *[getReceiver](robot.md#wb_robot_get_device)(const std::string &name);                              |
| &nbsp;&nbsp; [Servo](#cpp_servo) *[getServo](robot.md#wb_robot_get_device)(const std::string &name);                                       |
| &nbsp;&nbsp; [Speaker](#cpp_speaker) *[getSpeaker](robot.md#wb_robot_get_device)(const std::string &name);                                 |
| &nbsp;&nbsp; [TouchSensor](#cpp_touch_sensor) *[getTouchSensor](robot.md#wb_robot_get_device)(const std::string &name);                    |
| &nbsp;&nbsp; int [getNumberOfDevices](robot.md#wb_robot_get_device_by_index)();                                                            |
| &nbsp;&nbsp; [Device](#cpp_device) *[getDeviceByIndex](robot.md#wb_robot_get_device_by_index)(int index);                                  |
| &nbsp;&nbsp; virtual void [batterySensorEnable](robot.md#wb_robot_battery_sensor_enable)(int sampling_period);                             |
| &nbsp;&nbsp; virtual void [batterySensorDisable](robot.md#wb_robot_battery_sensor_enable)();                                               |
| &nbsp;&nbsp; int [batterySensorGetSamplingPeriod](robot.md#wb_robot_battery_sensor_enable)();                                              |
| &nbsp;&nbsp; double [batterySensorGetValue](robot.md#wb_robot_battery_sensor_enable)() const;                                              |
| &nbsp;&nbsp; double [getBasicTimeStep](robot.md#wb_robot_get_basic_time_step)() const;                                                     |
| &nbsp;&nbsp; int [getMode](robot.md#wb_robot_get_mode)() const;                                                                            |
| &nbsp;&nbsp; std::string [getModel](robot.md#wb_robot_get_model)() const;                                                                  |
| &nbsp;&nbsp; std::string [getData](robot.md#wb_robot_get_data)() const;                                                                    |
| &nbsp;&nbsp; void [setData](robot.md#wb_robot_get_data)(const std::string &data);                                                          |
| &nbsp;&nbsp; std::string [getName](robot.md#wb_robot_get_name)() const;                                                                    |
| &nbsp;&nbsp; std::string [getControllerName](robot.md#wb_robot_get_controller_name)() const;                                               |
| &nbsp;&nbsp; std::string [getControllerArguments](robot.md#wb_robot_get_controller_name)() const;                                          |
| &nbsp;&nbsp; std::string [getProjectPath](robot.md#wb_robot_get_project_path)() const;                                                     |
| &nbsp;&nbsp; bool [getSynchronization](robot.md#wb_robot_get_synchronization)() const;                                                     |
| &nbsp;&nbsp; double [getTime](robot.md#wb_robot_get_time)() const;                                                                         |
| &nbsp;&nbsp; std::string [getWorldPath](robot.md#wb_robot_get_world_path)() const;                                                         |
| &nbsp;&nbsp; int [getType](robot.md#wb_robot_get_type)() const;                                                                            |
| &nbsp;&nbsp; void *[windowCustomFunction](robot.md#wb_robot_window_custom_function)(void *arg);                                            |
| };                                                                                                                                         |

%end

%api "cpp_servo"

|                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Servo.hpp`>`                                                                                           |
| class [Servo](servo.md) : public [Device](#cpp_device) {                                                                  |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};                                                                                   |
| &nbsp;&nbsp; virtual void [setPosition](servo.md#wb_servo_set_position)(double position);                                 |
| &nbsp;&nbsp; virtual void [setVelocity](servo.md#wb_servo_set_position)(double vel);                                      |
| &nbsp;&nbsp; virtual void [setAcceleration](servo.md#wb_servo_set_position)(double force);                                |
| &nbsp;&nbsp; virtual void [setMotorForce](servo.md#wb_servo_set_position)(double motor\_force);                           |
| &nbsp;&nbsp; virtual void [setControlP](servo.md#wb_servo_set_position)(double p);                                        |
| &nbsp;&nbsp; double [getTargetPosition](servo.md#wb_servo_set_position)(double position) const;                           |
| &nbsp;&nbsp; double [getMinPosition](servo.md#wb_servo_set_position)() const;                                             |
| &nbsp;&nbsp; double [getMaxPosition](servo.md#wb_servo_set_position)() const;                                             |
| &nbsp;&nbsp; virtual void [enablePosition](servo.md#wb_servo_enable_position)(int sampling_period);                       |
| &nbsp;&nbsp; virtual void [disablePosition](servo.md#wb_servo_enable_position)();                                         |
| &nbsp;&nbsp; int [getPositionSamplingPeriod](servo.md#wb_servo_enable_position)();                                        |
| &nbsp;&nbsp; double [getPosition](servo.md#wb_servo_enable_position)() const;                                             |
| &nbsp;&nbsp; virtual void [enableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)();                   |
| &nbsp;&nbsp; double [getMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)() const;                       |
| &nbsp;&nbsp; int [getMotorForceFeedbackSamplingPeriod](servo.md#wb_servo_enable_motor_force_feedback)();                  |
| &nbsp;&nbsp; virtual void [setForce](servo.md#wb_servo_set_force)(double force);                                          |
| &nbsp;&nbsp; int [getType](servo.md#wb_servo_get_type)() const;                                                           |
| };                                                                                                                        |

%end

%api "cpp_speaker"

|                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Speaker.hpp`>`                                                                                                                                                        |
| class [Speaker](speaker.md) : public [Device](#cpp_device) {                                                                                                                             |
| &nbsp;&nbsp; static void [playSound](speaker.md#wb_speaker_play_sound)(Speaker *left, Speaker *right, const std::string &sound, double volume, double pitch, double balance, bool loop); |
| &nbsp;&nbsp; void [stop](speaker.md#wb_speaker_stop)(const std::string &sound);                                                                                                          |
| &nbsp;&nbsp; std::string [getEngine](speaker.md#wb_speaker_get_engine)();                                                                                                                |
| &nbsp;&nbsp; std::string [getLanguage](speaker.md#wb_speaker_get_language)();                                                                                                            |
| &nbsp;&nbsp; bool [setEngine](speaker.md#wb_speaker_set_engine)(const std::string &engine);                                                                                              |
| &nbsp;&nbsp; bool [setLanguage](speaker.md#wb_speaker_set_language)(const std::string &language);                                                                                        |
| &nbsp;&nbsp; void [speak](speaker.md#wb_speaker_set_language)(const std::string &text, double volume);                                                                                   |
| };                                                                                                                                                                                       |

%end

%api "cpp_supervisor"

|                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include `<`webots/Supervisor.hpp`>`                                                                                                                                       |
| class [Supervisor](supervisor.md) : public [Robot](#cpp_robot) {                                                                                                           |
| &nbsp;&nbsp; enum {SIMULATION\_MODE\_PAUSE, SIMULATION\_MODE\_REAL\_TIME, SIMULATION\_MODE\_RUN, SIMULATION\_MODE\_FAST};                                                  |
| &nbsp;&nbsp; [Supervisor](robot.md#wb_robot_step)();                                                                                                                       |
| &nbsp;&nbsp; virtual [~Supervisor](robot.md#wb_robot_step)();                                                                                                              |
| &nbsp;&nbsp; void [exportImage](supervisor.md#wb_supervisor_export_image)(const std::string &file, int quality) const;                                                     |
| &nbsp;&nbsp; [Node](#cpp_node) *[getRoot](supervisor.md#wb_supervisor_node_get_from_def)();                                                                                |
| &nbsp;&nbsp; [Node](#cpp_node) *[getSelf](supervisor.md#wb_supervisor_node_get_from_def)();                                                                                |
| &nbsp;&nbsp; [Node](#cpp_node) *[getFromDef](supervisor.md#wb_supervisor_node_get_from_def)(const std::string &name);                                                      |
| &nbsp;&nbsp; [Node](#cpp_node) *[getFromId](supervisor.md#wb_supervisor_node_get_from_def)(int id);                                                                        |
| &nbsp;&nbsp; [Node](#cpp_node) *[getSelected](supervisor.md#wb_supervisor_node_get_from_def)();                                                                            |
| &nbsp;&nbsp; virtual void [setLabel](supervisor.md#wb_supervisor_set_label)(int id, const std::string &label, double xpos, double ypos,                                    |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency, const std::string &font="Arial");                                                                    |
| &nbsp;&nbsp; virtual void [simulationQuit](supervisor.md#wb_supervisor_simulation_quit)(int status);                                                                       |
| &nbsp;&nbsp; virtual void [simulationRevert](supervisor.md#wb_supervisor_simulation_revert)();                                                                             |
| &nbsp;&nbsp; virtual void [simulationResetPhysics](supervisor.md#wb_supervisor_simulation_reset_physics)();                                                                |
| &nbsp;&nbsp; virtual void [simulationSetMode](supervisor.md#wb_supervisor_simulation_set_mode)(int mode);                                                                  |
| &nbsp;&nbsp; int [simulationGetMode](supervisor.md#wb_supervisor_simulation_set_mode)() const;                                                                             |
| &nbsp;&nbsp; virtual void [loadWorld](supervisor.md#wb_supervisor_load_world)(const std::string &file);                                                                    |
| &nbsp;&nbsp; virtual void [saveWorld](supervisor.md#wb_supervisor_load_world)();                                                                                           |
| &nbsp;&nbsp; virtual void [saveWorld](supervisor.md#wb_supervisor_load_world)(const std::string &file);                                                                    |
| &nbsp;&nbsp; virtual void [movieStartRecording](supervisor.md#wb_supervisor_movie_start_recording)(const std::string &file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp; int acceleration, bool caption) const;                                                                                                                        |
| &nbsp;&nbsp; virtual void [movieStopRecording](supervisor.md#wb_supervisor_movie_start_recording)();                                                                       |
| &nbsp;&nbsp; bool [movieIsReady](supervisor.md#wb_supervisor_movie_start_recording)() const;                                                                               |
| &nbsp;&nbsp; bool [movieFailed](supervisor.md#wb_supervisor_movie_start_recording)() const;                                                                                |
| &nbsp;&nbsp; virtual bool [animationStartRecording](supervisor.md#wb_supervisor_animation_start_recording)(const std::string &file);                                       |
| &nbsp;&nbsp; virtual bool [animationStopRecording](supervisor.md#wb_supervisor_animation_start_recording)();                                                               |
| &nbsp;&nbsp; bool [virtualRealityHeadsetIsUsed](supervisor.md#wb_supervisor_virtual_reality_headset_is_used)();                                                            |
| &nbsp;&nbsp; const double *[virtualRealityHeadsetGetPosition](supervisor.md#wb_supervisor_virtual_reality_headset_is_used)();                                              |
| &nbsp;&nbsp; const double *[virtualRealityHeadsetGetOrientation](supervisor.md#wb_supervisor_virtual_reality_headset_is_used)();                                           |
| };                                                                                                                                                                         |

%end

%api "cpp_touch_sensor"

|                                                                                                     |
| --------------------------------------------------------------------------------------------------- |
| #include `<`webots/TouchSensor.hpp`>`                                                               |
| class [TouchSensor](touchsensor.md) : public [Device](#cpp_device) {                                |
| &nbsp;&nbsp; enum {BUMPER, FORCE, FORCE3D};                                                         |
| &nbsp;&nbsp; virtual void [enable](touchsensor.md#wb_touch_sensor_get_values)(int sampling_period); |
| &nbsp;&nbsp; virtual void [disable](touchsensor.md#wb_touch_sensor_get_values)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](touchsensor.md#wb_touch_sensor_get_values)();                  |
| &nbsp;&nbsp; double [getValue](touchsensor.md#wb_touch_sensor_get_values)() const;                  |
| &nbsp;&nbsp; const double *[getValues](touchsensor.md#wb_touch_sensor_get_values)() const;          |
| &nbsp;&nbsp; int [getType](touchsensor.md#wb_touch_sensor_get_type)() const;                        |
| };                                                                                                  |

%end
