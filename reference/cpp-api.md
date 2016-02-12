## C++ API

The following tables describe the C++ classes and their methods.

| |
| --- |
| #include `<`webots/Accelerometer.hpp`>` |
| class [Accelerometer](reference/accelerometer.md#accelerometer) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](reference/accelerometer.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/accelerometer.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/accelerometer.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](reference/accelerometer.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Brake.hpp`>` |
| class [Brake](reference/brake.md#brake) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; void [setDampingConstant](reference/brake.md#description)(double dampingConstant) const; |
| &nbsp;&nbsp; int [getType](reference/brake.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Camera.hpp`>` |
| class [Camera](reference/camera.md#camera) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {COLOR, RANGE\_FINDER, BOTH}; |
| &nbsp;&nbsp; virtual void [enable](reference/camera.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/camera.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/camera.md#description)(); |
| &nbsp;&nbsp; double [getFov](reference/camera.md#description)() const; |
| &nbsp;&nbsp; double [getMinFov](reference/camera.md#description)() const; |
| &nbsp;&nbsp; double [getMaxFov](reference/camera.md#description)() const; |
| &nbsp;&nbsp; virtual void [setFov](reference/camera.md#description)(double fov); |
| &nbsp;&nbsp; double [getFocalLength](reference/camera.md#description)() const; |
| &nbsp;&nbsp; double [getFocalDistance](reference/camera.md#description)() const; |
| &nbsp;&nbsp; double [getMaxFocalDistance](reference/camera.md#description)() const; |
| &nbsp;&nbsp; double [getMinFocalDistance](reference/camera.md#description)() const; |
| &nbsp;&nbsp; virtual void [setFocalDistance](reference/camera.md#description)(double focalDistance); |
| &nbsp;&nbsp; int [getWidth](reference/camera.md#description)() const; |
| &nbsp;&nbsp; int [getHeight](reference/camera.md#description)() const; |
| &nbsp;&nbsp; double [getNear](reference/camera.md#description)() const; |
| &nbsp;&nbsp; double [getMaxRange](reference/camera.md#description)() const; |
| &nbsp;&nbsp; int [getType](reference/camera.md#description)() const; |
| &nbsp;&nbsp; const unsigned char *[getImage](reference/camera.md#description)() const; |
| &nbsp;&nbsp; static unsigned char [imageGetRed](reference/camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; static unsigned char [imageGetGreen](reference/camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; static unsigned char [imageGetBlue](reference/camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; static unsigned char [imageGetGrey](reference/camera.md#description)(const unsigned char *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; const float *[getRangeImage](reference/camera.md#description)() const; |
| &nbsp;&nbsp; static float [rangeImageGetDepth](reference/camera.md#description)(const float *image, |
| &nbsp;&nbsp;&nbsp;&nbsp; int width, int x, int y); |
| &nbsp;&nbsp; int [saveImage](reference/camera.md#description)(const std::string &filename, int quality) const; |
| }; |

| |
| --- |
| #include `<`webots/Compass.hpp`>` |
| class [Compass](reference/compass.md#compass) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](reference/compass.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/compass.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/compass.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](reference/compass.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Connector.hpp`>` |
| class [Connector](reference/connector.md#connector) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enablePresence](reference/connector.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disablePresence](reference/connector.md#description)(); |
| &nbsp;&nbsp; int [getPresence](reference/connector.md#description)() const; |
| &nbsp;&nbsp; virtual void [lock](reference/connector.md#description)(); |
| &nbsp;&nbsp; virtual void [unlock](reference/connector.md#description)(); |
| }; |

| |
| --- |
| #include `<`webots/Device.hpp`>` |
| class [Device](reference/device.md#device) { |
| &nbsp;&nbsp; const std::string &[getModel](reference/device.md#description)() const; |
| &nbsp;&nbsp; const std::string &[getName](reference/device.md#description)() const; |
| &nbsp;&nbsp; int [getNodeType](reference/device.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/DifferentialWheels.hpp`>` |
| class [DifferentialWheels](reference/differentialwheels.md#differentialwheels) : public [Robot](reference/cpp-api.md) { |
| &nbsp;&nbsp; [DifferentialWheels](reference/robot.md#description)(); |
| &nbsp;&nbsp; virtual [~DifferentialWheels](reference/robot.md#description)(); |
| &nbsp;&nbsp; virtual void [setSpeed](reference/differentialwheels.md#description)(double left, double right); |
| &nbsp;&nbsp; double [getLeftSpeed](reference/differentialwheels.md#description)() const; |
| &nbsp;&nbsp; double [getRightSpeed](reference/differentialwheels.md#description)() const; |
| &nbsp;&nbsp; virtual void [enableEncoders](reference/differentialwheels.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableEncoders](reference/differentialwheels.md#description)(); |
| &nbsp;&nbsp; int [getEncodersSamplingPeriod](reference/differentialwheels.md#description)(); |
| &nbsp;&nbsp; double [getLeftEncoder](reference/differentialwheels.md#description)() const; |
| &nbsp;&nbsp; double [getRightEncoder](reference/differentialwheels.md#description)() const; |
| &nbsp;&nbsp; virtual void [setEncoders](reference/differentialwheels.md#description)(double left, double right); |
| &nbsp;&nbsp; double [getMaxSpeed](reference/differentialwheels.md#description)() const; |
| &nbsp;&nbsp; double [getSpeedUnit](reference/differentialwheels.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Display.hpp`>` |
| class [Display](reference/display.md#display) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {RGB, RGBA, ARGB, BGRA}; |
| &nbsp;&nbsp; int [getWidth](reference/display.md#description)() const; |
| &nbsp;&nbsp; int [getHeight](reference/display.md#description)() const; |
| &nbsp;&nbsp; virtual void [setColor](reference/display.md#description)(int color); |
| &nbsp;&nbsp; virtual void [setAlpha](reference/display.md#description)(double alpha); |
| &nbsp;&nbsp; virtual void [setOpacity](reference/display.md#description)(double opacity); |
| &nbsp;&nbsp; virtual void [drawPixel](reference/display.md#description)(int x1, int y1); |
| &nbsp;&nbsp; virtual void [drawLine](reference/display.md#description)(int x1, int y1, int x2, int y2); |
| &nbsp;&nbsp; virtual void [drawRectangle](reference/display.md#description)(int x, int y, int width, int height); |
| &nbsp;&nbsp; virtual void [drawOval](reference/display.md#description)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; virtual void [drawPolygon](reference/display.md#description)(const int *x, const int *y, int size); |
| &nbsp;&nbsp; virtual void [drawText](reference/display.md#description)(const std::string &txt, int x, int y); |
| &nbsp;&nbsp; virtual void [fillRectangle](reference/display.md#description)(int x, int y, int width, int height); |
| &nbsp;&nbsp; virtual void [fillOval](reference/display.md#description)(int cx, int cy, int a, int b); |
| &nbsp;&nbsp; virtual void [fillPolygon](reference/display.md#description)(const int *x, const int *y, int size); |
| &nbsp;&nbsp; [ImageRef](reference/cpp-api.md) *[imageCopy](reference/display.md#description)(int x, int y, int width, int height) const; |
| &nbsp;&nbsp; virtual void [imagePaste](reference/display.md#description)([ImageRef](reference/cpp-api.md) *ir, int x, int y); |
| &nbsp;&nbsp; [ImageRef](reference/cpp-api.md) *[imageLoad](reference/display.md#description)(const std::string &filename) const; |
| &nbsp;&nbsp; [ImageRef](reference/cpp-api.md) *[imageNew](reference/display.md#description)(int width, int height, const void *data, int format) const; |
| &nbsp;&nbsp; void [imageSave](reference/display.md#description)([ImageRef](reference/cpp-api.md) *ir, const std::string &filename) const; |
| &nbsp;&nbsp; void [imageDelete](reference/display.md#description)([ImageRef](reference/cpp-api.md) *ir) const; |
| }; |

| |
| --- |
| #include `<`webots/DistanceSensor.hpp`>` |
| class [DistanceSensor](reference/distancesensor.md#distancesensor) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](reference/distancesensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/distancesensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/distancesensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](reference/distancesensor.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Emitter.hpp`>` |
| class [Emitter](reference/emitter.md#emitter) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST}; |
| &nbsp;&nbsp; virtual int [send](reference/emitter.md#description)(const void *data, int size); |
| &nbsp;&nbsp; int [getChannel](reference/emitter.md#description)() const; |
| &nbsp;&nbsp; virtual void [setChannel](reference/emitter.md#description)(int channel); |
| &nbsp;&nbsp; double [getRange](reference/emitter.md#description)() const; |
| &nbsp;&nbsp; virtual void [setRange](reference/emitter.md#description)(double range); |
| &nbsp;&nbsp; int [getBufferSize](reference/emitter.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Field.hpp`>` |
| class Field { |
| &nbsp;&nbsp; enum { SF\_BOOL, SF\_INT32, SF\_FLOAT, SF\_VEC2F, SF\_VEC3F, SF\_ROTATION, SF\_COLOR, SF\_STRING, SF\_NODE, MF, MF\_INT32, MF\_FLOAT, MF\_VEC2F, MF\_VEC3F, MF\_COLOR, MF\_STRING, MF\_NODE }; |
| &nbsp;&nbsp; int [getType](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getTypeName](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; int [getCount](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; bool [getSFBool](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; int [getSFInt32](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; double [getSFFloat](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFVec2f](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFVec3f](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFRotation](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getSFColor](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getSFString](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; [Node](reference/cpp-api.md) *[getSFNode](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; bool [getMFBool](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; int [getMFInt32](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; double [getMFFloat](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFVec2f](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFVec3f](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFRotation](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; const double *[getMFColor](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; std::string [getMFString](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; [Node](reference/cpp-api.md) *[getMFNode](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; void [setSFBool](reference/supervisor.md#description)(bool value); |
| &nbsp;&nbsp; void [setSFInt32](reference/supervisor.md#description)(int value); |
| &nbsp;&nbsp; void [setSFFloat](reference/supervisor.md#description)(double value); |
| &nbsp;&nbsp; void [setSFVec2f](reference/supervisor.md#description)(const double values[2]); |
| &nbsp;&nbsp; void [setSFVec3f](reference/supervisor.md#description)(const double values[3]); |
| &nbsp;&nbsp; void [setSFRotation](reference/supervisor.md#description)(const double values[4]); |
| &nbsp;&nbsp; void [setSFColor](reference/supervisor.md#description)(const double values[3]); |
| &nbsp;&nbsp; void [setSFString](reference/supervisor.md#description)(const std::string &value); |
| &nbsp;&nbsp; void [setMFBool](reference/supervisor.md#description)(int index, bool value); |
| &nbsp;&nbsp; void [setMFInt32](reference/supervisor.md#description)(int index, int value); |
| &nbsp;&nbsp; void [setMFFloat](reference/supervisor.md#description)(int index, double value); |
| &nbsp;&nbsp; void [setMFVec2f](reference/supervisor.md#description)(int index, const double values[2]); |
| &nbsp;&nbsp; void [setMFVec3f](reference/supervisor.md#description)(int index, const double values[3]); |
| &nbsp;&nbsp; void [setMFRotation](reference/supervisor.md#description)(int index, const double values[4]); |
| &nbsp;&nbsp; void [setMFColor](reference/supervisor.md#description)(int index, const double values[3]); |
| &nbsp;&nbsp; void [setMFString](reference/supervisor.md#description)(int index, const std::string &value); |
| &nbsp;&nbsp; void [importMFNode](reference/supervisor.md#description)(int position, const std::string &filename); |
| &nbsp;&nbsp; void [importMFNodeFromString](reference/supervisor.md#description)(int position, const std::string &nodeString); |
| &nbsp;&nbsp; void [removeMFNode](reference/supervisor.md#description)(int position); |
| }; |

| |
| --- |
| #include `<`webots/GPS.hpp`>` |
| class [GPS](reference/gps.md#gps) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](reference/gps.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/gps.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/gps.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](reference/gps.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Gyro.hpp`>` |
| class [Gyro](reference/gyro.md#gyro) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](reference/gyro.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/gyro.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/gyro.md#description)(); |
| &nbsp;&nbsp; const double *[getValues](reference/gyro.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/ImageRef.hpp`>` |
| class ImageRef { |
| }; |

| |
| --- |
| #include `<`webots/InertialUnit.hpp`>` |
| class [InertialUnit](reference/inertialunit.md#inertialunit) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](reference/inertialunit.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/inertialunit.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/inertialunit.md#description)(); |
| &nbsp;&nbsp; const double *[getRollPitchYaw](reference/inertialunit.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/LED.hpp`>` |
| class [LED](reference/led.md#led) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [set](reference/led.md#description)(int value); |
| &nbsp;&nbsp; int [get](reference/led.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/LightSensor.hpp`>` |
| class [LightSensor](reference/lightsensor.md#lightsensor) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [enable](reference/lightsensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/lightsensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/lightsensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](reference/lightsensor.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/utils/Motion.hpp`>` |
| class [Motion](reference/motion.md#motion) { |
| &nbsp;&nbsp; [Motion](reference/motion.md#description)(const std::string &fileName); |
| &nbsp;&nbsp; virtual [~Motion](reference/motion.md#description)(); |
| &nbsp;&nbsp; bool [isValid](reference/motion.md#description)() const; |
| &nbsp;&nbsp; virtual void [play](reference/motion.md#description)(); |
| &nbsp;&nbsp; virtual void [stop](reference/motion.md#description)(); |
| &nbsp;&nbsp; virtual void [setLoop](reference/motion.md#description)(bool loop); |
| &nbsp;&nbsp; virtual void [setReverse](reference/motion.md#description)(bool reverse); |
| &nbsp;&nbsp; bool [isOver](reference/motion.md#description)() const; |
| &nbsp;&nbsp; int [getDuration](reference/motion.md#description)() const; |
| &nbsp;&nbsp; int [getTime](reference/motion.md#description)() const; |
| &nbsp;&nbsp; virtual void [setTime](reference/motion.md#description)(int time); |
| }; |

| |
| --- |
| #include `<`webots/Motor.hpp`>` |
| class [Motor](reference/motor.md#motor) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR}; |
| &nbsp;&nbsp; virtual void [setPosition](reference/motor.md#description)(double position); |
| &nbsp;&nbsp; virtual void [setVelocity](reference/motor.md#description)(double vel); |
| &nbsp;&nbsp; virtual void [setAcceleration](reference/motor.md#description)(double force); |
| &nbsp;&nbsp; virtual void [setAvailableForce](reference/motor.md#description)(double motor\_force); |
| &nbsp;&nbsp; virtual void [setAvailableTorque](reference/motor.md#description)(double motor\_torque); |
| &nbsp;&nbsp; virtual void [setControlPID](reference/motor.md#description)(double p, double i, double d); |
| &nbsp;&nbsp; double [getTargetPosition](reference/motor.md#description)(double position) const; |
| &nbsp;&nbsp; double [getMinPosition](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxPosition](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getVelocity](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxVelocity](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getAcceleration](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getAvailableForce](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxForce](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getAvailableTorque](reference/motor.md#description)() const; |
| &nbsp;&nbsp; double [getMaxTorque](reference/motor.md#description)() const; |
| &nbsp;&nbsp; virtual void [enableForceFeedback](reference/motor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableForceFeedback](reference/motor.md#description)(); |
| &nbsp;&nbsp; int [getForceFeedbackSamplingPeriod](reference/motor.md#description)(); |
| &nbsp;&nbsp; double [getForceFeedback](reference/motor.md#description)() const; |
| &nbsp;&nbsp; virtual void [setForce](reference/motor.md#description)(double force); |
| &nbsp;&nbsp; virtual void [enableTorqueFeedback](reference/motor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableTorqueFeedback](reference/motor.md#description)(); |
| &nbsp;&nbsp; int [getTorqueFeedbackSamplingPeriod](reference/motor.md#description)(); |
| &nbsp;&nbsp; double [getTorqueFeedback](reference/motor.md#description)() const; |
| &nbsp;&nbsp; virtual void [setTorque](reference/motor.md#description)(double torque); |
| &nbsp;&nbsp; int [getType](reference/motor.md#description)() const; |
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
| &nbsp;&nbsp; virtual void [remove](reference/supervisor.md#description)(); |
| &nbsp;&nbsp; int [getId](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; int [getType](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getTypeName](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; std::string [getBaseTypeName](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; Node *[getParentNode](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; [Field](reference/cpp-api.md) *[getField](reference/supervisor.md#description)(const std::string &fieldName) const; |
| &nbsp;&nbsp; const double *[getPosition](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getOrientation](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getCenterOfMass](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double *[getContactPoint](reference/supervisor.md#description)(int index) const; |
| &nbsp;&nbsp; int [getNumberOfContactPoints](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; bool [getStaticBalance](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; const double * [getVelocity](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; void [setVelocity](reference/supervisor.md#description)(const double velocity[6]); |
| &nbsp;&nbsp; void [resetPhysics](reference/supervisor.md#description)(); |
| }; |

| |
| --- |
| #include `<`webots/Pen.hpp`>` |
| class [Pen](reference/pen.md#pen) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; virtual void [write](reference/pen.md#description)(bool write); |
| &nbsp;&nbsp; virtual void [setInkColor](reference/pen.md#description)(int color, double density); |
| }; |

| |
| --- |
| #include `<`webots/PositionSensor.hpp`>` |
| class [PositionSensor](reference/positionsensor.md#positionsensor) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {ANGULAR, LINEAR}; |
| &nbsp;&nbsp; virtual void [enable](reference/positionsensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/positionsensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/positionsensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](reference/positionsensor.md#description)() const; |
| &nbsp;&nbsp; int [getType](reference/positionsensor.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Receiver.hpp`>` |
| class [Receiver](reference/receiver.md#receiver) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {CHANNEL\_BROADCAST}; |
| &nbsp;&nbsp; virtual void [enable](reference/receiver.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/receiver.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/receiver.md#description)(); |
| &nbsp;&nbsp; int [getQueueLength](reference/receiver.md#description)() const; |
| &nbsp;&nbsp; virtual void [nextPacket](reference/receiver.md#description)(); |
| &nbsp;&nbsp; const void *[getData](reference/receiver.md#description)() const; |
| &nbsp;&nbsp; int [getDataSize](reference/receiver.md#description)() const; |
| &nbsp;&nbsp; double [getSignalStrength](reference/receiver.md#description)() const; |
| &nbsp;&nbsp; const double *[getEmitterDirection](reference/receiver.md#description)() const; |
| &nbsp;&nbsp; virtual void [setChannel](reference/receiver.md#description)(int channel); |
| &nbsp;&nbsp; int [getChannel](reference/receiver.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Robot.hpp`>` |
| class [Robot](reference/robot.md#robot) { |
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
| &nbsp;&nbsp; [Robot](reference/robot.md#description)(); |
| &nbsp;&nbsp; virtual [~Robot](reference/robot.md#description)(); |
| &nbsp;&nbsp; virtual int [step](reference/robot.md#description)(int ms); |
| &nbsp;&nbsp; [Accelerometer](reference/cpp-api.md) *[getAccelerometer](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Brake](reference/cpp-api.md) *[getBrake](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Camera](reference/cpp-api.md) *[getCamera](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Compass](reference/cpp-api.md) *[getCompass](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Connector](reference/cpp-api.md) *[getConnector](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Display](reference/cpp-api.md) *[getDisplay](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [DistanceSensor](reference/cpp-api.md) *[getDistanceSensor](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Emitter](reference/cpp-api.md) *[getEmitter](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [GPS](reference/cpp-api.md) *[getGPS](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Gyro](reference/cpp-api.md) *[getGyro](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [InertialUnit](reference/cpp-api.md) *[getInertialUnit](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [LED](reference/cpp-api.md) *[getLED](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [LightSensor](reference/cpp-api.md) *[getLightSensor](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Motor](reference/cpp-api.md) *[getMotor](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Pen](reference/cpp-api.md) *[getPen](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [PositionSensor](reference/cpp-api.md) *[getPositionSensor](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Receiver](reference/cpp-api.md) *[getReceiver](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Servo](reference/cpp-api.md) *[getServo](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; [TouchSensor](reference/cpp-api.md) *[getTouchSensor](reference/robot.md#description)(const std::string &name); |
| &nbsp;&nbsp; int [getNumberOfDevices](reference/robot.md#description)(); |
| &nbsp;&nbsp; [Device](reference/cpp-api.md) *[getDeviceByIndex](reference/robot.md#description)(int index); |
| &nbsp;&nbsp; virtual void [batterySensorEnable](reference/robot.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [batterySensorDisable](reference/robot.md#description)(); |
| &nbsp;&nbsp; int [batterySensorGetSamplingPeriod](reference/robot.md#description)(); |
| &nbsp;&nbsp; double [batterySensorGetValue](reference/robot.md#description)() const; |
| &nbsp;&nbsp; double [getBasicTimeStep](reference/robot.md#description)() const; |
| &nbsp;&nbsp; int [getMode](reference/robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getModel](reference/robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getData](reference/robot.md#description)() const; |
| &nbsp;&nbsp; void [setData](reference/robot.md#description)(const std::string &data); |
| &nbsp;&nbsp; std::string [getName](reference/robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getControllerName](reference/robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getControllerArguments](reference/robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getProjectPath](reference/robot.md#description)() const; |
| &nbsp;&nbsp; bool [getSynchronization](reference/robot.md#description)() const; |
| &nbsp;&nbsp; double [getTime](reference/robot.md#description)() const; |
| &nbsp;&nbsp; std::string [getWorldPath](reference/robot.md#description)() const; |
| &nbsp;&nbsp; virtual void [keyboardEnable](reference/robot.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [keyboardDisable](reference/robot.md#description)(); |
| &nbsp;&nbsp; int [keyboardGetKey](reference/robot.md#description)() const; |
| &nbsp;&nbsp; int [getType](reference/robot.md#description)() const; |
| &nbsp;&nbsp; void *[robotWindowCustomFunction](reference/robot.md#description)(void *arg); |
| }; |

| |
| --- |
| #include `<`webots/Servo.hpp`>` |
| class [Servo](reference/servo.md#servo) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {ROTATIONAL, LINEAR}; |
| &nbsp;&nbsp; virtual void [setPosition](reference/servo.md#description)(double position); |
| &nbsp;&nbsp; virtual void [setVelocity](reference/servo.md#description)(double vel); |
| &nbsp;&nbsp; virtual void [setAcceleration](reference/servo.md#description)(double force); |
| &nbsp;&nbsp; virtual void [setMotorForce](reference/servo.md#description)(double motor\_force); |
| &nbsp;&nbsp; virtual void [setControlP](reference/servo.md#description)(double p); |
| &nbsp;&nbsp; double [getTargetPosition](reference/servo.md#description)(double position) const; |
| &nbsp;&nbsp; double [getMinPosition](reference/servo.md#description)() const; |
| &nbsp;&nbsp; double [getMaxPosition](reference/servo.md#description)() const; |
| &nbsp;&nbsp; virtual void [enablePosition](reference/servo.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disablePosition](reference/servo.md#description)(); |
| &nbsp;&nbsp; int [getPositionSamplingPeriod](reference/servo.md#description)(); |
| &nbsp;&nbsp; double [getPosition](reference/servo.md#description)() const; |
| &nbsp;&nbsp; virtual void [enableMotorForceFeedback](reference/servo.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disableMotorForceFeedback](reference/servo.md#description)(); |
| &nbsp;&nbsp; int [getMotorForceFeedbackSamplingPeriod](reference/servo.md#description)(); |
| &nbsp;&nbsp; double [getMotorForceFeedback](reference/servo.md#description)() const; |
| &nbsp;&nbsp; virtual void [setForce](reference/servo.md#description)(double force); |
| &nbsp;&nbsp; int [getType](reference/servo.md#description)() const; |
| }; |

| |
| --- |
| #include `<`webots/Supervisor.hpp`>` |
| class [Supervisor](reference/supervisor.md#supervisor) : public [Robot](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {MOVIE\_READY, MOVIE\_RECORDING, MOVIE\_SAVING, MOVIE\_WRITE\_ERROR, MOVIE\_ENCODING\_ERROR, MOVIE\_SIMULATION\_ERROR}; |
| &nbsp;&nbsp; [Supervisor](reference/robot.md#description)(); |
| &nbsp;&nbsp; virtual [~Supervisor](reference/robot.md#description)(); |
| &nbsp;&nbsp; void [exportImage](reference/supervisor.md#description)(const std::string &file, int quality) const; |
| &nbsp;&nbsp; [Node](reference/cpp-api.md) *[getRoot](reference/supervisor.md#description)(); |
| &nbsp;&nbsp; [Node](reference/cpp-api.md) *[getSelf](reference/supervisor.md#description)(); |
| &nbsp;&nbsp; [Node](reference/cpp-api.md) *[getFromDef](reference/supervisor.md#description)(const std::string &name); |
| &nbsp;&nbsp; [Node](reference/cpp-api.md) *[getFromId](reference/supervisor.md#description)(int id); |
| &nbsp;&nbsp; virtual void [setLabel](reference/supervisor.md#description)(int id, const std::string &label, double xpos, double ypos, |
| &nbsp;&nbsp;&nbsp;&nbsp; double size, int color, double transparency); |
| &nbsp;&nbsp; virtual void [simulationQuit](reference/supervisor.md#description)(int status); |
| &nbsp;&nbsp; virtual void [simulationRevert](reference/supervisor.md#description)(); |
| &nbsp;&nbsp; virtual void [simulationResetPhysics](reference/supervisor.md#description)(); |
| &nbsp;&nbsp; virtual void [loadWorld](reference/supervisor.md#description)(const std::string &file); |
| &nbsp;&nbsp; virtual void [saveWorld](reference/supervisor.md#description)(); |
| &nbsp;&nbsp; virtual void [saveWorld](reference/supervisor.md#description)(const std::string &file); |
| &nbsp;&nbsp; virtual void [movieStartRecording](reference/supervisor.md#description)(const std::string &file, int width, int height, int codec, int quality, |
| &nbsp;&nbsp; int acceleration, bool caption) const; |
| &nbsp;&nbsp; virtual void [movieStopRecording](reference/supervisor.md#description)(); |
| &nbsp;&nbsp; int [movieGetStatus](reference/supervisor.md#description)() const; |
| &nbsp;&nbsp; virtual bool [animationStartRecording](reference/supervisor.md#description)(const std::string &file); |
| &nbsp;&nbsp; virtual bool [animationStopRecording](reference/supervisor.md#description)(); |
| }; |

| |
| --- |
| #include `<`webots/TouchSensor.hpp`>` |
| class [TouchSensor](reference/touchsensor.md#touchsensor) : public [Device](reference/cpp-api.md) { |
| &nbsp;&nbsp; enum {BUMPER, FORCE, FORCE3D}; |
| &nbsp;&nbsp; virtual void [enable](reference/touchsensor.md#description)(int ms); |
| &nbsp;&nbsp; virtual void [disable](reference/touchsensor.md#description)(); |
| &nbsp;&nbsp; int [getSamplingPeriod](reference/touchsensor.md#description)(); |
| &nbsp;&nbsp; double [getValue](reference/touchsensor.md#description)() const; |
| &nbsp;&nbsp; const double *[getValues](reference/touchsensor.md#description)() const; |
| &nbsp;&nbsp; int [getType](reference/touchsensor.md#description)() const; |
| }; |

