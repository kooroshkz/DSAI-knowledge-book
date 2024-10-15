Prcoessing either on board or in the cloud
Alexa uses cloud computing(because amazon can use things like Athen aDynamoDb)
It does need robust communication which can not be always does if the robot is mobile(if it doesn’t have access to internet the processing done on the cloud stops)

Ideally base processing like avoiding obstacles must be done on board the robot and the more advanced information can be processed if internet access is provided

<h5><font color=40E0D0>Software Architecture</font></h5>
Interaction with env demand processing sensor info in real time

Modular software 

![[482670DE-43D4-4630-AEDF-373281293D38.jpeg]]
[[Sensors Robot|Sense]] from sensors
Think - processing(ie software)
[[Actuators Robot|Act]] - actuators 


Also called the deliberate approach - however we also require reflex actions
Simple behaviours are programmed into the robot and are with sensor action processing loops

Act first think later

Emergent behaviour for apparent intelligence


Software platforms required - what code can run on what 

### Under Software Arch 
1. Classic Agent Cycle 
<font color=00CED1>Sense</font> -> <font color=00FF7F>Think</font> -> <font color=FF0000>Act</font>
Sensors will provide raw data 

 <font color=00FF7F>Thinking</font>
	-  Perception what raw input from sensors mean
	- Reasoning - what to do 
	- Decision making - based on surrounding and maybe a goal

<font color=FF0000>Actuators</font> are how the robot performs it’s selected decision 
1. Subsumption architecture
2. Layered Arch

Repeated cycles of a classic agent - will determine the way it behaves 
But it can not react quickly 

2. Subsumption architecture 
![[IMG_0694.jpeg]]
<font color=00CED1>Sensors</font> provide the raw data 

There is a type of reactive behaviour - explore world, wander around(use of <font color=00CED1>sensors</font> + <font color=FF0000>act</font>) + avoid objects(there is some <font color=00FF7F>thinking</font>/information processing happening here)

Composite behaviour - The combination of this reactive behaviour can lead to the robot, searching for something + going to something(this is <font color=00FF7F>thinking</font> explicitly)

<font color=FF0000>Actuators</font> - going to a specific destination and wandering around along with avoiding objects all require actuators 

- The architecture is organised + allows for the robot to perform specific tasks through composite behaviour 
- Linked through inhibition and excitation(comparison to reinforcement learning and neural networks, where certain actions are provided a positive value and are then done more)

Behaviour is generated continuously 
Complex behaviours are difficult to organise hierarchically 

3. Layered architecture 
![[IMG_0695.jpeg]]
- Behaviour organised in layers of abstraction 
- Each layer more advanced 
- <font color=00CED1>Sense</font> -> <font color=FFA500>Reactive</font> -> <font color=00FF7F>Exec + Deliberate + Reflect</font> -> <font color=FF0000>Act</font>

Behaviour is continuously coordinated at levels 
Not sure where to put all functions 

#### **Machine Learning**
Requires training Int data consisting of thousands or millions of examples

For classification AI, images are used so the AI can form judgements on whether something is traffic light

Feature extraction - preprocessing and changing representation to be more suitable 

Especially from raw sensor input 

Feature vector - row of numbers ready for processing 

1. Classification AI
Algorithm that decides what class a given data type fits into 

Perform better with more data

Error - overfitting or under fitting 
Either too focused on the training data that it only works for it 

Or too vague that nothing works

2. Deep learning
Relies on AI neural networks with thousands of interconnected nodes to simulate a brain

Forms the feature extraction on it’s own but requires large amounts of data 

HRI has issues with this because we do not have a lot of data for human robot interaction

Also impossible to know what the AI bases it’s judgements on so there’s no way to judge how it will act in the future

> The WAY to think about this is that subsumption architecture is reflexive and even the composite planning of the architecture is still based on the reflexive parts. Where as layered arch does have reflexive aspects, the executive layer is of a higher level and it’s more of a goal oriented arch 
<h5><font color=98FB98>Computer Vision</font></h5>
Interprets a 2D array of numbers - intends to recognise faces, gestures and movements, objects, depth and motion tracking

Can be used to determine if anything is moving in the sensor

So it seems like the robot is aware and able to interact

> There seems to be an obvious disconnect between the actual <font color=FF4500>intelligence</font> of agents we have and what we project them to be. A lot of the “<font color=FF4500>intelligence</font>” is actually <font color=FF4500>projected</font> onto these agents by humans. The rest of AI seems to continue raising this blanket over people’s eyes and encouraging the <font color=FF4500> irrational robophobia</font> that robots(as they are) are capable of wiping us out.

<h5><font color=FF4500>Limits</font></h5>
1. Sensors need an accurate depiction of the world - it can not be used considering the current levels of noise
2. Learning - currently is slow
3. Integration of all the subsections/modular systems require work - especially on complex robots
4. The robot may portray understanding but people like John Searle(Chinese room) argue they have no understanding of semantics

> However if the understanding of semantics is uniform, but our own experiences are individual and influence the semantics because of course they do. Then no human has a uniform understanding of semantics and this argument is flawed.

#### Modern Software
ROS - real robots
SAIBA - virtual agents 

- Layered and modular 
- Uses techniques like
	1. Classic Control 
	2. Machine Learning 
	3. Reasoning AI
	4. High level scripting 