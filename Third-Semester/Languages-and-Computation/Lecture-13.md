##### Undecidable Problema in CFG:
- Ambiguity Problem: We cannot find out if a given CFG is ambiguous or not.
- Equality or common string Problem ($L_1 = L_2$ or $L_1 \cap L_2 \neq \emptyset$): We cannot find out if the languages of two given CFGs are equal or have common strings.

##### Undecidable Problems in TM:

- $L(M) = \emptyset$ : Is the language of a given TM empty?
    - If you are given a specific TM, you cannot always decide whether its language is empty.
- $L(G) = \emptyset$ : We cannot decide whether an **unrestricted grammar** generates any string or not.
- $|L(M)|$ is finite: Is the language of a given TM finite?
    - If you are given a specific TM, you cannot always decide whether its language is finite or not.
- $w \in L(M)$ : Is a given string $w$ accepted by the TM?
    - You cannot always decide whether a specific TM accepts a specific string. If halts accepts else no clue.
- **Rice's Theorem**: Any non-trivial property of the language recognized by a Turing machine is undecidable.

**Halting Problem** is not **decidable**.
---

#### Summary:

- Everything in **DFA** is **Decidable**.
- Everything in **CFG** is **Decidable** except:
  - Ambiguity Problem
  - Equality or common string Problem
- Everything in **TM** is **Undecidable**.

##### Post Correspondence Problem (PCP)

Undecidable problem have no algorithm that can always answer whether a solution exists.

##### Complexity classes
- $P$: Problems that can be solved in polynomial time by a deterministic Turing machine. $|\text{input}| = n \Rightarrow$ Time Complexity: $O(n^k)$ for some constant $k$, denoted as $P$.
  - Like sorting, prime checking, finding shortest path in graphs.
- $NP$: Problems for which a proposed solution can be verified in polynomial time by a non-deterministic Turing machine. $|\text{input}| = n \Rightarrow$ Time Complexity: $- We can verify a solution fast if we are given proposed solution. - Most of daily problems which we can check solution fast but finding solution is hard like Sudoku, Hamiltonian path, k-clique. * **P** = easy to solve * **NP** = easy to check * **NP-complete** = hardest problems in NP * **Cook–Levin** = NP = SAT in polynomial time * Solve one NP-complete → solve all NP → **P = NP** Where SAT is a problem of assign$T|F$ to a logical formula such that the formula evaluates to true.