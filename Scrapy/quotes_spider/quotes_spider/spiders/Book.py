import scrapy
import pdb
import requests
from urllib.parse import urlencode
from urllib.parse import urljoin
from scrapy.crawler import CrawlerProcess

payload = {
    'k': 'TV',
    'ref': 'nb_sb_noss_1'
    # 'k': 'watch for man'
    # 'crid': '4HATIKHROIVH',
    # 'sprefix': "watch f,aps,285",
    # 'ref': 'nb_sb_ss_i_1_7'
}
count=0
# title=0
class QuotesSpider(scrapy.Spider):
    name = 'Books'

    def start_requests(self):
        # url="https://www.amazon.in/s?k=tv&ref=nb_sb_noss_2"
        url = 'https://www.amazon.com/s?' + urlencode(payload)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        global count
        count=count+1
        with open('page1'+ str(count) +'.html', 'wb') as html_file:
            html_file.write(response.body)
        urls = response.xpath("//a[@class='a-link-normal a-text-normal']/@href").extract()
        for ur in urls:
            ur = response.urljoin(ur)
            yield scrapy.Request(url=ur, callback=self.parse_details)

        next_page = response.xpath("//div/div/ul/li[@class='a-last']/a/@href").get()
        if next_page:
            abs_url = f"https://www.amazon.in{next_page}"
            print(abs_url)
            yield scrapy.Request(
                url=abs_url,
                callback=self.parse)
        else:
            print()
            print('No Page Left')
            print()

    def parse_details(self,response):
        # global title
        # title = title + 1
        # pdb.set_trace()
        title=""
        title=response.xpath("//title/text()")[0].extract()
        title = title.replace("Amazon.com:", "")
        title = title.replace(":", "")
        with open(str(title) +'.html', 'wb') as html_file1:
            html_file1.write(response.body)

# process=CrawlerProcess()
# process.crawl(QuotesSpider)
# process.start()
        # yield {
        #     'name':response.css('h3.author-title::text').extract_first(),
        #     'birth_date':response.css('span.author-born-date::text').extract_first()
        # }