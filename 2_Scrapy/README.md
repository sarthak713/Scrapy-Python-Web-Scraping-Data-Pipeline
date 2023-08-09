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

- Scrapy has its own interactive shell
- Check Scrapy: ```scrapy```
- Start Scrapy shell: ```scrapy shell "https://www/realtor.com"```
    - HTTP get request is sent to website
    - Response object is stored as response
    - Request parameters are stored in request object
    - An interactive shell is opened where response & request objects are available
- Get HTML content: ```response.body```
- Read HTML content using browser: ```view(response)```
- Get HTTP status code: ```response.status```
- Get HTTP headers: ```response.headers```
- Get Request headers: ```request.headers```
- Get Cookies: ```request.cookies```
- Exit Scrapy shell: ```exit()```

---

### Scrapy Project

1. Create Virtual Environment: ```python3 -m venv env_name```
    - cd inside venv folder
    - Activate: ```source bin/activate```
2. Install Scrapy: ```pip install scrapy```
3. Create Scrapy Project: ```scrapy startproject project_name```

#### Folder Structure

- spiders directory
    - This is where code is written to scrape websites
    - This is a directory (not a single file), indicating we can use more than 1 spider in a project
- The __init__.py files are needed by Scrapy to operate properly
- settings file is for configuring how spiders look & behave
- items.py defines items to be scraped, this has all fields that we need to extract from website
- middlewares.py (middleware works on data moving in pipeline), this file is used to defines logic to apply on data before going to website or how data coming from website should be processed before saving. 
- pipelines.py is used to define how & where to save extracted data

---

### Scrapy Spider

- Way 1: Create a new file in spiders directory
- Way 2: Use command ```scrapy genspider spider_name domain_name```
- Run Spider ```scrapy crawl spider_name```
- Store Data ```scrapy crawl spider_name -O filename.csv```

---

### Item Loaders

- Item = Data Container
- An item can be filled like a regular Python dictionary. 
    - Example: item['price]=listing.xpath('.//div[@class="si-listing__photo-price"]/span/text()').get()
- ItemLoader = Built-in Scrapy class that can modify data recieved from the spider using Input & Output Processors
- Input Processor   
    - works on data as it gets recieved from the spider
    - Example: removing whitespace & useless characters from data
- Output Processor   
    - works on data before it gets saved
    - Example: data structuring
- Used to extract and transform data from web pages in real time

---

### Spiders

- The Spider class we inherit our basic spider from is Base Class for other more complex spiders
- It can do basic web scraping stuff
- Scrapy provides other child spiders to provide more Specific logic: XML feed spider, CSV feed, sitemap, crawl spider

- Crawl spider follows links
    - Just provide url of start page & it starts following all links
    - Whenever it gets the HTML of a page, it is passed to a callback function to extract the required data from the page.
    - For this spider to work, it needs to be confined by some rules or it will continue crawling links indefinitely

---