## Java API

The following tables describe the Java classes and their methods.

%api "java_accelerometer"

|                                                                               |
| ----------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Accelerometer;                       |
| public class [Accelerometer](#accelerometer) extends [Device](#java_device) { |
| &nbsp;&nbsp; public void [enable](#wb_accelerometer_get_values)(int ms);      |
| &nbsp;&nbsp; public void [disable](#wb_accelerometer_get_values)();           |
| &nbsp;&nbsp; int [getSamplingPeriod](#wb_accelerometer_get_values)();         |
| &nbsp;&nbsp; public double[] [getValues](#wb_accelerometer_get_values)();     |
| }                                                                             |

%end

%api "java_brake"

|                                                                                                        |
| ------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Brake;                                                        |
| public class [Brake](#brake) extends [Device](#java_device) {                                          |
| &nbsp;&nbsp; public void [setDampingConstant](#wb_brake_set_damping_constant)(double dampingConstant); |
| &nbsp;&nbsp; public int [getType](#wb_brake_set_damping_constant)();                                   |
| }                                                                                                      |

%end

%api "java_camera"

|                                                                                                             |
| ----------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Camera;                                                            |
| public class [Camera](#camera) extends [Device](#java_device) {                                             |
| &nbsp;&nbsp; public final static int COLOR, RANGE\_FINDER, BOTH;                                            |
| &nbsp;&nbsp; public void [enable](#wb_camera_enable)(int ms);                                               |
| &nbsp;&nbsp; public void [disable](#wb_camera_enable)();                                                    |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_camera_enable)();                                           |
| &nbsp;&nbsp; public double [getFov](#wb_camera_get_fov)();                                                  |
| &nbsp;&nbsp; public double [getMinFov](#wb_camera_get_fov)();                                               |
| &nbsp;&nbsp; public double [getMaxFov](#wb_camera_get_fov)();                                               |
| &nbsp;&nbsp; public void [setFov](#wb_camera_get_fov)(double fov);                                          |
| &nbsp;&nbsp; public double [getFocalLength](#wb_camera_get_focal_length)();                                 |
| &nbsp;&nbsp; public double [getFocalDistance](#wb_camera_get_focal_length)();                               |
| &nbsp;&nbsp; public double [getMaxFocalDistance](#wb_camera_get_focal_length)();                            |
| &nbsp;&nbsp; public double [getMinFocalDistance](#wb_camera_get_focal_length)();                            |
| &nbsp;&nbsp; public void [setFocalDistance](#wb_camera_get_focal_length)(double focalDistance);             |
| &nbsp;&nbsp; public int [getWidth](#wb_camera_get_width)();                                                 |
| &nbsp;&nbsp; public int [getHeight](#wb_camera_get_width)();                                                |
| &nbsp;&nbsp; public double [getNear](#wb_camera_get_near)();                                                |
| &nbsp;&nbsp; public double [getMaxRange](#wb_camera_get_range_image)();                                     |
| &nbsp;&nbsp; public int [getType](#wb_camera_get_type)();                                                   |
| &nbsp;&nbsp; public int[] [getImage](#wb_camera_get_image)();                                               |
| &nbsp;&nbsp; public static int [imageGetRed](#wb_camera_get_image)(int[] image, int width, int x, int y);   |
| &nbsp;&nbsp; public static int [imageGetGreen](#wb_camera_get_image)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetBlue](#wb_camera_get_image)(int[] image, int width, int x, int y);  |
| &nbsp;&nbsp; public static int [imageGetGrey](#wb_camera_get_image)(int[] image, int width, int x, int y);  |
| &nbsp;&nbsp; public static int [pixelGetRed](#wb_camera_get_image)(int pixel);                              |
| &nbsp;&nbsp; public static int [pixelGetGreen](#wb_camera_get_image)(int pixel);                            |
| &nbsp;&nbsp; public static int [pixelGetBlue](#wb_camera_get_image)(int pixel);                             |
| &nbsp;&nbsp; public static int [pixelGetGrey](#wb_camera_get_image)(int pixel);                             |
| &nbsp;&nbsp; public float[] [getRangeImage](#wb_camera_get_range_image)();                                  |
| &nbsp;&nbsp; public static float [rangeImageGetDepth](#wb_camera_get_range_image)(float[] image,            |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);                                                          |
| &nbsp;&nbsp; public int [saveImage](#wb_camera_save_image)(String filename, int quality);                   |
| }                                                                                                           |

%end

%api "java_compass"

|                                                                        |
| ---------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Compass;                      |
| public class [Compass](#compass) extends [Device](#java_device) {      |
| &nbsp;&nbsp; public void [enable](#wb_compass_get_values)(int ms);     |
| &nbsp;&nbsp; public void [disable](#wb_compass_get_values)();          |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_compass_get_values)(); |
| &nbsp;&nbsp; public double[] [getValues](#wb_compass_get_values)();    |
| }                                                                      |

%end

%api "java_connector"

|                                                                                |
| ------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Connector;                            |
| public class [Connector](#connector) extends [Device](#java_device) {          |
| &nbsp;&nbsp; public void [enablePresence](#wb_connector_get_presence)(int ms); |
| &nbsp;&nbsp; public void [disablePresence](#wb_connector_get_presence)();      |
| &nbsp;&nbsp; public int [getPresence](#wb_connector_get_presence)();           |
| &nbsp;&nbsp; public void [lock](#wb_connector_lock)();                         |
| &nbsp;&nbsp; public void [unlock](#wb_connector_lock)();                       |
| }                                                                              |

%end

%api "java_device"

|                                                                    |
| ------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Device;                   |
| public class [Device](#device) {                                   |
| &nbsp;&nbsp; public String [getModel](#wb_device_get_model)();     |
| &nbsp;&nbsp; public String [getName](#wb_device_get_name)();       |
| &nbsp;&nbsp; public int [getNodeType](#wb_device_get_node_type)(); |
| }                                                                  |

%end

%api "java_differential_wheels"

|                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.DifferentialWheels;                                                 |
| public class [DifferentialWheels](#differentialwheels) extends [Robot](#java_robot) {                        |
| &nbsp;&nbsp; public [DifferentialWheels](#wb_robot_step)();                                                  |
| &nbsp;&nbsp; protected void [finalize](#wb_robot_step)();                                                    |
| &nbsp;&nbsp; public void [setSpeed](#wb_differential_wheels_set_speed)(double left, double right);           |
| &nbsp;&nbsp; public double [getLeftSpeed](#wb_differential_wheels_set_speed)();                              |
| &nbsp;&nbsp; public double [getRightSpeed](#wb_differential_wheels_set_speed)();                             |
| &nbsp;&nbsp; public void [enableEncoders](#wb_differential_wheels_enable_encoders)(int ms);                  |
| &nbsp;&nbsp; public void [disableEncoders](#wb_differential_wheels_enable_encoders)();                       |
| &nbsp;&nbsp; public int [getEncodersSamplingPeriod](#wb_differential_wheels_enable_encoders)();              |
| &nbsp;&nbsp; public double [getLeftEncoder](#wb_differential_wheels_get_left_encoder)();                     |
| &nbsp;&nbsp; public double [getRightEncoder](#wb_differential_wheels_get_left_encoder)();                    |
| &nbsp;&nbsp; public void [setEncoders](#wb_differential_wheels_get_left_encoder)(double left, double right); |
| &nbsp;&nbsp; public double [getMaxSpeed](#wb_differential_wheels_get_max_speed)();                           |
| &nbsp;&nbsp; public double [getSpeedUnit](#wb_differential_wheels_get_speed_unit)();                         |
| }                                                                                                            |

%end

%api "java_display"

|                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Display;                                                                                       |
| public class [Display](#display) extends [Device](#java_device) {                                                                       |
| &nbsp;&nbsp; public final static int RGB, RGBA, ARGB, BGRA;                                                                             |
| &nbsp;&nbsp; public int [getWidth](#wb_display_get_width)();                                                                            |
| &nbsp;&nbsp; public int [getHeight](#wb_display_get_width)();                                                                           |
| &nbsp;&nbsp; public void [setColor](#wb_display_set_context)(int color);                                                                |
| &nbsp;&nbsp; public void [setAlpha](#wb_display_set_context)(double alpha);                                                             |
| &nbsp;&nbsp; public void [setOpacity](#wb_display_set_context)(double opacity);                                                         |
| &nbsp;&nbsp; public void [drawPixel](#wb_display_draw_primitive)(int x1, int y1);                                                       |
| &nbsp;&nbsp; public void [drawLine](#wb_display_draw_primitive)(int x1, int y1, int x2, int y2);                                        |
| &nbsp;&nbsp; public void [drawRectangle](#wb_display_draw_primitive)(int x, int y, int width, int height);                              |
| &nbsp;&nbsp; public void [drawOval](#wb_display_draw_primitive)(int cx, int cy, int a, int b);                                          |
| &nbsp;&nbsp; public void [drawPolygon](#wb_display_draw_primitive)(int[] x, int[] y);                                                   |
| &nbsp;&nbsp; public void [drawText](#wb_display_draw_primitive)(String txt, int x, int y);                                              |
| &nbsp;&nbsp; public void [fillRectangle](#wb_display_draw_primitive)(int x, int y, int width, int height);                              |
| &nbsp;&nbsp; public void [fillOval](#wb_display_draw_primitive)(int cx, int cy, int a, int b);                                          |
| &nbsp;&nbsp; public void [fillPolygon](#wb_display_draw_primitive)(int[] x, int[] y);                                                   |
| &nbsp;&nbsp; public [ImageRef](#java_image_ref) [imageCopy](#wb_display_image_functions)(int x, int y, int width, int height);          |
| &nbsp;&nbsp; public void [imagePaste](#wb_display_image_functions)([ImageRef](#java_image_ref) ir, int x, int y);                       |
| &nbsp;&nbsp; public [ImageRef](#java_image_ref) [imageLoad](#wb_display_image_functions)(String filename);                              |
| &nbsp;&nbsp; public [ImageRef](#java_image_ref) [imageNew](#wb_display_image_functions)(int width, int height, int[] data, int format); |
| &nbsp;&nbsp; public void [imageSave](#wb_display_image_functions)([ImageRef](#java_image_ref) ir, String filename);                     |
| &nbsp;&nbsp; public void [imageDelete](#wb_display_image_functions)([ImageRef](#java_image_ref) ir);                                    |
| }                                                                                                                                       |

%end

%api "java_distance_sensor"

|                                                                                 |
| ------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.DistanceSensor;                        |
| public class [DistanceSensor](#distancesensor) extends [Device](#java_device) { |
| &nbsp;&nbsp; public void [enable](#wb_distance_sensor_get_value)(int ms);       |
| &nbsp;&nbsp; public void [disable](#wb_distance_sensor_get_value)();            |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_distance_sensor_get_value)();   |
| &nbsp;&nbsp; public double [getValue](#wb_distance_sensor_get_value)();         |
| }                                                                               |

%end

%api "java_emitter"

|                                                                              |
| ---------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Emitter;                            |
| public class [Emitter](#emitter) extends [Device](#java_device) {            |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST;                     |
| &nbsp;&nbsp; public int [send](#wb_emitter_send)(byte[] data);               |
| &nbsp;&nbsp; public int [getChannel](#wb_emitter_set_channel)();             |
| &nbsp;&nbsp; public void [setChannel](#wb_emitter_set_channel)(int channel); |
| &nbsp;&nbsp; public double [getRange](#wb_emitter_set_range)();              |
| &nbsp;&nbsp; public void [setRange](#wb_emitter_set_range)(double range);    |
| &nbsp;&nbsp; public int [getBufferSize](#wb_emitter_get_buffer_size)();      |
| }                                                                            |

%end

%api "java_field"

|                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.Field;                                                                          |
| public class Field {                                                                                                     |
| &nbsp;&nbsp; public final static int SF\_BOOL, SF\_INT32, SF\_FLOAT,                                                     |
| &nbsp;&nbsp; SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING,                                                  |
| &nbsp;&nbsp; SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F,                                                   |
| &nbsp;&nbsp; MF\_COLOR, MF\_STRING, MF\_NODE;                                                                            |
| &nbsp;&nbsp; public int [getType](#wb_supervisor_field_get)();                                                           |
| &nbsp;&nbsp; public String [getTypeName](#wb_supervisor_field_get)();                                                    |
| &nbsp;&nbsp; public int [getCount](#wb_supervisor_field_get)();                                                          |
| &nbsp;&nbsp; public bool [getSFBool](#wb_supervisor_field_get_sf_bool)();                                                |
| &nbsp;&nbsp; public int [getSFInt32](#wb_supervisor_field_get_sf_bool)();                                                |
| &nbsp;&nbsp; public double [getSFFloat](#wb_supervisor_field_get_sf_bool)();                                             |
| &nbsp;&nbsp; public double[] [getSFVec2f](#wb_supervisor_field_get_sf_bool)();                                           |
| &nbsp;&nbsp; public double[] [getSFVec3f](#wb_supervisor_field_get_sf_bool)();                                           |
| &nbsp;&nbsp; public double[] [getSFRotation](#wb_supervisor_field_get_sf_bool)();                                        |
| &nbsp;&nbsp; public double[] [getSFColor](#wb_supervisor_field_get_sf_bool)();                                           |
| &nbsp;&nbsp; public String [getSFString](#wb_supervisor_field_get_sf_bool)();                                            |
| &nbsp;&nbsp; public [Node](#java_node) [getSFNode](#wb_supervisor_field_get_sf_bool)();                                  |
| &nbsp;&nbsp; public bool [getMFBool](#wb_supervisor_field_get_sf_bool)(int index);                                       |
| &nbsp;&nbsp; public int [getMFInt32](#wb_supervisor_field_get_sf_bool)(int index);                                       |
| &nbsp;&nbsp; public double [getMFFloat](#wb_supervisor_field_get_sf_bool)(int index);                                    |
| &nbsp;&nbsp; public double[] [getMFVec2f](#wb_supervisor_field_get_sf_bool)(int index);                                  |
| &nbsp;&nbsp; public double[] [getMFVec3f](#wb_supervisor_field_get_sf_bool)(int index);                                  |
| &nbsp;&nbsp; public double[] [getMFColor](#wb_supervisor_field_get_sf_bool)(int index);                                  |
| &nbsp;&nbsp; public double[] [getMFRotation](#wb_supervisor_field_get_sf_bool)(int index);                               |
| &nbsp;&nbsp; public String [getMFString](#wb_supervisor_field_get_sf_bool)(int index);                                   |
| &nbsp;&nbsp; public [Node](#java_node) [getMFNode](#wb_supervisor_field_get_sf_bool)(int index);                         |
| &nbsp;&nbsp; public void [setSFBool](#wb_supervisor_field_set_sf_bool)(bool value);                                      |
| &nbsp;&nbsp; public void [setSFInt32](#wb_supervisor_field_set_sf_bool)(int value);                                      |
| &nbsp;&nbsp; public void [setSFFloat](#wb_supervisor_field_set_sf_bool)(double value);                                   |
| &nbsp;&nbsp; public void [setSFVec2f](#wb_supervisor_field_set_sf_bool)(double values[2]);                               |
| &nbsp;&nbsp; public void [setSFVec3f](#wb_supervisor_field_set_sf_bool)(double values[3]);                               |
| &nbsp;&nbsp; public void [setSFRotation](#wb_supervisor_field_set_sf_bool)(double values[4]);                            |
| &nbsp;&nbsp; public void [setSFColor](#wb_supervisor_field_set_sf_bool)(double values[3]);                               |
| &nbsp;&nbsp; public void [setSFString](#wb_supervisor_field_set_sf_bool)(String value);                                  |
| &nbsp;&nbsp; public void [setMFBool](#wb_supervisor_field_set_sf_bool)(int index, bool value);                           |
| &nbsp;&nbsp; public void [setMFInt32](#wb_supervisor_field_set_sf_bool)(int index, int value);                           |
| &nbsp;&nbsp; public void [setMFFloat](#wb_supervisor_field_set_sf_bool)(int index, double value);                        |
| &nbsp;&nbsp; public void [setMFVec2f](#wb_supervisor_field_set_sf_bool)(int index, double values[2]);                    |
| &nbsp;&nbsp; public void [setMFVec3f](#wb_supervisor_field_set_sf_bool)(int index, double values[3]);                    |
| &nbsp;&nbsp; public void [setMFRotation](#wb_supervisor_field_set_sf_bool)(int index, double values[4]);                 |
| &nbsp;&nbsp; public void [setMFColor](#wb_supervisor_field_set_sf_bool)(int index, double values[3]);                    |
| &nbsp;&nbsp; public void [setMFString](#wb_supervisor_field_set_sf_bool)(int index, String value);                       |
| &nbsp;&nbsp; public void [importMFNode](#wb_supervisor_field_import_mf_node)(int position, String filename);             |
| &nbsp;&nbsp; public void [importMFNodeFromString](#wb_supervisor_field_import_mf_node)(int position, String nodeString); |
| &nbsp;&nbsp; public void [removeMFNode](#wb_supervisor_field_import_mf_node)(int position);                              |
| }                                                                                                                        |

%end

%api "java_gps"

|                                                                    |
| ------------------------------------------------------------------ |
| import com.cyberbotics.webots.controller.GPS;                      |
| public class [GPS](#gps) extends [Device](#java_device) {          |
| &nbsp;&nbsp; public void [enable](#wb_gps_get_values)(int ms);     |
| &nbsp;&nbsp; public void [disable](#wb_gps_get_values)();          |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_gps_get_values)(); |
| &nbsp;&nbsp; public double[] [getValues](#wb_gps_get_values)();    |
| }                                                                  |

%end

%api "java_gyro"

|                                                                     |
| ------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Gyro;                      |
| public class [Gyro](#gyro) extends [Device](#java_device) {         |
| &nbsp;&nbsp; public void [enable](#wb_gyro_get_values)(int ms);     |
| &nbsp;&nbsp; public void [disable](#wb_gyro_get_values)();          |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_gyro_get_values)(); |
| &nbsp;&nbsp; public double[] [getValues](#wb_gyro_get_values)();    |
| }                                                                   |

%end

%api "java_image_ref"

|                                                    |
| -------------------------------------------------- |
| import com.cyberbotics.webots.controller.ImageRef; |
| public class ImageRef {                            |
| }                                                  |

%end

%api "java_inertial_unit"

|                                                                                         |
| --------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.InertialUnit;                                  |
| public class [InertialUnit](#inertialunit) extends [Device](#java_device) {             |
| &nbsp;&nbsp; public void [enable](#wb_inertial_unit_get_roll_pitch_yaw)(int ms);        |
| &nbsp;&nbsp; public void [disable](#wb_inertial_unit_get_roll_pitch_yaw)();             |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_inertial_unit_get_roll_pitch_yaw)();    |
| &nbsp;&nbsp; public double[] [getRollPitchYaw](#wb_inertial_unit_get_roll_pitch_yaw)(); |
| }                                                                                       |

%end

%api "java_led"

|                                                           |
| --------------------------------------------------------- |
| import com.cyberbotics.webots.controller.LED;             |
| public class [LED](#led) extends [Device](#java_device) { |
| &nbsp;&nbsp; public void [set](#wb_led_set)(int state);   |
| &nbsp;&nbsp; public int [get](#wb_led_set)();             |
| }                                                         |

%end

%api "java_light_sensor"

|                                                                            |
| -------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.LightSensor;                      |
| public class [LightSensor](#lightsensor) extends [Device](#java_device) {  |
| &nbsp;&nbsp; public void [enable](#wb_light_sensor_get_value)(int ms);     |
| &nbsp;&nbsp; public void [disable](#wb_light_sensor_get_value)();          |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_light_sensor_get_value)(); |
| &nbsp;&nbsp; public double [getValue](#wb_light_sensor_get_value)();       |
| }                                                                          |

%end

%api "java_motion"

|                                                                        |
| ---------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Motion;                       |
| public class [Motion](#motion) {                                       |
| &nbsp;&nbsp; public [Motion](#wbu_motion_new)(String fileName);        |
| &nbsp;&nbsp; protected void [finalize](#wbu_motion_new)();             |
| &nbsp;&nbsp; public bool [isValid](#wbu_motion_new)();                 |
| &nbsp;&nbsp; public void [play](#wbu_motion_play)();                   |
| &nbsp;&nbsp; public void [stop](#wbu_motion_play)();                   |
| &nbsp;&nbsp; public void [setLoop](#wbu_motion_play)(bool loop);       |
| &nbsp;&nbsp; public void [setReverse](#wbu_motion_play)(bool reverse); |
| &nbsp;&nbsp; public bool [isOver](#wbu_motion_is_over)();              |
| &nbsp;&nbsp; public int [getDuration](#wbu_motion_is_over)();          |
| &nbsp;&nbsp; public int [getTime](#wbu_motion_is_over)();              |
| &nbsp;&nbsp; public void [setTime](#wbu_motion_is_over)(int time);     |
| }                                                                      |

%end

%api "java_motor"

|                                                                                                 |
| ----------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Motor;                                                 |
| public class [Motor](#motor) extends [Device](#java_device) {                                   |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR;                                        |
| &nbsp;&nbsp; public void [setPosition](#wb_motor_set_position)(double position);                |
| &nbsp;&nbsp; public void [setVelocity](#wb_motor_set_position)(double vel);                     |
| &nbsp;&nbsp; public void [setAcceleration](#wb_motor_set_position)(double force);               |
| &nbsp;&nbsp; public void [setAvailableForce](#wb_motor_set_position)(double motor\_force);      |
| &nbsp;&nbsp; public void [setAvailableTorque](#wb_motor_set_position)(double motor\_torque);    |
| &nbsp;&nbsp; public void [setControlPID](#wb_motor_set_position)(double p, double i, double d); |
| &nbsp;&nbsp; public double [getTargetPosition](#wb_motor_set_position)();                       |
| &nbsp;&nbsp; public double [getMinPosition](#wb_motor_set_position)();                          |
| &nbsp;&nbsp; public double [getMaxPosition](#wb_motor_set_position)();                          |
| &nbsp;&nbsp; public double [getVelocity](#wb_motor_set_position)();                             |
| &nbsp;&nbsp; public double [getMaxVelocity](#wb_motor_set_position)();                          |
| &nbsp;&nbsp; public double [getAcceleration](#wb_motor_set_position)();                         |
| &nbsp;&nbsp; public double [getAvailableForce](#wb_motor_set_position)();                       |
| &nbsp;&nbsp; public double [getMaxForce](#wb_motor_set_position)();                             |
| &nbsp;&nbsp; public double [getAvailableTorque](#wb_motor_set_position)();                      |
| &nbsp;&nbsp; public double [getMaxTorque](#wb_motor_set_position)();                            |
| &nbsp;&nbsp; public void [enableForceFeedback](#wb_motor_enable_force_feedback)(int ms);        |
| &nbsp;&nbsp; public void [disableForceFeedback](#wb_motor_enable_force_feedback)();             |
| &nbsp;&nbsp; public int [getForceFeedbackSamplingPeriod](#wb_motor_enable_force_feedback)();    |
| &nbsp;&nbsp; public double [getForceFeedback](#wb_motor_enable_force_feedback)();               |
| &nbsp;&nbsp; public void [setForce](#wb_motor_set_force)(double force);                         |
| &nbsp;&nbsp; public void [enableTorqueFeedback](#wb_motor_enable_force_feedback)(int ms);       |
| &nbsp;&nbsp; public void [disableTorqueFeedback](#wb_motor_enable_force_feedback)();            |
| &nbsp;&nbsp; public int [getTorqueFeedbackSamplingPeriod](#wb_motor_enable_force_feedback)();   |
| &nbsp;&nbsp; public double [getTorqueFeedback](#wb_motor_enable_force_feedback)();              |
| &nbsp;&nbsp; public void [setTorque](#wb_motor_set_force)(double torque);                       |
| &nbsp;&nbsp; public int [getType](#wb_motor_get_type)();                                        |
| }                                                                                               |

%end

%api "java_node"

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Node;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| public class Node {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| &nbsp;&nbsp; public final static int NO\_NODE, ACCELEROMETER, APPEARANCE, BACKGROUND, BALL\_JOINT, BALL\_JOINT\_PARAMETERS, BOX, BRAKE, CAMERA, CAMERA\_FOCUS, CAMERA\_LENS\_DISTORTION, CAMERA\_ZOOM, CAPSULE, CHARGER, COLOR, COMPASS, CONE, CONNECTOR, CONTACT\_PROPERTIES, COORDINATE, CYLINDER, DAMPING, DIFFERENTIAL\_WHEELS, DIRECTIONAL\_LIGHT, DISPLAY, DISTANCE\_SENSOR, ELEVATION\_GRID, EMITTER, EXTRUSION, FLUID, FOG, GPS, GROUP, GYRO, HINGE\_2\_JOINT, HINGE\_2\_JOINT\_PARAMETERS, HINGE\_JOINT, HINGE\_JOINT\_PARAMETERS, IMAGE\_TEXTURE, IMMERSION\_PROPERTIES, INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, INERTIAL\_UNIT, JOINT\_PARAMETERS, LED, LIGHT\_SENSOR, LINEAR\_MOTOR, MATERIAL, MICROPHONE, PEN, PHYSICS, PLANE, POINT\_LIGHT, POSITION\_SENSOR, PROPELLER, RADIO, RECEIVER, ROBOT, ROTATIONAL\_MOTOR, SERVO, SHAPE, SLIDER\_JOINT, SLOT, SOLID, SOLID\_REFERENCE, SPEAKER, SPHERE, SPOT\_LIGHT, SUPERVISOR, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, TOUCH\_SENSOR, TRACK, TRACK\_WHEEL, TRANSFORM, VIEWPOINT, WORLD\_INFO; |
| &nbsp;&nbsp; public void [remove](#wb_supervisor_node_remove)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| &nbsp;&nbsp; public int [getId](#wb_supervisor_node_get_from_def)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| &nbsp;&nbsp; public int [getType](#wb_supervisor_node_get_type)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| &nbsp;&nbsp; public String [getTypeName](#wb_supervisor_node_get_type)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp; public String [getBaseTypeName](#wb_supervisor_node_get_type)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; public [Field](#java_field) [getField](#wb_supervisor_node_get_field)(String fieldName);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| &nbsp;&nbsp; public Node [getParentNode](#wb_supervisor_node_get_from_def)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; public double[] [getPosition](#wb_supervisor_node_get_position)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; public double[] [getOrientation](#wb_supervisor_node_get_position)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| &nbsp;&nbsp; public double[] [getCenterOfMass](#wb_supervisor_node_get_center_of_mass)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp; public double[] [getContactPoint](#wb_supervisor_node_get_contact_point)(int index);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &nbsp;&nbsp; public int [getNumberOfContactPoints](#wb_supervisor_node_get_number_of_contact_points)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| &nbsp;&nbsp; public bool [getStaticBalance](#wb_supervisor_node_get_static_balance)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| &nbsp;&nbsp; public double[] [getVelocity](#wb_supervisor_node_get_velocity)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| &nbsp;&nbsp; public void [setVelocity](#wb_supervisor_node_get_velocity)(double velocity[6]);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| &nbsp;&nbsp; public void [resetPhysics](#wb_supervisor_node_reset_physics)();                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

%end

%api "java_pen"

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Pen;                                             |
| public class [Pen](#pen) extends [Device](#java_device) {                                 |
| &nbsp;&nbsp; public void [write](#wb_pen_write)(bool write);                              |
| &nbsp;&nbsp; public void [setInkColor](#wb_pen_set_ink_color)(int color, double density); |
| }                                                                                         |

%end

%api "java_position_sensor"

|                                                                                 |
| ------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.PositionSensor;                        |
| public class [PositionSensor](#positionsensor) extends [Device](#java_device) { |
| &nbsp;&nbsp; public final static int ANGULAR, LINEAR;                           |
| &nbsp;&nbsp; public void [enable](#wb_position_sensor_get_value)(int ms);       |
| &nbsp;&nbsp; public void [disable](#wb_position_sensor_get_value)();            |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_position_sensor_get_value)();   |
| &nbsp;&nbsp; public double [getValue](#wb_position_sensor_get_value)();         |
| &nbsp;&nbsp; public int [getType](#wb_position_sensor_get_value)();             |
| }                                                                               |

%end

%api "java_receiver"

|                                                                                         |
| --------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Receiver;                                      |
| public class [Receiver](#receiver) extends [Device](#java_device) {                     |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST;                                |
| &nbsp;&nbsp; public void [enable](#wb_receiver_enable)(int ms);                         |
| &nbsp;&nbsp; public void [disable](#wb_receiver_enable)();                              |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_receiver_enable)();                     |
| &nbsp;&nbsp; public int [getQueueLength](#wb_receiver_get_queue_length)();              |
| &nbsp;&nbsp; public void [nextPacket](#wb_receiver_get_queue_length)();                 |
| &nbsp;&nbsp; public byte[] [getData](#wb_receiver_get_data)();                          |
| &nbsp;&nbsp; public int [getDataSize](#wb_receiver_get_data)();                         |
| &nbsp;&nbsp; public double [getSignalStrength](#wb_receiver_get_signal_strength)();     |
| &nbsp;&nbsp; public double[] [getEmitterDirection](#wb_receiver_get_signal_strength)(); |
| &nbsp;&nbsp; public void [setChannel](#wb_receiver_set_channel)(int channel);           |
| &nbsp;&nbsp; public int [getChannel](#wb_receiver_set_channel)();                       |
| }                                                                                       |

%end

%api "java_robot"

|                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Robot;                                                                |
| public class [Robot](#robot) {                                                                                 |
| &nbsp;&nbsp; public final static int MODE\_SIMULATION,                                                         |
| &nbsp;&nbsp; MODE\_CROSS\_COMPILATION, MODE\_REMOTE\_CONTROL;                                                  |
| &nbsp;&nbsp; public final static int KEYBOARD\_END, KEYBOARD\_HOME,                                            |
| &nbsp;&nbsp; KEYBOARD\_LEFT, KEYBOARD\_UP, KEYBOARD\_RIGHT,                                                    |
| &nbsp;&nbsp; KEYBOARD\_DOWN, KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN,                                             |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT,                                                   |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT,                                                    |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END,                                                    |
| &nbsp;&nbsp; KEYBOARD\_KEY, KEYBOARD\_SHIFT,                                                                   |
| &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT;                                                                 |
| &nbsp;&nbsp; public [Robot](#wb_robot_step)();                                                                 |
| &nbsp;&nbsp; protected void [finalize](#wb_robot_step)();                                                      |
| &nbsp;&nbsp; public int [step](#wb_robot_step)(int ms);                                                        |
| &nbsp;&nbsp; public [Accelerometer](#java_accelerometer) [getAccelerometer](#robotgetdevice)(String name);     |
| &nbsp;&nbsp; public [Brake](#java_brake) [getBrake](#robotgetdevice)(String name);                             |
| &nbsp;&nbsp; public [Camera](#java_camera) [getCamera](#robotgetdevice)(String name);                          |
| &nbsp;&nbsp; public [Compass](#java_compass) [getCompass](#robotgetdevice)(String name);                       |
| &nbsp;&nbsp; public [Connector](#java_connector) [getConnector](#robotgetdevice)(String name);                 |
| &nbsp;&nbsp; public [Display](#java_display) [getDisplay](#robotgetdevice)(String name);                       |
| &nbsp;&nbsp; public [DistanceSensor](#java_distance_sensor) [getDistanceSensor](#robotgetdevice)(String name); |
| &nbsp;&nbsp; public [Emitter](#java_emitter) [getEmitter](#robotgetdevice)(String name);                       |
| &nbsp;&nbsp; public [GPS](#java_gps) [getGPS](#robotgetdevice)(String name);                                   |
| &nbsp;&nbsp; public [Gyro](#java_gyro) [getGyro](#robotgetdevice)(String name);                                |
| &nbsp;&nbsp; public [InertialUnit](#java_inertial_unit) [getInertialUnit](#robotgetdevice)(String name);       |
| &nbsp;&nbsp; public [LED](#java_led) [getLED](#robotgetdevice)(String name);                                   |
| &nbsp;&nbsp; public [LightSensor](#java_light_sensor) [getLightSensor](#robotgetdevice)(String name);          |
| &nbsp;&nbsp; public [Motor](#java_motor) [getMotor](#robotgetdevice)(String name);                             |
| &nbsp;&nbsp; public [Pen](#java_pen) [getPen](#robotgetdevice)(String name);                                   |
| &nbsp;&nbsp; public [PositionSensor](#java_position_sensor) [getPositionSensor](#robotgetdevice)(String name); |
| &nbsp;&nbsp; public [Receiver](#java_receiver) [getReceiver](#robotgetdevice)(String name);                    |
| &nbsp;&nbsp; public [Servo](#java_servo) [getServo](#robotgetdevice)(String name);                             |
| &nbsp;&nbsp; public [TouchSensor](#java_touch_sensor) [getTouchSensor](#robotgetdevice)(String name);          |
| &nbsp;&nbsp; public int [getNumberOfDevices](#wb_robot_get_device_by_index)();                                 |
| &nbsp;&nbsp; public [Device](#java_device) [getDeviceByIndex](#wb_robot_get_device_by_index)(int index);       |
| &nbsp;&nbsp; public void [batterySensorEnable](#wb_robot_battery_sensor_enable)(int ms);                       |
| &nbsp;&nbsp; public void [batterySensorDisable](#wb_robot_battery_sensor_enable)();                            |
| &nbsp;&nbsp; public int [batterySensorGetSamplingPeriod](#wb_robot_battery_sensor_enable)();                   |
| &nbsp;&nbsp; public double [batterySensorGetValue](#wb_robot_battery_sensor_enable)();                         |
| &nbsp;&nbsp; public double [getBasicTimeStep](#wb_robot_get_basic_time_step)();                                |
| &nbsp;&nbsp; public int [getMode](#wb_robot_get_mode)();                                                       |
| &nbsp;&nbsp; public String [getModel](#wb_robot_get_model)();                                                  |
| &nbsp;&nbsp; public String [getData](#wb_robot_get_data)();                                                    |
| &nbsp;&nbsp; public [setData](#wb_robot_get_data)(String data);                                                |
| &nbsp;&nbsp; public String [getName](#wb_robot_get_name)();                                                    |
| &nbsp;&nbsp; public String [getControllerName](#wb_robot_get_controller_name)();                               |
| &nbsp;&nbsp; public String [getControllerArguments](#wb_robot_get_controller_name)();                          |
| &nbsp;&nbsp; public String [getProjectPath](#wb_robot_get_project_path)();                                     |
| &nbsp;&nbsp; public bool [getSynchronization](#wb_robot_get_synchronization)();                                |
| &nbsp;&nbsp; public double [getTime](#wb_robot_get_time)();                                                    |
| &nbsp;&nbsp; public String [getWorldPath](#wb_robot_get_world_path)();                                         |
| &nbsp;&nbsp; public void [keyboardEnable](#wb_robot_keyboard_enable)(int ms);                                  |
| &nbsp;&nbsp; public void [keyboardDisable](#wb_robot_keyboard_enable)();                                       |
| &nbsp;&nbsp; public int [keyboardGetKey](#wb_robot_keyboard_enable)();                                         |
| &nbsp;&nbsp; public int [getType](#wb_robot_get_type)();                                                       |
| }                                                                                                              |

%end

%api "java_servo"

|                                                                                                         |
| ------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Servo;                                                         |
| public class [Servo](#servo) extends [Device](#java_device) {                                           |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR;                                                |
| &nbsp;&nbsp; public void [setPosition](#wb_servo_set_position)(double position);                        |
| &nbsp;&nbsp; public double [getTargetPosition](#wb_servo_set_position)();                               |
| &nbsp;&nbsp; public void [setVelocity](#wb_servo_set_position)(double vel);                             |
| &nbsp;&nbsp; public void [setAcceleration](#wb_servo_set_position)(double force);                       |
| &nbsp;&nbsp; public void [setMotorForce](#wb_servo_set_position)(double motor\_force);                  |
| &nbsp;&nbsp; public void [setControlP](#wb_servo_set_position)(double p);                               |
| &nbsp;&nbsp; public double [getMinPosition](#wb_servo_set_position)();                                  |
| &nbsp;&nbsp; public double [getMaxPosition](#wb_servo_set_position)();                                  |
| &nbsp;&nbsp; public void [enablePosition](#wb_servo_enable_position)(int ms);                           |
| &nbsp;&nbsp; public void [disablePosition](#wb_servo_enable_position)();                                |
| &nbsp;&nbsp; public int [getPositionSamplingPeriod](#wb_servo_enable_position)();                       |
| &nbsp;&nbsp; public double [getPosition](#wb_servo_enable_position)();                                  |
| &nbsp;&nbsp; public void [enableMotorForceFeedback](#wb_servo_enable_motor_force_feedback)(int ms);     |
| &nbsp;&nbsp; public void [disableMotorForceFeedback](#wb_servo_enable_motor_force_feedback)();          |
| &nbsp;&nbsp; public int [getMotorForceFeedbackSamplingPeriod](#wb_servo_enable_motor_force_feedback)(); |
| &nbsp;&nbsp; public double [getMotorForceFeedback](#wb_servo_enable_motor_force_feedback)();            |
| &nbsp;&nbsp; public void [setForce](#wb_servo_set_force)(double force);                                 |
| &nbsp;&nbsp; public int [getType](#wb_servo_get_type)();                                                |
| }                                                                                                       |

%end

%api "java_supervisor"

|                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Supervisor;                                                                                                      |
| public class [Supervisor](#supervisor) extends [Robot](#java_robot) {                                                                                     |
| &nbsp;&nbsp; public final static int MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR |
| &nbsp;&nbsp; public [Supervisor](#wb_robot_step)();                                                                                                       |
| &nbsp;&nbsp; protected void [finalize](#wb_robot_step)();                                                                                                 |
| &nbsp;&nbsp; public void [exportImage](#wb_supervisor_export_image)(String file, int quality);                                                            |
| &nbsp;&nbsp; public [Node](#java_node) [getRoot](#wb_supervisor_node_get_from_def)();                                                                     |
| &nbsp;&nbsp; public [Node](#java_node) [getSelf](#wb_supervisor_node_get_from_def)();                                                                     |
| &nbsp;&nbsp; public [Node](#java_node) [getFromDef](#wb_supervisor_node_get_from_def)(String name);                                                       |
| &nbsp;&nbsp; public [Node](#java_node) [getFromId](#wb_supervisor_node_get_from_def)(int id);                                                             |
| &nbsp;&nbsp; public void [setLabel](#wb_supervisor_set_label)(int id, String label, double xpos, double ypos,                                             |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency);                                                                                    |
| &nbsp;&nbsp; public void [simulationQuit](#wb_supervisor_simulation_quit)(int status);                                                                    |
| &nbsp;&nbsp; public void [simulationRevert](#wb_supervisor_simulation_revert)();                                                                          |
| &nbsp;&nbsp; public void [simulationResetPhysics](#wb_supervisor_simulation_reset_physics)();                                                             |
| &nbsp;&nbsp; public void [loadWorld](#wb_supervisor_load_world)(String file);                                                                             |
| &nbsp;&nbsp; public void [saveWorld](#wb_supervisor_load_world)();                                                                                        |
| &nbsp;&nbsp; public void [saveWorld](#wb_supervisor_load_world)(String file);                                                                             |
| &nbsp;&nbsp; public void [movieStartRecording](#wb_supervisor_movie_start_recording)(String file, int width, int height, int codec, int quality,          |
| &nbsp;&nbsp;&nbsp;&nbsp; int acceleration, boolean caption);                                                                                              |
| &nbsp;&nbsp; public void [movieStopRecording](#wb_supervisor_movie_start_recording)();                                                                    |
| &nbsp;&nbsp; public int [movieGetStatus](#wb_supervisor_movie_start_recording)();                                                                         |
| &nbsp;&nbsp; public bool [animationStartRecording](#wb_supervisor_animation_start_recording)(String file);                                                |
| &nbsp;&nbsp; public bool [animationStopRecording](#wb_supervisor_animation_start_recording)();                                                            |
| }                                                                                                                                                         |

%end

%api "java_touch_sensor"

|                                                                             |
| --------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.TouchSensor;                       |
| public class [TouchSensor](#touchsensor) extends [Device](#java_device) {   |
| &nbsp;&nbsp; public final static int BUMPER, FORCE, FORCE3D;                |
| &nbsp;&nbsp; public void [enable](#wb_touch_sensor_get_values)(int ms);     |
| &nbsp;&nbsp; public void [disable](#wb_touch_sensor_get_values)();          |
| &nbsp;&nbsp; public int [getSamplingPeriod](#wb_touch_sensor_get_values)(); |
| &nbsp;&nbsp; public double [getValue](#wb_touch_sensor_get_values)();       |
| &nbsp;&nbsp; public double[] [getValues](#wb_touch_sensor_get_values)();    |
| &nbsp;&nbsp; public int [getType](#wb_touch_sensor_get_type)();             |
| }                                                                           |

%end

