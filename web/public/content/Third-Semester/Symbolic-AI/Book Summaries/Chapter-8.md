## **Chapter 8: First-Order Logic (FOL)**


**Sets**:
   - Predicates: $x \in s$, $s_1 \subseteq s_2$.
   - Axioms:
     - $\forall s Set(s) \Leftrightarrow (s = \{\} ) \lor \exists x, s_2 (Set(s_2) \land s = \{x|s_2\})$.
     - $\forall x, s x \in \{\} \Leftrightarrow False$.
     - $\forall x, s x \in \{x|s\} \Leftrightarrow True$.

**Wumpus World**:
   - Represent adjacency:
     - $\forall x, y, a, b Adjacent([x, y], [a, b]) \Leftrightarrow (x = a \land |y - b| = 1) \lor (y = b \land |x - a| = 1)$.
   - Breeze logic:
     - $\forall s Breezy(s) \Leftrightarrow \exists r Adjacent(r, s) \land Pit(r)$.

---

### **Key Advantages of FOL**
- **Expressiveness**: Captures general rules and relationships.
- **Compositionality**: The meaning of a complex sentence derives from its parts.
- **Logical Inference**: Supports structured reasoning and generalization.