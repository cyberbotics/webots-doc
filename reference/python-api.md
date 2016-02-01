## Python API

The following tables describe the Python classes and their methods.

```| from controller import Accelerometer |
| class `Accelerometer` (`Device`) : |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValues`(self) |
```

```| from controller import Brake |
| class `Brake` (`Device`) : |
| def `setDampingConstant`(self, dampingConstant) |
| def `getType`(self) |
```

```| from controller import Camera |
| class `Camera` (`Device`) : |
| COLOR, RANGE_FINDER, BOTH |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getFov`(self) |
| def `getMinFov`(self) |
| def `getMaxFov`(self) |
| def `setFov`(self, fov) |
| def `getFocalLength`(self) |
| def `getFocalDistance`(self) |
| def `getMaxFocalDistance`(self) |
| def `getMinFocalDistance`(self) |
| def `setFocalDistance`(self, focalDistance) |
| def `getWidth`(self) |
| def `getHeight`(self) |
| def `getNear`(self) |
| def `getMaxRange`(self) |
| def `getType`(self) |
| def `getImage`(self) |
| def `getImageArray`(self) |
| def `imageGetRed`(image, width, x, y) |
| imageGetRed = staticmethod(imageGetRed) |
| def `imageGetGreen`(image, width, x, y) |
| imageGetGreen = staticmethod(imageGetGreen) |
| def `imageGetBlue`(image, width, x, y) |
| imageGetBlue = staticmethod(imageGetBlue) |
| def `imageGetGrey`(image, width, x, y) |
| imageGetGrey = staticmethod(imageGetGrey) |
| def `getRangeImage`(self) |
| def `getRangeImageArray`(self) |
| def `rangeImageGetDepth`(image, width, x, y) |
| rangeImageGetDepth = staticmethod(rangeImageGetDepth) |
| def `saveImage`(self, filename, quality) |
```

```| from controller import Compass |
| class `Compass` (`Device`) : |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValues`(self) |
```

```| from controller import Connector |
| class `Connector` (`Device`) : |
| def `enablePresence`(self, ms) |
| def `disablePresence`(self) |
| def `getPresence`(self) |
| def `lock`(self) |
| def `unlock`(self) |
```

```| from controller import `Device` |
| class Device : |
| def `getModel`(self) |
| def `getName`(self) |
| def `getNodeType`(self) |
```

```| from controller import DifferentialWheels |
| class `DifferentialWheels` (`Robot`) : |
| def `__init__`(self) |
| def `__del__`(self) |
| def `setSpeed`(self, left, right) |
| def `getLeftSpeed`(self) |
| def `getRightSpeed`(self) |
| def `enableEncoders`(self, ms) |
| def `disableEncoders`(self) |
| def `getEncodersSamplingPeriod`(self) |
| def `getLeftEncoder`(self) |
| def `getRightEncoder`(self) |
| def `setEncoders`(self, left, right) |
| def `getMaxSpeed`(self) |
| def `getSpeedUnit`(self) |
```

```| from controller import Display |
| class `Display` (`Device`) : |
| RGB, RGBA, ARGB, BGRA |
| def `getWidth`(self) |
| def `getHeight`(self) |
| def `setColor`(self, color) |
| def `setAlpha`(self, alpha) |
| def `setOpacity`(self, opacity) |
| def `drawPixel`(self, x1, y1) |
| def `drawLine`(self, x1, y1, x2, y2) |
| def `drawRectangle`(self, x, y, width, height) |
| def `drawOval`(self, cx, cy, a, b) |
| def `drawPolygon`(self, x, y) |
| def `drawText`(self, txt, x, y) |
| def `fillRectangle`(self, x, y, width, height) |
| def `fillOval`(self, cx, cy, a, b) |
| def `fillPolygon`(self, x, y) |
| def `imageCopy`(self, x, y, width, height) |
| def `imagePaste`(self, ir, x, y) |
| def `imageLoad`(self, filename) |
| def `imageNew`(self, data, format) |
| def `imageSave`(self, ir, filename) |
| def `imageDelete`(self, ir) |
```

```| from controller import DistanceSensor |
| class `DistanceSensor` (`Device`) : |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValue`(self) |
```

```| from controller import Emitter |
| class `Emitter` (`Device`) : |
| CHANNEL_BROADCAST |
| def `send`(self, data) |
| def `getChannel`(self) |
| def `setChannel`(self, channel) |
| def `getRange`(self) |
| def `setRange`(self, range) |
| def `getBufferSize`(self) |
```

```| from controller import Field |
| class Field : |
| SF_BOOL, SF_INT32, SF_FLOAT, SF_VEC2F, SF_VEC3F, |
| SF_ROTATION, SF_COLOR, SF_STRING, SF_NODE, MF, |
| MF_INT32, MF_FLOAT, MF_VEC2F, MF_VEC3F, MF_COLOR, |
| MF_STRING, MF_NODE |
| def `getType`(self) |
| def `getTypeName`(self) |
| def `getCount`(self) |
| def `getSFBool`(self) |
| def `getSFInt32`(self) |
| def `getSFFloat`(self) |
| def `getSFVec2f`(self) |
| def `getSFVec3f`(self) |
| def `getSFRotation`(self) |
| def `getSFColor`(self) |
| def `getSFString`(self) |
| def `getSFNode`(self) |
| def `getMFBool`(self, index) |
| def `getMFInt32`(self, index) |
| def `getMFFloat`(self, index) |
| def `getMFVec2f`(self, index) |
| def `getMFVec3f`(self, index) |
| def `getMFRotation`(self, index) |
| def `getMFColor`(self, index) |
| def `getMFString`(self, index) |
| def `getMFNode`(self, index) |
| def `setSFBool`(self, value) |
| def `setSFInt32`(self, value) |
| def `setSFFloat`(self, value) |
| def `setSFVec2f`(self, values) |
| def `setSFVec3f`(self, values) |
| def `setSFRotation`(self, values) |
| def `setSFColor`(self, values) |
| def `setSFString`(self, value) |
| def `setMFBool`(self, index, value) |
| def `setMFInt32`(self, index, value) |
| def `setMFFloat`(self, index, value) |
| def `setMFVec2f`(self, index, values) |
| def `setMFVec3f`(self, index, values) |
| def `setMFRotation`(self, index, values) |
| def `setMFColor`(self, index, values) |
| def `setMFString`(self, index, value) |
| def `importMFNode`(self, position, filename) |
| def `importMFNodeFromString`(self, position, nodeString) |
| def `removeMFNode`(self, position) |
```

```| from controller import GPS |
| class `GPS` (`Device`) : |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValues`(self) |
```

```| from controller import Gyro |
| class `Gyro` (`Device`) : |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValues`(self) |
```

```| from controller import ImageRef |
| class ImageRef : |
```

```| from controller import InertialUnit |
| class `InertialUnit` (`Device`) : |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getRollPitchYaw`(self) |
```
```| from controller import LED |
| class `LED` (`Device`) : |
| def `set`(self, state) |
| def `get`(self) |
```

```| from controller import LightSensor |
| class `LightSensor` (`Device`) : |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValue`(self) |
```

```| from controller import Motion |
| class `Motion` : |
| def `__init__`(self, fileName) |
| def `__del__`(self) |
| def `isValid`(self) |
| def `play`(self) |
| def `stop`(self) |
| def `setLoop`(self, loop) |
| def `setReverse`(self, reverse) |
| def `isOver`(self) |
| def `getDuration`(self) |
| def `getTime`(self) |
| def `setTime`(self, time) |
```

```| from controller import Motor |
| class `Motor` (`Device`) : |
| ROTATIONAL, LINEAR |
| def `setPosition`(self, position) |
| def `setVelocity`(self, vel) |
| def `setAcceleration`(self, force) |
| def `setAvailableForce`(self, motor_force) |
| def `setAvailableTorque`(self, motor_torque) |
| def `setControlPID`(self, p, i, d) |
| def `getTargetPosition`(self) |
| def `getMinPosition`(self) |
| def `getMaxPosition`(self) |
| def `getVelocity`(self) |
| def `getMaxVelocity`(self) |
| def `getAcceleration`(self) |
| def `getAvailableForce`(self) |
| def `getMaxForce`(self) |
| def `getAvailableTorque`(self) |
| double `getMaxTorque`(self) |
| def `enableForceFeedback`(self, ms) |
| def `disableForceFeedback`(self) |
| def `getForceFeedbackSamplingPeriod`(self) |
| def `getForceFeedback`(self) |
| def `setForce`(self, torque) |
| def `enableTorqueFeedback`(self, ms) |
| def `disableTorqueFeedback`(self) |
| def `getTorqueFeedbackSamplingPeriod`(self) |
| def `getTorqueFeedback`(self) |
| def `setTorque`(self, torque) |
| def `getType`(self) |
```

```| from controller import Node |
| class Node : |
| NO_NODE, APPEARANCE, BACKGROUND, BOX, COLOR, CONE, |
| COORDINATE, CYLINDER, DIRECTIONAL_LIGHT, ELEVATION_GRID, |
| EXTRUSION, FOG, GROUP, IMAGE_TEXTURE, INDEXED_FACE_SET, |
| INDEXED_LINE_SET, MATERIAL, POINT_LIGHT, SHAPE, SPHERE, |
| SPOT_LIGHT, SWITCH, TEXTURE_COORDINATE, TEXTURE_TRANSFORM, |
| TRANSFORM, VIEWPOINT, WORLD_INFO, CAPSULE, PLANE, ROBOT, |
| SUPERVISOR, DIFFERENTIAL_WHEELS, SOLID, PHYSICS, CAMERA_ZOOM, |
| CHARGER, DAMPING, CONTACT_PROPERTIES, ACCELEROMETER, BRAKE, |
| CAMERA, COMPASS, CONNECTOR, DISPLAY, DISTANCE_SENSOR, |
| EMITTER, GPS, GYRO, LED, LIGHT_SENSOR, MICROPHONE, MOTOR, PEN, |
| POSITION_SENSOR, RADIO, RECEIVER, SERVO, SPEAKER, |
| TOUCH_SENSOR |
| def `remove`(self) |
| def `getType`(self) |
| def `getId`(self) |
| def `getTypeName`(self) |
| def `getBaseTypeName`(self) |
| def `getField`(self, fieldName) |
| def `getParentNode`(self) |
| def `getPosition`(self) |
| def `getOrientation`(self) |
| def `getCenterOfMass`(self) |
| def `getContactPoint`(self, index) |
| def `getNumberOfContactPoints`(self) |
| def `getStaticBalance`(self) |
| def `getVelocity`(self) |
| def `setVelocity`(self, velocity) |
| def `resetPhysics`(self) |
```

```| from controller import Pen |
| class `Pen` (`Device`) : |
| def `write`(self, write) |
| def `setInkColor`(self, color, density) |
```

```| from controller import PositionSensor |
| class `PositionSensor` (`Device`) : |
| ANGULAR, LINEAR |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValue`(self) |
| def `getType`(self) |
```

```| from controller import Receiver |
| class `Receiver` (`Device`) : |
| CHANNEL_BROADCAST |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getQueueLength`(self) |
| def `nextPacket`(self) |
| def `getData`(self) |
| def `getDataSize`(self) |
| def `getSignalStrength`(self) |
| def `getEmitterDirection`(self) |
| def `setChannel`(self, channel) |
| def `getChannel`(self) |
```

```| from controller import Robot |
| class `Robot` : |
| MODE_SIMULATION, MODE_CROSS_COMPILATION, |
| MODE_REMOTE_CONTROL |
| KEYBOARD_END, KEYBOARD_HOME, KEYBOARD_LEFT, KEYBOARD_UP, |
| KEYBOARD_RIGHT, KEYBOARD_DOWN, KEYBOARD_PAGEUP, |
| KEYBOARD_PAGEDOWN, KEYBOARD_NUMPAD_HOME, |
| KEYBOARD_NUMPAD_LEFT, KEYBOARD_NUMPAD_UP, |
| KEYBOARD_NUMPAD_RIGHT, KEYBOARD_NUMPAD_DOWN, |
| KEYBOARD_NUMPAD_END, KEYBOARD_KEY, KEYBOARD_SHIFT, |
| KEYBOARD_CONTROL, KEYBOARD_ALT |
| def `__init__`(self) |
| def `__del__`(self) |
| def `step`(self, ms) |
| def `getAccelerometer`(self, name) |
| def `getBrake`(self, name) |
| def `getCamera`(self, name) |
| def `getCompass`(self, name) |
| def `getConnector`(self, name) |
| def `getDisplay`(self, name) |
| def `getDistanceSensor`(self, name) |
| def `getEmitter`(self, name) |
| def `getGPS`(self, name) |
| def `getGyro`(self, name) |
| def `getInertialUnit`(self, name) |
| def `getLED`(self, name) |
| def `getLightSensor`(self, name) |
| def `getMotor`(self, name) |
| def `getPen`(self, name) |
| def `getPositionSensor`(self, name) |
| def `getReceiver`(self, name) |
| def `getServo`(self, name) |
| def `getTouchSensor`(self, name) |
| def `getNumberOfDevices`(self) |
| def `getDeviceByIndex`(self, index) |
| def `batterySensorEnable`(self, ms) |
| def `batterySensorDisable`(self) |
| def `batterySensorGetSamplingPeriod`(self) |
| def `batterySensorGetValue`(self) |
| def `getBasicTimeStep`(self) |
| def `getMode`(self) |
| def `getModel`(self) |
| def `getData`(self) |
| def `setData`(self, data) |
| def `getName`(self) |
| def `getControllerName`(self) |
| def `getControllerArguments`(self) |
| def `getProjectPath`(self) |
| def `getSynchronization`(self) |
| def `getTime`(self) |
| def `getWorldPath`(self) |
| def `keyboardEnable`(self, ms) |
| def `keyboardDisable`(self) |
| def `keyboardGetKey`(self) |
| def `getType`(self) |
```

```| from controller import Servo |
| class `Servo` (`Device`) : |
| ROTATIONAL, LINEAR |
| def `setPosition`(self, position) |
| def `getTargetPosition`(self) |
| def `setVelocity`(self, vel) |
| def `setAcceleration`(self, force) |
| def `setMotorForce`(self, motor_force) |
| def `setControlP`(self, p) |
| def `getMinPosition`(self) |
| def `getMaxPosition`(self) |
| def `enablePosition`(self, ms) |
| def `disablePosition`(self) |
| def `getPositionSamplingPeriod`(self) |
| def `getPosition`(self) |
| def `enableMotorForceFeedback`(self, ms) |
| def `disableMotorForceFeedback`(self) |
| def `getMotorForceFeedbackSamplingPeriod`(self) |
| def `getMotorForceFeedback`(self) |
| def `setForce`(self, force) |
| def `getType`(self) |
```

```| from controller import Supervisor |
| class `Supervisor` (`Robot`) : |
| MOVIE_READY, MOVIE_RECORDING, MOVIE_SAVING, MOVIE_WRITE_ERROR, MOVIE_ENCODING_ERROR, MOVIE_SIMULATION_ERROR |
| def `__init__`(self) |
| def `__del__`(self) |
| def `exportImage`(self, file, quality) |
| def `getRoot`(self) |
| def `getSelf`(self) |
| def `getFromDef`(self, name) |
| def `getFromId`(self, id) |
| def `setLabel`(self, id, label, xpos, ypos, size, color, transparency) |
| def `simulationQuit`(self, status) |
| def `simulationRevert`(self) |
| def `simulationResetPhysics`(self) |
| def `loadWorld`(self, file) |
| def `saveWorld`(self) |
| def `saveWorld`(self, file) |
| def `movieStartRecording`(self, file, width, height, codec, quality, acceleration, caption) |
| def `movieStopRecording`(self) |
| def `movieGetStatus`(self) |
| def `animationStartRecording`(self, file) |
| def `animationStopRecording`(self) |
```

```| from controller import TouchSensor |
| class `TouchSensor` (`Device`) : |
| BUMPER, FORCE, FORCE3D |
| def `enable`(self, ms) |
| def `disable`(self) |
| def `getSamplingPeriod`(self) |
| def `getValue`(self) |
| def `getValues`(self) |
| def `getType`(self) |
```

