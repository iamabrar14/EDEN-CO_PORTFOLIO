"""WSGI config for eden_co_portfolio project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eden_co_portfolio.settings")

application = get_wsgi_application()
