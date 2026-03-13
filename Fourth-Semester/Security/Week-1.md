# Introduction to Information Security

## **Basic Security Principles - CIA Triad**
1. **Confidentiality**: Restricting unauthorized access and disclosure.
2. **Integrity**: Ensuring data is not altered or tampered with.
3. **Availability**: Ensuring information is accessible when needed.

## **Additional Security Goals**
- **Authenticity**: Ensuring data or identity is genuine.
- **Authentication**: Verifying user/system identity.
- **Authorization**: Ensuring only permitted entities access resources.
- **Accuracy**: Ensuring information is correct for its purpose.
- **Accountability**: Tracing actions back to responsible entities.
- **Non-Repudiation**: Preventing denial of performed actions.
- **Privacy**: Controlling access to personal or sensitive information.

## **Key Definitions**
- **Computer Security (COMPUSEC)**: Protection of computer assets (hardware, software, data).
- **Information Systems Security (INFOSEC)**: Safeguarding data from unauthorized access and attacks.
- **Information Security**: Protecting data and systems from threats while ensuring CIA principles.

## **Threats, Vulnerabilities, and Risks**
- **Asset**: Anything valuable to an organization (e.g., data, hardware, people).
- **Vulnerability**: A weakness that could be exploited.
- **Threat**: A potential cause of security harm.
- **Risk**: The potential impact of an exploited vulnerability.
  - **Risk = Impact of Exploitation × Likelihood of Exploitation**
  - Risk is mitigated using security **countermeasures**.

## **Security Controls (Countermeasures)**
|                          | Physical            | Logical/Technical            | Administrative/Policies          |
|--------------------------|--------------------|-----------------------------|----------------------------------|
| **Preventive (+deterrence)** | Security guard    | Firewall                    | Employee screening policy       |
| **Detective**            | Security camera    | Intrusion detection system  | Policy to review transaction logs |
| **Corrective/Responsive**| Fire sprinklers    | Backup servers              | Law enforcement liaison         |

## **Attack Types and Security Requirements**
| **Attack/Threat** | **Violated Security Requirement** |
|-------------------|--------------------------------|
| Spoofing | Authenticity |
| Tampering | Integrity |
| Repudiation | Non-repudiation |
| Information Disclosure | Confidentiality |
| Denial of Service (DoS) | Availability |
| Elevation of Privilege | Authorization |

## **Security Trade-offs (Security Dilemmas)**
1. Users want security but lack expertise.
2. Security vs. usability – complex security is often bypassed.
3. Security is costly with no direct gain, only prevention.
4. Sometimes failure costs less than implementing security.
5. Theoretical security does not always align with practical security.
6. Increased security **adds system complexity**, increasing attack surfaces.

---

## **Trust in Security**
- **Trusted Component**: A system part we rely on but might not fully verify.
- **Trusted Computing Base (TCB)**: The minimal set of components that must be trusted.
- **Minimizing Trust**:
  - Reduce the number of **trusted** components.
  - Design systems to **require minimal trust**.
  - Verification increases **trustworthiness**.
