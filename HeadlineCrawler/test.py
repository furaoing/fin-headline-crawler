# -*- coding: utf-8 -*-

from HeadlineCrawler.spiders.baseSpider import spider
from HeadlineCrawler.conf.loadSite import load_sites
from HeadlineCrawler.lib.common import HeadLine
from HeadlineCrawler.conf.UserSetting import Setting
import time


sites = load_sites()
headline = HeadLine()
my_spider = spider()

site = sites["19"]

headline = my_spider.crawl_link_page_xpath(site, headline)
print(headline)
