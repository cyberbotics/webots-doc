## Python API

The following tables describe the Python classes and their methods.

| |
| --- |
| from controller import Accelerometer |
| class [Accelerometer](accelerometer.md#accelerometer) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enable](accelerometer.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](accelerometer.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](accelerometer.md#description)(self) |
| &nbsp;&nbsp; def [getValues](accelerometer.md#description)(self) |

| |
| --- |
| from controller import Brake |
| class [Brake](brake.md#brake) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [setDampingConstant](brake.md#description)(self, dampingConstant) |
| &nbsp;&nbsp; def [getType](brake.md#description)(self) |

| |
| --- |
| from controller import Camera |
| class [Camera](camera.md#camera) ([Device](python-api.md)) : |
| &nbsp;&nbsp; COLOR, RANGE\_FINDER, BOTH |
| &nbsp;&nbsp; def [enable](camera.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](camera.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](camera.md#description)(self) |
| &nbsp;&nbsp; def [getFov](camera.md#description)(self) |
| &nbsp;&nbsp; def [getMinFov](camera.md#description)(self) |
| &nbsp;&nbsp; def [getMaxFov](camera.md#description)(self) |
| &nbsp;&nbsp; def [setFov](camera.md#description)(self, fov) |
| &nbsp;&nbsp; def [getFocalLength](camera.md#description)(self) |
| &nbsp;&nbsp; def [getFocalDistance](camera.md#description)(self) |
| &nbsp;&nbsp; def [getMaxFocalDistance](camera.md#description)(self) |
| &nbsp;&nbsp; def [getMinFocalDistance](camera.md#description)(self) |
| &nbsp;&nbsp; def [setFocalDistance](camera.md#description)(self, focalDistance) |
| &nbsp;&nbsp; def [getWidth](camera.md#description)(self) |
| &nbsp;&nbsp; def [getHeight](camera.md#description)(self) |
| &nbsp;&nbsp; def [getNear](camera.md#description)(self) |
| &nbsp;&nbsp; def [getMaxRange](camera.md#description)(self) |
| &nbsp;&nbsp; def [getType](camera.md#description)(self) |
| &nbsp;&nbsp; def [getImage](camera.md#description)(self) |
| &nbsp;&nbsp; def [getImageArray](camera.md#description)(self) |
| &nbsp;&nbsp; def [imageGetRed](camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetRed = staticmethod(imageGetRed) |
| &nbsp;&nbsp; def [imageGetGreen](camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetGreen = staticmethod(imageGetGreen) |
| &nbsp;&nbsp; def [imageGetBlue](camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetBlue = staticmethod(imageGetBlue) |
| &nbsp;&nbsp; def [imageGetGrey](camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetGrey = staticmethod(imageGetGrey) |
| &nbsp;&nbsp; def [getRangeImage](camera.md#description)(self) |
| &nbsp;&nbsp; def [getRangeImageArray](camera.md#description)(self) |
| &nbsp;&nbsp; def [rangeImageGetDepth](camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; rangeImageGetDepth = staticmethod(rangeImageGetDepth) |
| &nbsp;&nbsp; def [saveImage](camera.md#description)(self, filename, quality) |

| |
| --- |
| from controller import Compass |
| class [Compass](compass.md#compass) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enable](compass.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](compass.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](compass.md#description)(self) |
| &nbsp;&nbsp; def [getValues](compass.md#description)(self) |

| |
| --- |
| from controller import Connector |
| class [Connector](connector.md#connector) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enablePresence](connector.md#description)(self, ms) |
| &nbsp;&nbsp; def [disablePresence](connector.md#description)(self) |
| &nbsp;&nbsp; def [getPresence](connector.md#description)(self) |
| &nbsp;&nbsp; def [lock](connector.md#description)(self) |
| &nbsp;&nbsp; def [unlock](connector.md#description)(self) |

| |
| --- |
| from controller import [Device](device.md#device) |
| class Device : |
| &nbsp;&nbsp; def [getModel](device.md#description)(self) |
| &nbsp;&nbsp; def [getName](device.md#description)(self) |
| &nbsp;&nbsp; def [getNodeType](device.md#description)(self) |

| |
| --- |
| from controller import DifferentialWheels |
| class [DifferentialWheels](differentialwheels.md#differentialwheels) ([Robot](python-api.md)) : |
| &nbsp;&nbsp; def [\_\_init\_\_](robot.md#description)(self) |
| &nbsp;&nbsp; def [\_\_del\_\_](robot.md#description)(self) |
| &nbsp;&nbsp; def [setSpeed](differentialwheels.md#description)(self, left, right) |
| &nbsp;&nbsp; def [getLeftSpeed](differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getRightSpeed](differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [enableEncoders](differentialwheels.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableEncoders](differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getEncodersSamplingPeriod](differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getLeftEncoder](differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getRightEncoder](differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [setEncoders](differentialwheels.md#description)(self, left, right) |
| &nbsp;&nbsp; def [getMaxSpeed](differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getSpeedUnit](differentialwheels.md#description)(self) |

| |
| --- |
| from controller import Display |
| class [Display](display.md#display) ([Device](python-api.md)) : |
| &nbsp;&nbsp; RGB, RGBA, ARGB, BGRA |
| &nbsp;&nbsp; def [getWidth](display.md#description)(self) |
| &nbsp;&nbsp; def [getHeight](display.md#description)(self) |
| &nbsp;&nbsp; def [setColor](display.md#description)(self, color) |
| &nbsp;&nbsp; def [setAlpha](display.md#description)(self, alpha) |
| &nbsp;&nbsp; def [setOpacity](display.md#description)(self, opacity) |
| &nbsp;&nbsp; def [drawPixel](display.md#description)(self, x1, y1) |
| &nbsp;&nbsp; def [drawLine](display.md#description)(self, x1, y1, x2, y2) |
| &nbsp;&nbsp; def [drawRectangle](display.md#description)(self, x, y, width, height) |
| &nbsp;&nbsp; def [drawOval](display.md#description)(self, cx, cy, a, b) |
| &nbsp;&nbsp; def [drawPolygon](display.md#description)(self, x, y) |
| &nbsp;&nbsp; def [drawText](display.md#description)(self, txt, x, y) |
| &nbsp;&nbsp; def [fillRectangle](display.md#description)(self, x, y, width, height) |
| &nbsp;&nbsp; def [fillOval](display.md#description)(self, cx, cy, a, b) |
| &nbsp;&nbsp; def [fillPolygon](display.md#description)(self, x, y) |
| &nbsp;&nbsp; def [imageCopy](display.md#description)(self, x, y, width, height) |
| &nbsp;&nbsp; def [imagePaste](display.md#description)(self, ir, x, y) |
| &nbsp;&nbsp; def [imageLoad](display.md#description)(self, filename) |
| &nbsp;&nbsp; def [imageNew](display.md#description)(self, data, format) |
| &nbsp;&nbsp; def [imageSave](display.md#description)(self, ir, filename) |
| &nbsp;&nbsp; def [imageDelete](display.md#description)(self, ir) |

| |
| --- |
| from controller import DistanceSensor |
| class [DistanceSensor](distancesensor.md#distancesensor) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enable](distancesensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](distancesensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](distancesensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](distancesensor.md#description)(self) |

| |
| --- |
| from controller import Emitter |
| class [Emitter](emitter.md#emitter) ([Device](python-api.md)) : |
| &nbsp;&nbsp; CHANNEL\_BROADCAST |
| &nbsp;&nbsp; def [send](emitter.md#description)(self, data) |
| &nbsp;&nbsp; def [getChannel](emitter.md#description)(self) |
| &nbsp;&nbsp; def [setChannel](emitter.md#description)(self, channel) |
| &nbsp;&nbsp; def [getRange](emitter.md#description)(self) |
| &nbsp;&nbsp; def [setRange](emitter.md#description)(self, range) |
| &nbsp;&nbsp; def [getBufferSize](emitter.md#description)(self) |

| |
| --- |
| from controller import Field |
| class Field : |
| &nbsp;&nbsp; SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, |
| &nbsp;&nbsp; SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, |
| &nbsp;&nbsp; MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, |
| &nbsp;&nbsp; MF\_STRING, MF\_NODE |
| &nbsp;&nbsp; def [getType](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getTypeName](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getCount](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFBool](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFInt32](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFFloat](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFVec2f](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFVec3f](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFRotation](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFColor](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFString](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFNode](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getMFBool](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFInt32](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFFloat](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFVec2f](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFVec3f](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFRotation](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFColor](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFString](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFNode](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [setSFBool](supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setSFInt32](supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setSFFloat](supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setSFVec2f](supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFVec3f](supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFRotation](supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFColor](supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFString](supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setMFBool](supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [setMFInt32](supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [setMFFloat](supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [setMFVec2f](supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFVec3f](supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFRotation](supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFColor](supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFString](supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [importMFNode](supervisor.md#description)(self, position, filename) |
| &nbsp;&nbsp; def [importMFNodeFromString](supervisor.md#description)(self, position, nodeString) |
| &nbsp;&nbsp; def [removeMFNode](supervisor.md#description)(self, position) |

| |
| --- |
| from controller import GPS |
| class [GPS](gps.md#gps) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enable](gps.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](gps.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](gps.md#description)(self) |
| &nbsp;&nbsp; def [getValues](gps.md#description)(self) |

| |
| --- |
| from controller import Gyro |
| class [Gyro](gyro.md#gyro) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enable](gyro.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](gyro.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](gyro.md#description)(self) |
| &nbsp;&nbsp; def [getValues](gyro.md#description)(self) |

| |
| --- |
| from controller import ImageRef |
| class ImageRef : |

| |
| --- |
| from controller import InertialUnit |
| class [InertialUnit](inertialunit.md#inertialunit) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enable](inertialunit.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](inertialunit.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](inertialunit.md#description)(self) |
| &nbsp;&nbsp; def [getRollPitchYaw](inertialunit.md#description)(self) |

| |
| --- |
| from controller import LED |
| class [LED](led.md#led) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [set](led.md#description)(self, state) |
| &nbsp;&nbsp; def [get](led.md#description)(self) |

| |
| --- |
| from controller import LightSensor |
| class [LightSensor](lightsensor.md#lightsensor) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [enable](lightsensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](lightsensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](lightsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](lightsensor.md#description)(self) |

| |
| --- |
| from controller import Motion |
| class [Motion](motion.md#motion) : |
| &nbsp;&nbsp; def [\_\_init\_\_](motion.md#description)(self, fileName) |
| &nbsp;&nbsp; def [\_\_del\_\_](motion.md#description)(self) |
| &nbsp;&nbsp; def [isValid](motion.md#description)(self) |
| &nbsp;&nbsp; def [play](motion.md#description)(self) |
| &nbsp;&nbsp; def [stop](motion.md#description)(self) |
| &nbsp;&nbsp; def [setLoop](motion.md#description)(self, loop) |
| &nbsp;&nbsp; def [setReverse](motion.md#description)(self, reverse) |
| &nbsp;&nbsp; def [isOver](motion.md#description)(self) |
| &nbsp;&nbsp; def [getDuration](motion.md#description)(self) |
| &nbsp;&nbsp; def [getTime](motion.md#description)(self) |
| &nbsp;&nbsp; def [setTime](motion.md#description)(self, time) |

| |
| --- |
| from controller import Motor |
| class [Motor](motor.md#motor) ([Device](python-api.md)) : |
| &nbsp;&nbsp; ROTATIONAL, LINEAR |
| &nbsp;&nbsp; def [setPosition](motor.md#description)(self, position) |
| &nbsp;&nbsp; def [setVelocity](motor.md#description)(self, vel) |
| &nbsp;&nbsp; def [setAcceleration](motor.md#description)(self, force) |
| &nbsp;&nbsp; def [setAvailableForce](motor.md#description)(self, motor\_force) |
| &nbsp;&nbsp; def [setAvailableTorque](motor.md#description)(self, motor\_torque) |
| &nbsp;&nbsp; def [setControlPID](motor.md#description)(self, p, i, d) |
| &nbsp;&nbsp; def [getTargetPosition](motor.md#description)(self) |
| &nbsp;&nbsp; def [getMinPosition](motor.md#description)(self) |
| &nbsp;&nbsp; def [getMaxPosition](motor.md#description)(self) |
| &nbsp;&nbsp; def [getVelocity](motor.md#description)(self) |
| &nbsp;&nbsp; def [getMaxVelocity](motor.md#description)(self) |
| &nbsp;&nbsp; def [getAcceleration](motor.md#description)(self) |
| &nbsp;&nbsp; def [getAvailableForce](motor.md#description)(self) |
| &nbsp;&nbsp; def [getMaxForce](motor.md#description)(self) |
| &nbsp;&nbsp; def [getAvailableTorque](motor.md#description)(self) |
| &nbsp;&nbsp; double [getMaxTorque](motor.md#description)(self) |
| &nbsp;&nbsp; def [enableForceFeedback](motor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableForceFeedback](motor.md#description)(self) |
| &nbsp;&nbsp; def [getForceFeedbackSamplingPeriod](motor.md#description)(self) |
| &nbsp;&nbsp; def [getForceFeedback](motor.md#description)(self) |
| &nbsp;&nbsp; def [setForce](motor.md#description)(self, torque) |
| &nbsp;&nbsp; def [enableTorqueFeedback](motor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableTorqueFeedback](motor.md#description)(self) |
| &nbsp;&nbsp; def [getTorqueFeedbackSamplingPeriod](motor.md#description)(self) |
| &nbsp;&nbsp; def [getTorqueFeedback](motor.md#description)(self) |
| &nbsp;&nbsp; def [setTorque](motor.md#description)(self, torque) |
| &nbsp;&nbsp; def [getType](motor.md#description)(self) |

| |
| --- |
| from controller import Node |
| class Node : |
| &nbsp;&nbsp; NO\_NODE, APPEARANCE, BACKGROUND, BOX, COLOR, CONE, |
| &nbsp;&nbsp; COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT, ELEVATION\_GRID, |
| &nbsp;&nbsp; EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE, INDEXED\_FACE\_SET, |
| &nbsp;&nbsp; INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT, SHAPE, SPHERE, |
| &nbsp;&nbsp; SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, |
| &nbsp;&nbsp; TRANSFORM, VIEWPOINT, WORLD\_INFO, CAPSULE, PLANE, ROBOT, |
| &nbsp;&nbsp; SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID, PHYSICS, CAMERA\_ZOOM, |
| &nbsp;&nbsp; CHARGER, DAMPING, CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE, |
| &nbsp;&nbsp; CAMERA, COMPASS, CONNECTOR, DISPLAY, DISTANCE\_SENSOR, |
| &nbsp;&nbsp; EMITTER, GPS, GYRO, LED, LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN, |
| &nbsp;&nbsp; POSITION\_SENSOR, RADIO, RECEIVER, SERVO, SPEAKER, |
| &nbsp;&nbsp; TOUCH\_SENSOR |
| &nbsp;&nbsp; def [remove](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getType](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getId](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getTypeName](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getBaseTypeName](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getField](supervisor.md#description)(self, fieldName) |
| &nbsp;&nbsp; def [getParentNode](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getPosition](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getOrientation](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getCenterOfMass](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getContactPoint](supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getNumberOfContactPoints](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getStaticBalance](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getVelocity](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [setVelocity](supervisor.md#description)(self, velocity) |
| &nbsp;&nbsp; def [resetPhysics](supervisor.md#description)(self) |

| |
| --- |
| from controller import Pen |
| class [Pen](pen.md#pen) ([Device](python-api.md)) : |
| &nbsp;&nbsp; def [write](pen.md#description)(self, write) |
| &nbsp;&nbsp; def [setInkColor](pen.md#description)(self, color, density) |

| |
| --- |
| from controller import PositionSensor |
| class [PositionSensor](positionsensor.md#positionsensor) ([Device](python-api.md)) : |
| &nbsp;&nbsp; ANGULAR, LINEAR |
| &nbsp;&nbsp; def [enable](positionsensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](positionsensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](positionsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](positionsensor.md#description)(self) |
| &nbsp;&nbsp; def [getType](positionsensor.md#description)(self) |

| |
| --- |
| from controller import Receiver |
| class [Receiver](receiver.md#receiver) ([Device](python-api.md)) : |
| &nbsp;&nbsp; CHANNEL\_BROADCAST |
| &nbsp;&nbsp; def [enable](receiver.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](receiver.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](receiver.md#description)(self) |
| &nbsp;&nbsp; def [getQueueLength](receiver.md#description)(self) |
| &nbsp;&nbsp; def [nextPacket](receiver.md#description)(self) |
| &nbsp;&nbsp; def [getData](receiver.md#description)(self) |
| &nbsp;&nbsp; def [getDataSize](receiver.md#description)(self) |
| &nbsp;&nbsp; def [getSignalStrength](receiver.md#description)(self) |
| &nbsp;&nbsp; def [getEmitterDirection](receiver.md#description)(self) |
| &nbsp;&nbsp; def [setChannel](receiver.md#description)(self, channel) |
| &nbsp;&nbsp; def [getChannel](receiver.md#description)(self) |

| |
| --- |
| from controller import Robot |
| class [Robot](robot.md#robot) : |
| &nbsp;&nbsp; MODE\_SIMULATION, MODE\_CROSS\_COMPILATION, |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL |
| &nbsp;&nbsp; KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT, KEYBOARD\_UP, |
| &nbsp;&nbsp; KEYBOARD\_RIGHT, KEYBOARD\_DOWN, KEYBOARD\_PAGEUP, |
| &nbsp;&nbsp; KEYBOARD\_PAGEDOWN, KEYBOARD\_NUMPAD\_HOME, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_LEFT, KEYBOARD\_NUMPAD\_UP, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_RIGHT, KEYBOARD\_NUMPAD\_DOWN, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_END, KEYBOARD\_KEY, KEYBOARD\_SHIFT, |
| &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT |
| &nbsp;&nbsp; def [\_\_init\_\_](robot.md#description)(self) |
| &nbsp;&nbsp; def [\_\_del\_\_](robot.md#description)(self) |
| &nbsp;&nbsp; def [step](robot.md#description)(self, ms) |
| &nbsp;&nbsp; def [getAccelerometer](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getBrake](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getCamera](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getCompass](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getConnector](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getDisplay](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getDistanceSensor](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getEmitter](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getGPS](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getGyro](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getInertialUnit](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getLED](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getLightSensor](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getMotor](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getPen](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getPositionSensor](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getReceiver](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getServo](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getTouchSensor](robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getNumberOfDevices](robot.md#description)(self) |
| &nbsp;&nbsp; def [getDeviceByIndex](robot.md#description)(self, index) |
| &nbsp;&nbsp; def [batterySensorEnable](robot.md#description)(self, ms) |
| &nbsp;&nbsp; def [batterySensorDisable](robot.md#description)(self) |
| &nbsp;&nbsp; def [batterySensorGetSamplingPeriod](robot.md#description)(self) |
| &nbsp;&nbsp; def [batterySensorGetValue](robot.md#description)(self) |
| &nbsp;&nbsp; def [getBasicTimeStep](robot.md#description)(self) |
| &nbsp;&nbsp; def [getMode](robot.md#description)(self) |
| &nbsp;&nbsp; def [getModel](robot.md#description)(self) |
| &nbsp;&nbsp; def [getData](robot.md#description)(self) |
| &nbsp;&nbsp; def [setData](robot.md#description)(self, data) |
| &nbsp;&nbsp; def [getName](robot.md#description)(self) |
| &nbsp;&nbsp; def [getControllerName](robot.md#description)(self) |
| &nbsp;&nbsp; def [getControllerArguments](robot.md#description)(self) |
| &nbsp;&nbsp; def [getProjectPath](robot.md#description)(self) |
| &nbsp;&nbsp; def [getSynchronization](robot.md#description)(self) |
| &nbsp;&nbsp; def [getTime](robot.md#description)(self) |
| &nbsp;&nbsp; def [getWorldPath](robot.md#description)(self) |
| &nbsp;&nbsp; def [keyboardEnable](robot.md#description)(self, ms) |
| &nbsp;&nbsp; def [keyboardDisable](robot.md#description)(self) |
| &nbsp;&nbsp; def [keyboardGetKey](robot.md#description)(self) |
| &nbsp;&nbsp; def [getType](robot.md#description)(self) |

| |
| --- |
| from controller import Servo |
| class [Servo](servo.md#servo) ([Device](python-api.md)) : |
| &nbsp;&nbsp; ROTATIONAL, LINEAR |
| &nbsp;&nbsp; def [setPosition](servo.md#description)(self, position) |
| &nbsp;&nbsp; def [getTargetPosition](servo.md#description)(self) |
| &nbsp;&nbsp; def [setVelocity](servo.md#description)(self, vel) |
| &nbsp;&nbsp; def [setAcceleration](servo.md#description)(self, force) |
| &nbsp;&nbsp; def [setMotorForce](servo.md#description)(self, motor\_force) |
| &nbsp;&nbsp; def [setControlP](servo.md#description)(self, p) |
| &nbsp;&nbsp; def [getMinPosition](servo.md#description)(self) |
| &nbsp;&nbsp; def [getMaxPosition](servo.md#description)(self) |
| &nbsp;&nbsp; def [enablePosition](servo.md#description)(self, ms) |
| &nbsp;&nbsp; def [disablePosition](servo.md#description)(self) |
| &nbsp;&nbsp; def [getPositionSamplingPeriod](servo.md#description)(self) |
| &nbsp;&nbsp; def [getPosition](servo.md#description)(self) |
| &nbsp;&nbsp; def [enableMotorForceFeedback](servo.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableMotorForceFeedback](servo.md#description)(self) |
| &nbsp;&nbsp; def [getMotorForceFeedbackSamplingPeriod](servo.md#description)(self) |
| &nbsp;&nbsp; def [getMotorForceFeedback](servo.md#description)(self) |
| &nbsp;&nbsp; def [setForce](servo.md#description)(self, force) |
| &nbsp;&nbsp; def [getType](servo.md#description)(self) |

| |
| --- |
| from controller import Supervisor |
| class [Supervisor](supervisor.md#supervisor) ([Robot](python-api.md)) : |
| &nbsp;&nbsp; MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR |
| &nbsp;&nbsp; def [\_\_init\_\_](robot.md#description)(self) |
| &nbsp;&nbsp; def [\_\_del\_\_](robot.md#description)(self) |
| &nbsp;&nbsp; def [exportImage](supervisor.md#description)(self, file, quality) |
| &nbsp;&nbsp; def [getRoot](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSelf](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getFromDef](supervisor.md#description)(self, name) |
| &nbsp;&nbsp; def [getFromId](supervisor.md#description)(self, id) |
| &nbsp;&nbsp; def [setLabel](supervisor.md#description)(self, id, label, xpos, ypos, size, color, transparency) |
| &nbsp;&nbsp; def [simulationQuit](supervisor.md#description)(self, status) |
| &nbsp;&nbsp; def [simulationRevert](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [simulationResetPhysics](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [loadWorld](supervisor.md#description)(self, file) |
| &nbsp;&nbsp; def [saveWorld](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [saveWorld](supervisor.md#description)(self, file) |
| &nbsp;&nbsp; def [movieStartRecording](supervisor.md#description)(self, file, width, height, codec, quality, acceleration, caption) |
| &nbsp;&nbsp; def [movieStopRecording](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [movieGetStatus](supervisor.md#description)(self) |
| &nbsp;&nbsp; def [animationStartRecording](supervisor.md#description)(self, file) |
| &nbsp;&nbsp; def [animationStopRecording](supervisor.md#description)(self) |

| |
| --- |
| from controller import TouchSensor |
| class [TouchSensor](touchsensor.md#touchsensor) ([Device](python-api.md)) : |
| &nbsp;&nbsp; BUMPER, FORCE, FORCE3D |
| &nbsp;&nbsp; def [enable](touchsensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValues](touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getType](touchsensor.md#description)(self) |

