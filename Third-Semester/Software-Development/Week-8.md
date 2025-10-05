## Class Diagram

In a class diagram, modifiers are used to determine the visibility of attributes and operations:

<img src="https://cdn-proxy.slickplan.com/wp-content/uploads/2023/10/9_uml.png" width="650">

- The pointer will stick to source.

- Aggregation `School ◇────── Teacher`: The hollow diamond (`◇`) points to indicating it is the "whole".
- Generalization `Teacher ▷────── MathTeacher`: The hollow triangle (`▷`) points to the "superclass".
- Inheritance `MathTeacher ▷────── MathTeacherAssistant`: The solid triangle (`▷`) points to the "superclass".


![](https://vertabelo.com/blog/uml-notation/uml_relationship.png)


### **1. `0..1` (Zero or One)** 

### **2. `1` (Exactly One)**  

### **3. `1..*` (One or More)**  

### **4. `0..*` or `*` (Zero or More)**  

- **Class A** and **Class B** are related with multiplicities.  
  - `Class A 1 ------ 0..1 Class B`: A single instance of `Class A` can be related to **zero or one** instance of `Class B`.

1. **Class Diagram**:
   - Illustrates the system's structure by showing classes, attributes, operations, and relationships.
   - ![Class Diagram](https://www.researchgate.net/profile/Robert-Milewski/publication/261699916/figure/fig2/AS:651206670180362@1532271177964/Class-diagram-of-student-evaluation-data.png)

2. **Object Diagram**:
   - Depicts object instances and their relationships at a particular moment.
   - ![Object Diagram](../../Files/third-semester/sd/3.png)

3. **Sequence Diagram**:
   - Shows how objects interact in a particular sequence, detailing the order of messages.
   - ![Sequence Diagram](https://miro.medium.com/v2/resize:fit:720/format:webp/1*LkDapTCD6_xxOKCC3kTzcw.jpeg)

4. **Activity Diagram**:
   - Represents workflows of stepwise activities and actions, including conditions.
   - ![Activity Diagram](https://cdn-images.visual-paradigm.com/guide/uml/what-is-activity-diagram/04-activity-diagram-example-process-order.png)
   - Shapes:
      - **Oval (Ellipse):** Represents the **start** or **end** of a process.  
      - **Rectangle:** Represents an **activity** (a specific task or action).
      - **Diamond:** Represents a **decision node**, where the flow splits into multiple paths based on conditions.
      - **Arrow:** Represents the **flow of control** or transition from one activity to another.
      - **Circle:** Represents a **connector** or a merging point where multiple paths converge without any condition.

5. **Gantt Chart**:
   - Visualizes project schedules, showing tasks, durations, and dependencies.
   - ![Gantt Chart](https://leansixsigmagroep.nl/wp-content/uploads/2023/11/gantt-chart-768x512-1.webp)