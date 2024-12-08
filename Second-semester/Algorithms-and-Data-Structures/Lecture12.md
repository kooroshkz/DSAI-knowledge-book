## Hash Tables
A hash table is a data structure that implements an associative array, a structure that can map keys to values.

It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
##### Example:
Assume student IDs and names:
- Alice: 12345
- Bob: 67890
- Carol: 11223
- Dave: 56789

Number of buckets: 10

Calculate Hash Codes:

- hash(12345) = 12345 % 10 = 5
- hash(67890) = 67890 % 10 = 0
- hash(11223) = 11223 % 10 = 3
- hash(56789) = 56789 % 10 = 9

Insert into Buckets:

- Bucket 0: [Bob (67890)]
- Bucket 3: [Carol (11223)]
- Bucket 5: [Alice (12345)]
- Bucket 9: [Dave (56789)]

### Set ADT (Abstract Data Type):
Common operations include 
- add(x)
- contains(x)
- size()
| Structure            | contains(x) | add(x)     | Notes                                        |
|----------------------|-------------|------------|----------------------------------------------|
| ListSet              | Θ(N)        | Θ(N)       |                                              |
| BST                  | Θ(N)        | Θ(N)       | Random trees are Θ(log N).                   |
| Self-balancing BST   | Θ(log N)    | Θ(log N)   | Special BSTs that are guaranteed to be short. |

### Python's Hash Tables

- Implementation: Python's set and dict use hash tables for efficient data storage and retrieval.
- hash Method: Objects define their hash function using the __hash__ method to generate hash codes.
- String Hashing: Includes salting to prevent attacks that exploit hash functions.