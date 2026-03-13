**Context Sensitive Languages**: Context sensitive languages can be recognized by linear bounded automata (LBA) which are non-deterministic Turing machine which have limited tape. (Size of tape = size of input)
    - Never make the word shrink

- **Decision Problems**: Problem with a YES/NO answer.
    - Example: for $x$ and $y$, if $x >= y$?
    - **Instance** of a decision problem: Set of specific inputs for the problem. (e.g. $(3,5)$ for the above problem)
    - **Decidable Problem**: If turing machine exists which halts for all inputs of the problem
**Thomson algorithm** and **Deterministic Finite Automaton** makes problems **decidable**(Y/N).

Pushdown automaton makes problems **partially decidable**(Yes but not always No).

##### Decidable Problems in DFA:
- Emptiness Problem ($w \in L$): Is the language of a given DFA empty?
    - If there is no path from start state to any accepting state -> empty language
- Finiteness Problem ($w$ is finite): Is the language of a given DFA finite?
    - If there is no cycle in the path from start state to any accepting state -> finite language
    - If there is a cycle in the path from start state to any accepting state -> infinite language
- Membership Problem ($w \in L$): Is a given string $w$ accepted by the DFA?
- Equality Problem ($L_1 = L_2$): Are the languages of two given DFAs equal? ($(L_1 \cap L_2) \cup (L_2 \cap L_1) = \emptyset$)

##### Decidable Problems in CFG:
- $L(G) = \emptyset$ : Is the language of a given CFG empty?
    - If there is no derivation from start symbol to any terminal string -> empty language
- $|L(G)|$ is finite: Is the language of a given CFG finite?
    - If there is no cycle in the derivation from start symbol to any terminal string -> finite language
    - If there is a cycle in the derivation from start symbol to any terminal string -> infinite language