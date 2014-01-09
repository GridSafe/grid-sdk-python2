# -*- coding: utf-8 -*-

from grid_sdk import GridSdk

if __name__ == "__main__":

    example = GridSdk()
    src_url = "https://www.cdnzz.com/logo,http://api.gridzz.net/api/json"
    print example.preload(src_url)
    print example.purge_cache(src_url)
