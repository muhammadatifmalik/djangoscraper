from celery import shared_task
from .models import Brand
from .scraper import scrape_products

@shared_task
def scrape_brand_products(brand_id):
    brand = Brand.objects.get(id=brand_id)
    scrape_products(brand.url, brand)

def setup_periodic_tasks(sender, **kwargs):
    from celery import current_app
    from celery.schedules import crontab

    current_app.conf.beat_schedule.clear()

    # Fetch all brands and schedule tasks for each
    brands = Brand.objects.all()
    for brand in brands:
        current_app.conf.beat_schedule[f'scrape-{brand.id}'] = {
            'task': 'products.tasks.scrape_brand_products',
            'schedule': crontab(minute=0, hour='*/6'),  # Every 6 hours
            'args': (brand.id,),
        }
