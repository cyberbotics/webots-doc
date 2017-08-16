## Simple Vehicles

### CarSimple

For each model of [Car](#car), a 'simple' PROTO is present too. These simplified
kinematic PROTO models are not based on a `Robot` node but on a `Solid` node, it is
therefore not possible to add sensors or control them. They are made to represent
non-moving parked vehicles or to be moved using a Supervisor because they are much
faster to simulate than the normal PROTO models.

```
 PROTO CarSimple {
   field       SFVec3f    translation             0 0.4 0
   field       SFRotation rotation                0 1 0 0
   field       SFColor    color                   0.0 0.25 0.65
   field       MFColor    recognitionColors       [ 0.0 0.25 0.65, 0.1 0.1 0.1 ]
   field       MFString   plate                   "textures/plate.jpg"
   field       SFString   name                    "vehicle"
   field       SFBool     wheelBoundingObject     FALSE
 }
 ```

#### CarSimple Field Summary

- `recognitionColors`: If not empty, this vehicle may be recognized by any Camera
device with recognition capability (i.e. with a Recognition node).
- `wheelBoundingObject`: Allows to enable the physical geometry of the wheels.

The different CarSimple PROTO represent the different models of [Car](#car):

- the Sport SVR from Range Rover
- the X5 from BMW
- the Prius from Toyota
- the MKZ from Lincoln
- the C-Zero from Citroen

%figure "Models of cars created using the CarSimple PROTO"

![cars.png](images/cars.png)

%end

### MotorcycleSimple

Due to the presence of driver, the MotorcycleSimple PROTO have a slightly different
organisation. The constituing models are not based on the `Solid` node of a `Robot`
as they cannot be controled in the way a [Car](#car) is.

```
PROTO MotocycleSimple {
  field       SFVec3f    translation             0 0.25 0
  field       SFRotation rotation                0 1 0 0
  vrmlField   SFColor    primaryColor            0.43 0.11 0.1
  vrmlField   SFColor    secondaryColor          0.69 0.43 0.43
  field       MFColor    recognitionColors       [ 0.43 0.11 0.1, 0.69 0.43 0.43 ]
  field       SFNode     driver                  ScooterDriver { }
  field       SFString   name                    "vehicle"
  field       SFBool     wheelBoundingObject     FALSE
}
```

#### MotorycleSimple Field Summary

- `secondaryColor`: Defines a secondary color to be chosen alongside the main one.
- `driver`: Defines a `Slot` node for the motorcycle driver.

The MotorycleSimple PROTO represents a scooter:

%figure "Models of MotorcycleSimple currently available"

![motorcycle.png](images/motorcycle.png)

%end
