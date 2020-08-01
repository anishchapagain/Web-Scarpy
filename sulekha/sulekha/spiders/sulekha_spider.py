import scrapy
from sulekha.items import SulekhaItem
#position-8 > aside > section > article.event-desc.clearfix > div.locwrp > span.venuename > a

class SulekhaSpiderSpider(scrapy.Spider):
    name = 'sulekha_spider'
    
    start_urls = ['http://events.sulekha.com/new-york-metro-area']

    def parse(self, response):
        rows = response.xpath("//div[@class='col-lg-4 col-md-6 col-sm-6 ACTION-filter']")
        # rows = response.xpath("//div[@class='eventwarp clearfix']")
        print("Response Type >>> ", type(response))
        # rows = response.css("div.col-lg-4 col-md-6 col-sm-6 ACTION-filter")
        print("Event rows Count >> ", rows.__len__())
        print(rows)
        # print("Response Type >>> ", type(response))
        item = SulekhaItem()
        for row in rows:
            item = SulekhaItem()
            print("#"*50)
            print(row)
            # Event_Name = response.xpath('//*[@id="position-1"]/aside/section/h3/a/text()').extract_first()
            item['Event_Name'] = response.css(".event-bd h3 a::text").extract()
            # Date = response.xpath('/html/body/div[4]/section[1]/div/article/article/div[1]/aside/section/article[1]/div[2]/span[1]/i').extract()
            item['Date']= response.css(".event-desc span:nth-child(1)::text").extract()
            # Drama_type = response.xpath('//*[@id="position-1"]/aside/section/article[1]/div[2]/span[2]/i/text()').extract()
            item['Title'] = response.css('.venuename , .venuename a').css('::text').extract()
            # item['Event_Name']=Event_Name
            # item['Date'] = Date
            # item['Title']=Title
        yield item
















    
        
