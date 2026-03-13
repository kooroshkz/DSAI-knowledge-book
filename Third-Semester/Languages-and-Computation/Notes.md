### Commons:

- **L = { aⁿbⁿ | n ≥ 0 }**.

```
S → aSb | ε
```

- **L = { aⁿbⁿ mix positions of a's and b's | n ≥ 0 }** 

```
S → aSb | bSa | SS | ε
```

- all even-length palindromes over {a, b}

```
S → aSa | bSb | ε
```
- all palindromes 

```
S → aSa | bSb | a | b | ε
```

- L = { aⁱbʲ | i, j ≥ 0 }** 

```
S → aS | T
T → bT | ε
```
-  **balanced parentheses** over `(` and `)`.

```
S → SS | (S) | ε
```

- **L = { aⁱbʲcᵏ | i = j }** 

```
S → AB
A → aAb | ε
B → cB | ε
```
- **L = { aⁿbᵐaⁿ | n, m ≥ 0 }** 

```
S → aSa | B
B → bB | ε
```

- **strings over {a, b} with equal numbers of a’s and b’s** 

```
S → aSbS | bSaS | SS | ε
```