import scrapy
from scrapy import Request, FormRequest


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def parse_login(self, response):
        ret = FormRequest.from_response(response, formdata={"username":"sarthak","password":"mypass"})
        self.log("Sent: "+str(ret.body))
        return ret

    # instructing scrapy to visit login page first, this func returns list of requests
    def start_requests(self):
        return [Request("http://quotes.toscrape.com/login", callback=self.parse_login)]
    
    def parse(self, response, **kwargs):
        pass