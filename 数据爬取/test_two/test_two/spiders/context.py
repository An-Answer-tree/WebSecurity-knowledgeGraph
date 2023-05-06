import scrapy
import numpy as np
from ..items import TestTwoItem


class ContextSpider(scrapy.Spider):
    name = "context"
    allowed_domains = ["www.secrss.com"]
    # 从CSV文件中读取数据
    data = np.genfromtxt('../../test_one/result.csv', delimiter=',', dtype=str)

    # 获取包含所有字符串的列表
    string_list = data.tolist()
    start_urls = string_list

    def parse(self, response):
        item = TestTwoItem()
        # 存储标题
        item["title"] = response.xpath('//h1//text()').extract()
        
        # 存储内容
        list = response.xpath("//div[@class='article-body']/p//text()").extract()
        item["context"] = list
        
        
        # 存储内容
        res_list = list(response.xpath('//div[@class="article-body"]/p//text()').extract())
        new_str = ''
        for i in res_list:
            new_str += i
        item["context"] = new_str
        
        yield item
    
