**Von Neumann Architecture:** Design model of the most modern computers with micro-architecture →
→ **CPU (Central Processing Unit)**
  ↳ **Control Unit (CU):** Directs the flow of data and instructions.
  ↳ **Arithmetic/Logic Unit (ALU):** Does math and logic operations.
→ **Memory Unit:** Stores both data and instructions.
→ **Input/Output (I/O) Unit:** For communication with the outside world.

**Von Neumann Bottleneck:** Data and instructions share the same bus (Stored in Memory), causing a limitation in throughput (data transfer rate).

**Process (fetch-decode-execute cycle):**
 1️⃣ **Fetch:** CPU gets next instruction from memory (using the program counter).
 2️⃣ **Decode + Execute:** CPU understands and runs it.
 3️⃣ **Increase Program Counter:** Move to next instruction (**Imperative paradigm**: goes instruction after instruction).

✔️ Well-defined → clear, unique answer.
✖️ Ill-defined → unclear, no single answer.

**MIPS Architecture:**
→ MIPS is a type of CPU design (a RISC – Reduced Instruction Set Computer).
→ Instructions are always **32 bits**, in **three formats:**
  • **R-type (Register):** For operations between registers (add, sub).
  • **I-type (Immediate):** For operations with constants or memory addresses.
  • **J-type (Jump):** For jump instructions (changing the program counter).

```assembly
add $r1,$r2, $r6 # This means: `$r6 = $r1 +$r2`
```

**Machine code (decimal fields):** `[ op | rs | rt | rd | shamt | funct ]`
  op = 0 → R-type instruction.
  rs = 1 → first input register.
  rt = 2 → second input register.
  rd = 6 → destination register.
  shamt = 0 → no shifting.
  funct = 32 → tells CPU this is an **add** operation.

🧠 **Zuse’s Plankalkül:** The first high-level programming language.

**Turing Machine:**
A computer model that uses:
→ **Initial data** (a tape of 1s and 0s).
→ **Rules** (a table: e.g., if in this state and number is 1 → change to 0 and move right).
→ **Halting state** (where computation stops).
The tape’s final state = computation result.
Shows that problems can be broken down into simple rules a Turing machine can handle → any computation a computer can do.

🗣 **Linguistic Relativity:** The language we speak influences how we think and perceive the world.

**Typing systems:**
→ **Duck Typing:** Type doesn’t matter if behavior fits (e.g., Python, Ruby).
→ **Static Typing:** Types checked at compile-time (e.g., Java, C, C#).
→ **Dynamic Typing:** Types checked at runtime (e.g., Python, JavaScript).
→ **Gradual Typing:** Mix of static + dynamic (e.g., TypeScript, Python with hints).

**Language types:**
→ **Formal Language:** Strict rules/syntax (e.g., programming languages).
→ **Natural Language:** Evolved for daily use (e.g., English, Spanish).
→ **Semi-formal Language:** Mix of both (e.g., math notation, UML diagrams).

---
**Formal Grammar Components**
- **1. Metalanguage**: Language used to describe another language (English for programming languages)
- **2. Object Language**: The language being described (Python, Java, etc.)
- **3. Terminal**: The smallest symbols of the object language (e.g., `2`, `+`, `3`)
- **4. Non-terminal**: Placeholder symbols (e.g., `<expression>`, `<number>`)
- **5. Rule (Production)**: A way to replace a non-terminal with other symbols (terminals or non-terminals). (e.g., `<expression> → <number> + <number>`, `<number> → 2 | 3`)
- **6. Derivation (Parse)**: The step-by-step process of applying rules until only terminals remain.
- **7. Start Symbol**: The main non-terminal we begin with.

- **Lexical ambiguity**, arising from multiple meanings of words like "I saw a bat" (the animal or the sporting equipment)
- **Syntactical ambiguity**, where the grammatical structure allows for different interpretations (or parse trees) like "I saw the man with the telescope."

**Chomsky Hierarchy**
- **Type-0: Unrestricted (Free Grammar - Most Complex and General)**: Like Universal languages (can describe any computable language)
- **Type-1: Context-Sensitive Grammar (CSG)**: Rules depend on surrounding symbols (e.g., `A B C → A D C` if `B` is in a certain context, e.g.: Grammar for natural languages)
- **Type-2: Context-Free Grammar (CFG)**: Rules are applied regardless of context (e.g., `A → B C`, e.g.: Grammar for arithmetic expressions) $\to$ **Most programming languages**
- **Type-3: Regular Grammar**: Simplest form, rules are linear (e.g., `A → aB | b`, e.g.: Grammar for making postaddresses)


**Associativity**: A binary operator ($\oplus$) can be: * **Left-associative**: $A \oplus B \oplus C = (A \oplus B) \oplus C$ * **Right-associative**: $A \oplus B \oplus C = A \oplus (B \oplus C)$ * **Associative**: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$ 

**Precedence**: If there are two binary operators, $\oplus$ and $\otimes$:  $\otimes$ has **higher precedence** than $\oplus$ if: $A \oplus B \otimes C = A \oplus (B \otimes C)$ Meaning: do $\otimes$ first before $\oplus$.

---
**Lexical Analysis**: First step of compilation which converts source code into tokens.
* **Lexeme**: The smallest meaningful unit in the source code. Example: `if`, `x`, `42`, `+` are all lexemes.
* **Token**: A **category** or **type** that groups lexemes. Example: `if` → keyword token `x` → identifier token `42` → number token `+` → operator token
* **Lexer** or **Scanner**: Program does lexical analysis, reads source code and produces tokens.
  * **Regular Expressions (Regex) Lexer**: Write rules like:
   * identifiers = `[a-zA-Z_][a-zA-Z0-9_]*`
   * numbers = `[0-9]+`
     Then, a program uses these rules to recognize tokens.
  * **Finite State Machine (FSM) Lexer**: Build a machine with states and transitions that recognize valid tokens step by step (like following a flowchart of character inputs).

**Syntax Analysis**: After lexical analysis, the **parser** takes a sequence of tokens (from the lexer) and tries to build a structure (parse tree) using those grammar rules. Tokens: `int`, `x`, `=`, `42`, `;` then *parser* check if it fits grammar rule like `Statement → Type Identifier '=' Number ';'`, then builds a parse tree.

**Parsing strategies**: **Top-Down Parsing**: Start from the root of the parse tree and try to build it down to the leaves (tokens). **Bottom-Up Parsing**: Start from the tokens and try to build up to the root of the parse tree.

**Parsing as Graph Search**

1. **Parsing** = build structure (parse tree) from tokens using grammar.
2. **Naive BFS** → explores all possibilities → exponential growth.
3. **Prefix test** → cut branches if they don’t match target string’s prefix.
4. **Leftmost derivation** = always expand the leftmost non-terminal first.
   * Makes search systematic.
5. **BFS + Leftmost + Prefix test** → faster, fewer branches.
6. **Problem**: Some grammars still blow up (too many useless branches).

**Recursive Descent Parsing**: A top-down parsing method with DFS instead of BFS using recursion. Each non-terminal in the grammar has a function. Each rule is handled by code inside that function. **Problem**: Infinite recursion $\to$ Solution:  **Left recursion**.

**Left Recursion**: A grammar is left recursive if a non-terminal A can eventually derive a form starting with itself $A ⇒^* Aγ$ where $⇒^*$ means in zero or more steps
    - Direct left recursion: $A ⇒ Aγ$
    - Indirect left recursion: $A ⇒^* Aγ$
    - **Problem**: Left recursion causes infinite recursion in recursive descent parsing.
    - **Solution**: Eliminate left recursion by rewriting rules. Remove Direct Left Recursion:

```
A ::= Aα1 | Aα2 | ... | Aαn | β1 | ... | βk
```

We rewrite as:

```
A ::= β1A' | β2A' | ... | βkA'
A' ::= α1A' | α2A' | ... | αnA' | ε
```

Where `Aα1,...` are Left Recursive productions and `β1,...` are Non-Left Recursive productions.

**‍Predictive Parser**:‌ BFS, DFS are slow due to backtracking. A **lookahead parser** peeks at the next token to decide which rule to apply, reducing backtracking.

**One-step lookahead**: Rule for $LL(1)$ grammar
- First L, parse from left-to-right and second creates the leftmost derivation (**Left recursion test**)
- If A → α, A → β then FIRST(α) ∩ FIRST(β) = ∅ (**pairwise disjointness test**)
- **LL(k) Parsers** use k tokens of lookahead to decide which rule to apply which is more powerful but more complex.
---

**Semantics**: Semantics tells us how to map syntax to behaviour.

**Formal Semantics**: Formal Semantics gives a precise specification to valid programs so that we can reason about them.

**Implementation**: An implementation is a formal semantic for a language.
But it is too precise to be useful, and does not provide us with
any insight.

**Approaches to Formal Semantics**
- **Operational semantics**: Explains what a program does step by step
    - **Structural Operational Semantics (SOS)**: Define rules to describe how each construct of the language changes the state of the computation.
        - **Small-step semantics**: Describe computation as a sequence of small steps. (rule-base transition rules)
- **Denotational Semantics**: Map the constructs of our language to mathematical objects to reason.
- **Axiomatic Semantics**: Explain by logical assertions, such as pre- and post-conditions, about program states.
    - **Hoare Triple**: {P} C {Q} means if pre-condition P holds before executing command C, then post-condition Q will hold after executing C.
        - **Weakest Precondition**: wp(c, Q) is least restrictive condition that guarantees that post-condition Q holds after executing C.
            - $∀P : \{P\}c\{Q\}$ iff $P → R$ where $R = wp(c, Q)$

**IMP Language**: Imperative Language given by the following grammar:

$S ::= x := a$ | skip | $S_0; S_1$ | if $b$ then $S_0$ else $S_1$ | while $b$ do $S$

**Evaluation Function** $(\llbracket \cdot \rrbracket_σ)$  : shows **how a statement or expression changes the state**. It’s *partial* — meaning it might not give an answer if the program never finishes (like an infinite loop). $\llbracket x := x + 1 \rrbracket_σ = {x: 6}$

**Structural Operational Semantics (SOS)** explains **how each small part of a program runs**, using *rules*.

**Assignment**: $(x := a, σ) → σ[x ↦ v]$ It means: “After running `x := a`, the new state is the old one but with x updated to the value of a.” like $x := 3 + 2$, with $σ = \{\}$ $→ σ[x ↦ 5] = {x: 5}$

**Skip**: $(skip, σ) → σ$ Doing `skip` means *do nothing*, the state stays the same. 

**Sequence**: $(S₀; S₁, σ) → (S₁, σ')$ This means: run the first statement `S₀`, then continue with `S₁`.

**If statement** If you have `if (x > 0) then y := 1 else y := 2 `and $σ = {x: 5}, →$condition true $→$ run `y := 1`.

$$(if\ b\ then\ S₀\ else\ S₁, σ) → (S₀, σ) \text{ if } \llbracket b \rrbracket_σ = true$$

$$(if\ b\ then\ S₀\ else\ S₁, σ) → (S₁, σ) \text{ if } \llbracket b \rrbracket_σ = false$$

**While loop** $ (while\ b\ do\ S, σ) → (if\ b\ then\ S; (while\ b\ do\ S)\ else\ skip, σ) $

**β-reduction** $(λx. M) N → M[N/x]$ Means: replace every `x` in `M` with `N`. Example: $(λx. x + 1) 5 → 5 + 1 = 6$

**α-conversion** $λx. M → λy. M[y/x]$ Means: you can rename variable names (to avoid confusion). Example: $λx. x + 1 → λy. y + 1$ Same meaning, just different variable name.

---
**Booleans** ` True  = λx.λy. x ` `False = λx.λy. y` **Logical NOT** `¬ = λx. x False True` **Logical OR** `∨ = λx.λy. x True y`

**Church Numerals** `0 = λs.λz. z  → apply s 0 times` `1 = λs.λz. s(z)       → apply s once` `2 = λs.λz. s(s(z))    → apply s twice`

**Free and Bound Variables** `(λy. z y x) (λx. x y) y and x is bounded due to λ but z is free in both expressions. ` Rules:
1- `FV(x) = {x}` 2- `FV(M N) = FV(M) ∪ FV(N)` 3- `FV(λx. N) = FV(N) \ {x}`

**Naive Substitution (the problem)** If we substitute variables **without care**, we can accidentally **capture free variables**. So first we rename variables to avoid this.

**Currying**: Turning a function that takes **many arguments** into a chain of functions that each take **one** argument.
`f 2 3 → (λx. λy. x + y) 2 3` -> `→ f = λx. (λy. x + y)` -> `→ (λy. 2 + y) 3` -> `→ 5`

**Confluence** A system is **confluent** if the order of applying rules doesn’t matter — you always get the same result.
**Example:** `M = (λx. x) ((λy. y) z)` 1. Reduce the **inner** one first: ` (λx. x) ((λy. y) z) → (λx. x) z → z ` 2. Reduce the **outer** one first: `(λx. x) ((λy. y) z) → ((λy. y) z) → z `

**Confluence** A system is **confluent** if the order of applying rules doesn’t matter — you always get the same result.
**Example:** `M = (λx. x) ((λy. y) z)` 1. Reduce the **inner** one first: ` (λx. x) ((λy. y) z) → (λx. x) z → z ` 2. Reduce the **outer** one first: `(λx. x) ((λy. y) z) → ((λy. y) z) → z `

## **β-redex and Normal Form**

- A **β-redex** is a reducible λ-expression of the form `(λx. M) O`, which can be simplified by substituting `O` for `x` in `M`.
- A **normal form** is an expression with **no more β-redexes** — it can’t be reduced further.

**Example:** `(λx. x + 1) 5  →  5 + 1  →  6 ` Here, `(λx. x + 1) 5` is a β-redex, and `6` is the normal form.

**Evaluation Strategies** We can reduce β-redexes in **different ways** (evaluation strategies).
- **Call-by-value**: We **first evaluate the argument** to a value before applying the function.
  - `(λx. x + 1) ((λy. y + 2) 3)` 1. Evaluate `((λy. y + 2) 3)` → `5` 2. Then apply `(λx. x + 1)` to `5` → `6`
- **Call-by-name** : We **don’t evaluate the argument first**, we *substitute* it directly into the function.
  - `(λx. x + 1) ((λy. y + 2) 3)` 1. Substitute directly: `((λy. y + 2) 3) + 1` 2. Then evaluate `((λy. y + 2) 3)` → `5` 3. Finally, `5 + 1` → `6`
- **Call-by-need (used in Haskell)**: It still avoids unnecessary computation, but **if** a value is needed later, it is computed **once** and reused.

**Functional Programming matters**: Because of **confluence** and **normal form**, FP languages: 1- Always give the same result for the same input 2- Can safely reorder computations, 3- Are easy to test and reason about mathematically.

**Referential transparency**: A program is **referentially transparent** if you can replace an expression with its value without changing the program's behavior. $( \lambda x x)z$ and $(\lambda y \lambda x x)a z$ are referentially transparent because both evaluate to `z`.

---

**Tail Recursion** A **tail call** is when the *last thing* a function does before it returns is **call another function** (including itself).

If a function is **tail recursive**, the compiler can optimize it using **Tail Call Optimization (TCO)**. 1- It doesn’t need to keep old function calls in memory. 2- It reuses the same stack frame. 3- So it runs in **constant space** — even for large inputs.

**Parametric Polymorphism**:‌Polymorphism = “many forms.”, You write one **generic** definition instead of many type-specific ones. You write functions or data types that work for **any type** like handling both `int` and `string`.

**The Y-Combinator** A **combinator** is a λ-expression with **no free variables**.  The **Y-combinator** is for defining recursion in λ-calculus. It is defined as: `Y ≡ λf. (λx. f (x x)) (λx. f (x x)) `It’s also called the **fixpoint combinator** allows **recursion** in λ-calculus. When we apply it to some function M, we get: `Y M = (λf. (λx. f (x x)) (λx. f (x x))) M` Now we do β-reduction (substitute M for f): `→ (λx. M (x x)) (λx. M (x x))`

**Simply Typed Lambda Calculus** (λ→) `e ::= x | e1 e2 | n | e1 + e2 | λx : τ. e` `v ::= λx : τ. e | n` `τ ::= int | τ → τ`

**Type context (Γ)** $Γ = { x : int, y : bool }$ Notation: $Γ ⊢ e : τ$ “Under context Γ, expression e has type τ.”

**Typing Rules**
- **T-VAR** If variable `x` has type `τ` in Γ, then `x` has type `τ`.
```
Γ(x) = τ (Type of x in context Γ)
------------  = τ (Type of x we found)
Γ ⊢ x : τ (Variable x has type τ)
```
- **T-INT** Numbers have type `int`. 'n : int'

- **T-APP (Function Application)** : If `e1` is a function from `τ` → `τ'` and `e2` has type `τ`, then applying `e1` to `e2` gives a result of type `τ'`.
```
Γ ⊢ e1 : τ → τ'      Γ ⊢ e2 : τ
--------------------------------
Γ ⊢ e1 e2 : τ'
```

- **T-ABS (Function Definition)** : If assuming `x : τ` lets us show `e : τ'`, then `λx : τ. e` is a function of type `τ → τ'`. 

```
Γ, x : τ ⊢ e : τ'
----------------------
Γ ⊢ λx : τ. e : τ → τ'
```
- **T-ADD**
```
Γ ⊢ e1 : int     Γ ⊢ e2 : int
------------------------------
Γ ⊢ e1 + e2 : int
```
**Type Soundness**: Well-typed programs **don’t get stuck** — they keep evaluating until they reach a value.

$$\text{If } ⊢ e : τ \text{ and } e → e', \text{ then either } e' \text{ is a value or there exists } e'' \text{ such that } e' → e''.$$

If an expression `e` has a type `τ`, and it reduces (takes one computation step) to another expression `e′`,
then: 1- Either `e′` is already a final value (like `5` or `λx : int. x + 1`), 2- Or you can keep reducing it (i.e. it still has valid next steps).

**Normalization**

$$\text{If } ⊢ e : τ, \text{ then there exists a value } v \text{ such that } e →* v.$$

If an expression `e` has a type, then you can always reduce it step by step (→*) until you reach a final **value** `v`.

In simple words: Every well-typed expression **finishes** — it does not loop forever.