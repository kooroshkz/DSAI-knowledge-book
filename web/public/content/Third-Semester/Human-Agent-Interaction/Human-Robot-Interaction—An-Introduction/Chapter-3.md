### 1. **Core Components of a Robot**:
   - **Hardware**:
     - **Sensors**: Cameras (RGB, Depth), microphones, LiDAR (long-distance measurements), tactile sensors (Touch sensor).
     - **Actuators**(For movement): Motors, pneumatic systems (used in RoboThespian), and speakers.

   **LiDAR**(Light Detection and Ranging): 

   <img src="https://geospatialmedia.s3.amazonaws.com/wp-content/uploads/2019/01/Wired1.jpg" height="200">

### 2. **Types of Robots**:
   - **Humanoid**: Pepper, iCub, Robovie (human-like body and face features).
   - **Androids**: Close human resemblance (Geminoid, Kokoro).
   - **Zoomorphic**: Animal-like robots (Aibo, Paro).
   - **Social drones**: Flying robots that interact with humans.
   - **Projection robots**: Use projections to simulate a face (e.g., Furhat).
   - **Virtual agents**: Not physical robots but AI-powered avatars.

### 4. **Robot Control Systems**:
   - **Sense-Plan-Act Model**: Robots sense their environment, plan their actions, and execute them.
   - **Subsumption Architecture**: Simple behaviors are triggered quickly, used for immediate responses (e.g., emergency stop).
### Middleware

Application software can directly run on the operating system, robotic applications often are run through middleware, consisting of many small pieces of software modules. Middleware is considered a “software glue,” being in the middle of software modules and the operating system.
 Middleware handles differences in hardware, allowing sensors to be used interchangeably by standardizing data formats.

The Robot Operating System (ROS) is a middleware platform, not an operating system. Rather, it is a collection of software modules and tools you can operate Nao and Pepper with.
**Motors**:

1. **DC Servo Motor**: The standard actuator for robots, consisting of a DC motor, microcontroller, and a sensor (potentiometer or encoder) that provides the motor’s position.
  
2. **PWM Control**: Speed is controlled using Pulse-Width Modulation (PWM), where on/off pulses determine motor speed. Feedback control adjusts motor position by comparing actual position with the desired one.

3. **Position and Velocity Control**: In robot arms and heads, the controller performs position control to move the motor to a specific angle. For mobile robots (e.g., wheels), velocity control is used to adjust speed.

4. **Degrees of Freedom (DOF)**: The number of motors depends on the robot’s design and function. For instance, Roomba has 2 DOFs, a humanoid robot's head can have 3 DOFs (pan, tilt, yaw), and robot arms can have up to 7 DOFs for manipulation.

Pointing finger has 4 degrees of freedom (DOFs).

<img src="https://www.researchgate.net/publication/288021741/figure/fig1/AS:669004922376195@1536514611397/Bones-and-joints-of-the-human-hand-DIP-Distal-Interphalangeal-joint-PIP-Proximal.jpg" height="300">

The minimum number of Degrees of Freedom (DOFs) that a robot arm needs to grasp an object from any direction is **6 DOFs**.

- **3 DOFs** for positioning the end effector (the "hand" or "gripper") in 3D space (X, Y, and Z axes).
- **3 DOFs** for orienting the end effector (to change its pitch, yaw, and roll) to grasp the object from any direction.

5. **End Effectors**: Robot arms need grippers or hands to grasp objects. A simple gripper may have 1 DOF, while more complex hands have multiple DOFs for precise movements.
#### Transfer Learning

**Transfer Learning Definition**: Transfer learning, or fine-tuning, solves this by reusing part of an already trained neural network and adding a small labeled dataset to tune specific parts of the network, usually near the output layer.

**Efficiency**: This allows the model to learn new skills or adapt to new tasks with a much smaller dataset compared to training a model from scratch like Language models like BERT and GPT, which are pre-trained on massive amounts of text, can be fine-tuned with much smaller data sets (e.g., less than 100 sentences) for specific tasks like intent recognition.
The technologies typically used as **sensors** on robots are **Camera**, **Microphone**, **LiDAR**and **Ultrasound sonar**.

**Loudspeakers**, **LED lights**, and **Servo motors** are not sensors. Loudspeakers are output devices, LED lights provide illumination, and servo motors are actuators used for movement which is simple motors for cheap robots controlled by the duty cycle of the control signal and continuously changes direction to maintain its set position.
The inertial measurement unit allows Pepper to measure its bodily orientation, which is fundamental for balance and localization.