from celery import Celery
from celery.signals import beat_init
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoScraper.settings')

app = Celery('djangoScraper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@beat_init.connect
def setup_periodic_tasks(sender, **kwargs):
    from products.tasks import setup_periodic_tasks
    setup_periodic_tasks(sender, **kwargs)
