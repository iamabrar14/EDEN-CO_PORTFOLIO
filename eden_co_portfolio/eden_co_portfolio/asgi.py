"""ASGI config for eden_co_portfolio project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eden_co_portfolio.settings")

application = get_asgi_application()
