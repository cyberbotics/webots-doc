## Java API

The following tables describe the Java classes and their methods.

%api "java_accelerometer"

|                                                                                                       |
| ----------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Accelerometer;                                               |
| public class [Accelerometer](accelerometer.md) extends [Device](#java_device) {                       |
| &nbsp;&nbsp; public void [enable](accelerometer.md#wb_accelerometer_get_values)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](accelerometer.md#wb_accelerometer_get_values)();                   |
| &nbsp;&nbsp; int [getSamplingPeriod](accelerometer.md#wb_accelerometer_get_values)();                 |
| &nbsp;&nbsp; public double[] [getValues](accelerometer.md#wb_accelerometer_get_values)();             |
| }                                                                                                     |

%end

%api "java_brake"

|                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Brake;                                                                |
| public class [Brake](brake.md) extends [Device](#java_device) {                                                |
| &nbsp;&nbsp; public void [setDampingConstant](brake.md#wb_brake_set_damping_constant)(double dampingConstant); |
| &nbsp;&nbsp; public int [getType](brake.md#wb_brake_set_damping_constant)();                                   |
| }                                                                                                              |

%end

%api "java_camera"

|                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Camera;                                                                     |
| public class [Camera](camera.md) extends [Device](#java_device) {                                                    |
| &nbsp;&nbsp; public void [enable](camera.md#wb_camera_enable)(int sampling_period);                                  |
| &nbsp;&nbsp; public void [disable](camera.md#wb_camera_enable)();                                                    |
| &nbsp;&nbsp; public int [getSamplingPeriod](camera.md#wb_camera_enable)();                                           |
| &nbsp;&nbsp; public double [getFov](camera.md#wb_camera_get_fov)();                                                  |
| &nbsp;&nbsp; public double [getMinFov](camera.md#wb_camera_get_fov)();                                               |
| &nbsp;&nbsp; public double [getMaxFov](camera.md#wb_camera_get_fov)();                                               |
| &nbsp;&nbsp; public void [setFov](camera.md#wb_camera_get_fov)(double fov);                                          |
| &nbsp;&nbsp; public double [getFocalLength](camera.md#wb_camera_get_focal_length)();                                 |
| &nbsp;&nbsp; public double [getFocalDistance](camera.md#wb_camera_get_focal_length)();                               |
| &nbsp;&nbsp; public double [getMaxFocalDistance](camera.md#wb_camera_get_focal_length)();                            |
| &nbsp;&nbsp; public double [getMinFocalDistance](camera.md#wb_camera_get_focal_length)();                            |
| &nbsp;&nbsp; public void [setFocalDistance](camera.md#wb_camera_get_focal_length)(double focalDistance);             |
| &nbsp;&nbsp; public int [getWidth](camera.md#wb_camera_get_width)();                                                 |
| &nbsp;&nbsp; public int [getHeight](camera.md#wb_camera_get_width)();                                                |
| &nbsp;&nbsp; public double [getNear](camera.md#wb_camera_get_near)();                                                |
| &nbsp;&nbsp; public int[] [getImage](camera.md#wb_camera_get_image)();                                               |
| &nbsp;&nbsp; public static int [imageGetRed](camera.md#wb_camera_get_image)(int[] image, int width, int x, int y);   |
| &nbsp;&nbsp; public static int [imageGetGreen](camera.md#wb_camera_get_image)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetBlue](camera.md#wb_camera_get_image)(int[] image, int width, int x, int y);  |
| &nbsp;&nbsp; public static int [imageGetGray](camera.md#wb_camera_get_image)(int[] image, int width, int x, int y);  |
| &nbsp;&nbsp; public static int [pixelGetRed](camera.md#wb_camera_get_image)(int pixel);                              |
| &nbsp;&nbsp; public static int [pixelGetGreen](camera.md#wb_camera_get_image)(int pixel);                            |
| &nbsp;&nbsp; public static int [pixelGetBlue](camera.md#wb_camera_get_image)(int pixel);                             |
| &nbsp;&nbsp; public static int [pixelGetGray](camera.md#wb_camera_get_image)(int pixel);                             |
| &nbsp;&nbsp; public int [saveImage](camera.md#wb_camera_save_image)(String filename, int quality);                   |
| &nbsp;&nbsp; public boolean [hasRecognition](camera.md#wb_camera_has_recognition)();                                 |
| &nbsp;&nbsp; public void [recognitionEnable](camera.md#wb_camera_has_recognition)(int samplingPeriod);               |
| &nbsp;&nbsp; public void [recognitionDisable](camera.md#wb_camera_has_recognition)();                                |
| &nbsp;&nbsp; public int [getRecognitionSamplingPeriod](camera.md#wb_camera_has_recognition)();                       |
| &nbsp;&nbsp; public int [getRecognitionNumberOfObjects](camera.md#wb_camera_has_recognition)();                      |
| &nbsp;&nbsp; public const CameraRecognitionObject *[getRecognitionObjects](camera.md#wb_camera_has_recognition)();   |
| }                                                                                                                    |

%end

%api "camera_recognition_object"

|                                                                   |
| ----------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.CameraRecognitionObject; |
| public class CameraRecognitionObject {                            |
| &nbsp;&nbsp; public int getId();                                  |
| &nbsp;&nbsp; public double[] getPosition();                       |
| &nbsp;&nbsp; public double[] getOrientation();                    |
| &nbsp;&nbsp; public double[] getSize();                           |
| &nbsp;&nbsp; public int[] getPositionOnImage();                   |
| &nbsp;&nbsp; public int[] getSizeOnImage();                       |
| &nbsp;&nbsp; public int getNumberOfColors();                      |
| &nbsp;&nbsp; public double[] getColors();                         |
| &nbsp;&nbsp; public String getNam]();                             |
| }                                                                 |

%end

%api "java_compass"

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Compass;                                         |
| public class [Compass](compass.md) extends [Device](#java_device) {                       |
| &nbsp;&nbsp; public void [enable](compass.md#wb_compass_get_values)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](compass.md#wb_compass_get_values)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](compass.md#wb_compass_get_values)();          |
| &nbsp;&nbsp; public double[] [getValues](compass.md#wb_compass_get_values)();             |
| }                                                                                         |

%end

%api "java_connector"

|                                                                                                         |
| ------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Connector;                                                     |
| public class [Connector](connector.md) extends [Device](#java_device) {                                 |
| &nbsp;&nbsp; public void [enablePresence](connector.md#wb_connector_get_presence)(int sampling_period); |
| &nbsp;&nbsp; public void [disablePresence](connector.md#wb_connector_get_presence)();                   |
| &nbsp;&nbsp; public int [getPresenceSamplingPeriod](connector.md#wb_connector_get_presence)();          |
| &nbsp;&nbsp; public int [getPresence](connector.md#wb_connector_get_presence)();                        |
| &nbsp;&nbsp; public void [lock](connector.md#wb_connector_lock)();                                      |
| &nbsp;&nbsp; public void [unlock](connector.md#wb_connector_lock)();                                    |
| }                                                                                                       |

%end

%api "java_device"

|                                                                             |
| --------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Device;                            |
| public class [Device](device.md) {                                          |
| &nbsp;&nbsp; public String [getModel](device.md#wb_device_get_model)();     |
| &nbsp;&nbsp; public String [getName](device.md#wb_device_get_name)();       |
| &nbsp;&nbsp; public int [getNodeType](device.md#wb_device_get_node_type)(); |
| }                                                                           |

%end

%api "java_differential_wheels"

|                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.DifferentialWheels;                                                                      |
| public class [DifferentialWheels](differentialwheels.md) extends [Robot](#java_robot) {                                           |
| &nbsp;&nbsp; public [DifferentialWheels](robot.md#wb_robot_step)();                                                               |
| &nbsp;&nbsp; protected void [finalize](robot.md#wb_robot_step)();                                                                 |
| &nbsp;&nbsp; public void [setSpeed](differentialwheels.md#wb_differential_wheels_set_speed)(double left, double right);           |
| &nbsp;&nbsp; public double [getLeftSpeed](differentialwheels.md#wb_differential_wheels_set_speed)();                              |
| &nbsp;&nbsp; public double [getRightSpeed](differentialwheels.md#wb_differential_wheels_set_speed)();                             |
| &nbsp;&nbsp; public void [enableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)(int sampling_period);     |
| &nbsp;&nbsp; public void [disableEncoders](differentialwheels.md#wb_differential_wheels_enable_encoders)();                       |
| &nbsp;&nbsp; public int [getEncodersSamplingPeriod](differentialwheels.md#wb_differential_wheels_enable_encoders)();              |
| &nbsp;&nbsp; public double [getLeftEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)();                     |
| &nbsp;&nbsp; public double [getRightEncoder](differentialwheels.md#wb_differential_wheels_get_left_encoder)();                    |
| &nbsp;&nbsp; public void [setEncoders](differentialwheels.md#wb_differential_wheels_get_left_encoder)(double left, double right); |
| &nbsp;&nbsp; public double [getMaxSpeed](differentialwheels.md#wb_differential_wheels_get_max_speed)();                           |
| &nbsp;&nbsp; public double [getSpeedUnit](differentialwheels.md#wb_differential_wheels_get_speed_unit)();                         |
| }                                                                                                                                 |

%end

%api "java_display"

|                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Display;                                                                                                      |
| public class [Display](display.md) extends [Device](#java_device) {                                                                                    |
| &nbsp;&nbsp; public final static int RGB, RGBA, ARGB, BGRA;                                                                                            |
| &nbsp;&nbsp; public int [getWidth](display.md#wb_display_get_width)();                                                                                 |
| &nbsp;&nbsp; public int [getHeight](display.md#wb_display_get_width)();                                                                                |
| &nbsp;&nbsp; public void [setColor](display.md#wb_display_set_color)(int color);                                                                       |
| &nbsp;&nbsp; public void [setAlpha](display.md#wb_display_set_color)(double alpha);                                                                    |
| &nbsp;&nbsp; public void [setOpacity](display.md#wb_display_set_color)(double opacity);                                                                |
| &nbsp;&nbsp; public void [setFont](display.md#wb_display_set_color)(String font, int size, boolean antiAliasing);                                      |
| &nbsp;&nbsp; public void [attachCamera](display.md#wb_display_attach_camera)(Camera camera);                                                           |
| &nbsp;&nbsp; public void [detachCamera](display.md#wb_display_attach_camera)();                                                                        |
| &nbsp;&nbsp; public void [drawPixel](display.md#wb_display_draw_pixel)(int x1, int y1);                                                                |
| &nbsp;&nbsp; public void [drawLine](display.md#wb_display_draw_pixel)(int x1, int y1, int x2, int y2);                                                 |
| &nbsp;&nbsp; public void [drawRectangle](display.md#wb_display_draw_pixel)(int x, int y, int width, int height);                                       |
| &nbsp;&nbsp; public void [drawOval](display.md#wb_display_draw_pixel)(int cx, int cy, int a, int b);                                                   |
| &nbsp;&nbsp; public void [drawPolygon](display.md#wb_display_draw_pixel)(int[] x, int[] y);                                                            |
| &nbsp;&nbsp; public void [drawText](display.md#wb_display_draw_pixel)(String txt, int x, int y);                                                       |
| &nbsp;&nbsp; public void [fillRectangle](display.md#wb_display_draw_pixel)(int x, int y, int width, int height);                                       |
| &nbsp;&nbsp; public void [fillOval](display.md#wb_display_draw_pixel)(int cx, int cy, int a, int b);                                                   |
| &nbsp;&nbsp; public void [fillPolygon](display.md#wb_display_draw_pixel)(int[] x, int[] y);                                                            |
| &nbsp;&nbsp; public [ImageRef](#java_image_ref) [imageCopy](display.md#wb_display_image_new)(int x, int y, int width, int height);                     |
| &nbsp;&nbsp; public void [imagePaste](display.md#wb_display_image_new)([ImageRef](#java_image_ref) ir, int x, int y, boolean blend);                   |
| &nbsp;&nbsp; public [ImageRef](#java_image_ref) [imageLoad](display.md#wb_display_image_new)(String filename);                                         |
| &nbsp;&nbsp; public [ImageRef](#java_image_ref) [imageNew](display.md#wb_display_image_new)(int width, int height, int[] data, int format);            |
| &nbsp;&nbsp; public void [imageSave](display.md#wb_display_image_new)([ImageRef](#java_image_ref) ir, String filename);                                |
| &nbsp;&nbsp; public void [imageDelete](display.md#wb_display_image_new)([ImageRef](#java_image_ref) ir);                                               |
| }                                                                                                                                                      |

%end

%api "java_distance_sensor"

|                                                                                                         |
| ------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.DistanceSensor;                                                |
| public class [DistanceSensor](distancesensor.md) extends [Device](#java_device) {                       |
| &nbsp;&nbsp; public final static int GENERIC, INFRA\_RED, SONAR, LASER;                                 |
| &nbsp;&nbsp; public void [enable](distancesensor.md#wb_distance_sensor_get_value)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](distancesensor.md#wb_distance_sensor_get_value)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](distancesensor.md#wb_distance_sensor_get_value)();          |
| &nbsp;&nbsp; public double [getValue](distancesensor.md#wb_distance_sensor_get_value)();                |
| &nbsp;&nbsp; public double [getMaxRange](distancesensor.md#wb_distance_sensor_get_max_range)();         |
| &nbsp;&nbsp; public double [getMinRange](distancesensor.md#wb_distance_sensor_get_max_range)();         |
| &nbsp;&nbsp; public double [getAperture](distancesensor.md#wb_distance_sensor_get_max_range)();         |
| &nbsp;&nbsp; public int [getType](distancesensor.md#wb_distance_sensor_get_type)();                     |
| }                                                                                                       |

%end

%api "java_emitter"

|                                                                                        |
| -------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Emitter;                                      |
| public class [Emitter](emitter.md) extends [Device](#java_device) {                    |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST;                               |
| &nbsp;&nbsp; public int [send](emitter.md#wb_emitter_send)(byte[] data);               |
| &nbsp;&nbsp; public int [getChannel](emitter.md#wb_emitter_set_channel)();             |
| &nbsp;&nbsp; public void [setChannel](emitter.md#wb_emitter_set_channel)(int channel); |
| &nbsp;&nbsp; public double [getRange](emitter.md#wb_emitter_set_range)();              |
| &nbsp;&nbsp; public void [setRange](emitter.md#wb_emitter_set_range)(double range);    |
| &nbsp;&nbsp; public int [getBufferSize](emitter.md#wb_emitter_get_buffer_size)();      |
| }                                                                                      |

%end

%api "java_field"

|                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Field;                                                                                       |
| public class Field {                                                                                                                  |
| &nbsp;&nbsp; public final static int SF\_BOOL, SF\_INT32, SF\_FLOAT,                                                                  |
| &nbsp;&nbsp; SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING,                                                               |
| &nbsp;&nbsp; SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F,                                                                |
| &nbsp;&nbsp; MF\_COLOR, MF\_STRING, MF\_NODE;                                                                                         |
| &nbsp;&nbsp; public int [getType](supervisor.md#wb_supervisor_field_get_type)();                                                      |
| &nbsp;&nbsp; public String [getTypeName](supervisor.md#wb_supervisor_field_get_type)();                                               |
| &nbsp;&nbsp; public int [getCount](supervisor.md#wb_supervisor_field_get_type)();                                                     |
| &nbsp;&nbsp; public boolean [getSFBool](supervisor.md#wb_supervisor_field_get_sf_bool)();                                             |
| &nbsp;&nbsp; public int [getSFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)();                                                |
| &nbsp;&nbsp; public double [getSFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)();                                             |
| &nbsp;&nbsp; public double[] [getSFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)();                                           |
| &nbsp;&nbsp; public double[] [getSFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)();                                           |
| &nbsp;&nbsp; public double[] [getSFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)();                                        |
| &nbsp;&nbsp; public double[] [getSFColor](supervisor.md#wb_supervisor_field_get_sf_bool)();                                           |
| &nbsp;&nbsp; public String [getSFString](supervisor.md#wb_supervisor_field_get_sf_bool)();                                            |
| &nbsp;&nbsp; public [Node](#java_node) [getSFNode](supervisor.md#wb_supervisor_field_get_sf_bool)();                                  |
| &nbsp;&nbsp; public boolean [getMFBool](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                                    |
| &nbsp;&nbsp; public int [getMFInt32](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                                       |
| &nbsp;&nbsp; public double [getMFFloat](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                                    |
| &nbsp;&nbsp; public double[] [getMFVec2f](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                                  |
| &nbsp;&nbsp; public double[] [getMFVec3f](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                                  |
| &nbsp;&nbsp; public double[] [getMFColor](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                                  |
| &nbsp;&nbsp; public double[] [getMFRotation](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                               |
| &nbsp;&nbsp; public String [getMFString](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                                   |
| &nbsp;&nbsp; public [Node](#java_node) [getMFNode](supervisor.md#wb_supervisor_field_get_sf_bool)(int index);                         |
| &nbsp;&nbsp; public void [setSFBool](supervisor.md#wb_supervisor_field_set_sf_bool)(boolean value);                                   |
| &nbsp;&nbsp; public void [setSFInt32](supervisor.md#wb_supervisor_field_set_sf_bool)(int value);                                      |
| &nbsp;&nbsp; public void [setSFFloat](supervisor.md#wb_supervisor_field_set_sf_bool)(double value);                                   |
| &nbsp;&nbsp; public void [setSFVec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(double values[2]);                               |
| &nbsp;&nbsp; public void [setSFVec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(double values[3]);                               |
| &nbsp;&nbsp; public void [setSFRotation](supervisor.md#wb_supervisor_field_set_sf_bool)(double values[4]);                            |
| &nbsp;&nbsp; public void [setSFColor](supervisor.md#wb_supervisor_field_set_sf_bool)(double values[3]);                               |
| &nbsp;&nbsp; public void [setSFString](supervisor.md#wb_supervisor_field_set_sf_bool)(String value);                                  |
| &nbsp;&nbsp; public void [setMFBool](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, boolean value);                        |
| &nbsp;&nbsp; public void [setMFInt32](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, int value);                           |
| &nbsp;&nbsp; public void [setMFFloat](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, double value);                        |
| &nbsp;&nbsp; public void [setMFVec2f](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, double values[2]);                    |
| &nbsp;&nbsp; public void [setMFVec3f](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, double values[3]);                    |
| &nbsp;&nbsp; public void [setMFRotation](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, double values[4]);                 |
| &nbsp;&nbsp; public void [setMFColor](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, double values[3]);                    |
| &nbsp;&nbsp; public void [setMFString](supervisor.md#wb_supervisor_field_set_sf_bool)(int index, String value);                       |
| &nbsp;&nbsp; public void [importMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(int position, String filename);             |
| &nbsp;&nbsp; public void [importMFNodeFromString](supervisor.md#wb_supervisor_field_import_mf_node)(int position, String nodeString); |
| &nbsp;&nbsp; public void [removeMFNode](supervisor.md#wb_supervisor_field_import_mf_node)(int position);                              |
| }                                                                                                                                     |

%end

%api "java_gps"

|                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.GPS;                                                                                        |
| public class [GPS](gps.md) extends [Device](#java_device) {                                                                          |
| &nbsp;&nbsp; public final static int LOCAL, WGS84;                                                                                   |
| &nbsp;&nbsp; public void [enable](gps.md#wb_gps_get_values)(int sampling_period);                                                    |
| &nbsp;&nbsp; public void [disable](gps.md#wb_gps_get_values)();                                                                      |
| &nbsp;&nbsp; public int [getSamplingPeriod](gps.md#wb_gps_get_values)();                                                             |
| &nbsp;&nbsp; public double[] [getValues](gps.md#wb_gps_get_values)();                                                                |
| &nbsp;&nbsp; public double [getSpeed](gps.md#wb_gps_get_values)();                                                                   |
| &nbsp;&nbsp; public int [getCoordinateSystem](gps.md#wb_gps_get_coordinate_system)();                                                |
| &nbsp;&nbsp; public String [convertToDegreesMinutesSeconds](gps.md#wb_gps_convert_to_degrees_minutes_seconds)(double decimalDegree); |
| }                                                                                                                                    |

%end

%api "java_gyro"

|                                                                                     |
| ----------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Gyro;                                      |
| public class [Gyro](gyro.md) extends [Device](#java_device) {                       |
| &nbsp;&nbsp; public void [enable](gyro.md#wb_gyro_get_values)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](gyro.md#wb_gyro_get_values)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](gyro.md#wb_gyro_get_values)();          |
| &nbsp;&nbsp; public double[] [getValues](gyro.md#wb_gyro_get_values)();             |
| }                                                                                   |

%end

%api "java_image_ref"

|                                                    |
| -------------------------------------------------- |
| import com.cyberbotics.webots.controller.ImageRef; |
| public class ImageRef {                            |
| }                                                  |

%end

%api "java_inertial_unit"

|                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.InertialUnit;                                                       |
| public class [InertialUnit](inertialunit.md) extends [Device](#java_device) {                                |
| &nbsp;&nbsp; public void [enable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)();          |
| &nbsp;&nbsp; public double[] [getRollPitchYaw](inertialunit.md#wb_inertial_unit_get_roll_pitch_yaw)();       |
| }                                                                                                            |

%end

%api "java_joystick"

|                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Joystick                                                                  |
| public class [Joystick](joystick.md) {                                                                             |
| &nbsp;&nbsp; public void [enable](joystick.md#wb_joystick_enable)(int sampling_period);                            |
| &nbsp;&nbsp; public void [disable](joystick.md#wb_joystick_enable)();                                              |
| &nbsp;&nbsp; public int [getSamplingPeriod](joystick.md#wb_joystick_enable)();                                     |
| &nbsp;&nbsp; public boolean [isConnected](joystick.md#wb_joystick_is_connected)();                                 |
| &nbsp;&nbsp; public int [getNumberOfAxes](joystick.md#wb_joystick_get_number_of_axes)();                           |
| &nbsp;&nbsp; public int [getAxisValue](joystick.md#wb_joystick_get_number_of_axes)(int axis);                      |
| &nbsp;&nbsp; public int [getPressedButton](joystick.md#wb_joystick_get_pressed_button)();                          |
| &nbsp;&nbsp; public void [setConstantForce](joystick.md#wb_joystick_set_constant_force)(int level);                |
| &nbsp;&nbsp; public void [setConstantForceDuration](joystick.md#wb_joystick_set_constant_force)(double duration);  |
| &nbsp;&nbsp; public void [setAutoCenteringGain](joystick.md#wb_joystick_set_constant_force)(double gain);          |
| &nbsp;&nbsp; public void [setResistanceGain](joystick.md#wb_joystick_set_constant_force)(double gain);             |
| };                                                                                                                 |

%end

%api "java_keyboard"

|                                                                                         |
| --------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Keyboard;                                      |
| public class [Keyboard](keyboard.md) {                                                  |
| &nbsp;&nbsp; public final static int END, HOME, LEFT, UP, RIGHT,                        |
| &nbsp;&nbsp; DOWN, PAGEUP, PAGEDOWN, NUMPAD\_HOME, NUMPAD\_LEFT,                        |
| &nbsp;&nbsp; NUMPAD\_UP, NUMPAD\_RIGHT, NUMPAD\_DOWN, NUMPAD\_END,                      |
| &nbsp;&nbsp; KEY, SHIFT, CONTROL, ALT;                                                  |
| &nbsp;&nbsp; public void [enable](keyboard.md#wb_keyboard_enable)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](keyboard.md#wb_keyboard_enable)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](keyboard.md#wb_keyboard_enable)();          |
| &nbsp;&nbsp; public int [getKey](keyboard.md#wb_keyboard_enable)();                     |
| }                                                                                       |

%end

%api "java_led"

|                                                                        |
| ---------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.LED;                          |
| public class [LED](led.md) extends [Device](#java_device) {            |
| &nbsp;&nbsp; public void [set](led.md#wb_led_set)(int state);          |
| &nbsp;&nbsp; public int [get](led.md#wb_led_set)();                    |
| }                                                                      |

%end

%api "java_lidar"

|                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Lidar;                                                                                 |
| public class [Lidar](lidar.md) extends [Device](#java_device) {                                                                 |
| &nbsp;&nbsp; public void [enable](lidar.md#wb_lidar_enable)(int sampling_period);                                               |
| &nbsp;&nbsp; public void [enablePointCloud](lidar.md#wb_lidar_enable_point_cloud)();                                            |
| &nbsp;&nbsp; public void [disable](lidar.md#wb_lidar_enable)();                                                                 |
| &nbsp;&nbsp; public void [disablePointCloud](lidar.md#wb_lidar_enable_point_cloud)();                                           |
| &nbsp;&nbsp; public int [getSamplingPeriod](lidar.md#wb_lidar_enable)();                                                        |
| &nbsp;&nbsp; public boolean [isPointCloudEnabled](lidar.md#wb_lidar_enable_point_cloud)();                                      |
| &nbsp;&nbsp; public float[] [getRangeImage](lidar.md#wb_lidar_get_range_image)();                                               |
| &nbsp;&nbsp; public float[] [getLayerRangeImage](lidar.md#wb_lidar_get_range_image)(int layer);                                 |
| &nbsp;&nbsp; public [LidarPoint](lidar.md#wblidarpoint)[] [getPointCloud](lidar.md#wb_lidar_get_point_cloud)();                 |
| &nbsp;&nbsp; public [LidarPoint](lidar.md#wblidarpoint)[] [getLayerPointCloud](lidar.md#wb_lidar_get_point_cloud)(int layer);   |
| &nbsp;&nbsp; public int [getNumberOfPoints](lidar.md#wb_lidar_get_point_cloud)();                                               |
| &nbsp;&nbsp; public double [getFrequency](lidar.md#wb_lidar_get_frequency)();                                                   |
| &nbsp;&nbsp; public void [setFrequency](lidar.md#wb_lidar_get_frequency)(double frequency);                                     |
| &nbsp;&nbsp; public int [getHorizontalResolution](lidar.md#wb_lidar_get_horizontal_resolution)();                               |
| &nbsp;&nbsp; public int [getNumberOfLayers](lidar.md#wb_lidar_get_horizontal_resolution)();                                     |
| &nbsp;&nbsp; public double [getMinFrequency](lidar.md#wb_lidar_get_min_frequency)();                                            |
| &nbsp;&nbsp; public double [getMaxFrequency](lidar.md#wb_lidar_get_min_frequency)();                                            |
| &nbsp;&nbsp; public double [getFov](lidar.md#wb_lidar_get_fov)();                                                               |
| &nbsp;&nbsp; public double [getVerticalFov](lidar.md#wb_lidar_get_fov)();                                                       |
| &nbsp;&nbsp; public double [getMinRange](lidar.md#wb_lidar_get_min_range)();                                                    |
| &nbsp;&nbsp; public double [getMaxRange](lidar.md#wb_lidar_get_min_range)();                                                    |
| }                                                                                                                               |

%end

%api "java_lidar_point"

|                                                                   |
| ----------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.LidarPoint;              |
| public class [LidarPoint](lidar.md#wblidarpoint) {                |
| &nbsp;&nbsp; public double [getX](lidar.md#wblidarpoint)();       |
| &nbsp;&nbsp; public double [getY](lidar.md#wblidarpoint)();       |
| &nbsp;&nbsp; public double [getZ](lidar.md#wblidarpoint)();       |
| &nbsp;&nbsp; public double [getLayerId](lidar.md#wblidarpoint)(); |
| &nbsp;&nbsp; public double [getTime](lidar.md#wblidarpoint)();    |
| }                                                                 |

%end

%api "java_light_sensor"

|                                                                                                   |
| ------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.LightSensor;                                             |
| public class [LightSensor](lightsensor.md) extends [Device](#java_device) {                       |
| &nbsp;&nbsp; public void [enable](lightsensor.md#wb_light_sensor_get_value)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](lightsensor.md#wb_light_sensor_get_value)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](lightsensor.md#wb_light_sensor_get_value)();          |
| &nbsp;&nbsp; public double [getValue](lightsensor.md#wb_light_sensor_get_value)();                |
| }                                                                                                 |

%end

%api "java_motion"

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Motion;                                   |
| public class [Motion](motion.md) {                                                 |
| &nbsp;&nbsp; public [Motion](motion.md#wbu_motion_new)(String fileName);           |
| &nbsp;&nbsp; protected void [finalize](motion.md#wbu_motion_new)();                |
| &nbsp;&nbsp; public boolean [isValid](motion.md#wbu_motion_new)();                 |
| &nbsp;&nbsp; public void [play](motion.md#wbu_motion_play)();                      |
| &nbsp;&nbsp; public void [stop](motion.md#wbu_motion_play)();                      |
| &nbsp;&nbsp; public void [setLoop](motion.md#wbu_motion_play)(boolean loop);       |
| &nbsp;&nbsp; public void [setReverse](motion.md#wbu_motion_play)(boolean reverse); |
| &nbsp;&nbsp; public boolean [isOver](motion.md#wbu_motion_is_over)();              |
| &nbsp;&nbsp; public int [getDuration](motion.md#wbu_motion_is_over)();             |
| &nbsp;&nbsp; public int [getTime](motion.md#wbu_motion_is_over)();                 |
| &nbsp;&nbsp; public void [setTime](motion.md#wbu_motion_is_over)(int time);        |
| }                                                                                  |

%end

%api "java_motor"

|                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Motor;                                                                |
| public class [Motor](motor.md) extends [Device](#java_device) {                                                |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR;                                                       |
| &nbsp;&nbsp; public void [setPosition](motor.md#wb_motor_set_position)(double position);                       |
| &nbsp;&nbsp; public void [setVelocity](motor.md#wb_motor_set_position)(double vel);                            |
| &nbsp;&nbsp; public void [setAcceleration](motor.md#wb_motor_set_position)(double force);                      |
| &nbsp;&nbsp; public void [setAvailableForce](motor.md#wb_motor_set_position)(double motor\_force);             |
| &nbsp;&nbsp; public void [setAvailableTorque](motor.md#wb_motor_set_position)(double motor\_torque);           |
| &nbsp;&nbsp; public void [setControlPID](motor.md#wb_motor_set_position)(double p, double i, double d);        |
| &nbsp;&nbsp; public double [getTargetPosition](motor.md#wb_motor_set_position)();                              |
| &nbsp;&nbsp; public double [getMinPosition](motor.md#wb_motor_set_position)();                                 |
| &nbsp;&nbsp; public double [getMaxPosition](motor.md#wb_motor_set_position)();                                 |
| &nbsp;&nbsp; public double [getVelocity](motor.md#wb_motor_set_position)();                                    |
| &nbsp;&nbsp; public double [getMaxVelocity](motor.md#wb_motor_set_position)();                                 |
| &nbsp;&nbsp; public double [getAcceleration](motor.md#wb_motor_set_position)();                                |
| &nbsp;&nbsp; public double [getAvailableForce](motor.md#wb_motor_set_position)();                              |
| &nbsp;&nbsp; public double [getMaxForce](motor.md#wb_motor_set_position)();                                    |
| &nbsp;&nbsp; public double [getAvailableTorque](motor.md#wb_motor_set_position)();                             |
| &nbsp;&nbsp; public double [getMaxTorque](motor.md#wb_motor_set_position)();                                   |
| &nbsp;&nbsp; public void [enableForceFeedback](motor.md#wb_motor_enable_force_feedback)(int sampling_period);  |
| &nbsp;&nbsp; public void [disableForceFeedback](motor.md#wb_motor_enable_force_feedback)();                    |
| &nbsp;&nbsp; public int [getForceFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)();           |
| &nbsp;&nbsp; public double [getForceFeedback](motor.md#wb_motor_enable_force_feedback)();                      |
| &nbsp;&nbsp; public void [setForce](motor.md#wb_motor_set_force)(double force);                                |
| &nbsp;&nbsp; public void [enableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)(int sampling_period); |
| &nbsp;&nbsp; public void [disableTorqueFeedback](motor.md#wb_motor_enable_force_feedback)();                   |
| &nbsp;&nbsp; public int [getTorqueFeedbackSamplingPeriod](motor.md#wb_motor_enable_force_feedback)();          |
| &nbsp;&nbsp; public double [getTorqueFeedback](motor.md#wb_motor_enable_force_feedback)();                     |
| &nbsp;&nbsp; public void [setTorque](motor.md#wb_motor_set_force)(double torque);                              |
| &nbsp;&nbsp; public int [getType](motor.md#wb_motor_get_type)();                                               |
| }                                                                                                              |

%end

%api "java_mouse"

|                                                                                             |
| ------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Mouse;                                             |
| public class [mouse](mouse.md) {                                                            |
| &nbsp;&nbsp; public void [enable](mouse.md#wb_mouse_enable)(int sampling_period);           |
| &nbsp;&nbsp; public void [disable](mouse.md#wb_mouse_enable)();                             |
| &nbsp;&nbsp; public int [getSamplingPeriod](mouse.md#wb_mouse_enable)();                    |
| &nbsp;&nbsp; public [MouseState](#java_mouse_state) [getState](mouse.md#wb_mouse_enable)(); |
| }                                                                                           |

%end

%api "java_mouse_state"

|                                                                         |
| ----------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.MouseState;                    |
| public class [MouseState](mouse.md#wbmousestate) {                      |
| &nbsp;&nbsp; public double [getLeft](mouse.md#wbmousestate)();          |
| &nbsp;&nbsp; public double [getMiddle](mouse.md#wbmousestate)();        |
| &nbsp;&nbsp; public double [getRight](mouse.md#wbmousestate)();         |
| &nbsp;&nbsp; public double [getX](mouse.md#wbmousestate)();             |
| &nbsp;&nbsp; public double [getY](mouse.md#wbmousestate)();             |
| &nbsp;&nbsp; public double [getZ](mouse.md#wbmousestate)();             |
| &nbsp;&nbsp; public int [getSelectedNodeId()](mouse.md#wbmousestate)(); |
| }                                                                       |

%end

%api "java_node"

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Node;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| public class Node {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| &nbsp;&nbsp; public final static int NO\_NODE, ACCELEROMETER, APPEARANCE, BACKGROUND, BALL\_JOINT, BALL\_JOINT\_PARAMETERS, BOX, BRAKE, CAMERA, CAPSULE, CHARGER, COLOR, COMPASS, CONE, CONNECTOR, CONTACT\_PROPERTIES, COORDINATE, CYLINDER, DAMPING, DIFFERENTIAL\_WHEELS, DIRECTIONAL\_LIGHT, DISPLAY, DISTANCE\_SENSOR, ELEVATION\_GRID, EMITTER, EXTRUSION, FOCUS, FLUID, FOG, GPS, GROUP, GYRO, HINGE\_2\_JOINT, HINGE\_2\_JOINT\_PARAMETERS, HINGE\_JOINT, HINGE\_JOINT\_PARAMETERS, IMAGE\_TEXTURE, IMMERSION\_PROPERTIES, INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, INERTIAL\_UNIT, JOINT\_PARAMETERS, LED, LENS\_DISTORTION, LIDAR, LIGHT\_SENSOR, LINEAR\_MOTOR, MATERIAL, MICROPHONE, PEN, PHYSICS, PLANE, POINT\_LIGHT, POSITION\_SENSOR, PROPELLER, RADAR, RADIO, RANGE\_FINDER, RECEIVER, RECOGNITION, ROBOT, ROTATIONAL\_MOTOR, SERVO, SHAPE, SLIDER\_JOINT, SLOT, SOLID, SOLID\_REFERENCE, SPEAKER, SPHERE, SPOT\_LIGHT, SUPERVISOR, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, TOUCH\_SENSOR, TRACK, TRACK\_WHEEL, TRANSFORM, VIEWPOINT, WORLD\_INFO, ZOOM; |
| &nbsp;&nbsp; public void [remove](supervisor.md#wb_supervisor_node_remove)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| &nbsp;&nbsp; public int [getId](supervisor.md#wb_supervisor_node_get_from_def)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; public int [getType](supervisor.md#wb_supervisor_node_get_type)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| &nbsp;&nbsp; public String [getTypeName](supervisor.md#wb_supervisor_node_get_type)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| &nbsp;&nbsp; public String [getBaseTypeName](supervisor.md#wb_supervisor_node_get_type)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; public String [getDef](supervisor.md#wb_supervisor_node_get_def)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &nbsp;&nbsp; public [Field](#java_field) [getField](supervisor.md#wb_supervisor_node_get_field)(String fieldName);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; public Node [getParentNode](supervisor.md#wb_supervisor_node_get_from_def)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; public double[] [getPosition](supervisor.md#wb_supervisor_node_get_position)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &nbsp;&nbsp; public double[] [getOrientation](supervisor.md#wb_supervisor_node_get_position)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| &nbsp;&nbsp; public double[] [getCenterOfMass](supervisor.md#wb_supervisor_node_get_center_of_mass)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &nbsp;&nbsp; public double[] [getContactPoint](supervisor.md#wb_supervisor_node_get_contact_point)(int index);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp; public int [getNumberOfContactPoints](supervisor.md#wb_supervisor_node_get_number_of_contact_points)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; public boolean [getStaticBalance](supervisor.md#wb_supervisor_node_get_static_balance)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| &nbsp;&nbsp; public double[] [getVelocity](supervisor.md#wb_supervisor_node_get_velocity)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &nbsp;&nbsp; public void [setVelocity](supervisor.md#wb_supervisor_node_get_velocity)(double velocity[6]);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; public void [resetPhysics](supervisor.md#wb_supervisor_node_reset_physics)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; public void [restartController](supervisor.md#wb_supervisor_node_restart_controller)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; public void [setVisibility](supervisor.md#wb_supervisor_node_set_visibility)(Node from, boolean visible);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

%end

%api "java_pen"

|                                                                                                 |
| ----------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Pen;                                                   |
| public class [Pen](pen.md) extends [Device](#java_device) {                                     |
| &nbsp;&nbsp; public void [write](pen.md#wb_pen_write)(boolean write);                           |
| &nbsp;&nbsp; public void [setInkColor](pen.md#wb_pen_set_ink_color)(int color, double density); |
| }                                                                                               |

%end

%api "java_position_sensor"

|                                                                                                         |
| ------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.PositionSensor;                                                |
| public class [PositionSensor](positionsensor.md) extends [Device](#java_device) {                       |
| &nbsp;&nbsp; public final static int ANGULAR, LINEAR;                                                   |
| &nbsp;&nbsp; public void [enable](positionsensor.md#wb_position_sensor_get_value)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](positionsensor.md#wb_position_sensor_get_value)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](positionsensor.md#wb_position_sensor_get_value)();          |
| &nbsp;&nbsp; public double [getValue](positionsensor.md#wb_position_sensor_get_value)();                |
| &nbsp;&nbsp; public int [getType](positionsensor.md#wb_position_sensor_get_value)();                    |
| }                                                                                                       |

%end

%api "java_radar"

|                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Radar;                                                              |
| public class [Radar](radar.md) extends [Device](#java_device) {                                              |
| &nbsp;&nbsp; public void [enable](radar.md#wb_radar_enable)(int sampling_period);                            |
| &nbsp;&nbsp; public void [disable](radar.md#wb_radar_enable)();                                              |
| &nbsp;&nbsp; public int [getSamplingPeriod](radar.md#wb_radar_enable)();                                     |
| &nbsp;&nbsp; public int [getNumberOfTargets](radar.md#wb_radar_get_number_of_targets)();                     |
| &nbsp;&nbsp; public [RadarTarget](radar.md#wbradartarget)[] [getTargets](radar.md#wb_radar_get_targets)();   |
| &nbsp;&nbsp; public doubles [getMinRange](radar.md#wb_radar_get_min_range)();                                |
| &nbsp;&nbsp; public double [getMaxRange](radar.md#wb_radar_get_min_range)();                                 |
| &nbsp;&nbsp; public double [getHorizontalFov](radar.md#wb_radar_get_horizontal_fov)();                       |
| &nbsp;&nbsp; public double [getVerticalFov](radar.md#wb_radar_get_horizontal_fov)();                         |
| }                                                                                                            |

%end

%api "java_radar_target"

|                                                                          |
| ------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.RadarTarget;                    |
| public class [RadarTarget](radar.md#wbradartarget) {                     |
| &nbsp;&nbsp; public double [getDistance](radar.md#wbradartarget)();      |
| &nbsp;&nbsp; public double [getReceivedPower](radar.md#wbradartarget)(); |
| &nbsp;&nbsp; public double [getSpeed](radar.md#wbradartarget)();         |
| &nbsp;&nbsp; public double [getAzimuth](radar.md#wbradartarget)();       |
| }                                                                        |

%end

%api "java_range_finder"

|                                                                                                               |
| ------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.RangeFinder;                                                         |
| public class [RangeFinder](rangefinder.md) extends [Device](#java_device) {                                   |
| &nbsp;&nbsp; public void [enable](rangefinder.md#wb_range_finder_enable)(int sampling_period);                |
| &nbsp;&nbsp; public void [disable](rangefinder.md#wb_range_finder_enable)();                                  |
| &nbsp;&nbsp; public int [getSamplingPeriod](rangefinder.md#wb_range_finder_enable)();                         |
| &nbsp;&nbsp; public double [getFov](rangefinder.md#wb_range_finder_get_fov)();                                |
| &nbsp;&nbsp; public int [getWidth](rangefinder.md#wb_range_finder_get_width)();                               |
| &nbsp;&nbsp; public int [getHeight](rangefinder.md#wb_range_finder_get_width)();                              |
| &nbsp;&nbsp; public double [getMinRange](rangefinder.md#wb_range_finder_get_min_range)();                     |
| &nbsp;&nbsp; public double [getMaxRange](rangefinder.md#wb_range_finder_get_min_range)();                     |
| &nbsp;&nbsp; public double[] [getRangeImage](rangefinder.md#wb_range_finder_get_range_image)();               |
| &nbsp;&nbsp; public int [saveImage](rangefinder.md#wb_range_finder_save_image)(String filename, int quality); |
| }                                                                                                             |

%end

%api "java_receiver"

|                                                                                                    |
| -------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Receiver;                                                 |
| public class [Receiver](receiver.md) extends [Device](#java_device) {                              |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST;                                           |
| &nbsp;&nbsp; public void [enable](receiver.md#wb_receiver_enable)(int sampling_period);            |
| &nbsp;&nbsp; public void [disable](receiver.md#wb_receiver_enable)();                              |
| &nbsp;&nbsp; public int [getSamplingPeriod](receiver.md#wb_receiver_enable)();                     |
| &nbsp;&nbsp; public int [getQueueLength](receiver.md#wb_receiver_get_queue_length)();              |
| &nbsp;&nbsp; public void [nextPacket](receiver.md#wb_receiver_get_queue_length)();                 |
| &nbsp;&nbsp; public byte[] [getData](receiver.md#wb_receiver_get_data)();                          |
| &nbsp;&nbsp; public int [getDataSize](receiver.md#wb_receiver_get_data)();                         |
| &nbsp;&nbsp; public double [getSignalStrength](receiver.md#wb_receiver_get_signal_strength)();     |
| &nbsp;&nbsp; public double[] [getEmitterDirection](receiver.md#wb_receiver_get_signal_strength)(); |
| &nbsp;&nbsp; public void [setChannel](receiver.md#wb_receiver_set_channel)(int channel);           |
| &nbsp;&nbsp; public int [getChannel](receiver.md#wb_receiver_set_channel)();                       |
| }                                                                                                  |

%end

%api "java_robot"

|                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Robot;                                                                                        |
| public class [Robot](robot.md) {                                                                                                       |
| &nbsp;&nbsp; public final static int MODE\_SIMULATION,                                                                                 |
| &nbsp;&nbsp; MODE\_CROSS\_COMPILATION, MODE\_REMOTE\_CONTROL;                                                                          |
| &nbsp;&nbsp; public [Robot](robot.md#wb_robot_step)();                                                                                 |
| &nbsp;&nbsp; protected void [finalize](robot.md#wb_robot_step)();                                                                      |
| &nbsp;&nbsp; public int [step](robot.md#wb_robot_step)(int sampling_period);                                                           |
| &nbsp;&nbsp; public [Accelerometer](#java_accelerometer) [getAccelerometer](robot.md#wb_robot_get_device)(String name);                |
| &nbsp;&nbsp; public [Brake](#java_brake) [getBrake](robot.md#wb_robot_get_device)(String name);                                        |
| &nbsp;&nbsp; public [Camera](#java_camera) [getCamera](robot.md#wb_robot_get_device)(String name);                                     |
| &nbsp;&nbsp; public [Compass](#java_compass) [getCompass](robot.md#wb_robot_get_device)(String name);                                  |
| &nbsp;&nbsp; public [Connector](#java_connector) [getConnector](robot.md#wb_robot_get_device)(String name);                            |
| &nbsp;&nbsp; public [Display](#java_display) [getDisplay](robot.md#wb_robot_get_device)(String name);                                  |
| &nbsp;&nbsp; public [DistanceSensor](#java_distance_sensor) [getDistanceSensor](robot.md#wb_robot_get_device)(String name);            |
| &nbsp;&nbsp; public [Emitter](#java_emitter) [getEmitter](robot.md#wb_robot_get_device)(String name);                                  |
| &nbsp;&nbsp; public [GPS](#java_gps) [getGPS](robot.md#wb_robot_get_device)(String name);                                              |
| &nbsp;&nbsp; public [Gyro](#java_gyro) [getGyro](robot.md#wb_robot_get_device)(String name);                                           |
| &nbsp;&nbsp; public [InertialUnit](#java_inertial_unit) [getInertialUnit](robot.md#wb_robot_get_device)(String name);                  |
| &nbsp;&nbsp; public [Joystick](#java_joystick) getJoystick();                                                                          |
| &nbsp;&nbsp; public [Keyboard](#java_keyboard) getKeyboard();                                                                          |
| &nbsp;&nbsp; public [LED](#java_led) [getLED](robot.md#wb_robot_get_device)(String name);                                              |
| &nbsp;&nbsp; public [Lidar](#java_lidar) [getLidar](robot.md#wb_robot_get_device)(String name);                                        |
| &nbsp;&nbsp; public [LightSensor](#java_light_sensor) [getLightSensor](robot.md#wb_robot_get_device)(String name);                     |
| &nbsp;&nbsp; public [Motor](#java_motor) [getMotor](robot.md#wb_robot_get_device)(String name);                                        |
| &nbsp;&nbsp; public [Motor](#java_mouse) getMouse();                                                                                   |
| &nbsp;&nbsp; public [Pen](#java_pen) [getPen](robot.md#wb_robot_get_device)(String name);                                              |
| &nbsp;&nbsp; public [PositionSensor](#java_position_sensor) [getPositionSensor](robot.md#wb_robot_get_device)(String name);            |
| &nbsp;&nbsp; public [Radar](#java_radar) [getRadar](robot.md#wb_robot_get_device)(String name);                                        |
| &nbsp;&nbsp; public [RangeFinder](#java_range_finder) [getRangeFinder](robot.md#wb_robot_get_device)(String name);                     |
| &nbsp;&nbsp; public [Receiver](#java_receiver) [getReceiver](robot.md#wb_robot_get_device)(String name);                               |
| &nbsp;&nbsp; public [Servo](#java_servo) [getServo](robot.md#wb_robot_get_device)(String name);                                        |
| &nbsp;&nbsp; public [Speaker](#java_speaker) [getSpeaker](robot.md#wb_robot_get_device)(String name);                                  |
| &nbsp;&nbsp; public [TouchSensor](#java_touch_sensor) [getTouchSensor](robot.md#wb_robot_get_device)(String name);                     |
| &nbsp;&nbsp; public int [getNumberOfDevices](robot.md#wb_robot_get_device_by_index)();                                                 |
| &nbsp;&nbsp; public [Device](#java_device) [getDeviceByIndex](robot.md#wb_robot_get_device_by_index)(int index);                       |
| &nbsp;&nbsp; public void [batterySensorEnable](robot.md#wb_robot_battery_sensor_enable)(int sampling_period);                          |
| &nbsp;&nbsp; public void [batterySensorDisable](robot.md#wb_robot_battery_sensor_enable)();                                            |
| &nbsp;&nbsp; public int [batterySensorGetSamplingPeriod](robot.md#wb_robot_battery_sensor_enable)();                                   |
| &nbsp;&nbsp; public double [batterySensorGetValue](robot.md#wb_robot_battery_sensor_enable)();                                         |
| &nbsp;&nbsp; public double [getBasicTimeStep](robot.md#wb_robot_get_basic_time_step)();                                                |
| &nbsp;&nbsp; public int [getMode](robot.md#wb_robot_get_mode)();                                                                       |
| &nbsp;&nbsp; public String [getModel](robot.md#wb_robot_get_model)();                                                                  |
| &nbsp;&nbsp; public String [getData](robot.md#wb_robot_get_data)();                                                                    |
| &nbsp;&nbsp; public [setData](robot.md#wb_robot_get_data)(String data);                                                                |
| &nbsp;&nbsp; public String [getName](robot.md#wb_robot_get_name)();                                                                    |
| &nbsp;&nbsp; public String [getControllerName](robot.md#wb_robot_get_controller_name)();                                               |
| &nbsp;&nbsp; public String [getControllerArguments](robot.md#wb_robot_get_controller_name)();                                          |
| &nbsp;&nbsp; public String [getProjectPath](robot.md#wb_robot_get_project_path)();                                                     |
| &nbsp;&nbsp; public boolean [getSynchronization](robot.md#wb_robot_get_synchronization)();                                             |
| &nbsp;&nbsp; public double [getTime](robot.md#wb_robot_get_time)();                                                                    |
| &nbsp;&nbsp; public String [getWorldPath](robot.md#wb_robot_get_world_path)();                                                         |
| &nbsp;&nbsp; public int [getType](robot.md#wb_robot_get_type)();                                                                       |
| }                                                                                                                                      |

%end

%api "java_servo"

|                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Servo;                                                                          |
| public class [Servo](servo.md) extends [Device](#java_device) {                                                          |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR;                                                                 |
| &nbsp;&nbsp; public void [setPosition](servo.md#wb_servo_set_position)(double position);                                 |
| &nbsp;&nbsp; public double [getTargetPosition](servo.md#wb_servo_set_position)();                                        |
| &nbsp;&nbsp; public void [setVelocity](servo.md#wb_servo_set_position)(double vel);                                      |
| &nbsp;&nbsp; public void [setAcceleration](servo.md#wb_servo_set_position)(double force);                                |
| &nbsp;&nbsp; public void [setMotorForce](servo.md#wb_servo_set_position)(double motor\_force);                           |
| &nbsp;&nbsp; public void [setControlP](servo.md#wb_servo_set_position)(double p);                                        |
| &nbsp;&nbsp; public double [getMinPosition](servo.md#wb_servo_set_position)();                                           |
| &nbsp;&nbsp; public double [getMaxPosition](servo.md#wb_servo_set_position)();                                           |
| &nbsp;&nbsp; public void [enablePosition](servo.md#wb_servo_enable_position)(int sampling_period);                       |
| &nbsp;&nbsp; public void [disablePosition](servo.md#wb_servo_enable_position)();                                         |
| &nbsp;&nbsp; public int [getPositionSamplingPeriod](servo.md#wb_servo_enable_position)();                                |
| &nbsp;&nbsp; public double [getPosition](servo.md#wb_servo_enable_position)();                                           |
| &nbsp;&nbsp; public void [enableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)(int sampling_period); |
| &nbsp;&nbsp; public void [disableMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)();                   |
| &nbsp;&nbsp; public int [getMotorForceFeedbackSamplingPeriod](servo.md#wb_servo_enable_motor_force_feedback)();          |
| &nbsp;&nbsp; public double [getMotorForceFeedback](servo.md#wb_servo_enable_motor_force_feedback)();                     |
| &nbsp;&nbsp; public void [setForce](servo.md#wb_servo_set_force)(double force);                                          |
| &nbsp;&nbsp; public int [getType](servo.md#wb_servo_get_type)();                                                         |
| }                                                                                                                        |

%end

%api "java_speaker"

|                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Speaker;                                                                                                                                    |
| public class [Speaker](speaker.md) extends [Device](#java_device) {                                                                                                                  |
| class [Speaker](speaker.md) : public [Device](#cpp_device) {                                                                                                                         |
| &nbsp;&nbsp; public static void [playSound](speaker.md#wb_speaker_play_sound)(Speaker left, Speaker right, String sound, double volume, double pitch, double balance, boolean loop); |
| &nbsp;&nbsp; public void [stop](speaker.md#wb_speaker_stop)(const std::string &sound);                                                                                               |
| &nbsp;&nbsp; public std::string [getLanguage](speaker.md#wb_speaker_get_engine)();                                                                                                   |
| &nbsp;&nbsp; public std::string [getLanguage](speaker.md#wb_speaker_get_language)();                                                                                                 |
| &nbsp;&nbsp; public boolean [setEngine](speaker.md#wb_speaker_set_engine)(const std::string &engine);                                                                                |
| &nbsp;&nbsp; public boolean [setLanguage](speaker.md#wb_speaker_set_language)(const std::string &language);                                                                          |
| &nbsp;&nbsp; public void [speak](speaker.md#wb_speaker_set_language)(const std::string &text, double volume);                                                                        |
| };                                                                                                                                                                                   |

%end

%api "java_supervisor"

|                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Supervisor;                                                                                                          |
| public class [Supervisor](supervisor.md) extends [Robot](#java_robot) {                                                                                       |
| &nbsp;&nbsp; public final static int SIMULATION\_MODE\_PAUSE, SIMULATION\_MODE\_REAL\_TIME, SIMULATION\_MODE\_RUN, SIMULATION\_MODE\_FAST                     |
| &nbsp;&nbsp; public [Supervisor](robot.md#wb_robot_step)();                                                                                                   |
| &nbsp;&nbsp; protected void [finalize](robot.md#wb_robot_step)();                                                                                             |
| &nbsp;&nbsp; public void [exportImage](supervisor.md#wb_supervisor_export_image)(String file, int quality);                                                   |
| &nbsp;&nbsp; public [Node](#java_node) [getRoot](supervisor.md#wb_supervisor_node_get_from_def)();                                                            |
| &nbsp;&nbsp; public [Node](#java_node) [getSelf](supervisor.md#wb_supervisor_node_get_from_def)();                                                            |
| &nbsp;&nbsp; public [Node](#java_node) [getFromDef](supervisor.md#wb_supervisor_node_get_from_def)(String name);                                              |
| &nbsp;&nbsp; public [Node](#java_node) [getFromId](supervisor.md#wb_supervisor_node_get_from_def)(int id);                                                    |
| &nbsp;&nbsp; public void [setLabel](supervisor.md#wb_supervisor_set_label)(int id, String label, double xpos, double ypos,                                    |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency, String font);                                                                           |
| &nbsp;&nbsp; public void [setLabel](supervisor.md#wb_supervisor_set_label)(int id, String label, double xpos, double ypos,                                    |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency);                                                                                        |
| &nbsp;&nbsp; public void [simulationQuit](supervisor.md#wb_supervisor_simulation_quit)(int status);                                                           |
| &nbsp;&nbsp; public void [simulationRevert](supervisor.md#wb_supervisor_simulation_revert)();                                                                 |
| &nbsp;&nbsp; public void [simulationResetPhysics](supervisor.md#wb_supervisor_simulation_reset_physics)();                                                    |
| &nbsp;&nbsp; public int [simulationGetMode](supervisor.md#wb_supervisor_simulation_set_mode)();                                                               |
| &nbsp;&nbsp; public void [simulationSetMode](supervisor.md#wb_supervisor_simulation_set_mode)(int mode);                                                      |
| &nbsp;&nbsp; public void [loadWorld](supervisor.md#wb_supervisor_load_world)(String file);                                                                    |
| &nbsp;&nbsp; public void [saveWorld](supervisor.md#wb_supervisor_load_world)();                                                                               |
| &nbsp;&nbsp; public void [saveWorld](supervisor.md#wb_supervisor_load_world)(String file);                                                                    |
| &nbsp;&nbsp; public void [movieStartRecording](supervisor.md#wb_supervisor_movie_start_recording)(String file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp;&nbsp;&nbsp; int acceleration, boolean caption);                                                                                                  |
| &nbsp;&nbsp; public void [movieStopRecording](supervisor.md#wb_supervisor_movie_start_recording)();                                                           |
| &nbsp;&nbsp; public boolean [movieIsReady](supervisor.md#wb_supervisor_movie_start_recording)();                                                              |
| &nbsp;&nbsp; public boolean [movieFailed](supervisor.md#wb_supervisor_movie_start_recording)();                                                               |
| &nbsp;&nbsp; public boolean [animationStartRecording](supervisor.md#wb_supervisor_animation_start_recording)(String file);                                    |
| &nbsp;&nbsp; public boolean [animationStopRecording](supervisor.md#wb_supervisor_animation_start_recording)();                                                |
| &nbsp;&nbsp; public boolean [virtualRealityHeadsetIsUsed](supervisor.md#wb_supervisor_virtual_reality_headset_is_used)();                                     |
| &nbsp;&nbsp; public double[] [virtualRealityHeadsetGetPosition](supervisor.md#wb_supervisor_virtual_reality_headset_is_used)();                               |
| &nbsp;&nbsp; public double[] [virtualRealityHeadsetGetOrientation](supervisor.md#wb_supervisor_virtual_reality_headset_is_used)();                            |
| }                                                                                                                                                             |

%end

%api "java_touch_sensor"

|                                                                                                    |
| -------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.TouchSensor;                                              |
| public class [TouchSensor](touchsensor.md) extends [Device](#java_device) {                        |
| &nbsp;&nbsp; public final static int BUMPER, FORCE, FORCE3D;                                       |
| &nbsp;&nbsp; public void [enable](touchsensor.md#wb_touch_sensor_get_values)(int sampling_period); |
| &nbsp;&nbsp; public void [disable](touchsensor.md#wb_touch_sensor_get_values)();                   |
| &nbsp;&nbsp; public int [getSamplingPeriod](touchsensor.md#wb_touch_sensor_get_values)();          |
| &nbsp;&nbsp; public double [getValue](touchsensor.md#wb_touch_sensor_get_values)();                |
| &nbsp;&nbsp; public double[] [getValues](touchsensor.md#wb_touch_sensor_get_values)();             |
| &nbsp;&nbsp; public int [getType](touchsensor.md#wb_touch_sensor_get_type)();                      |
| }                                                                                                  |

%end
