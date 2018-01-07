import os.path

import urllib.parse
import arrow

from scrapy.http import HtmlResponse
from selenium import webdriver

driver = webdriver.PhantomJS()

class SeleniumMiddleware(object):

    def process_request(self, request, spider):

        driver.get(request.url)

        return HtmlResponse(driver.current_url,
            body = driver.page_source,
            encoding = 'utf-8',
            request = request)


def close_driver():
    driver.close()