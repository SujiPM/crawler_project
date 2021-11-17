import scrapy
from scrapy.loader import ItemLoader


class project(scrapy.Spider):
    # name = 'project'
    # start_urls = ['https://www.bayut.com/property/details-5382212.html']

    # def parse(self, response):
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[3]/span[2]/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[2]/span[2]/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[1]/span[2]/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[6]/span[2]/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[4]/span[2]/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div[1]/div/span[1]/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[2]/span[2]/span/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[1]/span[2]/span/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[3]/span[2]/span/span/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/div[2]/span[2]/text()').getall())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/div[3]/span[2]/text()').get())
    #   print(response.xpath('/html/body/div/main/div[2]/div[1]/div[1]/div[1]/picture/img/text()').get())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/h1/text()').get())
    #   print(response.xpath("//span[@class='_005a682a']/text()").extract())
    #   print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[1]/div[1]/div/div/div/span/text()').getall())    
    #   print("hello")

    name = 'fake'
    flow = "home"
    start_urls = 'https://www.bayut.com/to-rent/property/dubai/'
    
    def start_requests(self):
        a=2
        for i in range(1,4):
            if i == 1:
                yield scrapy.Request(self.start_urls)
            else:
                url='https://www.bayut.com/to-rent/property/dubai/page-'+str(i)+'/'
                print(url)
                yield scrapy.Request(url)
    def parse(self,response):
        # print(response.xpath("//a[@class='_287661cb']/@href").extract()[1])
        if self.flow == 'home':
            print(response.xpath("//a[@class='_287661cb']/@href").extract()[1])
            self.flow = 'row'
        else:
            url = 'https://www.bayut.com/property/details-5382212.html'
            yield scrapy.Request(url)
            print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[2]/span[2]/text()').get())
            


