# -*- coding: utf-8 -*-

import requests
from lxml import etree
from io import StringIO
import re

from HeadlineCrawler.conf.UserSetting import Setting
from HeadlineCrawler.lib import ERROR


class BaseCrawler(object):
    def __init__(self):
        self.htmlparser = etree.HTMLParser()

    def html_download(self, url, charset):
        try:
            r = requests.get(url, timeout=Setting.REQUEST_TIMEOUT)
            r.encoding = charset
            return r.text
        except ERROR.TimeoutError as e:
            raise e

    def xpath_parse(self, html, xpath):
        f = StringIO(html)
        tree = etree.parse(f, self.htmlparser)
        nodes = tree.xpath(xpath)

        return nodes

    def strip_end_forwardslash(self, URL):
        if URL[-1] == r"/":
            resultURL = URL[:-1]
        else:
            resultURL = URL
        return resultURL

    def path_fix(self, SiteURL, BodyURL):
        if r"http://" in BodyURL:
            return BodyURL
        else:
            BaseURL = self.strip_end_forwardslash(SiteURL)
            if BodyURL[0] == r".":
                return BaseURL + r"/" + BodyURL[2:]
            elif BodyURL[0] == r"/":
                return BaseURL + r"/" + BodyURL[1:]
            else:
                raise Exception

    def cleanHTML(self, html):
        html = html.replace("\r", "")
        html = html.replace("\n", "")
        html = html.replace("\t", "")
        return html

    def cleanText(self, text):
        text = text.replace("\r", "")
        text = text.replace("\n", "")
        text = text.replace("\t", "")
        return text

    def regex_parse(self, pattern, text):
        result = re.findall(pattern, text)
        return result


class HeadLine(object):
    def __init__(self):
        self.source = None
        self.title = None
        self.body = None
        self.body_url = None
        self.pub_time = None
        self.crawl_time = None

    def ok(self):
        if self.source and self.title and self.body and self.body_url and self.pub_time and self.crawl_time:
            return True
        else:
            return False
