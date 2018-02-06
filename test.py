txt = """
# testA

- Abc
- DEF
- ghi
klm
nm

testB test
test

- *version* corresponds to the real Nao version. The supported versions are "3.3",
"4.0" and "5.0".

## test C

- Hello world.
- test!

testD...

- **Simulation**: You will be able to test your controller in simulation, without
any risk of damaging the robot. You will also be able to run automatically a lot
of different simulations in a very small amount of time (to tune up parameters
for example), which would be impossible to do with the real robot.
- **Remote compilation**: When your controller is doing fine in simulation, you will
be able to send, compile and run it on the real robot, without changing anything to your
code, just by pressing a button in the robot window.
- **Remote control**: To debug or understand your controller's behavior, you will be
able to see in real time all sensor and actuator states on your
computer screen. This is available both in simulation and on the real robot.
Here again, this is done in just one click. You will also be able to run your
controller on the computer, but instead of sending commands to and reading
sensor data from the simulated robot, it sends commands to and reads sensor data
from the real robot.

testE...

- test
- test
"""

import re
r = re.sub(r'\n\s*-.+?(?=\n\n)', '', txt, flags=re.S)
r = re.sub(r'\n\s*-.+?(?=\n)', '', r, flags=re.S)
print r
