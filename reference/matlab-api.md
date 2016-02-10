## Matlab API

The following tables describe the Matlab functions.

| % [Accelerometer](reference/accelerometer.md#accelerometer) : |
| --- |
| [wb\_accelerometer\_enable](reference/accelerometer.md)(tag, ms) |
| [wb\_accelerometer\_disable](reference/accelerometer.md)(tag) |
| period =
[wb\_accelerometer\_get\_sampling\_period](reference/accelerometer.md)(tag) |
| [x y z] = [wb\_accelerometer\_get\_values](reference/accelerometer.md)(tag) |

| % [Brake](reference/brake.md#brake) : |
| --- |
| [wb\_brake\_set\_damping\_constant](reference/brake.md)(tag, dampingConstant) |
| type = [wb\_brake\_get\_type](reference/brake.md)(tag) |

| % [Camera](reference/camera.md#camera) : |
| --- |
| WB\_CAMERA\_COLOR |
| WB\_CAMERA\_RANGE\_FINDER |
| [wb\_camera\_enable](reference/camera.md)(tag, ms) |
| [wb\_camera\_disable](reference/camera.md)(tag) |
| period = [wb\_camera\_get\_sampling\_period](reference/camera.md)(tag) |
| fov = [wb\_camera\_get\_fov](reference/camera.md)(tag) |
| fov = [wb\_camera\_get\_min\_fov](reference/camera.md)(tag) |
| fov = [wb\_camera\_get\_max\_fov](reference/camera.md)(tag) |
| [wb\_camera\_set\_fov](reference/camera.md)(tag, fov) |
| fov = [wb\_camera\_get\_focal\_length](reference/camera.md)(tag) |
| fov = [wb\_camera\_get\_focal\_distance](reference/camera.md)(tag) |
| fov = [wb\_camera\_get\_max\_focal\_distance](reference/camera.md)(tag) |
| fov = [wb\_camera\_get\_min\_focal\_distance](reference/camera.md)(tag) |
| [wb\_camera\_set\_focal\_distance](reference/camera.md)(tag, focal\_distance) |
| width = [wb\_camera\_get\_width](reference/camera.md)(tag) |
| height = [wb\_camera\_get\_height](reference/camera.md)(tag) |
| near = [wb\_camera\_get\_near](reference/camera.md)(tag) |
| type = [wb\_camera\_get\_type](reference/camera.md)(tag) |
| image = [wb\_camera\_get\_image](reference/camera.md)(tag) |
| image = [wb\_camera\_get\_range\_image](reference/camera.md)(tag) |
| max\_range = [wb\_camera\_get\_max\_range](reference/camera.md)(tag) |
| [wb\_camera\_save\_image](reference/camera.md)(tag, 'filename', quality) |

| % [Compass](reference/compass.md#compass) : |
| --- |
| [wb\_compass\_enable](reference/compass.md)(tag, ms) |
| [wb\_compass\_disable](reference/compass.md)(tag) |
| period = [wb\_compass\_get\_sampling\_period](reference/compass.md)(tag) |
| [x y z] = [wb\_compass\_get\_values](reference/compass.md)(tag) |

| % [Connector](reference/connector.md#connector) : |
| --- |
| [wb\_connector\_enable\_presence](reference/connector.md)(tag, ms) |
| [wb\_connector\_disable\_presence](reference/connector.md)(tag) |
| presence = [wb\_connector\_get\_presence](reference/connector.md)(tag) |
| [wb\_connector\_lock](reference/connector.md)(tag) |
| [wb\_connector\_unlock](reference/connector.md)(tag) |

| % [Device](reference/device.md#device) : |
| --- |
| model = [wb\_device\_get\_model](reference/device.md)(tag) |
| name = [wb\_device\_get\_name](reference/device.md)(tag) |
| type = [wb\_device\_get\_node\_type](reference/device.md)(tag) |

| % [DifferentialWheels](reference/differentialwheels.md#differentialwheels) : |
| --- |
| [wb\_differential\_wheels\_set\_speed](reference/differentialwheels.md)(left,
right) |
| left =
[wb\_differential\_wheels\_get\_left\_speed](reference/differentialwheels.md)() |
| right =
[wb\_differential\_wheels\_get\_right\_speed](reference/differentialwheels.md)() |
| [wb\_differential\_wheels\_enable\_encoders](reference/differentialwheels.md)(ms
) |
| [wb\_differential\_wheels\_disable\_encoders](reference/differentialwheels.md)() |
| period = [wb\_differential\_wheels\_get\_encoders\_sampling\_period](reference/d
ifferentialwheels.md)() |
| left = [wb\_differential\_wheels\_get\_left\_encoder](reference/differentialwhee
ls.md)() |
| right = [wb\_differential\_wheels\_get\_right\_encoder](reference/differentialwh
eels.md)() |
| [wb\_differential\_wheels\_set\_encoders](reference/differentialwheels.md)(left,
right) |
| max =
[wb\_differential\_wheels\_get\_max\_speed](reference/differentialwheels.md)() |
| unit =
[wb\_differential\_wheels\_get\_speed\_unit](reference/differentialwheels.md)() |

| % [Display](reference/display.md#display) : |
| --- |
| RGB |
| RGBA |
| ARGB |
| BGRA |
| width = [wb\_display\_get\_width](reference/display.md)(tag) |
| height = [wb\_display\_get\_height](reference/display.md)(tag) |
| [wb\_display\_set\_color](reference/display.md)(tag, [r g b]) |
| [wb\_display\_set\_alpha](reference/display.md)(tag, alpha) |
| [wb\_display\_set\_opacity](reference/display.md)(tag, opacity) |
| [wb\_display\_draw\_pixel](reference/display.md)(tag, x, y) |
| [wb\_display\_draw\_line](reference/display.md)(tag, x1, y1, x2, y2) |
| [wb\_display\_draw\_rectangle](reference/display.md)(tag, x, y, width, height) |
| [wb\_display\_draw\_oval](reference/display.md)(tag, cx, cy, a, b) |
| [wb\_display\_draw\_polygon](reference/display.md)(tag, [x1 x2 ... xn], [y1 y2
... yn]) |
| [wb\_display\_draw\_text](reference/display.md)(tag, 'txt', x, y) |
| [wb\_display\_fill\_rectangle](reference/display.md)(tag, x, y, width, height) |
| [wb\_display\_fill\_oval](reference/display.md)(tag, cx, cy, a, b) |
| [wb\_display\_fill\_polygon](reference/display.md)(tag, [x1 x2 ... xn], [y1 y2
... yn]) |
| image = [wb\_display\_image\_copy](reference/display.md)(tag, x, y, width,
height) |
| [wb\_display\_image\_paste](reference/display.md)(tag, image, x, y) |
| image = [wb\_display\_image\_load](reference/display.md)(tag, 'filename') |
| image = [wb\_display\_image\_new](reference/display.md)(tag, width, height, data
,format) |
| [wb\_display\_image\_save](reference/display.md)(tag, image, 'filename') |
| [wb\_display\_image\_delete](reference/display.md)(tag, image) |

| % [DistanceSensor](reference/distancesensor.md#distancesensor) : |
| --- |
| [wb\_distance\_sensor\_enable](reference/distancesensor.md)(tag, ms) |
| [wb\_distance\_sensor\_disable](reference/distancesensor.md)(tag) |
| period =
[wb\_distance\_sensor\_get\_sampling\_period](reference/distancesensor.md)(tag) |
| value = [wb\_distance\_sensor\_get\_value](reference/distancesensor.md)(tag) |

| % [Emitter](reference/emitter.md#emitter) : |
| --- |
| WB\_CHANNEL\_BROADCAST |
| [wb\_emitter\_send](reference/emitter.md)(tag, data) |
| [wb\_emitter\_set\_channel](reference/emitter.md)(tag, channel) |
| channel = [wb\_emitter\_get\_channel](reference/emitter.md)(tag) |
| range = [wb\_emitter\_get\_range](reference/emitter.md)(tag) |
| [wb\_emitter\_set\_range](reference/emitter.md)(tag, range) |
| size = [wb\_emitter\_get\_buffer\_size](reference/emitter.md)(tag) |

| % [GPS](reference/gps.md#gps) : |
| --- |
| [wb\_gps\_enable](reference/gps.md)(tag, ms) |
| [wb\_gps\_disable](reference/gps.md)(tag) |
| period = [wb\_gps\_get\_sampling\_period](reference/gps.md)(tag) |
| [x y z] = [wb\_gps\_get\_values](reference/gps.md)(tag) |

| % [Gyro](reference/gyro.md#gyro) : |
| --- |
| [wb\_gyro\_enable](reference/gyro.md)(tag, ms) |
| [wb\_gyro\_disable](reference/gyro.md)(tag) |
| period = [wb\_gyro\_get\_sampling\_period](reference/gyro.md)(tag) |
| [x y z] = [wb\_gyro\_get\_values](reference/gyro.md)(tag) |

| % [InertialUnit](reference/inertialunit.md#inertialunit) : |
| --- |
| [wb\_inertial\_unit\_enable](reference/inertialunit.md)(tag, ms) |
| [wb\_inertial\_unit\_disable](reference/inertialunit.md)(tag) |
| period =
[wb\_inertial\_unit\_get\_sampling\_period](reference/inertialunit.md)(tag) |
| [roll pitch yaw] =
[wb\_inertial\_unit\_get\_roll\_pitch\_yaw](reference/inertialunit.md)(tag) |

| % [LED](reference/led.md#led) : |
| --- |
| [wb\_led\_set](reference/led.md)(tag, state) |
| state = [wb\_led\_get](reference/led.md)(tag) |

| % [LightSensor](reference/lightsensor.md#lightsensor) : |
| --- |
| [wb\_light\_sensor\_enable](reference/lightsensor.md)(tag, ms) |
| [wb\_light\_sensor\_disable](reference/lightsensor.md)(tag) |
| period =
[wb\_light\_sensor\_get\_sampling\_period](reference/lightsensor.md)(tag) |
| value = [wb\_light\_sensor\_get\_value](reference/lightsensor.md)(tag) |

| % [Motion](reference/motion.md#motion) : |
| --- |
| motion = [wbu\_motion\_new](reference/motion.md)('filename') |
| [wbu\_motion\_delete](reference/motion.md)(motion) |
| [wbu\_motion\_play](reference/motion.md)(motion) |
| [wbu\_motion\_stop](reference/motion.md)(motion) |
| [wbu\_motion\_set\_loop](reference/motion.md)(motion, loop) |
| [wbu\_motion\_set\_reverse](reference/motion.md)(motion, reverse) |
| over = [wbu\_motion\_is\_over](reference/motion.md)(motion) |
| duration = [wbu\_motion\_get\_duration](reference/motion.md)(motion) |
| time = [wbu\_motion\_get\_time](reference/motion.md)(motion) |
| [wbu\_motion\_set\_time](reference/motion.md)(motion, time) |

| % [Motor](reference/motor.md#motor) : |
| --- |
| WB\_MOTOR\_ROTATIONAL, WB\_MOTOR\_LINEAR |
| [wb\_motor\_set\_position](reference/motor.md)(tag, position) |
| [wb\_motor\_set\_velocity](reference/motor.md)(tag, vel) |
| [wb\_motor\_set\_acceleration](reference/motor.md)(tag, acc) |
| [wb\_motor\_set\_available\_force](reference/motor.md)(tag, force) |
| [wb\_motor\_set\_available\_torque](reference/motor.md)(tag, torque) |
| [wb\_motor\_set\_control\_pid](reference/motor.md)(tag, p, i, d) |
| target = [wb\_motor\_get\_target\_position](reference/motor.md)(tag) |
| min = [wb\_motor\_get\_min\_position](reference/motor.md)(tag) |
| max = [wb\_motor\_get\_max\_position](reference/motor.md)(tag) |
| vel = [wb\_motor\_get\_velocity](reference/motor.md)(tag) |
| vel = [wb\_motor\_get\_max\_velocity](reference/motor.md)(tag) |
| acc = [wb\_motor\_get\_acceleration](reference/motor.md)(tag) |
| force = [wb\_motor\_get\_available\_force](reference/motor.md)(tag) |
| force = [wb\_motor\_get\_max\_force](reference/motor.md)(tag) |
| torque = [wb\_motor\_get\_available\_torque](reference/motor.md)(tag) |
| torque = [wb\_motor\_get\_max\_torque](reference/motor.md)(tag) |
| [wb\_motor\_enable\_force\_feedback](reference/motor.md)(tag, ms) |
| [wb\_motor\_disable\_force\_feedback](reference/motor.md)(tag) |
| period =
[wb\_motor\_get\_force\_feedback\_sampling\_period](reference/motor.md)(tag) |
| force = [wb\_motor\_get\_force\_feedback](reference/motor.md)(tag) |
| [wb\_motor\_set\_force](reference/motor.md)(tag, force) |
| [wb\_motor\_enable\_torque\_feedback](reference/motor.md)(tag, ms) |
| [wb\_motor\_disable\_torque\_feedback](reference/motor.md)(tag) |
| period =
[wb\_motor\_get\_torque\_feedback\_sampling\_period](reference/motor.md)(tag) |
| force = [wb\_motor\_get\_torque\_feedback](reference/motor.md)(tag) |
| [wb\_motor\_set\_torque](reference/motor.md)(tag, torque) |
| type = [wb\_motor\_get\_type](reference/motor.md)(tag) |

| Node: |
| --- |
| WB\_NODE\_NO\_NODE, WB\_NODE\_APPEARANCE, WB\_NODE\_BACKGROUND, |
| WB\_NODE\_BOX, WB\_NODE\_COLOR, WB\_NODE\_CONE, |
| WB\_NODE\_COORDINATE,  WB\_NODE\_CYLINDER, |
| WB\_NODE\_DIRECTIONAL\_LIGHT, WB\_NODE\_ELEVATION\_GRID, |
| WB\_NODE\_EXTRUSION, WB\_NODE\_FOG, WB\_NODE\_GROUP, |
| WB\_NODE\_IMAGE\_TEXTURE, WB\_NODE\_INDEXED\_FACE\_SET, |
| WB\_NODE\_INDEXED\_LINE\_SET, WB\_NODE\_MATERIAL, |
| WB\_NODE\_POINT\_LIGHT,  WB\_NODE\_SHAPE, WB\_NODE\_SPHERE, |
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

| % [Pen](reference/pen.md#pen) : |
| --- |
| [wb\_pen\_write](reference/pen.md)(tag, write) |
| [wb\_pen\_set\_ink\_color](reference/pen.md)(tag, [r g b], density) |

| % [PositionSensor](reference/positionsensor.md#positionsensor) : |
| --- |
| WB\_ANGULAR, WB\_LINEAR |
| [wb\_position\_sensor\_enable](reference/positionsensor.md)(tag, ms) |
| [wb\_position\_sensor\_disable](reference/positionsensor.md)(tag) |
| period =
[wb\_position\_sensor\_get\_sampling\_period](reference/positionsensor.md)(tag) |
| value = [wb\_position\_sensor\_get\_value](reference/positionsensor.md)(tag) |
| type = [wb\_position\_sensor\_get\_type](reference/positionsensor.md)(tag) |

| % [Receiver](reference/receiver.md#receiver) : |
| --- |
| WB\_CHANNEL\_BROADCAST |
| [wb\_receiver\_enable](reference/receiver.md)(tag, ms) |
| [wb\_receiver\_disable](reference/receiver.md)(tag) |
| period = [wb\_receiver\_get\_sampling\_period](reference/receiver.md)(tag) |
| length = [wb\_receiver\_get\_queue\_length](reference/receiver.md)(tag) |
| [wb\_receiver\_next\_packet](reference/receiver.md)(tag) |
| size = [wb\_receiver\_get\_data\_size](reference/receiver.md)(tag) |
| data = [wb\_receiver\_get\_data](reference/receiver.md)(tag) |
| strength = [wb\_receiver\_get\_signal\_strength](reference/receiver.md)(tag) |
| [x y z] = [wb\_receiver\_get\_emitter\_direction](reference/receiver.md)(tag) |
| [wb\_receiver\_set\_channel](reference/receiver.md)(tag, channel) |
| channel = [wb\_receiver\_get\_channel](reference/receiver.md)(tag) |

| % [Robot](reference/robot.md#robot) : |
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
| [wb\_robot\_step](reference/robot.md)(ms) |
| tag = [wb\_robot\_get\_device](reference/robot.md)('name') |
| &nbsp;&nbsp; size = [wb\_robot\_get\_number\_of\_devices](reference/robot.md)() |
| &nbsp;&nbsp; tag =
[wb\_robot\_get\_device\_by\_index](reference/robot.md)(index) |
| [wb\_robot\_battery\_sensor\_enable](reference/robot.md)(ms) |
| [wb\_robot\_battery\_sensor\_disable](reference/robot.md)() |
| period =
[wb\_robot\_battery\_sensor\_get\_sampling\_period](reference/robot.md)() |
| value = [wb\_robot\_battery\_sensor\_get\_value](reference/robot.md)() |
| step = [wb\_robot\_get\_basic\_time\_step](reference/robot.md)() |
| mode = [wb\_robot\_get\_mode](reference/robot.md)() |
| model = [wb\_robot\_get\_model](reference/robot.md)() |
| &nbsp;&nbsp; data = [getData](reference/robot.md)() |
| &nbsp;&nbsp; [setData](reference/robot.md)('data') |
| name = [wb\_robot\_get\_name](reference/robot.md)() |
| name = [wb\_robot\_get\_controller\_name](reference/robot.md)() |
| name = [wb\_robot\_get\_controller\_arguments](reference/robot.md)() |
| path = [wb\_robot\_get\_project\_path](reference/robot.md)() |
| sync = [wb\_robot\_get\_synchronization](reference/robot.md)() |
| time = [wb\_robot\_get\_time](reference/robot.md)() |
| path = [wb\_robot\_get\_world\_path](reference/robot.md)() |
| [wb\_robot\_keyboard\_enable](reference/robot.md)(ms) |
| [wb\_robot\_keyboard\_disable](reference/robot.md)() |
| key = [wb\_robot\_keyboard\_get\_key](reference/robot.md)() |
| type = [wb\_robot\_get\_type](reference/robot.md)() |

| % [Servo](reference/servo.md#servo) : |
| --- |
| WB\_SERVO\_ROTATIONAL, WB\_SERVO\_LINEAR |
| [wb\_servo\_set\_position](reference/servo.md)(tag, position) |
| target = [wb\_servo\_get\_target\_position](reference/servo.md)(tag) |
| [wb\_servo\_set\_velocity](reference/servo.md)(tag, vel) |
| [wb\_servo\_set\_acceleration](reference/servo.md)(tag, acc) |
| [wb\_servo\_set\_motor\_force](reference/servo.md)(tag, force) |
| [wb\_servo\_set\_control\_p](reference/servo.md)(tag, p) |
| min = [wb\_servo\_get\_min\_position](reference/servo.md)(tag) |
| max = [wb\_servo\_get\_max\_position](reference/servo.md)(tag) |
| [wb\_servo\_enable\_position](reference/servo.md)(tag, ms) |
| [wb\_servo\_disable\_position](reference/servo.md)(tag) |
| period = [wb\_servo\_get\_position\_sampling\_period](reference/servo.md)(tag) |
| position = [wb\_servo\_get\_position](reference/servo.md)(tag) |
| [wb\_servo\_enable\_motor\_force\_feedback](reference/servo.md)(tag, ms) |
| [wb\_servo\_disable\_motor\_force\_feedback](reference/servo.md)(tag) |
| period = [wb\_servo\_get\_motor\_force\_feedback\_sampling\_period](reference/se
rvo.md)(tag) |
| force = [wb\_servo\_get\_motor\_force\_feedback](reference/servo.md)(tag) |
| [wb\_servo\_set\_force](reference/servo.md)(tag, force) |
| type = [wb\_servo\_get\_type](reference/servo.md)(tag) |

| % [Supervisor](reference/supervisor.md#supervisor) : |
| --- |
| WB\_SF\_BOOL, WB\_SF\_INT32, WB\_SF\_FLOAT, WB\_SF\_VEC2F, |
| WB\_SF\_VEC3F, WB\_SF\_ROTATION, WB\_SF\_COLOR, WB\_SF\_STRING, |
| WB\_SF\_NODE, WB\_MF, WB\_MF\_INT32, WB\_MF\_FLOAT, B\_MF\_VEC2F, |
| WB\_MF\_VEC3F, WB\_MF\_COLOR, WB\_MF\_STRING, WB\_MF\_NODE |
| WB\_SUPERVISOR\_MOVIE\_READY, WB\_SUPERVISOR\_MOVIE\_RECORDING,
WB\_SUPERVISOR\_MOVIE\_SAVING, WB\_SUPERVISOR\_MOVIE\_WRITE\_ERROR,
WB\_SUPERVISOR\_MOVIE\_ENCODING\_ERROR, WB\_SUPERVISOR\_MOVIE\_SIMULATION\_ERROR |
| [wb\_supervisor\_export\_image](reference/supervisor.md)('filename', quality) |
| node = [wb\_supervisor\_node\_get\_root](reference/supervisor.md)() |
| node = [wb\_supervisor\_node\_get\_self](reference/supervisor.md)() |
| node = [wb\_supervisor\_node\_get\_from\_def](reference/supervisor.md)('def') |
| node = [wb\_supervisor\_node\_get\_from\_id](reference/supervisor.md)('id') |
| id = [wb\_supervisor\_node\_get\_id](reference/supervisor.md)(node) |
| node = [wb\_supervisor\_node\_get\_parent\_node](reference/supervisor.md)(node) |
| [wb\_supervisor\_node\_remove](reference/supervisor.md)(node) |
| [wb\_supervisor\_set\_label](reference/supervisor.md)(id, 'text', x, y, size, [r
g b], transparency) |
| [wb\_supervisor\_simulation\_quit](reference/supervisor.md)(status) |
| [wb\_supervisor\_simulation\_revert](reference/supervisor.md)() |
| [wb\_supervisor\_simulation\_reset\_physics](reference/supervisor.md)() |
| [wb\_supervisor\_load\_world](reference/supervisor.md)('filename') |
| [wb\_supervisor\_save\_world](reference/supervisor.md)() |
| [wb\_supervisor\_save\_world](reference/supervisor.md)('filename') |
| [wb\_supervisor\_movie\_start\_recording](reference/supervisor.md)('filename',
width, height, codec, quality, |
| acceleration, caption) |
| [wb\_supervisor\_movie\_stop\_recording](reference/supervisor.md)() |
| status = [wb\_supervisor\_movie\_get\_status](reference/supervisor.md)() |
| success = [wb\_supervisor\_animation\_start\_recording](reference/supervisor.md)
('filename') |
| success =
[wb\_supervisor\_animation\_stop\_recording](reference/supervisor.md)() |
| type = [wb\_supervisor\_field\_get\_type](reference/supervisor.md)(field) |
| name = [wb\_supervisor\_field\_get\_type\_name](reference/supervisor.md)(field) |
| count = [wb\_supervisor\_field\_get\_count](reference/supervisor.md)(field) |
| b = [wb\_supervisor\_field\_get\_sf\_bool](reference/supervisor.md)(field) |
| i = [wb\_supervisor\_field\_get\_sf\_int32](reference/supervisor.md)(field) |
| f = [wb\_supervisor\_field\_get\_sf\_float](reference/supervisor.md)(field) |
| [x y] = [wb\_supervisor\_field\_get\_sf\_vec2f](reference/supervisor.md)(field) |
| [x y z] =
[wb\_supervisor\_field\_get\_sf\_vec3f](reference/supervisor.md)(field) |
| [x y z alpha] =
[wb\_supervisor\_field\_get\_sf\_rotation](reference/supervisor.md)(field) |
| [r g b] =
[wb\_supervisor\_field\_get\_sf\_color](reference/supervisor.md)(field) |
| s = [wb\_supervisor\_field\_get\_sf\_string](reference/supervisor.md)(field) |
| node = [wb\_supervisor\_field\_get\_sf\_node](reference/supervisor.md)(field) |
| b = [wb\_supervisor\_field\_get\_mf\_bool](reference/supervisor.md)(field,
index) |
| i = [wb\_supervisor\_field\_get\_mf\_int32](reference/supervisor.md)(field,
index) |
| f = [wb\_supervisor\_field\_get\_mf\_float](reference/supervisor.md)(field,
index) |
| [x y] = [wb\_supervisor\_field\_get\_mf\_vec2f](reference/supervisor.md)(field,
index) |
| [x y z] =
[wb\_supervisor\_field\_get\_mf\_vec3f](reference/supervisor.md)(field, index) |
| [x y z a] =
[wb\_supervisor\_field\_get\_mf\_rotation](reference/supervisor.md)(field,
index) |
| [r g b] =
[wb\_supervisor\_field\_get\_mf\_color](reference/supervisor.md)(field, index) |
| s = [wb\_supervisor\_field\_get\_mf\_string](reference/supervisor.md)(field,
index) |
| node = [wb\_supervisor\_field\_get\_mf\_node](reference/supervisor.md)(field,
index) |
| [wb\_supervisor\_field\_set\_sf\_bool](reference/supervisor.md)(field, value) |
| [wb\_supervisor\_field\_set\_sf\_int32](reference/supervisor.md)(field, value) |
| [wb\_supervisor\_field\_set\_sf\_float](reference/supervisor.md)(field, value) |
| [wb\_supervisor\_field\_set\_sf\_vec2f](reference/supervisor.md)(field, [x y]) |
| [wb\_supervisor\_field\_set\_sf\_vec3f](reference/supervisor.md)(field, [x y z]) |
| [wb\_supervisor\_field\_set\_sf\_rotation](reference/supervisor.md)(field, [x y
z alpha]) |
| [wb\_supervisor\_field\_set\_sf\_color](reference/supervisor.md)(field, [r g b]) |
| [wb\_supervisor\_field\_set\_sf\_string](reference/supervisor.md)(field,
'value') |
| [wb\_supervisor\_field\_set\_mf\_bool](reference/supervisor.md)(field, index,
value) |
| [wb\_supervisor\_field\_set\_mf\_int32](reference/supervisor.md)(field, index,
value) |
| [wb\_supervisor\_field\_set\_mf\_float](reference/supervisor.md)(field, index,
value) |
| [wb\_supervisor\_field\_set\_mf\_vec2f](reference/supervisor.md)(field, index,
[x y]) |
| [wb\_supervisor\_field\_set\_mf\_vec3f](reference/supervisor.md)(field, index,
[x y z]) |
| [wb\_supervisor\_field\_set\_mf\_rotation](reference/supervisor.md)(field,
index, [x y z a]) |
| [wb\_supervisor\_field\_set\_mf\_color](reference/supervisor.md)(field, index,
[r g b]) |
| [wb\_supervisor\_field\_set\_mf\_string](reference/supervisor.md)(field, index,
'value') |
| [wb\_supervisor\_field\_import\_mf\_node](reference/supervisor.md)(field,
position, 'filename') |
| [wb\_supervisor\_field\_import\_mf\_node\_from\_string](reference/supervisor.md)
(field, position, 'node\_string') |
| [wb\_supervisor\_field\_remove\_mf\_node](reference/supervisor.md)(field,
position) |
| type = [wb\_supervisor\_node\_get\_type](reference/supervisor.md)(node) |
| name = [wb\_supervisor\_node\_get\_type\_name](reference/supervisor.md)(node) |
| name =
[wb\_supervisor\_node\_get\_base\_type\_name](reference/supervisor.md)(node) |
| field = [wb\_supervisor\_node\_get\_field](reference/supervisor.md)(node,
'field\_name') |
| position = [wb\_supervisor\_node\_get\_position](reference/supervisor.md)(node) |
| orientation =
[wb\_supervisor\_node\_get\_orientation](reference/supervisor.md)(node) |
| com =
[wb\_supervisor\_node\_get\_center\_of\_mass](reference/supervisor.md)(node) |
| contact\_point =
[wb\_supervisor\_node\_get\_contact\_point](reference/supervisor.md)(node,
index) |
| number\_of\_contacts = [wb\_supervisor\_node\_get\_number\_of\_contact\_points](
reference/supervisor.md)(index) |
| balance =
[wb\_supervisor\_node\_get\_static\_balance](reference/supervisor.md)(node) |
| velocity = [wb\_supervisor\_node\_get\_velocity](reference/supervisor.md)(node) |
| [wb\_supervisor\_node\_set\_velocity](reference/supervisor.md)(node, velocity) |
| [wb\_supervisor\_node\_reset\_physics](reference/supervisor.md)(node) |

| % [TouchSensor](reference/touchsensor.md#touchsensor) : |
| --- |
| WB\_TOUCH\_SENSOR\_BUMPER, WB\_TOUCH\_SENSOR\_FORCE, |
| WB\_TOUCH\_SENSOR\_FORCE3D |
| [wb\_touch\_sensor\_enable](reference/touchsensor.md)(tag, ms) |
| [wb\_touch\_sensor\_disable](reference/touchsensor.md)(tag) |
| period =
[wb\_touch\_sensor\_get\_sampling\_period](reference/touchsensor.md)(tag) |
| value = [wb\_touch\_sensor\_get\_value](reference/touchsensor.md)(tag) |
| [x y z] = [wb\_touch\_sensor\_get\_values](reference/touchsensor.md)(tag) |
| type = [wb\_touch\_sensor\_get\_type](reference/touchsensor.md)(tag) |

