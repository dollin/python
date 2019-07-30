
import json
import logging
import urllib.parse as urlparse
import job_postings.postings.job_posting as job_posting
from datetime import datetime

visited_pages = set()
urls = list()

def crawl_jobs(soup, root, jp_file):
    logging.info(f'crawling for root site: {root}')
    for jp_item in soup.find_all("div", {'class': tag for tag in ['card js-job', 'card js-job isp']}):
        role = jp_item.find('div', {'class': 'jobposting-title-container'}).h2.a.string
        company = jp_item.h3.text.replace('\u00a0', '')
        rate = ''
        description = jp_item.p.text
        url = root + jp_item.find('a', {'class': 'card-link'}).get('href')
        posted = datetime.strptime(jp_item.find("div", {'class': 'SerpJob-metaInfoRight'}).time['datetime'],
                                   "%Y-%m-%dT%H:%M:%SZ").strftime('%Y%m%d')

        if url not in urls:
            job_posting.write_to_file(role, company, rate, description, url, posted, jp_file)
            urls.append(url)

def crawl_children(soup, site_context, work_queue, max_pages):
    for page_info in soup.find('div', {'class': 'pagination Pagination'}).find_all('a', href=True):
        parameters = urlparse.urlparse(page_info['href']).query
        if 'pn' in urlparse.parse_qs(parameters):
            page_number = urlparse.parse_qs(parameters)['pn']
            if page_number[0] not in visited_pages and len(visited_pages) < max_pages:
                visited_pages.add(page_number[0])
                work_queue.put([site_context[0], site_context[1], page_info['href']])
