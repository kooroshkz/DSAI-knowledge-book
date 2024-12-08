## Dynamic Programming ≈ Recursive Algorithm + Memoization
A technique for solving problems with overlapping subproblems having two approaches:
- **Top-down approach**: In this approach, problems are broken down into smaller parts, which help users identify what needs to be done.
- **Bottom-up approach**: Often implies building a solution iteratively or dynamically, starting from the base cases and working upwards to the final solution.
### Bottom-Up Fibonacci


**Algorithm**:
1. Start with the base cases: $ F(0) = 0 $ and $ F(1) = 1 $.
2. Use a loop to calculate each Fibonacci number from $ F(2) $ to $ F(n) $.
3. Store only the last two Fibonacci numbers at each step to save space.

### Differences Between Bottom-Up Fibonacci and Recursive Fibonacci

1. **Efficiency**:
   - **Recursive Fibonacci**: Has an exponential time complexity $ O(2^n) $ due to repeated calculations of the same Fibonacci numbers.
   - **Bottom-Up Fibonacci**: Has a linear time complexity $ O(n) $ as it computes each Fibonacci number once and uses constant space $ O(1) $.

2. **Space Complexity**:
   - **Recursive Fibonacci**: Uses stack space proportional to $ n $ due to the depth of the recursion, resulting in $ O(n) $ space complexity.
   - **Bottom-Up Fibonacci**: Uses only a constant amount of space $ O(1) $ by storing the last two computed Fibonacci numbers.

3. **Implementation**:
   - **Recursive Fibonacci**:
     ```python
     def fibonacci_recursive(n):
         if n <= 1:
             return n
         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
     ```
   - **Bottom-Up Fibonacci**:
     ```python
     def fibonacci_bottom_up(n):
         if n == 0:
             return 0
         elif n == 1:
             return 1
         
         a, b = 0, 1
         for i in range(2, n + 1):
             a, b = b, a + b
         return b
     ```

4. **Calculation Process**:
   - **Recursive Fibonacci**: Repeatedly breaks down the problem into smaller subproblems and uses a top-down approach.
   - **Bottom-Up Fibonacci**: Builds the solution from the smallest subproblems up to the desired Fibonacci number, using an iterative approach.