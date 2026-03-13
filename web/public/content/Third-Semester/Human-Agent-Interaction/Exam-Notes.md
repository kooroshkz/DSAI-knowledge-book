**The Research Process (8 Steps)**:
   1. **Research Topic**
   2. **Research Question/Hypothesis**
   3. **Research Strategy and Experiment Design**:
      - Types of research strategies:
        - **Descriptive**: Describes current states of variables.
        - **Correlational**: Examines relationships between variables.
        - **Experimental**: Cause-effect relationships by manipulating variables.
      - Experiment designs include:
         - **within-subjects**: Same participants experience all conditions.
         - **between-subjects**: Different participants for each condition.
         - **factorial designs**: Tests multiple variables simultaneously.
   4. **Operationalizing Variables**: Define variables in measurable terms, ensuring their reliability and validity.
   5. **Selecting a Sample**
   6. **Data Collection**
   7. **Data Processing and Analysis**
   8. **Reporting Results I**(ntroduction)**M**(ethods)**R**(esults)a**D**(iscussion) **format)**
- **Models and Approaches**:
    - **Rule-based Models**: Use social science rules to create nonverbal behaviors.
    - **Performance-based Models**: Rely on human recordings to animate gestures.
    - **Machine Learning Models**

**Challenges in Multimodal Behavior Modeling**:
- Addressing **polysemy**, where a single gesture can have multiple meanings.
**Rule-based vs. Data-driven Approaches**
   - **Rule-based models**: Use predefined rules and linguistic information to generate gestures.
      - **Cerebella Architecture**:
      - A hybrid system that uses both **acoustic** and **linguistic elements** to dynamically generate gestures with both the speech's auditory cues and its semantic structure.
      - Used in both **virtual agent** and **social robotics**.
      - Divides its process into stages:
      1. Input treatment (text and audio processing).
      2. Communicative functions (CFs) like emotion, emphasis analysis.
      3. Behavior mapping based on the context.
      4. Animation scheduling.

      - **GRETA Architecture**:
         - Uses **high-level concepts** and external context (e.g., **dialogue goals** or **user moves**) to influence gesture generation by **communicative intentions**
      
**Workflow**:
   1. **User Input**
   2. **MIND**: The system processes this input, deciding the agent’s emotional tone and what it should say.
   3. **MIDAS**: Adds details to the agent’s response by selecting appropriate gestures and expressions that match the speech.
   4. **BODY**: The chosen gestures are generated and timed perfectly with the speech for a natural response.
   5. **User Model & Context Features**: Throughout, the system considers the user's preferences, reactions, and the external context to tailor the response, ensuring it fits the conversation setting.
- **Moravec’s Paradox**: Machines perform complex tasks, but simple tasks like those a child can do are extremely difficult for robots.
- **Morphology** prioritizes a robot's practical design for specific tasks over appearance.
- **Anthropomorphism** focuses on adding human-like features and behaviors to enhance social interaction.
- **Design Patterns**: Reusable solutions to common problems in HRI design, such as communication patterns, can be applied across different robot designs.
    - **Underpromise and Overdeliver**: Set realistic expectations to avoid disappointment; don’t overhype a robot’s abilities.
    - **Interaction Expands Function**: `Open-ended` design allows users to adapt the robot to their own needs and expectations.
    - **Do Not Mix Metaphors**: Keep design consistent—appearance and behavior should align to avoid discomfort or confusion.
- **Engineering Design Process**: Emphasizes technical problem-solving through simulations, but is limited in open-ended contexts.
- **User-Centered Design (UCD)**: Involves users to ensure designs meet their needs, with early prototype testing.
- **Participatory Design**: Collaborative approach where users co-create designs, essential for specific groups like the elderly.
**Measuring Anthropomorphization**:
   - **Explicit measurements** involve directly asking people about their perceptions.
      - **Mind perception**: assess people believe a robot has **agency** (the ability to act intentionally) and **experience** (the ability to feel emotions).
      - **Warmth and competence - Robotic Social Attributes Scale (RoSAS)**: how friendly (warm) and capable (competent) they are.
      - The **Godspeed Questionnaire**: evaluate human-robot interaction through five key dimensions:
         - **Anthropomorphism** – How human-like the robot appears.
         - **Animacy** – How "alive" or animated the robot seems.
         - **Likeability**
         - **Intelligence**
         - **Safety** – How safe the person feels interacting with the robot.

   - **Implicit measurements** assess by observing behaviors, like measuring their **reaction times**.
- **multimodal perception** by McGurk Effect: Visual cues (like lip movements) influence what we hear.
- **Voice Activity Detection (VAD)**: Recognizes when someone is speaking but doesn’t transcribe. Useful for detecting when a robot should start listening.

- **Artificial Languages**:
  - **Engineered Languages**: Designed for **logic, philosophy, or linguistics** experiments (e.g., **Loglan**, **ROILA**).
    - **ROILA**: Developed for **HRI** to improve **speech-recognition accuracy**. Words are designed to sound distinct for better recognition by robots. Like "Go forward" = **kanek koloke**, "Go back" = **kanek nole**.
  - **Auxiliary Languages**: Created to **bridge natural languages** or serve as an **international medium** (e.g., **Esperanto**).
  - **Artistic Languages**: Made for **fictional worlds** (e.g., **Klingon**, **Elfish**, **Dothraki**).
- Ambivalent(uncertainty) Attitudes Toward Robots: This ambivalence can cause internal conflict and affect how society integrates robots.
- **Research Questions:**
    - Exploratory: No pre-hypotheses
    - Confirmatory: With hypotheses

- **Research Type**
    - *Correlation:* Identifies patterns not determine cause (e.g., survey studies).
     - *Causation:* Experimental on cause-effect relationship (e.g., randomized control trials).
     - *Spurious correlation:* Correlation without Causation
- **Research Designs:**
   - **Between-Subjects Design:** Different groups experience different conditions (e.g., comparing two robot types).
   - **Within-Subjects Design:** Same participants experience all conditions.(e.g., multiple robots).
   - **Sample Size**
- Variables:
    -  Independent Variables (IV)
        - Variable that the experimenter **manipulates or changes**
        
    - Dependent Variables (DV)
        - **Definition**: The variable that the experimenter **measures**.
- The **independent variable** causes changes.
- The **dependent variable** shows the effects.
- Standards for Statistical Analysis

    - **Core Elements**: Tendency (mean), variability (spread), and sample size -> generate p-values.
    - **NHST**: Null hypothesis significance testing (NHST) uses the **p-value**
    - **Errors**
    - **Effect Size**
#### Socially Interactive Agent (SIA)

- No or minimal embodiment
    - Chatbots and automated call centers (Siri & Eliza)
- Physical embodiment
    - social robots with a focus on physical properties (Morphology) like NAO & Pepper
- Virtual embodiment
    - Intelligent Virtual Agents

- **Agent Architectures**
   - **Sense-Think-Act Cycle**
   - **Subsumption Architecture**:
     - Hierarchical task-specific modules for continuous behavior (action-reaction).
     - Difficult to manage complex behaviors.
   - **Layered Architecture**:
     - Behavior organized in layers (Reactive, Executive, Deliberative, Reflective).
     - Challenges include deciding functionality placement.
**Location Context**:
   - **Lab**: Controlled setting.
   - **Field**: Real-world setting.
   - **Crowd-Sourced**: Remote studies (e.g., MTurk).
### Prototypical HAI Studies
1. **Perception Study**: Evaluating user perception of robot behavior.
2. **Pilot Study**: Testing system robustness and usability.
3. **Impact Study**: Measuring the effect of robot interaction on learning or behavior.
- **Social Signal Processing (SSP)**: Understand non-verbal behaviors in machines for human interaction with components:

1. **Behavioral Cues**: Short-term, observable actions (e.g., nodding, smiling, raising voice).
2. **Behavior**: Longer-term patterns of cues (e.g., nodding and smiling signal agreement).
3. **Social Signals**: Cues or behaviors that convey social meaning (e.g., dominance, warmth, competence).
- **Proxemics**: The study of personal space in social interactions. Four zones:
   - **Intimate Distance** (< 0.5m): Close relationships.
   - **Personal Distance** (0.5m–1.2m): Friends and relatives.
   - **Social Distance** (1.2m–3.7m): Acquaintances.
   - **Public Distance** (> 3.7m): Strangers, public speaking.
- prototypes:
    - **Low fidelity**: Simple, static, basic design.
    - **High fidelity**: Detailed, functional, closer to the final product.
- Robot should join L-shape converstation also:
    - O-space: inner circle while converstating
    - P-space: The circle people are standing
    - R-space: Border of P-space circle
- Affordance: Features determina how object can be used.
    - Perceived affordances (what a person thinks is possible) 
    - Supported affordances (what the system actually allows)