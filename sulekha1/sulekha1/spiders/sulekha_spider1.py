import scrapy
from sulekha1.items import Sulekha1Item

class SulekhaSpider1Spider(scrapy.Spider):
    name = 'sulekha_spider1'
    # allowed_domains = ['us.sulekha.com']
    # start_urls = ['http://indianroommates.sulekha.com/rentals_in_new-york-metro-area']
    start_urls = ['http://indianroommates.sulekha.com/rentals_in_new-york-metro-area']

    page_number = 2
    def parse(self, response):
        items=Sulekha1Item()
        print("Response Type >>> ", type(response))
        rows = response.xpath("//div[@about='#offering']")
        print("Event rows Count >> ", rows.__len__())
        for row in rows:
            roomtitle=row.css(".roomtitle a::text").extract()
            Available_From=row.css(".renlistview1373907 span:nth-child(4) em , .avlfrm b").css("::text").extract()
            post_by=row.css("small+ span::text").extract()
            location=row.css("figure+ .room-location , .room-location:nth-child(1) , #city4 , .renlistview1374405 .avlfrm b").css("::text").extract()
            rental=row.css("span:nth-child(2) a").css("::text").extract()
            bedrooms=row.css("span~ span+ span a").css("::text").extract()
            bathrooms=row.css("span:nth-child(4) b").css("::text").extract()
            size=row.css(".renlistview1373810 .room-location+ .room-location , span:nth-child(5) b").css("::text").extract()
            description=row.css("p::text").extract()
            
            # yield {"roomtitle":roomtitle,"Available_From":Available_From,"post_by":post_by,"location":location,"rental":rental,"bedrooms":bedrooms,"bathrooms":bathrooms,"size":size,"description":description}
            items['roomtitle']=roomtitle
            items['Available_From']=Available_From
            items['post_by']=post_by
            items['location']=location
            items['rental']=rental
            items['bedrooms']=bedrooms
            items['size']=size
            items['description']=description
            yield items
            # nextPage = row.css(".active a::attr(href)").extract_first()
        next_page='http://indianroommates.sulekha.com/rentals_in_new-york-metro-area_'+str(SulekhaSpider1Spider.page_number)
        print("*"*50)
        print(next_page)
        if SulekhaSpider1Spider.page_number <=6:
            SulekhaSpider1Spider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
            # nextPage = row.xpath("//div[@class='pagination margin20b']/ul//li[@class='active']/a/@href").extract_first()
            # print(nextPage)
            # if nextPage:
                # print("Next Page URL: ",nextPage)
                #nextPage obtained from either XPath or CSS can be used.
                # yield scrapy.Request('http://indianroommates.sulekha.com'+str(nextPage),callback=self.parse)
                # print('Completed')
        




        # for row in rows:
        #     item = Sulekha1Item()
        #     item['offer']=row.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "roomtitle", " " ))]//a/text()').extract()
        #     # item['offer'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/h3[@class='roomtitle']/a/text()").extract()
        #     item['room_location'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='room-location']/text()").extract()
        #     item['post_hr'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='room-location']/small/text()").extract()
        #     item['post_by'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='room-location']/span/text()").extract_first()
        #     # item['post_by'] =row.xpath('//small+//span').extract_first()
        #     ## item['Available_From'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='room-location']/span[@class='avlfrm']/text()").extract()
        #     # item['Ad_Type'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/iv[@class='clearfix']/div[@class='part-detail']/div[@class='part-info']/div[@class='mobilescroll']/span/b/a/text()").extract()
        #     item['Rental'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='part-detail']/div[@class='part-info']/div[@class='mobilescroll']/span/b/a/text()").extract()
        #     # item['bedrooms'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='part-detail']/div[@class='part-info']/div[@class='mobilescroll']/span/b/a/text()").extract()
        #     # item['Bedrooms'] = row.xpath("//span~//span+//span//a/text()").extract()
        #     # item['bathrooms'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='part-detail']/div[@class='part-info']/div[@class='mobilescroll']/span/b/a/text()").extract()
        #     # item['sizes_sqft'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/div[@class='part-detail']/div[@class='part-info']/div[@class='mobilescroll']/span/b/a/text()").extract()
        #     item['Details'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/p[@id='desc1']/text()").extract()
        #     item['prize_per_month'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-rt']/div[@class='card-price']/div[@id='price1']/em[@class='possession']/text()").extract()
        #     item['University_nearby'] =row.xpath("//div[@class='listing-detail-wrp clearfix']/div[@class='listing-detail-lt']/div[@class='listing-detail']/div[@class='clearfix']/p[@class='univer-link']/b/a/text()").extract()
        #     yield item
        #     next_page = "http://indianroommates.sulekha.com/rentals_in_new-york-metro-area_"+ str(SulekhaSpider1Spider.page_number)
        #     if SulekhaSpider1Spider.page_number <= 2:
        #         SulekhaSpider1Spider.page_number += 1
        #     yield response.follow(next_page, callback= self.parse)