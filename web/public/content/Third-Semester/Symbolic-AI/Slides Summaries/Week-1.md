Understanding and consciousness: Human biological brain
Intelligent behavior does not imply the machine is conscious and understanding
However, machines can be intelligent
**Artificial General Intelligence :** reasoning, learning, problem solving, generalisation

**Strong AI:** Machines that act intelligently can eventually also possess consciousness

### Different approaches to AI:

1. **Classic AI**: (Focus on model structure, formalism and architecture)
    - Agent-based reasoning
    - Utilizes search, logic, and rule-based systems
    - Symbol manipulation
    - Includes agents, environments, and memory

2. **Machine Learning**

3. **Cognitive Science/Cognitive Modelling**: (Focus on model structure, formalism and architecture)
    - Replicating psychological and biological mechanisms that lead to intelligent behavior
    - Utilizes frameworks like ACT-R and SOAR.

4. **Computational Intelligence/Natural Computing:** (More Biological Approach, Focus on model outputs behavior and solution)
    - Draws inspiration from biological systems for search and optimization
    - Includes techniques like swarm intelligence* and genetic algorithms.

*Swarm intelligence: agents interacting locally with one another and with the environment

### Classical (Symbolic) AI or Good Old-fashioned AI (GOFAI)

focusses on knowledge representation and general purpose “reasoning” mechanisms.

- Separation between knowledge and reasoning.
- Generic reasoning (problem-solving) based on search and logic.
**Rational agent** = an agent program that chooses actions such
that for any given percept sequence the expectation of
payoff for an action is maximal according to some pay-off
function.
---

### Approaches to AI
- **Classical AI**: Rule-based reasoning and logic.
- **Machine Learning**: Data-driven approach with minimal domain knowledge.
- **Cognitive Modeling**: Mimics biological and psychological mechanisms.
- **Computational Intelligence**: Inspired by biology (e.g., genetic algorithms, swarm intelligence).

<hr>

### **Environment Properties:**
These describe the nature of the world the agent interacts with.

1. **Fully Observable vs. Partially Observable:**
   - **Fully Observable:** The agent can see everything it needs to make a decision (e.g., Tic Tac Toe: you can see the entire board).
   - **Partially Observable:** The agent can't see the entire environment (e.g., in a game like Stratego, you can’t see all of your opponent’s pieces).

2. **Single Agent vs. Multi-Agent:**
   - **Single Agent:** Only one agent is making decisions (e.g., Solitaire).
   - **Multi-Agent:** Multiple agents interact, which can be competitive (e.g., Tic Tac Toe) or cooperative (e.g., multiplayer games).

3. **Deterministic vs. Stochastic:**
   - **Deterministic:** The next state is entirely predictable from the current state and action (e.g., a puzzle game like Tetris).
   - **Stochastic:** There is some randomness in the outcome of actions (e.g., Pacman, where ghosts can move unpredictably).

4. **Episodic vs. Sequential:**
   - **Episodic:** Each action is independent of previous ones (e.g., a game where every round resets).
   - **Sequential:** Actions are connected, and decisions in earlier steps affect future outcomes (e.g., Mario Bros).

5. **Static vs. Dynamic:**
   - **Static:** The environment only changes when the agent acts (e.g., Chess, where the board stays the same until a move is made).
   - **Dynamic:** The environment changes on its own, regardless of the agent’s actions (e.g., Pacman, where ghosts move around even if Pacman doesn’t).

6. **Discrete vs. Continuous:**
   - **Discrete:** The environment has a limited set of distinct states or actions (e.g., Tic Tac Toe has a fixed number of moves).
   - **Continuous:** There are infinite possibilities for states or actions (e.g., controlling a car in a racing game).

7. **Known Model vs. Learned Model:**
   - **Known Model:** The agent already knows how its actions will affect the environment (e.g., an experienced driver who knows how turning the wheel affects the car).
   - **Learned Model:** The agent has to learn the effects of its actions over time (e.g., a beginner learning to drive).

---

### **Types of Agents:**

1. **Reflexive Agents:**
   - These agents react directly to current perceptions without thinking about the past or the future.
   - Example: In Tic Tac Toe, if the other player puts an “X” in the middle, the reflexive agent always responds by putting an “O” in a specific corner.
   - **Limitations:** These agents don’t store history, so they may make poor decisions, like making illegal moves.

2. **Model-based Reflexive Agents:**
   - These agents remember past states (percepts) to make better decisions.
   - Example: The agent remembers that it placed an “O” in a specific spot earlier and won’t place another piece there.
   - **Benefit:** Solves issues of illegal or irrational moves by using memory.
   - **Limitation:** Can’t plan ahead to win; it just reacts.

3. **Goal-based Agents:**
   - These agents have specific goals and plan actions to reach those goals.
   - Example: In Tic Tac Toe, the agent plans moves to create a row of three “O”s and win the game.
   - **Benefit:** They can plan steps to reach a goal.
   - **Limitation:** If there are multiple goals or paths, it’s harder to decide the best one.

4. **Utility-based Agents:**
   - These agents consider not just goals but also the value (utility) of different outcomes and actions.
   - Example: An agent that knows winning is worth more than a draw and makes moves that maximize its chance of winning.
   - **Benefit:** They make more sophisticated decisions by considering the desirability of different outcomes.
   - **Limitation:** Calculating utilities for all possible outcomes can be complex.


---

### **Knowledge Representation:**

1. **Atomic Representation:**
   - Each state is represented as a single symbol without any internal structure.
   - Example: In Tic Tac Toe, the entire board could be represented by a single number, like “5” to describe the state of the game.
   - **Limitation:** There’s no way to compare states or make detailed decisions.

2. **Factorial Representation:**
   - A state is represented as a set of features, and each feature can have a value.
   - Example: In Tic Tac Toe, the state could be represented by the presence or absence of an “X” or “O” in each square. Each square could be a Boolean (true/false) value.
   - **Benefit:** You can compare states based on their features (e.g., does one square have an “X” while another has an “O”?).
   - **Limitation:** Only captures predefined features, so it's less flexible.

3. **Structural Representation:**
   - States are represented as objects and their relationships, similar to how humans think.
   - Example: In Tic Tac Toe, instead of just marking squares, you could describe relationships like "there are two ‘O’s in a row in the top row."
   - **Benefit:** This allows for more complex reasoning, similar to human thought processes.
   - **Limitation:** It can be more complex to implement and manage.
