
# Inference in First-Order Logic

### Inference Rules for Quantifiers
- **Universal Instantiation (UI):** From $\forall x P(x)$, infer $P(a)$ for any constant $a$.
  - Example: From $\forall x (King(x) \land Greedy(x) \Rightarrow Evil(x))$, infer:
    - $(King(John) \land Greedy(John)) \Rightarrow Evil(John)$
- **Existential Instantiation (EI):** From $\exists x P(x)$, infer $P(k)$, where $k$ is a new constant (Skolem constant).
  - Example: From $\exists x (Crown(x) \land OnHead(x, John))$, infer:
    - $Crown(C_1) \land OnHead(C_1, John)$

### Unification
Unification finds a substitution $\theta$ that makes two expressions identical.
- Example: UNIFY($Knows(John, x)$, $Knows(John, Mary)$) $\rightarrow \{\theta: x/Mary\}$

- **Forward Chaining**
    - Start with known facts.
    - Apply rules in a forward direction to infer new facts.
    - Stop when no new facts can be inferred or when the query is proven.

- **Backward Chaining**
    - Start with the goal (query).
    - Find rules that could satisfy the goal.
    - Recursively prove the premises of these rules.
---

## Resolution

### Converting to Conjunctive Normal Form (CNF)
1. Eliminate implications: $A \Rightarrow B$ becomes $\neg A \lor B$.
2. Standardize variables: Rename variables to avoid conflicts.
3. Skolemize: Replace existential quantifiers with Skolem constants/functions.
4. Distribute $\lor$ over $\land$.