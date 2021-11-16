import scrapy
from scrapy.loader import ItemLoader


class project(scrapy.Spider):
    name = 'project'
    start_urls = ['https://www.bayut.com/property/details-5382212.html']

    def parse(self, response):
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[3]/span[2]/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[2]/span[2]/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[1]/span[2]/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[6]/span[2]/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[4]/span[2]/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div[1]/div/span[1]/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[2]/span[2]/span/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[1]/span[2]/span/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[3]/span[2]/span/span/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/div[2]/span[2]/text()').getall())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/div[3]/span[2]/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[1]/div[1]/picture/source/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/h1/text()').get())
      print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[1]/div[1]/div/div/div/span/text()').getall())    
      print("hello")

