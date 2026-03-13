## Standards and Frameworks

- **ISO/IEC 27000 series:** Info security management standards.
- **ISO 31000:** Risk management Process.
 - Identify vulnerabilities and threats $\to$ select tools, techniques $\to$ assess risk $\to$ decide strategies $\to$ consider countermeasures.
- **NIST 800-30:** Guide for risk assessments.
- **NIST 800-53:** Security and privacy controls.
- **ISACA COBIT:** IT systems management framework.

---

## Principles and Best Practices

### Design Principles

- **Separation of Duties (SoD):** Avoid conflicts by dividing tasks among different people (e.g., one person creates users, another approves).
- **Least Privilege:** Give users only the access they need, no more.

## Risk Management Methods

- **Tabular methods:** Popular in industry (tables showing risks and controls).
- **Graphical methods:** More academic (diagrams, charts).

---

## Threat Modeling: STRIDE Framework

| Threat                      | Concern                      | Countermeasures                                          |
| --------------------------- | ---------------------------- | -------------------------------------------------------- |
| **Spoofing**                | Can you trust the identity?  | Authentication, session management, digital certificates |
| **Tampering**               | Can data be changed?         | Digital signatures, access control, auditing             |
| **Repudiation**             | Can actions be denied?       | Logging, auditing, digital signatures                    |
| **Information Disclosure**  | Risk of data theft?          | Access control, encryption                               |
| **Denial of Service (DoS)** | Prevent service access?      | Rate limiting, boundary protection, redundancy           |
| **Elevation of Privilege**  | Unauthorized privilege gain? | Authorization, least privilege, input validation         |

## STRIDE Threat Modeling Steps

1. Define key assets and security needs.
2. Create data flow diagrams (DFDs).
3. Draw trust boundaries (zones with different trust levels).
4. Identify threats crossing these boundaries.
5. Plan controls to mitigate threats.
6. Validate controls work.