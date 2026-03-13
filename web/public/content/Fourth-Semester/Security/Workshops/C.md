### Memory Management in C

* Two memory areas: **stack** and **heap**.
* Stack: stores fixed-size variables, size known at compile time.
* Heap: dynamic memory, allocated at runtime using `malloc()`.
* After using heap memory, release it with `free()`.
* Example:

  ```c
  int* nums = (int*)malloc(3 * sizeof(int));  // allocate memory for 3 ints
  nums[0] = 1;
  nums[1] = 2;
  free(nums);  // release memory
  ```
* Be careful of **use-after-free** bugs (using memory after `free`).

---

### Pointers

* Pointers hold memory addresses.
* You can use pointers to access and modify memory directly.
* Passing variables by **value** copies the data (no changes affect original).
* Passing by **reference** (passing pointer) allows modifying original data.
* Example difference:

  ```c
  void byValue(int a, int b, int c) { c = a + b; }        // no effect outside
  void byReference(int* p) { p[2] = p[0] + p[1]; }       // modifies original array
  ```

---

### Strings in C

* No built-in string type; strings are **arrays of chars**.
* Strings end with a **null-terminator** `\0`.
* Always allocate one extra byte for the null terminator.
* Example to count letters:

  ```c
  char* my_string = "Hello world";
  int count = 0;
  char* c = my_string;
  while (*c != '\0') {
      if (*c == 'l') count++;
      c++;
  }
  printf("Number of 'l's: %d\n", count);
  ```

---

### Arguments and Return Codes

* `main` can take arguments: `int main(int argc, char** argv)`

  * `argc`: number of arguments.
  * `argv`: array of strings (arguments).
* Program name is always the first argument (`argv[0]`).
* Return code signals success (0) or failure (non-zero).
* Example:

  ```c
  int main(int argc, char** argv) {
      if (argc < 2) return 1;  // exit if not enough arguments
      for (int i = 0; i < argc; i++) {
          printf("%s\n", argv[i]);
      }
      return 0;
  }
  ```

---

### Important Practical Tips

* Always free memory allocated with `malloc()`.
* Use pointers carefully to avoid bugs.
* Remember to include space for the null terminator in strings.
* When passing variables to functions, use pointers if you want the function to modify the original data.
* Return codes help indicate if your program ran successfully.
