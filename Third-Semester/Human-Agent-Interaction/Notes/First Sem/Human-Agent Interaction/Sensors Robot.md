**Vision**
1. Camera - light sensor that converts light to energy 
Images are stored using RGB at least for colour 
Camera’s do not exactly see light but they can determine intensity 
RGB makes use of filters to only allow certain colours 

Cameras can facilitate accurate vision however ethical issues!

Image needs to be processed before it can be acted upon 

2. <font color=1E90FF>Depth</font> - measure distance(we take the camera image and make it 3D)
RGBD - image is created 

<font color=9932CC>Infrared tech</font> is used(discredits ability to work outdoors) - emits infrared light and then calculates distance based on reflection

| <font color=228B22>Advantages</font> | <font color=DC143C>Disadvantages</font> |
| ------------------------------------ | --------------------------------------- |
| Small form factor                    | Limited distance and or resolution      |
| Low power consumption                | Affected by env conditions              |
| Continuous measurement               |                                         |
| Object can have complex geometry     |                                         |

<font color=FF1493>Ultrasonic Distance Sensors - TOF</font> - transmits pulses of ultrasound and then measures the time between the transmission and when it is reflected back

| <font color=228B22>Advantages</font>               | <font color=DC143C>Disadvantages</font>        |
| -------------------------------------------------- | ---------------------------------------------- |
| Unaffected by colour                               | Limited distance                               |
| Useable in any light conditions                    | Objects can not be small                       |
| Low- power consumption to use this type of sensors | Can not be fast(otherwise won’t be registered) |
|                                                    | Objects can not have complex textures          |

Xbox Kinect - skeleton tracking for just dance

3. Laser range finders
 <font color=FF7F50>Li-DAR tech - Uses TOF</font> - emits a pulse of laser light which is reflected off an object, time taken till its reflected back

| <font color=228B22>Advantages</font> | <font color=DC143C>Disadvantages</font>  |
| ------------------------------------ | ---------------------------------------- |
| High accuracy                        | Higher costs                             |
| Suitable for fast-moving objects     | Eyes may need protection                 |
| Can detect small objects             | Need to rotate housing([[Robot Design]]) |
|                                      |                                          |

Measures distances up to 30m away and takes a reading 50 times per second
On a rotating platform to give robot a sense of all of it’s surroundings 

#### Depth calculation 
<font color=6495ED>Stereo Triangulation </font>
Depth is calculated from corresponding points in two images of a scene taken at the same time from different positions 

<font color=ADFF2F>Structured Light </font>
Depth data is cascade from deformation of a known patter of light projected on to a scene. 

![[IMG_0696.jpeg]]

<font color=48D1CC>Time-of-flight(TOF)</font>
Depth date is calculated from the time taken for a pulse of laser light to return to the camera sensor 


**Audio**
<font color=F4A460>Microphone</font>
Convert sound into electric signals because WHY NOT

Mic arrays are used for sound source localization - what is the angle of a sound considering it’s position from the mic array

<font color=ADFF2F>Beamforming</font>
Technique for determing the position of a sound source 

**Tactile**
Good when robot is physically guided by the user
This tests for human robot interaction
AKA how can robot respond to the human’s actions

Mechanical push switch + bumper -> sense collision with env

Pressure sensors(or capacity) -> can also regulate the force a robot is using on a person or fragile equipment 

**Misc**
- LED + infrared -> sense when people are coming

The Wilde hunt approaches

- IMU - accelerometer, gyroscope and magnetometer -> allow the robot to sense if it falls or it has moved over time
- FIR - detect people + temperature sensor 


<font color=FF8C00>NOTE</font>
Sensors can be in room and not on the robot itself

This means that if the robot is using the camera in the room then it’s a part of the robot 

Chinese gym argument - although the the individual translator may not understand Chinese. The entire room does

Consider argument about testing in an experimental setting - this HRI approach would only work in a closed setting 

