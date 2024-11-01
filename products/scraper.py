import requests
from bs4 import BeautifulSoup
from .models import Product, Brand

def scrape_products(brand_url, brand):
    response = requests.get(brand_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.select('.product-selector')

    for product in products:
        name = product.select_one('.product-name').text
        asin = product['data-asin']
        sku = product.select_one('.product-sku').text if product.select_one('.product-sku') else None
        image = product.select_one('.product-image')['src']

        Product.objects.update_or_create(
            asin=asin,
            defaults={'name': name, 'sku': sku, 'image': image, 'brand': brand}
        )
