## 1. What is GDB?

* GDB (GNU Debugger) lets you **run and control** programs, **pause** them at specific points, and **inspect memory, variables, and registers**.
* It’s useful for debugging and especially important in cybersecurity when source code is not available.
* You can start GDB from the terminal:

  ```bash
  gdb program_name
  ```
* In GDB, type `run` to start the program.

---

## 2. Debug Information in Executables

* Compilers usually add **debug symbols** to executables to help debugging (function names, variable info).
* Using `gcc -g` adds debug info; `gcc -s` strips it (makes debugging harder).
* Without debug info, GDB can’t easily stop at function names, so you must use memory addresses.

---

## 3. Breakpoints — Pausing Execution

* Breakpoints stop the program at specific points so you can inspect it.

### 3.1 Setting Breakpoints

* Stop at function start prologue (first instruction of function setup):

  ```gdb
  break *function_name
  ```
* Stop just after function prologue (start of “real” function code):

  ```gdb
  break function_name
  ```
* Stop at specific instruction address:

  ```gdb
  break *0xaddress
  ```
* You can also do relative breakpoints like:

  ```gdb
  break *main+12
  ```

  (12 bytes after main’s start)

---

### 3.2 Controlling Execution

* Step **one assembly instruction** at a time:

  ```gdb
  stepi  # or si
  ```
* Continue running until next breakpoint or program ends:

  ```gdb
  continue  # or c
  ```

---

### 3.3 Managing Breakpoints

* List all breakpoints:

  ```gdb
  info breakpoints
  ```
* Disable/enable breakpoints:

  ```gdb
  disable breakpoint_number
  enable breakpoint_number
  ```
* Ignore breakpoint a number of times before stopping:

  ```gdb
  ignore breakpoint_number times
  ```
* Delete breakpoints:

  ```gdb
  delete breakpoint_number  # or delete all
  ```

---

## 4. Viewing Assembly Code (Disassemble)

* Use Intel syntax for consistency:

  ```gdb
  set disassembly-flavor intel
  ```
* Show assembly of current function:

  ```gdb
  disassemble
  ```
* Show assembly of a specific function:

  ```gdb
  disassemble function_name
  ```
* Useful to find exact instruction addresses for breakpoints.

---

## 5. Inspecting Registers and Memory

### 5.1 Registers

* Show all CPU registers:

  ```gdb
  info registers
  ```

  or

  ```gdb
  i r
  ```
* Important registers:

  * `rdi, rsi, rdx, rcx`: 1st 4 function arguments.
  * `rax`: Return value.
  * `rip`: Next instruction to execute.
  * `rsp, rbp`: Stack pointer and base pointer.

---

### 5.2 Memory Layout Overview

| Segment / Region            | Description                                       |
| --------------------------- | ------------------------------------------------- |
| Kernel space                | OS memory, inaccessible to programs               |
| CLI args & environment vars | Program arguments and environment variables       |
| Stack                       | Local variables, grows downward, tracked by `rsp` |
| Heap                        | Dynamic memory via `malloc()`, non-contiguous     |
| Uninitialized data          | Globals/statics without initial values            |
| Initialized data            | Globals/statics with initial values               |
| Text segment                | Program’s code instructions, `rip` points here    |

---

### 5.3 Inspect Memory

* Command:

  ```
  x/nuf address
  ```

  where:

  * `n` = number of units (default 1)
  * `u` = unit size: `b`(1 byte), `h`(2 bytes), `w`(4 bytes), `g`(8 bytes)
  * `f` = format: `x`(hex), `d`(decimal), `t`(binary), `a`(address), `s`(string), `c`(char), `i`(assembly)
  * `address` can be a symbol, register (`$rip`), expression, or number. * Examples: * Show 3 instructions at `main`: ``` x/3i main ``` * Show 8 bytes below `rbp`: ``` x/-8bx$rbp
    ```
  * Show 2 words (4 bytes each) below `rbp`:

    ```
    x/-2wx $rbp
    ```

---

## 6. Endianness (Byte Order)

* Most CPUs (including x86-64) use **little endian**: least significant byte stored at lowest address.
* For example, `0x00000001` stored as bytes: `01 00 00 00`.
* Important when reading memory dumps byte-by-byte.
* Big endian is the opposite (rare on personal computers).

---

## 7. Advanced GDB Usage (Bonus Tips)

* Compile with `-g` to add debug info for better debugging.
* GDB can map assembly to source code lines, variable names, etc.
* Explore many other commands and features in GDB manuals.
