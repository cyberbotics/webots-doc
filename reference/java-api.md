## Java API

The following tables describe the Java classes and their methods.

| |
| --- |
| import com.cyberbotics.webots.controller.Accelerometer; |
| public class [Accelerometer](reference/accelerometer.md#accelerometer) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enable](reference/accelerometer.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/accelerometer.md)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/accelerometer.md)(); |
| &nbsp;&nbsp; public double[] [getValues](reference/accelerometer.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Brake; |
| public class [Brake](reference/brake.md#brake) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [setDampingConstant](reference/brake.md)(double dampingConstant); |
| &nbsp;&nbsp; public int [getType](reference/brake.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Camera; |
| public class [Camera](reference/camera.md#camera) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int COLOR, RANGE\_FINDER, BOTH; |
| &nbsp;&nbsp; public void [enable](reference/camera.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/camera.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getFov](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getMinFov](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getMaxFov](reference/camera.md)(); |
| &nbsp;&nbsp; public void [setFov](reference/camera.md)(double fov); |
| &nbsp;&nbsp; public double [getFocalLength](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getFocalDistance](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getMaxFocalDistance](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getMinFocalDistance](reference/camera.md)(); |
| &nbsp;&nbsp; public void [setFocalDistance](reference/camera.md)(double focalDistance); |
| &nbsp;&nbsp; public int [getWidth](reference/camera.md)(); |
| &nbsp;&nbsp; public int [getHeight](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getNear](reference/camera.md)(); |
| &nbsp;&nbsp; public double [getMaxRange](reference/camera.md)(); |
| &nbsp;&nbsp; public int [getType](reference/camera.md)(); |
| &nbsp;&nbsp; public int[] [getImage](reference/camera.md)(); |
| &nbsp;&nbsp; public static int [imageGetRed](reference/camera.md)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetGreen](reference/camera.md)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetBlue](reference/camera.md)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetGrey](reference/camera.md)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [pixelGetRed](reference/camera.md)(int pixel); |
| &nbsp;&nbsp; public static int [pixelGetGreen](reference/camera.md)(int pixel); |
| &nbsp;&nbsp; public static int [pixelGetBlue](reference/camera.md)(int pixel); |
| &nbsp;&nbsp; public static int [pixelGetGrey](reference/camera.md)(int pixel); |
| &nbsp;&nbsp; public float[] [getRangeImage](reference/camera.md)(); |
| &nbsp;&nbsp; public static float [rangeImageGetDepth](reference/camera.md)(float[] image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; public int [saveImage](reference/camera.md)(String filename, int quality); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Compass; |
| public class [Compass](reference/compass.md#compass) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enable](reference/compass.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/compass.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/compass.md)(); |
| &nbsp;&nbsp; public double[] [getValues](reference/compass.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Connector; |
| public class [Connector](reference/connector.md#connector) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enablePresence](reference/connector.md)(int ms); |
| &nbsp;&nbsp; public void [disablePresence](reference/connector.md)(); |
| &nbsp;&nbsp; public int [getPresence](reference/connector.md)(); |
| &nbsp;&nbsp; public void [lock](reference/connector.md)(); |
| &nbsp;&nbsp; public void [unlock](reference/connector.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Device; |
| public class [Device](reference/device.md#device) { |
| &nbsp;&nbsp; public String [getModel](reference/device.md)(); |
| &nbsp;&nbsp; public String [getName](reference/device.md)(); |
| &nbsp;&nbsp; public int [getNodeType](reference/device.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.DifferentialWheels; |
| public class [DifferentialWheels](reference/differentialwheels.md#differentialwheels) extends [Robot](reference/java-api.md) { |
| &nbsp;&nbsp; public [DifferentialWheels](reference/robot.md)(); |
| &nbsp;&nbsp; protected void [finalize](reference/robot.md)(); |
| &nbsp;&nbsp; public void [setSpeed](reference/differentialwheels.md)(double left, double right); |
| &nbsp;&nbsp; public double [getLeftSpeed](reference/differentialwheels.md)(); |
| &nbsp;&nbsp; public double [getRightSpeed](reference/differentialwheels.md)(); |
| &nbsp;&nbsp; public void [enableEncoders](reference/differentialwheels.md)(int ms); |
| &nbsp;&nbsp; public void [disableEncoders](reference/differentialwheels.md)(); |
| &nbsp;&nbsp; public int [getEncodersSamplingPeriod](reference/differentialwheels.md)(); |
| &nbsp;&nbsp; public double [getLeftEncoder](reference/differentialwheels.md)(); |
| &nbsp;&nbsp; public double [getRightEncoder](reference/differentialwheels.md)(); |
| &nbsp;&nbsp; public void [setEncoders](reference/differentialwheels.md)(double left, double right); |
| &nbsp;&nbsp; public double [getMaxSpeed](reference/differentialwheels.md)(); |
| &nbsp;&nbsp; public double [getSpeedUnit](reference/differentialwheels.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Display; |
| public class [Display](reference/display.md#display) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int RGB, RGBA, ARGB, BGRA; |
| &nbsp;&nbsp; public int [getWidth](reference/display.md)(); |
| &nbsp;&nbsp; public int [getHeight](reference/display.md)(); |
| &nbsp;&nbsp; public void [setColor](reference/display.md)(int color); |
| &nbsp;&nbsp; public void [setAlpha](reference/display.md)(double alpha); |
| &nbsp;&nbsp; public void [setOpacity](reference/display.md)(double opacity); |
| &nbsp;&nbsp; public void [drawPixel](reference/display.md)(int x1, int y1); |
| &nbsp;&nbsp; public void [drawLine](reference/display.md)(int x1, int y1, int x2, int y2); |
| &nbsp;&nbsp; public void [drawRectangle](reference/display.md)(int x, int y, int width, int height); |
| &nbsp;&nbsp; public void [drawOval](reference/display.md)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; public void [drawPolygon](reference/display.md)(int[] x, int[] y); |
| &nbsp;&nbsp; public void [drawText](reference/display.md)(String txt, int x, int y); |
| &nbsp;&nbsp; public void [fillRectangle](reference/display.md)(int x, int y, int width, int height); |
| &nbsp;&nbsp; public void [fillOval](reference/display.md)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; public void [fillPolygon](reference/display.md)(int[] x, int[] y); |
| &nbsp;&nbsp; public [ImageRef](reference/java-api.md) [imageCopy](reference/display.md)(int x, int y, int width, int height); |
| &nbsp;&nbsp; public void [imagePaste](reference/display.md)([ImageRef](reference/java-api.md) ir, int x, int y); |
| &nbsp;&nbsp; public [ImageRef](reference/java-api.md) [imageLoad](reference/display.md)(String filename); |
| &nbsp;&nbsp; public [ImageRef](reference/java-api.md) [imageNew](reference/display.md)(int width, int height, int[] data, int format); |
| &nbsp;&nbsp; public void [imageSave](reference/display.md)([ImageRef](reference/java-api.md) ir, String filename); |
| &nbsp;&nbsp; public void [imageDelete](reference/display.md)([ImageRef](reference/java-api.md) ir); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.DistanceSensor; |
| public class [DistanceSensor](reference/distancesensor.md#distancesensor) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enable](reference/distancesensor.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/distancesensor.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/distancesensor.md)(); |
| &nbsp;&nbsp; public double [getValue](reference/distancesensor.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Emitter; |
| public class [Emitter](reference/emitter.md#emitter) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST; |
| &nbsp;&nbsp; public int [send](reference/emitter.md)(byte[] data); |
| &nbsp;&nbsp; public int [getChannel](reference/emitter.md)(); |
| &nbsp;&nbsp; public void [setChannel](reference/emitter.md)(int channel); |
| &nbsp;&nbsp; public double [getRange](reference/emitter.md)(); |
| &nbsp;&nbsp; public void [setRange](reference/emitter.md)(double range); |
| &nbsp;&nbsp; public int [getBufferSize](reference/emitter.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Field; |
| public class Field { |
| &nbsp;&nbsp; public final static int SF\_BOOL, SF\_INT32, SF\_FLOAT, |
| &nbsp;&nbsp; SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, |
| &nbsp;&nbsp; SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, |
| &nbsp;&nbsp; MF\_COLOR, MF\_STRING, MF\_NODE; |
| &nbsp;&nbsp; public int [getType](reference/supervisor.md)(); |
| &nbsp;&nbsp; public String [getTypeName](reference/supervisor.md)(); |
| &nbsp;&nbsp; public int [getCount](reference/supervisor.md)(); |
| &nbsp;&nbsp; public bool [getSFBool](reference/supervisor.md)(); |
| &nbsp;&nbsp; public int [getSFInt32](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double [getSFFloat](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getSFVec2f](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getSFVec3f](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getSFRotation](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getSFColor](reference/supervisor.md)(); |
| &nbsp;&nbsp; public String [getSFString](reference/supervisor.md)(); |
| &nbsp;&nbsp; public [Node](reference/java-api.md) [getSFNode](reference/supervisor.md)(); |
| &nbsp;&nbsp; public bool [getMFBool](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public int [getMFInt32](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public double [getMFFloat](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public double[] [getMFVec2f](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public double[] [getMFVec3f](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public double[] [getMFColor](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public double[] [getMFRotation](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public String [getMFString](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public [Node](reference/java-api.md) [getMFNode](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public void [setSFBool](reference/supervisor.md)(bool value); |
| &nbsp;&nbsp; public void [setSFInt32](reference/supervisor.md)(int value); |
| &nbsp;&nbsp; public void [setSFFloat](reference/supervisor.md)(double value); |
| &nbsp;&nbsp; public void [setSFVec2f](reference/supervisor.md)(double values[2]); |
| &nbsp;&nbsp; public void [setSFVec3f](reference/supervisor.md)(double values[3]); |
| &nbsp;&nbsp; public void [setSFRotation](reference/supervisor.md)(double values[4]); |
| &nbsp;&nbsp; public void [setSFColor](reference/supervisor.md)(double values[3]); |
| &nbsp;&nbsp; public void [setSFString](reference/supervisor.md)(String value); |
| &nbsp;&nbsp; public void [setMFBool](reference/supervisor.md)(int index, bool value); |
| &nbsp;&nbsp; public void [setMFInt32](reference/supervisor.md)(int index, int value); |
| &nbsp;&nbsp; public void [setMFFloat](reference/supervisor.md)(int index, double value); |
| &nbsp;&nbsp; public void [setMFVec2f](reference/supervisor.md)(int index, double values[2]); |
| &nbsp;&nbsp; public void [setMFVec3f](reference/supervisor.md)(int index, double values[3]); |
| &nbsp;&nbsp; public void [setMFRotation](reference/supervisor.md)(int index, double values[4]); |
| &nbsp;&nbsp; public void [setMFColor](reference/supervisor.md)(int index, double values[3]); |
| &nbsp;&nbsp; public void [setMFString](reference/supervisor.md)(int index, String value); |
| &nbsp;&nbsp; public void [importMFNode](reference/supervisor.md)(int position, String filename); |
| &nbsp;&nbsp; public void [importMFNodeFromString](reference/supervisor.md)(int position, String nodeString); |
| &nbsp;&nbsp; public void [removeMFNode](reference/supervisor.md)(int position); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.GPS; |
| public class [GPS](reference/gps.md#gps) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enable](reference/gps.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/gps.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/gps.md)(); |
| &nbsp;&nbsp; public double[] [getValues](reference/gps.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Gyro; |
| public class [Gyro](reference/gyro.md#gyro) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enable](reference/gyro.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/gyro.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/gyro.md)(); |
| &nbsp;&nbsp; public double[] [getValues](reference/gyro.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.ImageRef; |
| public class ImageRef { |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.InertialUnit; |
| public class [InertialUnit](reference/inertialunit.md#inertialunit) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enable](reference/inertialunit.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/inertialunit.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/inertialunit.md)(); |
| &nbsp;&nbsp; public double[] [getRollPitchYaw](reference/inertialunit.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.LED; |
| public class [LED](reference/led.md#led) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [set](reference/led.md)(int state); |
| &nbsp;&nbsp; public int [get](reference/led.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.LightSensor; |
| public class [LightSensor](reference/lightsensor.md#lightsensor) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [enable](reference/lightsensor.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/lightsensor.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/lightsensor.md)(); |
| &nbsp;&nbsp; public double [getValue](reference/lightsensor.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Motion; |
| public class [Motion](reference/motion.md#motion) { |
| &nbsp;&nbsp; public [Motion](reference/motion.md)(String fileName); |
| &nbsp;&nbsp; protected void [finalize](reference/motion.md)(); |
| &nbsp;&nbsp; public bool [isValid](reference/motion.md)(); |
| &nbsp;&nbsp; public void [play](reference/motion.md)(); |
| &nbsp;&nbsp; public void [stop](reference/motion.md)(); |
| &nbsp;&nbsp; public void [setLoop](reference/motion.md)(bool loop); |
| &nbsp;&nbsp; public void [setReverse](reference/motion.md)(bool reverse); |
| &nbsp;&nbsp; public bool [isOver](reference/motion.md)(); |
| &nbsp;&nbsp; public int [getDuration](reference/motion.md)(); |
| &nbsp;&nbsp; public int [getTime](reference/motion.md)(); |
| &nbsp;&nbsp; public void [setTime](reference/motion.md)(int time); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Motor; |
| public class [Motor](reference/motor.md#motor) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR; |
| &nbsp;&nbsp; public void [setPosition](reference/motor.md)(double position); |
| &nbsp;&nbsp; public void [setVelocity](reference/motor.md)(double vel); |
| &nbsp;&nbsp; public void [setAcceleration](reference/motor.md)(double force); |
| &nbsp;&nbsp; public void [setAvailableForce](reference/motor.md)(double motor\_force); |
| &nbsp;&nbsp; public void [setAvailableTorque](reference/motor.md)(double motor\_torque); |
| &nbsp;&nbsp; public void [setControlPID](reference/motor.md)(double p, double i, double d); |
| &nbsp;&nbsp; public double [getTargetPosition](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getMinPosition](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getMaxPosition](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getVelocity](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getMaxVelocity](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getAcceleration](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getAvailableForce](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getMaxForce](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getAvailableTorque](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getMaxTorque](reference/motor.md)(); |
| &nbsp;&nbsp; public void [enableForceFeedback](reference/motor.md)(int ms); |
| &nbsp;&nbsp; public void [disableForceFeedback](reference/motor.md)(); |
| &nbsp;&nbsp; public int [getForceFeedbackSamplingPeriod](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getForceFeedback](reference/motor.md)(); |
| &nbsp;&nbsp; public void [setForce](reference/motor.md)(double force); |
| &nbsp;&nbsp; public void [enableTorqueFeedback](reference/motor.md)(int ms); |
| &nbsp;&nbsp; public void [disableTorqueFeedback](reference/motor.md)(); |
| &nbsp;&nbsp; public int [getTorqueFeedbackSamplingPeriod](reference/motor.md)(); |
| &nbsp;&nbsp; public double [getTorqueFeedback](reference/motor.md)(); |
| &nbsp;&nbsp; public void [setTorque](reference/motor.md)(double torque); |
| &nbsp;&nbsp; public int [getType](reference/motor.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Node; |
| public class Node { |
| &nbsp;&nbsp; public final static int NO\_NODE, APPEARANCE, BACKGROUND, |
| &nbsp;&nbsp; BOX, COLOR, CONE, COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT, |
| &nbsp;&nbsp; ELEVATION\_GRID, EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE, |
| &nbsp;&nbsp; INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT, |
| &nbsp;&nbsp; SHAPE, SPHERE, SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE, |
| &nbsp;&nbsp; TEXTURE\_TRANSFORM, TRANSFORM, VIEWPOINT, WORLD\_INFO, |
| &nbsp;&nbsp; CAPSULE, PLANE, ROBOT, SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID, |
| &nbsp;&nbsp; PHYSICS, CAMER\_ZOOM, CHARGER, DAMPING, |
| &nbsp;&nbsp; CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE, CAMERA, COMPASS, |
| &nbsp;&nbsp; CONNECTOR, DISPLAY, DISTANCE\_SENSOR, EMITTER, GPS, GYRO, LED, |
| &nbsp;&nbsp; LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN, POSITION\_SENSOR, RADIO, |
| &nbsp;&nbsp; RECEIVER, SERVO, SPEAKER, TOUCH\_SENSOR; |
| &nbsp;&nbsp; public void [remove](reference/supervisor.md)(); |
| &nbsp;&nbsp; public int [getId](reference/supervisor.md)(); |
| &nbsp;&nbsp; public int [getType](reference/supervisor.md)(); |
| &nbsp;&nbsp; public String [getTypeName](reference/supervisor.md)(); |
| &nbsp;&nbsp; public String [getBaseTypeName](reference/supervisor.md)(); |
| &nbsp;&nbsp; public [Field](reference/java-api.md) [getField](reference/supervisor.md)(String fieldName); |
| &nbsp;&nbsp; public Node [getParentNode](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getPosition](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getOrientation](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getCenterOfMass](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getContactPoint](reference/supervisor.md)(int index); |
| &nbsp;&nbsp; public int [getNumberOfContactPoints](reference/supervisor.md)(); |
| &nbsp;&nbsp; public bool [getStaticBalance](reference/supervisor.md)(); |
| &nbsp;&nbsp; public double[] [getVelocity](reference/supervisor.md)(); |
| &nbsp;&nbsp; public void [setVelocity](reference/supervisor.md)(double velocity[6]); |
| &nbsp;&nbsp; public void [resetPhysics](reference/supervisor.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Pen; |
| public class [Pen](reference/pen.md#pen) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public void [write](reference/pen.md)(bool write); |
| &nbsp;&nbsp; public void [setInkColor](reference/pen.md)(int color, double density); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.PositionSensor; |
| public class [PositionSensor](reference/positionsensor.md#positionsensor) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int ANGULAR, LINEAR; |
| &nbsp;&nbsp; public void [enable](reference/positionsensor.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/positionsensor.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/positionsensor.md)(); |
| &nbsp;&nbsp; public double [getValue](reference/positionsensor.md)(); |
| &nbsp;&nbsp; public int [getType](reference/positionsensor.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Receiver; |
| public class [Receiver](reference/receiver.md#receiver) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST; |
| &nbsp;&nbsp; public void [enable](reference/receiver.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/receiver.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/receiver.md)(); |
| &nbsp;&nbsp; public int [getQueueLength](reference/receiver.md)(); |
| &nbsp;&nbsp; public void [nextPacket](reference/receiver.md)(); |
| &nbsp;&nbsp; public byte[] [getData](reference/receiver.md)(); |
| &nbsp;&nbsp; public int [getDataSize](reference/receiver.md)(); |
| &nbsp;&nbsp; public double [getSignalStrength](reference/receiver.md)(); |
| &nbsp;&nbsp; public double[] [getEmitterDirection](reference/receiver.md)(); |
| &nbsp;&nbsp; public void [setChannel](reference/receiver.md)(int channel); |
| &nbsp;&nbsp; public int [getChannel](reference/receiver.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Robot; |
| public class [Robot](reference/robot.md#robot) { |
| &nbsp;&nbsp; public final static int MODE\_SIMULATION, |
| &nbsp;&nbsp; MODE\_CROSS\_COMPILATION, MODE\_REMOTE\_CONTROL; |
| &nbsp;&nbsp; public final static int KEYBOARD\_END, KEYBOARD\_HOME, |
| &nbsp;&nbsp; KEYBOARD\_LEFT, KEYBOARD\_UP, KEYBOARD\_RIGHT, |
| &nbsp;&nbsp; KEYBOARD\_DOWN, KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END, |
| &nbsp;&nbsp; KEYBOARD\_KEY, KEYBOARD\_SHIFT, |
| &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT; |
| &nbsp;&nbsp; public [Robot](reference/robot.md)(); |
| &nbsp;&nbsp; protected void [finalize](reference/robot.md)(); |
| &nbsp;&nbsp; public int [step](reference/robot.md)(int ms); |
| &nbsp;&nbsp; public [Accelerometer](reference/java-api.md) [getAccelerometer](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Brake](reference/java-api.md) [getBrake](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Camera](reference/java-api.md) [getCamera](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Compass](reference/java-api.md) [getCompass](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Connector](reference/java-api.md) [getConnector](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Display](reference/java-api.md) [getDisplay](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [DistanceSensor](reference/java-api.md) [getDistanceSensor](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Emitter](reference/java-api.md) [getEmitter](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [GPS](reference/java-api.md) [getGPS](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Gyro](reference/java-api.md) [getGyro](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [InertialUnit](reference/java-api.md) [getInertialUnit](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [LED](reference/java-api.md) [getLED](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [LightSensor](reference/java-api.md) [getLightSensor](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Motor](reference/java-api.md) [getMotor](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Pen](reference/java-api.md) [getPen](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [PositionSensor](reference/java-api.md) [getPositionSensor](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Receiver](reference/java-api.md) [getReceiver](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [Servo](reference/java-api.md) [getServo](reference/robot.md)(String name); |
| &nbsp;&nbsp; public [TouchSensor](reference/java-api.md) [getTouchSensor](reference/robot.md)(String name); |
| &nbsp;&nbsp; public int [getNumberOfDevices](reference/robot.md)(); |
| &nbsp;&nbsp; public [Device](reference/java-api.md) [getDeviceByIndex](reference/robot.md)(int index); |
| &nbsp;&nbsp; public void [batterySensorEnable](reference/robot.md)(int ms); |
| &nbsp;&nbsp; public void [batterySensorDisable](reference/robot.md)(); |
| &nbsp;&nbsp; public int [batterySensorGetSamplingPeriod](reference/robot.md)(); |
| &nbsp;&nbsp; public double [batterySensorGetValue](reference/robot.md)(); |
| &nbsp;&nbsp; public double [getBasicTimeStep](reference/robot.md)(); |
| &nbsp;&nbsp; public int [getMode](reference/robot.md)(); |
| &nbsp;&nbsp; public String [getModel](reference/robot.md)(); |
| &nbsp;&nbsp; public String [getData](reference/robot.md)(); |
| &nbsp;&nbsp; public [setData](reference/robot.md)(String data); |
| &nbsp;&nbsp; public String [getName](reference/robot.md)(); |
| &nbsp;&nbsp; public String [getControllerName](reference/robot.md)(); |
| &nbsp;&nbsp; public String [getControllerArguments](reference/robot.md)(); |
| &nbsp;&nbsp; public String [getProjectPath](reference/robot.md)(); |
| &nbsp;&nbsp; public bool [getSynchronization](reference/robot.md)(); |
| &nbsp;&nbsp; public double [getTime](reference/robot.md)(); |
| &nbsp;&nbsp; public String [getWorldPath](reference/robot.md)(); |
| &nbsp;&nbsp; public void [keyboardEnable](reference/robot.md)(int ms); |
| &nbsp;&nbsp; public void [keyboardDisable](reference/robot.md)(); |
| &nbsp;&nbsp; public int [keyboardGetKey](reference/robot.md)(); |
| &nbsp;&nbsp; public int [getType](reference/robot.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Servo; |
| public class [Servo](reference/servo.md#servo) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR; |
| &nbsp;&nbsp; public void [setPosition](reference/servo.md)(double position); |
| &nbsp;&nbsp; public double [getTargetPosition](reference/servo.md)(); |
| &nbsp;&nbsp; public void [setVelocity](reference/servo.md)(double vel); |
| &nbsp;&nbsp; public void [setAcceleration](reference/servo.md)(double force); |
| &nbsp;&nbsp; public void [setMotorForce](reference/servo.md)(double motor\_force); |
| &nbsp;&nbsp; public void [setControlP](reference/servo.md)(double p); |
| &nbsp;&nbsp; public double [getMinPosition](reference/servo.md)(); |
| &nbsp;&nbsp; public double [getMaxPosition](reference/servo.md)(); |
| &nbsp;&nbsp; public void [enablePosition](reference/servo.md)(int ms); |
| &nbsp;&nbsp; public void [disablePosition](reference/servo.md)(); |
| &nbsp;&nbsp; public int [getPositionSamplingPeriod](reference/servo.md)(); |
| &nbsp;&nbsp; public double [getPosition](reference/servo.md)(); |
| &nbsp;&nbsp; public void [enableMotorForceFeedback](reference/servo.md)(int ms); |
| &nbsp;&nbsp; public void [disableMotorForceFeedback](reference/servo.md)(); |
| &nbsp;&nbsp; public int [getMotorForceFeedbackSamplingPeriod](reference/servo.md)(); |
| &nbsp;&nbsp; public double [getMotorForceFeedback](reference/servo.md)(); |
| &nbsp;&nbsp; public void [setForce](reference/servo.md)(double force); |
| &nbsp;&nbsp; public int [getType](reference/servo.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Supervisor; |
| public class [Supervisor](reference/supervisor.md#supervisor) extends [Robot](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR |
| &nbsp;&nbsp; public [Supervisor](reference/robot.md)(); |
| &nbsp;&nbsp; protected void [finalize](reference/robot.md)(); |
| &nbsp;&nbsp; public void [exportImage](reference/supervisor.md)(String file, int quality); |
| &nbsp;&nbsp; public [Node](reference/java-api.md) [getRoot](reference/supervisor.md)(); |
| &nbsp;&nbsp; public [Node](reference/java-api.md) [getSelf](reference/supervisor.md)(); |
| &nbsp;&nbsp; public [Node](reference/java-api.md) [getFromDef](reference/supervisor.md)(String name); |
| &nbsp;&nbsp; public [Node](reference/java-api.md) [getFromId](reference/supervisor.md)(int id); |
| &nbsp;&nbsp; public void [setLabel](reference/supervisor.md)(int id, String label, double xpos, double ypos, |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency); |
| &nbsp;&nbsp; public void [simulationQuit](reference/supervisor.md)(int status); |
| &nbsp;&nbsp; public void [simulationRevert](reference/supervisor.md)(); |
| &nbsp;&nbsp; public void [simulationResetPhysics](reference/supervisor.md)(); |
| &nbsp;&nbsp; public void [loadWorld](reference/supervisor.md)(String file); |
| &nbsp;&nbsp; public void [saveWorld](reference/supervisor.md)(); |
| &nbsp;&nbsp; public void [saveWorld](reference/supervisor.md)(String file); |
| &nbsp;&nbsp; public void [movieStartRecording](reference/supervisor.md)(String file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp;&nbsp;&nbsp; int acceleration, boolean caption); |
| &nbsp;&nbsp; public void [movieStopRecording](reference/supervisor.md)(); |
| &nbsp;&nbsp; public int [movieGetStatus](reference/supervisor.md)(); |
| &nbsp;&nbsp; public bool [animationStartRecording](reference/supervisor.md)(String file); |
| &nbsp;&nbsp; public bool [animationStopRecording](reference/supervisor.md)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.TouchSensor; |
| public class [TouchSensor](reference/touchsensor.md#touchsensor) extends [Device](reference/java-api.md) { |
| &nbsp;&nbsp; public final static int BUMPER, FORCE, FORCE3D; |
| &nbsp;&nbsp; public void [enable](reference/touchsensor.md)(int ms); |
| &nbsp;&nbsp; public void [disable](reference/touchsensor.md)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](reference/touchsensor.md)(); |
| &nbsp;&nbsp; public double [getValue](reference/touchsensor.md)(); |
| &nbsp;&nbsp; public double[] [getValues](reference/touchsensor.md)(); |
| &nbsp;&nbsp; public int [getType](reference/touchsensor.md)(); |
| } |

