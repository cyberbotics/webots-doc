## Car

The `Car` PROTO inherits from the [AckermannVehicle](ackermannvehicle.md) PROTO
and extends it. It should be used with the [driver](driver-library.md) library
in order to add a model of the engine, transmission, lights, gearbox and brake.
The joint devices are automatically filled in with the appropriate devices depending
on the transmission type set in the parameters.

```
Car {
  #fields specific to Car
  SFString   type                           "traction"
  SFString   engineType                     "combustion"
  SFString   engineSound                    "sounds/engine.wav"
  SFFloat    engineSoundRpmReference        1000
  SFFloat    brakeCoefficient               500
  SFFloat    time0To100                     10
  SFFloat    engineMaxTorque                250
  SFFloat    engineMaxPower                 50000
  SFFloat    engineMinRPM                   1000
  SFFloat    engineMaxRPM                   4500
  SFVec3f    engineFunctionCoefficients     150 0.1 0
  MFFloat    gearRatio                      [-12 10 7 5 2.5 1]
  SFFloat    hybridPowerSplitRatio          0.25
  SFFloat    hybridPowerSplitRPM            3000
}
```

### Car Field Summary

- `type`: Defines the transmission type of the car, supported types are:
`traction` (front wheels), `propulsion` (rear wheels) or `4x4` (both).
- `engineType`: Defines the type of engine, supported types are: `combustion`,
`electric`, `parallel hybrid` and `power-split hybrid` (for a serial hybrid
please use electric instead). See section [Engine
models](driver-library.md#engine-models) for more information.
- `engineSound`: Defines the sound used to simulate the engine sound, if the string is empty the engine sound is not simulated.
- `engineSoundRpmReference`: Defines the reference rotation per minutes of the engine sound. See the [Engine sound](#engine-sound) paragraph for more information about the engine sound simulation.
- `brakeCoefficient`: Defines the maximum `dampingConstant` applied by the brake
on the wheels joint.
- `time0To100`: Defines the time to accelerate from 0 to 100 km/h in seconds, this
value is used to compute the wheels acceleration when controlling the car in
cruising speed thanks to the [driver](driver-library.md)
- `engineMaxTorque`: Defines the maximum torque of the motor in `Nm` used to
compute the electric engine torque.
- `engineMaxPower`: Defines the maximum power of the motor in `W` used to compute
the electric engine torque.
- `engineMinRPM and engineMaxRPM`: Defines the working range of the engine
(`engineMinRPM` not used in case of `electric` `engineType`).
- `engineFunctionCoefficients`: Define the coefficients of the second order
function used to approximate the output torque as a function of the rotational
speed of the motor.
- `gearRatio`: Defines the total (not only the gearbox ratio) ratio between the
rotational speed of the engine and the wheels, the number of elements defines
the number of gears, the first element should be negative and is the reverse
gear.
- `hybridPowerSplitRatio`: Defines the ratio of the output power of the combustion
engine that is used to charge the battery in case of `power-split hybrid`
`engineType`.
- `hybridPowerSplitRPM`: Defines the fixed rotational speed of the combustion
engine in case of `power-split hybrid` `engineType`.

The `extensionSlot` field is filled in by default with the `AutomobileLights`
PROTO.

#### Engine sound

If the `engineSound` field of the `Car` PROTO is not empty, the sound file defined in this field is used to simulate the engine sound. The amplitude and frequency of the sound is modulated in function of the rpm and throttle values:

%figure "Engine sound simulation"
![engine_sound.png](images/engine_sound.png)
%end

### AutomobileLights

The `AutomobileLights` PROTO is used to add all the models of the regular lights
present in a car (based on `LED` nodes). For each light you can specify its
shape and the color emitted when the light is switched on. Of course if you
don't need to have lights you can safely remove the `AutomobileLights` PROTO
from `extensionSlot`.

```
AutomobileLights {
  MFNode    front           [ ]
  MFColor   frontColor      [ 0.8 0.8 0.8 ]
  MFNode    rightIndicator  [ ]
  MFNode    leftIndicator   [ ]
  MFColor   indicatorColor  [ 1 0.7 0.1 ]
  MFNode    antifog         [ ]
  MFColor   antifogColor    [ 0.8 0.8 0.8 ]
  MFNode    braking         [ ]
  MFColor   brakingColor    [ 0.7 0.12 0.12 ]
  MFNode    rear            [ ]
  MFColor   rearColor       [ 0.8 0.8 0.8 ]
  MFNode    backwards       [ ]
  MFColor   backwardsColor  [ 0.7 0.12 0.12 ]
}
```

Here again, you can easily create your own PROTO that inherits from the
[Car](#car) PROTO to define your own custom and complete model of car. Several
PROTO models that inherit from the [Car](#car) PROTO are provided. They
represent different models of car:

- the Sport SVR from Range Rover
- the X5 from BMW
- the Prius from Toyota
- the MKZ from Lincoln
- the C-Zero from Citroen

%figure "Models of cars created using the Car PROTO"

![cars.png](images/cars.png)

%end

An interesting aspect of these PROTO nodes is that the `extensionSlot` is
divided into four `sensorsSlot` in order to provide smart predefined positions
where to put sensors (or actuators if needed), which are in the front, top, rear
and center of the car. The position of the central sensors slot is always at 0 0
0 (which is the center of the rear wheels axis). For the three other sensor
slots, the positions are different for each model (because the size of the cars
differs), see the [following table](#slotpositions) for the exact positions.

%figure "Positions of the sensors slots"

| Model              | Front slot translation | Top slot translation | Rear slot translation |
| ------------------ | ---------------------- | -------------------- | --------------------- |
| BmwX5              | 0.0 0.45 3.850         | 0.0 1.45 1.000       | 0.0 0.3 -1.000        |
| LincolnMKZ         | 0.0 0.142 3.944        | 0.0 1.16 1.110       | 0.0 0.33 -1.06        |
| RangeRoverSportSVR | 0.0 0.5 3.5            | 0.0 1.3 1.4          | 0.0 0.33 -1.06        |
| CitroenCZero       | 0.0 0.05 3.075         | 0.0 1.35 1.075       | 0.0 0.3 -0.425        |
| ToyotaPrius        | 0.0 0.40 3.635         | 0.0 1.30 1.100       | 0.0 0.3 -0.850        |

%end

In order to lighten up some simulations, `Solid` based cars can be used from the [VehicleSimple](#vehicle-simple) PROTO.
