## Evolution of software design techniques
- **Exploratory Style**: Gives complete freedom to the programmer to choose the activities to develop a software system.
- **Structured Style**: It is based on the concept of divide and conquer. It divides the problem into smaller subproblems and solves them.
    - Customrt $\rightarrow$ Initial-Code $\rightarrow$ Test(Bug/Debug) $\rightarrow$ Deliver
- **Control Flow Oriented Style**: It is based on if-then-else and do-while constructs.
    - Problem: Size and complexity of programs kept on increasing.
- **Data Structure Oriented Style**: Design program’s data structures, and then develop the code structure based on the data structure.
- **Data Flow Oriented Style**: It is based on the concept of data flow diagrams (DFDs).
- **Object Oriented Style**: It is based on the concept of objects. An object is a real-world entity that has a state and behavior.
### **Collect Requirements**
- **Studying existing documentation**
- **Interviewing**
- **Task Analysis**
- **Scenario analysis**
- **Form analysis**


### Four Fundamental Activities to Design Software:

1. **Requirement Analysis**
- Requirement Engineering $\rightarrow$ Software Requirements Specification (SRS)
    - Functional (Requirements) = What the system does (features) $\rightarrow$ Defined by the customer
    - Non-functional (Requirements) = How it performs (quality) $\rightarrow$ Defined by the developer
2. **Design & Implementation**
- **System Architecture Design:** Defines the high-level structure, identifying components, modules, and interactions to create a system blueprint.
- **( Detailed & UI & DB & Algorithm & Code Architecture )** Design
3. **Software Validation**
4. **Software Evolution**

---
**Revision Control System (RCS)**: Keep files patch ($\delta$) $!=$ **Version Control System (VCS)**: Keep snapshots

- **git checkout**
   - <branch-name>: Switch
   - -b <branch-name>: Create and switch
   - <commit-hash>: Revert
   - <commit-hash> <file-name>: Restore
- **git remote**
   - -v: List
   - add <remote-name> <url>: Add
   - remove <remote-name>: Remove
- **Merge vs Rebase**
   - Merge: Merge the changes from one branch to another branch
   - Rebase: Reapply the changes from one branch to another branch

---
#### **4 Pillars of OOP**
1. **Abstraction**
2. **Encapsulation**
3. **Inheritance**
4. **Polymorphism**

1. **@classmethod**:
   - Operates on the **class itself**, not instances.
   - Requires the `cls` parameter to refer to the class.
   - Use it when you want to access or modify class-level data (e.g., shared attributes).

   ```python
   class Example:
       shared_data = 0

       @classmethod
       def modify_shared_data(cls, value):
           cls.shared_data += value

   Example.modify_shared_data(5)
   print(Example.shared_data)  # Output: 5
   ```

2. **@staticmethod**:
   - Independent of the class or instance.
   - Does **not require `self` or `cls`**.
   - Use it when you need a utility function that logically belongs to the class but doesn’t touch class/instance data.

   ```python
   class Example:
       @staticmethod
       def utility(a, b):
           return a + b

   print(Example.utility(3, 4))  # Output: 7
   ```
---

**Process Model frameworks Activities**:
   - Communication
   - Planning
   - Modeling
   - Construction
   - Deployment

**Umbrella Activities** (applied throughout the process):
   - Project tracking and control
   - Risk management
   - Quality assurance
   - Configuration management
   - Technical reviews

#### **Process Models**

- **1. Waterfall Model**
  - For Adaptations and Suitable for projects with clear and fixed requirements but with late discovery of errors can create big issues. Inappropriate for fast-paced, dynamic projects.

- **2. V-Model**
  - A variation of the Waterfall model, emphasizing quality assurance and validation.

- **3. Incremental Process Model**
  - For projects needing quick delivery of a usable product with technical uncertainties or lengthy schedules.
 - **4. Evolutionary Process Models**: Iterative and adaptable to changing requirements. Includes:
   - **Prototyping**: For unclear requirements; early customer feedback aids refinement.
   - **Spiral**: Risk-driven, combining iterative development with controlled documentation.
 - **6. Unified Process (UP)**: Iterative and incremental
    - **Phases**:
      - Inception: Establishes the project’s scope, feasibility, and risks.
      - Elaboration: Refines the project’s vision, scope, and architecture.
      - Construction: Develops the software system.
      - Transition: Moves the software from development to production.
      - Production: Maintains and supports the software.
  - **7. Agile Process Models**: Iterative and incremental, emphasizing flexibility and customer collaboration.
    - **Agile Process Models:**
      - Extreme Programming (XP): 
        - Planning
        - Designing
        - Coding
        - Testing
      - Scrum:
        - Requirements
        - Analysis
        - Design
        - Evolution
        - Delivery

### Pros and Cons of Software Development Process Models

| **Process Model**                  | **Pros**                                                                                       | **Cons**                                                                                              |
|------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Waterfall Model**                | - Simple and easy to understand.<br>- Structured and systematic approach.<br>- Clear milestones. | - Difficult to accommodate changes.<br>- Sequential flow is unrealistic for real projects.<br>- High risk and inflexible. |
| **V-Model**                        | - Emphasizes quality assurance.<br>- Clear relationship between testing and development phases. | - Expensive and inflexible.<br>- Unsuitable for complex or fast-paced projects.                     |
| **Incremental Model**              | - Delivers functional software early.<br>- Easier to manage risk and changes.<br>- Cost-effective for lengthy projects. | - Requires clear requirements.<br>- Increased complexity and higher costs.<br>- Tracking progress is challenging. |
| **Evolutionary Model**             | - Accommodates uncertainty.<br>- Develops increasingly complete versions.<br>- Continuous customer involvement. | - Uncertain development cycles.<br>- May lead to chaos with fast-paced evolutions.<br>- Late delivery risks. |
| **Prototyping**                    | - Helps clarify unclear requirements.<br>- Allows iterative feedback.<br>- Early validation of concepts. | - Inefficient algorithms or designs.<br>- Expensive for iterative cycles.<br>- Not suitable for large-scale systems. |
| **Spiral Model**                   | - Best for high-risk projects.<br>- Strong focus on risk management.<br>- Flexible and iterative. | - High cost and complexity.<br>- Time estimation challenges.<br>- Requires risk assessment expertise. |
| **Concurrent Model**               | - Allows overlapping tasks.<br>- Flexible and adaptable to changes.<br>- Supports iterative refinement. | - Complexity in managing concurrent states.<br>- May require high coordination efforts.             |
| **Agile Models**                   | - Responds well to changes.<br>- Delivers working software quickly.<br>- Strong team collaboration.<br>- Customer-centric. | - Less emphasis on documentation.<br>- Requires experienced teams.<br>- Difficult in large-scale projects. |
| **Extreme Programming (XP)**       | - Continuous feedback and testing.<br>- High adaptability.<br>- Team cohesion.<br>- Emphasizes customer satisfaction. | - Informal requirement handling.<br>- Lack of formal design.<br>- Not suitable for large or complex projects. |
| **Scrum**                          | - Highly adaptive.<br>- Focuses on customer satisfaction.<br>- Enhances team collaboration.<br>- Efficient for tight timelines. | - Needs additional practices like XP.<br>- Not suitable for unclear projects.<br>- High resource demands. |
| **Component-Based Development**    | - Reusable components.<br>- Faster development.<br>- Easier integration with existing systems. | - Integration challenges.<br>- Heavy reliance on existing components.<br>- High testing overhead.  |
| **Formal Methods**                 | - Produces defect-free software.<br>- Mathematically rigorous.                              | - Expensive and time-consuming.<br>- Requires expertise.<br>- Poor communication with non-technical clients. |
| **Aspect-Oriented Software Development (AOSD)** | - Addresses cross-cutting concerns.<br>- Enhances modularity.<br>- Complements existing paradigms. | - Complexity in implementation.<br>- Limited applicability in some domains.                        |
**Specialized Models**
   - **Component-Based Development**: Builds reusable integrated software components.
   - **Formal Methods Model**: Uses mathematical specifications for high reliability but is costly, time consuming and complex.
   - **Aspect-Oriented Development**: Focuses on cross-cutting concerns like security or performance.

**Agile Development**
   - **Agility Principles**:
     - Customer satisfaction through frequent delivery.
     - Welcome changing requirements.
     - Continuous collaboration and sustainable development.
---
### **File Operations**
  - `'x'`: Exclusive Creation (throws an error if the file already exists, creates a new file for writing only).

### **Regular Expressions**
- `.`: Any
- `^`: Start
- `$`: End
- `*`: Zero or more
- `+`: One or more
- `?`: Zero or one
- `.*`: Greedy
- `.*?`: Non-greedy
- `[abc] != `[^abc]`: Not a, b, or c


|**Character Classes**|**Negated Character Classes**|
|---|---|
|`\b`: Word boundary|`\B`: Not a word boundary|
|`\d`: Digit|`\D`: Not a digit|
|`\s`: Whitespace|`\S`: Not a whitespace|
|`\w`: Word|`\W`: Not a word|
---
## Class Diagram

- **Public (+)**: Accessible from anywhere.
- **Private (-)**: Accessible only from within the class.
- **Protected (#)**: Accessible only from within the class and its subclasses.
- **Package (~)**: Accessible only from within the package.

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

- Shapes:
      - **Circle:** Represents a **connector** or a merging point where multiple paths converge without any condition.
---
- **Test Case**: Input, state, and expected result ([I, S, R]).


- **Static Analysis (Verification)**: Code inspection for errors.
    - Review: Manual code inspection.
    - Walkthrough: Detailed code review.
    - Inspection: Checklist-based review.
         

- Dynamic testing: Executing code to find errors. (Validation)
    - Black box: Input/output validation.
    - White box: Code coverage and logic testing.
    - **Coverage-based testing**:
        - **Statement Coverage**: Each statement executed
        - **Path Coverage**: Each path executed
    - Fault-based testing:
        - **Mutation Testing**: Introduce faults to test cases.
    - Gray box: Context-specific testing(White + Black).
   - ![Verification vs. Validation](../../Files/third-semester/sd/4.png)

**Debugging Approaches**:
- **Brute Force**: Insert print statements.
- **Backtracking**: Trace backwards from an error point.
- **Cause Elimination**: Test hypotheses for error causes.
- **Program Slicing**: Analyze variable dependencies.


#### **Unit Testing**
- Tests smallest units (functions, classes).
- Automated for consistency and coverage measurement.
- Code Coverage Metrics:
  - **Statement**
  - **Branch/Path**
  - **Condition**

![Unit Testing](../../Files/third-semester/sd/5.png)
---
1. **Mutation Testing**
   - A white-box testing technique.
   - Arbitrary changes (mutations) are made to the program.
   - Changes produce a **mutant** program.
     - If the test suite detects the mutation, the mutant is considered **dead**.
     - If undetected, the test suite needs improvement.
   - **Types**:
     1. **Value Mutations**: Change numerical values.
     2. **Decision Mutations**: Change logical or arithmetic operators.
     3. **Statement Mutations**: Modify or delete statements.

2. **Integration Testing**
   - Ensures modules interact correctly by testing their interfaces.
   - **Approaches**:
     - **Big-bang**: All modules integrated at once (useful for small systems).
     - **Incremental**: Modules are integrated incrementally.
       - **Top-down**: Higher-level modules are integrated first.
       - **Bottom-up**: Lower-level modules are integrated first.
       - **Mixed (Sandwich)**: Combines top-down and bottom-up approaches.
#### **System Testing**
- Validates the entire system against the **SRS (Software Requirement Specification)**.
- Conducted after integration and before acceptance testing.
- **Types**:
  1. **Performance Testing**: Evaluates speed, stability, and reliability.
  2. **Load Testing**: Tests system behavior under expected loads.
  3. **Stress Testing**: Assesses robustness under extreme loads.
  4. **Scalability Testing**: Measures the ability to handle scaling user loads.

### **The 5 Cs of Data Ethics**
These principles guide ethical practices in data science:

1. **Consent**:
   - Users should know and agree to how their data is used.
   - Clarity is essential to ensure informed decisions.

2. **Clarity**:
   - Explain terms and conditions in simple, understandable language.
   - Avoid lengthy, complex legal jargon.

3. **Consistency**:
   - Maintain ethical and fair practices consistently.
   - Build user trust by adhering to policies.

4. **Control**:
   - Users should have control over their data, including options to delete it.

5. **Consequences**:
   - Consider potential consequences, including unintended or harmful outcomes.

#### **Key Principles of Data Science**:
1. **Observe Regulations**:
   - Understand and comply with relevant data protection laws.
   - Know why regulations exist and what they protect.

2. **Respect Privacy**:
   - Ensure personal identifiers (e.g., emails, IDs) remain private and anonymized.

3. **Eliminate Bias**:
   - Use diverse and representative data.
   - Test for bias and error rates among different groups.

4. **Avoid Fabrication or Falsification**:
   - Report only genuine results without manipulating data.

5. **Show Transparency**:
   - Be open about data collection and analysis methods.
   - Obtain informed consent from participants.

6. **Secure Data Collection**:
   - Use secure methods for storing and analyzing data.

7. **Use Algorithms Responsibly**:
   - Test algorithms for fairness and bias.
   - Ensure they are explainable and ethical in use.

8. **Consider Long-Term Impacts**:
   - Evaluate societal implications of algorithms and data use.
   - Avoid perpetuating inequality or privacy risks.



### **Algorithmic Fairness**

#### **Types of Harm**:
1. **Allocation Harm**: Unequal resource distribution (e.g., jobs or loans).
2. **Quality-of-Service Harm**: Models work better for some groups than others (e.g., face detection algorithms).
3. **Stereotyping**: Reinforces harmful or inaccurate stereotypes (e.g., biased search results).

#### **Principles**:
- **Individual Fairness**: Treat similar individuals similarly.
- **Group Fairness**: Ensure equal treatment for different groups.



### **Six Ethical Issues (CNIL Framework)**:
1. **Autonomous Machines**:
   - Delegation of critical decisions to machines raises accountability concerns.
   - Example: Responsibility for accidents by autonomous vehicles.

2. **Bias, Discrimination, and Exclusion**:
   - Algorithms can amplify systemic biases.
   - **Solutions**:
     - Use explainable and transparent algorithms.

3. **Algorithmic Profiling**:
   - Profiling can lead to misuse (e.g., Cambridge Analytica scandal in 2016 elections).

4. **Massive Data Collection**:
   - AI requires large datasets, but this must balance privacy concerns.
   - Example: Non-identifiable datasets in health studies.

5. **Data Quality and Bias**:
   - Poor-quality training data can lead to harmful results.
   - Example: Microsoft's Twitter bot (Tay) was manipulated into producing offensive content.

6. **Human Identity and AI**:
   - Human-machine hybridization raises ethical questions about emotional attachment to robots.
---

### **Risks and Challenges in Cloud Computing**
1. **Vendor Lock-In**:
   - Limited ability to switch providers due to proprietary technologies.
2. **Data Security and Privacy**:
   - Sensitive data may be exposed to unauthorized access.
   - Jurisdictional issues when data is stored in foreign countries.
3. **Complex Migration**:
   - Legacy applications may require significant changes to run on the cloud.
4. **Skill Requirements**:
   - IT teams must adapt to cloud technologies.
