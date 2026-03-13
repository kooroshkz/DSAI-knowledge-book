## Chumsky Normal Form (CNF)

If we write grammer in this form it makes parsing speed increase way faster. Every grammer can be converted to CNF form.

- We want all production to be:
    - A -> BC (A non-terminal produce B and C non-terminals)
    - A -> a (A non-terminal produce a terminal)

Algorithms to convert grammer to CNF:
- 1a) **Identify nullable variables**: ($S,T,U,.. \in V_N$)
- 1b) **Eliminate Null Productions** and **Add new productions**:
    - If $T \rightarrow aTb$ and $T$ is nullable then remove $T$ and add the rest to productions $T \rightarrow aTb | ab$
    - If we have two Nullables we write them each or combination like:
        - $S \rightarrow TU$ will be $S \rightarrow TU | T | U$
        - For $S \rightarrow ACB$ we have $S \rightarrow ACB | CB | AB | AC | A | B | C$
- 2a) **Draw a directed graph for nullable variables**
- 2b) **Remove lonely Nullable productions in RHS and add derivations to production**
- 3a) **For terminals define a production and replace**
- 3b) **To make it CNF we need to break down productions with more than 2 non-terminals in RHS**

<img src="../../Files/third-semester/lac/34.png" alt="Chomsky Normal Form Example" width="600"/> <br>

<img src="../../Files/third-semester/lac/35.png" alt="Chomsky Normal Form Example" width="600"/> <br>

<img src="../../Files/third-semester/lac/36.png" alt="Chomsky Normal Form Example" width="300"/>
