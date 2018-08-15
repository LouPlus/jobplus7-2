import multiprocessing

bind = '127.0.0.1:80'

workers = multiprocessing.cpu_count() * 2 + 1
