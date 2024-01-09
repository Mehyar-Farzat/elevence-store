import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()


from products.models import Product
import random
from faker import Faker





def add_products(n):
    fake = Faker()
    images = ['product-1.png','product-2.png','product-3.png','product-4.jpg','product-5.jpg','product-6.jpeg','product-7.jpeg','product-8.png','product-9.jpg']
    icons = ['01.png']
    for x in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f"product_images/{images[random.randint(0,8)]}" ,
            icon = f"product_icon/{icons[(0)]}" ,
            price = round(random.uniform(30.99,99.99),2) ,
            sku = random.randint(1000,5000),
            description = fake.text(max_nb_chars=1000),
            quantity = random.randint(10,30),
        )


    print(f'{n} Products was created successfully')

add_products(43)