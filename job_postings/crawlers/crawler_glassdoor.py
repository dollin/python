
import json
import logging
import re
import job_postings.postings.job_posting as job_posting
from datetime import datetime
from datetime import timedelta

visited_pages = set()
urls = list()

def crawl_jobs(soup, root, jp_file):
    logging.info(f'crawling for root site: {root}')
    for jp_item in soup.find_all('li', {'class': 'jl'}):
        company = jp_item.find('div', {'class': 'jobInfoItem jobEmpolyerName'}).text.split('–')[0].strip()
        rate = ''
        description = re.sub('  ', '', jp_item.find('div', {'class': 'minor descSnippet'}).text).replace('\n', ' ')
        title = jp_item.find('div', {'class': 'jobContainer'})
        role = title.a.text.strip()
        url = root + title.a['href']

        days_old = 0
        if jp_item.find('span', {'class': 'minor'}) is not None:
            age = re.split('[+ d]', jp_item.find('span', {'class': 'minor'}).text.strip())[0]
            days_old = int('0' if age == 'Today' else age)

        posted = (datetime.now() - timedelta(days=days_old)).strftime('%Y%m%d')

        if url not in urls:
            job_posting.write_to_file(role, company, rate, description, url, posted, jp_file)
            urls.append(url)


def crawl_children(soup, site_context, work_queue, max_pages):
    for page_info in soup.find_all('li', {'class': 'page'}):
        if page_info.a is not None:
            page_number = page_info.text.strip()
            if page_number not in visited_pages  and len(visited_pages) < max_pages:
                visited_pages.add(page_number)
                work_queue.put([site_context[0], site_context[1], page_info.a['href']])
