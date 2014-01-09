# -*- coding: utf-8 -*-

__author__ = "lycheng"
__email__ = "cheng@grid-safe.com"
__date__ = "2013-08-28"
__version__ = "0.1.0"

import requests

from config import USER_NAME
from config import USER_SIGNATURE

import re
import json

class GridSdk(object):

    def __init__(self, user_name="", signature=""):
        self.user_name = USER_NAME if not user_name else user_name
        self.signature = USER_SIGNATURE if not signature else signature
        self.api_url = "https://www.cdnzz.com/api/json"

    def __request(self, urls, method):
        """post 数据

        :param url: 进行清缓存或者预加载的url
        :param method: 具体进行的操作
        """
        post_data = {
            "user": self.user_name,
            "signature": self.signature,
            "method": method,
            "url": urls
        }
        try:
            response = requests.post(self.api_url, data=post_data)
        except:
            return False, "Network Error"

        rv = json.loads(response.content)

        if "error" == rv["result"]:
            return False, rv["msg"]

        return True, rv["msg"]

    def __validate_urls(self, urls):
        """判断一个url 是否合乎规范

        :param url: 需要进行判断的URL

        :return boolean
        """
        # django url validator
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            # domain
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?'
            r'|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        try:
            urls = urls.split(",")
            rv = []
            for url in urls:
                if not regex.search(url):
                    continue
                rv.append(url)
            return ",".join(rv)
        except:
            return ""

    def preload(self, urls):
        """预加载指定的链接

        :param url: 要进行预加载的链接

        :return (boolean, msg): 是否完成，相关的信息
        """
        urls = self.__validate_urls(urls)
        if not urls:
            return False, "URL invalid"

        return self.__request(urls, "AddPreload")

    def purge_cache(self, urls):
        """通过指定链接清除缓存

        :param url: 要清除缓存的链接

        :return (boolean, msg): 是否完成，相关的信息
        """
        urls = self.__validate_urls(urls)
        if not urls:
            return False, "URL invalid"

        return self.__request(urls, "PurgeCache")
