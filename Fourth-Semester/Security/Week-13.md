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