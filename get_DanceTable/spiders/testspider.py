# -*- coding: utf-8 -*-
import scrapy
from ..selenium_middleware import close_driver

class TestspiderSpider(scrapy.Spider):
    name = "testspider" # 実行時の名前に指定
    start_urls = ['http://race.netkeiba.com/?pid=data&id=c201806010211&mode=coursedata']

    #サーバーに配慮
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "get_DanceTable.selenium_middleware.SeleniumMiddleware": 0,
        },
        "DOWNLOAD_DELAY": 1,
    }
    # list_allow_parse = [r'(正z規表現)']  #データ抽出するリンク指定

    # allowed_domains = ["keiba.yahoo.co.jp"]
    # start_urls = ['http://keiba.yahoo.co.jp/']

    # start_urls = ['https://keiba.yahoo.co.jp/race/denma/1709050611/']
    def parse(self, response):
            # for racehorse in response.xpath('//tr'):
        yield {
                # 'racename': response.xpath('//div[@id=\'raceTitName\']/h1/text()').extract(),
            'racename': response.xpath('//*[@id="main"]/div/div/div[4]/div/dl/dd/h1/text()').extract(),
            # 'Venue':,
            # 'distance':,
            # 'field':,
            # 'circumference':,
            'racehorse': response.xpath('//*[@id="RaceData"]/div/div/table/tbody/tr/td[3]/span[1]/a/text()').extract(),
            # 'racehorsepass': response.xpath('//td/a[contains(@href,\'/directory/horse/\' )]/@href').extract(),
            # 'type':response.xpath('//td/span[contains(text,\'牡\' ) or contains(text,\'牝\' )]/text()').extract(),
            #'jockey': response.xpath('//td/a[contains(@href,\'/directory/jocky/\' )]/text()').extract()
        }

    def close_driver():
        driver.close()