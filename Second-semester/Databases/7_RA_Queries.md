# Relational Algebra
### Basic Syntax Constraints
Positional vs. named-field notation:
- In positional we call field position number like field1
- In Named-Field Notation we Call the name of the column like "Age"
### Operators
#### Projection $\pi_{a_1,...,a_k}(R)$
Deletes fields (columns) that are not in the projection list and then removes duplicate tuples

$\pi_{name,age}$ returns a relation with only the name and age fields where there is no duplicate tuple
#### Selection $\sigma_{c(a_1,...,a_k)}(R)$
Returns tuples (rows) of the relation instance that satisfy the selection condition.

$\sigma_{name='Jake' \lor age<50}$ returns a relation with only the name and age fields where there is no duplicate tuple
#### Set Operations $ \cup , \cap , \setminus $


### Division in Relational Algebra

The division operation is used to find tuples in one relation that match all tuples in another relation.


Given two relations $A(X, Y)$ and $B(Y)$, the division $A \div B$ will result in a relation $C(X)$ that includes all $X$ values such that for every $y$ in $B$, there exists a tuple $(x, y)$ in $A$.

### Example

Given the table $R$:

| Driver |CarNr |
|--------|------|
| Anton  |AH-378|
| Anna   |TX-345|
| Anna   |AH-378|
| Iska   |AH-378|
| Rui    |AH-378|

$\pi_{\text{CarNr}}(R)$ results in:

| CarNr  |
|--------|
| AH-378 |
| TX-345 |

The division $\pi_{\text{Driver, CarNr}}(R) \div \pi_{\text{CarNr}}(R)$ will result in the set of drivers who have all the car numbers listed in the $\pi_{\text{CarNr}}(R)$.
To perform the division:
- Identify the unique car numbers: AH-378 and TX-345.
- Find drivers who have both of these car numbers.

The result of $\pi_{\text{Driver, CarNr}}(R) \div \pi_{\text{CarNr}}(R)$ is:

| Driver |
|--------|
| Anna   |
#### Cross-product $\times$
$T = R \times S $ Computes all combinations of tuples in R with tuples in S where \circ is Concatenation in $T = \{ a \circ b \mid a \in R \text{ and } b \in S \}$ 
**S =**

| sid | name   | age  |
|-----|--------|------|
| 22  | Dustin | 35   |
| 31  | Lubber | 55.5 |
| 44  | Guppy  | 35   |

**R =**

| sid | bid | day       |
|-----|-----|-----------|
| 22  | 12  | 12/4/2013 |
| 31  | 4   | 8/4/2013  |

**S × R =**

| (sid) | name   | age  | (sid) | bid | day       |
|-------|--------|------|-------|-----|-----------|
| 22    | Dustin | 35   | 22    | 12  | 12/4/2013 |
| 31    | Lubber | 55.5 | 22    | 12  | 12/4/2013 |
| 44    | Guppy  | 35   | 22    | 12  | 12/4/2013 |
| 22    | Dustin | 35   | 31    | 4   | 8/4/2013  |
| 31    | Lubber | 55.5 | 31    | 4   | 8/4/2013  |
| 44    | Guppy  | 35   | 31    | 4   | 8/4/2013  |

#### Renaming $\rho_{{i1} \rightarrow a_1, \ldots, {ik} \rightarrow a_m}(R)$
Rename Column title like in above example $\rho_{{1} \rightarrow StudentID, 4 \rightarrow SecondID}(R)$
#### Theta-Join $ \Join_{c(a_1, \ldots, a_n)}$
Computes all combinations of tuples from R and S
that satisfy the condition.
$R \Join_{c(a_1, \ldots, a_n)} S = \sigma_{{c(a_1, \ldots, a_n)}}(R \times S)$
#### Equi-Join $ \Join_{a_1, \ldots, a_n}$
Computes all combinations of tuples from R and S that satisfy condition $R.a_1 = S.a_1, ..., R.a_k = S.a_k$ and deletes duplicate columns, i.e., keep first occurrence:
$ R  \Join a_1,...,a_k S = \sigma_{R.a_1=S.a_1\land \ldots \land R.a_k=S.a_k}(R \times S) $
#### Natural Join $  \bowtie $

Will join  two relations based on their common attributes (eg. B and C). The result will include columns A, B, C, and D, where B and C are common attributes.
**Note**: In joins we typically need renaming to avoid column name conflicts like:

$S \bowtie_{S.sid > R.sid} R$ should be $T = \rho_{1 \to sid1, 4 \to sid2}(S \bowtie_{S.sid > R.sid} R)$
#### Outer Joins
- Left outer join $R =\Join S$: preserves the tuples on the left, i.e., in R, that would be lost in a natural join.
- Full outer join $R \Join S$: preserves the tuples in both relations $R \Join S = (R \Join S) \cup (R \Join S)$
Note: Non-matched will be Null
#### Division $ X / Y $
For $P$ denoting a relation with fields $x_1, \ldots, x_m, y_1, \ldots, y_k$, and $R$ denoting a relation with fields $y_1, \ldots, y_k$, the division of $P$ by $R$, in symbols $S = P/R$, is a relation with schema $x_1, \ldots, x_m$.

#### Important Equivalences
- Pushing selection : C(B) denote a condition $\sigma_{C(B)}(A \Join B) ≡ A \Join \sigma_{C(B)}(B)$
- Pushing projection : S(B) denote common field identifiers of B and A, and S(A) only attributes of A $\pi_{S(A)}(A \Join B) ≡ π_{S(A)}(A \Join \pi_{S(B)}(B))$
#### Catalan Numbers

The number of join trees for $ m $ relation instances is given by the $ n = m - 1 $ th Catalan number, recursively defined as:

$ C_0 = 1, \quad C_n = \sum_{i=0}^{n-1} C_i C_{n-i-1}, C_n = 1, 1, 2, 5, 14, 42, 132, 429$

<img src="../../Files/second-semester/db/5.jpg" style="height: 400px">
#### Relational vs. Turing Completeness

- SQL is **relationally complete** ( can compute every RA query ), but has additional functionality to RA, e.g., aggregation, grouping.
- **Turing complete**: A programming language works fine on Turing machine (or in simple C language)