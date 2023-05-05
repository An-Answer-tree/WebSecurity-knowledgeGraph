import scrapy
import numpy as np
from ..items import TestTwoItem


class ContextSpider(scrapy.Spider):
    name = "context"
    allowed_domains = ["www.freebuf.com"]
    # 从CSV文件中读取数据
    data = np.genfromtxt('../../test_one/result.csv', delimiter=',', dtype=str)

    # 获取包含所有字符串的列表
    string_list = data.tolist()
    # print('-----------------------------------------------------------------------')
    # print(type(string_list[0]))
    start_urls = string_list
    # start_urls = ['https://www.freebuf.com/articles/network/364616.html']
    
    def parse(self, response):
        item = TestTwoItem()
        # 存储标题
        item["title"] = response.xpath('//span[@class="title-span"]/text()').extract()
        
        # 存储内容
        res_list = list(response.xpath('//div[@class="content-detail"]//text()').extract())
        new_str = ''
        for i in res_list:
            new_str += i
        item["context"] = new_str
        
        yield item
    
