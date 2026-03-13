## 1. Introduction to Assembly

* **C programs are compiled** into binary machine code that the CPU executes.
* **Assembly language** is a human-readable form very close to machine code, using labels instead of raw addresses.
* Different CPUs use different assembly languages (called dialects).
* This workshop focuses on **x86-64 assembly**, common in most personal computers.
* Understanding assembly helps you know what happens when high-level programs run and is key for understanding low-level cybersecurity attacks.
* Use **[https://godbolt.org/](https://godbolt.org/)** to explore assembly generated from C code interactively.
* You don’t need to write assembly yourself but understand it.

---

## 2. Registers

* Registers are tiny, super-fast storage areas inside the CPU (nanoseconds speed).
* On x86-64, there are **16 general-purpose registers** each storing **64 bits (8 bytes)**.
* Registers are named historically:

  * First 8: `rax`, `rbx`, `rcx`, `rdx`, `rsi`, `rdi`, `rsp`, `rbp`.
  * These can be accessed partially:

    * Full 64-bit: e.g., `rax`
    * Lower 32-bit: `eax` (replaces `r` with `e`)
    * Lower 16-bit: `ax` (remove `r` and `e`)
    * Lower 8-bit or second 8-bit parts exist (like `al` and `ah`), but not covered here.
  * Next 8 registers: `r8` to `r15` with variants like `r8d` (32-bit), `r8w` (16-bit), `r8b` (8-bit).

---

## 2.1 Stack Registers

* The **stack** stores function local variables.
* Two special registers manage the stack:

  * **`rsp` (Stack Pointer):** Points to the top of the stack (next free space).
  * **`rbp` (Base Pointer):** Points to the start of the current function’s stack frame.
* `rsp` moves as we push/pop data; `rbp` stays fixed to reference variables in the current function.

---

## 2.2 Our First Program in Assembly

* Simple C program adds two numbers:

```c
void main() {
    int num1 = 1;
    int num2 = 2;
    int result = num1 + num2;
}
```

* Corresponding assembly steps:

  * **Set up the stack:**

    * `push rbp` saves old base pointer.
    * `mov rbp, rsp` sets base pointer to current stack top.
  * **Store variables:**

    * `mov DWORD PTR [rbp-4], 1` stores `num1` at `rbp - 4` (stack grows downward).
    * `mov DWORD PTR [rbp-8], 2` stores `num2` at `rbp - 8`.
  * **Load variables into registers:**

    * `mov edx, DWORD PTR [rbp-4]` loads `num1` into `edx` (32-bit register).
    * `mov eax, DWORD PTR [rbp-8]` loads `num2` into `eax`.
  * **Add:**

    * `add eax, edx` adds `edx` to `eax`, result in `eax`.
  * **Store result back:**

    * `mov DWORD PTR [rbp-12], eax` stores result at `rbp - 12`.
  * **Cleanup:**

    * `pop rbp` restores old base pointer.
    * `ret` returns from function.

* Notes:

  * `DWORD PTR` means 4 bytes (size of int).
  * Stack addresses use `[rbp - offset]` since stack grows down.
  * Registers are used for fast computation.

---

## 3. Calling Functions & Calling Conventions

* Assembly functions are placed one after another.
* Calling a function means jumping to its address.
* **Passing parameters:** Must follow system-specific rules called **calling conventions**.
* Example conventions:

  * On Windows: first argument in `rcx`.
  * On Linux: first argument in `rdi`.
* Registers can be used by functions, so conventions define who saves/restores what to avoid losing data.
* Example C program with function call:

```c
int add(int a, int b) {
    return a + b;
}
void main() {
    int num1 = 1;
    int num2 = 2;
    printf("%d plus %d is %d\n", num1, num2, add(num1, num2));
}
```

* Assembly steps for calling `add`:

  * Prepare stack frame (`push rbp`, `mov rbp, rsp`).
  * Move arguments into registers (`rdi` = `num1`, `rsi` = `num2` for Linux).
  * Call `add` (`call add`), which:

    * Saves caller’s `rbp`.
    * Moves arguments to local variables.
    * Adds values and returns result in `eax`.
    * Restores `rbp` and returns.
  * `main` then calls `printf` with the format string and values.

---

## 4. Arrays and the Heap in Assembly

* Example C code:

```c
void main() {
    int* nums = (int*)malloc(3 * sizeof(int));
    nums[0] = 1;
    nums[1] = 2;
    printf("The array is at %p\n", nums);
    printf("The second number is %d\n", nums[1]);
    free(nums);
}
```

* Assembly details:

  * Call `malloc` with `edi` = size (e.g., 12 bytes).
  * `malloc` returns pointer in `rax`.
  * Store values at `[rax]` and `[rax + 4]` (each int = 4 bytes).
  * Call `printf` to print the pointer and a value.
  * Call `free` to release memory.
* Arrays in C are pointers to memory addresses.
* Access memory via pointers by dereferencing (`[rax]` means contents at address in `rax`).

---

## 5. Compiler Optimizations

* Compilers can optimize code to make it smaller and faster with flags like `-O1`, `-O2`, `-O3`.
* Example:

  * If variables are declared but not used, compiler may remove all code (`ret` only).
  * If variables are constant and only used in functions like `printf`, compiler computes results in advance and avoids extra instructions.
  * XOR of a register with itself is used to zero a register efficiently (`xor eax, eax` sets `eax` to 0).
  * Jump (`jmp`) instead of call/ret can be used for faster execution.
