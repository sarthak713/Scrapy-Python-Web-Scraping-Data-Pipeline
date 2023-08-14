import scrapy


class RemoteJobsSpider(scrapy.Spider):
    name = 'remote_jobs'
    allowed_domains = ['naukri.com']
    start_urls = ['http://naukri.com/']

    def parse(self, response):
        pass
