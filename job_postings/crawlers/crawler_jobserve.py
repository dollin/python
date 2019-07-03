
import json
import logging
import job_postings.postings.job_posting as job_posting
from datetime import datetime

visited_pages = set()
urls = list()

def crawl_jobs(soup, root, jp_file):
    logging.info(f'crawling for root site: {root}')
    for jp_item in soup.find_all("div", {'class': tag for tag in ['jobListItem newjobsum']}):
        company = None
        rate = empty_if_null(jp_item.find('span', id='summrate'))
        description = empty_if_null(jp_item.p).strip()
        url = empty_if_null(jp_item.find('span', id='summpermalink'))
        posted = datetime.strptime(jp_item.find('span', id='summposteddate').text.strip(),
                                   '%d/%m/%Y %H:%M:%S').strftime('%Y%m%d')
        jp_title = jp_item.find('div', {'class': 'jobListHeaderPanel'})
        role = jp_title.a.string if jp_title.h2 is None else jp_title.h2.a.string

        for jp_span in jp_item.find_all('span', {'class': 'jobListDetail left'}):
            if jp_span.a is not None and jp_span.a.get('target') is not None:
                company = jp_span.a.text
        if url not in urls:
            job_posting.write_to_file(role, company, rate, description, url, posted, jp_file)
            urls.append(url)


def empty_if_null(field):
    return '' if field is None else field.text

def crawl_children(soup, site_context, work_queue, max_pages):
    for page_info in soup.find('div', {'class': 'jobListPagingControl'}).find_all('a', {'class': 'Small notonpage'}):
        if page_info.text not in visited_pages and len(visited_pages) < max_pages:
            visited_pages.add(page_info.text)
            work_queue.put([site_context[0], site_context[1], page_info.get('href')])

