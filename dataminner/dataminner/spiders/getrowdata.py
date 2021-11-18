
import scrapy
import xlrd
import openpyxl


from scrapy.loader import ItemLoader


class getrowdata(scrapy.Spider):
     name = 'getrowdata'
     path = r"C:\\Users\\SUJI\\Desktop\\crawler_project\\dataminner\\dataminner\\spiders\\urls.xlsx"
     
     

     start_urls = 'https://www.bayut.com'
     def start_requests(self):
        wb_obj = openpyxl.load_workbook(self.path)
        sheet_obj = wb_obj.active
        
        # print(self.start_urls)
        # print(cell_obj.value)
        for i in range(1,2):
            cell_obj = sheet_obj.cell(row = i, column = 1)
            yield scrapy.Request(self.start_urls+str(cell_obj.value))
     def parse(self,response):   
        print(response.xpath('/html/body/div[1]/main/div[3]/div[1]/div[4]/div/div[2]/ul/li[2]/span[2]/text()').get())

    
    
