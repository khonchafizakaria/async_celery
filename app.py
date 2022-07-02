import os

from django.db import transaction

from celery import Celery, Task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


app = Celery(
    'core',
    task_cls="async_celery.task_cls:TransactionTask"
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('async_celery.config')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
