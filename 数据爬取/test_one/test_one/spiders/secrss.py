import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class SecrssSpider(scrapy.Spider):
    name = "secrss"
    allowed_domains = ["www.freebuf.com"]
    start_urls = ["https://www.freebuf.com/search?search=攻击"]
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.start_urls[0])
        i = 2
        while True:
            # try:
            xpath = '//li[@title="' + str(i) + '"]/a'
            # 新增 爬取链接
            self.links = []
            sel = Selector(text=self.driver.page_source)
            # 在页面上查找需要的数据
            self.links.extend(list(sel.xpath('//a[@class="text text-line-2"]/@href').extract()))
            # time.sleep(0.5)  
                
            # 翻页
            element = self.driver.find_element(By.XPATH, xpath)
            self.driver.execute_script("arguments[0].click();", element)

            
            # more_button = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, '//li[@title="2"]')))
            # more_button.click()
            i += 1
            time.sleep(0.5)                
            if i == 3:
                break
            # except:
            #     break        
            
        # 将新的链接列表赋值给 self.links
        new_links = []
        for link in self.links:
            # 如果链接不是以'http'或'https'开头，则添加主网址
            if not link.startswith('http'):
                link = "https://www.freebuf.com" + link
            new_links.append(link)
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

        

