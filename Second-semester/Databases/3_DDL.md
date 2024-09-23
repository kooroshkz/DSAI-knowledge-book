## SQL-DDL
### Data types

| Data Type | Description |
|-----------|-------------|
| INTEGER   | Integer values |
| REAL      | Floating-point values |
| TEXT      | Textual data |
| BLOB      | Binary data (Large object, e.g. picture) |
| NULL      | Null values |
### Head up

While we want to remove existing table and create new one, we can use the following command:

```sql
DROP TABLE IF EXISTS table_name;
CREATE TABLE table_name ( ... );
```
<hr>
### Create table

```sql
CREATE TABLE Students (
    sid INTEGER PRIMARY KEY,
    name TEXT,
    login CHAR(9),
    age INTEGER,
    gpa REAL
);

##### Assign unique items and more than one Primary Key to a table

```sql
CREATE TABLE Clients (postcode CHAR(5), name TEXT,
login TEXT, birthday TEXT, PRIMARY KEY(name,
postcode), UNIQUE(login));
```


<hr>
### Altering a table:

- Add column firstYear to table:
```sql
ALTER TABLE Students ADD COLUMN firstYear INTEGER;
```
- Drop column:
```sql
ALTER TABLE Students DROP COLUMN firstYear;
```
<hr>
<br>

### Update items

```sql
UPDATE table_name SET id = 20 WHERE name="Koorosh";
```
<hr>
### Inserting and deleting rows

#### Insert a row in table Students:

```sql
INSERT INTO Students (sid, name, login, age, gpa)
VALUES (53688, 'Smith', 'smith@ee.nl', 18, 3.2);
```
Delete one or many rows in table Students:
```sql
DELETE FROM Students AS S WHERE S.name = "Smith";
```
Note: Key attribute will specify single row only.
<hr>
### Select

```sql
SELECT * FROM Students S
WHERE S.age = 18;
```
<hr>
### Join operation
Students
| sid   | name  | login        | age | gpa |
|-------|-------|--------------|-----|-----|
| 53666 | Jones | jon@cc.nl    | 18  | 3.4 |
| 53688 | Smith | smith@ee.nl  | 18  | 3.2 |

Enrolled
| sid   | course | grade |
|-------|--------|-------|
| 53666 | HisT   | B     |
| 53688 | XTz    | A     |

```sql
SELECT S.name, E.course
FROM Students S, Enrolled E
WHERE S.sid = E.sid AND E.grade = 'A';
```Smith|XTz```
<hr>
# Translation
### Translating a relationship set without constraints

```sql
CREATE TABLE WorksIn(
ssn CHAR(8), did INTEGER, since DATE,
PRIMARY KEY (ssn, did),
FOREIGN KEY (ssn) REFERENCES Employees(ssn),
FOREIGN KEY (did) REFERENCES Departments(did))
```
** Assume relation is WorksIN with since attribute, Employees table have Attribute ssn and other attributes like Departments have "did".
### Translating a relationship set with simple key constraint
In this scenario, we have a relationship set with a simple key constraint. The source table, represented by an arrow in the ERD, will have its primary key used as the primary key for the final table.

Unlike the previous example, where we had two primary keys, this time we only have one primary key from the source table.
### Translating a combined key and total participation constraint

- The primary key in the source will become the main primary key.
- The primary key in the destination will be defined as NOT NULL in the table creation argument.
```sql
    ssn CHAR(11) NOT NULL
```
- The primary key in the destination will become a foreign key."

### Weak entity sets
- Primary key will be tuple of both tables primary keys
- Destination table primary key will be define as NOT NULL
- Destination table primary key will be define as Foreign Key with ON DELETE CASCADE
```sql
    FOREIGN KEY (ssn) REFERENCES Employees(ssn) ON DELETE CASCADE)
```
### Total participation without key constraint

We may capture total participation by using NOT NUL
<hr>

## Example inheritance with E/R method
```sql
CREATE TABLE Boats (
    bid INTEGER,
    length REAL,
    height REAL,
    PRIMARY KEY (bid)
);

CREATE TABLE Sloeps (
    bid INTEGER,
    maxspeed REAL,
    priceperday REAL,
    PRIMARY KEY (bid),
    FOREIGN KEY (bid) REFERENCES Boats ON DELETE CASCADE
);

CREATE TABLE Kajaks (
    bid INTEGER,
    PricePerHour REAL,
    color VARCHAR,
    PRIMARY KEY (bid),
    FOREIGN KEY (bid) REFERENCES Boats ON DELETE CASCADE
);
```

ON DELETE CASCADE is mandatory.
<hr>

### Relation
- Instance
    - n of rows = cardinality
- Schema
    - n of columns = arity (degree or argument)
        - Binary relation
        - N-ary relation

### Collections

|Name|Order|Repetition|
|--|--|--|
|Set|$\times$|$\times$|
|Bags|$\times$|$\checkmark$|