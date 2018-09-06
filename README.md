
#### 反爬处理


1.随机 User_Agent:

    settings.py
    -----------
        DEFAULT_REQUEST_HEADERS = {
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en',
           'User-Agent':random.choice(USER_AGENTS),
           'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
        }


2.代理IP:
#### ip_proxy: 获取代理ip (http://www.xicidaili.com/)
    现在只是爬取一个网站,后期将该成多个网站


#### Random proxy middleware for Scrapy  使用代理爬取
    这里自己修改了一下 将RandomProxy直接放到了middlewares.py中,
    源码安装方法(https://github.com/aivarsk/scrapy-proxies)

    settings.py
    -----------

        # Retry many times since proxies often fail
        RETRY_TIMES = 10
        # Retry on most error codes since proxies fail for different reasons
        RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

        DOWNLOADER_MIDDLEWARES = {
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
            'scrapy_proxies.RandomProxy': 100,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
        }

        # Proxy list containing entries like
        # http://host1:port
        # http://username:password@host2:port
        # http://host3:port
        # ...
        PROXY_LIST = './zhihuuser/ip_proxy/proxies.txt' #文件路径

        # Proxy mode
        # 0 = Every requests have different proxy  每个请求都使用不同代理
        # 1 = Take only one proxy from the list and assign it to every requests 使用一个代理访问所有请求
        # 2 = Put a custom proxy to use in the settings  自定义指定一个代理
        PROXY_MODE = 0

        # If proxy mode is 2 uncomment this sentence :
        #CUSTOM_PROXY = "http://host1:port"

    For older versions of Scrapy (before 1.0.0) you have to use
    scrapy.contrib.downloadermiddleware.retry.RetryMiddleware and
    scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware
    middlewares instead.


    Your spider
    -----------

    In each callback ensure that proxy /really/ returned your target page by
    checking for site logo or some other significant element.
    If not - retry request with dont_filter=True

        if not hxs.select('//get/site/logo'):
            yield Request(url=response.url, dont_filter=True)




#### scrapy-redis 实现分布式

    settings.py
    -----------

        ITEM_PIPELINES = {
           'zhihuuser.pipelines.MongoPipeline': 300,     #数据持久化(入库)
           'scrapy_redis.pipelines.RedisPipeline': 301,
        }
    
        #分布式 调度器
        SCHEDULER = "scrapy_redis.scheduler.Scheduler"
        #去重
        DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    
        REDIS_URL = 'redis://root:1234@192.168.30.11:6379/1' #有密码
        # REDIS_URL = 'redis://192.168.30.11:6379/1'  #无密码





