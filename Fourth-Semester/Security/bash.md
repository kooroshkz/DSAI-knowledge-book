# **Introduction to Shell**

A **shell** is a type of CLI that allows users to execute commands and programs. Examples of shells:
- **Bash (Bourne Again Shell)** (most common)
- **Zsh (Z Shell)**
- **Fish (Friendly Interactive Shell)**

Verify shell Type:
```sh
echo $SHELL # for location
echo $0 # for name
```


### **Common Commands:**
| Command | Description |
|---------|-------------|
| `echo "text"` | Print text to the screen |
| `less <file>` | View file contents one page at a time |
| `man <command>` | Show manual pages for a command |

### **Directory Structure:**
- **Root Directory (`/`)**: The base of the file system.
- **Home Directory (`~`)**: Each user has a home directory.


## **Executing Multiple Commands**
| Operator | Function |
|----------|------------|
| `;` | Execute multiple commands sequentially |
| `&&` | Execute next command only if the first succeeds |
| `||` | Execute next command only if the first fails |
| `&` | Run command in the background |

### **Examples:**
```sh
python3 script.py & ls  # Run script in background, then list files
```

## **5. Output Redirection & Piping**
| Operator | Function |
|----------|------------|
| `>` | Redirect output to a file (overwrite) |
| `>>` | Append output to a file |
| `<` | Read input from a file |
| `|` | Pipe output of one command to another |

### **Examples:**
```sh
ls > files.txt  # Save directory listing to files.txt
echo "Hello" >> messages.txt  # Append Hello to messages.txt
sort < names.txt  # Sort contents of names.txt
ls | grep "txt"  # Show only .txt files
```

## **4. File and Directory Permissions**
Each file/directory has three types of permissions for three groups:
1. **Owner** (u) → Creator of the file.
2. **Group** (g) → Users belonging to the same group.
3. **Others** (o) → Everyone else.

| **Symbol** | **Permission** | **For files** | **For directories** |
|-----------|-------------|------------|-------------|
| `r` | Read | View contents | List files |
| `w` | Write | Modify file | Add/delete files |
| `x` | Execute | Run as a program | Enter the directory |

**Example of `ls -l` output:**
```bash
drwxrwxr-x 2 cesar students 40 Jan 1 00:01 pictures
-r--r--r-- 1 cesar students 429 Jan 1 00:01 favourite_pokemons.txt
```
- `d` → Directory.
- `rwxrwxr-x` → Permissions (Owner: `rwx`, Group: `rwx`, Others: `r-x`).
- `2` → Number of links to the file.
    - Give permissions to a file:
      ```sh
      chmod u+x script.sh
      ```
    - Remove permissions from a file:
      ```sh
      chmod u-x script.sh
      ```
    - Change permissions for all groups:
      ```sh
      chmod a+r script.sh
      ```
    - Change permissions for a group:
      ```sh
      chmod g-w script.sh
      ```
    - Change permissions using numbers:
      ```sh
      chmod 755 script.sh
      ```
      - `7` → Owner has `rwx` permissions.
      - `5` → Group has `r-x` permissions.
      - `5` → Others have `r-x` permissions.
      - `4` → `r--`, `6` → `rw-`, `0` → `---`.


## **7. Environment Variables**
- View all environment variables:
  ```sh
  printenv
  ```
- View a specific variable:
  ```sh
  echo $PATH
  ```
- Set a temporary variable:
  ```sh
  VARIABLE=value command
  ```
    - Example:
      ```sh
      MEMORY_LIMIT=1024 python3 script.py # Runs `script.py` with `MEMORY_LIMIT` set to `1024` temporarily till the script executes.
      ```

- Set a persistent variable:
  ```sh
  export VARIABLE=value
  ```

### **Variables in Scripts:**
```sh
#!/bin/bash
NAME=Francesco
echo "${NAME} is learning Bash!"
```

### **Conditional Statements:**
```sh
if [[ ${USER} == "root" ]]; then
    echo "You are root!"
else
    echo "You are not root!"
fi
```

### **Loops in Bash:**
```sh
for i in {1..5}; do
  echo "Iteration $i"
done
```