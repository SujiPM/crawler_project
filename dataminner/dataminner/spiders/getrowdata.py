
import scrapy
import xlrd
import openpyxl
import json
import re


from scrapy.loader import ItemLoader


class getrowdata(scrapy.Spider):
     name = 'getrowdata'
     path = r"C:\\Users\\SUJI\\Desktop\\crawler_project\\dataminner\\dataminner\\spiders\\urls.xlsx"
     property_id="null"
     purpose="null"
     type_="null"
     added_on="null"
     furnishing="null"
     price="null"
     currency_type="null"
     currency_amount="null"
     location="null"
     bed_bath_size="null"
     bedrooms="null"
     bathrooms="null"
     size="null"
     permit_number="null"
     agent_name="null"
     img_url="null"
     breadcrumbs="null"
     amenities="null"
     description="null"
     def createdictionary(self):
        dictionary ={
            "property_id" : self.property_id,
            "purpose": self.purpose,
            "type_": self.type_,
            "added_on": self.added_on,
            "furnishing":self.furnishing,
            "price": {
            "currency": self.currency_type,
            "amount": self.currency_amount
            },
            "location": self.location,
            "bed_bath_size": {
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "size": self.size
            },
            "permit_number": self.permit_number,
            "agent_name": self.agent_name,
            "img_url": self.img_url,
            "breadcrumbs": self.breadcrumbs,
            "amenities": self.amenities,
            "description": self.description


            }
        return dictionary
        
     

     start_urls = 'https://www.bayut.com'
     def start_requests(self):
        wb_obj = openpyxl.load_workbook(self.path)
        sheet_obj = wb_obj.active
        
        # print(self.start_urls)
        # print(cell_obj.value)
        for i in range(1,1009):
            cell_obj = sheet_obj.cell(row = i, column = 1)
            yield scrapy.Request(self.start_urls+str(cell_obj.value))
            print("file written :" ,i)
     def parse(self,response):   
        print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[2]/span[2]/text()').get())
        self.property_id=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[3]/span[2]/text()').get()
        self.purpose=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[2]/span[2]/text()').get()
        self.type_=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[1]/span[2]/text()').get()
        self.added_on=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[6]/span[2]/text()').get()
        self.furnishing=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[4]/span[2]/text()').get()
        self.currency_type=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div[1]/div/span[1]/text()').get()
        self.currency_amount=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[1]/div[1]/div/span[3]/text()').get()
        self.location=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[2]/text()').get()
        self.bedrooms=re.findall(r'\d+',response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[1]/span[2]/span/text()').get())[0]
        self.bathrooms=re.findall(r'\d+',response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[2]/span[2]/span/text()').get())[0]
        self.size=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[2]/div[3]/div[3]/span[2]/span/span/text()').get()
        self.permit_number=response.xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/div[2]/span[2]/text()').getall()[2]
        self.agent_name=response.xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/div[3]/span[2]/text()').get()
        self.img_url=response.xpath("//picture[@class='_219b7e0a']/img/@data-src").extract()[0]
        self.breadcrumbs=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/h1/text()').get()
        temp = []
        [temp.append(x) for x in response.xpath("//span[@class='_005a682a']/text()").extract() if x not in temp]
        self.amenities=temp
        self.description=response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[1]/div[1]/div/div/div/span/text()').get()

        json_object = json.dumps(self.createdictionary(), indent = 4)
  
        # Writing to sample.json
        with open("output.json", "a") as outfile:
            outfile.write(json_object)

 



    
