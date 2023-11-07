""" Gunicorn deployment configuration """
# Standard libraries
from math import ceil
from multiprocessing import cpu_count
from os import getenv

# Binding address
bind = "{}:{}".format(
    getenv("HOST", "localhost"),
    getenv("PORT", "5000"),
)

# WSGI app
wsgi_app = "{}:{}".format(
    "server",
    "server"
)

# Number of worker processes
workers = ceil(cpu_count() / 2)

# Number of threads used
threads = 1
