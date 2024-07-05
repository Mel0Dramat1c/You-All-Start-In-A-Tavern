import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'you_all_start_in_a_tavern.settings')

application = get_wsgi_application()
