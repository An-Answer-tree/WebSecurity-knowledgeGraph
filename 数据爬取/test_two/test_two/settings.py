# Scrapy settings for test_two project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "test_two"

SPIDER_MODULES = ["test_two.spiders"]
NEWSPIDER_MODULE = "test_two.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "test_two (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Cookie': 'Hm_lpvt_75bd0223beb9520a49897a3bfbefa004=1682329590; Hm_lvt_75bd0223beb9520a49897a3bfbefa004=1682318551,1682318588; XSRF-TOKEN=eyJpdiI6IitjSStEdVZ0QlZ3ZklHT3NTRHd6S0E9PSIsInZhbHVlIjoicWNGVExIblNcLzR2WnRuVXVUSVJRRjM3OCtNaGdCU1ZaVWdiZEFaOHdaQWR2dmNYRzVoUXpxTUtpQkcrRFZlYjUiLCJtYWMiOiJhZmJjMWEyNmM1NWRkZGMxYzAxYjQ0NjY2NjZmODRjNjJkMWZkNTJmMjFjMWEwMjlkZWEzODMxYTYzYmRlZDEzIn0%3D; _session=eyJpdiI6IkNJNXJWTDc1MEg5OWt1OEhEV2dycnc9PSIsInZhbHVlIjoieE1kcllFQjR1UDNxV3NqUGZFUG5NU2x0ejdMa2NzcmxvbGdDZDJyTTRhZDF3cnJjXC9yb1BaVGwwSk42R2w4aFkiLCJtYWMiOiI0YTI1NDM3Yjk4ZDVmMTI3NTVlYTg4ZTkzMzYwMjg0YTE1ZDYwZjAyMzczMmY2NzViYWNlZTlkNzQzMDFhM2NmIn0%3D; wzws_sessionid=gDExMi40LjE3Ny4yMTGBMzBjMDMwgjVlYmNiZKBkRiWi',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.secrss.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Referer': 'https://www.secrss.com/articles?tag=%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB',
    'Connection': 'keep-alive'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "test_two.middlewares.TestTwoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "test_two.middlewares.TestTwoDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "test_two.pipelines.TestTwoPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
