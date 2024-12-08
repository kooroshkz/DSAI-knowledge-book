## GCD Calculation Methods $gcd(m,n)$
### Euclid's algorithm:

```python
def euclid(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m
```
### Algorithm 2

1. **Step 1:** Determine min(m,n) assign this value to t
2. **Step 2:** Divide m by t. If the remainder is 0, go to Step 3; Otherwise, go to Step 4
3. **Step 3:** Divide n by t. If the remainder is 0, then the gcd is t, so return t and terminate; otherwise go to step 4
4. **Step 4:** Decrease t with 1 and go to step 2

- Note: This algorithm fails if either m or n is zero. Legal input is: m ≠ 0 and n ≠ 0.

### Method 3

- The following algorithm determines the greatest common divisor by decomposing m and n into their prime factors. The gcd is the product of the common factors.
  
- **Example:** 
  - For 60 = 2^2 * 3 * 5 and 24 = 2^3 * 3,
  - gcd(60, 24) = 2^2 * 3 = 12.

1. **Step 1:** Determine the prime factors of m
2. **Step 2:** Determine the prime factors of n
3. **Step 3:** Determine the common prime factors
4. **Step 4:** Calculate the product of these common prime factors and return this value
<hr>
# Data Structures

## Linear Data Structure:

| Array | List |
|-------|------|
| Fixed-size | Dynamic size |
| Contiguous memory storage | Elements may not be contiguous |
| Access by index | Sequential access, slower for random access |

## Various Types of Lists

- **Array**
  - 345   0   871   1   ...

- **Singly Linked List** (not often used in Python)
  - → 345 → 871 → ... → 692 → null

- **Doubly Linked List** (not often used in Python)
  - → null 345 ←→ 871 ←→ ... →← 692 null ←→

Differences in how items can be accessed, stored, or removed from a list.


## Special lists:

| Queue | Stack | Priority Queue |
|-------|-------|----------------|
| FIFO | LIFO | abstract priority based data type |
| **Operations:** | **Operations:** | higher priorities elements are dequeued before elements with lower priorities |
| - enqueue : adding an element to the back | - push : adding an element to the top | |
| - dequeue : removing an element from the front | - pop : removing an element from the top | |
| line of people waiting for a bus | plates | heaps or arrays |

In Queue Enqueue means insert to begining and Dequeue means pop from end
