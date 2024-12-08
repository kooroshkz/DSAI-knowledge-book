# Python Syntax for DSA
## Data Structures
#### Set {1,3,5}
To add to a set
```python
set.add(x)
```
To remove from a set
```python
set.pop #pop takes no argument and remove from [0]

set.remove(x) # x is a value of specific item
```

#### Adjacency_list
We use dictionary and reach items through for loop with dict.items():
```python
adj_list = {3: {1, 3}, 1: set(), 2: {1, 3}}

n = len(adj_list)
matrix = np.zeros((n,n))

for row , cols in x.items():  #x.items() returns [  () , () ...   ]
    for col in cols:
        matrix[row-1][col-1] = 1
```

## Numpy
Zeros Matrix
```python
np.zeros(  (  m , n  )  )  #grid should be given in tuple format
```
## Binary tree
```python
class Node():
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        
class BinarySearchTree(BinaryTree):
    def ... #Configue and change
    
## Recursive Highest value identifier in Binary tree
```py
def highest_val(root):
    if root is None:
        return None
    return rec_highest_val(root)

def rec_highest_val(node):
    if node is None:
        return -np.inf
    return max(node.val, rec_highest_val(node.left), rec_highest_val(node.right))
```
### Binary Search

```py
def binary_search(arr, target):
    """
    This function performs a binary search on a sorted list.

    :param arr: A sorted list of values.
    :type arr: list
    :param target: The value to search for.
    :type target: int
    :return: The index of the target value if found, otherwise None.
    :rtype: int or None
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Example usage
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value_to_find = 7

result = binary_search(sorted_list, value_to_find)

if result is not None:
    print(f"Value found at index {result}")
else:
    print("Value not found")

```
### GCD
```py
def gcd(a, b):
    """
    This function calculates the greatest common divisor of a and b.
    """
    if b == 0:
        return a
    return gcd(b, a % b)