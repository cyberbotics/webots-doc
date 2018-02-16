## Using the Aibo ERS7 robot

%figure "Aibo ERS7"

![aibo_ers7.png](images/aibo_ers7.png)

%end

Aibo ERS7 is a four-legged dog-like robot designed by Sony Corp.
The model includes 26 LEDs, 3 infra-red distance sensors and a total of 20 motors controlling different parts of the robot such as the neck, the tail of the head tilt.

More information on the Aibo robots can be found [here](https://en.wikipedia.org/wiki/AIBO).

### Aibo ERS7 model

The following [table](#aibo-ers7-motor-names) shows the different names of the motors and position sensors supported on the Aibo ERS7.

%figure "Aibo ERS7 motor and position sensor names"

| Joints           | Motor names                     | Position sensor names              |
| ---------------- | ------------------------------- | ---------------------------------- |
| Neck tilt        | 'PRM:/r1/c1-Joint2:11'          | N/A                                |
| Head pan         | 'PRM:/r1/c1/c2-Joint2:12'       | N/A                                |
| Head tilt        | 'PRM:/r1/c1/c2/c3-Joint2:13'    | N/A                                |
| Left ear         | 'PRM:/r1/c1/c2/c3/e5-Joint4:15' | N/A                                |
| Right ear        | 'PRM:/r1/c1/c2/c3/e6-Joint4:16' | N/A                                |
| Jaw              | 'PRM:/r1/c1/c2/c3/c4-Joint2:14' | N/A                                |
| Tail tilt        | 'PRM:/r6/c1-Joint2:61'          | N/A                                |
| Tail pan         | 'PRM:/r6/c2-Joint2:62'          | N/A                                |
| Right foreleg J1 | 'PRM:/r4/c1-Joint2:41'          | 'PRM:/r4/c1-JointSensor2:41'       |
| Right foreleg J2 | 'PRM:/r4/c1/c2-Joint2:42'       | 'PRM:/r4/c1/c2-JointSensor2:42'    |
| Right foreleg J3 | 'PRM:/r4/c1/c2/c3-Joint2:43'    | 'PRM:/r4/c1/c2/c3-JointSensor2:43' |
| Right hindleg J1 | 'PRM:/r5/c1-Joint2:51'          | 'PRM:/r5/c1-JointSensor2:51'       |
| Right hindleg J2 | 'PRM:/r5/c1/c2-Joint2:52'       | 'PRM:/r5/c1/c2-JointSensor2:52'    |
| Right hindleg J3 | 'PRM:/r5/c1/c2/c3-Joint2:53'    | 'PRM:/r5/c1/c2/c3-JointSensor2:53' |
| Left foreleg J2  | 'PRM:/r2/c1/c2-Joint2:22'       | 'PRM:/r2/c1/c2-JointSensor2:22'    |
| Left foreleg J1  | 'PRM:/r2/c1-Joint2:21'          | 'PRM:/r2/c1-JointSensor2:21'       |
| Left foreleg J3  | 'PRM:/r2/c1/c2/c3-Joint2:23'    | 'PRM:/r2/c1/c2/c3-JointSensor2:23' |
| Left hindleg J1  | 'PRM:/r3/c1-Joint2:31'          | 'PRM:/r3/c1-JointSensor2:31'       |
| Left hindleg J2  | 'PRM:/r3/c1/c2-Joint2:32'       | 'PRM:/r3/c1/c2-JointSensor2:32'    |
| Left hindleg J3  | 'PRM:/r3/c1/c2/c3-Joint2:33'    | 'PRM:/r3/c1/c2/c3-JointSensor2:33' |

%end

The following [figure](#motor-positions) shows the position of the joints previously mentioned.

%end

%figure "Motor positions"

![aibo_ers7_motors.png](images/aibo_ers7_motors.png)

%end

The following [table](#aibo-ers7-motor-names) shows the different names of the LEDs present on the Aibo ERS7.

%figure "Aibo ERS7 LED names"

| LED                     | Name                          |
| ----------------------- | ----------------------------- |
| Back Front Light Color  | 'PRM:/lu-LED3:lu'             |
| Back Front Light White  | 'PRM:/lv-LED3:lv'             |
| Back Middle Light Color | 'PRM:/lw-LED3:lw'             |
| Back Middle Light White | 'PRM:/lx-LED3:lx'             |
| Back Rear Light Color   | 'PRM:/ly-LED3:ly'             |
| Back Rear Light White   | 'PRM:/lz-LED3:lz'             |
| Head Light Color        | 'PRM:/r1/c1/c2/c3/l1-LED2:l1' |
| Head Light White        | 'PRM:/r1/c1/c2/c3/l2-LED2:l2' |
| Mode Indicator Red      | 'PRM:/r1/c1/c2/c3/l3-LED2:l3' |
| Mode Indicator Green    | 'PRM:/r1/c1/c2/c3/l4-LED2:l4' |
| Mode Indicator Blue     | 'PRM:/r1/c1/c2/c3/l5-LED2:l5' |
| Wireless Light          | 'PRM:/r1/c1/c2/c3/l6-LED2:l6' |
| FaceLight 1             | 'PRM:/r1/c1/c2/c3/la-LED3:la' |
| FaceLight 2             | 'PRM:/r1/c1/c2/c3/lb-LED3:lb' |
| FaceLight 3             | 'PRM:/r1/c1/c2/c3/lc-LED3:lc' |
| FaceLight 4             | 'PRM:/r1/c1/c2/c3/ld-LED3:ld' |
| FaceLight 5             | 'PRM:/r1/c1/c2/c3/le-LED3:le' |
| FaceLight 6             | 'PRM:/r1/c1/c2/c3/lf-LED3:lf' |
| FaceLight 7             | 'PRM:/r1/c1/c2/c3/lg-LED3:lg' |
| FaceLight 8             | 'PRM:/r1/c1/c2/c3/lh-LED3:lh' |
| FaceLight 9             | 'PRM:/r1/c1/c2/c3/li-LED3:li' |
| FaceLight 10            | 'PRM:/r1/c1/c2/c3/lj-LED3:lj' |
| FaceLight 11            | 'PRM:/r1/c1/c2/c3/lk-LED3:lk' |
| FaceLight 12            | 'PRM:/r1/c1/c2/c3/ll-LED3:ll' |
| FaceLight 13            | 'PRM:/r1/c1/c2/c3/lm-LED3:lm' |
| FaceLight 14            | 'PRM:/r1/c1/c2/c3/ln-LED3:ln' |

%end

The following [table](#aibo-ers7-motor-names) shows the different names of the distance sensors present on the Aibo ERS7.

%figure "Aibo ERS7 distance sensor names"

| Distance Sensor  | Name                             |
| --------------- | -------------------------------- |
| Head Near       | 'PRM:/r1/c1/c2/c3/p1-Sensor:p1'  |
| Head Far        | 'PRM:/r1/c1/c2/c3/p2-Sensor:p2'  |
| Chest           | 'PRM:/p1-Sensor:p1'              |

%end

The following [figure](#distance-sensor-positions) shows the position and direction of the distance sensors previously mentioned.

%figure "Distance sensor positions"

![aibo_ers7_distance_sensors.png](images/aibo_ers7_distance_sensors.png)

%end

### Samples

#### aibo\_ers7.wbt

![aibo_ers7_example.png](images/aibo_ers7_example.png) In this example, you can see a silver Aibo ERS-7 robot walking on a textured soccer field.
On this field you can also see its toys : a ball, a charger and a bone.
