import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))
from portfolio_ravi.wsgi import application

# wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
# application = wsgi.application
