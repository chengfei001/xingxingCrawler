import scrapy
from scrapy.selector import  Selector

class QuotesSpider(scrapy.Spider):
    name = "ireadweek"
    start_urls = [
        'http://www.ireadweek.com/index.php/index/2.html',
    ]

    def parse(self, response):
        print(response.css('ul.hanghang-list a::attr(href)'))
        print('--------------------------------------')
        for quote in response.css('ul.hanghang-list a::attr(href)'):
            print('()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()')
            print(quote.xpath('/a/@href').extract_first())
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            yield {
                # 'text': quote.css('span.text::text').extract_first(),
                # 'author': quote.xpath('span/small/text()').extract_first(),
            }

        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)


