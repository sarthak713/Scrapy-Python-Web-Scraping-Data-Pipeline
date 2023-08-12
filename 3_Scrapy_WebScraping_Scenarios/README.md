### Scrapy Web-Scraping Scenarios

- Login to Website
- Changing User-Agents
- Extract data from pages that use AJAX
- Cache extracted data 
- Image Harvesting
- Store images in FTP server or S3 Bucket

---

#### Login To Websites
- Done in 2_Scapy module in 'quotes project'

---

#### User Agents
- One of the headers sent alongside web-requests
- Contains info about the browser
- If web-server detects client is using User-Agent it cannot recognize, it may block the requests
- Check status using Scrapy Shell:
    - ```scrapy shell "linktowebsite"```
    - ```view(response)```
    - Check user agent in network tab, copy
    - ```scrapy shell -s USER_AGENT="paste user agent" "linktowebsite"```

---