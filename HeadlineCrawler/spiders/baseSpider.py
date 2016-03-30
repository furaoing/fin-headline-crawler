# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:27:27 2016

@author: roy
"""

import traceback
from HeadlineCrawler.lib.common import BaseCrawler
from HeadlineCrawler.lib import ERROR

#title = node[0].text
#body_url = node[0].attrib["href"]


class spider(object):
    def __init__(self):
        self.baseCrawler = BaseCrawler()

    def crawl_link_page_xpath(self, site, headline):
        html = self.baseCrawler.html_download(site["url"], site["charset"])
        tree_nodes = self.baseCrawler.xpath_parse(html, site["xpath1"])
        if len(tree_nodes) > 1 or len(tree_nodes) == 0:
            raise ERROR.MatchError

        tree_node = tree_nodes[0]
        headline.title = tree_node.text
        headline.body_url = tree_node.attrib["href"]
        headline.source = site["source"]

        headline.title = self.baseCrawler.cleanText(headline.title)
        headline.body_url = self.baseCrawler.cleanText(headline.body_url)

        headline.body_url = self.baseCrawler.path_fix(site["url"], headline.body_url)
        return headline

    def crawl_link_page_regex(self, site, headline):
        html = self.baseCrawler.html_download(site["url"], site["charset"])
        html = self.baseCrawler.cleanHTML(html)
        match_result = self.baseCrawler.regex_parse(site["pattern1"], html)

        if len(match_result) > 1 or len(match_result) == 0:
            raise ERROR.MatchError

        headline.title = match_result[0][1]
        headline.body_url = match_result[0][0]
        headline.source = site["source"]

        headline.title = self.baseCrawler.cleanText(headline.title)
        headline.body_url = self.baseCrawler.cleanText(headline.body_url)

        headline.body_url = self.baseCrawler.path_fix(site["url"], headline.body_url)
        return headline

    """
    def crawl_body_page_xpath(self, site, headline):
        html = self.baseCrawler.html_download(headline.body_url, site["charset"])
        #tree_node = self.baseCrawler.html_parse(html, site["xpath2"])

        headline.body = self.baseCrawler.cleanHTML(html)
        headline.pub_time = site["source"]
        headline.crawl_time = None
        headline.pub_time = None

        return headline
    """
        
    
        





