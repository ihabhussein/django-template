import multiprocessing

bind = '127.0.0.1:__PORT__'
workers = multiprocessing.cpu_count() * 2 + 1
reload = True

capture_output = True
accesslog = '/var/log/__NAME__.log'
errorlog = '/var/log/__NAME__.err'
