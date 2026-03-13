#### Defenses in Application Security

- **Language-Based Safety**
    - **Spatial safety:** No out-of-bounds access (don't read/write outside allocated buffers).
    - **Temporal safety:** No use-after-free or use of uninitialized pointers (don't use memory that’s been freed).
    - **Dangling pointers:** Point to freed or invalid memory → dangerous.
    - **Type safety:** Operations on data must match their type (e.g., treating an integer as a pointer is unsafe).
- **Preventive Measures**
    - **Non-Executable Memory**
        - Mark memory areas (like stack/heap) as non-executable to prevent running injected code.
        - Prevents running injected malicious code.
    - **Address Space Layout Randomization (ASLR)**
        - Randomly rearranges memory locations of key program areas (like stack, heap, libraries).
- **Detective Measures**
  - **Stack Canaries**
    - Special values placed before return addresses on the stack to detect buffer overflows.
    - If a buffer overflow overwrites this value, the program detects it and aborts.
    - Types:
      - Terminator canaries (special chars)
      - Random canaries (random secret values)
      - XOR canaries (random canaries XORed with return address)
  - **Control Flow Integrity (CFI)**
    - Program’s control flow (which functions jump where) is checked against expected paths and stops if unexpected jumps occur.
    - A Control Flow Graph (CFG) is built during compile time.
    - **Can stop:**
      - Code injection attacks (like buffer overflows that redirect execution)
      - Redirecting control flow to malicious code (like return-to-libc attacks)
    - **Cannot stop:**
      - Attacks that follow allowed paths but misuse them (mimicry attacks)
      - Data corruption or data leaks (like Heartbleed)
      - Control flow changes based on bad data (CFI only checks function jumps, not data flow)
    - **In-line Reference Monitor (IRM):** This is extra code added to check if the next jump is allowed by looking at labels attached to possible jump targets.

| Attack Type                 | What it Does                      | Defense/Prevention               |
| --------------------------- | --------------------------------- | -------------------------------- |
| Buffer Overflow             | Overwrites memory                 | Bounds checks, stack canaries    |
| Heap Overflow               | Overflow in heap memory           | Bounds checks, safe memory alloc |
| Format String Vulnerability | Manipulates format specifiers     | Use format strings properly      |
| Integer Overflow            | Wrap-around number errors         | Check integer sizes              |
| TOCTOU Race Condition       | Time gap exploitation in file use | Atomic operations, safer code    |
| Return-to-libc              | Jump to existing code             | ASLR                             |
| Code Injection              | Inject malicious code             | Non-executable memory            |
| Control Flow Hijack         | Jump to unexpected code           | CFI                              |