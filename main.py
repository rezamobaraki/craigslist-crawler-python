"""
Craigslist Crawler - Main Entry Point

A Python-based web crawler for extracting real estate listings from Craigslist.

Author: Reza Mobaraki
GitHub: https://github.com/rezamobaraki
LinkedIn: https://linkedin.com/in/reza-mobaraki
"""

import sys

from crawl import LinkCrawler, DataCrawler, ImageDownloader


def get_pages_data():
    raise NotImplementedError


if __name__ == '__main__':
    switch = sys.argv[1]
    if switch == 'find_links':
        crawler = LinkCrawler(cities=['paris', 'berlin', 'amsterdam', 'munich'])
        crawler.start(store=True)
    elif switch == 'extract_pages':
        crawler = DataCrawler()
        crawler.start(store=True)
    elif switch == 'download_images':
        crawler = ImageDownloader()
        crawler.start(store=True)
