## Divide and Conquer:

Breaking a problem into smaller subproblems, solving each subproblem independently, and then combining their solutions to solve the original problem. like:
- Merge Sort
- Quick Sort
- Binary Search
### Merge Sort
**Explanation**:
- Merge Sort is a divide-and-conquer algorithm.
- It divides the array into two halves, recursively sorts each half, and then merges the sorted halves to produce the sorted array.

**Example**:
1. Given array: `[38, 27, 43, 3, 9, 82, 10]`
2. Divide into two halves: `[38, 27, 43, 3]` and `[9, 82, 10]`
3. Recursively sort each half:
   - `[38, 27, 43, 3]` -> `[27, 38, 3, 43]` -> `[3, 27, 38, 43]`
   - `[9, 82, 10]` -> `[9, 10, 82]`
4. Merge the sorted halves:
   - `[3, 27, 38, 43]` and `[9, 10, 82]` -> `[3, 9, 10, 27, 38, 43, 82]`

**Time Complexity**:
- $O(n \log n)$

<img src="../../Files/second-semester/dsa/merge.gif" style="height: 400px">
<hr>
### Quick Sort
**Explanation**:
- Quick Sort is a divide-and-conquer algorithm.
- It selects a 'pivot' element, partitions the array around the pivot, and recursively sorts the subarrays.

**Example**:
1. Given array: `[10, 7, 8, 9, 1, 5]`
2. Choose pivot (last element): `5`
3. Partition the array around pivot:
   - `[1, 5, 8, 9, 10, 7]`
4. Recursively sort subarrays:
   - `[1, 5]` and `[8, 9, 10, 7]`
   - `[1, 5]` is already sorted.
   - `[8, 9, 10, 7]` with pivot 7 -> `[1, 5, 7, 8, 9, 10]`

**Time Complexity**:
- **Best Case**: $\Omega(n \log n)$
- **Average Case**: $\theta (n \log n)$
- **Worst Case**: $O(n^2)$ (when pivot selection is poor)

<img src="../../Files/second-semester/dsa/quick.gif" style="height: 400px">
<hr>
### Insertion Sort
**Explanation**:
- Insertion Sort builds the final sorted array one element at a time.
- It works by repeatedly taking the next element and inserting it into the correct position in the already sorted part of the array.

**Example**:
1. Given array: `[12, 11, 13, 5, 6]`
2. Start with the first element: `[12]`
3. Insert 11: `[11, 12]`
4. Insert 13: `[11, 12, 13]`
5. Insert 5: `[5, 11, 12, 13]`
6. Insert 6: `[5, 6, 11, 12, 13]`

**Time Complexity**:
- **Best Case**: $O(n)$ (when the array is already sorted)
- **Average Case**: $O(n^2)$
- **Worst Case**: $O(n^2)$

These explanations and examples should help you understand the mechanics and efficiencies of each sorting algorithm.
<img src="../../Files/second-semester/dsa/insertion.gif" style="height: 400px">
<hr>

### Selection sort
Time Complexity: $O(n^2)$

<img src="../../Files/second-semester/dsa/ss.gif" style="height: 400px">