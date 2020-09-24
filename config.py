import os
from datetime import timedelta

DEBUG = True
SECRET_KEY = os.urandom(12)
PERMANENT_SESSION_LIFETIME = timedelta(days=7)