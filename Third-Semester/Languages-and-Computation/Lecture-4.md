## Brzozowski–McCluskey
### Automaton $\to$ Regular Expression

<img src="../../Files/third-semester/lac/14.png" alt="Brzozowski-McCluskey algorithm example 1" width="500"/>

Step 1 matters: Put $\lambda$-transitions to the beginning of the automaton.

**Also** remove all final states (even if there is only one), add one general one and make $\lambda$-transitions from all previous final states to the new one.

**If** there was two loops on the same state, we can combine them as $(xyz+abc)^*$.

### Example:

<img src="../../Files/third-semester/lac/15.png" alt="Brzozowski-McCluskey algorithm example 2" width="300"/>

Answer:

<img src="../../Files/third-semester/lac/16.png" alt="Brzozowski-McCluskey algorithm example 3" width="300"/>

Example 2:

<img src="../../Files/third-semester/lac/17.png" alt="Brzozowski-McCluskey algorithm example 4" width="200"/><br>

Answer:

<img src="../../Files/third-semester/lac/18.png" alt="Brzozowski-McCluskey algorithm example 5" width="300"/>