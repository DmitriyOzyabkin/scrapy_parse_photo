import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from items import UnsplashParsingItem


class UnsplashcomSpider(scrapy.Spider):
    name = "unsplashcom"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]

    # Получает список категорий на unsplash.com и гунерирует ответ по каждой из категорий
    def parse(self, response:HtmlResponse):
        categories = response.xpath("//a[contains(@href, '/t/')]//@href").getall()
        for category in categories:
            yield response.follow(url=category, callback=self.parse_category)

    # Получает список фотографий в категории и гунерирует ответ по каждой из фотографий
    def parse_category(self, response:HtmlResponse):
        photos = response.xpath("//figure//a[@itemprop='contentUrl']//@href").getall()
        for photo in photos:
            yield response.follow(url=photo, callback=self.parse_photo)

    # Получает со странички данные о фотографии и возвращает объек для создания item
    def parse_photo(self, response:HtmlResponse):
        loader = ItemLoader(item=UnsplashParsingItem(), response=response)
        loader.add_xpath('title', "//h1/text()")
        loader.add_xpath("category", "//a[@class='ZTh7D kXLw7']/text()")
        loader.add_xpath("url", "//img[contains(@sizes, 'min')]//@srcset[1]")
        return loader.load_item()



    
