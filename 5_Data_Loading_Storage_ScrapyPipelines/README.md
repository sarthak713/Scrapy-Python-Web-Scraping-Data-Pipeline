### Data Loading (Storage) using Scrapy's Pipelines

- How to store data to MongoDB/MySQL databases
- How to store sensitive information like database username & password in Vault & how to use that along with Scrapy
- How to store data to data-lake like AWS S3 buckets 
- How to query this data in place using Amazon Athena and AWS Glue

---

#### MongoDB

- A NoSQL Database Engine
- SQL Databases: MySQL, Microsoft SQL Server, Oracle, etc
- NoSQL Databases don't have relations betweeb tables
- They are suitable for storing unstructured data (like web-scraped data)
- If data is in-consistent:
    - Use Pipelines to drop data that do not contain all needed fields
    - Dropping data should be your last resort in data engineering/ML world
    - Use a NoSQL database where items with different Schemas can be stored
- Use pymongo package

---