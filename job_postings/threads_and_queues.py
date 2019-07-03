
# import wikipedia
#
# result = wikipedia.page('freeCodeCamp')
# print(result.summary)
# for link in result.links:
#     print(link)

# import uuid
import logging


#
# user_id = uuid.uuid4()
# logging.info(user_id)

import threading
import time
from queue import Queue

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(threadName)s] %(funcName)s:%(lineno)d %(message)s',
)

# lock to serialize console output
lock = threading.Lock()

def do_work(item):
    time.sleep(.1)  # pretend to do some lengthy work.
    # Make sure the whole print completes or threads can mix up output in one line.
    with lock:
        if item not in s:
            logging.info(f'{threading.current_thread().name} {item}')
            s.add(item)
            q.put(item)
        else:
            logging.info(f'already added {item}')

# The worker thread pulls an item from the queue and processes it
def worker():
    while True:
        time.sleep(.1)
        work_item = q.get()  # Not atomic so multi-threads 'could' (actually, they WILL) get the same value
        do_work(work_item)
        q.task_done()

# Create the queue and thread pool.
s = set()
q = Queue()
for i in range(4):
    t = threading.Thread(target=worker)
    t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    t.start()

# stuff work items on the queue (in this case, just a number).
start = time.perf_counter()
for i in range(11):
    q.put(i)

q.join()       # block until all tasks are done

# "Work" took .1 seconds per task.
# 20 tasks serially would be 2 seconds.
# With 4 threads should be about .5 seconds (contrived because non-CPU intensive "work")
logging.info(f'time: {time.perf_counter() - start}')
