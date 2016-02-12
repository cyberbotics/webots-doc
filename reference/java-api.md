## Java API

The following tables describe the Java classes and their methods.

| |
| --- |
| import com.cyberbotics.webots.controller.Accelerometer; |
| public class [Accelerometer](accelerometer.md#accelerometer) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enable](accelerometer.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](accelerometer.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](accelerometer.md#description)(); |
| &nbsp;&nbsp; public double[] [getValues](accelerometer.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Brake; |
| public class [Brake](brake.md#brake) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [setDampingConstant](brake.md#description)(double dampingConstant); |
| &nbsp;&nbsp; public int [getType](brake.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Camera; |
| public class [Camera](camera.md#camera) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int COLOR, RANGE\_FINDER, BOTH; |
| &nbsp;&nbsp; public void [enable](camera.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](camera.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](camera.md#description)(); |
| &nbsp;&nbsp; public double [getFov](camera.md#description)(); |
| &nbsp;&nbsp; public double [getMinFov](camera.md#description)(); |
| &nbsp;&nbsp; public double [getMaxFov](camera.md#description)(); |
| &nbsp;&nbsp; public void [setFov](camera.md#description)(double fov); |
| &nbsp;&nbsp; public double [getFocalLength](camera.md#description)(); |
| &nbsp;&nbsp; public double [getFocalDistance](camera.md#description)(); |
| &nbsp;&nbsp; public double [getMaxFocalDistance](camera.md#description)(); |
| &nbsp;&nbsp; public double [getMinFocalDistance](camera.md#description)(); |
| &nbsp;&nbsp; public void [setFocalDistance](camera.md#description)(double focalDistance); |
| &nbsp;&nbsp; public int [getWidth](camera.md#description)(); |
| &nbsp;&nbsp; public int [getHeight](camera.md#description)(); |
| &nbsp;&nbsp; public double [getNear](camera.md#description)(); |
| &nbsp;&nbsp; public double [getMaxRange](camera.md#description)(); |
| &nbsp;&nbsp; public int [getType](camera.md#description)(); |
| &nbsp;&nbsp; public int[] [getImage](camera.md#description)(); |
| &nbsp;&nbsp; public static int [imageGetRed](camera.md#description)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetGreen](camera.md#description)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetBlue](camera.md#description)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [imageGetGrey](camera.md#description)(int[] image, int width, int x, int y); |
| &nbsp;&nbsp; public static int [pixelGetRed](camera.md#description)(int pixel); |
| &nbsp;&nbsp; public static int [pixelGetGreen](camera.md#description)(int pixel); |
| &nbsp;&nbsp; public static int [pixelGetBlue](camera.md#description)(int pixel); |
| &nbsp;&nbsp; public static int [pixelGetGrey](camera.md#description)(int pixel); |
| &nbsp;&nbsp; public float[] [getRangeImage](camera.md#description)(); |
| &nbsp;&nbsp; public static float [rangeImageGetDepth](camera.md#description)(float[] image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; public int [saveImage](camera.md#description)(String filename, int quality); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Compass; |
| public class [Compass](compass.md#compass) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enable](compass.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](compass.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](compass.md#description)(); |
| &nbsp;&nbsp; public double[] [getValues](compass.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Connector; |
| public class [Connector](connector.md#connector) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enablePresence](connector.md#description)(int ms); |
| &nbsp;&nbsp; public void [disablePresence](connector.md#description)(); |
| &nbsp;&nbsp; public int [getPresence](connector.md#description)(); |
| &nbsp;&nbsp; public void [lock](connector.md#description)(); |
| &nbsp;&nbsp; public void [unlock](connector.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Device; |
| public class [Device](device.md#device) { |
| &nbsp;&nbsp; public String [getModel](device.md#description)(); |
| &nbsp;&nbsp; public String [getName](device.md#description)(); |
| &nbsp;&nbsp; public int [getNodeType](device.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.DifferentialWheels; |
| public class [DifferentialWheels](differentialwheels.md#differentialwheels) extends [Robot](java-api.md) { |
| &nbsp;&nbsp; public [DifferentialWheels](robot.md#description)(); |
| &nbsp;&nbsp; protected void [finalize](robot.md#description)(); |
| &nbsp;&nbsp; public void [setSpeed](differentialwheels.md#description)(double left, double right); |
| &nbsp;&nbsp; public double [getLeftSpeed](differentialwheels.md#description)(); |
| &nbsp;&nbsp; public double [getRightSpeed](differentialwheels.md#description)(); |
| &nbsp;&nbsp; public void [enableEncoders](differentialwheels.md#description)(int ms); |
| &nbsp;&nbsp; public void [disableEncoders](differentialwheels.md#description)(); |
| &nbsp;&nbsp; public int [getEncodersSamplingPeriod](differentialwheels.md#description)(); |
| &nbsp;&nbsp; public double [getLeftEncoder](differentialwheels.md#description)(); |
| &nbsp;&nbsp; public double [getRightEncoder](differentialwheels.md#description)(); |
| &nbsp;&nbsp; public void [setEncoders](differentialwheels.md#description)(double left, double right); |
| &nbsp;&nbsp; public double [getMaxSpeed](differentialwheels.md#description)(); |
| &nbsp;&nbsp; public double [getSpeedUnit](differentialwheels.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Display; |
| public class [Display](display.md#display) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int RGB, RGBA, ARGB, BGRA; |
| &nbsp;&nbsp; public int [getWidth](display.md#description)(); |
| &nbsp;&nbsp; public int [getHeight](display.md#description)(); |
| &nbsp;&nbsp; public void [setColor](display.md#description)(int color); |
| &nbsp;&nbsp; public void [setAlpha](display.md#description)(double alpha); |
| &nbsp;&nbsp; public void [setOpacity](display.md#description)(double opacity); |
| &nbsp;&nbsp; public void [drawPixel](display.md#description)(int x1, int y1); |
| &nbsp;&nbsp; public void [drawLine](display.md#description)(int x1, int y1, int x2, int y2); |
| &nbsp;&nbsp; public void [drawRectangle](display.md#description)(int x, int y, int width, int height); |
| &nbsp;&nbsp; public void [drawOval](display.md#description)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; public void [drawPolygon](display.md#description)(int[] x, int[] y); |
| &nbsp;&nbsp; public void [drawText](display.md#description)(String txt, int x, int y); |
| &nbsp;&nbsp; public void [fillRectangle](display.md#description)(int x, int y, int width, int height); |
| &nbsp;&nbsp; public void [fillOval](display.md#description)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; public void [fillPolygon](display.md#description)(int[] x, int[] y); |
| &nbsp;&nbsp; public [ImageRef](java-api.md) [imageCopy](display.md#description)(int x, int y, int width, int height); |
| &nbsp;&nbsp; public void [imagePaste](display.md#description)([ImageRef](java-api.md) ir, int x, int y); |
| &nbsp;&nbsp; public [ImageRef](java-api.md) [imageLoad](display.md#description)(String filename); |
| &nbsp;&nbsp; public [ImageRef](java-api.md) [imageNew](display.md#description)(int width, int height, int[] data, int format); |
| &nbsp;&nbsp; public void [imageSave](display.md#description)([ImageRef](java-api.md) ir, String filename); |
| &nbsp;&nbsp; public void [imageDelete](display.md#description)([ImageRef](java-api.md) ir); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.DistanceSensor; |
| public class [DistanceSensor](distancesensor.md#distancesensor) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enable](distancesensor.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](distancesensor.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](distancesensor.md#description)(); |
| &nbsp;&nbsp; public double [getValue](distancesensor.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Emitter; |
| public class [Emitter](emitter.md#emitter) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST; |
| &nbsp;&nbsp; public int [send](emitter.md#description)(byte[] data); |
| &nbsp;&nbsp; public int [getChannel](emitter.md#description)(); |
| &nbsp;&nbsp; public void [setChannel](emitter.md#description)(int channel); |
| &nbsp;&nbsp; public double [getRange](emitter.md#description)(); |
| &nbsp;&nbsp; public void [setRange](emitter.md#description)(double range); |
| &nbsp;&nbsp; public int [getBufferSize](emitter.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Field; |
| public class Field { |
| &nbsp;&nbsp; public final static int SF\_BOOL, SF\_INT32, SF\_FLOAT, |
| &nbsp;&nbsp; SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, |
| &nbsp;&nbsp; SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, |
| &nbsp;&nbsp; MF\_COLOR, MF\_STRING, MF\_NODE; |
| &nbsp;&nbsp; public int [getType](supervisor.md#description)(); |
| &nbsp;&nbsp; public String [getTypeName](supervisor.md#description)(); |
| &nbsp;&nbsp; public int [getCount](supervisor.md#description)(); |
| &nbsp;&nbsp; public bool [getSFBool](supervisor.md#description)(); |
| &nbsp;&nbsp; public int [getSFInt32](supervisor.md#description)(); |
| &nbsp;&nbsp; public double [getSFFloat](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getSFVec2f](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getSFVec3f](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getSFRotation](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getSFColor](supervisor.md#description)(); |
| &nbsp;&nbsp; public String [getSFString](supervisor.md#description)(); |
| &nbsp;&nbsp; public [Node](java-api.md) [getSFNode](supervisor.md#description)(); |
| &nbsp;&nbsp; public bool [getMFBool](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public int [getMFInt32](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public double [getMFFloat](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public double[] [getMFVec2f](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public double[] [getMFVec3f](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public double[] [getMFColor](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public double[] [getMFRotation](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public String [getMFString](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public [Node](java-api.md) [getMFNode](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public void [setSFBool](supervisor.md#description)(bool value); |
| &nbsp;&nbsp; public void [setSFInt32](supervisor.md#description)(int value); |
| &nbsp;&nbsp; public void [setSFFloat](supervisor.md#description)(double value); |
| &nbsp;&nbsp; public void [setSFVec2f](supervisor.md#description)(double values[2]); |
| &nbsp;&nbsp; public void [setSFVec3f](supervisor.md#description)(double values[3]); |
| &nbsp;&nbsp; public void [setSFRotation](supervisor.md#description)(double values[4]); |
| &nbsp;&nbsp; public void [setSFColor](supervisor.md#description)(double values[3]); |
| &nbsp;&nbsp; public void [setSFString](supervisor.md#description)(String value); |
| &nbsp;&nbsp; public void [setMFBool](supervisor.md#description)(int index, bool value); |
| &nbsp;&nbsp; public void [setMFInt32](supervisor.md#description)(int index, int value); |
| &nbsp;&nbsp; public void [setMFFloat](supervisor.md#description)(int index, double value); |
| &nbsp;&nbsp; public void [setMFVec2f](supervisor.md#description)(int index, double values[2]); |
| &nbsp;&nbsp; public void [setMFVec3f](supervisor.md#description)(int index, double values[3]); |
| &nbsp;&nbsp; public void [setMFRotation](supervisor.md#description)(int index, double values[4]); |
| &nbsp;&nbsp; public void [setMFColor](supervisor.md#description)(int index, double values[3]); |
| &nbsp;&nbsp; public void [setMFString](supervisor.md#description)(int index, String value); |
| &nbsp;&nbsp; public void [importMFNode](supervisor.md#description)(int position, String filename); |
| &nbsp;&nbsp; public void [importMFNodeFromString](supervisor.md#description)(int position, String nodeString); |
| &nbsp;&nbsp; public void [removeMFNode](supervisor.md#description)(int position); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.GPS; |
| public class [GPS](gps.md#gps) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enable](gps.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](gps.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](gps.md#description)(); |
| &nbsp;&nbsp; public double[] [getValues](gps.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Gyro; |
| public class [Gyro](gyro.md#gyro) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enable](gyro.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](gyro.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](gyro.md#description)(); |
| &nbsp;&nbsp; public double[] [getValues](gyro.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.ImageRef; |
| public class ImageRef { |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.InertialUnit; |
| public class [InertialUnit](inertialunit.md#inertialunit) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enable](inertialunit.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](inertialunit.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](inertialunit.md#description)(); |
| &nbsp;&nbsp; public double[] [getRollPitchYaw](inertialunit.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.LED; |
| public class [LED](led.md#led) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [set](led.md#description)(int state); |
| &nbsp;&nbsp; public int [get](led.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.LightSensor; |
| public class [LightSensor](lightsensor.md#lightsensor) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [enable](lightsensor.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](lightsensor.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](lightsensor.md#description)(); |
| &nbsp;&nbsp; public double [getValue](lightsensor.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Motion; |
| public class [Motion](motion.md#motion) { |
| &nbsp;&nbsp; public [Motion](motion.md#description)(String fileName); |
| &nbsp;&nbsp; protected void [finalize](motion.md#description)(); |
| &nbsp;&nbsp; public bool [isValid](motion.md#description)(); |
| &nbsp;&nbsp; public void [play](motion.md#description)(); |
| &nbsp;&nbsp; public void [stop](motion.md#description)(); |
| &nbsp;&nbsp; public void [setLoop](motion.md#description)(bool loop); |
| &nbsp;&nbsp; public void [setReverse](motion.md#description)(bool reverse); |
| &nbsp;&nbsp; public bool [isOver](motion.md#description)(); |
| &nbsp;&nbsp; public int [getDuration](motion.md#description)(); |
| &nbsp;&nbsp; public int [getTime](motion.md#description)(); |
| &nbsp;&nbsp; public void [setTime](motion.md#description)(int time); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Motor; |
| public class [Motor](motor.md#motor) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR; |
| &nbsp;&nbsp; public void [setPosition](motor.md#description)(double position); |
| &nbsp;&nbsp; public void [setVelocity](motor.md#description)(double vel); |
| &nbsp;&nbsp; public void [setAcceleration](motor.md#description)(double force); |
| &nbsp;&nbsp; public void [setAvailableForce](motor.md#description)(double motor\_force); |
| &nbsp;&nbsp; public void [setAvailableTorque](motor.md#description)(double motor\_torque); |
| &nbsp;&nbsp; public void [setControlPID](motor.md#description)(double p, double i, double d); |
| &nbsp;&nbsp; public double [getTargetPosition](motor.md#description)(); |
| &nbsp;&nbsp; public double [getMinPosition](motor.md#description)(); |
| &nbsp;&nbsp; public double [getMaxPosition](motor.md#description)(); |
| &nbsp;&nbsp; public double [getVelocity](motor.md#description)(); |
| &nbsp;&nbsp; public double [getMaxVelocity](motor.md#description)(); |
| &nbsp;&nbsp; public double [getAcceleration](motor.md#description)(); |
| &nbsp;&nbsp; public double [getAvailableForce](motor.md#description)(); |
| &nbsp;&nbsp; public double [getMaxForce](motor.md#description)(); |
| &nbsp;&nbsp; public double [getAvailableTorque](motor.md#description)(); |
| &nbsp;&nbsp; public double [getMaxTorque](motor.md#description)(); |
| &nbsp;&nbsp; public void [enableForceFeedback](motor.md#description)(int ms); |
| &nbsp;&nbsp; public void [disableForceFeedback](motor.md#description)(); |
| &nbsp;&nbsp; public int [getForceFeedbackSamplingPeriod](motor.md#description)(); |
| &nbsp;&nbsp; public double [getForceFeedback](motor.md#description)(); |
| &nbsp;&nbsp; public void [setForce](motor.md#description)(double force); |
| &nbsp;&nbsp; public void [enableTorqueFeedback](motor.md#description)(int ms); |
| &nbsp;&nbsp; public void [disableTorqueFeedback](motor.md#description)(); |
| &nbsp;&nbsp; public int [getTorqueFeedbackSamplingPeriod](motor.md#description)(); |
| &nbsp;&nbsp; public double [getTorqueFeedback](motor.md#description)(); |
| &nbsp;&nbsp; public void [setTorque](motor.md#description)(double torque); |
| &nbsp;&nbsp; public int [getType](motor.md#description)(); |
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
| &nbsp;&nbsp; public void [remove](supervisor.md#description)(); |
| &nbsp;&nbsp; public int [getId](supervisor.md#description)(); |
| &nbsp;&nbsp; public int [getType](supervisor.md#description)(); |
| &nbsp;&nbsp; public String [getTypeName](supervisor.md#description)(); |
| &nbsp;&nbsp; public String [getBaseTypeName](supervisor.md#description)(); |
| &nbsp;&nbsp; public [Field](java-api.md) [getField](supervisor.md#description)(String fieldName); |
| &nbsp;&nbsp; public Node [getParentNode](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getPosition](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getOrientation](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getCenterOfMass](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getContactPoint](supervisor.md#description)(int index); |
| &nbsp;&nbsp; public int [getNumberOfContactPoints](supervisor.md#description)(); |
| &nbsp;&nbsp; public bool [getStaticBalance](supervisor.md#description)(); |
| &nbsp;&nbsp; public double[] [getVelocity](supervisor.md#description)(); |
| &nbsp;&nbsp; public void [setVelocity](supervisor.md#description)(double velocity[6]); |
| &nbsp;&nbsp; public void [resetPhysics](supervisor.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Pen; |
| public class [Pen](pen.md#pen) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public void [write](pen.md#description)(bool write); |
| &nbsp;&nbsp; public void [setInkColor](pen.md#description)(int color, double density); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.PositionSensor; |
| public class [PositionSensor](positionsensor.md#positionsensor) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int ANGULAR, LINEAR; |
| &nbsp;&nbsp; public void [enable](positionsensor.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](positionsensor.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](positionsensor.md#description)(); |
| &nbsp;&nbsp; public double [getValue](positionsensor.md#description)(); |
| &nbsp;&nbsp; public int [getType](positionsensor.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Receiver; |
| public class [Receiver](receiver.md#receiver) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST; |
| &nbsp;&nbsp; public void [enable](receiver.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](receiver.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](receiver.md#description)(); |
| &nbsp;&nbsp; public int [getQueueLength](receiver.md#description)(); |
| &nbsp;&nbsp; public void [nextPacket](receiver.md#description)(); |
| &nbsp;&nbsp; public byte[] [getData](receiver.md#description)(); |
| &nbsp;&nbsp; public int [getDataSize](receiver.md#description)(); |
| &nbsp;&nbsp; public double [getSignalStrength](receiver.md#description)(); |
| &nbsp;&nbsp; public double[] [getEmitterDirection](receiver.md#description)(); |
| &nbsp;&nbsp; public void [setChannel](receiver.md#description)(int channel); |
| &nbsp;&nbsp; public int [getChannel](receiver.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Robot; |
| public class [Robot](robot.md#robot) { |
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
| &nbsp;&nbsp; public [Robot](robot.md#description)(); |
| &nbsp;&nbsp; protected void [finalize](robot.md#description)(); |
| &nbsp;&nbsp; public int [step](robot.md#description)(int ms); |
| &nbsp;&nbsp; public [Accelerometer](java-api.md) [getAccelerometer](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Brake](java-api.md) [getBrake](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Camera](java-api.md) [getCamera](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Compass](java-api.md) [getCompass](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Connector](java-api.md) [getConnector](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Display](java-api.md) [getDisplay](robot.md#description)(String name); |
| &nbsp;&nbsp; public [DistanceSensor](java-api.md) [getDistanceSensor](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Emitter](java-api.md) [getEmitter](robot.md#description)(String name); |
| &nbsp;&nbsp; public [GPS](java-api.md) [getGPS](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Gyro](java-api.md) [getGyro](robot.md#description)(String name); |
| &nbsp;&nbsp; public [InertialUnit](java-api.md) [getInertialUnit](robot.md#description)(String name); |
| &nbsp;&nbsp; public [LED](java-api.md) [getLED](robot.md#description)(String name); |
| &nbsp;&nbsp; public [LightSensor](java-api.md) [getLightSensor](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Motor](java-api.md) [getMotor](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Pen](java-api.md) [getPen](robot.md#description)(String name); |
| &nbsp;&nbsp; public [PositionSensor](java-api.md) [getPositionSensor](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Receiver](java-api.md) [getReceiver](robot.md#description)(String name); |
| &nbsp;&nbsp; public [Servo](java-api.md) [getServo](robot.md#description)(String name); |
| &nbsp;&nbsp; public [TouchSensor](java-api.md) [getTouchSensor](robot.md#description)(String name); |
| &nbsp;&nbsp; public int [getNumberOfDevices](robot.md#description)(); |
| &nbsp;&nbsp; public [Device](java-api.md) [getDeviceByIndex](robot.md#description)(int index); |
| &nbsp;&nbsp; public void [batterySensorEnable](robot.md#description)(int ms); |
| &nbsp;&nbsp; public void [batterySensorDisable](robot.md#description)(); |
| &nbsp;&nbsp; public int [batterySensorGetSamplingPeriod](robot.md#description)(); |
| &nbsp;&nbsp; public double [batterySensorGetValue](robot.md#description)(); |
| &nbsp;&nbsp; public double [getBasicTimeStep](robot.md#description)(); |
| &nbsp;&nbsp; public int [getMode](robot.md#description)(); |
| &nbsp;&nbsp; public String [getModel](robot.md#description)(); |
| &nbsp;&nbsp; public String [getData](robot.md#description)(); |
| &nbsp;&nbsp; public [setData](robot.md#description)(String data); |
| &nbsp;&nbsp; public String [getName](robot.md#description)(); |
| &nbsp;&nbsp; public String [getControllerName](robot.md#description)(); |
| &nbsp;&nbsp; public String [getControllerArguments](robot.md#description)(); |
| &nbsp;&nbsp; public String [getProjectPath](robot.md#description)(); |
| &nbsp;&nbsp; public bool [getSynchronization](robot.md#description)(); |
| &nbsp;&nbsp; public double [getTime](robot.md#description)(); |
| &nbsp;&nbsp; public String [getWorldPath](robot.md#description)(); |
| &nbsp;&nbsp; public void [keyboardEnable](robot.md#description)(int ms); |
| &nbsp;&nbsp; public void [keyboardDisable](robot.md#description)(); |
| &nbsp;&nbsp; public int [keyboardGetKey](robot.md#description)(); |
| &nbsp;&nbsp; public int [getType](robot.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Servo; |
| public class [Servo](servo.md#servo) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR; |
| &nbsp;&nbsp; public void [setPosition](servo.md#description)(double position); |
| &nbsp;&nbsp; public double [getTargetPosition](servo.md#description)(); |
| &nbsp;&nbsp; public void [setVelocity](servo.md#description)(double vel); |
| &nbsp;&nbsp; public void [setAcceleration](servo.md#description)(double force); |
| &nbsp;&nbsp; public void [setMotorForce](servo.md#description)(double motor\_force); |
| &nbsp;&nbsp; public void [setControlP](servo.md#description)(double p); |
| &nbsp;&nbsp; public double [getMinPosition](servo.md#description)(); |
| &nbsp;&nbsp; public double [getMaxPosition](servo.md#description)(); |
| &nbsp;&nbsp; public void [enablePosition](servo.md#description)(int ms); |
| &nbsp;&nbsp; public void [disablePosition](servo.md#description)(); |
| &nbsp;&nbsp; public int [getPositionSamplingPeriod](servo.md#description)(); |
| &nbsp;&nbsp; public double [getPosition](servo.md#description)(); |
| &nbsp;&nbsp; public void [enableMotorForceFeedback](servo.md#description)(int ms); |
| &nbsp;&nbsp; public void [disableMotorForceFeedback](servo.md#description)(); |
| &nbsp;&nbsp; public int [getMotorForceFeedbackSamplingPeriod](servo.md#description)(); |
| &nbsp;&nbsp; public double [getMotorForceFeedback](servo.md#description)(); |
| &nbsp;&nbsp; public void [setForce](servo.md#description)(double force); |
| &nbsp;&nbsp; public int [getType](servo.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.Supervisor; |
| public class [Supervisor](supervisor.md#supervisor) extends [Robot](java-api.md) { |
| &nbsp;&nbsp; public final static int MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR |
| &nbsp;&nbsp; public [Supervisor](robot.md#description)(); |
| &nbsp;&nbsp; protected void [finalize](robot.md#description)(); |
| &nbsp;&nbsp; public void [exportImage](supervisor.md#description)(String file, int quality); |
| &nbsp;&nbsp; public [Node](java-api.md) [getRoot](supervisor.md#description)(); |
| &nbsp;&nbsp; public [Node](java-api.md) [getSelf](supervisor.md#description)(); |
| &nbsp;&nbsp; public [Node](java-api.md) [getFromDef](supervisor.md#description)(String name); |
| &nbsp;&nbsp; public [Node](java-api.md) [getFromId](supervisor.md#description)(int id); |
| &nbsp;&nbsp; public void [setLabel](supervisor.md#description)(int id, String label, double xpos, double ypos, |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency); |
| &nbsp;&nbsp; public void [simulationQuit](supervisor.md#description)(int status); |
| &nbsp;&nbsp; public void [simulationRevert](supervisor.md#description)(); |
| &nbsp;&nbsp; public void [simulationResetPhysics](supervisor.md#description)(); |
| &nbsp;&nbsp; public void [loadWorld](supervisor.md#description)(String file); |
| &nbsp;&nbsp; public void [saveWorld](supervisor.md#description)(); |
| &nbsp;&nbsp; public void [saveWorld](supervisor.md#description)(String file); |
| &nbsp;&nbsp; public void [movieStartRecording](supervisor.md#description)(String file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp;&nbsp;&nbsp; int acceleration, boolean caption); |
| &nbsp;&nbsp; public void [movieStopRecording](supervisor.md#description)(); |
| &nbsp;&nbsp; public int [movieGetStatus](supervisor.md#description)(); |
| &nbsp;&nbsp; public bool [animationStartRecording](supervisor.md#description)(String file); |
| &nbsp;&nbsp; public bool [animationStopRecording](supervisor.md#description)(); |
| } |

| |
| --- |
| import com.cyberbotics.webots.controller.TouchSensor; |
| public class [TouchSensor](touchsensor.md#touchsensor) extends [Device](java-api.md) { |
| &nbsp;&nbsp; public final static int BUMPER, FORCE, FORCE3D; |
| &nbsp;&nbsp; public void [enable](touchsensor.md#description)(int ms); |
| &nbsp;&nbsp; public void [disable](touchsensor.md#description)(); |
| &nbsp;&nbsp; public int [getSamplingPeriod](touchsensor.md#description)(); |
| &nbsp;&nbsp; public double [getValue](touchsensor.md#description)(); |
| &nbsp;&nbsp; public double[] [getValues](touchsensor.md#description)(); |
| &nbsp;&nbsp; public int [getType](touchsensor.md#description)(); |
| } |

