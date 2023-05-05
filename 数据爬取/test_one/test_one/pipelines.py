# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import numpy as np


class TestOnePipeline:
    def process_item(self, item, spider):
        result = np.array(dict(item)['url'])
        print(type(result))
        np.savetxt("../result.csv", result, delimiter=',', fmt='%s')
        
        return item
