import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://www.amazon.in/s?k=watch&ref=nb_sb_noss_2']

    def parse(self, response):
        with open('page1.html', 'wb') as html_file:
            html_file.write(response.body)
