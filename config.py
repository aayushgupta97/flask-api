import multiprocessing

bind = 'localhost:8000'
backlog = 2048

workers = 9
# workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
# threads = 3
worker_connections = 1000
timeout = 30
keepalive = 2

spew = False
daemon = False

user = None
group = None
tmp_upload_dir = None

errorlog = '-'
# loglevel = 'critical'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = None


# gunicorn -c config.py wsgi:app
# gunicorn -w8 wsgi:app

# without request logging
# gunicorn -b :8091 -w 1 -k gevent --worker-connections=2000 --backlog=1000 -p gunicorn.pid --log-level=critical rse:app
# 40 200 product
