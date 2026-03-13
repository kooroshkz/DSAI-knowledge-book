**Semantics**: Semantics tells us how to map syntax to behaviour.

**Formal Semantics**: Formal Semantics gives a precise specification to valid programs so that we can reason about them.

**Implementation**: An implementation is a formal semantic for a language.
But it is too precise to be useful, and does not provide us with
any insight.

#### Approaches to Formal Semantics
- **Operational semantics**: Explains what a program does step by step
    - **Structural Operational Semantics (SOS)**: Define rules to describe how each construct of the language changes the state of the computation.
        - **Small-step semantics**: Describe computation as a sequence of small steps. (rule-base transition rules)
- **Denotational Semantics**: Map the constructs of our language to mathematical objects to reason.
- **Axiomatic Semantics**: Explain by logical assertions, such as pre- and post-conditions, about program states.
    - **Hoare Triple**: {P} C {Q} means if pre-condition P holds before executing command C, then post-condition Q will hold after executing C.
        - **Weakest Precondition**: wp(c, Q) is least restrictive condition that guarantees that post-condition Q holds after executing C.
            - $∀P : \{P\}c\{Q\}$ iff $P → R$ where $R = wp(c, Q)$

##### IMP Language

Imperative Language given by the following grammar:

$S ::= x := a$ | skip | $S_0; S_1$ | if $b$ then $S_0$ else $S_1$ | while $b$ do $S$

---

### **State**

* A **state (σ)** means the *current memory* of the program.
* It shows what values each variable has. 
  $σ = \{x₁: val₁, x₂: val₂, ...\}$

For
```
x = 5
y = 3
```

Then the state is $σ = {x: 5, y: 3}$

### **Evaluation Function**

* The evaluation function $(\llbracket \cdot \rrbracket_σ)$ shows **how a statement or expression changes the state**.
* It’s *partial* — meaning it might not give an answer if the program never finishes (like an infinite loop).

If your statement is `x := x + 1`, and the current state is $({x: 5})$, then after running it:

$$\llbracket x := x + 1 \rrbracket_σ = {x: 6}$$

### **Transition System**

* A **transition system** describes **how the program moves** from one state to another while it runs.
* Think of it as showing “step-by-step” how the computer changes things.

For 

```
x := 5;
y := x + 2;
```

You can show transitions like this:

1. Start: σ = {}
2. After $x := 5: σ = {x: 5} $
3. After $y := x + 2: σ = {x: 5, y: 7} $

---

##  **Structural Operational Semantics (SOS)**

SOS explains **how each small part of a program runs**, using *rules*.

### **Assignment**

$(x := a, σ) → σ[x ↦ v]$
It means:
“After running `x := a`, the new state is the old one but with x updated to the value of a.”

**Example:**
$x := 3 + 2$, with $σ = \{\}$ $→ σ[x ↦ 5] = {x: 5}$

### **Skip**

$(skip, σ) → σ$
Doing `skip` means *do nothing*, the state stays the same.

**Example:**
`skip` with σ = {x: 1}
→ still {x: 1}

### **Sequence**

$(S₀; S₁, σ) → (S₁, σ')$
This means: run the first statement `S₀`, then continue with `S₁`.

**Example:**

```
x := 1;
y := x + 1;
```

1. Run `x := 1` → σ = {x: 1}
2. Then run `y := x + 1` → σ = {x: 1, y: 2}

### **If statement**

$$(if\ b\ then\ S₀\ else\ S₁, σ) → (S₀, σ) \text{ if } \llbracket b \rrbracket_σ = true$$

$$(if\ b\ then\ S₀\ else\ S₁, σ) → (S₁, σ) \text{ if } \llbracket b \rrbracket_σ = false$$

**Example:**
If you have

```
if (x > 0) then y := 1 else y := 2
```

and $σ = {x: 5}, →$condition true $→$ run `y := 1`.

### **While loop**

$$(while\ b\ do\ S, σ) → (if\ b\ then\ S; (while\ b\ do\ S)\ else\ skip, σ)$$

This means:
A `while` loop works like an `if` that keeps repeating.

**Example:**

```
while (x < 3) do x := x + 1
```

If σ = {x: 1},
→ becomes `if (x < 3) then x := x + 1; while(x < 3) do x := x + 1 else skip`
→ keeps looping until x = 3.


---

## **Lambda Calculus**

The **λ-calculus** is a tiny, mathematical language that models computation (it’s the base of functional programming).

It uses **functions only** — no variables, no loops, no ifs — just functions and function calls.

**Example**
```
(λx. x + 1) 5
```

This means: “a function that adds 1 to its input, applied to 5.”
→ Result: 6

### **Rules**

#### **β-reduction**

$(λx. M) N → M[N/x]$
Means: replace every `x` in `M` with `N`.

Example:

$(λx. x + 1) 5 → 5 + 1 = 6$

#### **α-conversion**

$λx. M → λy. M[y/x]$
Means: you can rename variable names (to avoid confusion).

Example:

$λx. x + 1 → λy. y + 1$

Same meaning, just different variable name.
