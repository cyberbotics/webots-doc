## Lidar sensors

A wide range of lidar sensors have been modelled.

### Ibeo lux

The `IbeoLux` is a 4 layers lidar with a range of up to 200 meters and a field
of view of up to 110 degrees, it returns 680 points per layer per scan.

The model of the `IbeoLux` contains a spherical projection, a fixed resolution
of 0.04 meter and a gaussian noise with a standard deviation of 0.1 meter.

%figure "Ibeo Lux lidar"

![ibeo.png](images/ibeo.png)

%end

```
IbeoLux {
    SFVec3f    translation             0 0 0
    SFRotation rotation                0 1 0 0
    SFString   name                    "ibeo"
    SFBool     useExtendedFieldOfView  FALSE
    SFBool     fastModel               FALSE
  }
```

The `IbeoLux` PROTO can either be used in normal field of view mode (80 degrees
field of view) or in extended field of view mode (110 degrees field of view)
depending on the value of the `useExtendedFieldOfView` field.

The `fastModel` field can be used to simplify the model of the sensor by
removing the spherical projection, the noise and the limited resolution in order
to speed up the simulation.

### Sick Lms 291

The `Sick Lms 291` is a 1 layer lidar with a range of up to 80 meters and a
field of view of up to 180 degrees.

The model of the `IbeoLux` contains a spherical projection, a configurable fixed
resolution and a configurable gaussian noise.

%figure "Sick Lms 291 lidar"

![sick.png](images/sick.png)

%end

```
SickLms291 {
    SFVec3f translation 0 0 0
    SFRotation rotation  0 1 0 0
    SFString name "lms291"
    SFFloat noise 0.0
    SFInt32 resolution 180
  }
```

The `noise` field specifies the standard deviation of the gaussian noise in
meters.

The `resolution` field specifies the number of points returned per layer per
scan.

### Velodyne

All the models of velodyne sensors are available.

#### Velodyne VLP 16

The `Velodyne VLP 16` is a 16 layers lidar with a range of up to 100 meters and
a field of view of 360 degrees, it returns 3600 points per layer per scan.

The model of the `Velodyne VLP 16` contains a spherical projection and a
gaussian noise with a standard deviation of 0.03 meter.

%figure "Velodyne VLP 16 model"

![velodyne_vpl_16.png](images/velodyne_vpl_16.png)

%end

```
VelodyneVLP-16 {
    SFVec3f    translation    0 0 0
    SFRotation rotation       0 1 0 0
    SFString   name           "velodyne"
    SFBool     fastModel      FALSE
    }
```

The `fastModel` field can be used to simplify the model of the sensor by
removing the noise in order to speed up the simulation.

#### Velodyne HDL 32E

The `Velodyne HDL 32E` is a 32 layers lidar with a range of up to 70 meters and
a field of view of 360 degrees, it returns 4500 points per layer per scan.

The model of the `Velodyne HDL 32` contains a gaussian noise with a standard
deviation of 0.02 meter and a rotating head.

%figure "Velodyne HDL 32E lidar"

![velodyne_hdl_32e.png](images/velodyne_hdl_32e.png)

%end

```
VelodyneHDL-32E {
    SFVec3f    translation    0 0 0
    SFRotation rotation       0 1 0 0
    SFString   name           "velodyne"
    SFBool     fastModel      FALSE
    }
```

The `fastModel` field can be used to simplify the model of the sensor by
removing the noise in order to speed up the simulation.

#### Velodyne HDL 64E

The `Velodyne HDL 64E` is a 64 layers lidar with a range of up to 120 meters and
a field of view of 360 degrees, it returns 4500 points per layer per scan.

The model of the `Velodyne HDL 64` contains a gaussian noise with a standard
deviation of 0.02 meter and a rotating head.

%figure "Velodyne HDL 64E lidar"

![velodyne_hdl_64e.png](images/velodyne_hdl_64e.png)

%end

```
VelodyneHDL-32E {
    SFVec3f    translation    0 0 0
    SFRotation rotation       0 1 0 0
    SFString   name           "velodyne"
    SFBool     fastModel      FALSE
    }
```

The `fastModel` field can be used to simplify the model of the sensor by
removing the noise in order to speed up the simulation.

