# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import numpy as np


class TestTwoPipeline:
    def process_item(self, item, spider):
        # items = dict(item)
        # title_list = items["title"]
        # context_list = items["context"]
        # np.savetxt("see.txt", title_list, fmt='%s')
        return item
