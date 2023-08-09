# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# use one or more function for data in items
from scrapy.loader.processors import MapCompose, Join

# input processor function
def description_in(d):
    return d.strip()

# output processor function
def description_out(d):
    labels = d[0:3]
    values = d[3:]
    output={
        labels[0]: "".join(values[0]),
        labels[1]: " ".join(values[1:-1]),
        labels[2]: "".join(values[-1])
    }
    return output

class RealEstateItem(scrapy.Item):
    name = scrapy.Field(output_processor=Join())
    description = scrapy.Field(input_processor=MapCompose(description_in),output_processor=description_out)
    price = scrapy.Field(output_processor=Join())
    agency = scrapy.Field(output_processor=Join())