# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose


# Преобразует строку со сслыками на фотографии различного разрешения, 
# выделяя первую ссылку.  
def process_url(value:list):
    return value[0].split(',')[0].split()[0]


class UnsplashParsingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field()
    url = scrapy.Field(output_processor=Compose(process_url))
    path = scrapy.Field()

