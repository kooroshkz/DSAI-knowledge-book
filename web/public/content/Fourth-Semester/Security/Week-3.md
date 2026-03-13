- **Access Control steps:** Process to allow only authorized users/programs to access or modify system resources.
  - **Identification**
    - Badges, User IDs, Account Numbers, MAC/IP addresses, RFID tags (used in passports, goods), Email addresses (common but spoofable)
  - **Authentication**
    - Verifying identity using passwords, biometrics (iris: for eye), tokens, USB devices, etc.
      -  Biometric accuracy is measured by:
        - False Reject Rate (FRR)
        - False Accept Rate (FAR)
        - Crossover Error Rate (CER) (FRR = FAR, optimal point)
    - MFA (Multi-Factor Authentication): Combining two or more methods for stronger security. 
  - **Authorization**
  - **Accountability** (logging and auditing)
- **Access Control Policies**
  - **Discretionary Access Control (DAC):** Owner decides access; rights can be transferred.
  - **Mandatory Access Control (MAC):** System/admin enforces strict rules based on labels; no transfer of rights.
  - **Non-Discretionary Access Control:** Access based on roles or attributes; admin controls permissions.
  - **Role-Based Access Control (RBAC):** Access granted based on roles (job functions).

- **Access Control Mechanisms**
  - **Access Control Lists (ACLs):** List of permissions attached to each resource.
  - **Capabilities:** Tokens held by users defining their access rights.
  - **ACLs** are simpler to implement, but harder to check at runtime, **Capabilities** are easier to check but harder to manage in big systems.

---

### Permissions in Linux (rwx notation)

- **r (read)** or 4
- **w (write)** or 2
- **x (execute)** or 1

- **Order**: file/dir | Owner | Group | World (example: `-rwxr-xr--`)
  - **File/Dir Type**: `-` for file, `d` for directory, `l` for link.
  - Then come 9 characters divided into 3 parts:
    - **Owner permissions**: first 3 characters (rwx or 7)
    - **Group permissions**: next 3 characters (r-x or 5)
    - **World permissions**: last 3 characters (r-- or 4)
    - Can also be represented in octal (e.g., 754 and `chmod 754 filename` to set permissions).

### Privilege Classes in Systems

* **Owner:** The creator or admin of a resource, with full access, can set permissions for others. (rwx)
* **Group:** A set of users grouped together, have shared access rights to resources.
* **World:** All other users with minimal privileges.
* **Superuser:** Has all privileges. (rwx)

---

### Separation of Duties (SoD)

- Not giving one person too much control in a system or process.
  * A user **cannot have conflicting roles** (e.g., cannot be both accountant and auditor).
  * A user in role r1 **must also have role r2** (e.g., a lecturer must also be a faculty member).
  * A least 2 users for role r1)
  * **Four eyes principle:** Certain actions require approval of at least two people 

- **Multi-level Security Models**
  - **Bell-LaPadula Model** (Confidentiality of information: keep information secret)
    - **Simple Security Property:** No read up — Lecturers cannot read faculty secrets.
    - **\*-Property (Star Property):** No write down — Board Members can’t share secrets with Lecturers or Students.
  - **Biba Model (Integrity Focus)** (no unauthorized changes: keep information accurate and trustworthy)
    - **Simple Integrity :** No read down — Everyone can read a website.
    - **star / \*-Integrity :** No write up — Only admins can edit a website.
  - **Chinese Wall Model (Conflict of Interest Focus)**
    - Make sure people don’t see or share information between companies that compete with each other.