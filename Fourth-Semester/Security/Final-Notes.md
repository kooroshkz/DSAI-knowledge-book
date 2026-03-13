- **Security Principles (CIA Triad)**: 
  - **Confidentiality**: Restricting unauthorized access and disclosure.
  - **Integrity**: Ensuring data is not altered or tampered with.
  - **Availability**: Ensuring information is accessible when needed.
- **Additional Security Goals**:
  - **Authenticity**: Ensuring data or identity is genuine.
  - **Authentication**: Verifying user/system identity.
  - **Authorization**: Ensuring only permitted entities access resources.
  - **Accuracy**: Ensuring information is correct for its purpose.
  - **Accountability**: Tracing actions back to responsible entities.
  - **Non-Repudiation**: Preventing denial of performed actions.
  - **Privacy**: Controlling access to personal or sensitive information.
  - **Computer Security (COMPUSEC)**: Protection of computer assets (hardware, software, data).
  - **Information Systems Security (INFOSEC)**: Safeguarding data from unauthorized access and attacks.
  - **Information Security**: Protecting data and systems from threats while ensuring CIA principles.

## **Security Controls (Countermeasures)**
|                          | Physical            | Logical/Technical            | Administrative/Policies          |
|--------------------------|--------------------|-----------------------------|----------------------------------|
| **Preventive (+deterrence)** | Security guard    | Firewall                    | Employee screening policy       |
| **Detective**            | Security camera    | Intrusion detection system  | Policy to review transaction logs |
| **Corrective/Responsive**| Fire sprinklers    | Backup servers              | Law enforcement liaison         |

- **Attack/Threat Types $\to$ Security Requirements**
  - Spoofing $\to$ Authenticity
  - Tampering $\to$ Integrity
  - Repudiation $\to$ Non-repudiation
  - Information Disclosure $\to$ Confidentiality
  - Denial of Service (DoS) $\to$ Availability
  - Elevation of Privilege $\to$ Authorization
- **Trust in Security**
  - **Trusted Component**: A system part we rely on but might not fully verify.
  - **Trusted Computing Base (TCB)**: The minimal set of components that must be trusted.
  - **Minimizing Trust**:
    - Reduce the number of **trusted** components.
    - Design systems to **require minimal trust**.
    - Verification increases **trustworthiness**.

---
- **Risk Assessment**:
    - Assets: What is valuable in the system (User data, Software, Hardware)
    - Threats scenarios: What could harm the assets (Hackers stealing data (information disclosure), System crashes or downtime (denial of service), Unauthorized access or data changes (spoofing, tampering))
    - Impact of threats: How severe the consequences are (If data is stolen (threat), student privacy (asset) is lost.)
    - Quantify the risks: Estimate how likely each threat is to happen (%,l/m/h - low damage, financial loss, reputation damage - Risk = Likelihood × Impact (can be numeric or descriptive).)
    - Countermeasures: what to reduce the risk (Encryption, Access controls, Regular backups, Security training for users) 

- **Standards and Frameworks**
    - **ISO/IEC 27000 series:** Info security management standards.
    - **ISO 31000:** Risk management Process.
    - Identify vulnerabilities and threats $\to$ select tools, techniques $\to$ assess risk $\to$ decide strategies $\to$ consider countermeasures.
    - **NIST 800-30:** Guide for risk assessments.
    - **NIST 800-53:** Security and privacy controls.
    - **ISACA COBIT:** IT systems management framework.

- **Design Principles**
    - **Separation of Duties (SoD):** Avoid conflicts by dividing tasks among different people (e.g., one person creates users, another approves).
    - **Least Privilege:** Give users only the access they need, no more.
- **Risk Management Methods**
    - **Tabular methods:** Popular in industry (tables showing risks and controls).
    - **Graphical methods:** More academic (diagrams, charts).

- **STRIDE Framework (Threat Modeling)** $\to$ Countermeasures:
    - **Spoofing** $\to$ Trust the identity? $\to$ Authentication, session management, digital certificates
    - **Tampering** $\to$ Data changed? $\to$ Digital signatures, access control, auditing
    - **Repudiation** $\to$ Actions denied? $\to$ Logging, auditing, digital signatures
    - **Information Disclosure** $\to$ Data theft risk? $\to$ Access control, encryption
    - **Denial of Service (DoS)** $\to$ Service access prevented? $\to$ Rate limiting, boundary protection, redundancy
    - **Elevation of Privilege** $\to$ Unauthorized privilege gain? $\to$ Authorization, least privilege, input validation

- **STRIDE Threat Modeling Steps**
    - Define key assets and security needs.
    - Create data flow diagrams (DFDs).
    - Draw trust boundaries (zones with different trust levels).
    - Identify threats crossing these boundaries.
    - Plan controls to mitigate threats.
    - Validate controls work.

---

- **Access Control steps:** Process to allow only authorized users/programs to access or modify system resources.
  - **Identification**
  - **Authentication**
    - Verifying identity using passwords, biometrics (iris: for eye), tokens, USB devices, etc.
      -  Biometric accuracy is measured by:
        - False Reject Rate (FRR)
        - False Accept Rate (FAR)
        - Crossover Error Rate (CER) (FRR = FAR, optimal point)
    - **Factors**:
      - Authentication by knowledge —something a person knows
      - Authentication by possession —something a person has
      - Authentication by characteristic —something a person is
    - MFA (Multi-Factor Authentication): Combining two or more methods for stronger security. 
  - **Authorization**
  - **Accountability** (logging and auditing)
- **Access Control Policies**
  - **Discretionary Access Control (DAC):** Owner decides access; rights can be transferred.
  - **Mandatory Access Control (MAC):** is a security model where the system (or administrator) enforces access restrictions based on security labels, and users cannot change or transfer their own access rights.
  - **Non-Discretionary Access Control:** Access based on roles or attributes; admin controls permissions.
  - **Role-Based Access Control (RBAC):** Access granted based on roles (job functions).

- **Access Control Mechanisms**
  - **Access Control Lists (ACLs):** List of permissions attached to each resource.
  - **Capabilities:** Tokens held by users defining their access rights.
  - **ACLs** are simpler to implement, but harder to check at runtime, **Capabilities** are easier to check but harder to manage in big systems.

- **Separation of Duties (SoD)**

    - Not giving one person too much control in a system or process.
    - A user **cannot have conflicting roles**
    - A user in role r1 **must also have role r2**
    - **Four eyes principle**

- **Multi-level Security Models**
  - **Bell-LaPadula Model** (Confidentiality of information: keep information secret)
    - **Simple Security Property:** No read up — Lecturers cannot read faculty secrets.
    - **\*-Property (Star Property):** No write down — Board Members can’t share secrets with Lecturers or Students.
  - **Biba Model (Integrity Focus)** (no unauthorized changes: keep information accurate and trustworthy)
    - **Simple Integrity :** No read down — Everyone can read a website.
    - **star / \*-Integrity :** No write up — Only admins can edit a website.
  - **Chinese Wall Model (Conflict of Interest Focus)**
    - Make sure people don’t see or share information between companies that compete with each other.

---

- **OSI Model** has **7 layers** (from top to bottom):
  - **1) Application** (user interface, e.g. browsers, email): HTTP, SMPTP, DNS
  - **2) Presentation**: Handles how data is formatted or encrypted so both ends understand each other: Telnet, FTP
  - **3) Session**: Manages and controls connections between apps (starting, maintaining, ending sessions).
  - **4) Transport** Responsible for sending data between hosts reliably or unreliably.
    - TCP: Makes a connection before sending ordered data, slower but reliable, use 3 hand shakes(e.g. web pages, emails)
    - UDP: Sends data without establishing a connection and recieve check, Faster but less reliable (e.g. video streaming, online gaming)
  - **5) Network** Deals with routing and logical addressing (IP addresses).
    - **Addressing** (IP of destination used until reached)
    - **Fragmentation** (breaking large packets into smaller ones for transmission)
    
  - **6) Data Link** Makes sure data frames are error-free and handles hardware addresses (MAC).
    - Logical Link Control (LLC): Manages connections between two peers, providing error and flow control
    - Media Access Control (MAC): Transmits/Receives frames. Logical topologies and HW addresses are defined here.
  - **7) Physical**: Physical signals, cables, and bits transmitted.

- **TCP/IP** model is similar but with fewer layers:

  * Application (In OSI: Application, Presentation, Session)
    - HTTP, FTP, SMTP, DNS (domain name system)
  * Transport (In OSI: Transport)
    - TCP (reliable), UDP (unreliable)
  * Internet (In OSI: Network)
    - IP (Internet Protocol), ICMP (error messages)
  * Network access (In OSI: Data Link, Physical)
    - Ethernet, Wi-Fi, etc.

- **HTTP Proxying**: A way to send web requests through another server.
  - **Anonymizing proxies:** These hide who you really are when you browse the web.
    - Example:* A company uses this so competitors can’t see what websites they visit.
  - **Open proxy servers:** These let anyone use them to send web requests without restrictions. (Attackers -> hide their identity.)
  - **Content filtering:** Block websites that are not allowed (like social media at work).

- **HTTP Tunneling**:
  - Used to **get around firewalls or restrictions** but not to break security. It wraps (or hides) the real data inside regular web traffic (HTTP), so firewalls don’t block it.
    - If a firewall blocks a video app, HTTP tunneling can let the app work by sending its data inside normal web requests.

- **IPSec**: Used to secure communication over IP networks (VPNs), provides **authentication** and **encryption**.
  - Key Parts:
    - **AH (Authentication Header)**: Checks the data wasn’t changed and confirms the sender’s identity, sends a special code (hash) before each packet to prove it’s real.
    - **ESP (Encapsulating Security Payload)**: Encrypts the data so only the receiver can read it and check data didn't got changed
    - **Security Associations (SAs)**: Contract between two devices on using AH or ESPand encryption and authentication methods.
  - **Modes**:
    - **Transport Mode**: Only payload is encrypted, used for end-to-end communication.
    - **Tunnel Mode**: Encrypts the entire packet, creating a new IP header, used for VPNs.
- **IKE (Internet Key Exchange)**: Used to set up secure connections and manage keys for IPSec.
  - **Phases**:
    - **Phase 1**: Establishes a secure channel between two devices.
    - **Phase 2**: Using that tunnel, they set up the real security rules (SAs) to protect the data communication.

- **Network Attacks**
    - **Scanning Techniques**
        - **Port Scanning:** Checks open ports to find vulnerabilities by TCP handshakes.
        - **FIN**: Sends TCP packet to close a connection without completing the handshake, used to find open ports.
        - **NULL Scan**: Sends packets with no flags set, used to identify open ports.
        - **XMAS Scan**: Sends packets with FIN, URG, and PSH flags set, used to identify open ports.
- **IP Fragmentation Attacks**
    - **Teardrop Attack:** Sends overlapping fragments causing crashes.
    - **Overlapping Fragment Attack:** Bypasses firewall by sending harmful fragments after harmless ones.
    - **Source Routing Exploitation:** Attacker controls packet route to access internal networks.
    - **Smurf Attack:** Attacker spoofs victim IP, sends broadcast ping; victim overwhelmed by replies.
- **Denial of Service**
    - **DoS** , **DDoS (Distributed Denial of Service)**
    - **SYN Flood:** In DDoS, sends many fake connection requests to exhaust server resources, preventing legitimate connections.
Here’s your completed notes based on the lecture content and simple explanations:
- **Spoofing**
    - **IP Address Spoofing:** The attacker sends packets with fake (bogus) source IP addresses.
        - In a **SYN flood attack**, the attacker sends many connection requests (SYN packets) with fake IPs. The victim replies with SYN+ACK packets but never gets the final ACK, leaving many half-open connections. This overloads the victim’s system and blocks real users.
    - **Email Spoofing:** Typo of phishing where attacker sends fake emails by changing sender'd address by telnet on mail servers (port 25)
- **DNS Attacks**
    - **DNS Spoofing / DNS Poisoning:** Attackers inject fake DNS records into a DNS server’s cache.
        - **DNSSEC** helps by adding authentication to DNS responses but isn’t widely used yet.
    - **Pharming:**  Redirecting users to fake websites by:
        - Changing the **hosts file** on a user’s computer.
        - Hacking or compromising the DNS server itself.
---

- Data travels through many **hops** (e.g., your PC → home router → university router → server).
- **Spoofing** $\to$ Data can be modified
- **Lack of confidentiality** $\to$ Data can be read
- **Lack of authenticity** $\to$ Fake data can be sent
- **Firewall** : Controls data entering or leaving a networkin boundary (like a router/devide)
  - **DMZ (Demilitarized Zone)**: A separate network area that adds an extra layer of security between the internet and the internal network (trusted network: which is most secure area).
- **Packet-filtering Firewalls** (Common): Apply **rules** to packets, actions can be: ACCEPT, REJECT, or DROP packets
  - **Stateless:** Checks packets individually, no memory of past packets.
  - **Stateful:** Keeps track of connections, more secure.
  - **Disadvantages:**
    - Cannot block all attacks.
    - Can be tricked by hiding traffic in allowed ports.
    - Complex rule sets can be hard to manage.
    - Only works if traffic passes through firewall (mobile data bypasses it).
- **Proxy Firewalls** (Application - Layer 7):
  - Acts as an intermediary between client and server which can filter traffic more intelligently than packet-filtering firewalls.
  - Can be **explicit** (client knows about proxy) or **transparent** (client doesn’t know).
  - Can require authentication.
  - **Advantages:**
    - Logs all activity (good for accountability).
    - Can cache content to reduce bandwidth.
    - Filters traffic more intelligently.
  - **Disadvantages:**
    - Complex to set up and maintain.
    - Can slow down performance.
    - Must trust proxy with sensitive data (proxy sees all traffic).
- **Tiered Architecture**: Combining different firewalls (packet-filtering + proxy) for better protection between internet and internal network.
- **Intrusion Detection Systems (IDS)**:  monitor network or system events to detect unauthorized activity.
  - **Base Rate Fallacy in IDS**:
    - Produce many false alarms.
    - Increasing sensitivity $\to$ reduces missed attacks but $\to$ increases false positives.
    - Decision on sensitivity depends on **threat model** and **risk tolerance**.
  - **NIDS (Network-based IDS):** Listens to network traffic at key points like routers or switches. Example tools: Snort, Suricata.
  - **HIDS (Host-based IDS):** Monitors activities on a specific device (logs, files, system calls). Example tool: OSSEC.
- **Intrusion Prevention Systems (IPS)** can also take action to stop attacks (e.g., block traffic).
- **Event Analysis Methods**
  - **Signature-based Detection**:
    - Uses known patterns (signatures) of attacks to identify malicious activity.
    - Fast and accurate if signatures are updated.
    - Can miss new or unknown attacks.
    - Example: Detects ping scans (nmap) by looking for empty ICMP packets.
  - **Anomaly-based Detection**:
    - Learns normal behavior and alerts on deviations.
    - Can detect new attacks.
    - Hard to configure and can cause false alarms.
    - Requires good training data.
---

## Memory Layout: Stack & Heap

- **Stack:** Stores function calls, local variables, return addresses in order. (LIFO - Last In, First Out).
- **Heap:** Used for dynamic memory allocation (malloc/new). (Follows a more complex structure, not LIFO).
- Functions push data onto the stack in a specific way (arguments, return address, frame pointer, local variables).
- When a function is called:
    - Arguments pushed in reverse order.
    - Return address saved.
    - Stack frame set up with local variables.
- **Buffer** fixed-size block of memory that holds data, like an array.

| Stack Position                       | Content                                                           |
| ------------------------------------ | ----------------------------------------------------------------- |
| Top (higher addr)                    | main's data                                                       |
| Arguments                            | arg3, arg2, arg1                                                  |
| Saved `%ebp`                         | The old base pointer                                              |
| Return Address (for `%eip`)          | Address where func should return to (next instruction after call) |
| Local Variables                      | Below saved `%ebp`                                                |
| `%esp` points here (bottom of frame) |                                                                   |

- `%esp` is the stack pointer register stores the address of the top of the stack

- `%ebp` or **Extended Base Pointer** mark the base of the current stack frame and in functino call %ebp is then set to the current stack pointer %esp helping the program keep track of where the function's local variables and arguments are stored on the stack.

- `%eip` is the instruction pointer register which holds the address of the next instruction to run. In function call, return address (where to go after) is saved on the stack for %eip to use later.

- **Buffer Overflow:**
    - First, **overflow the local buffer** with your attack code.
    - Then overwrite the **saved %ebp** (optional, but often done).
    - Finally, **overwrite the return address** with an address pointing back to your shellcode in the buffer.
    - When the function returns, CPU uses the overwritten return address (`%eip`) and jumps to your malicious code.
- **Stack Overflow** (Stack Smashing): is a type of buffer overflow that attacker overwrite the **return address** on the stack and inject **malicious code (shellcode)** that runs a command.
- **Nop Sled:** A technique where many "no operation" commands (NOPs) are placed before shellcode to help find the right jump address.
- **Heap Overflow**
- **Integer Overflow**
- **Read Overflow** - **Heartbleed Bug**

- **Race Conditions (TOCTOU - Time Of Check to Time Of Use)**
    - Happens when a program checks a condition but the situation changes before the action is done.
    - Attackers exploit this to cause unexpected behavior or security holes.
    - Like a program checks permission of code changing sth on file first, but an attacker can change the file between that check and actual writing time gap, causing the program to write to a wrong or protected file.

---
- **Defenses in Application Security**:
  - **Language-Based Safety**
      - **Spatial safety:** No out-of-bounds access (don't read/write outside allocated buffers).
      - **Temporal safety:** No use-after-free or use of uninitialized pointers (don't use memory that’s been freed).
      - **Dangling pointers:** Point to freed or invalid memory → dangerous.
      - **Type safety:** Operations on data must match their type (e.g., treating an integer as a pointer is unsafe).
  - **Preventive Measures**
      - **Non-Executable Memory**
          - Mark memory areas (like stack/heap) as non-executable to prevent running injected code.
          - Prevents running injected malicious code.
      - **Address Space Layout Randomization (ASLR)**
          - Randomly rearranges memory locations of key program areas (like stack, heap, libraries).
  - **Detective Measures**
    - **Stack Canaries**
      - Special values placed before return addresses on the stack to detect buffer overflows.
      - If a buffer overflow overwrites this value, the program detects it and aborts.
      - Types:
        - Terminator canaries (special chars)
        - Random canaries (random secret values)
        - XOR canaries (random canaries XORed with return address)
    - **Control Flow Integrity (CFI)**
      - Program’s control flow (which functions jump where) is checked against expected paths and stops if unexpected jumps occur.
      - A Control Flow Graph (CFG) is built during compile time.
      - **Can stop:**
        - Code injection attacks (like buffer overflows that redirect execution)
        - Redirecting control flow to malicious code (like return-to-libc attacks)
      - **Cannot stop:**
        - Attacks that follow allowed paths but misuse them (mimicry attacks)
        - Data corruption or data leaks (like Heartbleed)
        - Control flow changes based on bad data (CFI only checks function jumps, not data flow)
      - **In-line Reference Monitor (IRM):** This is extra code added to check if the next jump is allowed by looking at labels attached to possible jump targets.

| Attack Type                 | What it Does                      | Defense/Prevention               |
| --------------------------- | --------------------------------- | -------------------------------- |
| Buffer Overflow             | Overwrites memory                 | Bounds checks, stack canaries    |
| Heap Overflow               | Overflow in heap memory           | Bounds checks, safe memory alloc |
| Format String Vulnerability | Manipulates format specifiers     | Use format strings properly      |
| Integer Overflow            | Wrap-around number errors         | Check integer sizes              |
| TOCTOU Race Condition       | Time gap exploitation in file use | Atomic operations, safer code    |
| Return-to-libc              | Jump to existing code             | ASLR                             |
| Code Injection              | Inject malicious code             | Non-executable memory            |
| Control Flow Hijack         | Jump to unexpected code           | CFI                              |

---

- **Cryptography:** Confidentiality, Authentication, Non-repudiation (Sender cannot deny they sent it)
  - **Symmetric-Key Cryptography**: one shared secret key, faster than public-key but harder to share keys securely.
    - **Advantages**: Fast encryption and decryption, Efficient for hardware and software, Provides confidentiality and some integrity
    - **Disadvantages**: Hard to distribute and manage keys, Number of keys grows quickly with users, No support for digital signatures (non-repudiation)
  - **Classical Cryptosystems** (Old-school ciphers)
    - **Caesar Cipher:** Shift letters by 3 places.
    - **Vigenère Cipher:** Uses keyword to shift letters differently per position.
    - **Transposition Cipher:** Rearranges letters without changing them in zigzag pattern.
  - **The Three Big Ideas**
    - **Confusion:** Hide plaintext-ciphertext link.
    - **Diffusion:** Spread influence of plaintext bits over ciphertext bits.
    - **Kerckhoffs’s Principle:** Keep algorithm public, key secret.
  - **Symmetric Encryption Algorithms**
    - **Stream Ciphers:** Encrypt data one bit or byte at a time. (e.g., One-Time Pad: Pass bits through XOR with key).
      - Key must be as long as message, truly random, never reused.
    - **Block Ciphers:** Encrypt data in fixed-size blocks. (e.g., AES)
      - **Advanced Encryption Standard (AES):** Block size 128 bits, key sizes 128, 192, or 256 bits.
      - **Block Cipher Modes of Operation** (Encrypted):
        - **ECB (Electronic Codebook):** Encrypts each block independently.
          - Same plaintext blocks → same ciphertext blocks (reveals patterns).
        - **CBC (Cipher Block Chaining):** Each block XORed with previous ciphertext block before encryption, uses IV (Initialization Vector) for first block.
          - Errors in one block affect that block and the next.
        - **CFB (Cipher Feedback):** Turns block cipher into stream cipher, encrypts small parts (like bytes), self-synchronizing.
        - **OFB (Output Feedback):** Similar to CFB but errors do not propagate.
        - **CTR (Counter Mode):** Uses counter + key to generate key stream, allows parallel processing, errors affect only corresponding block.
  - **Hybrid Encryption**: Asymmetric encryption is used to securely exchange a **symmetric key** then, symmetric key is used for fast encryption of data.
  - **Good Hashing Functions**:
    - **Easy to compute**
    -  **Pre-image resistance:** Hard to find a message from a given hash.
    -  **Second pre-image resistance:** Hard to find a different message with the same hash.
    -  **Collision resistance:** Hard to find any two different messages with the same hash.
  - **Common Hashes**:
    - MD5 (128 bits) — outdated, not collision resistant.
    - SHA-1 (160 bits) — weakened, collisions found.
    - SHA-256, SHA-384, SHA-512 — strong and widely used.

  - Hash + secret key = **Message Authentication Code (MAC)** for authentication.
  - **Message Authentication Codes (MAC):** Small piece of data added to message to verify it wasn't changed with a secret key. 
    - **Types of MACs:**
      - **CBC-MAC:** Uses a type of encryption (block cipher) to create the MAC. It looks at the message in blocks and uses the last block as the MAC.
      - **HMAC:** Uses a hash function (like SHA-256) with the secret key to make a secure MAC. This is more common and safer.
---


- **Elliptic Curve Cryptography (ECC)**: A type of public-key cryptography that uses the mathematics of elliptic curves to provide security with smaller key sizes compared to traditional methods like RSA.
- **ElGamal Encryption**: A public-key encryption scheme based on the Diffie-Hellman problem, which allows secure message encryption and decryption using a private key.
- **Public-Key Infrastructure (PKI)**: A system that uses digital certificates by trusted third-party (Certificate Authority or CA) to establish a chain of trust for public keys, ensuring secure communication over networks.
- **TLS (Transport Layer Security)**: A protocol for HTTPS uses PKI and digital certificates that provides secure communication over a computer network, ensuring privacy, integrity, and authentication through the use of public-key cryptography and symmetric encryption.
  - **TLS session key establishment**: Client and server exchange random numbers (nonces) and keys securely, generate shared secret keys, verify the connection, and then communicate safely.
    - K0: Pre-master key (temporary secret)
    - K1: Master secret key (created from K0 and nonces)
    - key: Session key (used to encrypt messages)
    - MAC: A code to check message integrity and authenticity
  - **Double Hashing**: A technique used in TLS to ensure the integrity of the handshake process by hashing the handshake messages twice to prevent tampering.
- **RSA Algorithm**: A widely used public-key cryptosystem that relies on the difficulty of factoring large integers. It is used for secure data transmission and digital signatures.
  - **RSA Padding**: Padding adds randomness to the message before encryption, preventing the same plaintext from producing the same ciphertext when encrypted multiple times.
  - **Homomorphism in RSA** RSA encryption allows **multiplication on ciphertexts**, resulting in multiplication of plaintexts after decryption. This “malleability” can be a risk for attacks but also useful in secure computation.

- **Public-Key Cryptography**
  - **Advantages**: No need to share keys in advance, Supports digital signatures, Provides authenticity and non-repudiation.
  - **Disadvantages**: Slower than symmetric cryptography, Larger ciphertext size, Requires more computation.

- **RSA Key generation**:
- Choose two different large primes (p and q) and compute $n = p \times q$
- Compute $\lambda(n) = \text{lcm}(p-1, q-1) = \frac{(p-1) \times (q-1)}{\text{gcd}(p-1, q-1)}$ 
- Choose $e < \lambda(n)$ and relatively prime to $\lambda(n)$
- Calculate $d = e^{-1} \mod \lambda(n)$
- Public key = $(e, n)$, Private key = $(p, q)$ or $d$
- Encryption $c = m^e \mod n$ and Decryption $m = c^d \mod n$

---

- **DBMS Properties (ACID)**
  - **Atomicity:** Transaction is all or nothing.
  - **Consistency:** Database stays valid.
  - **Isolation:** Transactions don’t interfere with each other.
  - **Durability:** Once done, changes stay even if system crashes.
- **SQL Injection Countermeasures**
  - **Input Validation**: Always check if input is safe.
  - **Sanitization**:
    - **Blacklisting:** Remove dangerous characters like `'`, `;`, `--`.
    - **Escaping:** Replace dangerous characters with safe ones, e.g., `'` → `\'`.
  - **Whitelisting:** Only allow known good input formats.
  - **Prepared Statements:** Use parameterized queries so inputs are never treated as code.

### Server-side attacks

- **HTTP** is **Stateless** (Without memory) $\neq$ Stateful 
  - **Hidden Values**(visible, changable): `<form><input type="hidden" name="**session_id**" value="123456789"></form>`
  - **Capabilities** (Unpredictable tokens): random tokens sent through URLs or headers.
  - **Cookies:** Key-value pairs stored by the browser and sent automatically on each request.
    - **Session Hijacking:** If attacker steals a cookie, they can impersonate the user.
      - Using tools like Firesheep, attackers can steal cookies on insecure Wi-Fi.
    - **Server-Side Defenses for Cookies:**
      - Make cookies expire quickly.
      - Invalidate cookies when user logs out.
      - Use different cookies for each session.
      - Check patterns to detect suspicious behavior.
    - **Cross-Site Request Forgery (CSRF)**: An attack tricking a logged-in user to perform unwanted actions.
      - **Protections:**
        - **Referer Check:** Server checks where the request came from.
        - **Secret Tokens:** Add a secret random token to each form or request that attackers cannot guess.
        - **SameSite Cookie Attribute:** Controls if cookies are sent on cross-site requests.
          - `Strict` = Cookies only sent to same-site requests. (most secure)
          - `Lax` = Cookies sent on top-level navigation (clicking) but not on sub-requests (like images or frames).
          - `None` = Cookies sent always (least secure).

### Client-Side Attacks

- **Same origin policy (SOP)**: Browsers restrict scripts to only access data from the same origin (domain, protocol, port).
example:
- **Cross-site Scripting (XSS)**: Attackers inject malicious scripts into trusted websites, can steal cookies, hijack sessions, or perform other harmful actions.
  - **Persistent XSS:** Code stored on the server (e.g., comments).
  - **Reflected XSS:** Code in URL or form input, reflected immediately in the page response.
---

- **Third-party cookies:** These are cookies set by a domain other than the one you are currently visiting. They are often used by advertisers to track your browsing across different sites.

- **Supercookies:**
  These are special tracking cookies that are harder to delete. Unlike normal cookies, they can be stored in unusual places like HTTP headers or other parts of your device, making them difficult to remove.

- **Evercookies (Zombie cookies):**
  These are even trickier. They store tracking data in many different places (like Flash storage, browser history, HTML5 storage). If you delete the cookie, the website can "resurrect" it using other saved data—like a zombie coming back to life.
- **Tracking URLs**:
Tracking URLs have extra information (parameters) in them to record details like where you clicked the link, how many times, and what you do after clicking. (Like affiliate links that track purchases.)
**Browser Fingerprinting**: 
Websites gather lots of small details from your browser and device (like screen size, fonts installed, browser version, plugins) to create a unique "fingerprint." This fingerprint can identify you without using cookies. Because these details vary from person to person, fingerprinting can uniquely identify millions of users even if cookies are blocked.
- **Corporate Surveillance**: Companies track users extensively, monitoring their behavior, relationships, interests, and even emotional states. 
  - **Data Brokers:** 
  Companies that collect, buy, and sell massive amounts of personal data from various sources, often without your knowledge.
- **Protection Measures Against Tracking**: 
- **Command Injection**: Website lets users run commands on the server without proper checks. (e.g., `nslookup ...; XXX`)
- **Path Traversal**: Users manipulate file paths to access unauthorized files (e.g., `../../etc/passwd`).
- **File Inclusion**: Users can include files from the server or remote locations, potentially executing malicious code (e.g., `index.php?name=http://badsite.com/malicious.php` instead of `http://example.com/index.php?page=about.php`).
---

- **PETs** are tools or methods that let companies or users process data **while keeping the data private and confidential** helping to protect **Personally Identifiable Information (PII)**—like name, address, or phone number—when it is handled by online services.
- **Differential Privacy (DP)**: A **mathematical way** to keep individual data private while still analyzing datasets by adding some “noise” or randomness to the data or output so individual info is hidden. This noise is carefully designed to mask any single individual’s contribution but still give accurate overall results.
    - DP has a **privacy budget** — more queries or more precise answers use up more privacy.
    - There’s a **tradeoff**: stronger privacy means less accurate results, and vice versa.
- **Cryptographic Techniques**
    - **Homomorphic Encryption (HE)**: Allows computations on encrypted data without needing to decrypt it first, so the data remains private during processing. For outsourcing computations to untrusted servers.
    - **Multiparty Computation (MPC)**: Enables multiple parties with no trust to jointly compute a function over their inputs while keeping those inputs private from each other. Trudt distributed, cominication rounds needed. (More efficient than HE but still slower than regular computation.) An example is the Millionaires' Problem, where two parties want to find out who is richer without revealing their actual wealth.
      - **Security Models**: 
        - **Active security (Malicious adversary):** The attacker can cheat or behave arbitrarily.
        - **Passive security (Honest-but-curious adversary):** The attacker follows the protocol but tries to learn extra info.
        - **MPC Techniques**:
          - **Secret Sharing MPC:** Data is split into shares distributed among parties. Addition is easy (done locally) but multiplication needs communication rounds.
          - **Garbled Circuits:** The function is represented as a circuit. One party “garbles” the circuit (encrypts it), and the other party “evaluates” it without learning inputs.

| Type                        | Operations Allowed                   | Number of Operations Allowed |
| --------------------------- | ------------------------------------ | ---------------------------- |
| Partially Homomorphic (PHE) | Only addition or only multiplication | Unlimited                    |
| Somewhat Homomorphic (SHE)  | Both addition and multiplication     | Limited                      |
| Fully Homomorphic (FHE)     | Both addition and multiplication     | Unlimited                    |

- **Real-World Applications**
  - **EPIC (Efficient Private Image Classification)**: Classifying images privately using machine learning (Transfer Learning and MPC) without revealing the images or the model. Faster and more communication-efficient than Gazelle.
  - **Privacy-Preserving Genome-Wide Association Study (GWAS)**: Analyzing genetic data without revealing individual data or exact statistics using HE or MPC.

---

- **chroot** for **sandboxing** changes the app’s "root folder" so it thinks it’s the only thing on the device.
- Modern systems use **containers** (Linux namespaces) for **sandboxing** to isolate apps.
- **Mobile Programming Paradigm**
    - **Event-driven:** Apps respond to things like taps, messages, or network events.
    - **Low resources:** Apps can be paused or killed anytime by the system to save battery or memory.
- **Android App Components**
    - **Activity:** a single screen with UI
    - **Service:** background job
    - **Content provider:** manages app data like databases or files
    - **Broadcast receiver:** listens for system or app messages/events
    - **Manifest:** an XML file describing app parts and permissions
- **Malware spread on mobile methods:**
  - **Repackaging:** legitimate app is modified with malware added.
  - **Fake apps:** pretend to be real apps but are malware.
  - **Update attacks:** app downloads malware after installation.
  - **Malicious websites:** trick users to download malware.
  - **Exploiting vulnerabilities:** gaining root access or spying without user knowledge.
- **Malware functions (payloads):**
  - **Rooting:** gaining full control of the device.
  - **Premium SMS/calls**
  - **Data theft**
  - **Botnets:** using the phone as part of a network for attacks.
  - **Cryptojacking** 
  - **Ransomware:** locking the phone and demanding money to unlock it.

