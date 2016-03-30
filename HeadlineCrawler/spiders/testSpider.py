# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:27:27 2016

@author: roy
"""

import requests
from roy_py import system
from lxml import etree
from io import StringIO
import re

url = "http://www.ftchinese.com/"

r = requests.get(url)
r.encoding="utf8"

"""
_xpath = "/html/body/div[@class='b_box']/div[6]/div[@class='box_mid']/div[@class='b_jujiao']/h2[1]"

f = StringIO(r.text)
htmlparser = etree.HTMLParser()
tree = etree.parse(f, htmlparser)
r = tree.xpath(_xpath)
"""

html = r.text

html = html.replace("\r", "")
html = html.replace("\n", "")
html = html.replace("\t", "")
system.write_content("html.txt", html)


pattern1 = r'<a class="nowrap-on-wide c-headline" target=_blank href="(.+?)">(.+?)</a>'
result = re.findall(pattern1, html)




