"""
WSGI config for azuresite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azuresite.settings')
if os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_azure_nrg.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_azure_nrg.settings')

application = get_wsgi_application()
