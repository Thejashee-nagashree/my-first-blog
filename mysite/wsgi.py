import sys
import os

# Add your project directory to the sys.path
path = '/home/Thejashree/thejashree.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Activate virtual environment
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()