## C++ API

The following tables describe the C++ classes and their methods.

| |
| --- |
| #include <webots/Accelerometer.hpp>  |
|  class `Accelerometer` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; const double *`getValues`() const;  |
| };  |

| |
| --- |
| #include <webots/Brake.hpp>  |
|  class `Brake` : public `Device` {  |
|  &nbsp;&nbsp; void `setDampingConstant`(double dampingConstant) const;  |
|  &nbsp;&nbsp; int `getType`() const;  |
| };  |

| |
| --- |
| #include <webots/Camera.hpp>  |
|  class `Camera` : public `Device` {  |
|  &nbsp;&nbsp; enum {COLOR, RANGE\_FINDER, BOTH};  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getFov`() const;  |
|  &nbsp;&nbsp; double `getMinFov`() const;  |
|  &nbsp;&nbsp; double `getMaxFov`() const;  |
|  &nbsp;&nbsp; virtual void `setFov`(double fov);  |
|  &nbsp;&nbsp; double `getFocalLength`() const;  |
|  &nbsp;&nbsp; double `getFocalDistance`() const;  |
|  &nbsp;&nbsp; double `getMaxFocalDistance`() const;  |
|  &nbsp;&nbsp; double `getMinFocalDistance`() const;  |
|  &nbsp;&nbsp; virtual void `setFocalDistance`(double focalDistance);  |
|  &nbsp;&nbsp; int `getWidth`() const;  |
|  &nbsp;&nbsp; int `getHeight`() const;  |
|  &nbsp;&nbsp; double `getNear`() const;  |
|  &nbsp;&nbsp; double `getMaxRange`() const;  |
|  &nbsp;&nbsp; int `getType`() const;  |
|  &nbsp;&nbsp; const unsigned char *`getImage`() const;  |
|  &nbsp;&nbsp; static unsigned char `imageGetRed`(const unsigned char *image,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);  |
|  &nbsp;&nbsp; static unsigned char `imageGetGreen`(const unsigned char *image,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);  |
|  &nbsp;&nbsp; static unsigned char `imageGetBlue`(const unsigned char *image,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);  |
|  &nbsp;&nbsp; static unsigned char `imageGetGrey`(const unsigned char *image,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);  |
|  &nbsp;&nbsp; const float *`getRangeImage`() const;  |
|  &nbsp;&nbsp; static float `rangeImageGetDepth`(const float *image,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y);  |
|  &nbsp;&nbsp; int `saveImage`(const std::string &filename, int quality) const;  |
| };  |

| |
| --- |
| #include <webots/Compass.hpp>  |
|  class `Compass` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; const double *`getValues`() const;  |
| };  |

| |
| --- |
| #include <webots/Connector.hpp>  |
|  class `Connector` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enablePresence`(int ms);  |
|  &nbsp;&nbsp; virtual void `disablePresence`();  |
|  &nbsp;&nbsp; int `getPresence`() const;  |
|  &nbsp;&nbsp; virtual void `lock`();  |
|  &nbsp;&nbsp; virtual void `unlock`();  |
| };  |

| |
| --- |
| #include <webots/Device.hpp>  |
|  class `Device` {  |
|  &nbsp;&nbsp; const std::string &`getModel`() const;  |
|  &nbsp;&nbsp; const std::string &`getName`() const;  |
|  &nbsp;&nbsp; int `getNodeType`() const;  |
| };  |

| |
| --- |
| #include <webots/DifferentialWheels.hpp>  |
|  class `DifferentialWheels` : public `Robot` {  |
|  &nbsp;&nbsp; `DifferentialWheels`();  |
|  &nbsp;&nbsp; virtual `~DifferentialWheels`();  |
|  &nbsp;&nbsp; virtual void `setSpeed`(double left, double right);  |
|  &nbsp;&nbsp; double `getLeftSpeed`() const;  |
|  &nbsp;&nbsp; double `getRightSpeed`() const;  |
|  &nbsp;&nbsp; virtual void `enableEncoders`(int ms);  |
|  &nbsp;&nbsp; virtual void `disableEncoders`();  |
|  &nbsp;&nbsp; int `getEncodersSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getLeftEncoder`() const;  |
|  &nbsp;&nbsp; double `getRightEncoder`() const;  |
|  &nbsp;&nbsp; virtual void `setEncoders`(double left, double right);  |
|  &nbsp;&nbsp; double `getMaxSpeed`() const;  |
|  &nbsp;&nbsp; double `getSpeedUnit`() const;  |
| };  |

| |
| --- |
| #include <webots/Display.hpp>  |
|  class `Display` : public `Device` {  |
|  &nbsp;&nbsp; enum {RGB, RGBA, ARGB, BGRA};  |
|  &nbsp;&nbsp; int `getWidth`() const;  |
|  &nbsp;&nbsp; int `getHeight`() const;  |
|  &nbsp;&nbsp; virtual void `setColor`(int color);  |
|  &nbsp;&nbsp; virtual void `setAlpha`(double alpha);  |
|  &nbsp;&nbsp; virtual void `setOpacity`(double opacity);  |
|  &nbsp;&nbsp; virtual void `drawPixel`(int x1, int y1);  |
|  &nbsp;&nbsp; virtual void `drawLine`(int x1, int y1, int x2, int y2);  |
|  &nbsp;&nbsp; virtual void `drawRectangle`(int x, int y, int width, int height);  |
|  &nbsp;&nbsp; virtual void `drawOval`(int cx, int cy, int a, int b);  |
|  &nbsp;&nbsp; virtual void `drawPolygon`(const int *x, const int *y, int size);  |
|  &nbsp;&nbsp; virtual void `drawText`(const std::string &txt, int x, int y);  |
|  &nbsp;&nbsp; virtual void `fillRectangle`(int x, int y, int width, int height);  |
|  &nbsp;&nbsp; virtual void `fillOval`(int cx, int cy, int a, int b);  |
|  &nbsp;&nbsp; virtual void `fillPolygon`(const int *x, const int *y, int size);  |
|  &nbsp;&nbsp; `ImageRef` *`imageCopy`(int x, int y, int width, int height) const;  |
|  &nbsp;&nbsp; virtual void `imagePaste`(`ImageRef` *ir, int x, int y);  |
|  &nbsp;&nbsp; `ImageRef` *`imageLoad`(const std::string &filename) const;  |
|  &nbsp;&nbsp; `ImageRef` *`imageNew`(int width, int height, const void *data, int format) const;  |
|  &nbsp;&nbsp; void `imageSave`(`ImageRef` *ir, const std::string &filename) const;  |
|  &nbsp;&nbsp; void `imageDelete`(`ImageRef` *ir) const;  |
| };  |

| |
| --- |
| #include <webots/DistanceSensor.hpp>  |
|  class `DistanceSensor` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getValue`() const;  |
| };  |

| |
| --- |
| #include <webots/Emitter.hpp>  |
|  class `Emitter` : public `Device` {  |
|  &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};  |
|  &nbsp;&nbsp; virtual int `send`(const void *data, int size);  |
|  &nbsp;&nbsp; int `getChannel`() const;  |
|  &nbsp;&nbsp; virtual void `setChannel`(int channel);  |
|  &nbsp;&nbsp; double `getRange`() const;  |
|  &nbsp;&nbsp; virtual void `setRange`(double range);  |
|  &nbsp;&nbsp; int `getBufferSize`() const;  |
| };  |

| |
| --- |
| #include <webots/Field.hpp>  |
|  class Field {  |
|  &nbsp;&nbsp; enum { SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, MF\_STRING, MF\_NODE };  |
|  &nbsp;&nbsp; int `getType`() const;  |
|  &nbsp;&nbsp; std::string `getTypeName`() const;  |
|  &nbsp;&nbsp; int `getCount`() const;  |
|  &nbsp;&nbsp; bool `getSFBool`() const;  |
|  &nbsp;&nbsp; int `getSFInt32`() const;  |
|  &nbsp;&nbsp; double `getSFFloat`() const;  |
|  &nbsp;&nbsp; const double *`getSFVec2f`() const;  |
|  &nbsp;&nbsp; const double *`getSFVec3f`() const;  |
|  &nbsp;&nbsp; const double *`getSFRotation`() const;  |
|  &nbsp;&nbsp; const double *`getSFColor`() const;  |
|  &nbsp;&nbsp; std::string `getSFString`() const;  |
|  &nbsp;&nbsp; `Node` *`getSFNode`() const;  |
|  &nbsp;&nbsp; bool `getMFBool`(int index) const;  |
|  &nbsp;&nbsp; int `getMFInt32`(int index) const;  |
|  &nbsp;&nbsp; double `getMFFloat`(int index) const;  |
|  &nbsp;&nbsp; const double *`getMFVec2f`(int index) const;  |
|  &nbsp;&nbsp; const double *`getMFVec3f`(int index) const;  |
|  &nbsp;&nbsp; const double *`getMFRotation`(int index) const;  |
|  &nbsp;&nbsp; const double *`getMFColor`(int index) const;  |
|  &nbsp;&nbsp; std::string `getMFString`(int index) const;  |
|  &nbsp;&nbsp; `Node` *`getMFNode`(int index) const;  |
|  &nbsp;&nbsp; void `setSFBool`(bool value);  |
|  &nbsp;&nbsp; void `setSFInt32`(int value);  |
|  &nbsp;&nbsp; void `setSFFloat`(double value);  |
|  &nbsp;&nbsp; void `setSFVec2f`(const double values[2]);  |
|  &nbsp;&nbsp; void `setSFVec3f`(const double values[3]);  |
|  &nbsp;&nbsp; void `setSFRotation`(const double values[4]);  |
|  &nbsp;&nbsp; void `setSFColor`(const double values[3]);  |
|  &nbsp;&nbsp; void `setSFString`(const std::string &value);  |
|  &nbsp;&nbsp; void `setMFBool`(int index, bool value);  |
|  &nbsp;&nbsp; void `setMFInt32`(int index, int value);  |
|  &nbsp;&nbsp; void `setMFFloat`(int index, double value);  |
|  &nbsp;&nbsp; void `setMFVec2f`(int index, const double values[2]);  |
|  &nbsp;&nbsp; void `setMFVec3f`(int index, const double values[3]);  |
|  &nbsp;&nbsp; void `setMFRotation`(int index, const double values[4]);  |
|  &nbsp;&nbsp; void `setMFColor`(int index, const double values[3]);  |
|  &nbsp;&nbsp; void `setMFString`(int index, const std::string &value);  |
|  &nbsp;&nbsp; void `importMFNode`(int position, const std::string &filename);  |
|  &nbsp;&nbsp; void `importMFNodeFromString`(int position, const std::string &nodeString);  |
|  &nbsp;&nbsp; void `removeMFNode`(int position);  |
| };  |

| |
| --- |
| #include <webots/GPS.hpp>  |
|  class `GPS` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; const double *`getValues`() const;  |
| };  |

| |
| --- |
| #include <webots/Gyro.hpp>  |
|  class `Gyro` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; const double *`getValues`() const;  |
| };  |

| |
| --- |
| #include <webots/ImageRef.hpp>  |
|  class ImageRef {  |
| };  |

| |
| --- |
| #include <webots/InertialUnit.hpp>  |
|  class `InertialUnit` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; const double *`getRollPitchYaw`() const;  |
| };  |

| |
| --- |
| #include <webots/LED.hpp>  |
|  class `LED` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `set`(int value);  |
|  &nbsp;&nbsp; int `get`() const;  |
| };  |

| |
| --- |
| #include <webots/LightSensor.hpp>  |
|  class `LightSensor` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getValue`() const;  |
| };  |

| |
| --- |
| #include <webots/utils/Motion.hpp>  |
|  class `Motion` {  |
|  &nbsp;&nbsp; `Motion`(const std::string &fileName);  |
|  &nbsp;&nbsp; virtual `~Motion`();  |
|  &nbsp;&nbsp; bool `isValid`() const;  |
|  &nbsp;&nbsp; virtual void `play`();  |
|  &nbsp;&nbsp; virtual void `stop`();  |
|  &nbsp;&nbsp; virtual void `setLoop`(bool loop);  |
|  &nbsp;&nbsp; virtual void `setReverse`(bool reverse);  |
|  &nbsp;&nbsp; bool `isOver`() const;  |
|  &nbsp;&nbsp; int `getDuration`() const;  |
|  &nbsp;&nbsp; int `getTime`() const;  |
|  &nbsp;&nbsp; virtual void `setTime`(int time);  |
| };  |

| |
| --- |
| #include <webots/Motor.hpp>  |
|  class `Motor` : public `Device` {  |
|  &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};  |
|  &nbsp;&nbsp; virtual void `setPosition`(double position);  |
|  &nbsp;&nbsp; virtual void `setVelocity`(double vel);  |
|  &nbsp;&nbsp; virtual void `setAcceleration`(double force);  |
|  &nbsp;&nbsp; virtual void `setAvailableForce`(double motor\_force);  |
|  &nbsp;&nbsp; virtual void `setAvailableTorque`(double motor\_torque);  |
|  &nbsp;&nbsp; virtual void `setControlPID`(double p, double i, double d);  |
|  &nbsp;&nbsp; double `getTargetPosition`(double position) const;  |
|  &nbsp;&nbsp; double `getMinPosition`() const;  |
|  &nbsp;&nbsp; double `getMaxPosition`() const;  |
|  &nbsp;&nbsp; double `getVelocity`() const;  |
|  &nbsp;&nbsp; double `getMaxVelocity`() const;  |
|  &nbsp;&nbsp; double `getAcceleration`() const;  |
|  &nbsp;&nbsp; double `getAvailableForce`() const;  |
|  &nbsp;&nbsp; double `getMaxForce`() const;  |
|  &nbsp;&nbsp; double `getAvailableTorque`() const;  |
|  &nbsp;&nbsp; double `getMaxTorque`() const;  |
|  &nbsp;&nbsp; virtual void `enableForceFeedback`(int ms);  |
|  &nbsp;&nbsp; virtual void `disableForceFeedback`();  |
|  &nbsp;&nbsp; int `getForceFeedbackSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getForceFeedback`() const;  |
|  &nbsp;&nbsp; virtual void `setForce`(double force);  |
|  &nbsp;&nbsp; virtual void `enableTorqueFeedback`(int ms);  |
|  &nbsp;&nbsp; virtual void `disableTorqueFeedback`();  |
|  &nbsp;&nbsp; int `getTorqueFeedbackSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getTorqueFeedback`() const;  |
|  &nbsp;&nbsp; virtual void `setTorque`(double torque);  |
|  &nbsp;&nbsp; int `getType`() const;  |
| };  |

| |
| --- |
| #include <webots/Node.hpp>  |
|  class Node {  |
|  &nbsp;&nbsp; enum { NO\_NODE, APPEARANCE, BACKGROUND, BOX, COLOR, CONE,  |
|  &nbsp;&nbsp; COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT, ELEVATION\_GRID,  |
|  &nbsp;&nbsp; EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE, INDEXED\_FACE\_SET,  |
|  &nbsp;&nbsp; INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT, SHAPE, SPHERE,  |
|  &nbsp;&nbsp; SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM,  |
|  &nbsp;&nbsp; TRANSFORM, VIEWPOINT, WORLD\_INFO, CAPSULE, PLANE, ROBOT,  |
|  &nbsp;&nbsp; SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID, PHYSICS, CAMERA\_ZOOM,  |
|  &nbsp;&nbsp; CHARGER, DAMPING, CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE,  |
|  &nbsp;&nbsp; CAMERA, COMPASS, CONNECTOR, DISPLAY, DISTANCE\_SENSOR,  |
|  &nbsp;&nbsp; EMITTER, GPS,GYRO, LED, LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN,  |
|  &nbsp;&nbsp; POSITION\_SENSOR, RADIO, RECEIVER, SERVO, SPEAKER,  |
|  &nbsp;&nbsp; TOUCH\_SENSOR };  |
|  &nbsp;&nbsp; virtual void `remove`();  |
|  &nbsp;&nbsp; int `getId`() const;  |
|  &nbsp;&nbsp; int `getType`() const;  |
|  &nbsp;&nbsp; std::string `getTypeName`() const;  |
|  &nbsp;&nbsp; std::string `getBaseTypeName`() const;  |
|  &nbsp;&nbsp; Node *`getParentNode`() const;  |
|  &nbsp;&nbsp; `Field` *`getField`(const std::string &fieldName) const;  |
|  &nbsp;&nbsp; const double *`getPosition`() const;  |
|  &nbsp;&nbsp; const double *`getOrientation`() const;  |
|  &nbsp;&nbsp; const double *`getCenterOfMass`() const;  |
|  &nbsp;&nbsp; const double *`getContactPoint`(int index) const;  |
|  &nbsp;&nbsp; int `getNumberOfContactPoints`() const;  |
|  &nbsp;&nbsp; bool `getStaticBalance`() const;  |
|  &nbsp;&nbsp; const double * `getVelocity`() const;  |
|  &nbsp;&nbsp; void `setVelocity`(const double velocity[6]);  |
|  &nbsp;&nbsp; void `resetPhysics`();  |
| };  |

| |
| --- |
| #include <webots/Pen.hpp>  |
|  class `Pen` : public `Device` {  |
|  &nbsp;&nbsp; virtual void `write`(bool write);  |
|  &nbsp;&nbsp; virtual void `setInkColor`(int color, double density);  |
| };  |

| |
| --- |
| #include <webots/PositionSensor.hpp>  |
|  class `PositionSensor` : public `Device` {  |
|  &nbsp;&nbsp; enum {ANGULAR, LINEAR};  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getValue`() const;  |
|  &nbsp;&nbsp; int `getType`() const;  |
| };  |

| |
| --- |
| #include <webots/Receiver.hpp>  |
|  class `Receiver` : public `Device` {  |
|  &nbsp;&nbsp; enum {CHANNEL\_BROADCAST};  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; int `getQueueLength`() const;  |
|  &nbsp;&nbsp; virtual void `nextPacket`();  |
|  &nbsp;&nbsp; const void *`getData`() const;  |
|  &nbsp;&nbsp; int `getDataSize`() const;  |
|  &nbsp;&nbsp; double `getSignalStrength`() const;  |
|  &nbsp;&nbsp; const double *`getEmitterDirection`() const;  |
|  &nbsp;&nbsp; virtual void `setChannel`(int channel);  |
|  &nbsp;&nbsp; int `getChannel`() const;  |
| };  |

| |
| --- |
| #include <webots/Robot.hpp>  |
|  class `Robot` {  |
|  &nbsp;&nbsp; enum {MODE\_SIMULATION, MODE\_CROSS\_COMPILATION,  |
|  &nbsp;&nbsp; MODE\_REMOTE\_CONTROL};  |
|  &nbsp;&nbsp; enum {KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT,  |
|  &nbsp;&nbsp; KEYBOARD\_UP, KEYBOARD\_RIGHT, KEYBOARD\_DOWN,  |
|  &nbsp;&nbsp; KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT,  |
|  &nbsp;&nbsp; KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END,  |
|  &nbsp;&nbsp; KEYBOARD\_KEY, KEYBOARD\_SHIFT, KEYBOARD\_CONTROL,  |
|  &nbsp;&nbsp; KEYBOARD\_ALT};  |
|  &nbsp;&nbsp; `Robot`();  |
|  &nbsp;&nbsp; virtual `~Robot`();  |
|  &nbsp;&nbsp; virtual int `step`(int ms);  |
|  &nbsp;&nbsp; `Accelerometer` *`getAccelerometer`(const std::string &name);  |
|  &nbsp;&nbsp; `Brake` *`getBrake`(const std::string &name);  |
|  &nbsp;&nbsp; `Camera` *`getCamera`(const std::string &name);  |
|  &nbsp;&nbsp; `Compass` *`getCompass`(const std::string &name);  |
|  &nbsp;&nbsp; `Connector` *`getConnector`(const std::string &name);  |
|  &nbsp;&nbsp; `Display` *`getDisplay`(const std::string &name);  |
|  &nbsp;&nbsp; `DistanceSensor` *`getDistanceSensor`(const std::string &name);  |
|  &nbsp;&nbsp; `Emitter` *`getEmitter`(const std::string &name);  |
|  &nbsp;&nbsp; `GPS` *`getGPS`(const std::string &name);  |
|  &nbsp;&nbsp; `Gyro` *`getGyro`(const std::string &name);  |
|  &nbsp;&nbsp; `InertialUnit` *`getInertialUnit`(const std::string &name);  |
|  &nbsp;&nbsp; `LED` *`getLED`(const std::string &name);  |
|  &nbsp;&nbsp; `LightSensor` *`getLightSensor`(const std::string &name);  |
|  &nbsp;&nbsp; `Motor` *`getMotor`(const std::string &name);  |
|  &nbsp;&nbsp; `Pen` *`getPen`(const std::string &name);  |
|  &nbsp;&nbsp; `PositionSensor` *`getPositionSensor`(const std::string &name);  |
|  &nbsp;&nbsp; `Receiver` *`getReceiver`(const std::string &name);  |
|  &nbsp;&nbsp; `Servo` *`getServo`(const std::string &name);  |
|  &nbsp;&nbsp; `TouchSensor` *`getTouchSensor`(const std::string &name);  |
|  &nbsp;&nbsp; int `getNumberOfDevices`();  |
|  &nbsp;&nbsp; `Device` *`getDeviceByIndex`(int index);  |
|  &nbsp;&nbsp; virtual void `batterySensorEnable`(int ms);  |
|  &nbsp;&nbsp; virtual void `batterySensorDisable`();  |
|  &nbsp;&nbsp; int `batterySensorGetSamplingPeriod`();  |
|  &nbsp;&nbsp; double `batterySensorGetValue`() const;  |
|  &nbsp;&nbsp; double `getBasicTimeStep`() const;  |
|  &nbsp;&nbsp; int `getMode`() const;  |
|  &nbsp;&nbsp; std::string `getModel`() const;  |
|  &nbsp;&nbsp; std::string `getData`() const;  |
|  &nbsp;&nbsp; void `setData`(const std::string &data);  |
|  &nbsp;&nbsp; std::string `getName`() const;  |
|  &nbsp;&nbsp; std::string `getControllerName`() const;  |
|  &nbsp;&nbsp; std::string `getControllerArguments`() const;  |
|  &nbsp;&nbsp; std::string `getProjectPath`() const;  |
|  &nbsp;&nbsp; bool `getSynchronization`() const;  |
|  &nbsp;&nbsp; double `getTime`() const;  |
|  &nbsp;&nbsp; std::string `getWorldPath`() const;  |
|  &nbsp;&nbsp; virtual void `keyboardEnable`(int ms);  |
|  &nbsp;&nbsp; virtual void `keyboardDisable`();  |
|  &nbsp;&nbsp; int `keyboardGetKey`() const;  |
|  &nbsp;&nbsp; int `getType`() const;  |
|  &nbsp;&nbsp; void *`robotWindowCustomFunction`(void *arg);  |
| };  |

| |
| --- |
| #include <webots/Servo.hpp>  |
|  class `Servo` : public `Device` {  |
|  &nbsp;&nbsp; enum {ROTATIONAL, LINEAR};  |
|  &nbsp;&nbsp; virtual void `setPosition`(double position);  |
|  &nbsp;&nbsp; virtual void `setVelocity`(double vel);  |
|  &nbsp;&nbsp; virtual void `setAcceleration`(double force);  |
|  &nbsp;&nbsp; virtual void `setMotorForce`(double motor\_force);  |
|  &nbsp;&nbsp; virtual void `setControlP`(double p);  |
|  &nbsp;&nbsp; double `getTargetPosition`(double position) const;  |
|  &nbsp;&nbsp; double `getMinPosition`() const;  |
|  &nbsp;&nbsp; double `getMaxPosition`() const;  |
|  &nbsp;&nbsp; virtual void `enablePosition`(int ms);  |
|  &nbsp;&nbsp; virtual void `disablePosition`();  |
|  &nbsp;&nbsp; int `getPositionSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getPosition`() const;  |
|  &nbsp;&nbsp; virtual void `enableMotorForceFeedback`(int ms);  |
|  &nbsp;&nbsp; virtual void `disableMotorForceFeedback`();  |
|  &nbsp;&nbsp; int `getMotorForceFeedbackSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getMotorForceFeedback`() const;  |
|  &nbsp;&nbsp; virtual void `setForce`(double force);  |
|  &nbsp;&nbsp; int `getType`() const;  |
| };  |

| |
| --- |
| #include <webots/Supervisor.hpp>  |
|  class `Supervisor` : public `Robot` {  |
|  &nbsp;&nbsp; enum {MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR};  |
|  &nbsp;&nbsp; `Supervisor`();  |
|  &nbsp;&nbsp; virtual `~Supervisor`();  |
|  &nbsp;&nbsp; void `exportImage`(const std::string &file, int quality) const;  |
|  &nbsp;&nbsp; `Node` *`getRoot`();  |
|  &nbsp;&nbsp; `Node` *`getSelf`();  |
|  &nbsp;&nbsp; `Node` *`getFromDef`(const std::string &name);  |
|  &nbsp;&nbsp; `Node` *`getFromId`(int id);  |
|  &nbsp;&nbsp; virtual void `setLabel`(int id, const std::string &label, double xpos, double ypos,  |
|  &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency);  |
|  &nbsp;&nbsp; virtual void `simulationQuit`(int status);  |
|  &nbsp;&nbsp; virtual void `simulationRevert`();  |
|  &nbsp;&nbsp; virtual void `simulationResetPhysics`();  |
|  &nbsp;&nbsp; virtual void `loadWorld`(const std::string &file);  |
|  &nbsp;&nbsp; virtual void `saveWorld`();  |
|  &nbsp;&nbsp; virtual void `saveWorld`(const std::string &file);  |
|  &nbsp;&nbsp; virtual void `movieStartRecording`(const std::string &file, int width, int height, int codec, int quality,  |
|  &nbsp;&nbsp; int acceleration, bool caption) const;  |
|  &nbsp;&nbsp; virtual void `movieStopRecording`();  |
|  &nbsp;&nbsp; int `movieGetStatus`() const;  |
|  &nbsp;&nbsp; virtual bool `animationStartRecording`(const std::string &file);  |
|  &nbsp;&nbsp; virtual bool `animationStopRecording`();  |
| };  |

| |
| --- |
| #include <webots/TouchSensor.hpp>  |
|  class `TouchSensor` : public `Device` {  |
|  &nbsp;&nbsp; enum {BUMPER, FORCE, FORCE3D};  |
|  &nbsp;&nbsp; virtual void `enable`(int ms);  |
|  &nbsp;&nbsp; virtual void `disable`();  |
|  &nbsp;&nbsp; int `getSamplingPeriod`();  |
|  &nbsp;&nbsp; double `getValue`() const;  |
|  &nbsp;&nbsp; const double *`getValues`() const;  |
|  &nbsp;&nbsp; int `getType`() const;  |
| };  |

