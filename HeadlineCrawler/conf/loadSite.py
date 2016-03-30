# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:37:36 2016

@author: roy
"""

from TaikorCommon import system
from HeadlineCrawler.conf.UserSetting import Setting


def load_sites():
    return system.json_read(Setting.SITE_CONF_PATH)


