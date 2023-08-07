### What is a Web Bot?

- We navigate website through browsers
- But we may not recieve same HTML/HTTP response as we get in a browser
- This is because not all websites like accessing them through bots, so they take measures to prevent this:
    - give different response
    - use captcha code/image
- Making it difficult for computer programs (web bots) to recognize and solve
    - Some web servers return 403 & deny access with no Captcha challenge
    - Some will totally restrict access to IP address the bot is using (for a temprary period)

### Is using a Web Bot legal/ethical ?

- Depends on how you use the bot & scraped data for
- Website ban bots because:
    - Bots can be used to scan websites for vulnerabilities & may launch cyber attacks
    - They can start Denial of Service (DoS) attacks by sending many requests at the same time & the website comes down
    - Web Servers cannot easily determine if bot is malicious or ligitimate. So they ban all bots as a safety measure

---

### The Scrapy Shell

- Scrapy has its own ineractive shell