### Logical Agents and Knowledge-Based Systems


#### **1. Knowledge-Based Agents (KBA):**
- **Components:**
  - **Knowledge Base (KB)** 
  - **Inference Mechanism:** Derives new knowledge and actions from the KB.

#### **2. Representation and Reasoning:**
- **Syntax and Semantics:**
  - Syntax defines the structure of sentences.
  - Semantics assigns truth values to sentences based on possible worlds or models.
- **Entailment (α ⊨ β):**
  - Sentence **α** entails **β** means β is true in all models where α is true.
  - Equivalently:
    - **Validity:** $ \alpha ⇒ β $ If α is true, then β is guaranteed to be true.
    - **Unsatisfiability:** $ \alpha ∧ ¬β $ means α and ¬β cannot be true together.

---

### Inference Methods:

#### **1. Model Checking:**
- Enumerates all possible models to verify entailment.
- **Advantages:** Simple and guarantees correctness.
- **Disadvantages:** Computationally expensive ($ O(2^n) $) for large KBs.

#### **2. Logical Inference:**
- Uses rules like **Modus Ponens** and **Resolution** to derive new sentences.
- **Soundness:** Produces only entailed sentences.
- **Completeness:** Derives all entailed sentences.

#### **3. Resolution:**
- A single, powerful inference rule for CNF sentences.
- **Steps:**
  1. Convert KB and query to CNF.
  2. Add the negation of the query ($ ¬α $) to the KB.
  3. Resolve clauses iteratively to derive the empty clause (contradiction).
- **Properties:** Sound and complete.

#### **4. Chaining Algorithms:**
- **Forward Chaining:**
  - Data-driven reasoning.
  - Starts with known facts, applies rules to derive new facts.
  - **Efficient for Horn clauses.**
- **Backward Chaining:**
  - Goal-directed reasoning.
  - Works backward from the query to find supporting facts.
  - Suitable for answering specific questions.