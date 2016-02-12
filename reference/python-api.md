## Python API

The following tables describe the Python classes and their methods.

| |
| --- |
| from controller import Accelerometer |
| class [Accelerometer](reference/accelerometer.md#accelerometer) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enable](reference/accelerometer.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/accelerometer.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/accelerometer.md#description)(self) |
| &nbsp;&nbsp; def [getValues](reference/accelerometer.md#description)(self) |

| |
| --- |
| from controller import Brake |
| class [Brake](reference/brake.md#brake) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [setDampingConstant](reference/brake.md#description)(self, dampingConstant) |
| &nbsp;&nbsp; def [getType](reference/brake.md#description)(self) |

| |
| --- |
| from controller import Camera |
| class [Camera](reference/camera.md#camera) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; COLOR, RANGE\_FINDER, BOTH |
| &nbsp;&nbsp; def [enable](reference/camera.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getFov](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getMinFov](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getMaxFov](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [setFov](reference/camera.md#description)(self, fov) |
| &nbsp;&nbsp; def [getFocalLength](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getFocalDistance](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getMaxFocalDistance](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getMinFocalDistance](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [setFocalDistance](reference/camera.md#description)(self, focalDistance) |
| &nbsp;&nbsp; def [getWidth](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getHeight](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getNear](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getMaxRange](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getType](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getImage](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getImageArray](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [imageGetRed](reference/camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetRed = staticmethod(imageGetRed) |
| &nbsp;&nbsp; def [imageGetGreen](reference/camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetGreen = staticmethod(imageGetGreen) |
| &nbsp;&nbsp; def [imageGetBlue](reference/camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetBlue = staticmethod(imageGetBlue) |
| &nbsp;&nbsp; def [imageGetGrey](reference/camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; imageGetGrey = staticmethod(imageGetGrey) |
| &nbsp;&nbsp; def [getRangeImage](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [getRangeImageArray](reference/camera.md#description)(self) |
| &nbsp;&nbsp; def [rangeImageGetDepth](reference/camera.md#description)(image, width, x, y) |
| &nbsp;&nbsp; rangeImageGetDepth = staticmethod(rangeImageGetDepth) |
| &nbsp;&nbsp; def [saveImage](reference/camera.md#description)(self, filename, quality) |

| |
| --- |
| from controller import Compass |
| class [Compass](reference/compass.md#compass) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enable](reference/compass.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/compass.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/compass.md#description)(self) |
| &nbsp;&nbsp; def [getValues](reference/compass.md#description)(self) |

| |
| --- |
| from controller import Connector |
| class [Connector](reference/connector.md#connector) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enablePresence](reference/connector.md#description)(self, ms) |
| &nbsp;&nbsp; def [disablePresence](reference/connector.md#description)(self) |
| &nbsp;&nbsp; def [getPresence](reference/connector.md#description)(self) |
| &nbsp;&nbsp; def [lock](reference/connector.md#description)(self) |
| &nbsp;&nbsp; def [unlock](reference/connector.md#description)(self) |

| |
| --- |
| from controller import [Device](reference/device.md#device) |
| class Device : |
| &nbsp;&nbsp; def [getModel](reference/device.md#description)(self) |
| &nbsp;&nbsp; def [getName](reference/device.md#description)(self) |
| &nbsp;&nbsp; def [getNodeType](reference/device.md#description)(self) |

| |
| --- |
| from controller import DifferentialWheels |
| class [DifferentialWheels](reference/differentialwheels.md#differentialwheels) ([Robot](reference/python-api.md)) : |
| &nbsp;&nbsp; def [\_\_init\_\_](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [\_\_del\_\_](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [setSpeed](reference/differentialwheels.md#description)(self, left, right) |
| &nbsp;&nbsp; def [getLeftSpeed](reference/differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getRightSpeed](reference/differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [enableEncoders](reference/differentialwheels.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableEncoders](reference/differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getEncodersSamplingPeriod](reference/differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getLeftEncoder](reference/differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getRightEncoder](reference/differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [setEncoders](reference/differentialwheels.md#description)(self, left, right) |
| &nbsp;&nbsp; def [getMaxSpeed](reference/differentialwheels.md#description)(self) |
| &nbsp;&nbsp; def [getSpeedUnit](reference/differentialwheels.md#description)(self) |

| |
| --- |
| from controller import Display |
| class [Display](reference/display.md#display) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; RGB, RGBA, ARGB, BGRA |
| &nbsp;&nbsp; def [getWidth](reference/display.md#description)(self) |
| &nbsp;&nbsp; def [getHeight](reference/display.md#description)(self) |
| &nbsp;&nbsp; def [setColor](reference/display.md#description)(self, color) |
| &nbsp;&nbsp; def [setAlpha](reference/display.md#description)(self, alpha) |
| &nbsp;&nbsp; def [setOpacity](reference/display.md#description)(self, opacity) |
| &nbsp;&nbsp; def [drawPixel](reference/display.md#description)(self, x1, y1) |
| &nbsp;&nbsp; def [drawLine](reference/display.md#description)(self, x1, y1, x2, y2) |
| &nbsp;&nbsp; def [drawRectangle](reference/display.md#description)(self, x, y, width, height) |
| &nbsp;&nbsp; def [drawOval](reference/display.md#description)(self, cx, cy, a, b) |
| &nbsp;&nbsp; def [drawPolygon](reference/display.md#description)(self, x, y) |
| &nbsp;&nbsp; def [drawText](reference/display.md#description)(self, txt, x, y) |
| &nbsp;&nbsp; def [fillRectangle](reference/display.md#description)(self, x, y, width, height) |
| &nbsp;&nbsp; def [fillOval](reference/display.md#description)(self, cx, cy, a, b) |
| &nbsp;&nbsp; def [fillPolygon](reference/display.md#description)(self, x, y) |
| &nbsp;&nbsp; def [imageCopy](reference/display.md#description)(self, x, y, width, height) |
| &nbsp;&nbsp; def [imagePaste](reference/display.md#description)(self, ir, x, y) |
| &nbsp;&nbsp; def [imageLoad](reference/display.md#description)(self, filename) |
| &nbsp;&nbsp; def [imageNew](reference/display.md#description)(self, data, format) |
| &nbsp;&nbsp; def [imageSave](reference/display.md#description)(self, ir, filename) |
| &nbsp;&nbsp; def [imageDelete](reference/display.md#description)(self, ir) |

| |
| --- |
| from controller import DistanceSensor |
| class [DistanceSensor](reference/distancesensor.md#distancesensor) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enable](reference/distancesensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/distancesensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/distancesensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](reference/distancesensor.md#description)(self) |

| |
| --- |
| from controller import Emitter |
| class [Emitter](reference/emitter.md#emitter) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; CHANNEL\_BROADCAST |
| &nbsp;&nbsp; def [send](reference/emitter.md#description)(self, data) |
| &nbsp;&nbsp; def [getChannel](reference/emitter.md#description)(self) |
| &nbsp;&nbsp; def [setChannel](reference/emitter.md#description)(self, channel) |
| &nbsp;&nbsp; def [getRange](reference/emitter.md#description)(self) |
| &nbsp;&nbsp; def [setRange](reference/emitter.md#description)(self, range) |
| &nbsp;&nbsp; def [getBufferSize](reference/emitter.md#description)(self) |

| |
| --- |
| from controller import Field |
| class Field : |
| &nbsp;&nbsp; SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, |
| &nbsp;&nbsp; SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, |
| &nbsp;&nbsp; MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, |
| &nbsp;&nbsp; MF\_STRING, MF\_NODE |
| &nbsp;&nbsp; def [getType](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getTypeName](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getCount](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFBool](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFInt32](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFFloat](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFVec2f](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFVec3f](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFRotation](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFColor](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFString](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSFNode](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getMFBool](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFInt32](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFFloat](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFVec2f](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFVec3f](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFRotation](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFColor](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFString](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getMFNode](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [setSFBool](reference/supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setSFInt32](reference/supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setSFFloat](reference/supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setSFVec2f](reference/supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFVec3f](reference/supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFRotation](reference/supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFColor](reference/supervisor.md#description)(self, values) |
| &nbsp;&nbsp; def [setSFString](reference/supervisor.md#description)(self, value) |
| &nbsp;&nbsp; def [setMFBool](reference/supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [setMFInt32](reference/supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [setMFFloat](reference/supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [setMFVec2f](reference/supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFVec3f](reference/supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFRotation](reference/supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFColor](reference/supervisor.md#description)(self, index, values) |
| &nbsp;&nbsp; def [setMFString](reference/supervisor.md#description)(self, index, value) |
| &nbsp;&nbsp; def [importMFNode](reference/supervisor.md#description)(self, position, filename) |
| &nbsp;&nbsp; def [importMFNodeFromString](reference/supervisor.md#description)(self, position, nodeString) |
| &nbsp;&nbsp; def [removeMFNode](reference/supervisor.md#description)(self, position) |

| |
| --- |
| from controller import GPS |
| class [GPS](reference/gps.md#gps) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enable](reference/gps.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/gps.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/gps.md#description)(self) |
| &nbsp;&nbsp; def [getValues](reference/gps.md#description)(self) |

| |
| --- |
| from controller import Gyro |
| class [Gyro](reference/gyro.md#gyro) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enable](reference/gyro.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/gyro.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/gyro.md#description)(self) |
| &nbsp;&nbsp; def [getValues](reference/gyro.md#description)(self) |

| |
| --- |
| from controller import ImageRef |
| class ImageRef : |

| |
| --- |
| from controller import InertialUnit |
| class [InertialUnit](reference/inertialunit.md#inertialunit) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enable](reference/inertialunit.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/inertialunit.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/inertialunit.md#description)(self) |
| &nbsp;&nbsp; def [getRollPitchYaw](reference/inertialunit.md#description)(self) |

| |
| --- |
| from controller import LED |
| class [LED](reference/led.md#led) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [set](reference/led.md#description)(self, state) |
| &nbsp;&nbsp; def [get](reference/led.md#description)(self) |

| |
| --- |
| from controller import LightSensor |
| class [LightSensor](reference/lightsensor.md#lightsensor) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [enable](reference/lightsensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/lightsensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/lightsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](reference/lightsensor.md#description)(self) |

| |
| --- |
| from controller import Motion |
| class [Motion](reference/motion.md#motion) : |
| &nbsp;&nbsp; def [\_\_init\_\_](reference/motion.md#description)(self, fileName) |
| &nbsp;&nbsp; def [\_\_del\_\_](reference/motion.md#description)(self) |
| &nbsp;&nbsp; def [isValid](reference/motion.md#description)(self) |
| &nbsp;&nbsp; def [play](reference/motion.md#description)(self) |
| &nbsp;&nbsp; def [stop](reference/motion.md#description)(self) |
| &nbsp;&nbsp; def [setLoop](reference/motion.md#description)(self, loop) |
| &nbsp;&nbsp; def [setReverse](reference/motion.md#description)(self, reverse) |
| &nbsp;&nbsp; def [isOver](reference/motion.md#description)(self) |
| &nbsp;&nbsp; def [getDuration](reference/motion.md#description)(self) |
| &nbsp;&nbsp; def [getTime](reference/motion.md#description)(self) |
| &nbsp;&nbsp; def [setTime](reference/motion.md#description)(self, time) |

| |
| --- |
| from controller import Motor |
| class [Motor](reference/motor.md#motor) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; ROTATIONAL, LINEAR |
| &nbsp;&nbsp; def [setPosition](reference/motor.md#description)(self, position) |
| &nbsp;&nbsp; def [setVelocity](reference/motor.md#description)(self, vel) |
| &nbsp;&nbsp; def [setAcceleration](reference/motor.md#description)(self, force) |
| &nbsp;&nbsp; def [setAvailableForce](reference/motor.md#description)(self, motor\_force) |
| &nbsp;&nbsp; def [setAvailableTorque](reference/motor.md#description)(self, motor\_torque) |
| &nbsp;&nbsp; def [setControlPID](reference/motor.md#description)(self, p, i, d) |
| &nbsp;&nbsp; def [getTargetPosition](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getMinPosition](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getMaxPosition](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getVelocity](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getMaxVelocity](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getAcceleration](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getAvailableForce](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getMaxForce](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getAvailableTorque](reference/motor.md#description)(self) |
| &nbsp;&nbsp; double [getMaxTorque](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [enableForceFeedback](reference/motor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableForceFeedback](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getForceFeedbackSamplingPeriod](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getForceFeedback](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [setForce](reference/motor.md#description)(self, torque) |
| &nbsp;&nbsp; def [enableTorqueFeedback](reference/motor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableTorqueFeedback](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getTorqueFeedbackSamplingPeriod](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [getTorqueFeedback](reference/motor.md#description)(self) |
| &nbsp;&nbsp; def [setTorque](reference/motor.md#description)(self, torque) |
| &nbsp;&nbsp; def [getType](reference/motor.md#description)(self) |

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
| &nbsp;&nbsp; def [remove](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getType](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getId](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getTypeName](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getBaseTypeName](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getField](reference/supervisor.md#description)(self, fieldName) |
| &nbsp;&nbsp; def [getParentNode](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getPosition](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getOrientation](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getCenterOfMass](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getContactPoint](reference/supervisor.md#description)(self, index) |
| &nbsp;&nbsp; def [getNumberOfContactPoints](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getStaticBalance](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getVelocity](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [setVelocity](reference/supervisor.md#description)(self, velocity) |
| &nbsp;&nbsp; def [resetPhysics](reference/supervisor.md#description)(self) |

| |
| --- |
| from controller import Pen |
| class [Pen](reference/pen.md#pen) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; def [write](reference/pen.md#description)(self, write) |
| &nbsp;&nbsp; def [setInkColor](reference/pen.md#description)(self, color, density) |

| |
| --- |
| from controller import PositionSensor |
| class [PositionSensor](reference/positionsensor.md#positionsensor) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; ANGULAR, LINEAR |
| &nbsp;&nbsp; def [enable](reference/positionsensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/positionsensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/positionsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](reference/positionsensor.md#description)(self) |
| &nbsp;&nbsp; def [getType](reference/positionsensor.md#description)(self) |

| |
| --- |
| from controller import Receiver |
| class [Receiver](reference/receiver.md#receiver) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; CHANNEL\_BROADCAST |
| &nbsp;&nbsp; def [enable](reference/receiver.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [getQueueLength](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [nextPacket](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [getData](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [getDataSize](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [getSignalStrength](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [getEmitterDirection](reference/receiver.md#description)(self) |
| &nbsp;&nbsp; def [setChannel](reference/receiver.md#description)(self, channel) |
| &nbsp;&nbsp; def [getChannel](reference/receiver.md#description)(self) |

| |
| --- |
| from controller import Robot |
| class [Robot](reference/robot.md#robot) : |
| &nbsp;&nbsp; MODE\_SIMULATION, MODE\_CROSS\_COMPILATION, |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL |
| &nbsp;&nbsp; KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT, KEYBOARD\_UP, |
| &nbsp;&nbsp; KEYBOARD\_RIGHT, KEYBOARD\_DOWN, KEYBOARD\_PAGEUP, |
| &nbsp;&nbsp; KEYBOARD\_PAGEDOWN, KEYBOARD\_NUMPAD\_HOME, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_LEFT, KEYBOARD\_NUMPAD\_UP, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_RIGHT, KEYBOARD\_NUMPAD\_DOWN, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_END, KEYBOARD\_KEY, KEYBOARD\_SHIFT, |
| &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT |
| &nbsp;&nbsp; def [\_\_init\_\_](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [\_\_del\_\_](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [step](reference/robot.md#description)(self, ms) |
| &nbsp;&nbsp; def [getAccelerometer](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getBrake](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getCamera](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getCompass](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getConnector](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getDisplay](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getDistanceSensor](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getEmitter](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getGPS](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getGyro](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getInertialUnit](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getLED](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getLightSensor](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getMotor](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getPen](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getPositionSensor](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getReceiver](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getServo](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getTouchSensor](reference/robot.md#description)(self, name) |
| &nbsp;&nbsp; def [getNumberOfDevices](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getDeviceByIndex](reference/robot.md#description)(self, index) |
| &nbsp;&nbsp; def [batterySensorEnable](reference/robot.md#description)(self, ms) |
| &nbsp;&nbsp; def [batterySensorDisable](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [batterySensorGetSamplingPeriod](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [batterySensorGetValue](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getBasicTimeStep](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getMode](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getModel](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getData](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [setData](reference/robot.md#description)(self, data) |
| &nbsp;&nbsp; def [getName](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getControllerName](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getControllerArguments](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getProjectPath](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getSynchronization](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getTime](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getWorldPath](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [keyboardEnable](reference/robot.md#description)(self, ms) |
| &nbsp;&nbsp; def [keyboardDisable](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [keyboardGetKey](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [getType](reference/robot.md#description)(self) |

| |
| --- |
| from controller import Servo |
| class [Servo](reference/servo.md#servo) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; ROTATIONAL, LINEAR |
| &nbsp;&nbsp; def [setPosition](reference/servo.md#description)(self, position) |
| &nbsp;&nbsp; def [getTargetPosition](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [setVelocity](reference/servo.md#description)(self, vel) |
| &nbsp;&nbsp; def [setAcceleration](reference/servo.md#description)(self, force) |
| &nbsp;&nbsp; def [setMotorForce](reference/servo.md#description)(self, motor\_force) |
| &nbsp;&nbsp; def [setControlP](reference/servo.md#description)(self, p) |
| &nbsp;&nbsp; def [getMinPosition](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [getMaxPosition](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [enablePosition](reference/servo.md#description)(self, ms) |
| &nbsp;&nbsp; def [disablePosition](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [getPositionSamplingPeriod](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [getPosition](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [enableMotorForceFeedback](reference/servo.md#description)(self, ms) |
| &nbsp;&nbsp; def [disableMotorForceFeedback](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [getMotorForceFeedbackSamplingPeriod](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [getMotorForceFeedback](reference/servo.md#description)(self) |
| &nbsp;&nbsp; def [setForce](reference/servo.md#description)(self, force) |
| &nbsp;&nbsp; def [getType](reference/servo.md#description)(self) |

| |
| --- |
| from controller import Supervisor |
| class [Supervisor](reference/supervisor.md#supervisor) ([Robot](reference/python-api.md)) : |
| &nbsp;&nbsp; MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR |
| &nbsp;&nbsp; def [\_\_init\_\_](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [\_\_del\_\_](reference/robot.md#description)(self) |
| &nbsp;&nbsp; def [exportImage](reference/supervisor.md#description)(self, file, quality) |
| &nbsp;&nbsp; def [getRoot](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getSelf](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [getFromDef](reference/supervisor.md#description)(self, name) |
| &nbsp;&nbsp; def [getFromId](reference/supervisor.md#description)(self, id) |
| &nbsp;&nbsp; def [setLabel](reference/supervisor.md#description)(self, id, label, xpos, ypos, size, color, transparency) |
| &nbsp;&nbsp; def [simulationQuit](reference/supervisor.md#description)(self, status) |
| &nbsp;&nbsp; def [simulationRevert](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [simulationResetPhysics](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [loadWorld](reference/supervisor.md#description)(self, file) |
| &nbsp;&nbsp; def [saveWorld](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [saveWorld](reference/supervisor.md#description)(self, file) |
| &nbsp;&nbsp; def [movieStartRecording](reference/supervisor.md#description)(self, file, width, height, codec, quality, acceleration, caption) |
| &nbsp;&nbsp; def [movieStopRecording](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [movieGetStatus](reference/supervisor.md#description)(self) |
| &nbsp;&nbsp; def [animationStartRecording](reference/supervisor.md#description)(self, file) |
| &nbsp;&nbsp; def [animationStopRecording](reference/supervisor.md#description)(self) |

| |
| --- |
| from controller import TouchSensor |
| class [TouchSensor](reference/touchsensor.md#touchsensor) ([Device](reference/python-api.md)) : |
| &nbsp;&nbsp; BUMPER, FORCE, FORCE3D |
| &nbsp;&nbsp; def [enable](reference/touchsensor.md#description)(self, ms) |
| &nbsp;&nbsp; def [disable](reference/touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getSamplingPeriod](reference/touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValue](reference/touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getValues](reference/touchsensor.md#description)(self) |
| &nbsp;&nbsp; def [getType](reference/touchsensor.md#description)(self) |

