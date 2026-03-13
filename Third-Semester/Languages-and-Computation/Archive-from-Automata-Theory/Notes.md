A **Pushdown Automaton (PDA)** is formally defined as a **7-tuple**:

$$(Q, \Sigma, \Gamma, q_0, Z_0, A, \delta)$$

| **Symbol** | **Meaning**                        |
|------------|------------------------------------|
| $ Q $     | Set of states                     |
| $ \Sigma $ | Input alphabet                    |
| $ \Gamma $ | Stack alphabet                    |
| $ q_0 $    | Initial state                     |
| $ Z_0 $    | Initial stack symbol              |
| $ A $      | Set of accepting states           |
| $ \delta $ | Transition function               |

---

### Combine **PDA $M_1$** and **FA $M_2$** to accept $L(M_1) \cap L(M_2)$.

## **Summary of the Combined PDA**
1. **States**:  
   $\{(1, P), (1, Q), (2, P), (2, Q)\}$ will be shown as $(1P), (1Q), (2P), (2Q)$.

2. **Transitions**:  
   - From $(1, P)$: Start transitions pushing $a$ or $b$.  
   - From $(2, P)$ and $(2, Q)$: Process $a$'s and $b$'s while updating stack and FA state.

3. **Accepting State** will be intersected like $Accepting(M_1) \cap Accepting(M_2)$.

---

- For a **deterministic finite automaton (DFA)**, each state **must have a transition** for every symbol in the alphabet $\Sigma$.  
     - If a transition for a symbol doesn't exist, the automaton is **incomplete**.
- For a **nondeterministic finite automaton (NFA)**, a state **may or may not** have transitions for every symbol in the alphabet. Missing transitions are allowed.

---

### **Distinguishable Strings**
 
   Two strings $x$ and $y$ are *L-distinguishable* if there exists a string $z$ such that:
   - $xz \in L$ and $yz \notin L$, **or**  
   - $xz \notin L$ and $yz \in L$.  

**Automaton Perspective**:

$$\delta^*(q_0, x) \neq \delta^*(q_0, y),$$

---

**Question:** What does it mean when a string $x \in \Sigma^*$ is accepted by a pushdown automaton $M$ **by empty stack**?

**Answer:**  
A string $x$ is accepted by $M$ by empty stack if:

$$(q_0, x, Z_0) \vdash_M^* (q, \Lambda, \Lambda)$$

for some $ q \in Q $.  

**Explanation**:  
- $ x $ is completely read (input becomes $ \Lambda $).  
- The stack is completely empty, including the initial stack symbol $ Z_0 $.  
- The final state $ q $ does not matter.

---

### **Question**: How can you transform a PDA $M$ (accepting by empty stack) into another PDA $M_1$ that accepts the same language by accepting states?

### **Answer**:

![PDA](../../Files/third-semester/automata/27.png)

##### Sample above applied to PDA:

Before:

![PDA](../../Files/third-semester/automata/28.png)

After:

![PDA](../../Files/third-semester/automata/29.png)

---

### **Pumping Lemma for Context-Free Languages**

Let $L$ be a context-free language. Then there exists an integer $n$ such that for every string $u \in L$ with $|u| \geq n$, the string $u$ can be written as:

$$u = vwx yz$$

where $ v, w, x, y, z $ are substrings of $ u $ that satisfy the following conditions:

1. $ |wy| \geq 1 $ (at least one of $ w $ or $ y $ is non-empty).  
2. $ |wxy| \leq n $ (the combined length of $ w, x, y $ is bounded).  
3. For every $ m \geq 0 $, the string $ v w^m x y^m z $ is also in $ L $ (repeating $ w $ and $ y $ any number of times, including 0, keeps the string in $ L $).

---

### **Key Idea**:
The pumping lemma allows us to identify infinite structures or patterns in context-free languages and can be used to prove that a language is *not* context-free by contradiction.

---

#### $L(M_2) = {L \prime}_1$
We only change accepting states

$Q_2 = Q_1$

$q_2 = q_1$

$\Sigma_2 = \Sigma_1$

$A_2 = Q_1 - A_1$

$\delta_2 = \delta_1$

---

# DFA Minimization

1. For states $x$ and $y$:
    - If **only one** of them is an accepting state, mark it with 1 and leave the rest as 0.

2. For all non-marked pairs left, such as $(1,2)$:
    - a: $\delta(1,a) = m$, $\delta(2,a) = n$
    - b: $\delta(1,b) = l$, $\delta(2,b) = s$

    If $(m,n)$ or $(l,s)$ were marked from step 1, mark it with 2.

3. If it was marked with 2 before, mark it with 3.

4. Draw the minimized graph:
    - 4a: The completed column (mostly $q_0$ or 0) will be the starting point. The final state, which doesn't fit in the table (9), is the accepting state. Draw $A$ and $q_0$ first.
    - 4b: Look at a column to see which ones have a dot and group them. Shape different groups and check in the original graph which states are connected to each other to apply the same grouping. Finally, make the previous accepting states group the new accepting state.

![Automata Image](../../Files/third-semester/automata/3.JPG)
![Automata Image](../../Files/third-semester/automata/4.JPG)

---

## **Subset construction (From $NFA \to DFA$)**

First we make a transition table with the head $|State (q)| \delta(q,a)| \delta (q,b)$ then start from the initial state and find the next states for each input symbol. Finally we will draw a new graph with the states as the nodes and the transitions as the edges.

##### Example:
![automata](../../Files/third-semester/automata/25.png)
| state \( q \) | \( \delta(q, a) \) | \( \delta(q, b) \) |
|--------------|-------------------|-------------------|
| 1            | 234               | ∅                 |
| 234          | 14                | 34                |
| 14           | 1234              | ∅                 |
| 34           | 14                | 4                 |
| 1234         | 1234              | 34                |
| 4            | 14                | ∅                 |
| ∅            | ∅                 | ∅                 |

![automata](../../Files/third-semester/automata/26.png)

---
### Thompson’s Construction (RegEx to NFA):
Converts a RegEx into an equivalent NFA. For example:
- RegEx: $(aa + b)^* (aba)^* bab$
- Step-by-step builds an NFA by combining subcomponents.

![Automata Image](../../Files/third-semester/automata/7.jpg)
![Automata Image](../../Files/third-semester/automata/8.jpg)
![Automata Image](../../Files/third-semester/automata/9.jpg)

---
- **Live Variable**: $A \Rightarrow^* x$ (derives some string $x$ made of terminals).
- **Reachable Variable**: $S \Rightarrow^* \alpha A \beta$ (reachable from the start symbol $S$).

### **Example**:
Let:

$$S \to AB \,|\, b, \quad A \to a, \quad B \to C, \quad C \to D$$

- $ A $ is live and reachable (derives $ a $).
- $ B $ and $ C $ are reachable but not live (they don't derive terminal strings).
- $ D $ is neither live nor reachable.

- **Remove variables** that are not both live and reachable.

---

### **Steps to Convert CFG to CNF**:
1. **Remove $\Lambda$-productions** (empty productions).
2. **Remove unit productions**.
3. **Introduce new variables for terminals**:
   - Replace terminals in long productions with variables (e.g., $X_a \to a$).
4. **Split long productions**:
   - Break down $A \to \alpha$ where $\alpha$ has more than 2 symbols.

Given:

$$S \to aTb \,|\, ab, \quad T \to aTb \,|\, ab$$

1. Replace terminals with variables:
   - $X_a \to a, X_b \to b$.
   - Replace:

$$S \to X_a T X_b \,|\, X_a X_b, \quad T \to X_a T X_b \,|\, X_a X_b$$

2. Split long productions:
   - $S \to X_a Y_1, Y_1 \to T X_b$.
   - $T \to X_a Y_2, Y_2 \to T X_b$.

**Final CNF**:

$$S \to X_a Y_1, \, Y_1 \to T X_b, \, T \to X_a Y_2, \, Y_2 \to T X_b, \, S \to X_a X_b$$

---