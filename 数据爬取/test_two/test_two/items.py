# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestTwoItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()   # 字典，内容为一个列表，列表中有一个字符串
    context = scrapy.Field() # 字典，内容为一个列表，列表中有许多字符串
    pass
