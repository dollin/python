
import configparser
import dateutil.relativedelta as datedelta
import job_postings.postings.job_posting as job_posting
import json
import re
from datetime import datetime

cache = set()

config = configparser.ConfigParser()
config.read('../resources/rules.ini')


def recently_posted(posted_on):
    dd = -1 * int(config['posted']['days_limit'])
    return datetime.now() + datedelta.relativedelta(days=dd) < datetime.strptime(posted_on, '%Y%m%d')


def populate_cache():
    with open('../data/job_postings.json', 'r', encoding='utf-8') as job_postings_json:
        jobs = json.load(job_postings_json)

    for job in jobs:
        if recently_posted(job['posted']):
            for key in 'company', 'role', 'description':
                weights = config[key]['weights'].split(',')
                for i, priority in enumerate(['high', 'medium', 'low']):
                    for key_priority in config[key][priority].split(','):
                        if key_priority.strip() in job[key].lower():
                            job['relevance'] += int(weights[i].strip())
            jp = job_posting.instance(job)
            cache.add(jp)


def sort_cache():
    by_date = sorted(cache, key=lambda jp: jp.posted, reverse=False)
    by_relevance = sorted(by_date, key=lambda jp: jp.relevance, reverse=False)
    return by_relevance


def print_summary(company=None):
    print('{:8.8}, {:10.10}, {:45.45}, {:48.48}, {:24.24}, {:100.100}, {}'
          .format('rank', 'posted', 'role', 'company', 'rate', 'description', 'link'))

    count = 0
    for job in filter(lambda jp: jp.relevance > 1 and (company is None or company.upper() in jp.company.upper()),
                      sort_cache()):
        print('{:08d}, {:%Y-%m-%d}, {:45.45}, {:48.48}, {:24.24}, {}, {}'.format(
            job.relevance,
            datetime.strptime(job.posted, '%Y%m%d'),
            job.role,
            job.company,
            job.rate,
            job.description,
            job.link))
        count += 1
    print(f'count: [{count}]')


if __name__ == "__main__":
    populate_cache()
    print_summary()
