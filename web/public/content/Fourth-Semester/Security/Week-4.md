- **OSI Model** has **7 layers** (from top to bottom):
  - **1) Application** (user interface, e.g. browsers, email)
    - HTTP (web pages)
    - SMTP (email)
    - DNS (domain name system)
  - **2) Presentation**: Handles how data is formatted or encrypted so both ends understand each other.
    - Telnet (remote terminal)
    - FTP
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

---

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

---

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