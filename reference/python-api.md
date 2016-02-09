## Python API

The following tables describe the Python classes and their methods.

| |
| --- |
| from controller import Accelerometer  |
|  class `Accelerometer` (`Device`) :  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValues`(self)  |

| |
| --- |
| from controller import Brake  |
|  class `Brake` (`Device`) :  |
|  &nbsp;&nbsp; def `setDampingConstant`(self, dampingConstant)  |
|  &nbsp;&nbsp; def `getType`(self)  |

| |
| --- |
| from controller import Camera  |
|  class `Camera` (`Device`) :  |
|  &nbsp;&nbsp; COLOR, RANGE\_FINDER, BOTH  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getFov`(self)  |
|  &nbsp;&nbsp; def `getMinFov`(self)  |
|  &nbsp;&nbsp; def `getMaxFov`(self)  |
|  &nbsp;&nbsp; def `setFov`(self, fov)  |
|  &nbsp;&nbsp; def `getFocalLength`(self)  |
|  &nbsp;&nbsp; def `getFocalDistance`(self)  |
|  &nbsp;&nbsp; def `getMaxFocalDistance`(self)  |
|  &nbsp;&nbsp; def `getMinFocalDistance`(self)  |
|  &nbsp;&nbsp; def `setFocalDistance`(self, focalDistance)  |
|  &nbsp;&nbsp; def `getWidth`(self)  |
|  &nbsp;&nbsp; def `getHeight`(self)  |
|  &nbsp;&nbsp; def `getNear`(self)  |
|  &nbsp;&nbsp; def `getMaxRange`(self)  |
|  &nbsp;&nbsp; def `getType`(self)  |
|  &nbsp;&nbsp; def `getImage`(self)  |
|  &nbsp;&nbsp; def `getImageArray`(self)  |
|  &nbsp;&nbsp; def `imageGetRed`(image, width, x, y)  |
|  &nbsp;&nbsp; imageGetRed = staticmethod(imageGetRed)  |
|  &nbsp;&nbsp; def `imageGetGreen`(image, width, x, y)  |
|  &nbsp;&nbsp; imageGetGreen = staticmethod(imageGetGreen)  |
|  &nbsp;&nbsp; def `imageGetBlue`(image, width, x, y)  |
|  &nbsp;&nbsp; imageGetBlue = staticmethod(imageGetBlue)  |
|  &nbsp;&nbsp; def `imageGetGrey`(image, width, x, y)  |
|  &nbsp;&nbsp; imageGetGrey = staticmethod(imageGetGrey)  |
|  &nbsp;&nbsp; def `getRangeImage`(self)  |
|  &nbsp;&nbsp; def `getRangeImageArray`(self)  |
|  &nbsp;&nbsp; def `rangeImageGetDepth`(image, width, x, y)  |
|  &nbsp;&nbsp; rangeImageGetDepth = staticmethod(rangeImageGetDepth)  |
|  &nbsp;&nbsp; def `saveImage`(self, filename, quality)  |

| |
| --- |
| from controller import Compass  |
|  class `Compass` (`Device`) :  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValues`(self)  |

| |
| --- |
| from controller import Connector  |
|  class `Connector` (`Device`) :  |
|  &nbsp;&nbsp; def `enablePresence`(self, ms)  |
|  &nbsp;&nbsp; def `disablePresence`(self)  |
|  &nbsp;&nbsp; def `getPresence`(self)  |
|  &nbsp;&nbsp; def `lock`(self)  |
|  &nbsp;&nbsp; def `unlock`(self)  |

| |
| --- |
| from controller import `Device`  |
|  class Device :  |
|  &nbsp;&nbsp; def `getModel`(self)  |
|  &nbsp;&nbsp; def `getName`(self)  |
|  &nbsp;&nbsp; def `getNodeType`(self)  |

| |
| --- |
| from controller import DifferentialWheels  |
|  class `DifferentialWheels` (`Robot`) :  |
|  &nbsp;&nbsp; def `__init__`(self)  |
|  &nbsp;&nbsp; def `__del__`(self)  |
|  &nbsp;&nbsp; def `setSpeed`(self, left, right)  |
|  &nbsp;&nbsp; def `getLeftSpeed`(self)  |
|  &nbsp;&nbsp; def `getRightSpeed`(self)  |
|  &nbsp;&nbsp; def `enableEncoders`(self, ms)  |
|  &nbsp;&nbsp; def `disableEncoders`(self)  |
|  &nbsp;&nbsp; def `getEncodersSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getLeftEncoder`(self)  |
|  &nbsp;&nbsp; def `getRightEncoder`(self)  |
|  &nbsp;&nbsp; def `setEncoders`(self, left, right)  |
|  &nbsp;&nbsp; def `getMaxSpeed`(self)  |
|  &nbsp;&nbsp; def `getSpeedUnit`(self)  |

| |
| --- |
| from controller import Display  |
|  class `Display` (`Device`) :  |
|  &nbsp;&nbsp; RGB, RGBA, ARGB, BGRA  |
|  &nbsp;&nbsp; def `getWidth`(self)  |
|  &nbsp;&nbsp; def `getHeight`(self)  |
|  &nbsp;&nbsp; def `setColor`(self, color)  |
|  &nbsp;&nbsp; def `setAlpha`(self, alpha)  |
|  &nbsp;&nbsp; def `setOpacity`(self, opacity)  |
|  &nbsp;&nbsp; def `drawPixel`(self, x1, y1)  |
|  &nbsp;&nbsp; def `drawLine`(self, x1, y1, x2, y2)  |
|  &nbsp;&nbsp; def `drawRectangle`(self, x, y, width, height)  |
|  &nbsp;&nbsp; def `drawOval`(self, cx, cy, a, b)  |
|  &nbsp;&nbsp; def `drawPolygon`(self, x, y)  |
|  &nbsp;&nbsp; def `drawText`(self, txt, x, y)  |
|  &nbsp;&nbsp; def `fillRectangle`(self, x, y, width, height)  |
|  &nbsp;&nbsp; def `fillOval`(self, cx, cy, a, b)  |
|  &nbsp;&nbsp; def `fillPolygon`(self, x, y)  |
|  &nbsp;&nbsp; def `imageCopy`(self, x, y, width, height)  |
|  &nbsp;&nbsp; def `imagePaste`(self, ir, x, y)  |
|  &nbsp;&nbsp; def `imageLoad`(self, filename)  |
|  &nbsp;&nbsp; def `imageNew`(self, data, format)  |
|  &nbsp;&nbsp; def `imageSave`(self, ir, filename)  |
|  &nbsp;&nbsp; def `imageDelete`(self, ir)  |

| |
| --- |
| from controller import DistanceSensor  |
|  class `DistanceSensor` (`Device`) :  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValue`(self)  |

| |
| --- |
| from controller import Emitter  |
|  class `Emitter` (`Device`) :  |
|  &nbsp;&nbsp; CHANNEL\_BROADCAST  |
|  &nbsp;&nbsp; def `send`(self, data)  |
|  &nbsp;&nbsp; def `getChannel`(self)  |
|  &nbsp;&nbsp; def `setChannel`(self, channel)  |
|  &nbsp;&nbsp; def `getRange`(self)  |
|  &nbsp;&nbsp; def `setRange`(self, range)  |
|  &nbsp;&nbsp; def `getBufferSize`(self)  |

| |
| --- |
| from controller import Field  |
|  class Field :  |
|  &nbsp;&nbsp; SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F,  |
|  &nbsp;&nbsp; SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF,  |
|  &nbsp;&nbsp; MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR,  |
|  &nbsp;&nbsp; MF\_STRING, MF\_NODE  |
|  &nbsp;&nbsp; def `getType`(self)  |
|  &nbsp;&nbsp; def `getTypeName`(self)  |
|  &nbsp;&nbsp; def `getCount`(self)  |
|  &nbsp;&nbsp; def `getSFBool`(self)  |
|  &nbsp;&nbsp; def `getSFInt32`(self)  |
|  &nbsp;&nbsp; def `getSFFloat`(self)  |
|  &nbsp;&nbsp; def `getSFVec2f`(self)  |
|  &nbsp;&nbsp; def `getSFVec3f`(self)  |
|  &nbsp;&nbsp; def `getSFRotation`(self)  |
|  &nbsp;&nbsp; def `getSFColor`(self)  |
|  &nbsp;&nbsp; def `getSFString`(self)  |
|  &nbsp;&nbsp; def `getSFNode`(self)  |
|  &nbsp;&nbsp; def `getMFBool`(self, index)  |
|  &nbsp;&nbsp; def `getMFInt32`(self, index)  |
|  &nbsp;&nbsp; def `getMFFloat`(self, index)  |
|  &nbsp;&nbsp; def `getMFVec2f`(self, index)  |
|  &nbsp;&nbsp; def `getMFVec3f`(self, index)  |
|  &nbsp;&nbsp; def `getMFRotation`(self, index)  |
|  &nbsp;&nbsp; def `getMFColor`(self, index)  |
|  &nbsp;&nbsp; def `getMFString`(self, index)  |
|  &nbsp;&nbsp; def `getMFNode`(self, index)  |
|  &nbsp;&nbsp; def `setSFBool`(self, value)  |
|  &nbsp;&nbsp; def `setSFInt32`(self, value)  |
|  &nbsp;&nbsp; def `setSFFloat`(self, value)  |
|  &nbsp;&nbsp; def `setSFVec2f`(self, values)  |
|  &nbsp;&nbsp; def `setSFVec3f`(self, values)  |
|  &nbsp;&nbsp; def `setSFRotation`(self, values)  |
|  &nbsp;&nbsp; def `setSFColor`(self, values)  |
|  &nbsp;&nbsp; def `setSFString`(self, value)  |
|  &nbsp;&nbsp; def `setMFBool`(self, index, value)  |
|  &nbsp;&nbsp; def `setMFInt32`(self, index, value)  |
|  &nbsp;&nbsp; def `setMFFloat`(self, index, value)  |
|  &nbsp;&nbsp; def `setMFVec2f`(self, index, values)  |
|  &nbsp;&nbsp; def `setMFVec3f`(self, index, values)  |
|  &nbsp;&nbsp; def `setMFRotation`(self, index, values)  |
|  &nbsp;&nbsp; def `setMFColor`(self, index, values)  |
|  &nbsp;&nbsp; def `setMFString`(self, index, value)  |
|  &nbsp;&nbsp; def `importMFNode`(self, position, filename)  |
|  &nbsp;&nbsp; def `importMFNodeFromString`(self, position, nodeString)  |
|  &nbsp;&nbsp; def `removeMFNode`(self, position)  |

| |
| --- |
| from controller import GPS  |
|  class `GPS` (`Device`) :  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValues`(self)  |

| |
| --- |
| from controller import Gyro  |
|  class `Gyro` (`Device`) :  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValues`(self)  |

| |
| --- |
| from controller import ImageRef  |
|  class ImageRef :  |

| |
| --- |
| from controller import InertialUnit  |
|  class `InertialUnit` (`Device`) :  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getRollPitchYaw`(self)  |

| |
| --- |
| from controller import LED  |
|  class `LED` (`Device`) :  |
|  &nbsp;&nbsp; def `set`(self, state)  |
|  &nbsp;&nbsp; def `get`(self)  |

| |
| --- |
| from controller import LightSensor  |
|  class `LightSensor` (`Device`) :  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValue`(self)  |

| |
| --- |
| from controller import Motion  |
|  class `Motion` :  |
|  &nbsp;&nbsp; def `__init__`(self, fileName)  |
|  &nbsp;&nbsp; def `__del__`(self)  |
|  &nbsp;&nbsp; def `isValid`(self)  |
|  &nbsp;&nbsp; def `play`(self)  |
|  &nbsp;&nbsp; def `stop`(self)  |
|  &nbsp;&nbsp; def `setLoop`(self, loop)  |
|  &nbsp;&nbsp; def `setReverse`(self, reverse)  |
|  &nbsp;&nbsp; def `isOver`(self)  |
|  &nbsp;&nbsp; def `getDuration`(self)  |
|  &nbsp;&nbsp; def `getTime`(self)  |
|  &nbsp;&nbsp; def `setTime`(self, time)  |

| |
| --- |
| from controller import Motor  |
|  class `Motor` (`Device`) :  |
|  &nbsp;&nbsp; ROTATIONAL, LINEAR  |
|  &nbsp;&nbsp; def `setPosition`(self, position)  |
|  &nbsp;&nbsp; def `setVelocity`(self, vel)  |
|  &nbsp;&nbsp; def `setAcceleration`(self, force)  |
|  &nbsp;&nbsp; def `setAvailableForce`(self, motor\_force)  |
|  &nbsp;&nbsp; def `setAvailableTorque`(self, motor\_torque)  |
|  &nbsp;&nbsp; def `setControlPID`(self, p, i, d)  |
|  &nbsp;&nbsp; def `getTargetPosition`(self)  |
|  &nbsp;&nbsp; def `getMinPosition`(self)  |
|  &nbsp;&nbsp; def `getMaxPosition`(self)  |
|  &nbsp;&nbsp; def `getVelocity`(self)  |
|  &nbsp;&nbsp; def `getMaxVelocity`(self)  |
|  &nbsp;&nbsp; def `getAcceleration`(self)  |
|  &nbsp;&nbsp; def `getAvailableForce`(self)  |
|  &nbsp;&nbsp; def `getMaxForce`(self)  |
|  &nbsp;&nbsp; def `getAvailableTorque`(self)  |
|  &nbsp;&nbsp; double `getMaxTorque`(self)  |
|  &nbsp;&nbsp; def `enableForceFeedback`(self, ms)  |
|  &nbsp;&nbsp; def `disableForceFeedback`(self)  |
|  &nbsp;&nbsp; def `getForceFeedbackSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getForceFeedback`(self)  |
|  &nbsp;&nbsp; def `setForce`(self, torque)  |
|  &nbsp;&nbsp; def `enableTorqueFeedback`(self, ms)  |
|  &nbsp;&nbsp; def `disableTorqueFeedback`(self)  |
|  &nbsp;&nbsp; def `getTorqueFeedbackSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getTorqueFeedback`(self)  |
|  &nbsp;&nbsp; def `setTorque`(self, torque)  |
|  &nbsp;&nbsp; def `getType`(self)  |

| |
| --- |
| from controller import Node  |
|  class Node :  |
|  &nbsp;&nbsp; NO\_NODE, APPEARANCE, BACKGROUND, BOX, COLOR, CONE,  |
|  &nbsp;&nbsp; COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT, ELEVATION\_GRID,  |
|  &nbsp;&nbsp; EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE, INDEXED\_FACE\_SET,  |
|  &nbsp;&nbsp; INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT, SHAPE, SPHERE,  |
|  &nbsp;&nbsp; SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM,  |
|  &nbsp;&nbsp; TRANSFORM, VIEWPOINT, WORLD\_INFO, CAPSULE, PLANE, ROBOT,  |
|  &nbsp;&nbsp; SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID, PHYSICS, CAMERA\_ZOOM,  |
|  &nbsp;&nbsp; CHARGER, DAMPING, CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE,  |
|  &nbsp;&nbsp; CAMERA, COMPASS, CONNECTOR, DISPLAY, DISTANCE\_SENSOR,  |
|  &nbsp;&nbsp; EMITTER, GPS, GYRO, LED, LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN,  |
|  &nbsp;&nbsp; POSITION\_SENSOR, RADIO, RECEIVER, SERVO, SPEAKER,  |
|  &nbsp;&nbsp; TOUCH\_SENSOR  |
|  &nbsp;&nbsp; def `remove`(self)  |
|  &nbsp;&nbsp; def `getType`(self)  |
|  &nbsp;&nbsp; def `getId`(self)  |
|  &nbsp;&nbsp; def `getTypeName`(self)  |
|  &nbsp;&nbsp; def `getBaseTypeName`(self)  |
|  &nbsp;&nbsp; def `getField`(self, fieldName)  |
|  &nbsp;&nbsp; def `getParentNode`(self)  |
|  &nbsp;&nbsp; def `getPosition`(self)  |
|  &nbsp;&nbsp; def `getOrientation`(self)  |
|  &nbsp;&nbsp; def `getCenterOfMass`(self)  |
|  &nbsp;&nbsp; def `getContactPoint`(self, index)  |
|  &nbsp;&nbsp; def `getNumberOfContactPoints`(self)  |
|  &nbsp;&nbsp; def `getStaticBalance`(self)  |
|  &nbsp;&nbsp; def `getVelocity`(self)  |
|  &nbsp;&nbsp; def `setVelocity`(self, velocity)  |
|  &nbsp;&nbsp; def `resetPhysics`(self)  |

| |
| --- |
| from controller import Pen  |
|  class `Pen` (`Device`) :  |
|  &nbsp;&nbsp; def `write`(self, write)  |
|  &nbsp;&nbsp; def `setInkColor`(self, color, density)  |

| |
| --- |
| from controller import PositionSensor  |
|  class `PositionSensor` (`Device`) :  |
|  &nbsp;&nbsp; ANGULAR, LINEAR  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValue`(self)  |
|  &nbsp;&nbsp; def `getType`(self)  |

| |
| --- |
| from controller import Receiver  |
|  class `Receiver` (`Device`) :  |
|  &nbsp;&nbsp; CHANNEL\_BROADCAST  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getQueueLength`(self)  |
|  &nbsp;&nbsp; def `nextPacket`(self)  |
|  &nbsp;&nbsp; def `getData`(self)  |
|  &nbsp;&nbsp; def `getDataSize`(self)  |
|  &nbsp;&nbsp; def `getSignalStrength`(self)  |
|  &nbsp;&nbsp; def `getEmitterDirection`(self)  |
|  &nbsp;&nbsp; def `setChannel`(self, channel)  |
|  &nbsp;&nbsp; def `getChannel`(self)  |

| |
| --- |
| from controller import Robot  |
|  class `Robot` :  |
|  &nbsp;&nbsp; MODE\_SIMULATION, MODE\_CROSS\_COMPILATION,  |
|  &nbsp;&nbsp; MODE\_REMOTE\_CONTROL  |
|  &nbsp;&nbsp; KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT, KEYBOARD\_UP,  |
|  &nbsp;&nbsp; KEYBOARD\_RIGHT, KEYBOARD\_DOWN, KEYBOARD\_PAGEUP,  |
|  &nbsp;&nbsp; KEYBOARD\_PAGEDOWN, KEYBOARD\_NUMPAD\_HOME,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_LEFT, KEYBOARD\_NUMPAD\_UP,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_RIGHT, KEYBOARD\_NUMPAD\_DOWN,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_END, KEYBOARD\_KEY, KEYBOARD\_SHIFT,  |
|  &nbsp;&nbsp; KEYBOARD\_CONTROL, KEYBOARD\_ALT  |
|  &nbsp;&nbsp; def `__init__`(self)  |
|  &nbsp;&nbsp; def `__del__`(self)  |
|  &nbsp;&nbsp; def `step`(self, ms)  |
|  &nbsp;&nbsp; def `getAccelerometer`(self, name)  |
|  &nbsp;&nbsp; def `getBrake`(self, name)  |
|  &nbsp;&nbsp; def `getCamera`(self, name)  |
|  &nbsp;&nbsp; def `getCompass`(self, name)  |
|  &nbsp;&nbsp; def `getConnector`(self, name)  |
|  &nbsp;&nbsp; def `getDisplay`(self, name)  |
|  &nbsp;&nbsp; def `getDistanceSensor`(self, name)  |
|  &nbsp;&nbsp; def `getEmitter`(self, name)  |
|  &nbsp;&nbsp; def `getGPS`(self, name)  |
|  &nbsp;&nbsp; def `getGyro`(self, name)  |
|  &nbsp;&nbsp; def `getInertialUnit`(self, name)  |
|  &nbsp;&nbsp; def `getLED`(self, name)  |
|  &nbsp;&nbsp; def `getLightSensor`(self, name)  |
|  &nbsp;&nbsp; def `getMotor`(self, name)  |
|  &nbsp;&nbsp; def `getPen`(self, name)  |
|  &nbsp;&nbsp; def `getPositionSensor`(self, name)  |
|  &nbsp;&nbsp; def `getReceiver`(self, name)  |
|  &nbsp;&nbsp; def `getServo`(self, name)  |
|  &nbsp;&nbsp; def `getTouchSensor`(self, name)  |
|  &nbsp;&nbsp; def `getNumberOfDevices`(self)  |
|  &nbsp;&nbsp; def `getDeviceByIndex`(self, index)  |
|  &nbsp;&nbsp; def `batterySensorEnable`(self, ms)  |
|  &nbsp;&nbsp; def `batterySensorDisable`(self)  |
|  &nbsp;&nbsp; def `batterySensorGetSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `batterySensorGetValue`(self)  |
|  &nbsp;&nbsp; def `getBasicTimeStep`(self)  |
|  &nbsp;&nbsp; def `getMode`(self)  |
|  &nbsp;&nbsp; def `getModel`(self)  |
|  &nbsp;&nbsp; def `getData`(self)  |
|  &nbsp;&nbsp; def `setData`(self, data)  |
|  &nbsp;&nbsp; def `getName`(self)  |
|  &nbsp;&nbsp; def `getControllerName`(self)  |
|  &nbsp;&nbsp; def `getControllerArguments`(self)  |
|  &nbsp;&nbsp; def `getProjectPath`(self)  |
|  &nbsp;&nbsp; def `getSynchronization`(self)  |
|  &nbsp;&nbsp; def `getTime`(self)  |
|  &nbsp;&nbsp; def `getWorldPath`(self)  |
|  &nbsp;&nbsp; def `keyboardEnable`(self, ms)  |
|  &nbsp;&nbsp; def `keyboardDisable`(self)  |
|  &nbsp;&nbsp; def `keyboardGetKey`(self)  |
|  &nbsp;&nbsp; def `getType`(self)  |

| |
| --- |
| from controller import Servo  |
|  class `Servo` (`Device`) :  |
|  &nbsp;&nbsp; ROTATIONAL, LINEAR  |
|  &nbsp;&nbsp; def `setPosition`(self, position)  |
|  &nbsp;&nbsp; def `getTargetPosition`(self)  |
|  &nbsp;&nbsp; def `setVelocity`(self, vel)  |
|  &nbsp;&nbsp; def `setAcceleration`(self, force)  |
|  &nbsp;&nbsp; def `setMotorForce`(self, motor\_force)  |
|  &nbsp;&nbsp; def `setControlP`(self, p)  |
|  &nbsp;&nbsp; def `getMinPosition`(self)  |
|  &nbsp;&nbsp; def `getMaxPosition`(self)  |
|  &nbsp;&nbsp; def `enablePosition`(self, ms)  |
|  &nbsp;&nbsp; def `disablePosition`(self)  |
|  &nbsp;&nbsp; def `getPositionSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getPosition`(self)  |
|  &nbsp;&nbsp; def `enableMotorForceFeedback`(self, ms)  |
|  &nbsp;&nbsp; def `disableMotorForceFeedback`(self)  |
|  &nbsp;&nbsp; def `getMotorForceFeedbackSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getMotorForceFeedback`(self)  |
|  &nbsp;&nbsp; def `setForce`(self, force)  |
|  &nbsp;&nbsp; def `getType`(self)  |

| |
| --- |
| from controller import Supervisor  |
|  class `Supervisor` (`Robot`) :  |
|  &nbsp;&nbsp; MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR  |
|  &nbsp;&nbsp; def `__init__`(self)  |
|  &nbsp;&nbsp; def `__del__`(self)  |
|  &nbsp;&nbsp; def `exportImage`(self, file, quality)  |
|  &nbsp;&nbsp; def `getRoot`(self)  |
|  &nbsp;&nbsp; def `getSelf`(self)  |
|  &nbsp;&nbsp; def `getFromDef`(self, name)  |
|  &nbsp;&nbsp; def `getFromId`(self, id)  |
|  &nbsp;&nbsp; def `setLabel`(self, id, label, xpos, ypos, size, color, transparency)  |
|  &nbsp;&nbsp; def `simulationQuit`(self, status)  |
|  &nbsp;&nbsp; def `simulationRevert`(self)  |
|  &nbsp;&nbsp; def `simulationResetPhysics`(self)  |
|  &nbsp;&nbsp; def `loadWorld`(self, file)  |
|  &nbsp;&nbsp; def `saveWorld`(self)  |
|  &nbsp;&nbsp; def `saveWorld`(self, file)  |
|  &nbsp;&nbsp; def `movieStartRecording`(self, file, width, height, codec, quality, acceleration, caption)  |
|  &nbsp;&nbsp; def `movieStopRecording`(self)  |
|  &nbsp;&nbsp; def `movieGetStatus`(self)  |
|  &nbsp;&nbsp; def `animationStartRecording`(self, file)  |
|  &nbsp;&nbsp; def `animationStopRecording`(self)  |

| |
| --- |
| from controller import TouchSensor  |
|  class `TouchSensor` (`Device`) :  |
|  &nbsp;&nbsp; BUMPER, FORCE, FORCE3D  |
|  &nbsp;&nbsp; def `enable`(self, ms)  |
|  &nbsp;&nbsp; def `disable`(self)  |
|  &nbsp;&nbsp; def `getSamplingPeriod`(self)  |
|  &nbsp;&nbsp; def `getValue`(self)  |
|  &nbsp;&nbsp; def `getValues`(self)  |
|  &nbsp;&nbsp; def `getType`(self)  |

