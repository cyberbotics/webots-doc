## Matlab API

The following tables describe the Matlab functions.

| % [Accelerometer](accelerometer.md#accelerometer) : |
| --- |
| [wb\_accelerometer\_enable](accelerometer.md#description)(tag, ms) |
| [wb\_accelerometer\_disable](accelerometer.md#description)(tag) |
| period = [wb\_accelerometer\_get\_sampling\_period](accelerometer.md#description)(tag) |
| [x y z] = [wb\_accelerometer\_get\_values](accelerometer.md#description)(tag) |

| % [Brake](brake.md#brake) : |
| --- |
| [wb\_brake\_set\_damping\_constant](brake.md#description)(tag, dampingConstant) |
| type = [wb\_brake\_get\_type](brake.md#description)(tag) |

| % [Camera](camera.md#camera) : |
| --- |
| WB\_CAMERA\_COLOR |
| WB\_CAMERA\_RANGE\_FINDER |
| [wb\_camera\_enable](camera.md#description)(tag, ms) |
| [wb\_camera\_disable](camera.md#description)(tag) |
| period = [wb\_camera\_get\_sampling\_period](camera.md#description)(tag) |
| fov = [wb\_camera\_get\_fov](camera.md#description)(tag) |
| fov = [wb\_camera\_get\_min\_fov](camera.md#description)(tag) |
| fov = [wb\_camera\_get\_max\_fov](camera.md#description)(tag) |
| [wb\_camera\_set\_fov](camera.md#description)(tag, fov) |
| fov = [wb\_camera\_get\_focal\_length](camera.md#description)(tag) |
| fov = [wb\_camera\_get\_focal\_distance](camera.md#description)(tag) |
| fov = [wb\_camera\_get\_max\_focal\_distance](camera.md#description)(tag) |
| fov = [wb\_camera\_get\_min\_focal\_distance](camera.md#description)(tag) |
| [wb\_camera\_set\_focal\_distance](camera.md#description)(tag, focal\_distance) |
| width = [wb\_camera\_get\_width](camera.md#description)(tag) |
| height = [wb\_camera\_get\_height](camera.md#description)(tag) |
| near = [wb\_camera\_get\_near](camera.md#description)(tag) |
| type = [wb\_camera\_get\_type](camera.md#description)(tag) |
| image = [wb\_camera\_get\_image](camera.md#description)(tag) |
| image = [wb\_camera\_get\_range\_image](camera.md#description)(tag) |
| max\_range = [wb\_camera\_get\_max\_range](camera.md#description)(tag) |
| [wb\_camera\_save\_image](camera.md#description)(tag, 'filename', quality) |

| % [Compass](compass.md#compass) : |
| --- |
| [wb\_compass\_enable](compass.md#description)(tag, ms) |
| [wb\_compass\_disable](compass.md#description)(tag) |
| period = [wb\_compass\_get\_sampling\_period](compass.md#description)(tag) |
| [x y z] = [wb\_compass\_get\_values](compass.md#description)(tag) |

| % [Connector](connector.md#connector) : |
| --- |
| [wb\_connector\_enable\_presence](connector.md#description)(tag, ms) |
| [wb\_connector\_disable\_presence](connector.md#description)(tag) |
| presence = [wb\_connector\_get\_presence](connector.md#description)(tag) |
| [wb\_connector\_lock](connector.md#description)(tag) |
| [wb\_connector\_unlock](connector.md#description)(tag) |

| % [Device](device.md#device) : |
| --- |
| model = [wb\_device\_get\_model](device.md#description)(tag) |
| name = [wb\_device\_get\_name](device.md#description)(tag) |
| type = [wb\_device\_get\_node\_type](device.md#description)(tag) |

| % [DifferentialWheels](differentialwheels.md#differentialwheels) : |
| --- |
| [wb\_differential\_wheels\_set\_speed](differentialwheels.md#description)(left, right) |
| left = [wb\_differential\_wheels\_get\_left\_speed](differentialwheels.md#description)() |
| right = [wb\_differential\_wheels\_get\_right\_speed](differentialwheels.md#description)() |
| [wb\_differential\_wheels\_enable\_encoders](differentialwheels.md#description)(ms) |
| [wb\_differential\_wheels\_disable\_encoders](differentialwheels.md#description)() |
| period = [wb\_differential\_wheels\_get\_encoders\_sampling\_period](differentialwheels.md#description)() |
| left = [wb\_differential\_wheels\_get\_left\_encoder](differentialwheels.md#description)() |
| right = [wb\_differential\_wheels\_get\_right\_encoder](differentialwheels.md#description)() |
| [wb\_differential\_wheels\_set\_encoders](differentialwheels.md#description)(left, right) |
| max = [wb\_differential\_wheels\_get\_max\_speed](differentialwheels.md#description)() |
| unit = [wb\_differential\_wheels\_get\_speed\_unit](differentialwheels.md#description)() |

| % [Display](display.md#display) : |
| --- |
| RGB |
| RGBA |
| ARGB |
| BGRA |
| width = [wb\_display\_get\_width](display.md#description)(tag) |
| height = [wb\_display\_get\_height](display.md#description)(tag) |
| [wb\_display\_set\_color](display.md#description)(tag, [r g b]) |
| [wb\_display\_set\_alpha](display.md#description)(tag, alpha) |
| [wb\_display\_set\_opacity](display.md#description)(tag, opacity) |
| [wb\_display\_draw\_pixel](display.md#description)(tag, x, y) |
| [wb\_display\_draw\_line](display.md#description)(tag, x1, y1, x2, y2) |
| [wb\_display\_draw\_rectangle](display.md#description)(tag, x, y, width, height) |
| [wb\_display\_draw\_oval](display.md#description)(tag, cx, cy, a, b) |
| [wb\_display\_draw\_polygon](display.md#description)(tag, [x1 x2 ... xn], [y1 y2 ... yn]) |
| [wb\_display\_draw\_text](display.md#description)(tag, 'txt', x, y) |
| [wb\_display\_fill\_rectangle](display.md#description)(tag, x, y, width, height) |
| [wb\_display\_fill\_oval](display.md#description)(tag, cx, cy, a, b) |
| [wb\_display\_fill\_polygon](display.md#description)(tag, [x1 x2 ... xn], [y1 y2 ... yn]) |
| image = [wb\_display\_image\_copy](display.md#description)(tag, x, y, width, height) |
| [wb\_display\_image\_paste](display.md#description)(tag, image, x, y) |
| image = [wb\_display\_image\_load](display.md#description)(tag, 'filename') |
| image = [wb\_display\_image\_new](display.md#description)(tag, width, height, data ,format) |
| [wb\_display\_image\_save](display.md#description)(tag, image, 'filename') |
| [wb\_display\_image\_delete](display.md#description)(tag, image) |

| % [DistanceSensor](distancesensor.md#distancesensor) : |
| --- |
| [wb\_distance\_sensor\_enable](distancesensor.md#description)(tag, ms) |
| [wb\_distance\_sensor\_disable](distancesensor.md#description)(tag) |
| period = [wb\_distance\_sensor\_get\_sampling\_period](distancesensor.md#description)(tag) |
| value = [wb\_distance\_sensor\_get\_value](distancesensor.md#description)(tag) |

| % [Emitter](emitter.md#emitter) : |
| --- |
| WB\_CHANNEL\_BROADCAST |
| [wb\_emitter\_send](emitter.md#description)(tag, data) |
| [wb\_emitter\_set\_channel](emitter.md#description)(tag, channel) |
| channel = [wb\_emitter\_get\_channel](emitter.md#description)(tag) |
| range = [wb\_emitter\_get\_range](emitter.md#description)(tag) |
| [wb\_emitter\_set\_range](emitter.md#description)(tag, range) |
| size = [wb\_emitter\_get\_buffer\_size](emitter.md#description)(tag) |

| % [GPS](gps.md#gps) : |
| --- |
| [wb\_gps\_enable](gps.md#description)(tag, ms) |
| [wb\_gps\_disable](gps.md#description)(tag) |
| period = [wb\_gps\_get\_sampling\_period](gps.md#description)(tag) |
| [x y z] = [wb\_gps\_get\_values](gps.md#description)(tag) |

| % [Gyro](gyro.md#gyro) : |
| --- |
| [wb\_gyro\_enable](gyro.md#description)(tag, ms) |
| [wb\_gyro\_disable](gyro.md#description)(tag) |
| period = [wb\_gyro\_get\_sampling\_period](gyro.md#description)(tag) |
| [x y z] = [wb\_gyro\_get\_values](gyro.md#description)(tag) |

| % [InertialUnit](inertialunit.md#inertialunit) : |
| --- |
| [wb\_inertial\_unit\_enable](inertialunit.md#description)(tag, ms) |
| [wb\_inertial\_unit\_disable](inertialunit.md#description)(tag) |
| period = [wb\_inertial\_unit\_get\_sampling\_period](inertialunit.md#description)(tag) |
| [roll pitch yaw] = [wb\_inertial\_unit\_get\_roll\_pitch\_yaw](inertialunit.md#description)(tag) |

| % [LED](led.md#led) : |
| --- |
| [wb\_led\_set](led.md#description)(tag, state) |
| state = [wb\_led\_get](led.md#description)(tag) |

| % [LightSensor](lightsensor.md#lightsensor) : |
| --- |
| [wb\_light\_sensor\_enable](lightsensor.md#description)(tag, ms) |
| [wb\_light\_sensor\_disable](lightsensor.md#description)(tag) |
| period = [wb\_light\_sensor\_get\_sampling\_period](lightsensor.md#description)(tag) |
| value = [wb\_light\_sensor\_get\_value](lightsensor.md#description)(tag) |

| % [Motion](motion.md#motion) : |
| --- |
| motion = [wbu\_motion\_new](motion.md#description)('filename') |
| [wbu\_motion\_delete](motion.md#description)(motion) |
| [wbu\_motion\_play](motion.md#description)(motion) |
| [wbu\_motion\_stop](motion.md#description)(motion) |
| [wbu\_motion\_set\_loop](motion.md#description)(motion, loop) |
| [wbu\_motion\_set\_reverse](motion.md#description)(motion, reverse) |
| over = [wbu\_motion\_is\_over](motion.md#description)(motion) |
| duration = [wbu\_motion\_get\_duration](motion.md#description)(motion) |
| time = [wbu\_motion\_get\_time](motion.md#description)(motion) |
| [wbu\_motion\_set\_time](motion.md#description)(motion, time) |

| % [Motor](motor.md#motor) : |
| --- |
| WB\_MOTOR\_ROTATIONAL, WB\_MOTOR\_LINEAR |
| [wb\_motor\_set\_position](motor.md#description)(tag, position) |
| [wb\_motor\_set\_velocity](motor.md#description)(tag, vel) |
| [wb\_motor\_set\_acceleration](motor.md#description)(tag, acc) |
| [wb\_motor\_set\_available\_force](motor.md#description)(tag, force) |
| [wb\_motor\_set\_available\_torque](motor.md#description)(tag, torque) |
| [wb\_motor\_set\_control\_pid](motor.md#description)(tag, p, i, d) |
| target = [wb\_motor\_get\_target\_position](motor.md#description)(tag) |
| min = [wb\_motor\_get\_min\_position](motor.md#description)(tag) |
| max = [wb\_motor\_get\_max\_position](motor.md#description)(tag) |
| vel = [wb\_motor\_get\_velocity](motor.md#description)(tag) |
| vel = [wb\_motor\_get\_max\_velocity](motor.md#description)(tag) |
| acc = [wb\_motor\_get\_acceleration](motor.md#description)(tag) |
| force = [wb\_motor\_get\_available\_force](motor.md#description)(tag) |
| force = [wb\_motor\_get\_max\_force](motor.md#description)(tag) |
| torque = [wb\_motor\_get\_available\_torque](motor.md#description)(tag) |
| torque = [wb\_motor\_get\_max\_torque](motor.md#description)(tag) |
| [wb\_motor\_enable\_force\_feedback](motor.md#description)(tag, ms) |
| [wb\_motor\_disable\_force\_feedback](motor.md#description)(tag) |
| period = [wb\_motor\_get\_force\_feedback\_sampling\_period](motor.md#description)(tag) |
| force = [wb\_motor\_get\_force\_feedback](motor.md#description)(tag) |
| [wb\_motor\_set\_force](motor.md#description)(tag, force) |
| [wb\_motor\_enable\_torque\_feedback](motor.md#description)(tag, ms) |
| [wb\_motor\_disable\_torque\_feedback](motor.md#description)(tag) |
| period = [wb\_motor\_get\_torque\_feedback\_sampling\_period](motor.md#description)(tag) |
| force = [wb\_motor\_get\_torque\_feedback](motor.md#description)(tag) |
| [wb\_motor\_set\_torque](motor.md#description)(tag, torque) |
| type = [wb\_motor\_get\_type](motor.md#description)(tag) |

| Node: |
| --- |
| WB\_NODE\_NO\_NODE, WB\_NODE\_APPEARANCE, WB\_NODE\_BACKGROUND, |
| WB\_NODE\_BOX, WB\_NODE\_COLOR, WB\_NODE\_CONE, |
| WB\_NODE\_COORDINATE, WB\_NODE\_CYLINDER, |
| WB\_NODE\_DIRECTIONAL\_LIGHT, WB\_NODE\_ELEVATION\_GRID, |
| WB\_NODE\_EXTRUSION, WB\_NODE\_FOG, WB\_NODE\_GROUP, |
| WB\_NODE\_IMAGE\_TEXTURE, WB\_NODE\_INDEXED\_FACE\_SET, |
| WB\_NODE\_INDEXED\_LINE\_SET, WB\_NODE\_MATERIAL, |
| WB\_NODE\_POINT\_LIGHT, WB\_NODE\_SHAPE, WB\_NODE\_SPHERE, |
| WB\_NODE\_SPOT\_LIGHT, WB\_NODE\_SWITCH, |
| WB\_NODE\_TEXTURE\_COORDINATE, WB\_NODE\_TEXTURE\_TRANSFORM, |
| WB\_NODE\_TRANSFORM, WB\_NODE\_VIEWPOINT, WB\_NODE\_WORLD\_INFO, |
| WB\_NODE\_CAPSULE, WB\_NODE\_PLANE, WB\_NODE\_ROBOT, |
| WB\_NODE\_SUPERVISOR, WB\_NODE\_DIFFERENTIAL\_WHEELS, |
| WB\_NODE\_SOLID, WB\_NODE\_PHYSICS, WB\_NODE\_CAMERA\_ZOOM, |
| WB\_NODE\_CHARGER, WB\_NODE\_DAMPING, |
| WB\_NODE\_CONTACT\_PROPERTIES, WB\_NODE\_ACCELEROMETER, WB\_NODE\_BRAKE, |
| WB\_NODE\_CAMERA, WB\_NODE\_COMPASS, WB\_NODE\_CONNECTOR, |
| WB\_NODE\_DISPLAY, WB\_NODE\_DISTANCE\_SENSOR, WB\_NODE\_EMITTER, |
| WB\_NODE\_GPS, WB\_NODE\_GYRO, WB\_NODE\_LED, |
| WB\_NODE\_LIGHT\_SENSOR, WB\_NODE\_MICROPHONE, WB\_NODE\_MOTOR, |
| WB\_NODE\_PEN, WB\_NODE\_POSITION\_SENSOR, WB\_NODE\_RADIO, |
| WB\_NODE\_RECEIVER, WB\_NODE\_SERVO, WB\_NODE\_SPEAKER, |
| WB\_NODE\_TOUCH\_SENSOR |

| % [Pen](pen.md#pen) : |
| --- |
| [wb\_pen\_write](pen.md#description)(tag, write) |
| [wb\_pen\_set\_ink\_color](pen.md#description)(tag, [r g b], density) |

| % [PositionSensor](positionsensor.md#positionsensor) : |
| --- |
| WB\_ANGULAR, WB\_LINEAR |
| [wb\_position\_sensor\_enable](positionsensor.md#description)(tag, ms) |
| [wb\_position\_sensor\_disable](positionsensor.md#description)(tag) |
| period = [wb\_position\_sensor\_get\_sampling\_period](positionsensor.md#description)(tag) |
| value = [wb\_position\_sensor\_get\_value](positionsensor.md#description)(tag) |
| type = [wb\_position\_sensor\_get\_type](positionsensor.md#description)(tag) |

| % [Receiver](receiver.md#receiver) : |
| --- |
| WB\_CHANNEL\_BROADCAST |
| [wb\_receiver\_enable](receiver.md#description)(tag, ms) |
| [wb\_receiver\_disable](receiver.md#description)(tag) |
| period = [wb\_receiver\_get\_sampling\_period](receiver.md#description)(tag) |
| length = [wb\_receiver\_get\_queue\_length](receiver.md#description)(tag) |
| [wb\_receiver\_next\_packet](receiver.md#description)(tag) |
| size = [wb\_receiver\_get\_data\_size](receiver.md#description)(tag) |
| data = [wb\_receiver\_get\_data](receiver.md#description)(tag) |
| strength = [wb\_receiver\_get\_signal\_strength](receiver.md#description)(tag) |
| [x y z] = [wb\_receiver\_get\_emitter\_direction](receiver.md#description)(tag) |
| [wb\_receiver\_set\_channel](receiver.md#description)(tag, channel) |
| channel = [wb\_receiver\_get\_channel](receiver.md#description)(tag) |

| % [Robot](robot.md#robot) : |
| --- |
| WB\_MODE\_SIMULATION, |
| WB\_MODE\_CROSS\_COMPILATION, |
| WB\_MODE\_REMOTE\_CONTROL |
| WB\_ROBOT\_KEYBOARD\_END |
| WB\_ROBOT\_KEYBOARD\_HOME |
| WB\_ROBOT\_KEYBOARD\_LEFT |
| WB\_ROBOT\_KEYBOARD\_UP |
| WB\_ROBOT\_KEYBOARD\_RIGHT |
| WB\_ROBOT\_KEYBOARD\_DOWN |
| WB\_ROBOT\_KEYBOARD\_PAGEUP |
| WB\_ROBOT\_KEYBOARD\_PAGEDOWN |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_HOME |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_LEFT |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_UP |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_RIGHT |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_DOWN |
| WB\_ROBOT\_KEYBOARD\_NUMPAD\_END |
| WB\_ROBOT\_KEYBOARD\_KEY |
| WB\_ROBOT\_KEYBOARD\_SHIFT |
| WB\_ROBOT\_KEYBOARD\_CONTROL |
| WB\_ROBOT\_KEYBOARD\_ALT |
| [wb\_robot\_step](robot.md#description)(ms) |
| tag = [wb\_robot\_get\_device](robot.md#description)('name') |
| size = [wb\_robot\_get\_number\_of\_devices](robot.md#description)() |
| tag = [wb\_robot\_get\_device\_by\_index](robot.md#description)(index) |
| [wb\_robot\_battery\_sensor\_enable](robot.md#description)(ms) |
| [wb\_robot\_battery\_sensor\_disable](robot.md#description)() |
| period = [wb\_robot\_battery\_sensor\_get\_sampling\_period](robot.md#description)() |
| value = [wb\_robot\_battery\_sensor\_get\_value](robot.md#description)() |
| step = [wb\_robot\_get\_basic\_time\_step](robot.md#description)() |
| mode = [wb\_robot\_get\_mode](robot.md#description)() |
| model = [wb\_robot\_get\_model](robot.md#description)() |
| data = [getData](robot.md#description)() |
| [setData](robot.md#description)('data') |
| name = [wb\_robot\_get\_name](robot.md#description)() |
| name = [wb\_robot\_get\_controller\_name](robot.md#description)() |
| name = [wb\_robot\_get\_controller\_arguments](robot.md#description)() |
| path = [wb\_robot\_get\_project\_path](robot.md#description)() |
| sync = [wb\_robot\_get\_synchronization](robot.md#description)() |
| time = [wb\_robot\_get\_time](robot.md#description)() |
| path = [wb\_robot\_get\_world\_path](robot.md#description)() |
| [wb\_robot\_keyboard\_enable](robot.md#description)(ms) |
| [wb\_robot\_keyboard\_disable](robot.md#description)() |
| key = [wb\_robot\_keyboard\_get\_key](robot.md#description)() |
| type = [wb\_robot\_get\_type](robot.md#description)() |

| % [Servo](servo.md#servo) : |
| --- |
| WB\_SERVO\_ROTATIONAL, WB\_SERVO\_LINEAR |
| [wb\_servo\_set\_position](servo.md#description)(tag, position) |
| target = [wb\_servo\_get\_target\_position](servo.md#description)(tag) |
| [wb\_servo\_set\_velocity](servo.md#description)(tag, vel) |
| [wb\_servo\_set\_acceleration](servo.md#description)(tag, acc) |
| [wb\_servo\_set\_motor\_force](servo.md#description)(tag, force) |
| [wb\_servo\_set\_control\_p](servo.md#description)(tag, p) |
| min = [wb\_servo\_get\_min\_position](servo.md#description)(tag) |
| max = [wb\_servo\_get\_max\_position](servo.md#description)(tag) |
| [wb\_servo\_enable\_position](servo.md#description)(tag, ms) |
| [wb\_servo\_disable\_position](servo.md#description)(tag) |
| period = [wb\_servo\_get\_position\_sampling\_period](servo.md#description)(tag) |
| position = [wb\_servo\_get\_position](servo.md#description)(tag) |
| [wb\_servo\_enable\_motor\_force\_feedback](servo.md#description)(tag, ms) |
| [wb\_servo\_disable\_motor\_force\_feedback](servo.md#description)(tag) |
| period = [wb\_servo\_get\_motor\_force\_feedback\_sampling\_period](servo.md#description)(tag) |
| force = [wb\_servo\_get\_motor\_force\_feedback](servo.md#description)(tag) |
| [wb\_servo\_set\_force](servo.md#description)(tag, force) |
| type = [wb\_servo\_get\_type](servo.md#description)(tag) |

| % [Supervisor](supervisor.md#supervisor) : |
| --- |
| WB\_SF\_BOOL, WB\_SF\_INT32, WB\_SF\_FLOAT, WB\_SF\_VEC2F, |
| WB\_SF\_VEC3F, WB\_SF\_ROTATION, WB\_SF\_COLOR, WB\_SF\_STRING, |
| WB\_SF\_NODE, WB\_MF, WB\_MF\_INT32, WB\_MF\_FLOAT, B\_MF\_VEC2F, |
| WB\_MF\_VEC3F, WB\_MF\_COLOR, WB\_MF\_STRING, WB\_MF\_NODE |
| WB\_SUPERVISOR\_MOVIE\_READY, WB\_SUPERVISOR\_MOVIE\_RECORDING, WB\_SUPERVISOR\_MOVIE\_SAVING, WB\_SUPERVISOR\_MOVIE\_WRITE\_ERROR, WB\_SUPERVISOR\_MOVIE\_ENCODING\_ERROR, WB\_SUPERVISOR\_MOVIE\_SIMULATION\_ERROR |
| [wb\_supervisor\_export\_image](supervisor.md#description)('filename', quality) |
| node = [wb\_supervisor\_node\_get\_root](supervisor.md#description)() |
| node = [wb\_supervisor\_node\_get\_self](supervisor.md#description)() |
| node = [wb\_supervisor\_node\_get\_from\_def](supervisor.md#description)('def') |
| node = [wb\_supervisor\_node\_get\_from\_id](supervisor.md#description)('id') |
| id = [wb\_supervisor\_node\_get\_id](supervisor.md#description)(node) |
| node = [wb\_supervisor\_node\_get\_parent\_node](supervisor.md#description)(node) |
| [wb\_supervisor\_node\_remove](supervisor.md#description)(node) |
| [wb\_supervisor\_set\_label](supervisor.md#description)(id, 'text', x, y, size, [r g b], transparency) |
| [wb\_supervisor\_simulation\_quit](supervisor.md#description)(status) |
| [wb\_supervisor\_simulation\_revert](supervisor.md#description)() |
| [wb\_supervisor\_simulation\_reset\_physics](supervisor.md#description)() |
| [wb\_supervisor\_load\_world](supervisor.md#description)('filename') |
| [wb\_supervisor\_save\_world](supervisor.md#description)() |
| [wb\_supervisor\_save\_world](supervisor.md#description)('filename') |
| [wb\_supervisor\_movie\_start\_recording](supervisor.md#description)('filename', width, height, codec, quality, |
| acceleration, caption) |
| [wb\_supervisor\_movie\_stop\_recording](supervisor.md#description)() |
| status = [wb\_supervisor\_movie\_get\_status](supervisor.md#description)() |
| success = [wb\_supervisor\_animation\_start\_recording](supervisor.md#description)('filename') |
| success = [wb\_supervisor\_animation\_stop\_recording](supervisor.md#description)() |
| type = [wb\_supervisor\_field\_get\_type](supervisor.md#description)(field) |
| name = [wb\_supervisor\_field\_get\_type\_name](supervisor.md#description)(field) |
| count = [wb\_supervisor\_field\_get\_count](supervisor.md#description)(field) |
| b = [wb\_supervisor\_field\_get\_sf\_bool](supervisor.md#description)(field) |
| i = [wb\_supervisor\_field\_get\_sf\_int32](supervisor.md#description)(field) |
| f = [wb\_supervisor\_field\_get\_sf\_float](supervisor.md#description)(field) |
| [x y] = [wb\_supervisor\_field\_get\_sf\_vec2f](supervisor.md#description)(field) |
| [x y z] = [wb\_supervisor\_field\_get\_sf\_vec3f](supervisor.md#description)(field) |
| [x y z alpha] = [wb\_supervisor\_field\_get\_sf\_rotation](supervisor.md#description)(field) |
| [r g b] = [wb\_supervisor\_field\_get\_sf\_color](supervisor.md#description)(field) |
| s = [wb\_supervisor\_field\_get\_sf\_string](supervisor.md#description)(field) |
| node = [wb\_supervisor\_field\_get\_sf\_node](supervisor.md#description)(field) |
| b = [wb\_supervisor\_field\_get\_mf\_bool](supervisor.md#description)(field, index) |
| i = [wb\_supervisor\_field\_get\_mf\_int32](supervisor.md#description)(field, index) |
| f = [wb\_supervisor\_field\_get\_mf\_float](supervisor.md#description)(field, index) |
| [x y] = [wb\_supervisor\_field\_get\_mf\_vec2f](supervisor.md#description)(field, index) |
| [x y z] = [wb\_supervisor\_field\_get\_mf\_vec3f](supervisor.md#description)(field, index) |
| [x y z a] = [wb\_supervisor\_field\_get\_mf\_rotation](supervisor.md#description)(field, index) |
| [r g b] = [wb\_supervisor\_field\_get\_mf\_color](supervisor.md#description)(field, index) |
| s = [wb\_supervisor\_field\_get\_mf\_string](supervisor.md#description)(field, index) |
| node = [wb\_supervisor\_field\_get\_mf\_node](supervisor.md#description)(field, index) |
| [wb\_supervisor\_field\_set\_sf\_bool](supervisor.md#description)(field, value) |
| [wb\_supervisor\_field\_set\_sf\_int32](supervisor.md#description)(field, value) |
| [wb\_supervisor\_field\_set\_sf\_float](supervisor.md#description)(field, value) |
| [wb\_supervisor\_field\_set\_sf\_vec2f](supervisor.md#description)(field, [x y]) |
| [wb\_supervisor\_field\_set\_sf\_vec3f](supervisor.md#description)(field, [x y z]) |
| [wb\_supervisor\_field\_set\_sf\_rotation](supervisor.md#description)(field, [x y z alpha]) |
| [wb\_supervisor\_field\_set\_sf\_color](supervisor.md#description)(field, [r g b]) |
| [wb\_supervisor\_field\_set\_sf\_string](supervisor.md#description)(field, 'value') |
| [wb\_supervisor\_field\_set\_mf\_bool](supervisor.md#description)(field, index, value) |
| [wb\_supervisor\_field\_set\_mf\_int32](supervisor.md#description)(field, index, value) |
| [wb\_supervisor\_field\_set\_mf\_float](supervisor.md#description)(field, index, value) |
| [wb\_supervisor\_field\_set\_mf\_vec2f](supervisor.md#description)(field, index, [x y]) |
| [wb\_supervisor\_field\_set\_mf\_vec3f](supervisor.md#description)(field, index, [x y z]) |
| [wb\_supervisor\_field\_set\_mf\_rotation](supervisor.md#description)(field, index, [x y z a]) |
| [wb\_supervisor\_field\_set\_mf\_color](supervisor.md#description)(field, index, [r g b]) |
| [wb\_supervisor\_field\_set\_mf\_string](supervisor.md#description)(field, index, 'value') |
| [wb\_supervisor\_field\_import\_mf\_node](supervisor.md#description)(field, position, 'filename') |
| [wb\_supervisor\_field\_import\_mf\_node\_from\_string](supervisor.md#description)(field, position, 'node\_string') |
| [wb\_supervisor\_field\_remove\_mf\_node](supervisor.md#description)(field, position) |
| type = [wb\_supervisor\_node\_get\_type](supervisor.md#description)(node) |
| name = [wb\_supervisor\_node\_get\_type\_name](supervisor.md#description)(node) |
| name = [wb\_supervisor\_node\_get\_base\_type\_name](supervisor.md#description)(node) |
| field = [wb\_supervisor\_node\_get\_field](supervisor.md#description)(node, 'field\_name') |
| position = [wb\_supervisor\_node\_get\_position](supervisor.md#description)(node) |
| orientation = [wb\_supervisor\_node\_get\_orientation](supervisor.md#description)(node) |
| com = [wb\_supervisor\_node\_get\_center\_of\_mass](supervisor.md#description)(node) |
| contact\_point = [wb\_supervisor\_node\_get\_contact\_point](supervisor.md#description)(node, index) |
| number\_of\_contacts = [wb\_supervisor\_node\_get\_number\_of\_contact\_points](supervisor.md#description)(index) |
| balance = [wb\_supervisor\_node\_get\_static\_balance](supervisor.md#description)(node) |
| velocity = [wb\_supervisor\_node\_get\_velocity](supervisor.md#description)(node) |
| [wb\_supervisor\_node\_set\_velocity](supervisor.md#description)(node, velocity) |
| [wb\_supervisor\_node\_reset\_physics](supervisor.md#description)(node) |

| % [TouchSensor](touchsensor.md#touchsensor) : |
| --- |
| WB\_TOUCH\_SENSOR\_BUMPER, WB\_TOUCH\_SENSOR\_FORCE, |
| WB\_TOUCH\_SENSOR\_FORCE3D |
| [wb\_touch\_sensor\_enable](touchsensor.md#description)(tag, ms) |
| [wb\_touch\_sensor\_disable](touchsensor.md#description)(tag) |
| period = [wb\_touch\_sensor\_get\_sampling\_period](touchsensor.md#description)(tag) |
| value = [wb\_touch\_sensor\_get\_value](touchsensor.md#description)(tag) |
| [x y z] = [wb\_touch\_sensor\_get\_values](touchsensor.md#description)(tag) |
| type = [wb\_touch\_sensor\_get\_type](touchsensor.md#description)(tag) |

