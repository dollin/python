
import configparser
import job_postings.crawlers.retry as retry
import json
import logging
import queue
import re
import sys
import uuid
from bs4 import BeautifulSoup
from job_postings.postings.job_posting import JobPosting
from datetime import datetime
from shutil import copyfile
from pydoc import locate

work_queue = queue.Queue()
max_pages = 2

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(threadName)s] %(funcName)s:%(lineno)d %(message)s',
)


def process_root(root):
    logging.info('reading urls from ' + root)
    config = configparser.ConfigParser()
    config.read(root)

    for section in config.sections():
        logging.info('adding link for [' + section + '] to work_queue')
        work_queue.put([section, config[section]['root'], config[section]['url']])


def process_work_queue(json):
    html_file = open('../log/log_' + datetime.now().strftime("%y-%m-%d_%H.%M") + '.html', 'w+', encoding='utf-8')
    while not work_queue.empty():
        work_item = work_queue.get()
        html = retry.get_html(''.join(work_item[1:3]))
        if html is not None:
            soup = BeautifulSoup(html, features='html.parser')
            html_file.write(soup.prettify())
            crawler = locate(f'job_postings.crawlers.crawler_{work_item[0]}')
            crawler.crawl_jobs(soup, work_item[1], json)
            crawler.crawl_children(soup, work_item, work_queue, max_pages)
        work_queue.task_done()
    html_file.close()


def log(soup, enabled):
    if enabled is True:
        html_filename = '../log/log_' + datetime.now().strftime("%y-%m-%d_%H.%M") + '.html'
        with open(html_filename, 'w+', encoding='utf-8') as log_html:
            log_html.write(soup.prettify())
            log_html.close()
        copyfile(html_filename, '../log/logging.html')


def remove_last_comma(postings_file):
    lines = open(postings_file, 'r+').readlines()
    lines[-1] = lines[-1].replace(',', '')
    json = open(postings_file, 'w+', encoding='utf-8')
    json.writelines(lines)
    json.close()


def start_crawler():
    logging.info("start_crawler")
    process_root('../resources/sites.ini')
    postings_file = '../data/job_postings_' + datetime.now().strftime("%y-%m-%d_%H.%M") + '.json'

    json = open(postings_file, 'w+', encoding='utf-8')
    json.write('[\n')
    process_work_queue(json)
    json.write(']')
    json.close()

    remove_last_comma(postings_file)
    copyfile(postings_file, '../data/job_postings.json')


if __name__ == "__main__":
    start_crawler()
