import scrapy
from scrapy.spiders import Spider
from scrapy.http import FormRequest
from scrapy.crawler import CrawlerProcess

class Test(scrapy.Spider):
    name = 'yahoo'

    base_url = 'https://www.yell.com{}'
    start_urls = [
        'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=770796459&keywords=hospitals&location=united+kingdom']

    def parse(self, response):
        for data in response.css('div.row.businessCapsule--mainRow'):
            title = data.css('.text-h2::text').get()
            avg_rating = response.css('span.starRating--average::text').get()

            yield scrapy.Request(final_url, callback=self.parse_site, cb_kwargs:{"title": title, "avg_rating": avg_rating})

            next_page = response.urljoin(response.css('a.pagination--next::attr(href)').extract_first())
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

    def parse_site(self, response, title, final_url, avg_rating):
        opening_hours = response.css('strong::text').get()
        opening_hours = opening_hours.strip() if opening_hours else ""

        items = {
            'Title': title,
            'Average Rating': avg_rating,
            'Hours': opening_hours
        }
        yield items


process=CrawlerProcess()
process.crawl(Test)
process.start()