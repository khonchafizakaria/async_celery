import json
import os

from django.conf import settings

RABBITMQ = {
    "PROTOCOL": "amqp",  # in prod change with "amqps"
    "HOST": os.getenv("RABBITMQ_HOST", "localhost"),
    "PORT": os.getenv("RABBITMQ_PORT", 5672),
    "BROKER_PORT": os.getenv("RABBITMQ_BROKER_PORT", 15672),
    "USER": os.getenv("RABBITMQ_DEFAULT_USER", "guest"),
    "PASSWORD": os.getenv("RABBITMQ_DEFAULT_PASSWORD", "guest"),
}

django_conf = "settings"
broker_url = f"{RABBITMQ['PROTOCOL']}://{RABBITMQ['USER']}:{RABBITMQ['PASSWORD']}@{RABBITMQ['HOST']}:{RABBITMQ['PORT']}//"
broker_api = f"http://{RABBITMQ['USER']}:{RABBITMQ['PASSWORD']}@{RABBITMQ['HOST']}:{RABBITMQ['BROKER_PORT']}/api//"
result_backend = 'django_celery_results.backends:DatabaseBackend'
result_accept_content = ['application/json']
accept_content = ['application/json']
task_serializer = 'json'
result_serializer = 'json'
enable_utc = True
timezone = settings.TIME_ZONE
worker_concurrency = 3
loglevel = 'DEBUG'
logging = 'DEBUG'
