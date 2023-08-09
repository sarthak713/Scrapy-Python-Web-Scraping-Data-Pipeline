import scrapy
from real_estate.items import RealEstateItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# class ListingsSpider(scrapy.Spider):
class ListingsSpider(CrawlSpider):
    name = 'listings'
    allowed_domains = ['arizonarealestate.com']
    # start_urls = [
    #     'https://www.arizonarealestate.com/maricopa/',
    #     'https://www.arizonarealestate.com/goodyear/',
    #     'https://www.arizonarealestate.com/tempe/'
    # ]
    start_urls = [
        'https://www.arizonarealestate.com'
    ]
    # Rules for Crawl Spider
    rules = (
        # can contain main params
        Rule(
            # logic: limit link extraction to only that part of page defined by one or more XPath queries
            LinkExtractor(restrict_xpaths=(
                "//section[@class='section-city-list']"
            )),
            # logic that needs to be applied on the page that each link will get
            callback="parse",
            follow=True
        ),
    )

    def parse(self, response):
        gallery = response.xpath('//div[@class="si-listings-column"]')
        for listing in gallery:
            # item = RealEstateItem()
            item = ItemLoader(item = RealEstateItem(), response = response, selector = listing)
            # item['name'] = listing.xpath('.//div[@class="si-listing__title-main"]/text() | .//div[@class="si-listing__neighborhood"]/span[@class="si-listing__neighborhood-place"]/text()').getall()
            item.add_xpath('name', './/div[@class="si-listing__title-main"]/text()')
            item.add_xpath('name', './/div[@class="si-listing__neighborhood"]/span[@class="si-listing__neighborhood-place"]/text()')
            item.add_xpath('description','.//div[@class="si-listing__info"]//div[@class="si-listing__info-label"]/text()')
            item.add_xpath('description','.//div[@class="si-listing__info"]//div[@class="si-listing__info-value"]/descendant::*/text()')
            item.add_xpath('price','.//div[@class="si-listing__photo-price"]/span/text()')
            item.add_xpath('agency','.//div[@class="si-listing__footer"]/div/text()')
            # yield item
            yield item.load_item()
            # pagination handling
            next_page = response.xpath('//a[@class="js-page-link"]/@href').get()
            if next_page:
                yield response.follow(next_page, callback = self.parse)
