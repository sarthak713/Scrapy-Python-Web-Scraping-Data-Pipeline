import scrapy
from freeimages.items import FreeimagesItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor


class ImagesSpider(CrawlSpider):

    def __init__(self, *a, **kw):
        super(ImagesSpider,self).__init__(*a, **kw)
        self.category=[kw.get('category')]
        self.start_urls=[f"https://www.freeimages.com/search/{self.category}"]

    name = 'images'
    allowed_domains = ['freeimages.com']
    # start_urls = ['http://freeimages.com/search/cat']
    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=(
                '//div[contains(@class,"masonry-container")]'
            )),
            callback="parse",
            follow=False
        ),
    )

    def parse(self, response):
        item=ItemLoader(item=FreeimagesItem(),response=response,selector=response)
        item.add_xpath("image_urls","//div[@id='photo-wrapper']/img[@id='photo']/@src")
        yield(item.load_item())
