# -*- coding: utf-8 -*-
import scrapy



class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    def start_requests(self):
        urls = ['http://www.ireadweek.com/index.php/index/2.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log('hanghang %s' % response.css('ul.hanghang-list li.next a::attr(href)'))


        ''' 获取保存页面
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        '''

