## Java library

The `automobile` library provides a Java wrapper of the C libraries `libdriver` and `libcar`.

### Driver

The `Driver` class provides the following methods:

%api "java_driver"

|                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Driver;                                                                    |
| public class [Driver](driver-library.md) {                                                                          |
| &nbsp;&nbsp; public final static int INDICATOR\_OFF, INDICATOR\_RIGHT, INDICATOR\_LEFT;                             |
| &nbsp;&nbsp; public final static int SPEED, TORQUE;                                                                 |
| &nbsp;&nbsp; public int [step](driver-library.md#wbu_driver_step)();                                                |
| &nbsp;&nbsp; public void [setSteeringAngle](driver-library.md#wbu_driver_set_steering_angle)(double steeringAngle); |
| &nbsp;&nbsp; public double [getSteeringAngle](driver-library.md#wbu_driver_set_steering_angle)();                   |
| &nbsp;&nbsp; public void [setCruisingSpeed](driver-library.md#wbu_driver_set_cruising_speed)(double speed);         |
| &nbsp;&nbsp; public double [getTargetCruisingSpeed](driver-library.md#wbu_driver_set_cruising_speed)();             |
| &nbsp;&nbsp; public double [getCurrentSpeed](driver-library.md#wbu_driver_get_current_speed)();                     |
| &nbsp;&nbsp; public void [setThrottle](driver-library.md#wbu_driver_set_throttle)(double throttle);                 |
| &nbsp;&nbsp; public double [getThrottle](driver-library.md#wbu_driver_set_throttle)();                              |
| &nbsp;&nbsp; public void [setBrake](driver-library.md#wbu_driver_set_brake)(double brake);                          |
| &nbsp;&nbsp; public double [getBrake](driver-library.md#wbu_driver_set_brake)();                                    |
| &nbsp;&nbsp; public void [setIndicator](driver-library.md#wbu_driver_set_indicator)(int state);                     |
| &nbsp;&nbsp; public void [setHazardFlashers](driver-library.md#wbu_driver_set_indicator)(bool state);               |
| &nbsp;&nbsp; public int [getIndicator](driver-library.md#wbu_driver_set_indicator)();                               |
| &nbsp;&nbsp; public bool [getHazardFlashers](driver-library.md#wbu_driver_set_indicator)();                         |
| &nbsp;&nbsp; public void [setDippedBeams](driver-library.md#wbu_driver_set_dipped_beams)(bool state);               |
| &nbsp;&nbsp; public void [setAntifogLights](driver-library.md#wbu_driver_set_dipped_beams)(bool state);             |
| &nbsp;&nbsp; public bool [getDippedBeams](driver-library.md#wbu_driver_set_dipped_beams)();                         |
| &nbsp;&nbsp; public bool [getAntifogLights](driver-library.md#wbu_driver_set_dipped_beams)();                       |
| &nbsp;&nbsp; public double [getRpm](driver-library.md#wbu_driver_get_rpm)();                                        |
| &nbsp;&nbsp; public int [getGear](driver-library.md#wbu_driver_set_gear)();                                         |
| &nbsp;&nbsp; public void [setGear](driver-library.md#wbu_driver_set_gear)(int gear);                                |
| &nbsp;&nbsp; public int [getGearNumber](driver-library.md#wbu_driver_set_gear)();                                   |
| &nbsp;&nbsp; public int [getControlMode](driver-library.md#wbu_driver_get_control_mode)();                          |
| }                                                                                                                   |

%end

### Car

The `Car` class inherits from the `Driver` class and provides the following
methods:

%api "java_car"

|                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| import com.cyberbotics.webots.controller.Car;                                                                                       |
| public class [Car](car-library.md) extends [Driver](#java_driver) {                                                                 |
| &nbsp;&nbsp; public final static int TRACTION, PROPULSION, FOUR\_BY\_FOUR;                                                          |
| &nbsp;&nbsp; public final static int COMBUTSION\_ENGINE, ELECTRIC\_ENGINE, PARALLEL\_HYBRID\_ENGINE, POWER\_SPLIT\_HYBRID\_ENGINE;  |
| &nbsp;&nbsp; public final static int WHEEL\_FRONT\_RIGHT, WHEEL\_FRONT\_LEFT, WHEEL\_REAR\_RIGHT, WHEEL\_REAR\_LEFT, WHEEL\_NB;     |
| &nbsp;&nbsp; public int [getType](car-library.md#wbu_car_get_type)();                                                               |
| &nbsp;&nbsp; public int [getEngineType](car-library.md#wbu_car_get_type)();                                                         |
| &nbsp;&nbsp; public void [setIndicatorPeriod](car-library.md#wbu_car_set_indicator_period)(double period);                          |
| &nbsp;&nbsp; public double [getIndicatorPeriod](car-library.md#wbu_car_set_indicator_period)();                                     |
| &nbsp;&nbsp; public bool [getBackwardsLights](car-library.md#wbu_car_get_backwards_lights)();                                       |
| &nbsp;&nbsp; public bool [getBrakeLights](car-library.md#wbu_car_get_backwards_lights)();                                           |
| &nbsp;&nbsp; public double [getTrackFront](car-library.md#wbu_car_get_track_front)();                                               |
| &nbsp;&nbsp; public double [getTrackRear](car-library.md#wbu_car_get_track_front)();                                                |
| &nbsp;&nbsp; public double [getWheelbase](car-library.md#wbu_car_get_track_front)();                                                |
| &nbsp;&nbsp; public double [getFrontWheelRadius](car-library.md#wbu_car_get_track_front)();                                         |
| &nbsp;&nbsp; public double [getRearWheelRadius](car-library.md#wbu_car_get_track_front)();                                          |
| &nbsp;&nbsp; public double [getWheelEncoder](car-library.md#wbu_car_get_wheel_encoder)(int wheel);                                  |
| &nbsp;&nbsp; public double [getWheelSpeed](car-library.md#wbu_car_get_wheel_encoder)(int wheel);                                    |
| &nbsp;&nbsp; public double [getRightSteeringAngle](car-library.md#wbu_car_get_right_steering_angle)();                              |
| &nbsp;&nbsp; public double [getLeftSteeringAngle](car-library.md#wbu_car_get_right_steering_angle)();                               |
| &nbsp;&nbsp; public void [enableLimitedSlipDifferential](car-library.md#wbu_car_enable_limited_slip_differential)(bool enable);     |
| &nbsp;&nbsp; public void [enableIndicatorAutoDisabling](car-library.md#wbu_car_enable_indicator_auto_disabling)(bool enable);       |
| }                                                                                                                                   |

%end

