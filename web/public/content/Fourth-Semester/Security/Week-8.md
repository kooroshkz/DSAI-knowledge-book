- **Cryptography:** Confidentiality, Authentication, Non-repudiation (Sender cannot deny they sent it)
  - **Symmetric-Key Cryptography**: one shared secret key, faster than public-key but harder to share keys securely.
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

#### Advantages & Challenges of Symmetric Crypto

| Advantages                                  | Challenges                                          |
| ------------------------------------------- | --------------------------------------------------- |
| Fast encryption and decryption              | Hard to distribute and manage keys                  |
| Efficient for hardware and software         | Number of keys grows quickly with users             |
| Provides confidentiality and some integrity | No support for digital signatures (non-repudiation) |

---
| Concept       | Example                                                  |
| ------------- | -------------------------------------------------------- |
| Caesar Cipher | Shift "HELLO" by 3 → "KHOOR"                             |
| One-Time Pad  | Plaintext 0101 XOR key 1010 → ciphertext 1111            |
| CBC Mode      | Plaintext blocks chained with IV and previous ciphertext |
| Hash function | SHA-256("hello") → fixed hash string                     |
| HMAC          | Hash + secret key for message authentication             |