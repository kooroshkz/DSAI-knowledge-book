## **- Boolean/Propositional logic**:
- **Components:**
  - **Atoms**: Basic symbols represent facts can be either True (1) or False (0): $Wall_{1,2}$.
  - **Literals**: Atoms with possible negation (e.g., A, ¬B).
  - **Sentences**: literals connected by operators: Agent1,1 ∧ ¬Wall1,2 → Moveright

- **Note**: The subscript is NOT a variable, $Agent_{1,1}$ is a particular variable encoding the knowledge at location y,x. A separate variable is needed for every possible location.
The KB represents all the information you assume to be true in the problem. 

**Inference** is the process of deriving new information or conclusions from known facts or rules using logical reasoning.
#### **Inference Techniques**
1. **Inference by Enumeration**:
   - Check if the query (e.g., `Moveright`) is always true when the knowledge base (KB) is true.
   - Example:
     - Rules: `Agent1,1 ∧ ¬Wall1,2 ⇒ Moveright`, `Agent1,1`, `¬Wall1,2`.
     - Query: Is `Moveright` true?
     - Analyze combinations of truth values in a truth table.

2. **Inference by Proof**:
   - Use inference rules to deduce whether KB leads to the query.
   - Trial and error may be needed to identify applicable rules.

3. **Inference with just one rule: Resolution**:
   - a logical inference rule used to prove whether a statement (query) is true or false by combining known facts and rules.
   - It works by **eliminating contradictions** to determine if the query follows logically from the knowledge base (KB).
   - **CNF** is a standardized format to make resolution possible.

##### How to Convert to CNF:
1. **Eliminate Implications (⇒)**:
   - `A ⇒ B` becomes `¬A ∨ B`.
2. **Move NOTs (`¬`) Inside** (De Morgan's Laws):
   - `¬(A ∨ B)` becomes `¬A ∧ ¬B`.
   - `¬(A ∧ B)` becomes `¬A ∨ ¬B`.
3. **Distribute OR (`∨`) Over AND (`∧`)**:
   - `(A ∧ B) ∨ C` becomes `(A ∨ C) ∧ (B ∨ C)`.

#### **Definite Clauses**
- Form: `(A ∧ B ∧ …) ⇒ C` or `¬A ∨ ¬B ∨ … ∨ C`.
- Advantage:
  - Simplifies chaining proofs.
  - Human-readable format.

#### **Chaining**
- **Forward Chaining**:
  - Derive new facts from known rules and facts.

- **Horn Clauses:**
  - A special subset of CNF with at most one positive literal.
  - Used in efficient inference methods (e.g., forward/backward chaining).
## **- First order logic/Predicatecalculus/Predicate logic logic**:
- Representation of **objects**, **relations**, and **facts** with **quantifiers**.


### **Components of FOL**
1. **Facts**: Statements about the world (e.g., `mother(Heleen, Joost)`).
2. **Objects**: Entities (e.g., `Heleen`, `Joost`).
3. **Relations**: Connect objects (e.g., `mother(x, y)`, `loves(x, y)`).
4. **Quantifiers**:
   - **Universal Quantifier (`∀`)**:`∀x loves(x, y)`
   - **Existential Quantifier (`∃`)**:`∃x loves(x, y)`
   - **Nest Quantifiers**: `∀x ∃y relation(x, y)` 


##### **Example**
- **Statement**: "My mother, Heleen, has three children: Joost, Fien, and Lot. Children always love each other."
  - **Representation**:
    - `mother(Heleen, Joost)`, `mother(Heleen, Fien)`, `mother(Heleen, Lot)`.
    - `∀x ∀y child(x) ∧ child(y) ⇒ loves(x, y)`.
## **- Inference with predicate logic**:
#### **Reduction to Propositional Logic**
1. **Universal Instantiation**:
   - Replace universal quantifiers (`∀`) with ground terms from the domain.
   - Example:
     - `∀x human(x) ⇒ mortal(x)` becomes:
       - `human(joost) ⇒ mortal(joost)`
       - `human(fien) ⇒ mortal(fien)`
   - Translate to propositional logic:
     - `H_j ⇒ M_j`, `H_f ⇒ M_f`, `H_j`, `H_f`.
   - Query: `M_j` (Is `mortal(joost)` true?).

2. **Existential Instantiation**:
   - Replace existential quantifiers (`∃`) with a **Skolem constant** (a placeholder for an unspecified object).
   - Example:
     - `∀y (∃x owns(y, x) ⇒ hasProperty(y))` becomes:
       - `∀y owns(y, C) ⇒ hasProperty(y)` (with `C` as the Skolem constant).
     - Query: `hasProperty(joost)`.


#### **Resolution in First-Order Logic**
1. **Steps**:
   - Convert sentences to **Conjunctive Normal Form (CNF)**.
   - Use **unification** to match variables in literals.
   - Combine clauses and remove complementary literals.

2. **Example**:
   - **Knowledge**:
     - `∀y (∃x owns(y, x) ⇒ hasProperty(y))`
     - `owns(joost, house)`
   - **Query**: `hasProperty(joost)`.

   - **Conversion to CNF**:
     1. `⇒` elimination: `∀y (¬∃x owns(y, x) ∨ hasProperty(y))`.
     2. Move `¬` inside using De Morgan's Laws: `∀y ∀x (¬owns(y, x) ∨ hasProperty(y))`.
     3. Drop quantifiers: `¬owns(y, x) ∨ hasProperty(y)` (lifted CNF).

   - **Resolution**:
     - Assume `¬hasProperty(joost)` (negation of query).
     - Unify `owns(joost, house)` with `¬owns(y, x)`.
     - Results in `hasProperty(joost)` and `¬hasProperty(joost)` → Contradiction.
     - Conclusion: `hasProperty(joost)` is true.


#### **Unification**
- **Definition**: Process of making two logical expressions identical by substituting variables.
- **Example**:
  - Database: `father(peter, joost)`.
  - Query: `father(x, y)`?
  - Substitution: `x/peter`, `y/joost`.


#### **Forward Chaining**
1. Start with facts and repeatedly apply rules to deduce new facts.
2. **Example**:
   - KB:
     - `Parent(joost, sacha)`, `Parent(joost, leon)`.
     - `Parent(x, y) ∧ Parent(x, z) ∧ ¬(y = z) ⇒ sibling(y, z)`.
   - Query: `sibling(leon, x)` (Who are siblings of Leon?).
3. **Process**:
   - Substitute `x` with known values: `sibling(leon, sacha)`.


#### **Backward Chaining**
1. Start with the query and work backward, finding rules that lead to it.
2. **Example**:
   - KB:
     - `Parent(joost, sacha)`, `Parent(joost, leon)`.
     - `Parent(x, y) ∧ Parent(x, z) ∧ ¬(y = z) ⇒ sibling(y, z)`.
   - Query: `sibling(leon, sacha)` (Is Sacha a sibling of Leon?).
3. **Process**:
   - Check if `sibling(leon, sacha)` unifies with any known fact.
   - Substitute variables in rules and verify premises.