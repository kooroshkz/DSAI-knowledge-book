- RCS (Revision Control System) was one of the most popular Local Version Control Systems (VCS).
- RCS works by keeping patch sets (that is, the differences between files) in a special format on disk.
- Centralized Version Control Systems (CVCS) were developed to solve the problem of sharing changes with developers in different locations.
- Distributed Version Control Systems (DVCS) make every clone is really a full backup of the whole project to prevent data loss by server crash. (Git)

**Git vs. Other VCS**  
- **Other VCS**: Uses **delta-based version control**, tracking changes as file-by-file modifications over time.  
- **Git**: Stores complete snapshots of the project, not just deltas, making it faster and more efficient.

---

- **`git config --local`**: Sets settings only for the current project.  
- **`git config --global`**: Sets settings for all your projects on your computer.  

we can then set `user.name` and `user.email`
### **General Usage of `git checkout`**

1. **Switch to Another Branch**:  
   ```bash
   git checkout <branch_name>
   ```
2. **Create and Switch to a New Branch**:  
   ```bash
   git checkout -b <new_branch_name> #Alternatively, git branch <new_branch_name> but wont switch to it
   ```
3. **Restore a Specific File**:  
   ```bash
   git checkout <commit_hash> -- <file_name>
   ```
   - Example: `git checkout abc123 -- README.md`  
   - Reverts a file to its state in the specified commit.

4. **Switch to a Specific Commit (Detached HEAD)**:  
   ```bash
   git checkout <commit_hash>
   ```
   - Example: `git checkout abc123`  
   - Moves to a specific commit, leaving you in a detached HEAD state.

### **Tips**

- ```bash
  git status -s # Short status. A means added, M means modified, D means deleted.
  ```
- **Untracked files** must be added to Git before `git diff` can show their changes, else we should try 
```bash
  git log -p -1
  ```
- Remove staged file from all logs and commits
```bash
  git rm --cached <file_name>
  ```
- Add tag for a checksum
```bash
  git tag -a <tag_name> <checksum>
  ```


### Git Switch 
1. **Switch to an existing branch**:
   ```bash
   git switch testing-branch
   ```

2. **Create a new branch and switch to it**:
   ```bash
   git switch -c new-branch
   ```
   (The `-c` flag stands for `--create`.)

3. **Return to the previous branch**:
   ```bash
   git switch -
   ```
## Merge

1. **Merge a Branch**:
   ```bash
   git merge <branch_name>
   ```

2. **When a Merge Conflict Occurs**:
   - Git pauses the merge and shows conflicting files:
     ```bash
     git status
     ```

3. **Resolve Conflicts**:
   - Open the file with conflicts and look for markers:
     ```text
     <<<<<<< HEAD
     (your branch changes)
     =======
     (other branch changes)
     >>>>>>> branch_name
     ```
   - Edit the file to resolve the conflict, removing the markers.

4. **Mark as Resolved**:
   ```bash
   git add <file>
   ```

5. **Complete the Merge**:
   ```bash
   git commit
   ```

6. **Abort a Merge** (if you want to cancel):
   ```bash
   git merge --abort
   ```

7. **Use a Visual Tool (optional)**:
   ```bash
   git mergetool
   ```
### **Rebase vs. Merge**

### **1. Merge:**
- **What It Does**: Combines two branches, creating a **merge commit** that reflects the integration.
- **Key Features**:
  - Keeps the full history of both branches.
  - Useful when you want to preserve a branch’s context and history.
  - Results in a branch structure with multiple lines (a "merge graph").


### **2. Rebase:**
- **What It Does**: Re-applies the commits from one branch onto another, creating a **linear history**.
- **Key Features**:
  - Avoids merge commits, making the history cleaner and easier to read.
  - Useful when preparing a feature branch for integration.
  - Changes commit hashes because it rewrites history.

- **Command**:
  ```bash
  git rebase <branch_name>
  ```

### Git Remote

**Remote Repositories**:
   - `git remote` shows remote repositories:
     ```bash
     git remote -v
     ```

   - Add a new remote:
     ```bash
     git remote add <name> <url>
     ```
