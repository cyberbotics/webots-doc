## Java API

The following tables describe the Java classes and their methods.

| |
| --- |
| import com.cyberbotics.webots.controller.Accelerometer;  |
|  public class `Accelerometer` extends `Device` {  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double[] `getValues`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Brake;  |
|  public class `Brake` extends `Device` {  |
|  &nbsp;&nbsp; public void `setDampingConstant`(double dampingConstant);  |
|  &nbsp;&nbsp; public int `getType`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Camera;  |
|  public class `Camera` extends `Device` {  |
|  &nbsp;&nbsp; public final static int COLOR, RANGE\_FINDER, BOTH;  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getFov`();  |
|  &nbsp;&nbsp; public double `getMinFov`();  |
|  &nbsp;&nbsp; public double `getMaxFov`();  |
|  &nbsp;&nbsp; public void `setFov`(double fov);  |
|  &nbsp;&nbsp; public double `getFocalLength`();  |
|  &nbsp;&nbsp; public double `getFocalDistance`();  |
|  &nbsp;&nbsp; public double `getMaxFocalDistance`();  |
|  &nbsp;&nbsp; public double `getMinFocalDistance`();  |
|  &nbsp;&nbsp; public void `setFocalDistance`(double focalDistance);  |
|  &nbsp;&nbsp; public int `getWidth`();  |
|  &nbsp;&nbsp; public int `getHeight`();  |
|  &nbsp;&nbsp; public double `getNear`();  |
|  &nbsp;&nbsp; public double `getMaxRange`();  |
|  &nbsp;&nbsp; public int `getType`();  |
|  &nbsp;&nbsp; public int[] `getImage`();  |
|  &nbsp;&nbsp; public static int `imageGetRed`(int[] image, int width, int x, int y);  |
|  &nbsp;&nbsp; public static int `imageGetGreen`(int[] image, int width, int x, int y);  |
|  &nbsp;&nbsp; public static int `imageGetBlue`(int[] image, int width, int x, int y);  |
|  &nbsp;&nbsp; public static int `imageGetGrey`(int[] image, int width, int x, int y);  |
|  &nbsp;&nbsp; public static int `pixelGetRed`(int pixel);  |
|  &nbsp;&nbsp; public static int `pixelGetGreen`(int pixel);  |
|  &nbsp;&nbsp; public static int `pixelGetBlue`(int pixel);  |
|  &nbsp;&nbsp; public static int `pixelGetGrey`(int pixel);  |
|  &nbsp;&nbsp; public float[] `getRangeImage`();  |
|  &nbsp;&nbsp; public static float `rangeImageGetDepth`(float[] image,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);  |
|  &nbsp;&nbsp; public int `saveImage`(String filename, int quality);  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Compass;  |
|  public class `Compass` extends `Device` {  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double[] `getValues`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Connector;  |
|  public class `Connector` extends `Device` {  |
|  &nbsp;&nbsp; public void `enablePresence`(int ms);  |
|  &nbsp;&nbsp; public void `disablePresence`();  |
|  &nbsp;&nbsp; public int `getPresence`();  |
|  &nbsp;&nbsp; public void `lock`();  |
|  &nbsp;&nbsp; public void `unlock`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Device;  |
|  public class `Device` {  |
|  &nbsp;&nbsp; public String `getModel`();  |
|  &nbsp;&nbsp; public String `getName`();  |
|  &nbsp;&nbsp; public int `getNodeType`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.DifferentialWheels;  |
|  public class `DifferentialWheels` extends `Robot` {  |
|  &nbsp;&nbsp; public `DifferentialWheels`();  |
|  &nbsp;&nbsp; protected void `finalize`();  |
|  &nbsp;&nbsp; public void `setSpeed`(double left, double right);  |
|  &nbsp;&nbsp; public double `getLeftSpeed`();  |
|  &nbsp;&nbsp; public double `getRightSpeed`();  |
|  &nbsp;&nbsp; public void `enableEncoders`(int ms);  |
|  &nbsp;&nbsp; public void `disableEncoders`();  |
|  &nbsp;&nbsp; public int `getEncodersSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getLeftEncoder`();  |
|  &nbsp;&nbsp; public double `getRightEncoder`();  |
|  &nbsp;&nbsp; public void `setEncoders`(double left, double right);  |
|  &nbsp;&nbsp; public double `getMaxSpeed`();  |
|  &nbsp;&nbsp; public double `getSpeedUnit`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Display;  |
|  public class `Display` extends `Device` {  |
|  &nbsp;&nbsp; public final static int RGB, RGBA, ARGB, BGRA;  |
|  &nbsp;&nbsp; public int `getWidth`();  |
|  &nbsp;&nbsp; public int `getHeight`();  |
|  &nbsp;&nbsp; public void `setColor`(int color);  |
|  &nbsp;&nbsp; public void `setAlpha`(double alpha);  |
|  &nbsp;&nbsp; public void `setOpacity`(double opacity);  |
|  &nbsp;&nbsp; public void `drawPixel`(int x1, int y1);  |
|  &nbsp;&nbsp; public void `drawLine`(int x1, int y1, int x2, int y2);  |
|  &nbsp;&nbsp; public void `drawRectangle`(int x, int y, int width, int height);  |
|  &nbsp;&nbsp; public void `drawOval`(int cx, int cy, int a, int b);  |
|  &nbsp;&nbsp; public void `drawPolygon`(int[] x, int[] y);  |
|  &nbsp;&nbsp; public void `drawText`(String txt, int x, int y);  |
|  &nbsp;&nbsp; public void `fillRectangle`(int x, int y, int width, int height);  |
|  &nbsp;&nbsp; public void `fillOval`(int cx, int cy, int a, int b);  |
|  &nbsp;&nbsp; public void `fillPolygon`(int[] x, int[] y);  |
|  &nbsp;&nbsp; public `ImageRef` `imageCopy`(int x, int y, int width, int height);  |
|  &nbsp;&nbsp; public void `imagePaste`(`ImageRef` ir, int x, int y);  |
|  &nbsp;&nbsp; public `ImageRef` `imageLoad`(String filename);  |
|  &nbsp;&nbsp; public `ImageRef` `imageNew`(int width, int height, int[] data, int format);  |
|  &nbsp;&nbsp; public void `imageSave`(`ImageRef` ir, String filename);  |
|  &nbsp;&nbsp; public void `imageDelete`(`ImageRef` ir);  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.DistanceSensor;  |
|  public class `DistanceSensor` extends `Device` {  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getValue`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Emitter;  |
|  public class `Emitter` extends `Device` {  |
|  &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST;  |
|  &nbsp;&nbsp; public int `send`(byte[] data);  |
|  &nbsp;&nbsp; public int `getChannel`();  |
|  &nbsp;&nbsp; public void `setChannel`(int channel);  |
|  &nbsp;&nbsp; public double `getRange`();  |
|  &nbsp;&nbsp; public void `setRange`(double range);  |
|  &nbsp;&nbsp; public int `getBufferSize`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Field;  |
|  public class Field {  |
|  &nbsp;&nbsp; public final static int SF\_BOOL, SF\_INT32, SF\_FLOAT,  |
|  &nbsp;&nbsp; SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING,  |
|  &nbsp;&nbsp; SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F,  |
|  &nbsp;&nbsp; MF\_COLOR, MF\_STRING, MF\_NODE;  |
|  &nbsp;&nbsp; public int `getType`();  |
|  &nbsp;&nbsp; public String `getTypeName`();  |
|  &nbsp;&nbsp; public int `getCount`();  |
|  &nbsp;&nbsp; public bool `getSFBool`();  |
|  &nbsp;&nbsp; public int `getSFInt32`();  |
|  &nbsp;&nbsp; public double `getSFFloat`();  |
|  &nbsp;&nbsp; public double[] `getSFVec2f`();  |
|  &nbsp;&nbsp; public double[] `getSFVec3f`();  |
|  &nbsp;&nbsp; public double[] `getSFRotation`();  |
|  &nbsp;&nbsp; public double[] `getSFColor`();  |
|  &nbsp;&nbsp; public String `getSFString`();  |
|  &nbsp;&nbsp; public `Node` `getSFNode`();  |
|  &nbsp;&nbsp; public bool `getMFBool`(int index);  |
|  &nbsp;&nbsp; public int `getMFInt32`(int index);  |
|  &nbsp;&nbsp; public double `getMFFloat`(int index);  |
|  &nbsp;&nbsp; public double[] `getMFVec2f`(int index);  |
|  &nbsp;&nbsp; public double[] `getMFVec3f`(int index);  |
|  &nbsp;&nbsp; public double[] `getMFColor`(int index);  |
|  &nbsp;&nbsp; public double[] `getMFRotation`(int index);  |
|  &nbsp;&nbsp; public String `getMFString`(int index);  |
|  &nbsp;&nbsp; public `Node` `getMFNode`(int index);  |
|  &nbsp;&nbsp; public void `setSFBool`(bool value);  |
|  &nbsp;&nbsp; public void `setSFInt32`(int value);  |
|  &nbsp;&nbsp; public void `setSFFloat`(double value);  |
|  &nbsp;&nbsp; public void `setSFVec2f`(double values[2]);  |
|  &nbsp;&nbsp; public void `setSFVec3f`(double values[3]);  |
|  &nbsp;&nbsp; public void `setSFRotation`(double values[4]);  |
|  &nbsp;&nbsp; public void `setSFColor`(double values[3]);  |
|  &nbsp;&nbsp; public void `setSFString`(String value);  |
|  &nbsp;&nbsp; public void `setMFBool`(int index, bool value);  |
|  &nbsp;&nbsp; public void `setMFInt32`(int index, int value);  |
|  &nbsp;&nbsp; public void `setMFFloat`(int index, double value);  |
|  &nbsp;&nbsp; public void `setMFVec2f`(int index, double values[2]);  |
|  &nbsp;&nbsp; public void `setMFVec3f`(int index, double values[3]);  |
|  &nbsp;&nbsp; public void `setMFRotation`(int index, double values[4]);  |
|  &nbsp;&nbsp; public void `setMFColor`(int index, double values[3]);  |
|  &nbsp;&nbsp; public void `setMFString`(int index, String value);  |
|  &nbsp;&nbsp; public void `importMFNode`(int position, String filename);  |
|  &nbsp;&nbsp; public void `importMFNodeFromString`(int position, String nodeString);  |
|  &nbsp;&nbsp; public void `removeMFNode`(int position);  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.GPS;  |
|  public class `GPS` extends `Device` {  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double[] `getValues`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Gyro;  |
|  public class `Gyro` extends `Device` {  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double[] `getValues`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.ImageRef;  |
|  public class ImageRef {  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.InertialUnit;  |
|  public class `InertialUnit` extends `Device` {  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double[] `getRollPitchYaw`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.LED;  |
|  public class `LED` extends `Device` {  |
|  &nbsp;&nbsp; public void `set`(int state);  |
|  &nbsp;&nbsp; public int `get`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.LightSensor;  |
|  public class `LightSensor` extends `Device` {  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getValue`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Motion;  |
|  public class `Motion` {  |
|  &nbsp;&nbsp; public `Motion`(String fileName);  |
|  &nbsp;&nbsp; protected void `finalize`();  |
|  &nbsp;&nbsp; public bool `isValid`();  |
|  &nbsp;&nbsp; public void `play`();  |
|  &nbsp;&nbsp; public void `stop`();  |
|  &nbsp;&nbsp; public void `setLoop`(bool loop);  |
|  &nbsp;&nbsp; public void `setReverse`(bool reverse);  |
|  &nbsp;&nbsp; public bool `isOver`();  |
|  &nbsp;&nbsp; public int `getDuration`();  |
|  &nbsp;&nbsp; public int `getTime`();  |
|  &nbsp;&nbsp; public void `setTime`(int time);  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Motor;  |
|  public class `Motor` extends `Device` {  |
|  &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR;  |
|  &nbsp;&nbsp; public void `setPosition`(double position);  |
|  &nbsp;&nbsp; public void `setVelocity`(double vel);  |
|  &nbsp;&nbsp; public void `setAcceleration`(double force);  |
|  &nbsp;&nbsp; public void `setAvailableForce`(double motor\_force);  |
|  &nbsp;&nbsp; public void `setAvailableTorque`(double motor\_torque);  |
|  &nbsp;&nbsp; public void `setControlPID`(double p, double i, double d);  |
|  &nbsp;&nbsp; public double `getTargetPosition`();  |
|  &nbsp;&nbsp; public double `getMinPosition`();  |
|  &nbsp;&nbsp; public double `getMaxPosition`();  |
|  &nbsp;&nbsp; public double `getVelocity`();  |
|  &nbsp;&nbsp; public double `getMaxVelocity`();  |
|  &nbsp;&nbsp; public double `getAcceleration`();  |
|  &nbsp;&nbsp; public double `getAvailableForce`();  |
|  &nbsp;&nbsp; public double `getMaxForce`();  |
|  &nbsp;&nbsp; public double `getAvailableTorque`();  |
|  &nbsp;&nbsp; public double `getMaxTorque`();  |
|  &nbsp;&nbsp; public void `enableForceFeedback`(int ms);  |
|  &nbsp;&nbsp; public void `disableForceFeedback`();  |
|  &nbsp;&nbsp; public int `getForceFeedbackSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getForceFeedback`();  |
|  &nbsp;&nbsp; public void `setForce`(double force);  |
|  &nbsp;&nbsp; public void `enableTorqueFeedback`(int ms);  |
|  &nbsp;&nbsp; public void `disableTorqueFeedback`();  |
|  &nbsp;&nbsp; public int `getTorqueFeedbackSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getTorqueFeedback`();  |
|  &nbsp;&nbsp; public void `setTorque`(double torque);  |
|  &nbsp;&nbsp; public int `getType`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Node;  |
|  public class Node {  |
|  &nbsp;&nbsp; public final static int NO\_NODE, APPEARANCE, BACKGROUND,  |
|  &nbsp;&nbsp; BOX, COLOR, CONE, COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT,  |
|  &nbsp;&nbsp; ELEVATION\_GRID, EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE,  |
|  &nbsp;&nbsp; INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT,  |
|  &nbsp;&nbsp; SHAPE, SPHERE, SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE,  |
|  &nbsp;&nbsp; TEXTURE\_TRANSFORM, TRANSFORM, VIEWPOINT, WORLD\_INFO,  |
|  &nbsp;&nbsp; CAPSULE, PLANE, ROBOT, SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID,  |
|  &nbsp;&nbsp; PHYSICS, CAMER\_ZOOM, CHARGER, DAMPING,  |
|  &nbsp;&nbsp; CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE, CAMERA, COMPASS,  |
|  &nbsp;&nbsp; CONNECTOR, DISPLAY, DISTANCE\_SENSOR, EMITTER, GPS, GYRO, LED,  |
|  &nbsp;&nbsp; LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN, POSITION\_SENSOR, RADIO,  |
|  &nbsp;&nbsp; RECEIVER, SERVO, SPEAKER, TOUCH\_SENSOR;  |
|  &nbsp;&nbsp; public void `remove`();  |
|  &nbsp;&nbsp; public int `getId`();  |
|  &nbsp;&nbsp; public int `getType`();  |
|  &nbsp;&nbsp; public String `getTypeName`();  |
|  &nbsp;&nbsp; public String `getBaseTypeName`();  |
|  &nbsp;&nbsp; public `Field` `getField`(String fieldName);  |
|  &nbsp;&nbsp; public Node `getParentNode`();  |
|  &nbsp;&nbsp; public double[] `getPosition`();  |
|  &nbsp;&nbsp; public double[] `getOrientation`();  |
|  &nbsp;&nbsp; public double[] `getCenterOfMass`();  |
|  &nbsp;&nbsp; public double[] `getContactPoint`(int index);  |
|  &nbsp;&nbsp; public int `getNumberOfContactPoints`();  |
|  &nbsp;&nbsp; public bool `getStaticBalance`();  |
|  &nbsp;&nbsp; public double[] `getVelocity`();  |
|  &nbsp;&nbsp; public void `setVelocity`(double velocity[6]);  |
|  &nbsp;&nbsp; public void `resetPhysics`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Pen;  |
|  public class `Pen` extends `Device` {  |
|  &nbsp;&nbsp; public void `write`(bool write);  |
|  &nbsp;&nbsp; public void `setInkColor`(int color, double density);  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.PositionSensor;  |
|  public class `PositionSensor` extends `Device` {  |
|  &nbsp;&nbsp; public final static int ANGULAR, LINEAR;  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getValue`();  |
|  &nbsp;&nbsp; public int `getType`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Receiver;  |
|  public class `Receiver` extends `Device` {  |
|  &nbsp;&nbsp; public final static int CHANNEL\_BROADCAST;  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public int `getQueueLength`();  |
|  &nbsp;&nbsp; public void `nextPacket`();  |
|  &nbsp;&nbsp; public byte[] `getData`();  |
|  &nbsp;&nbsp; public int `getDataSize`();  |
|  &nbsp;&nbsp; public double `getSignalStrength`();  |
|  &nbsp;&nbsp; public double[] `getEmitterDirection`();  |
|  &nbsp;&nbsp; public void `setChannel`(int channel);  |
|  &nbsp;&nbsp; public int `getChannel`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Robot;  |
|  public class `Robot` {  |
|  &nbsp;&nbsp; public final static int MODE\_SIMULATION,  |
|  &nbsp;&nbsp; MODE\_CROSS\_COMPILATION, MODE\_REMOTE\_CONTROL;  |
|  &nbsp;&nbsp; public final static int KEYBOARD\_END, KEYBOARD\_HOME,  |
|  &nbsp;&nbsp; KEYBOARD\_LEFT, KEYBOARD\_UP, KEYBOARD\_RIGHT,  |
|  &nbsp;&nbsp; KEYBOARD\_DOWN, KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END,  |
|  &nbsp;&nbsp; KEYBOARD\_KEY, KEYBOARD\_SHIFT,  |
|  &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT;  |
|  &nbsp;&nbsp; public `Robot`();  |
|  &nbsp;&nbsp; protected void `finalize`();  |
|  &nbsp;&nbsp; public int `step`(int ms);  |
|  &nbsp;&nbsp; public `Accelerometer` `getAccelerometer`(String name);  |
|  &nbsp;&nbsp; public `Brake` `getBrake`(String name);  |
|  &nbsp;&nbsp; public `Camera` `getCamera`(String name);  |
|  &nbsp;&nbsp; public `Compass` `getCompass`(String name);  |
|  &nbsp;&nbsp; public `Connector` `getConnector`(String name);  |
|  &nbsp;&nbsp; public `Display` `getDisplay`(String name);  |
|  &nbsp;&nbsp; public `DistanceSensor` `getDistanceSensor`(String name);  |
|  &nbsp;&nbsp; public `Emitter` `getEmitter`(String name);  |
|  &nbsp;&nbsp; public `GPS` `getGPS`(String name);  |
|  &nbsp;&nbsp; public `Gyro` `getGyro`(String name);  |
|  &nbsp;&nbsp; public `InertialUnit` `getInertialUnit`(String name);  |
|  &nbsp;&nbsp; public `LED` `getLED`(String name);  |
|  &nbsp;&nbsp; public `LightSensor` `getLightSensor`(String name);  |
|  &nbsp;&nbsp; public `Motor` `getMotor`(String name);  |
|  &nbsp;&nbsp; public `Pen` `getPen`(String name);  |
|  &nbsp;&nbsp; public `PositionSensor` `getPositionSensor`(String name);  |
|  &nbsp;&nbsp; public `Receiver` `getReceiver`(String name);  |
|  &nbsp;&nbsp; public `Servo` `getServo`(String name);  |
|  &nbsp;&nbsp; public `TouchSensor` `getTouchSensor`(String name);  |
|  &nbsp;&nbsp; public int `getNumberOfDevices`();  |
|  &nbsp;&nbsp; public `Device` `getDeviceByIndex`(int index);  |
|  &nbsp;&nbsp; public void `batterySensorEnable`(int ms);  |
|  &nbsp;&nbsp; public void `batterySensorDisable`();  |
|  &nbsp;&nbsp; public int `batterySensorGetSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `batterySensorGetValue`();  |
|  &nbsp;&nbsp; public double `getBasicTimeStep`();  |
|  &nbsp;&nbsp; public int `getMode`();  |
|  &nbsp;&nbsp; public String `getModel`();  |
|  &nbsp;&nbsp; public String `getData`();  |
|  &nbsp;&nbsp; public `setData`(String data);  |
|  &nbsp;&nbsp; public String `getName`();  |
|  &nbsp;&nbsp; public String `getControllerName`();  |
|  &nbsp;&nbsp; public String `getControllerArguments`();  |
|  &nbsp;&nbsp; public String `getProjectPath`();  |
|  &nbsp;&nbsp; public bool `getSynchronization`();  |
|  &nbsp;&nbsp; public double `getTime`();  |
|  &nbsp;&nbsp; public String `getWorldPath`();  |
|  &nbsp;&nbsp; public void `keyboardEnable`(int ms);  |
|  &nbsp;&nbsp; public void `keyboardDisable`();  |
|  &nbsp;&nbsp; public int `keyboardGetKey`();  |
|  &nbsp;&nbsp; public int `getType`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Servo;  |
|  public class `Servo` extends `Device` {  |
|  &nbsp;&nbsp; public final static int ROTATIONAL, LINEAR;  |
|  &nbsp;&nbsp; public void `setPosition`(double position);  |
|  &nbsp;&nbsp; public double `getTargetPosition`();  |
|  &nbsp;&nbsp; public void `setVelocity`(double vel);  |
|  &nbsp;&nbsp; public void `setAcceleration`(double force);  |
|  &nbsp;&nbsp; public void `setMotorForce`(double motor\_force);  |
|  &nbsp;&nbsp; public void `setControlP`(double p);  |
|  &nbsp;&nbsp; public double `getMinPosition`();  |
|  &nbsp;&nbsp; public double `getMaxPosition`();  |
|  &nbsp;&nbsp; public void `enablePosition`(int ms);  |
|  &nbsp;&nbsp; public void `disablePosition`();  |
|  &nbsp;&nbsp; public int `getPositionSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getPosition`();  |
|  &nbsp;&nbsp; public void `enableMotorForceFeedback`(int ms);  |
|  &nbsp;&nbsp; public void `disableMotorForceFeedback`();  |
|  &nbsp;&nbsp; public int `getMotorForceFeedbackSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getMotorForceFeedback`();  |
|  &nbsp;&nbsp; public void `setForce`(double force);  |
|  &nbsp;&nbsp; public int `getType`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.Supervisor;  |
|  public class `Supervisor` extends `Robot` {  |
|  &nbsp;&nbsp; public final static int MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR  |
|  &nbsp;&nbsp; public `Supervisor`();  |
|  &nbsp;&nbsp; protected void `finalize`();  |
|  &nbsp;&nbsp; public void `exportImage`(String file, int quality);  |
|  &nbsp;&nbsp; public `Node` `getRoot`();  |
|  &nbsp;&nbsp; public `Node` `getSelf`();  |
|  &nbsp;&nbsp; public `Node` `getFromDef`(String name);  |
|  &nbsp;&nbsp; public `Node` `getFromId`(int id);  |
|  &nbsp;&nbsp; public void `setLabel`(int id, String label, double xpos, double ypos,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency);  |
|  &nbsp;&nbsp; public void `simulationQuit`(int status);  |
|  &nbsp;&nbsp; public void `simulationRevert`();  |
|  &nbsp;&nbsp; public void `simulationResetPhysics`();  |
|  &nbsp;&nbsp; public void `loadWorld`(String file);  |
|  &nbsp;&nbsp; public void `saveWorld`();  |
|  &nbsp;&nbsp; public void `saveWorld`(String file);  |
|  &nbsp;&nbsp; public void `movieStartRecording`(String file, int width, int height, int codec, int quality,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; int acceleration, boolean caption);  |
|  &nbsp;&nbsp; public void `movieStopRecording`();  |
|  &nbsp;&nbsp; public int `movieGetStatus`();  |
|  &nbsp;&nbsp; public bool `animationStartRecording`(String file);  |
|  &nbsp;&nbsp; public bool `animationStopRecording`();  |
| }  |

| |
| --- |
| import com.cyberbotics.webots.controller.TouchSensor;  |
|  public class `TouchSensor` extends `Device` {  |
|  &nbsp;&nbsp; public final static int BUMPER, FORCE, FORCE3D;  |
|  &nbsp;&nbsp; public void `enable`(int ms);  |
|  &nbsp;&nbsp; public void `disable`();  |
|  &nbsp;&nbsp; public int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; public double `getValue`();  |
|  &nbsp;&nbsp; public double[] `getValues`();  |
|  &nbsp;&nbsp; public int `getType`();  |
| }  |

