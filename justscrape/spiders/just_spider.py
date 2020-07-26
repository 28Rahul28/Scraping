
#bcard0 > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1)
#bcard1 > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1)
#bcard2 > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1)
#bcard0 > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1) > span:nth-child(1)
#bcard0 > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > p:nth-child(4) > span:nth-child(2) > a:nth-child(1) > b:nth-child(1) > span:nth-child(7)
import scrapy 

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        "https://www.justdial.com/Delhi/House-On-Rent/nct-10192844",
    ]
   

    def parse(self, response):
        for x in range(10):
            number = ''
            for f in range(7,17):
                val = response.css('#bcard'+str(x)+' > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > p:nth-child(4) > span:nth-child(2) > a:nth-child(1) > b:nth-child(1) > span:nth-child('+str(f)+')::attr(class)').get()
                if(val[14:]=='ji'):
                    number = number + str(9)
                elif(val[14:]=='lk'):
                    number = number + str(8)
                elif(val[14:]=='nm'):
                    number = number + str(7)    
                elif(val[14:]=='po'):
                    number = number + str(6)
                elif(val[14:]=='rq'):
                    number = number + str(5)
                elif(val[14:]=='ts'):
                    number = number + str(4)
                elif(val[14:]=='vu'):
                    number = number + str(3)
                elif(val[14:]=='wx'):
                    number = number + str(2)
                elif(val[14:]=='yz'):
                    number = number + str(1)
                elif(val[14:]=='acb'):
                    number = number + str(0)                
            yield {
                'title':response.css('#bcard'+str(x)+' > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > h2:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1)::text').get(),
                'rating':response.css('#bcard'+str(x)+' > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1) > span:nth-child(1)::text').get(),
                'number':number,
                'address':response.css('#bcard'+str(x)+' > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > p:nth-child(5) > span:nth-child(2) > span:nth-child(1)::text').get().split(".")[0][13:],
                }

        