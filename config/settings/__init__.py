# Django importa "config.settings" como modulo de configuracion
# (ver DJANGO_SETTINGS_MODULE en manage.py/wsgi.py/asgi.py). Se separa
# en su propia carpeta -equivalente a src/main/resources/application.properties
# del proyecto Java- para poder crecer mas adelante en varios archivos
# (por ejemplo base.py, local.py, production.py) sin ensuciar la raiz.
from .base import *  # noqa: F401,F403
