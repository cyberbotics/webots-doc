## C++, Java and Python wrappers of the automobile libraries

The [driver](driver-library.md) and [car](car-library.md) libraries are also
available as oriented-object wrappers for the C++, the Java and the Python languages.

The [Driver](cpp-libraries.md#cppdriver) and [Car](cpp-libraries.md#cppcar)
classes are containing all the methods described in the C API. Camel case is
used to define the method names. The `init` and `cleanup` functions are called
automatically from the constructor/destructor of the
[Driver](cpp-libraries.md#cppdriver) and [Car](cpp-libraries.md#cppcar) classes.

> **Note** [Java]:
The following program shows how to set the cruising speed and the steering angle
in Java:

> ```java
> import com.cyberbotics.webots.controller.Robot;
> import com.cyberbotics.webots.automobile.Driver;
>
> public class VehicleDriver {
>   public static void main(String[] args) {
>     Driver driver = new Driver();
>     driver.setCruisingSpeed(20.0);
>
>     while (driver.step() != -1) {
>       double angle = 0.3 * Math.cos(driver.getTime());
>       driver.setSteeringAngle(angle);
>     };
>   }
> }
> ```

> **Note** [Python]:
The following program shows how to set the cruising speed and the steering angle
in Python:

> ```python
> import math
> import os
> import sys
>
> try:
>   libraryPath = os.environ.get("WEBOTS_HOME") + "/projects/automobile/libraries/python"
>   libraryPath.replace('/', os.sep)
>   sys.path.append(libraryPath)
>   from automobile import Driver
> except ImportError:
>   sys.stderr.write("Warning: 'automobile' module not found.\n")
>   sys.exit(0)
>
> driver = Driver()
> driver.setSteeringAngle(0.2)
> driver.setCruisingSpeed(20)
>
> while driver.step() != -1:
>   angle = 0.3 * math.cos(driver.getTime())
>   driver.setSteeringAngle(angle)
> ```
