## Four Pillars of OOP

- **Abstraction**
- **Encapsulation** : Encapsulation is "hiding" the internal details of a class and providing methods to interact with it.
- **Inheritance**
- **Polymorphism**: Same method name performs different tasks depending on the object.

- Class variable can be called thorugh objects and Class name.
```python
class Dog:
    kind = 'canine'  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

d1 = Dog('Fido')

d1.kind == 'canine' == Dog.kind
```
---

The `assert` keyword is used when debugging code.

The `assert` keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.

```python
x = "welcome"

#if condition returns False, AssertionError is raised:
assert x != "hello", "x should be 'hello'"
```
---
1. **@classmethod**:
   - Operates on the **class itself**, not instances.
   - Requires the `cls` parameter to refer to the class.
   - Use it when you want to access or modify class-level data (e.g., shared attributes).

   ```python
   class Example:
       shared_data = 0

       @classmethod
       def modify_shared_data(cls, value):
           cls.shared_data += value

   Example.modify_shared_data(5)
   print(Example.shared_data)  # Output: 5
   ```

2. **@staticmethod**:
   - Independent of the class or instance.
   - Does **not require `self` or `cls`**.
   - Use it when you need a utility function that logically belongs to the class but doesn’t touch class/instance data.

   ```python
   class Example:
       @staticmethod
       def utility(a, b):
           return a + b

   print(Example.utility(3, 4))  # Output: 7
   ```

### **Private Variables**

- **Private-like Variables**: Prefix with `__` to prevent accidental access.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # Output: 150
# print(account.__balance)  # Error: AttributeError
```

---

### **Iterators**

- **Iterator**: Object with `__iter__` and `__next__` methods.
- The for loop automatically calls __iter__() to get the iterator and repeatedly calls __next__() to fetch elements to make iterable objects.

```python
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = ReverseIterator("hello")
for char in rev:
    print(char)  # Output: o l l e h
```

---

### **8. Generators**

- **Generators** simplify iterators using `yield`.
- Saves state between `yield` calls.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
# Output: 5 4 3 2 1
```

- Generators are concise compared to custom iterators.
- With Return statement, the generator function will raise a StopIteration exception.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
    return "done"

gen = countdown(5)
while True:
    try:
        number = next(gen)
        print(number)
    except StopIteration as e:
        print(e.value)
        break
```

---

### **9. Polymorphism**

- **Same method, different behavior** depending on the class.

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())
# Output: Woof Meow Animal sound
```

---

### **10. Special Methods**

- Enable custom behavior for built-in operators (`+`, `==`, `len()`, etc.).

#### Common Special Methods
- `__init__`: Object initialization.
- `__str__`: String representation.
- `__add__`: Add objects.
- `__len__`: Return length.

**Example**: Custom `Vector` class.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3)  # Output: Vector(6, 4)
```