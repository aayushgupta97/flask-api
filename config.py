import multiprocessing

bind = 'localhost:8000'
backlog = 2048

# workers = 8
workers = 9
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

spew = False


daemon = False

pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = None


# gunicorn -c config.py wsgi:app
# gunicorn -w8 wsgi:app
