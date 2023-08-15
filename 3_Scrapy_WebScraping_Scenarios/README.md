### Scrapy Web-Scraping Scenarios

- Login to Website
- Changing User-Agents
- Extract data from pages that use AJAX
- Cache extracted data 
- Image Harvesting
- Store images in FTP server or S3 Bucket

---

#### Login To Websites

- [Implemented Here](https://github.com/sarthak713/Scrapy-Python-Web-Scraping-Data-Pipeline/tree/main/projects/quotes/quotes)

---

#### User Agents
- It is one of the headers sent alongside web-requests
- Contains info about the browser
- If web-server detects client is using User-Agent it cannot recognize, it may block the requests
- Check status using Scrapy Shell:
    - ```scrapy shell "linktowebsite"```
    - The status of response may be 403: forbidden
    - ```view(response)```
    - Check user agent in network tab, copy
    - Change User Agent ```scrapy shell -s USER_AGENT="paste user agent" "linktowebsite"```

---

#### AJAX
- Asynchronous JavaScript & XML
    - Used for loading content dynamically after the web page finishes loading
    - JavaScript is used to place the returned content in the pages's HTML


#### Handling Ajax Requests

- [Implemented Here](https://github.com/sarthak713/Scrapy-Python-Web-Scraping-Data-Pipeline/tree/main/projects/naukri/naukri)

---

#### Caching Responses

- When a project scrapes website containing thousands of pages, it doesn't make sense to scrape each and every page again.
- If Scrapy knows that a page has been  visited & data has been extracted, this will save time and network bandwidth.
- Go to ```settings.py```, to the bottom
    - Uncomment all fields
    - Caching is disabled by default in scrapy projects, caching enables scrapy to save crawled pages, so when page is encountered again it refers to cached version instead of re-downloading
- Fields:
    - HTTPCACHE_ENABLED = True
    - HTTPCACHE_EXPIRATION_SECS = 1000 (defines how long scrapy considers the cache as valid before attempting to redownload)
    - HTTPCACHE_DIR = 'httpcache' where data is saved

---

#### Image Harvesting
##### Using Scrapy's image pipeline to download & process images from web pages

- [Implemented Here](https://github.com/sarthak713/Scrapy-Python-Web-Scraping-Data-Pipeline/tree/main/projects/freeimages/freeimages)

1. Plain Python:
    - Get image URL using Xpath
    - Download image using Requests or similar module
2. Scrapy's Images Pipeline:
    - Automatic thumbnail creation (useful for preparing data from ML models)
    - Only downloaded images with minimum dimensions (saves you a data cleansing step)
    - Set expiration date for images to be redownloaded (useful when working with a constantly changing source)
    - Downloads images in parallel to speed the process

---