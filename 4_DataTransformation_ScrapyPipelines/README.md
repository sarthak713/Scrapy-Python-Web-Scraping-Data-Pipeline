### Data Processing Pipelines

- Scrapy not only handles web-scraping but also provides options for actions to perform on extracted data.
    - Data Cleansing
    - Storage

### Scrapy Pipelines

- Pipeline: A chain of one or more data processors
- Processing is applied to each scraped item (RealEstate property, job, image, etc)
- "ImagesPipeline" is an example of built-in pipeline in Scrapy
    - It monitors images_urls list for links. An image is downloaded, resized & saved

#### What can we do with Pipelines?

- Virtually, anything that Python can do to data
- HTML cleansing (can also be done with ItemLoaders)
- Data validation: allow only items with specific feilds (only products with defined prices)
- Data Deduplication: Disallow items with identical fields (titles)
- Saving items to data stores (database, Elastic Search, Kafka, AWS SQS, etc)

##### Crawling click.in 

- [Implemented Here](https://github.com/sarthak713/Scrapy-Python-Web-Scraping-Data-Pipeline/tree/main/projects/classifieds/classifieds)