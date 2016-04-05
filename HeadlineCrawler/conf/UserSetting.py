# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:14:48 2016

@author: roy
"""

from waffle import system


class Setting(object):
    SITE_CONF_RELPATH = "conf/site_spec.json"
    REFRESH_INTERVAL = 1*60
    REQUEST_TIMEOUT = 5
    LOG_FILE_RELPATH = "log/log.txt"

    SITE_CONF_PATH = system.create_abs_path(SITE_CONF_RELPATH)
    LOG_PATH = system.create_abs_path(LOG_FILE_RELPATH)
