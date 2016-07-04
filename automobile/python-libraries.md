## Python library

The `automobile` library provides a Python wrapper of the C libraries `libdriver` and `libcar`.

### Driver

The `Driver` class provides the following methods:

%api "python_driver"

|                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------- |
| from automobile import Driver                                                                                       |
| class [Driver](driver-library.md) (Robot) :                                                                         |
| &nbsp;&nbsp; INDICATOR\_OFF, INDICATOR\_RIGHT, INDICATOR\_LEFT                                                      |
| &nbsp;&nbsp; SPEED, TORQUE                                                                                          |
| &nbsp;&nbsp; def [step](driver-library.md#wbu_driver_step)(self)                                                    |
| &nbsp;&nbsp; def [setSteeringAngle](driver-library.md#wbu_driver_set_steering_angle)(self, steeringAngle)           |
| &nbsp;&nbsp; def [getSteeringAngle](driver-library.md#wbu_driver_set_steering_angle)(self)                          |
| &nbsp;&nbsp; def [setCruisingSpeed](driver-library.md#wbu_driver_set_cruising_speed)(self, speed)                   |
| &nbsp;&nbsp; def [getTargetCruisingSpeed](driver-library.md#wbu_driver_set_cruising_speed)(self)                    |
| &nbsp;&nbsp; def [getCurrentSpeed](driver-library.md#wbu_driver_get_current_speed)(self)                            |
| &nbsp;&nbsp; def [setThrottle](driver-library.md#wbu_driver_set_throttle)(self, throttle)                           |
| &nbsp;&nbsp; def [getThrottle](driver-library.md#wbu_driver_set_throttle)(self)                                     |
| &nbsp;&nbsp; def [setBrake](driver-library.md#wbu_driver_set_brake)(self, brake)                                    |
| &nbsp;&nbsp; def [getBrake](driver-library.md#wbu_driver_set_brake)(self)                                           |
| &nbsp;&nbsp; def [setIndicator](driver-library.md#wbu_driver_set_indicator)(self, state)                            |
| &nbsp;&nbsp; def [setHazardFlashers](driver-library.md#wbu_driver_set_indicator)(self, state)                       |
| &nbsp;&nbsp; def [getIndicator](driver-library.md#wbu_driver_set_indicator)(self)                                   |
| &nbsp;&nbsp; def [getHazardFlashers](driver-library.md#wbu_driver_set_indicator)(self)                              |
| &nbsp;&nbsp; def [setDippedBeams](driver-library.md#wbu_driver_set_dipped_beams)(self, state)                       |
| &nbsp;&nbsp; def [setAntifogLights](driver-library.md#wbu_driver_set_dipped_beams)(self, state)                     |
| &nbsp;&nbsp; def [getDippedBeams](driver-library.md#wbu_driver_set_dipped_beams)(self)                              |
| &nbsp;&nbsp; def [getAntifogLights](driver-library.md#wbu_driver_set_dipped_beams)(self)                            |
| &nbsp;&nbsp; def [getRpm](driver-library.md#wbu_driver_get_rpm)(self)                                               |
| &nbsp;&nbsp; def [getGear](driver-library.md#wbu_driver_set_gear)(self)                                             |
| &nbsp;&nbsp; def [setGear](driver-library.md#wbu_driver_set_gear)(self, gear)                                       |
| &nbsp;&nbsp; def [getGearNumber](driver-library.md#wbu_driver_set_gear)(self)                                       |
| &nbsp;&nbsp; def [getControlMode](driver-library.md#wbu_driver_get_control_mode)(self)                              |

%end

### Car

The `Car` class inherits from the `Driver` class and provides the following
methods:

%api "python_car"

|                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------- |
| from automobile import Car                                                                                                   |
| public class [Car](car-library.md) ([Driver](#python_driver)) :                                                              |
| &nbsp;&nbsp; TRACTION, PROPULSION, FOUR\_BY\_FOUR                                                                            |
| &nbsp;&nbsp; COMBUTSION\_ENGINE, ELECTRIC\_ENGINE, PARALLEL\_HYBRID\_ENGINE, POWER\_SPLIT\_HYBRID\_ENGINE                    |
| &nbsp;&nbsp; WHEEL\_FRONT\_RIGHT, WHEEL\_FRONT\_LEFT, WHEEL\_REAR\_RIGHT, WHEEL\_REAR\_LEFT, WHEEL\_NB                       |
| &nbsp;&nbsp; def [getType](car-library.md#wbu_car_get_type)(self)                                                            |
| &nbsp;&nbsp; def [getEngineType](car-library.md#wbu_car_get_type)(self)                                                      |
| &nbsp;&nbsp; def [setIndicatorPeriod](car-library.md#wbu_car_set_indicator_period)(self, period)                             |
| &nbsp;&nbsp; def [getIndicatorPeriod](car-library.md#wbu_car_set_indicator_period)(self)                                     |
| &nbsp;&nbsp; def [getBackwardsLights](car-library.md#wbu_car_get_backwards_lights)(self)                                     |
| &nbsp;&nbsp; def [getBrakeLights](car-library.md#wbu_car_get_backwards_lights)(self)                                         |
| &nbsp;&nbsp; def [getTrackFront](car-library.md#wbu_car_get_track_front)(self)                                               |
| &nbsp;&nbsp; def [getTrackRear](car-library.md#wbu_car_get_track_front)(self)                                                |
| &nbsp;&nbsp; def [getWheelbase](car-library.md#wbu_car_get_track_front)(self)                                                |
| &nbsp;&nbsp; def [getFrontWheelRadius](car-library.md#wbu_car_get_track_front)(self)                                         |
| &nbsp;&nbsp; def [getRearWheelRadius](car-library.md#wbu_car_get_track_front)(self)                                          |
| &nbsp;&nbsp; def [getWheelEncoder](car-library.md#wbu_car_get_wheel_encoder)(self, wheel)                                    |
| &nbsp;&nbsp; def [getWheelSpeed](car-library.md#wbu_car_get_wheel_encoder)(self, wheel)                                      |
| &nbsp;&nbsp; def [getRightSteeringAngle](car-library.md#wbu_car_get_right_steering_angle)(self)                              |
| &nbsp;&nbsp; def [getLeftSteeringAngle](car-library.md#wbu_car_get_right_steering_angle)(self)                               |
| &nbsp;&nbsp; def [enableLimitedSlipDifferential](car-library.md#wbu_car_enable_limited_slip_differential)(self, enable)      |
| &nbsp;&nbsp; def [enableIndicatorAutoDisabling](car-library.md#wbu_car_enable_indicator_auto_disabling)(self, enable)        |

%end
