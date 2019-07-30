
import configparser
import job_postings.crawlers.crawler_simplyhired as simplyhired
import job_postings.crawlers.crawler_jobserve as jobserve
import json
import logging
import queue
import re
import sys
import urllib
import uuid
from bs4 import BeautifulSoup
from job_postings.postings.job_posting import JobPosting
from datetime import datetime
from datetime import timedelta
from urllib.request import Request, urlopen
from shutil import copyfile

visited_pages = set()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(lineno)d %(funcName)s %(message)s',
)


def start_static_crawler(log):
    logging.info(f"start_static_crawler for [{log}]")
    html = open(log, 'r+', encoding='utf-8').read()
    soup = BeautifulSoup(html, features='html.parser')
    crawl_children(soup)


def crawl_children(soup):
    for page_info in soup.find_all('li', {'class': 'page'}):
        if page_info.a is not None:
            page_number = page_info.text.strip()
            if page_number not in visited_pages:
                visited_pages.add(page_number)
                # work_queue.put([site_context[0], site_context[1], page_info.a['href']])
                logging.info(page_number + page_info.a['href'])


if __name__ == "__main__":
    start_static_crawler('../log/log.html')
