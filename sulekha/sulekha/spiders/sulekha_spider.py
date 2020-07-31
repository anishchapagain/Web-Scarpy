import scrapy
from sulekha.items import SulekhaItem

class SulekhaSpiderSpider(scrapy.Spider):
    name = 'sulekha_spider'
    # allowed_domains = ['http://us.sulekha.com/']
    start_urls = ['http://events.sulekha.com/new-york-metro-area']

    def parse(self, response):
        item = SulekhaItem()
        print("Response Type >>> ", type(response))
        print("Response Type >>> ", type(response))
        # item['title'] = response.css(".titlebg h2::text").extract()
        item['Event_Name'] = response.css(".event-bd h3 a::text").extract()
        item['Date'] = response.css(".event-desc span:nth-child(1)::text").extract()
        item['Drama_type'] = response.css('.venuename::text').extract()
        yield item
        # rows = response.xpath("//div[@class='col-lg-4 col-md-6 col-sm-6 ACTION-filter']")
        # print("Event rows Count >> ", rows.__len__())
        # for row in rows:
        #     item = SulekhaItem()
      
            # item['Event_Name'] = row.xpath("//aside[@class='event-container']/section[@class='event-bd']/h3/a/text()")[0].extract()
            # item['Event_day'] = row.xpath("//aside[@class='event-container']/section[@class='event-bd']/article[@class='event-desc clearfix']/div[@class='caldr ftlt']/span[@class='day']/text()[1]")[0].extract()
            # item['Event_month'] = row.xpath("//aside[@class='event-container']/section[@class='event-bd']/article[@class='event-desc clearfix']/div[@class='caldr ftlt']/span[@class='month']/text()")[0].extract()
            # item['Date'] = row.xpath("//aside[@class='event-container']/section[@class='event-bd']/article[@class='event-desc clearfix']/div[@class='locwrp']/span[@class='times']/text()[1]")[0].extract()
            # item['Drama_type'] = row.xpath("//aside[@class='event-container']/section[@class='event-bd']/article[@class='event-desc clearfix']/div[@class='locwrp']/span[@class='venuename']/text()")[0].extract()
            # yield item
















    
        
