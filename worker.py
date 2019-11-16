import os

import redis
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()


"""
from rq import Queue
from rq.job import Job
from worker import conn

q = Queue(connection=conn)
 job = q.enqueue_call(
            func=count_and_save_words, args=(url,), result_ttl=5000
        )
"""