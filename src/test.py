# -*- coding: utf-8 -*-

from grid_sdk import GridSdk

import unittest
import time

class TestGridSDK(unittest.TestCase):

    def setUp(self):
        self.test_sdk = GridSdk()

    def __get_url(self):
        ts = str(int(time.time()))
        url = "http://www.true.com/public/js/jquery.%s.js" % ts
        return url

    def test_purge(self):
        self.assertTrue(self.test_sdk.purge_cache(self.__get_url())[0])

        self.assertFalse(self.test_sdk.purge_cache("http://www.baidu.com/png.jpg")[0])

        self.assertFalse(self.test_sdk.purge_cache("no url")[0])

        self.test_sdk.user_name = "error user name"
        self.assertFalse(self.test_sdk.purge_cache(self.__get_url())[0])

        self.test_sdk.user_name = "true@126.com"
        self.test_sdk.signature= "error signature"
        self.assertFalse(self.test_sdk.purge_cache(self.__get_url())[0])

    def test_preload(self):

        self.assertTrue(self.test_sdk.preload(self.__get_url())[0])

        self.assertFalse(self.test_sdk.preload("http://www.baidu.com/png.jpg")[0])

        self.assertFalse(self.test_sdk.preload("no url")[0])

        self.test_sdk.user_name = "error user name"
        self.assertFalse(self.test_sdk.preload(self.__get_url())[0])

        self.test_sdk.user_name = "true@126.com"
        self.test_sdk.signature= "error signature"
        self.assertFalse(self.test_sdk.preload(self.__get_url())[0])


if __name__ == "__main__":
    unittest.main()
