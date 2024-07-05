import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'you_all_start_in_a_tavern.settings')

application = get_asgi_application()
