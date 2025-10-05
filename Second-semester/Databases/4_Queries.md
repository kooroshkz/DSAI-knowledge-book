## SQL queries

Query : = Request to a database
### SQL query structure
```sql
SELECT [DISTINCT] target-list FROM relation-list WHERE qualification
```
#### Querying Multiple Relations

```sql
SELECT S.name, E.cid
FROM Students S, Enrolled E
WHERE S.sid=E.sid AND E.grade="B";
```
#### Range variables

Aliases for easier calling of table
    
Example: 
```sql
SELECT S.sname FROM Sailors S, Reserves R WHERE S.sid=R.sid AND R.bid=103;
```
Or by using **AS**
```sql
SELECT S.age, S.age/10 AS age1, 12*S.age AS months
FROM Sailors S
WHERE S.sname = "dustin";
```
## String matching using LIKE

```sql
SELECT S.sname, S.age
FROM Sailors S
WHERE S.sname LIKE "B_%B";
```

- ” ” stands for any one character and ”%” stands for 0 or more arbitrary characters.
- So ”BAOBAB” would qualify, and also ”BOB”, but not ”BB” or ”BEN”
<hr>
### DISTINCT

The "DISTINCT" keyword in the SQL query ensures that only unique values are returned.

```sql
SELECT DISTINCT R.sid
FROM Boats B,Reserves R
WHERE R.bid=B.bid AND
(B.color="red" OR
B.color="green");
```
### UNION
 combine the results of two or more SELECT statements into a single result set.

 ```sql
 SELECT student_id, name, age FROM Students_A
UNION
SELECT student_id, name, age FROM Students_B;
```

**UNION ALL** : Ignore and will show duplicates
### INNER JOIN

```sql
SELECT Students.name, Grades.subject, Grades.grade
FROM Students
INNER JOIN Grades ON Students.student_id = Grades.student_id;
```


#### INNER JOIN VS UNION ALL
INNER JOIN is used to combine related rows from different tables based on a common column, while UNION ALL is used to combine the results of multiple queries into a single result set, including all rows from each query, regardless of duplicates.
### INTERSECT

 INTERSECT operator to find the intersection of two result sets. It looks for common rows between the two SELECT queries.

 Eg.
```sql
SELECT S.sid
FROM Sailors S, Boats B, Reserves R
WHERE S.sid=R.sid AND R.bid=B.bid AND B.color="red"
INTERSECT
SELECT S.sid
FROM Sailors S, Boats B, Reserves R
WHERE S.sid=R.sid AND R.bid=B.bid AND B.color="green"
```

## Nested Queries
Queries that are embedded within another SQL statement.

```SQL
SELECT S.sname
FROM Sailors S
WHERE S.sid IN (SELECT R.sid
FROM Reserves R
WHERE R.bid=103)
```
##  IN, NOT IN

```sql
SELECT * FROM Employees WHERE Department IN ('HR', 'Finance', 'Marketing');
-- Which the functionality is same as
SELECT * FROM Employees E WHERE E.Department = 'HR' OR E.Department = Finance' OR E.Department = 'Marketing';

SELECT * FROM Students WHERE Grade NOT IN ('A', 'B');
```
### EXISTS, NOT EXISTS

**EXISTS:** This returns rows where the subquery returns one or more rows.

**NOT EXISTS:** This returns rows where the subquery returns no rows.
```sql
SELECT * FROM table1 WHERE EXISTS (SELECT * FROM table2 WHERE table1.id = table2.id);
-- This query selects all rows from table1 where there's at least one row in table2 with the same id.

SELECT * FROM table1 WHERE NOT EXISTS (SELECT * FROM table2 WHERE table1.id = table2.id);
-- This query selects all rows from table1 where there are no rows in table2 with the same id.

```

### ANY

```sql
SELECT *`FROM Sailors S WHERE S.rating > ANY (SELECT S2.rating
FROM Sailors S2 WHERE S2.sname=’Horatio’);
```
<hr>
## Aggregate operators in projection list
```sql
-- Aggregate operators:
-- count
COUNT (*)
COUNT([DISTINCT] A)
-- summation (single
column)
SUM ([DISTINCT] A)
-- averaging (single col)
AVG ([DISTINCT] A)
-- minimum, maximum
(single col)
MAX (A)
MIN (A)
```
```sql
SELECT
  AlbumId,
  ROUND(AVG(Milliseconds) / 60000, 0) AS "Average In Minutes"
FROM
  Tracks
GROUP BY
  AlbumId;
-- AS is optional here
```
<hr>
##  GROUP BY

```sql
SELECT [DISTINCT] target-link FROM relation-list [WHERE qualification] GROUP BY grouping-list

-- Example:
SELECT S.rating, MIN(S.age)
FROM Sailors S WHERE S.age >= 18
GROUP BY S.rating;
```
Use the **HAVING** clause with the GROUP BY clause to
restrict which group-rows are returned in the result set:

```sql
SELECT S.age, MAX(S.rating)
FROM Sailors S
GROUP BY S.age
HAVING COUNT (*) > 1; /* Groups must qualify */
```