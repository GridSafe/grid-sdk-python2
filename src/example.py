# -*- coding: utf-8 -*-

from grid_sdk import GridSdk

if __name__ == "__main__":

    example = GridSdk()
    src_url = "url"
    example.preload(src_url)
    example.purge_cache(src_url)
