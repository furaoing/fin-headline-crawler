# -*- coding: utf-8 -*-

from TaikorCommon.util.util import TimeFormater

from HeadlineCrawler.spiders.baseSpider import spider
from HeadlineCrawler.conf.loadSite import load_sites
from HeadlineCrawler.lib.common import HeadLine
from HeadlineCrawler.conf.UserSetting import Setting
from HeadlineCrawler.lib import ERROR
import time
import traceback
import logging
import sys

if __name__ == "__main__":

    tt = TimeFormater("mysql")

    logging.basicConfig(
            filename=Setting.LOG_PATH,
            filemode="a",
            format="%(asctime)s %(levelname)s/%(name)s, %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.ERROR
            )

    def crawl(site, spider, HeadlineSourceID):
        headline = HeadLine()
        try:
            if site["type"] == "regex":
                headline = spider.crawl_link_page_regex(site, headline)
            else:
                headline = spider.crawl_link_page_xpath(site, headline)
            console_msg = "%s %s; source: %s" % (tt.format_time(), headline.title, headline.source)
            print(console_msg)
            return headline
        except ERROR.TimeoutError as e:
            logging.critical("Http Request Timeout: id - " + HeadlineSourceID)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_str = "".join(traceback.format_tb(exc_traceback))
            logging.critical(traceback_str)
            traceback.print_exc()
        except ERROR.MatchError as e:
            logging.critical("Xpath or Regex Error: id - " + HeadlineSourceID)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_str = "".join(traceback.format_tb(exc_traceback))
            logging.critical(traceback_str)
            traceback.print_exc()
        except BaseException as e:
            logging.critical("Undefined Exception: id - " + HeadlineSourceID)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_str = "".join(traceback.format_tb(exc_traceback))
            logging.critical(traceback_str)
            traceback.print_exc()

    def epoch(interval):
        sites = load_sites()
        my_spider = spider()
        while True:
            for HeadlineSourceID in sites.keys():
                crawl(sites[HeadlineSourceID], my_spider, HeadlineSourceID)
            time.sleep(interval)

    epoch(Setting.REFRESH_INTERVAL)
