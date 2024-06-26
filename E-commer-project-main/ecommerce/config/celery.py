import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

celery_app = Celery(
    'config',
    broker=os.environ.setdefault('CELERY_BROKER_URL', 'redis://redis:6379/0'),
    include=[
        'api.tasks',
    ])