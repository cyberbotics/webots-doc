## C++ libraries

The two libraries (`libCppDriver` and `libCppCar`) provide a C++ wrapper of the C libraries `libdriver` and `libcar`.

### CppDriver

The `Driver` class provides the following methods:

%api "cpp_driver"

|                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Driver.hpp`>`                                                                             |
| class [Driver](driver-library.md) {                                                                          |
| &nbsp;&nbsp; enum {INDICATOR\_OFF, INDICATOR\_RIGHT, INDICATOR\_LEFT};                                       |
| &nbsp;&nbsp; enum {SPEED, TORQUE };                                                                          |
| &nbsp;&nbsp; enum {DOWN, SLOW, NORMAL, FAST};                                                                |
| &nbsp;&nbsp; virtual int [step](driver-library.md#wbu_driver_step)();                                        |
| &nbsp;&nbsp; void [setSteeringAngle](driver-library.md#wbu_driver_set_steering_angle)(double steeringAngle); |
| &nbsp;&nbsp; double [getSteeringAngle](driver-library.md#wbu_driver_set_steering_angle)();                   |
| &nbsp;&nbsp; void [setCruisingSpeed](driver-library.md#wbu_driver_set_cruising_speed)(double speed);         |
| &nbsp;&nbsp; double [getTargetCruisingSpeed](driver-library.md#wbu_driver_set_cruising_speed)();             |
| &nbsp;&nbsp; double [getCurrentSpeed](driver-library.md#wbu_driver_get_current_speed)();                     |
| &nbsp;&nbsp; void [setThrottle](driver-library.md#wbu_driver_set_throttle)(double throttle);                 |
| &nbsp;&nbsp; double [getThrottle](driver-library.md#wbu_driver_set_throttle)();                              |
| &nbsp;&nbsp; void [setBrakeIntensity](driver-library.md#wbu_driver_set_brake_intensity)(double intensity);   |
| &nbsp;&nbsp; double [getBrakeIntensity](driver-library.md#wbu_driver_set_brake_intensity)();                 |
| &nbsp;&nbsp; void [setIndicator](driver-library.md#wbu_driver_set_indicator)(int state);                     |
| &nbsp;&nbsp; void [setHazardFlashers](driver-library.md#wbu_driver_set_indicator)(bool state);               |
| &nbsp;&nbsp; int [getIndicator](driver-library.md#wbu_driver_set_indicator)();                               |
| &nbsp;&nbsp; bool [getHazardFlashers](driver-library.md#wbu_driver_set_indicator)();                         |
| &nbsp;&nbsp; void [setDippedBeams](driver-library.md#wbu_driver_set_dipped_beams)(bool state);               |
| &nbsp;&nbsp; void [setAntifogLights](driver-library.md#wbu_driver_set_dipped_beams)(bool state);             |
| &nbsp;&nbsp; bool [getDippedBeams](driver-library.md#wbu_driver_set_dipped_beams)();                         |
| &nbsp;&nbsp; bool [getAntifogLights](driver-library.md#wbu_driver_set_dipped_beams)();                       |
| &nbsp;&nbsp; double [getRpm](driver-library.md#wbu_driver_get_rpm)();                                        |
| &nbsp;&nbsp; int [getGear](driver-library.md#wbu_driver_set_gear)();                                         |
| &nbsp;&nbsp; void [setGear](driver-library.md#wbu_driver_set_gear)(int gear);                                |
| &nbsp;&nbsp; int [getGearNumber](driver-library.md#wbu_driver_set_gear)();                                   |
| &nbsp;&nbsp; int [getControlMode](driver-library.md#wbu_driver_get_control_mode)();                          |
| &nbsp;&nbsp; void [setWipersMode](driver-library.md#wbu_driver_set_wipers_mode)(int mode);                   |
| &nbsp;&nbsp; int [getWipersMode](driver-library.md#wbu_driver_set_wipers_mode)();                            |
| };                                                                                                           |

%end

### CppCar

The `Car` class inherits from the `Driver` class and provides the following methods:

%api "cpp_car"

|                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ |
| #include `<`webots/Car.hpp`>`                                                                                            |
| class [Car](car-library.md) : public [Driver](#cppdriver) {                                                              |
| &nbsp;&nbsp; enum { TRACTION, PROPULSION=1, FOUR\_BY\_FOUR=2};                                                           |
| &nbsp;&nbsp; enum { COMBUTSION\_ENGINE, ELECTRIC\_ENGINE, PARALLEL\_HYBRID\_ENGINE, POWER\_SPLIT\_HYBRID\_ENGINE };      |
| &nbsp;&nbsp; enum { WHEEL\_FRONT\_RIGHT, WHEEL\_FRONT\_LEFT, WHEEL\_REAR\_RIGHT, WHEEL\_REAR\_LEFT, WHEEL\_NB };         |
| &nbsp;&nbsp; int [getType](car-library.md#wbu_car_get_type)();                                                           |
| &nbsp;&nbsp; int [getEngineType](car-library.md#wbu_car_get_type)();                                                     |
| &nbsp;&nbsp; void [setIndicatorPeriod](car-library.md#wbu_car_set_indicator_period)(double period);                      |
| &nbsp;&nbsp; double [getIndicatorPeriod](car-library.md#wbu_car_set_indicator_period)();                                 |
| &nbsp;&nbsp; bool [getBackwardsLights](car-library.md#wbu_car_get_backwards_lights)();                                   |
| &nbsp;&nbsp; bool [getBrakeLights](car-library.md#wbu_car_get_backwards_lights)();                                       |
| &nbsp;&nbsp; double [getTrackFront](car-library.md#wbu_car_get_track_front)();                                           |
| &nbsp;&nbsp; double [getTrackRear](car-library.md#wbu_car_get_track_front)();                                            |
| &nbsp;&nbsp; double [getWheelbase](car-library.md#wbu_car_get_track_front)();                                            |
| &nbsp;&nbsp; double [getFrontWheelRadius](car-library.md#wbu_car_get_track_front)();                                     |
| &nbsp;&nbsp; double [getRearWheelRadius](car-library.md#wbu_car_get_track_front)();                                      |
| &nbsp;&nbsp; double [getWheelEncoder](car-library.md#wbu_car_get_wheel_encoder)(int wheel);                              |
| &nbsp;&nbsp; double [getWheelSpeed](car-library.md#wbu_car_get_wheel_encoder)(int wheel);                                |
| &nbsp;&nbsp; double [getRightSteeringAngle](car-library.md#wbu_car_get_right_steering_angle)();                          |
| &nbsp;&nbsp; double [getLeftSteeringAngle](car-library.md#wbu_car_get_right_steering_angle)();                           |
| &nbsp;&nbsp; void [enableLimitedSlipDifferential](car-library.md#wbu_car_enable_limited_slip_differential)(bool enable); |
| &nbsp;&nbsp; void [enableIndicatorAutoDisabling](car-library.md#wbu_car_enable_indicator_auto_disabling)(bool enable);   |
| };                                                                                                                       |

%end
