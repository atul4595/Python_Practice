import scrapy
from scrapy.spiders import Spider
from scrapy.http import FormRequest
from scrapy.crawler import CrawlerProcess

count=0
count_1=0
class Test(scrapy.Spider):
    name='Scrapy_Test'
    headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#         "Cache-Control": "max-age=0",
# "Connection": "keep-alive",
# "Content-Length": "879",
# "Content-Type": "application/x-www-form-urlencoded",
# "Cookie": "JSESSIONID=acaVGpkqYmx1ssIJFBRr3uBAtME7x_bzKLFDvxaR.wdc-vm-dmz15; __utmz=228102172.1614320305.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=228102172.431947152.1614320305.1616646344.1616678207.15; __utmc=228102172; __utmt=1; __utmb=228102172.1.10.1616678207",
# "Host": "publicaccess.wycombe.gov.uk",
# "Origin": "https://publicaccess.wycombe.gov.uk",
# "Referer": "https://publicaccess.wycombe.gov.uk/idoxpa-web/search.do?action=advanced",
# 'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
# "sec-ch-ua-mobile": "?0",
# "Sec-Fetch-Dest": "document",
# "Sec-Fetch-Mode": "navigate",
# "Sec-Fetch-Site": "same-origin",
# "Sec-Fetch-User": "?1",
# "Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

    def start_requests(self):
        payload = {
            'searchCriteria.reference': '',
            'searchCriteria.planningPortalReference': '',
            'searchCriteria.alternativeReference': '',
            'searchCriteria.description': '',
            'searchCriteria.applicantName': '',
            'searchCriteria.caseType': '',
            'searchCriteria.ward': '',
            'searchCriteria.parish': '',
            'searchCriteria.conservationArea': '',
            'searchCriteria.agent': '',
            'searchCriteria.caseStatus': '',
            'searchCriteria.caseDecision': '',
            'searchCriteria.appealStatus': '',
            'searchCriteria.appealDecision': '',
            'searchCriteria.developmentType': '',
            'caseAddressType': 'Application',
            'searchCriteria.address': '',
            'date(applicationReceivedStart)': '',
            'date(applicationReceivedEnd)': '',
            'date(applicationValidatedStart)': '01/01/2021',
            'date(applicationValidatedEnd)': '30/01/2021',
            'date(applicationCommitteeStart)': '',
            'date(applicationCommitteeEnd)': '',
            'date(applicationDecisionStart)': '',
            'date(applicationDecisionEnd)': '',
            'date(appealDecisionStart)': '',
            'date(appealDecisionEnd)': '',
            'searchType': 'Application'
        }

        # url="https://www.amazon.in/s?k=tv&ref=nb_sb_noss_2"
        url = 'https://publicaccess.wycombe.gov.uk/idoxpa-web/advancedSearchResults.do?action=firstPage'
        # url = 'https://publicaccess.wycombe.gov.uk/idoxpa-web/search.do?action=advanced'
        meta = {'handle_httpstatus_all': True}
        yield FormRequest(url=url, headers=self.headers,formdata=payload,method='POST',
                                           meta=meta,callback=self.parse)
        # yield FormRequest(url=url, formdata=payload, headers=self.headers, callback=self.parse)

    def parse(self, response):
        global count
        count = count + 1
        with open(r'C:\Users\Jayendra\Desktop\Pyt\Scrap'+str(count) + '.html', 'wb') as html_file1:
            html_file1.write(response.body)
        count_1=0
        urls = response.xpath("// *[ @ id = 'searchresults']//li//a//@href").extract()
        for ur in urls:
            # ur = response.urljoin(ur)
            ur=f"https://publicaccess.wycombe.gov.uk{ur}"
            # ur = 'https://publicaccess.wycombe.gov.uk' + ur
            # ur=ur.replace("?dchild=1","")
            print(ur)
            # yield scrapy.Request(url=ur,callback=self.parse_details,headers=self.headers)
            req = scrapy.Request(url=ur,callback=self.parse_details,headers=self.headers)
            req.headers['Cookie'] = 'js_enabled=true; is_cookie_active=true;'
            yield req

        next_page = response.xpath("//*[@id='searchResultsContainer']/p[1]/a[@class='next']/@href").get()
        print(next_page)
        if next_page:
            abs_url = ""
            abs_url = f"https://publicaccess.wycombe.gov.uk{next_page}"
            print(abs_url)
            yield scrapy.Request(
                url=abs_url,
                callback=self.parse)
        else:
            print()
            print('No Page Left')
            print()
    def parse_details(self,response):
        global count_1
        count_1 = count_1 + 1
        # pdb.set_trace()
        title=""
        # title=response.xpath("//title/text()")[0].extract()
        # title = title.replace("Amazon.com:", "")
        Proposal=''
        Proposal = response.css('tr:nth-child(6) td::text')[0].extract()
        Proposal=Proposal.strip()

        with open(r'C:\Users\Jayendra\Desktop\Pyt\Scrap'+str(count) +"." +str(count_1)+'.html', 'wb') as html_file2:
            html_file2.write(response.body)
        yield {
            "Proposal":Proposal
        }
process=CrawlerProcess()
process.crawl(Test)
process.start()