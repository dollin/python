
import json
import logging
import uuid

def instance(job):
    return JobPosting(job['role'].strip(),
                      job['company'],
                      job['rate'],
                      job['description'],
                      job['link'].strip(),
                      job['posted'].strip(),
                      job['relevance'])

def write_to_file(role, company, rate, description, link, posted, jp_file):
    jp = JobPosting(role=role.strip(),
                    company=company,
                    rate=rate,
                    description=description,
                    link=link.strip(),
                    posted=posted.strip())
    logging.info(jp)
    jp_file.write(json.dumps(jp.__dict__, indent=4))
    jp_file.write(',')

class JobPosting:

    def __init__(self, role, company, rate, description, link, posted, relevance=1):
        self.job_id = str(uuid.uuid4())
        self.role = role
        self.company = '' if company is None else company
        self.rate = rate
        self.description = description
        self.link = link
        self.posted = posted
        self.relevance = relevance

    def __hash__(self):
        return hash(self.role) ^ hash(self.company) ^ hash(self.description) ^ hash(self.posted)

    def __eq__(self, other):
        return self.role == other.role \
               and self.company == other.company \
               and self.description == other.description \
               and self.posted == other.posted

    def __str__(self):
        return '{\n\tjob_id: ' + self.job_id \
               + '\n\trole: ' + self.role \
               + '\n\tcompany: ' + self.company \
               + '\n\trate: ' + self.rate \
               + '\n\tdescription: ' + self.description \
               + '\n\tlink: ' + self.link \
               + '\n\tposted: ' + self.posted \
               + '\n\trelevance: ' + str(self.relevance) \
               + '\n}'

    # @staticmethod
    # def write_to_file(role, company, rate, description, link, posted, jp_file):
    #     jp = JobPosting(role=role.strip(),
    #                     company=company,
    #                     rate=rate,
    #                     description=description,
    #                     link=link.strip(),
    #                     posted=posted.strip())
    #     logging.info(jp)
    #     jp_file.write(json.dumps(jp.__dict__, indent=4))
    #     jp_file.write(',')
