# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class UnsplashParsingPipeline:
    # Cохраняет полученный item в csv
    def process_item(self, item, spider):
        with open("images.csv", "a") as file:
            file.write(f"{item['title']};{item['category']};{item['url']};{item['path']}\n")
        return item

class PhotosPipeline(ImagesPipeline):
    # Загружает фото с сайта
    def get_media_requests(self, item, info):
        if item["url"]:
            try:
                yield scrapy.Request(item["url"])
            except:
                return "no URL"
    # Прописывает по ключу "path" путь к фото
    def item_completed(self, results, item, info):
        print()
        if results:
            item["path"] = results[0][1]["path"]
        return item