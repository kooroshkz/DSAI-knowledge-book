### **Von Neumann Architecture** 
Design model of the most modern computers with micro-architecture.
* **CPU (Central Processing Unit)** with:
  * **Control Unit (CU):** Directs the flow of data and instructions.
  * **Arithmetic/Logic Unit (ALU):** Does math and logic operations.
* **Memory Unit:** Stores both data and instructions.
* **Input/Output (I/O) Unit:** For communication with the outside world.

##### **Von Neumann Bottleneck**

- Data and instructions share the same bus (Stored in Memory), causing a limitation in throughput (data transfer rate).

The **process (called the fetch-decode-execute cycle):**
  1. **Fetch**: The CPU gets the next instruction from memory (using the program counter).
  2. **Decode + Execute**: The CPU understands the instruction and runs it.
  3. **Increase Program Counter**: Move to the next instruction. (**Imperative paradigm**: Goes Instruction after instruction)

* Well-defined → clear, unique answer.
* Ill-defined → unclear, no single answer.

---

### **MIPS Architecture**

* MIPS is a type of CPU design (a RISC – Reduced Instruction Set Computer).
* Instructions in MIPS are always **32 bits** long, but they come in **three formats**:

  * **R-type (Register):** For operations between registers (like add, sub).
  * **I-type (Immediate):** For operations with constants or memory addresses.
  * **J-type (Jump):** For jump instructions (changing the program counter).

  ```assembly
  add $r1,$r2, $r6 # This means: `$r6 = $r1 +$r2`
  ```

* **Machine code (decimal fields):**
  `[ op | rs | rt | rd | shamt | funct ]`

  * `op = 0` → because this is an R-type instruction.
  * `rs = 1` → first input register.
  * `rt = 2` → second input register.
  * `rd = 6` → destination register.
  * `shamt = 0` → no shifting here.
  * `funct = 32` → tells the CPU this is an **add** operation.

- **Zuse’s Plankalkül** : This was the first high-level programming language
---
### **Turing Machine**
Turing machine will say a computer can do computation which having a initial data (as a model we imagine a tape of 1s and 0s) and a set of rules (as a model we imagine a table of rules, if you where in this state and number was 1 -> change to 0 and move right) to manipulate the data, finnally if we reached halting state (a state where we stop) the data on the tape is the result of the computation. So it shows the problem is breakable down to a set of such simple rules that turing machine can do it. So with computer we can do any computation that turing machine can do.

- **Linguistic Relativity**: The idea that the language we speak influences how we think, see, and understand the world. Different languages may shape thought in different ways.

---

- **Duck Typing**: We dont care about the type of an object, only if it behaves as we expect. Like we define a function to transform given data, regardless which group of data it belongs to, as long as it has the required methods/attributes to be transformed. (e.g. Python, Ruby)
- **Static Typing**: Variable types are *checked at compile-time*, you must declare types before use. (e.g. Java, C, C#)
- **Dynamic Typing**: Types are *checked at runtime* and no need to declare type explicitly. (e.g. Python, JavaScript)
- **Gradual typing**: mix of static + dynamic (e.g., TypeScript, Python with type hints).

- **Formal Language**: A language with strict rules and syntax, often used in mathematics and computer science (e.g., programming languages, logic).
- **Natural Language**: A language that has evolved naturally among people for everyday communication (e.g., English, Spanish).
- **Semi-formal Language**: A language that combines elements of both formal and natural languages, often used in technical documentation (e.g., Mathematical notation, UML diagrams).

