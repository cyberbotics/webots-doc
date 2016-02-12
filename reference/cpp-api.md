## C++ API

The following tables describe the C++ classes and their methods.

| |
| --- |
| #include `<`webots/Accelerometer.hpp`>` |
| class [Accelerometer](accelerometer.md#accelerometer) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](accelerometer.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](accelerometer.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](accelerometer.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](accelerometer.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Brake.hpp`>` |
| class [Brake](brake.md#brake) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; void [setDampingConstant](brake.md#description)(double dampingConstant) const; |
| &nbsp;&nbsp; int [getType](brake.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Camera.hpp`>` |
| class [Camera](camera.md#camera) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {COLOR, RANGE\_FINDER, BOTH}; |
| &nbsp;&nbsp; virtual void [enable](camera.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](camera.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](camera.md#description)(); |
| &nbsp;&nbsp; double [getFov](camera.md#description)() const; |
| &nbsp;&nbsp; double [getMinFov](camera.md#description)() const; |
| &nbsp;&nbsp; double [getMaxFov](camera.md#description)() const; |
| &nbsp;&nbsp; virtual void [setFov](camera.md#description)(double fov); |
| &nbsp;&nbsp; double [getFocalLength](camera.md#description)() const; |
| &nbsp;&nbsp; double [getFocalDistance](camera.md#description)() const; |
| &nbsp;&nbsp; double [getMaxFocalDistance](camera.md#description)() const; |
| &nbsp;&nbsp; double [getMinFocalDistance](camera.md#description)() const; |
| &nbsp;&nbsp; virtual void [setFocalDistance](camera.md#description)(double focalDistance); |
| &nbsp;&nbsp; int [getWidth](camera.md#description)() const; |
| &nbsp;&nbsp; int [getHeight](camera.md#description)() const; |
| &nbsp;&nbsp; double [getNear](camera.md#description)() const; |
| &nbsp;&nbsp; double [getMaxRange](camera.md#description)() const; |
| &nbsp;&nbsp; int [getType](camera.md#description)() const; |
| &nbsp;&nbsp; const unsigned char *[getImage](camera.md#description)() const; |
| &nbsp;&nbsp; static unsigned char [imageGetRed](camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; static unsigned char [imageGetGreen](camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; static unsigned char [imageGetBlue](camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; static unsigned char [imageGetGrey](camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; const float *[getRangeImage](camera.md#description)() const; |
| &nbsp;&nbsp; static float [rangeImageGetDepth](camera.md#description)(const float *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; int [saveImage](camera.md#description)(const std::string &filename, int quality) const; |
| }; |

| |
| --- |
| #include `<`webots/Compass.hpp`>` |
| class [Compass](compass.md#compass) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](compass.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](compass.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](compass.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](compass.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Connector.hpp`>` |
| class [Connector](connector.md#connector) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enablePresence](connector.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disablePresence](connector.md#description)(); |
| &nbsp;&nbsp; int [getPresence](connector.md#description)() const; |
| &nbsp;&nbsp; virtual void [lock](connector.md#description)(); |
| &nbsp;&nbsp; virtual void [unlock](connector.md#description)(); |
| }; |

| |
| --- |
| #include `<`webots/Device.hpp`>` |
| class [Device](device.md#device) { |
| &nbsp;&nbsp; const std::string &[getModel](device.md#description)() const; |
| &nbsp;&nbsp; const std::string &[getName](device.md#description)() const; |
| &nbsp;&nbsp; int [getNodeType](device.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/DifferentialWheels.hpp`>` |
| class [DifferentialWheels](differentialwheels.md#differentialwheels) : public [Robot](cpp-api.md) { |
| &nbsp;&nbsp; [DifferentialWheels](robot.md#description)(); |
| &nbsp;&nbsp; virtual [~DifferentialWheels](robot.md#description)(); |
| &nbsp;&nbsp; virtual void [setSpeed](differentialwheels.md#description)(double left, double right); |
| &nbsp;&nbsp; double [getLeftSpeed](differentialwheels.md#description)() const; |
| &nbsp;&nbsp; double [getRightSpeed](differentialwheels.md#description)() const; |
| &nbsp;&nbsp; virtual void [enableEncoders](differentialwheels.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableEncoders](differentialwheels.md#description)(); |
| &nbsp;&nbsp; int [getEncodersSamplingPeriod](differentialwheels.md#description)(); |
| &nbsp;&nbsp; double [getLeftEncoder](differentialwheels.md#description)() const; |
| &nbsp;&nbsp; double [getRightEncoder](differentialwheels.md#description)() const; |
| &nbsp;&nbsp; virtual void [setEncoders](differentialwheels.md#description)(double left, double right); |
| &nbsp;&nbsp; double [getMaxSpeed](differentialwheels.md#description)() const; |
| &nbsp;&nbsp; double [getSpeedUnit](differentialwheels.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Display.hpp`>` |
| class [Display](display.md#display) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {RGB, RGBA, ARGB, BGRA}; |
| &nbsp;&nbsp; int [getWidth](display.md#description)() const; |
| &nbsp;&nbsp; int [getHeight](display.md#description)() const; |
| &nbsp;&nbsp; virtual void [setColor](display.md#description)(int color); |
| &nbsp;&nbsp; virtual void [setAlpha](display.md#description)(double alpha); |
| &nbsp;&nbsp; virtual void [setOpacity](display.md#description)(double opacity); |
| &nbsp;&nbsp; virtual void [drawPixel](display.md#description)(int x1, int y1); |
| &nbsp;&nbsp; virtual void [drawLine](display.md#description)(int x1, int y1, int x2, int y2); |
| &nbsp;&nbsp; virtual void [drawRectangle](display.md#description)(int x, int y, int width, int height); |
| &nbsp;&nbsp; virtual void [drawOval](display.md#description)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; virtual void [drawPolygon](display.md#description)(const int *x, const int *y, int size); |
| &nbsp;&nbsp; virtual void [drawText](display.md#description)(const std::string &txt, int x, int y); |
| &nbsp;&nbsp; virtual void [fillRectangle](display.md#description)(int x, int y, int width, int height); |
| &nbsp;&nbsp; virtual void [fillOval](display.md#description)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; virtual void [fillPolygon](display.md#description)(const int *x, const int *y, int size); |
| &nbsp;&nbsp; [ImageRef](cpp-api.md) *[imageCopy](display.md#description)(int x, int y, int width, int height) const; |
| &nbsp;&nbsp; virtual void [imagePaste](display.md#description)([ImageRef](cpp-api.md) *ir, int x, int y); |
| &nbsp;&nbsp; [ImageRef](cpp-api.md) *[imageLoad](display.md#description)(const std::string &filename) const; |
| &nbsp;&nbsp; [ImageRef](cpp-api.md) *[imageNew](display.md#description)(int width, int height, const void *data, int format) const; |
| &nbsp;&nbsp; void [imageSave](display.md#description)([ImageRef](cpp-api.md) *ir, const std::string &filename) const; |
| &nbsp;&nbsp; void [imageDelete](display.md#description)([ImageRef](cpp-api.md) *ir) const; |
| }; |

| |
| --- |
| #include `<`webots/DistanceSensor.hpp`>` |
| class [DistanceSensor](distancesensor.md#distancesensor) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](distancesensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](distancesensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](distancesensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](distancesensor.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Emitter.hpp`>` |
| class [Emitter](emitter.md#emitter) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST}; |
| &nbsp;&nbsp; virtual int [send](emitter.md#description)(const void *data, int size); |
| &nbsp;&nbsp; int [getChannel](emitter.md#description)() const; |
| &nbsp;&nbsp; virtual void [setChannel](emitter.md#description)(int channel); |
| &nbsp;&nbsp; double [getRange](emitter.md#description)() const; |
| &nbsp;&nbsp; virtual void [setRange](emitter.md#description)(double range); |
| &nbsp;&nbsp; int [getBufferSize](emitter.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Field.hpp`>` |
| class Field { |
| &nbsp;&nbsp; enum { SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, MF\_STRING, MF\_NODE }; |
| &nbsp;&nbsp; int [getType](supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getTypeName](supervisor.md#description)() const; |
| &nbsp;&nbsp; int [getCount](supervisor.md#description)() const; |
| &nbsp;&nbsp; bool [getSFBool](supervisor.md#description)() const; |
| &nbsp;&nbsp; int [getSFInt32](supervisor.md#description)() const; |
| &nbsp;&nbsp; double [getSFFloat](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFVec2f](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFVec3f](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFRotation](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFColor](supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getSFString](supervisor.md#description)() const; |
| &nbsp;&nbsp; [Node](cpp-api.md) *[getSFNode](supervisor.md#description)() const; |
| &nbsp;&nbsp; bool [getMFBool](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; int [getMFInt32](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; double [getMFFloat](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFVec2f](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFVec3f](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFRotation](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFColor](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; std::string [getMFString](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; [Node](cpp-api.md) *[getMFNode](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; void [setSFBool](supervisor.md#description)(bool value); |
| &nbsp;&nbsp; void [setSFInt32](supervisor.md#description)(int value); |
| &nbsp;&nbsp; void [setSFFloat](supervisor.md#description)(double value); |
| &nbsp;&nbsp; void [setSFVec2f](supervisor.md#description)(const double values[2]); |
| &nbsp;&nbsp; void [setSFVec3f](supervisor.md#description)(const double values[3]); |
| &nbsp;&nbsp; void [setSFRotation](supervisor.md#description)(const double values[4]); |
| &nbsp;&nbsp; void [setSFColor](supervisor.md#description)(const double values[3]); |
| &nbsp;&nbsp; void [setSFString](supervisor.md#description)(const std::string &value); |
| &nbsp;&nbsp; void [setMFBool](supervisor.md#description)(int index, bool value); |
| &nbsp;&nbsp; void [setMFInt32](supervisor.md#description)(int index, int value); |
| &nbsp;&nbsp; void [setMFFloat](supervisor.md#description)(int index, double value); |
| &nbsp;&nbsp; void [setMFVec2f](supervisor.md#description)(int index, const double values[2]); |
| &nbsp;&nbsp; void [setMFVec3f](supervisor.md#description)(int index, const double values[3]); |
| &nbsp;&nbsp; void [setMFRotation](supervisor.md#description)(int index, const double values[4]); |
| &nbsp;&nbsp; void [setMFColor](supervisor.md#description)(int index, const double values[3]); |
| &nbsp;&nbsp; void [setMFString](supervisor.md#description)(int index, const std::string &value); |
| &nbsp;&nbsp; void [importMFNode](supervisor.md#description)(int position, const std::string &filename); |
| &nbsp;&nbsp; void [importMFNodeFromString](supervisor.md#description)(int position, const std::string &nodeString); |
| &nbsp;&nbsp; void [removeMFNode](supervisor.md#description)(int position); |
| }; |

| |
| --- |
| #include `<`webots/GPS.hpp`>` |
| class [GPS](gps.md#gps) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](gps.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](gps.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](gps.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](gps.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Gyro.hpp`>` |
| class [Gyro](gyro.md#gyro) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](gyro.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](gyro.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](gyro.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](gyro.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/ImageRef.hpp`>` |
| class ImageRef { |
| }; |

| |
| --- |
| #include `<`webots/InertialUnit.hpp`>` |
| class [InertialUnit](inertialunit.md#inertialunit) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](inertialunit.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](inertialunit.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](inertialunit.md#description)(); |
| &nbsp;&nbsp; const double *[getRollPitchYaw](inertialunit.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/LED.hpp`>` |
| class [LED](led.md#led) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [set](led.md#description)(int value); |
| &nbsp;&nbsp; int [get](led.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/LightSensor.hpp`>` |
| class [LightSensor](lightsensor.md#lightsensor) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](lightsensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](lightsensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](lightsensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](lightsensor.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/utils/Motion.hpp`>` |
| class [Motion](motion.md#motion) { |
| &nbsp;&nbsp; [Motion](motion.md#description)(const std::string &fileName); |
| &nbsp;&nbsp; virtual [~Motion](motion.md#description)(); |
| &nbsp;&nbsp; bool [isValid](motion.md#description)() const; |
| &nbsp;&nbsp; virtual void [play](motion.md#description)(); |
| &nbsp;&nbsp; virtual void [stop](motion.md#description)(); |
| &nbsp;&nbsp; virtual void [setLoop](motion.md#description)(bool loop); |
| &nbsp;&nbsp; virtual void [setReverse](motion.md#description)(bool reverse); |
| &nbsp;&nbsp; bool [isOver](motion.md#description)() const; |
| &nbsp;&nbsp; int [getDuration](motion.md#description)() const; |
| &nbsp;&nbsp; int [getTime](motion.md#description)() const; |
| &nbsp;&nbsp; virtual void [setTime](motion.md#description)(int time); |
| }; |

| |
| --- |
| #include `<`webots/Motor.hpp`>` |
| class [Motor](motor.md#motor) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR}; |
| &nbsp;&nbsp; virtual void [setPosition](motor.md#description)(double position); |
| &nbsp;&nbsp; virtual void [setVelocity](motor.md#description)(double vel); |
| &nbsp;&nbsp; virtual void [setAcceleration](motor.md#description)(double force); |
| &nbsp;&nbsp; virtual void [setAvailableForce](motor.md#description)(double motor\_force); |
| &nbsp;&nbsp; virtual void [setAvailableTorque](motor.md#description)(double motor\_torque); |
| &nbsp;&nbsp; virtual void [setControlPID](motor.md#description)(double p, double i, double d); |
| &nbsp;&nbsp; double [getTargetPosition](motor.md#description)(double position) const; |
| &nbsp;&nbsp; double [getMinPosition](motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxPosition](motor.md#description)() const; |
| &nbsp;&nbsp; double [getVelocity](motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxVelocity](motor.md#description)() const; |
| &nbsp;&nbsp; double [getAcceleration](motor.md#description)() const; |
| &nbsp;&nbsp; double [getAvailableForce](motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxForce](motor.md#description)() const; |
| &nbsp;&nbsp; double [getAvailableTorque](motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxTorque](motor.md#description)() const; |
| &nbsp;&nbsp; virtual void [enableForceFeedback](motor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableForceFeedback](motor.md#description)(); |
| &nbsp;&nbsp; int [getForceFeedbackSamplingPeriod](motor.md#description)(); |
| &nbsp;&nbsp; double [getForceFeedback](motor.md#description)() const; |
| &nbsp;&nbsp; virtual void [setForce](motor.md#description)(double force); |
| &nbsp;&nbsp; virtual void [enableTorqueFeedback](motor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableTorqueFeedback](motor.md#description)(); |
| &nbsp;&nbsp; int [getTorqueFeedbackSamplingPeriod](motor.md#description)(); |
| &nbsp;&nbsp; double [getTorqueFeedback](motor.md#description)() const; |
| &nbsp;&nbsp; virtual void [setTorque](motor.md#description)(double torque); |
| &nbsp;&nbsp; int [getType](motor.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Node.hpp`>` |
| class Node { |
| &nbsp;&nbsp; enum { NO\_NODE, APPEARANCE, BACKGROUND, BOX, COLOR, CONE, |
| &nbsp;&nbsp; COORDINATE, CYLINDER, DIRECTIONAL\_LIGHT, ELEVATION\_GRID, |
| &nbsp;&nbsp; EXTRUSION, FOG, GROUP, IMAGE\_TEXTURE, INDEXED\_FACE\_SET, |
| &nbsp;&nbsp; INDEXED\_LINE\_SET, MATERIAL, POINT\_LIGHT, SHAPE, SPHERE, |
| &nbsp;&nbsp; SPOT\_LIGHT, SWITCH, TEXTURE\_COORDINATE, TEXTURE\_TRANSFORM, |
| &nbsp;&nbsp; TRANSFORM, VIEWPOINT, WORLD\_INFO, CAPSULE, PLANE, ROBOT, |
| &nbsp;&nbsp; SUPERVISOR, DIFFERENTIAL\_WHEELS, SOLID, PHYSICS, CAMERA\_ZOOM, |
| &nbsp;&nbsp; CHARGER, DAMPING, CONTACT\_PROPERTIES, ACCELEROMETER, BRAKE, |
| &nbsp;&nbsp; CAMERA, COMPASS, CONNECTOR, DISPLAY, DISTANCE\_SENSOR, |
| &nbsp;&nbsp; EMITTER, GPS,GYRO, LED, LIGHT\_SENSOR, MICROPHONE, MOTOR, PEN, |
| &nbsp;&nbsp; POSITION\_SENSOR, RADIO, RECEIVER, SERVO, SPEAKER, |
| &nbsp;&nbsp; TOUCH\_SENSOR }; |
| &nbsp;&nbsp; virtual void [remove](supervisor.md#description)(); |
| &nbsp;&nbsp; int [getId](supervisor.md#description)() const; |
| &nbsp;&nbsp; int [getType](supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getTypeName](supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getBaseTypeName](supervisor.md#description)() const; |
| &nbsp;&nbsp; Node *[getParentNode](supervisor.md#description)() const; |
| &nbsp;&nbsp; [Field](cpp-api.md) *[getField](supervisor.md#description)(const std::string &fieldName) const; |
| &nbsp;&nbsp; const double *[getPosition](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getOrientation](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getCenterOfMass](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getContactPoint](supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; int [getNumberOfContactPoints](supervisor.md#description)() const; |
| &nbsp;&nbsp; bool [getStaticBalance](supervisor.md#description)() const; |
| &nbsp;&nbsp; const double * [getVelocity](supervisor.md#description)() const; |
| &nbsp;&nbsp; void [setVelocity](supervisor.md#description)(const double velocity[6]); |
| &nbsp;&nbsp; void [resetPhysics](supervisor.md#description)(); |
| }; |

| |
| --- |
| #include `<`webots/Pen.hpp`>` |
| class [Pen](pen.md#pen) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; virtual void [write](pen.md#description)(bool write); |
| &nbsp;&nbsp; virtual void [setInkColor](pen.md#description)(int color, double density); |
| }; |

| |
| --- |
| #include `<`webots/PositionSensor.hpp`>` |
| class [PositionSensor](positionsensor.md#positionsensor) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {ANGULAR, LINEAR}; |
| &nbsp;&nbsp; virtual void [enable](positionsensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](positionsensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](positionsensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](positionsensor.md#description)() const; |
| &nbsp;&nbsp; int [getType](positionsensor.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Receiver.hpp`>` |
| class [Receiver](receiver.md#receiver) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST}; |
| &nbsp;&nbsp; virtual void [enable](receiver.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](receiver.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](receiver.md#description)(); |
| &nbsp;&nbsp; int [getQueueLength](receiver.md#description)() const; |
| &nbsp;&nbsp; virtual void [nextPacket](receiver.md#description)(); |
| &nbsp;&nbsp; const void *[getData](receiver.md#description)() const; |
| &nbsp;&nbsp; int [getDataSize](receiver.md#description)() const; |
| &nbsp;&nbsp; double [getSignalStrength](receiver.md#description)() const; |
| &nbsp;&nbsp; const double *[getEmitterDirection](receiver.md#description)() const; |
| &nbsp;&nbsp; virtual void [setChannel](receiver.md#description)(int channel); |
| &nbsp;&nbsp; int [getChannel](receiver.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Robot.hpp`>` |
| class [Robot](robot.md#robot) { |
| &nbsp;&nbsp; enum {MODE\_SIMULATION, MODE\_CROSS\_COMPILATION, |
| &nbsp;&nbsp; MODE\_REMOTE\_CONTROL}; |
| &nbsp;&nbsp; enum {KEYBOARD\_END, KEYBOARD\_HOME, KEYBOARD\_LEFT, |
| &nbsp;&nbsp; KEYBOARD\_UP, KEYBOARD\_RIGHT, KEYBOARD\_DOWN, |
| &nbsp;&nbsp; KEYBOARD\_PAGEUP, KEYBOARD\_PAGEDOWN, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_HOME, KEYBOARD\_NUMPAD\_LEFT, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_UP, KEYBOARD\_NUMPAD\_RIGHT, |
| &nbsp;&nbsp; KEYBOARD\_NUMPAD\_DOWN, KEYBOARD\_NUMPAD\_END, |
| &nbsp;&nbsp; KEYBOARD\_KEY, KEYBOARD\_SHIFT, KEYBOARD\_CONTROL, |
| &nbsp;&nbsp; KEYBOARD\_ALT}; |
| &nbsp;&nbsp; [Robot](robot.md#description)(); |
| &nbsp;&nbsp; virtual [~Robot](robot.md#description)(); |
| &nbsp;&nbsp; virtual int [step](robot.md#description)(int ms); |
| &nbsp;&nbsp; [Accelerometer](cpp-api.md) *[getAccelerometer](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Brake](cpp-api.md) *[getBrake](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Camera](cpp-api.md) *[getCamera](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Compass](cpp-api.md) *[getCompass](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Connector](cpp-api.md) *[getConnector](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Display](cpp-api.md) *[getDisplay](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [DistanceSensor](cpp-api.md) *[getDistanceSensor](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Emitter](cpp-api.md) *[getEmitter](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [GPS](cpp-api.md) *[getGPS](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Gyro](cpp-api.md) *[getGyro](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [InertialUnit](cpp-api.md) *[getInertialUnit](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [LED](cpp-api.md) *[getLED](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [LightSensor](cpp-api.md) *[getLightSensor](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Motor](cpp-api.md) *[getMotor](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Pen](cpp-api.md) *[getPen](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [PositionSensor](cpp-api.md) *[getPositionSensor](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Receiver](cpp-api.md) *[getReceiver](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Servo](cpp-api.md) *[getServo](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [TouchSensor](cpp-api.md) *[getTouchSensor](robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; int [getNumberOfDevices](robot.md#description)(); |
| &nbsp;&nbsp; [Device](cpp-api.md) *[getDeviceByIndex](robot.md#description)(int index); |
| &nbsp;&nbsp; virtual void [batterySensorEnable](robot.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [batterySensorDisable](robot.md#description)(); |
| &nbsp;&nbsp; int [batterySensorGetSamplingPeriod](robot.md#description)(); |
| &nbsp;&nbsp; double [batterySensorGetValue](robot.md#description)() const; |
| &nbsp;&nbsp; double [getBasicTimeStep](robot.md#description)() const; |
| &nbsp;&nbsp; int [getMode](robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getModel](robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getData](robot.md#description)() const; |
| &nbsp;&nbsp; void [setData](robot.md#description)(const std::string &data); |
| &nbsp;&nbsp; std::string [getName](robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getControllerName](robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getControllerArguments](robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getProjectPath](robot.md#description)() const; |
| &nbsp;&nbsp; bool [getSynchronization](robot.md#description)() const; |
| &nbsp;&nbsp; double [getTime](robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getWorldPath](robot.md#description)() const; |
| &nbsp;&nbsp; virtual void [keyboardEnable](robot.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [keyboardDisable](robot.md#description)(); |
| &nbsp;&nbsp; int [keyboardGetKey](robot.md#description)() const; |
| &nbsp;&nbsp; int [getType](robot.md#description)() const; |
| &nbsp;&nbsp; void *[robotWindowCustomFunction](robot.md#description)(void *arg); |
| }; |

| |
| --- |
| #include `<`webots/Servo.hpp`>` |
| class [Servo](servo.md#servo) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR}; |
| &nbsp;&nbsp; virtual void [setPosition](servo.md#description)(double position); |
| &nbsp;&nbsp; virtual void [setVelocity](servo.md#description)(double vel); |
| &nbsp;&nbsp; virtual void [setAcceleration](servo.md#description)(double force); |
| &nbsp;&nbsp; virtual void [setMotorForce](servo.md#description)(double motor\_force); |
| &nbsp;&nbsp; virtual void [setControlP](servo.md#description)(double p); |
| &nbsp;&nbsp; double [getTargetPosition](servo.md#description)(double position) const; |
| &nbsp;&nbsp; double [getMinPosition](servo.md#description)() const; |
| &nbsp;&nbsp; double [getMaxPosition](servo.md#description)() const; |
| &nbsp;&nbsp; virtual void [enablePosition](servo.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disablePosition](servo.md#description)(); |
| &nbsp;&nbsp; int [getPositionSamplingPeriod](servo.md#description)(); |
| &nbsp;&nbsp; double [getPosition](servo.md#description)() const; |
| &nbsp;&nbsp; virtual void [enableMotorForceFeedback](servo.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableMotorForceFeedback](servo.md#description)(); |
| &nbsp;&nbsp; int [getMotorForceFeedbackSamplingPeriod](servo.md#description)(); |
| &nbsp;&nbsp; double [getMotorForceFeedback](servo.md#description)() const; |
| &nbsp;&nbsp; virtual void [setForce](servo.md#description)(double force); |
| &nbsp;&nbsp; int [getType](servo.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Supervisor.hpp`>` |
| class [Supervisor](supervisor.md#supervisor) : public [Robot](cpp-api.md) { |
| &nbsp;&nbsp; enum {MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR}; |
| &nbsp;&nbsp; [Supervisor](robot.md#description)(); |
| &nbsp;&nbsp; virtual [~Supervisor](robot.md#description)(); |
| &nbsp;&nbsp; void [exportImage](supervisor.md#description)(const std::string &file, int quality) const; |
| &nbsp;&nbsp; [Node](cpp-api.md) *[getRoot](supervisor.md#description)(); |
| &nbsp;&nbsp; [Node](cpp-api.md) *[getSelf](supervisor.md#description)(); |
| &nbsp;&nbsp; [Node](cpp-api.md) *[getFromDef](supervisor.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Node](cpp-api.md) *[getFromId](supervisor.md#description)(int id); |
| &nbsp;&nbsp; virtual void [setLabel](supervisor.md#description)(int id, const std::string &label, double xpos, double ypos, |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency); |
| &nbsp;&nbsp; virtual void [simulationQuit](supervisor.md#description)(int status); |
| &nbsp;&nbsp; virtual void [simulationRevert](supervisor.md#description)(); |
| &nbsp;&nbsp; virtual void [simulationResetPhysics](supervisor.md#description)(); |
| &nbsp;&nbsp; virtual void [loadWorld](supervisor.md#description)(const std::string &file); |
| &nbsp;&nbsp; virtual void [saveWorld](supervisor.md#description)(); |
| &nbsp;&nbsp; virtual void [saveWorld](supervisor.md#description)(const std::string &file); |
| &nbsp;&nbsp; virtual void [movieStartRecording](supervisor.md#description)(const std::string &file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp; int acceleration, bool caption) const; |
| &nbsp;&nbsp; virtual void [movieStopRecording](supervisor.md#description)(); |
| &nbsp;&nbsp; int [movieGetStatus](supervisor.md#description)() const; |
| &nbsp;&nbsp; virtual bool [animationStartRecording](supervisor.md#description)(const std::string &file); |
| &nbsp;&nbsp; virtual bool [animationStopRecording](supervisor.md#description)(); |
| }; |

| |
| --- |
| #include `<`webots/TouchSensor.hpp`>` |
| class [TouchSensor](touchsensor.md#touchsensor) : public [Device](cpp-api.md) { |
| &nbsp;&nbsp; enum {BUMPER, FORCE, FORCE3D}; |
| &nbsp;&nbsp; virtual void [enable](touchsensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](touchsensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](touchsensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](touchsensor.md#description)() const; |
| &nbsp;&nbsp; const double *[getValues](touchsensor.md#description)() const; |
| &nbsp;&nbsp; int [getType](touchsensor.md#description)() const; |
| }; |

