
- **Terms:**
  - Variables: Start with uppercase (e.g., `X`, `Agent`).
  - Constants: Start with lowercase (e.g., `key`, `door`).

- **Predicates:**
  - Structure: `name(Term1, Term2, ...)`.
  - Example: `parent(joost, leon)`.

- **Sentences:**
  - Combine predicates with logical operators to create rules.
  - Structure: `{Condition} > {Conclusion}`.
  - Example: `parent(Z, X) & parent(Z, Y) & !=(X, Y) > sibling(X, Y)`.

---

#### 2. **Operators in SFOL:**
- **Belief Updates:**
  - `+`: Add fact to the belief base.
  - `-`: Remove fact from the belief base.

- **Goals and Intentions:**
  - `*`: Add goal (adopt).
  - `~`: Remove goal (drop automatically when achieved).
  - `_`: Add intention (action).

- **Reserved Predicates:**
  - `=(X, Y)`: True if `X` equals `Y`.
  - `!=(X, Y)`: True if `X` not equals `Y`.
  - `!pred(...)`: True if `pred(...)` is not in the belief base.

---

#### 3. **Defining Rules in SFOL:**

1. **Percept Rules:**
   - Process environmental perceptions to update the belief base.
   - Example:
     ```prolog
     at(X) > +agentLocation(X)
     passage(Y) > +link(agentLocation, Y)
     key(K) > +keyAtLocation(K)
     ```

2. **Program Rules:**
   - Define actions or goals based on current beliefs.
   - Example:
     ```prolog
     agentLocation(X) & keyAtLocation(K) > _grab(X, K)
     agentLocation(X) & locked(D) & key(K) > _open(X, K)
     link(X, Y) > _moveTo(Y)
     ```

3. **Action Rules:**
   - Specify postconditions for actions to update beliefs logically.
   - Example:
     ```prolog
     grab(X, K) > +hasKey(K) & -keyAtLocation(K)
     open(X, K) > -locked(D) & +doorOpen(D)
     moveTo(Y) > +agentLocation(Y) & -agentLocation(X)
     ```

---

#### 4. **Agent Cycle Using SFOL:**

1. **Sense:**
   - Process percepts from the environment and update the belief base.
   - Use percept rules for this step.

2. **Think:**
   - Evaluate program rules to generate new intentions (actions or goals).
   - Use inference to apply program rules based on the belief base.

3. **Decide:**
   - Select an action from the list of generated intentions.
   - Use planning if multiple actions need sequencing.

4. **Act:**
   - Execute the chosen action and update beliefs based on action rules.

---

#### 5. **Example Rules for a Maze-escaping Agent:**

1. **Percept Rules:**
   ```prolog
   at(X) > +currentLocation(X)
   passage(Y) > +passageTo(currentLocation, Y)
   key(K) > +keyAvailable(K)
   locked(D) > +doorLocked(D)
   ```

2. **Program Rules:**
   ```prolog
   currentLocation(X) & keyAvailable(K) > _grab(X, K)
   currentLocation(X) & doorLocked(D) & key(K) > _open(X, K)
   passageTo(currentLocation, Y) > _moveTo(Y)
   ```

3. **Action Rules:**
   ```prolog
   grab(X, K) > +hasKey(K) & -keyAvailable(K)
   open(X, K) > +doorUnlocked(D) & -doorLocked(D)
   moveTo(Y) > +currentLocation(Y) & -currentLocation(X)
   ```
