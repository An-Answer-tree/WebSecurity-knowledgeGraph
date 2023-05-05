import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..items import TestOneItem


class SecrssSpider(scrapy.Spider):
    name = "secrss"
    allowed_domains = ["www.secrss.com"]
    start_urls = ["https://www.secrss.com/articles?tag=网络攻击"]
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.start_urls[0])
        # i = 0
        while True:
            try:
                more_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[@class="more-button"]')))
                more_button.click()
                # i += 1
                time.sleep(3)                
                # if i == 2:
                #     break
            except:
                break
        self.links = []
        sel = Selector(text=self.driver.page_source)
        # 在页面上查找需要的数据
        self.links = sel.xpath('//h2/a/@href').extract()
        new_links = []
        for link in self.links:
            # 如果链接不是以'http'或'https'开头，则添加主网址
            if not link.startswith('http'):
                link = "https://www.secrss.com" + link
            new_links.append(link)

        # 将新的链接列表赋值给 self.links
        self.links = new_links
            
    def parse(self, response):
        url = self.links
        
        yield {
            'url': url
        }
        

    def closed(self, reason):
        self.driver.quit()
    
    # def parse(self, response):
        # items=TestOneItem()
        # lists=response.xpath('//h2/a/@href').extract()
        # items["url"] = lists

        

