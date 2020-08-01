import scrapy
from sulekha.items import SulekhaItem

class SulekhaSpiderSpider(scrapy.Spider):
    name = 'sulekha_spider'
    
    start_urls = ['http://events.sulekha.com/new-york-metro-area']

    def parse(self, response):
        item = SulekhaItem()
        rows = response.xpath("//div[@class='col-lg-4 col-md-6 col-sm-6 ACTION-filter']")
        print("Response Type >>> ", type(response))
        # rows = response.css("div.col-lg-4 col-md-6 col-sm-6 ACTION-filter")
        print("Event rows Count >> ", rows.__len__())
        print(rows)
        # print("Response Type >>> ", type(response))
        for row in rows:
            Event_Name = response.css(".event-bd h3 a::text").extract_first()
            Date= response.css(".event-desc span:nth-child(1)::text").extract_first()
            Drama_type = response.css('.venuename::text').extract_first()
            item['Event_Name']=Event_Name
            item['Date'] = Date
            item['Drama_type']=Drama_type
            yield item
















    
        
