import scrapy
from scrapy.linkextractors import LinkExtractor

class Spider103Spider(scrapy.Spider):
    name = 'spider103'
    allowed_domains = ['http://cppcl.property.hk']
    start_urls = ['http://cppcl.property.hk/tran_prop.php']
    rules =  (Rule(LinkExtractor(allow=(), restrict_xpaths=('//b',)), callback="parse", follow= True),)

    def parse(self, response):
        trs = response.xpath(
            "//td[3][@height='28']/text()").getall()
        # "//tr[@bgcolor='#E6FAFF' or @bgcolor='#CAF3FF']//td[3]/text()")
        #for tr in trs:
        #print (tr.get())
        for each in trs:
            print(each)

    next_page = response.css('li.next a::attr(href)').get()
    if next_page is not None:
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)