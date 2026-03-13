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