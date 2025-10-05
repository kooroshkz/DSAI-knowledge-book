### Study Notes: Building Blocks of Socially Interactive Agents

#### **Socially Interactive Agents**
   - **Definition**: Agents (virtual or physical) capable of autonomous communication with humans or other agents, exhibiting social intelligence via multi-modal behaviors.
   - **Types**:
     - **Social Robot**: Physical embodiment (e.g., robots).
     - **Intelligent Virtual Agent**: Virtual embodiment (e.g., virtual characters).

#### **Agent Architectures**
   - **Sense-Think-Act Cycle**: The classical cycle for agents but has limitations in reactivity.
   - **Subsumption Architecture**:
     - Hierarchical task-specific modules for continuous behavior (action-reaction).
     - Difficult to manage complex behaviors.
   - **Layered Architecture**:
     - Behavior organized in layers (Reactive, Executive, Deliberative, Reflective).
     - Challenges include deciding functionality placement.

#### **Modern Agent Architectures**
   - **Characteristics**:
     - Modular, layered systems for abstraction.
     - Machine learning, sensor/actuator abstraction via APIs.
     - Advanced modules (e.g., facial recognition) in the cloud, real-time control on the robot.
   - **Examples**: ROS (Robot Operating System), RIE, Virtual Human Toolkit.

#### **SAIBA and BML**
   - **Problem**: Synchronizing multi-modal behavior generation.
   - **Behavior Markup Language (BML)**: Helps manage and synchronize agent behaviors.