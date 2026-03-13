### How Java Code Works: From Writing to Execution

The `.java` file is compiled by the **Java compiler** (`javac`) into **bytecode**. The compiler generates a `.class` file for every class in program. The **Java Virtual Machine (JVM)** reads the bytecode in the `.class` file and executes it. The JVM translates the bytecode into machine code that your computer can understand.
### Java Structure:
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```
```java
public class Main {}
```

The keyword **public** makes the class accessible from anywhere (other classes and packages). Since the JVM needs access to this class to run your program, you must make it public.
```java
public static void main(String[] args) {    }

```
This is the **entry point** of any Java program, where execution begins. The method is marked **static** so that the JVM can call it **without creating an object** of the class. Normally, you have to create an object to use a method, but here, `main` runs without needing an object. The `void` keyword means the method **doesn't return any value**. The `main` method just starts the program but doesn't give anything back.

##### ** `main` and `Main`**
- In Java, method names are **case-sensitive**. The JVM specifically looks for the `main` method with a lowercase "m". If you write `Main` with an uppercase "M", the program won't run because it's a different method name.
```java
System.out.println("Hello");
```
`System` is a **class** provided by Java in the `java.lang` package, which gives access to system resources like input/output. `out` is a **static member** of the `System` class. It represents the standard **output stream** (like your console or terminal). It’s an instance of the `PrintStream` class.
<hr>
### Constructor
A **constructor** is a special method that runs when an object is created. It has the same name as the class and no return type. 
```java
public class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```
<hr>

#### Vector
Vector in Java is a type of dynamic array like list in python.

```java
import java.util.Vector;

public class VectorExample {
    public static void main(String[] args) {
        Vector<String> fruits = new Vector<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        System.out.println(fruits.get(0)); // Access element
        fruits.remove("Banana");           // Remove element

        System.out.println(fruits);        // Print vector
    }
}
```
