## Java API

The following tables describe the Java classes and their methods.

```| import com.cyberbotics.webots.controller.Accelerometer; |
| public class `Accelerometer` extends `Device` { |
| public void `enable`(int ms); |
| public void `disable`(); |
| int `getSamplingPeriod`(); |
| public double[] `getValues`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Brake; |
| public class `Brake` extends `Device` { |
| public void `setDampingConstant`(double dampingConstant); |
| public int `getType`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Camera; |
| public class `Camera` extends `Device` { |
| public final static int COLOR, RANGE\_FINDER, BOTH; |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double `getFov`(); |
| public double `getMinFov`(); |
| public double `getMaxFov`(); |
| public void `setFov`(double fov); |
| public double `getFocalLength`(); |
| public double `getFocalDistance`(); |
| public double `getMaxFocalDistance`(); |
| public double `getMinFocalDistance`(); |
| public void `setFocalDistance`(double focalDistance); |
| public int `getWidth`(); |
| public int `getHeight`(); |
| public double `getNear`(); |
| public double `getMaxRange`(); |
| public int `getType`(); |
| public int[] `getImage`(); |
| public static int `imageGetRed`(int[] image, int width, int x, int y); |
| public static int `imageGetGreen`(int[] image, int width, int x, int y); |
| public static int `imageGetBlue`(int[] image, int width, int x, int y); |
| public static int `imageGetGrey`(int[] image, int width, int x, int y); |
| public static int `pixelGetRed`(int pixel); |
| public static int `pixelGetGreen`(int pixel); |
| public static int `pixelGetBlue`(int pixel); |
| public static int `pixelGetGrey`(int pixel); |
| public float[] `getRangeImage`(); |
| public static float `rangeImageGetDepth`(float[] image, |
| int width, int x, int y); |
| public int `saveImage`(String filename, int quality); |
| } |
```

```| import com.cyberbotics.webots.controller.Compass; |
| public class `Compass` extends `Device` { |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double[] `getValues`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Connector; |
| public class `Connector` extends `Device` { |
| public void `enablePresence`(int ms); |
| public void `disablePresence`(); |
| public int `getPresence`(); |
| public void `lock`(); |
| public void `unlock`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Device; |
| public class `Device` { |
| public String `getModel`(); |
| public String `getName`(); |
| public int `getNodeType`(); |
| } |
```

```| import com.cyberbotics.webots.controller.DifferentialWheels; |
| public class `DifferentialWheels` extends `Robot` { |
| public `DifferentialWheels`(); |
| protected void `finalize`(); |
| public void `setSpeed`(double left, double right); |
| public double `getLeftSpeed`(); |
| public double `getRightSpeed`(); |
| public void `enableEncoders`(int ms); |
| public void `disableEncoders`(); |
| public int `getEncodersSamplingPeriod`(); |
| public double `getLeftEncoder`(); |
| public double `getRightEncoder`(); |
| public void `setEncoders`(double left, double right); |
| public double `getMaxSpeed`(); |
| public double `getSpeedUnit`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Display; |
| public class `Display` extends `Device` { |
| public final static int RGB, RGBA, ARGB, BGRA; |
| public int `getWidth`(); |
| public int `getHeight`(); |
| public void `setColor`(int color); |
| public void `setAlpha`(double alpha); |
| public void `setOpacity`(double opacity); |
| public void `drawPixel`(int x1, int y1); |
| public void `drawLine`(int x1, int y1, int x2, int y2); |
| public void `drawRectangle`(int x, int y, int width, int height); |
| public void `drawOval`(int cx, int cy, int a, int b); |
| public void `drawPolygon`(int[] x, int[] y); |
| public void `drawText`(String txt, int x, int y); |
| public void `fillRectangle`(int x, int y, int width, int height); |
| public void `fillOval`(int cx, int cy, int a, int b); |
| public void `fillPolygon`(int[] x, int[] y); |
| public `ImageRef` `imageCopy`(int x, int y, int width, int height); |
| public void `imagePaste`(`ImageRef` ir, int x, int y); |
| public `ImageRef` `imageLoad`(String filename); |
| public `ImageRef` `imageNew`(int width, int height, int[] data, int format); |
| public void `imageSave`(`ImageRef` ir, String filename); |
| public void `imageDelete`(`ImageRef` ir); |
| } |
```

```| import com.cyberbotics.webots.controller.DistanceSensor; |
| public class `DistanceSensor` extends `Device` { |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double `getValue`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Emitter; |
| public class `Emitter` extends `Device` { |
| public final static int CHANNEL\_BROADCAST; |
| public int `send`(byte[] data); |
| public int `getChannel`(); |
| public void `setChannel`(int channel); |
| public double `getRange`(); |
| public void `setRange`(double range); |
| public int `getBufferSize`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Field; |
| public class Field { |
| public final static int SF\_BOOL, SF\_INT32, SF\_FLOAT, |
| SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, |
| SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, |
| MF\_COLOR, MF\_STRING, MF\_NODE; |
| public int `getType`(); |
| public String `getTypeName`(); |
| public int `getCount`(); |
| public bool `getSFBool`(); |
| public int `getSFInt32`(); |
| public double `getSFFloat`(); |
| public double[] `getSFVec2f`(); |
| public double[] `getSFVec3f`(); |
| public double[] `getSFRotation`(); |
| public double[] `getSFColor`(); |
| public String `getSFString`(); |
| public `Node` `getSFNode`(); |
| public bool `getMFBool`(int index); |
| public int `getMFInt32`(int index); |
| public double `getMFFloat`(int index); |
| public double[] `getMFVec2f`(int index); |
| public double[] `getMFVec3f`(int index); |
| public double[] `getMFColor`(int index); |
| public double[] `getMFRotation`(int index); |
| public String `getMFString`(int index); |
| public `Node` `getMFNode`(int index); |
| public void `setSFBool`(bool value); |
| public void `setSFInt32`(int value); |
| public void `setSFFloat`(double value); |
| public void `setSFVec2f`(double values[2]); |
| public void `setSFVec3f`(double values[3]); |
| public void `setSFRotation`(double values[4]); |
| public void `setSFColor`(double values[3]); |
| public void `setSFString`(String value); |
| public void `setMFBool`(int index, bool value); |
| public void `setMFInt32`(int index, int value); |
| public void `setMFFloat`(int index, double value); |
| public void `setMFVec2f`(int index, double values[2]); |
| public void `setMFVec3f`(int index, double values[3]); |
| public void `setMFRotation`(int index, double values[4]); |
| public void `setMFColor`(int index, double values[3]); |
| public void `setMFString`(int index, String value); |
| public void `importMFNode`(int position, String filename); |
| public void `importMFNodeFromString`(int position, String nodeString); |
| public void `removeMFNode`(int position); |
| } |
```

```| import com.cyberbotics.webots.controller.GPS; |
| public class `GPS` extends `Device` { |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double[] `getValues`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Gyro; |
| public class `Gyro` extends `Device` { |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double[] `getValues`(); |
| } |
```

```| import com.cyberbotics.webots.controller.ImageRef; |
| public class ImageRef { |
| } |
```

```| import com.cyberbotics.webots.controller.InertialUnit; |
| public class `InertialUnit` extends `Device` { |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double[] `getRollPitchYaw`(); |
| } |
```
```| import com.cyberbotics.webots.controller.LED; |
| public class `LED` extends `Device` { |
| public void `set`(int state); |
| public int `get`(); |
| } |
```

```| import com.cyberbotics.webots.controller.LightSensor; |
| public class `LightSensor` extends `Device` { |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double `getValue`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Motion; |
| public class `Motion` { |
| public `Motion`(String fileName); |
| protected void `finalize`(); |
| public bool `isValid`(); |
| public void `play`(); |
| public void `stop`(); |
| public void `setLoop`(bool loop); |
| public void `setReverse`(bool reverse); |
| public bool `isOver`(); |
| public int `getDuration`(); |
| public int `getTime`(); |
| public void `setTime`(int time); |
| } |
```

```| import com.cyberbotics.webots.controller.Motor; |
| public class `Motor` extends `Device` { |
| public final static int ROTATIONAL, LINEAR; |
| public void `setPosition`(double position); |
| public void `setVelocity`(double vel); |
| public void `setAcceleration`(double force); |
| public void `setAvailableForce`(double motor\_force); |
| public void `setAvailableTorque`(double motor\_torque); |
| public void `setControlPID`(double p, double i, double d); |
| public double `getTargetPosition`(); |
| public double `getMinPosition`(); |
| public double `getMaxPosition`(); |
| public double `getVelocity`(); |
| public double `getMaxVelocity`(); |
| public double `getAcceleration`(); |
| public double `getAvailableForce`(); |
| public double `getMaxForce`(); |
| public double `getAvailableTorque`(); |
| public double `getMaxTorque`(); |
| public void `enableForceFeedback`(int ms); |
| public void `disableForceFeedback`(); |
| public int `getForceFeedbackSamplingPeriod`(); |
| public double `getForceFeedback`(); |
| public void `setForce`(double force); |
| public void `enableTorqueFeedback`(int ms); |
| public void `disableTorqueFeedback`(); |
| public int `getTorqueFeedbackSamplingPeriod`(); |
| public double `getTorqueFeedback`(); |
| public void `setTorque`(double torque); |
| public int `getType`(); |
| } |
```
```| import com.cyberbotics.webots.controller.Node; |
| public class Node { |
| public final static int NO\_NODE, APPEARANCE, BACKGROUND, |
| BOX, COLOR, CONE, COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT, |
| ELEVATION\_GRID, EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE, |
| INDEXED\_FACE\_SET, INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT, |
| SHAPE, SPHERE, SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE, |
| TEXTURE\_TRANSFORM, TRANSFORM, VIEWPOINT, WORLD\_INFO, |
| CAPSULE, PLANE, ROBOT, SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID, |
| PHYSICS, CAMER\_ZOOM, CHARGER, DAMPING, |
| CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE, CAMERA, COMPASS, |
| CONNECTOR, DISPLAY, DISTANCE\_SENSOR, EMITTER, GPS, GYRO, LED, |
| LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN, POSITION\_SENSOR, RADIO, |
| RECEIVER, SERVO, SPEAKER, TOUCH\_SENSOR; |
| public void `remove`(); |
| public int `getId`(); |
| public int `getType`(); |
| public String `getTypeName`(); |
| public String `getBaseTypeName`(); |
| public `Field` `getField`(String fieldName); |
| public Node `getParentNode`(); |
| public double[] `getPosition`(); |
| public double[] `getOrientation`(); |
| public double[] `getCenterOfMass`(); |
| public double[] `getContactPoint`(int index); |
| public int `getNumberOfContactPoints`(); |
| public bool `getStaticBalance`(); |
| public double[] `getVelocity`(); |
| public void `setVelocity`(double velocity[6]); |
| public void `resetPhysics`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Pen; |
| public class `Pen` extends `Device` { |
| public void `write`(bool write); |
| public void `setInkColor`(int color, double density); |
| } |
```

```| import com.cyberbotics.webots.controller.PositionSensor; |
| public class `PositionSensor` extends `Device` { |
| public final static int ANGULAR, LINEAR; |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double `getValue`(); |
| public int `getType`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Receiver; |
| public class `Receiver` extends `Device` { |
| public final static int CHANNEL\_BROADCAST; |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public int `getQueueLength`(); |
| public void `nextPacket`(); |
| public byte[] `getData`(); |
| public int `getDataSize`(); |
| public double `getSignalStrength`(); |
| public double[] `getEmitterDirection`(); |
| public void `setChannel`(int channel); |
| public int `getChannel`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Robot; |
| public class `Robot` { |
| public final static int MODE\_SIMULATION, |
| MODE\_CROSS\_COMPILATION, MODE\_REMOTE\_CONTROL; |
| public final static int KEYBOARD\_END, KEYBOARD\_HOME, |
| KEYBOARD\_LEFT, KEYBOARD\_UP, KEYBOARD\_RIGHT, |
| KEYBOARD\_DOWN, KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN, |
| KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT, |
| KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT, |
| KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END, |
| KEYBOARD\_KEY, KEYBOARD\_SHIFT, |
| KEYBOARD\_CONTROL, KEYBOARD\_ALT; |
| public `Robot`(); |
| protected void `finalize`(); |
| public int `step`(int ms); |
| public `Accelerometer` `getAccelerometer`(String name); |
| public `Brake` `getBrake`(String name); |
| public `Camera` `getCamera`(String name); |
| public `Compass` `getCompass`(String name); |
| public `Connector` `getConnector`(String name); |
| public `Display` `getDisplay`(String name); |
| public `DistanceSensor` `getDistanceSensor`(String name); |
| public `Emitter` `getEmitter`(String name); |
| public `GPS` `getGPS`(String name); |
| public `Gyro` `getGyro`(String name); |
| public `InertialUnit` `getInertialUnit`(String name); |
| public `LED` `getLED`(String name); |
| public `LightSensor` `getLightSensor`(String name); |
| public `Motor` `getMotor`(String name); |
| public `Pen` `getPen`(String name); |
| public `PositionSensor` `getPositionSensor`(String name); |
| public `Receiver` `getReceiver`(String name); |
| public `Servo` `getServo`(String name); |
| public `TouchSensor` `getTouchSensor`(String name); |
| public int `getNumberOfDevices`(); |
| public `Device` `getDeviceByIndex`(int index); |
| public void `batterySensorEnable`(int ms); |
| public void `batterySensorDisable`(); |
| public int `batterySensorGetSamplingPeriod`(); |
| public double `batterySensorGetValue`(); |
| public double `getBasicTimeStep`(); |
| public int `getMode`(); |
| public String `getModel`(); |
| public String `getData`(); |
| public `setData`(String data); |
| public String `getName`(); |
| public String `getControllerName`(); |
| public String `getControllerArguments`(); |
| public String `getProjectPath`(); |
| public bool `getSynchronization`(); |
| public double `getTime`(); |
| public String `getWorldPath`(); |
| public void `keyboardEnable`(int ms); |
| public void `keyboardDisable`(); |
| public int `keyboardGetKey`(); |
| public int `getType`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Servo; |
| public class `Servo` extends `Device` { |
| public final static int ROTATIONAL, LINEAR; |
| public void `setPosition`(double position); |
| public double `getTargetPosition`(); |
| public void `setVelocity`(double vel); |
| public void `setAcceleration`(double force); |
| public void `setMotorForce`(double motor\_force); |
| public void `setControlP`(double p); |
| public double `getMinPosition`(); |
| public double `getMaxPosition`(); |
| public void `enablePosition`(int ms); |
| public void `disablePosition`(); |
| public int `getPositionSamplingPeriod`(); |
| public double `getPosition`(); |
| public void `enableMotorForceFeedback`(int ms); |
| public void `disableMotorForceFeedback`(); |
| public int `getMotorForceFeedbackSamplingPeriod`(); |
| public double `getMotorForceFeedback`(); |
| public void `setForce`(double force); |
| public int `getType`(); |
| } |
```

```| import com.cyberbotics.webots.controller.Supervisor; |
| public class `Supervisor` extends `Robot` { |
| public final static int MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING,
MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR |
| public `Supervisor`(); |
| protected void `finalize`(); |
| public void `exportImage`(String file, int quality); |
| public `Node` `getRoot`(); |
| public `Node` `getSelf`(); |
| public `Node` `getFromDef`(String name); |
| public `Node` `getFromId`(int id); |
| public void `setLabel`(int id, String label, double xpos, double ypos, |
| double size, int color, double transparency); |
| public void `simulationQuit`(int status); |
| public void `simulationRevert`(); |
| public void `simulationResetPhysics`(); |
| public void `loadWorld`(String file); |
| public void `saveWorld`(); |
| public void `saveWorld`(String file); |
| public void `movieStartRecording`(String file, int width, int height, int codec,
int quality, |
| int acceleration, boolean caption); |
| public void `movieStopRecording`(); |
| public int `movieGetStatus`(); |
| public bool `animationStartRecording`(String file); |
| public bool `animationStopRecording`(); |
| } |
```

```| import com.cyberbotics.webots.controller.TouchSensor; |
| public class `TouchSensor` extends `Device` { |
| public final static int BUMPER, FORCE, FORCE3D; |
| public void `enable`(int ms); |
| public void `disable`(); |
| public int `getSamplingPeriod`(); |
| public double `getValue`(); |
| public double[] `getValues`(); |
| public int `getType`(); |
| } |
```

