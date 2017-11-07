import scrapy
from scrapy.selector import  Selector

class QuotesSpider(scrapy.Spider):
    name = "ireadweek"
    start_urls = [
        'http://www.ireadweek.com/index.php/index/2.html',
    ]

    def parse(self, response):
        for quote in response.css('ul.hanghang-list a::attr(href)'):
            print(quote.extract())
            yield {
                # 'text': quote.css('span.text::text').extract_first(),
                # 'author': quote.xpath('span/small/text()').extract_first(),
            }


