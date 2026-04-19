import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "api_integration_data_processing.settings"
)

app = get_wsgi_application()
