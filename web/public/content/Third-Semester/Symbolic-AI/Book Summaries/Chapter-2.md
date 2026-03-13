### **Intelligent Agents**

#### **Agents and Environments**
- **Agent:** Perceives environment with sensors and acts via actuators.  
  - Example: Humans (sensors: eyes, actuators: hands), robots, software systems.

#### **Rationality and Performance**
- **Rational Agent:** Selects actions that maximize the performance measure based on:
  - Percept sequence.
  - Prior knowledge.
  - Available actions.

#### **Types of Agents**
1. **Simple Reflex Agents:**
   - Act on current percepts using predefined condition–action rules.
   - Limitations: Fail in partially observable environments.

2. **Model-Based Reflex Agents:**
   - Handle **partially observable environments** by maintaining an internal state.
   - The **internal state** is a representation of the environment twhich can infer based on its history of percepts and actions stored in memory.


3. **Goal-Based Agents**

4. **Utility-Based Agents:**
   - Evaluate the desirability of states using a utility function and choose actions to maximize expected utility.
   - Maximize expected utility under uncertainty.

5. **Learning Agents**

#### **Task Environments (PEAS Framework)**
- **PEAS:** Performance measure, Environment, Actuators, Sensors.
- Example: Automated taxi:
  - **Performance Measure:** Safety, speed, passenger comfort, profit.
  - **Environment:** Roads, traffic, pedestrians.
  - **Actuators:** Steering, brakes, signals.
  - **Sensors:** Cameras, GPS, speedometer.


#### **Environment Types**
- **Fully Observable vs. Partially Observable**
- **Single Agent vs. Multiagent**
- **Deterministic vs. Stochastic:** Predictable outcomes or random elements.
- **Episodic vs. Sequential:** Independent tasks or dependent on prior actions.
- **Static vs. Dynamic:** Changes over time or remains constant.
- **Discrete vs. Continuous:** Distinct states vs. gradual changes.