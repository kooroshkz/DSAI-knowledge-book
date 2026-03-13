## **λ-calculus**

We use **λ-expressions** and **β-reductions** (substitution) to “run” programs.

**Example:**

* Think of `λx. x + 1` as a function `f(x) = x + 1`.
* Applying it: `(λx. x + 1) 4` → `4 + 1 = 5`.

In λ-calculus, you can **build everything** from this simple idea — even `True`, `False`, `if`, `0`, `1`, etc.

## Boolean Operators

Here, we see how to **encode True and False** using λ-functions.

##### **Booleans**

```
True  = λx.λy. x
False = λx.λy. y
```

##### **Logical NOT**

```
¬ = λx. x False True
```
##### **Logical OR**

```
∨ = λx.λy. x True y
```

##### **Church Numerals**

```
0 = λs.λz. z          → apply s 0 times
1 = λs.λz. s(z)       → apply s once
2 = λs.λz. s(s(z))    → apply s twice
3 = λs.λz. s(s(s(z))) → apply s three times
```
- **Successor function (S)**

```
S = λw.λf.λx. f (w f x)
```

This adds **1** to a number.

`S 2 → 3`

That’s because it applies `f` one more time than `2` does.

##### **Variable Names**

λ-calculus doesn’t care about *the name* of the variable — only its *role*.

```
λx. x have same I/O as: λy. y
```
- **α-conversion** — renaming bound variables.

**Rule:**

```
λx. M → λy. M[y/x]
```

means: you can rename `x` to `y` as long as it doesn’t mess up meaning.

##### **Free and Bound Variables**

Some variables are **bound** (used inside a λ), and some are **free** (not tied to any λ).

```
(λy. z y x) (λx. x y) y and x is bounded due to λ but z is free in both expressions.
```

- **Finding Free Variables (FV)**

Rules:

```
FV(x) = {x}
FV(M N) = FV(M) ∪ FV(N)
FV(λx. N) = FV(N) \ {x}
```
---

#### **Naive Substitution (the problem)**

If we substitute variables **without care**, we can accidentally **capture free variables**. So first we rename variables to avoid this.

**Rule:**

```
(λx. M) N → M[N/x]
```

Bad (captures variable):

```
(λx. λy. x) y
```

If we substitute directly:
`λy. y` ← wrong, because the free `y` we plugged in became bound.

Good (rename first):

```
(λx. λw. x) y → λw. y
```

#### **Currying**

> Turning a function that takes **many arguments** into a chain of functions that each take **one** argument.

```
f 2 3 → (λx. λy. x + y) 2 3
→ f = λx. (λy. x + y)
→ (λy. 2 + y) 3
→ 5
```

---

#### Confluence

A system is **confluent** if the order of applying rules doesn’t matter — you always get the same result.

Like

```
M → O
M → P
```
Both are valid but different paths. Confluence means there’s a common expression `Q` such that:

```
O → Q
P → Q
```

**Example:**

```
M = (λx. x) ((λy. y) z)
```

1. Reduce the **inner** one first:

   ```
   (λx. x) ((λy. y) z)
   → (λx. x) z
   → z
   ```

2. Reduce the **outer** one first:

   ```
   (λx. x) ((λy. y) z)
   → ((λy. y) z)
   → z
   ```

---
## **β-redex and Normal Form**

- A **β-redex** is a reducible λ-expression of the form `(λx. M) O`, which can be simplified by substituting `O` for `x` in `M`.
- A **normal form** is an expression with **no more β-redexes** — it can’t be reduced further.

**Example:**

```
(λx. x + 1) 5  →  5 + 1  →  6
```

Here, `(λx. x + 1) 5` is a β-redex, and `6` is the normal form.

---

#### **Evaluation Strategies**

We can reduce β-redexes in **different ways** (evaluation strategies).
- **Call-by-value**: We **first evaluate the argument** to a value before applying the function.
  - `(λx. x + 1) ((λy. y + 2) 3)
    - 1. Evaluate `((λy. y + 2) 3)` → `5`
    - 2. Then apply `(λx. x + 1)` to `5` → `6`
- **Call-by-name** : We **don’t evaluate the argument first**, we *substitute* it directly into the function.
  - `(λx. x + 1) ((λy. y + 2) 3)
    - 1. Substitute directly: `((λy. y + 2) 3) + 1`
    - 2. Then evaluate `((λy. y + 2) 3)` → `5`
    - 3. Finally, `5 + 1` → `6`
- **Call-by-need (used in Haskell)**: It still avoids unnecessary computation, but **if** a value is needed later, it is computed **once** and reused.

---

#### Why Functional Programming matters

Because of **confluence** and **normal form**, FP languages:

* Always give the same result for the same input,
* Can safely reorder computations,
* Are easy to test and reason about mathematically.
---

##### Referential transparency

A program is **referentially transparent** if you can replace an expression with its value without changing the program's behavior.

- $( \lambda x x)z$ and $(\lambda y \lambda x x)a z$ are referentially transparent because both evaluate to `z`.