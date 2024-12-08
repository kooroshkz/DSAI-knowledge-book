## Graph and Tree

### Binary trees
- Inorder: LNR
- Preorder: NLR
- Postorder: LRN



### Countring pre-order tree traversal nodes
```python
def node_count(root):
    if root is None:
        return 0
    else:
        return 1 + node_count(root.left) + node_count(root.right)
count = node_count(root)
```

Complete binary tree: Only on the bottom level, the right-most nodes may be empty.
```md
    7
   / \
  9   3
 / \ / \
8  4 5 
```

### Binary search tree
A binary tree where for each node holds that its value is greater than all values in the left subtree, and smaller than all values in the right subtree.
    
    example :
```md
       5
      / \
     3   7
    / \ / \ 
    1 4 6 8
```
#### Remove in binary search tree
<img src="../../Files/second-semester/dsa/2.jpg" style="height: 200px">

swap with greatest smaller value
## Binary Tree Height and Node Range

The table below shows the relationship between the height $h$ and the minimum ($n_{\text{min}}$) and maximum ($n_{\text{max}}$) number of nodes in a binary tree:

| h | nmin | nmax |
|---|------|------|
| 0 |  1   |  1   |
| 1 |  2   |  3   |
| 2 |  3   |  7   |
| 3 |  4   |  15  |
| 4 |  5   |  31  |

The maximum number of nodes $n_{\text{max}}$ can be calculated using the formula: $n_{\text{max}} = 2^{h+1} - 1$.

## Height of Binary Tree and Logarithm

For a binary tree with height $h$ and $n$ nodes, the following equation holds:

$h \leq \lceil \log_2(n + 1) \rceil - 1$
## Heap

A heap is a special tree-based data structure that satisfies the heap property. There are two types of heaps:

- Max-Heap: In a max-heap, for any given node I, the value of I is greater than or equal to the values of its children. The highest value is at the root.

- Min-Heap: In a min-heap, for any given node I, the value of I is less than or equal to the values of its children. The lowest value is at the root.

Key Characteristics:

- Heaps are commonly implemented as binary trees.
- They are used to implement priority queues.
- The operations insert and extract (remove) are efficient, typically O(log n) due to the tree height.