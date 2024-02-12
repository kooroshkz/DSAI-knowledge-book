# Lecture 1

## Proposition
A statement or assertion that expresses a judgment or opinion.

## Absurdity
Meaningless.

## Conventions
An agreement between people that assumes something.

| Connective | Name          | Pronunciation | Intuitive Meaning                          |
|------------|---------------|---------------|--------------------------------------------|
| ⊥          | Absurdity     | bottom        | ⊥ never holds (e.g., "The sky is blue and not blue" -> logically false) |
| ∧          | Conjunction   | and           | Both hold                                  |
| ∨          | Disjunction   | or            | φ or ψ or both hold                        |
| →          | Implication   | φ implies ψ   | If φ holds, then ψ holds                   |
| ¬φ         | Negation      | φ -> ⊥        |                                            |
| ⊤          | Truth or Top  | ¬⊥            | Always true (e.g., "A triangle has 3 vertices")|
| φ ↔ ψ      | Bi-implication|               | (φ -> ψ) ∧ (ψ -> φ)                        |

In the parse tree, ¬p will always be p → ⊥.

Sub((𝑟 ∧ 𝑢 → 𝑤) ∧ (𝑢 ∧ ¬𝑤) → ¬𝑟 ) = { 
    𝑟, 𝑢, 𝑟 ∧ 𝑢, 𝑤, 𝑟 ∧ 𝑢 → 𝑤, 
    ⊥, 𝑤 → ⊥, 𝑢 ∧ (𝑤 → ⊥), 
    𝑟 → ⊥, (𝑟 ∧ 𝑢 → 𝑤) ∧ (𝑢 ∧ (𝑤 → ⊥)), 
    (𝑟 ∧ 𝑢 → 𝑤) ∧ (𝑢 ∧ (𝑤 → ⊥)) → (𝑟 → ⊥) 
} 

Top-level connective: ∧ 
Direct subformulas: p, q 
Atomic formula: ⊥ 
Subformulas of 𝜑: all the formulas that appear in the parse tree of 𝜑, including 𝜑 itself  

Set of maps (𝐵^𝐴): 𝐴 → 𝐵 
Powerset: P(𝐴) = {𝑈 | 𝑈 ⊆ 𝐴} 
Natural Numbers: [𝑛] = {𝑘 ∈ N | 𝑘 < 𝑛} [0] = ∅, [1] = {0}
