# Normal Forms
### Normalization
process of splitting tables into single dependency tables
## Functional dependencies

| Course       | Professor | Employer |
|--------------|-----------|----------|
| Programming  | Kosters   | LIACS    |
| AI           | Kosters   | LIACS    |
| Algebra      | Lukina    | Math     |
| Logic        | Basold    | LIACS    |
| Representation | Lukina  | Math     |

transitive functional dependency (course transitively determines employer) (employer depends on professor, depends on course)

**Determinant** determines values of other attributes in tuple like on above example:

C -> E; P->E

In general K determines A if and only if each K value is associated with precisely one A value


Key -> Attributes: where key and Attributes is the first letter of column name
Key determines Attributes
### Functional Decomposition
A decomposition of R replaces R by two or more relations,
such that each relation contains a subset, and together they
include all attributes of R

For {ABCD}, {AB, BCD, CD} is a decomposition, {AB, BC} is not
### Super key:
- Attributes that uniquely identify a tuple (Attributes that all other attributes functionally depend on)

| ssn     | emp_id | name    | email            |
|---------|--------|---------|------------------|
| 102438  | 80     | Kosters | kosters@liacs.nl |
| 802345  | 23     | Lukina  | lukina@mi.nl     |
| 345328  | 43     | Basold  | basold@liacs.nl  |
| 556789  | 42     | Aarts   | aarts@phys.nl    |

Super keys
- { ssn }
- { emp_id }
- { email }
- { ssn, emp_id }
- { ssn, name }
- { ssn, email }
- { emp_id, email }
- { emp_id, name, email }
- { ssn, emp_id, name, email }
- …

### Minimal key:
- Smallest subset of super keys

### Candidate key:
- Minimal super key (see above)

- (RHS rule): If an attribute never occurs on the right hand
side of an FD, then it must belong to every key of the FD
- (LHS rule): If an attribute never occurs on the left hand
side of an FD, but occurs on at least one right hand side
of an FD, then it must not belong to any key

### Primary key:
- The candidate key chosen by the DBA for a table. Others are alternative keys

Axioms for FD
- Armstrong’s Axioms for FD:
  - reflexivity: For R, If Y is a subset of X, then X $\to$ Y
  - augmentation: For R, If X $\to$ Y, then XZ $\to$ YZ
  - transitivity: For R, If X $\to$ Y and Y $\to$ Z, then X $\to$ Z
- derived:
  - union: If X $\to$ Y and X $\to$ Z, then X $\to$ YZ
  - decomposition: If X $\to$ YZ, then X $\to$ Y and X $\to$ Z

# Normalization

## Normal Forms
- 1NF: No multivalued attributes
    - "Adam, UCLA" should be in seprated columns

- 2NF: 1NF +  all non-prime attributes must be fully dependent on the entire primary key.
    - For table COURSES " $ \underline{\text{course}} $,$ \underline{\text{year}} $, professor, book, employer"
        - (course, year) -> book
        - (course, year) -> professor -> employer

- 3NF: 2NF + No non-prime attribute of R is transitively dependent on the primary key.
    - For table COURSES " $ \underline{\text{course}} $,$ \underline{\text{year}} $, professor, book, employer"
        - (course, year) -> professor
        - professor -> employer
        - (course, year) -> employer (Transitive)
    - So it should be:
        - " $ \underline{\text{course}} $,$ \underline{\text{year}} $, professor, book "
        - " $ \underline{\text{professor}} $, employer"

- BCNF: 3NF + every determinant is a candidate key
    - Consider a table ENROLLMENT: $ \underline{\text{student\_id}}, \underline{\text{course}}, \text{instructor}, \text{grade} $
        - (student_id, course) -> instructor
        - instructor -> course (Not in BCNF since instructor is not a candidate key)
    - To convert to BCNF:
        - Decompose into:
            - $ \underline{\text{student\_id}}, \underline{\text{course}}, \text{grade} $
            - $ \underline{\text{instructor}}, \underline{\text{course}} $

** Transitively dependent: when a column is dependent to a non primary key