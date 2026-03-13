#### **Interfaces & Regular Expressions**

**REST API**: Web-based interaction.
- **GET**: Retrieve data from the server.  
  - Example: You want to see a list of books.  

- **POST**: Create new data on the server.  
  - Example: You want to add a new book.  

- **PUT**: Completely update existing data.  
  - Example: You want to replace all details of a book.  

- **PATCH**: Partially update existing data.  
  - Example: You want to update only the title of a book.  

- **DELETE**: Remove data from the server.  
  - Example: You want to delete a book.  

### **File Operations**
- **Modes**:
  - `'r'`: Read (throws an error if the file does not exist, opens in read-only mode).
  - `'r+'`: Read and Write (throws an error if the file does not exist, allows both reading and writing).
  - `'a'`: Append (throws an error if the file does not exist, opens the file for appending at the end).
  - `'w'`: Write (overwrites the existing content, creates the file if it does not exist).
  - `'x'`: Exclusive Creation (throws an error if the file already exists, creates a new file for writing only).

- **Reading/Writing**:
  - **Read**:
    - `f.readline(n)`: Reads `n` characters.
    - `f.readlines()`: Reads lines until newline (`\n`).
    - `f.read()`: Reads the entire file.
  - **Write**:
    - `f.write("string")`: Writes a string.
## **Regular Expressions**

### **1. Basic Characters**
- **`.`**: Matches any character except a newline.
  - Example: `a.b` matches `acb`, `a5b`, but not `ab`.


### **2. Character Classes**
- **`[abc]`**: Matches any character inside the brackets.
  - Example: `[aeiou]` matches `a` in `apple`.

- **`[^abc]`**: Matches any character NOT in the brackets.
  - Example: `[^aeiou]` matches `t` in `text`.

- **`[a-z]`**: Matches any lowercase letter.
  - Example: `[a-d]` matches `b` in `blue`.


### **3. Quantifiers**
- **`*`**: Matches 0 or more occurrences of the previous character.
  - Example: `a*` matches `aaaa` in `aaaa`. By 0 we mean between any character counts as empty string.

- **`+`**: Matches 1 or more occurrences of the previous character.
  - Example: `a+` matches `aaa` in `aaa`.

- **`?`**: Matches 0 or 1 occurrence of the previous character.
  - Example: `colou?r` matches `color` and `colour`.

- **`{n}`**: Matches exactly `n` occurrences.
  - Example: `a{3}` matches `aaa`.

- **`{n,}`**: Matches `n` or more occurrences.
  - Example: `a{2,}` matches `aaa`.

- **`{n,m}`**: Matches between `n` and `m` occurrences.
  - Example: `a{2,4}` matches `aa` or `aaa`.

- **Greedy vs. Lazy Quantifiers**:
  - Greedy: `.*` matches as much as possible.
  - Lazy: `.*?` matches as little as possible.


### **4. Anchors**
- **`^`**: Matches the beginning of a string.
  - Example: `^a` matches `a` in `apple`.

- **`$`**: Matches the end of a string.
  - Example: `e$` matches `e` in `apple`.

- **`\b`**: Matches a word boundary.
  - Example: `\bcat\b` matches `cat` but not `scatter`.

- **`\B`**: Matches a non-boundary.
  - Example: `\Bcat` matches `scatter`.


### **5. Special Sequences**
- **`\d`**: Matches any digit (0-9).
  - Example: `\d` matches `5` in `5a`.

- **`\D`**: Matches any non-digit.
  - Example: `\D` matches `a` in `5a`.

- **`\w`**: Matches any word character (alphanumeric + `_`).
  - Example: `\w` matches `a` in `a1`.

- **`\W`**: Matches any non-word character.
  - Example: `\W` matches `@` in `a@b`.

- **`\s`**: Matches any whitespace.
  - Example: `\s` matches the space in `a b`.

- **`\S`**: Matches any non-whitespace.
  - Example: `\S` matches `a` in `a b`.


### **6. Groups**
- **`(abc)`**: Matches the exact group.
  - Example: `(cat)` matches `cat` in `catapult`.

- **`|`**: Matches either of the options.
  - Example: `cat|dog` matches `cat` or `dog`.

- **Named Groups**:
  - **`(?P<name>abc)`**: Matches the group `abc` and names it `name`.
  - Example: `(?P<word>\w+)` matches `hello` and assigns it to `word`.

- **Backreferences**:
  - **`\1, \2, ...`**: Matches the same text as captured by a group.
  - Example: `(a)\1` matches `aa`.


### **7. Lookahead and Lookbehind**
- **`(?=abc)`**: Positive lookahead (matches if `abc` follows).
  - Example: `a(?=b)` matches `a` in `ab`.

- **`(?!abc)`**: Negative lookahead (matches if `abc` doesn't follow).
  - Example: `a(?!b)` matches `a` in `ac`.

- **`(?<=abc)`**: Positive lookbehind (matches if preceded by `abc`).
  - Example: `(?<=a)b` matches `b` in `ab`.

- **`(?<!abc)`**: Negative lookbehind (matches if not preceded by `abc`).
  - Example: `(?<!a)b` matches `b` in `cb`.


### **8. Escaping**
- **`\`**: Escapes special characters.
  - Example: `\$` matches `$`.


### **9. Flags**
- **`i`**: Case-insensitive matching.
  - Example: `(?i)a` matches `A` or `a`.

- **`m`**: Multiline mode (makes `^` and `$` match start/end of lines).
  - Example: `^a` matches `a` at the start of any line.

- **`s`**: Dotall mode (makes `.` match newlines).
  - Example: `.` matches `\n` in `a\nb`.

- **`x`**: Allows comments and ignores whitespace in the pattern.
  - Example:
    ```
    (?x)
    a   # Matches 'a'
    b   # Matches 'b'
    ```


### **10. Advanced Operators**
- **Conditionals**:
  - **`(?(condition)yes|no)`**: Matches based on the condition.
  - Example: `(?(1)yes|no)` matches `yes` if group 1 exists.

---
### **Using Regex in Python**

#### **1. Import and Compile**
```python
import re
pattern = re.compile(r'\d+')  # Matches digits
```

#### **2. Matching Methods**
- `match()`: Matches at the start.
- `search()`: Finds the first match anywhere.
- `findall()`: Returns all matches as a list.
- `finditer()`: Returns an iterator of matches.

Example:
```python
text = "12 apples and 10 oranges"
print(pattern.findall(text))  # ['12', '10']
```

#### **3. Substitution**
- `sub()`: Replace matches with a string.
- `subn()`: Same as `sub()` but also returns the number of replacements.

Example:
```python
text = "blue socks and red shoes"
pattern = re.compile(r'(blue|red)')
print(pattern.sub('color', text))  # 'color socks and color shoes'
```

#### **4. Splitting**
- `split()`: Splits a string by the pattern.

Example:
```python
pattern = re.compile(r'\W+')
print(pattern.split("This is a test!"))  # ['This', 'is', 'a', 'test', '']
```



### **Greedy vs Non-Greedy**
- Greedy: `.*` matches as much as possible.
- Non-Greedy: `.*?` matches as little as possible.

Example:
```python
text = "<html><title>Page</title>"
pattern = re.compile(r'<.*?>')  # Non-greedy
print(pattern.findall(text))  # ['<html>', '<title>', '</title>']
```



### **Flags**
- `re.IGNORECASE` (`I`): Case-insensitive matching.
- `re.DOTALL` (`S`): Makes `.` match newlines.
- `re.MULTILINE` (`M`): `^` and `$` match start/end of each line.
- `re.VERBOSE` (`X`): Allows comments and better formatting.

Example:
```python
pattern = re.compile(r"""
    \bword\b   # Match the word 'word'
""", re.VERBOSE)
```


### **Advanced Features**
- **Lookahead/Lookbehind**:
  - Positive: `(?=...)`, `(?<=...)`
  - Negative: `(?!...)`, `(?<!...)`
- **Named Groups**: Use descriptive names for clarity.
```python
pattern = re.compile(r'(?P<name>\w+)')
```


### **Tips and Common Problems**
1. Use raw strings (`r'...'`) to avoid Python’s string escaping issues.
2. Use `search()` for general matching; avoid adding `.*` to `match()`.
3. Be cautious of greedy quantifiers when parsing nested structures.

### **Conclusion**
Regex is a compact, powerful tool for text processing in Python. Practice basic patterns, grouping, and methods like `search()`, `sub()`, and `findall()` for proficiency.