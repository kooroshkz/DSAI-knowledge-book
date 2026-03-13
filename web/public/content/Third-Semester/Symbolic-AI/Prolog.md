### Quick Guide to Prolog Programming:

#### **Key Concepts in Prolog:**

1. **Facts**: Define simple truths.
   ```prolog
   male(joost).
   parent(joost, sacha).
   ```
2. **Rules**: Define relationships with conditions.
   ```prolog
   brother(X, Y) :- 
       male(X),
       parent(P, X),
       parent(P, Y),
       X \= Y.
   ```

3. **Queries**: Ask Prolog questions.
   ```prolog
   ?- parent(joost, X).
   ```

---

#### **Substitution & Unification**:
- **Unification**: Matches terms in a query with facts/rules.
- **Substitution**: Assigns variables specific values during unification.
  - Example:
    ```prolog
    ?- parent(joost, X).
    X = sacha ;
    X = leon.
    ```

---

#### **Working with Lists**:
- Lists are structured as `[Head | Tail]`.
- Example:
  ```prolog
  append([], X, X).
  append([H|T], Y, [H|Z]) :- append(T, Y, Z).
  ```

---

#### **Assignment-specific Highlights**:

1. **Family Relationships**:
   - Use recursive rules for **ancestor(X, Y)**.
   - Define **brother(X, Y)** and **sister(X, Y)** based on shared parents and gender.

2. **Cousins**:
   ```prolog
   cousin(X, Y) :-
       parent(P1, X),
       parent(P2, Y),
       (brother(P1, P2); sister(P1, P2)),
       X \= Y.
   ```

3. **Family Predicate**:
   ```prolog
   family(X, Y) :- ancestor(X, Y); ancestor(Y, X); (ancestor(Z, X), ancestor(Z, Y)).
   ```

---

#### **Simple Reflexive Agent**:
1. **Environment Representation**:
   - Define locations as `link(X, Y)` facts.
   - Represent the robot and goal:
     ```prolog
     robot(1).
     goal(5).
     ```

2. **Basic Agent Behavior**:
   - **Adjacent**:
     ```prolog
     adjacent(Y) :- link(X, Y), robot(X).
     ```
   - **Move**:
     ```prolog
     move(Y) :- adjacent(Y), retract(robot(_)), assert(robot(Y)).
     ```

3. **Pathfinding**:
   - Use recursion to find paths:
     ```prolog
     path(G, [G]) :- goal(G).
     path(X, [X|Rest]) :- link(X, Z), path(Z, Rest).
     ```

4. **Improved Suggestions**:
   - Suggest next step in path:
     ```prolog
     suggest(Next) :-
         robot(X),
         path([X, Next | _]).
     ```

---

#### **Debugging Tips**:
- Use `trace.` to follow execution.
- Stop queries with `<Ctrl>-C` + `a`.

#### **Submission**:
- Test all predicates with queries before submitting.
- Save files as `family.pl` and `wumpus.pl`.