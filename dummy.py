import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from django.conf import settings
from faker import Faker
from product.models import Brand, Product


def create_Products(n):
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.png']
    for _ in range(n):
       
        Product.objects.create(
  
        )

def create_Brand(n):
    fake = Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg']
    for _ in range(n):
       
        Brand.objects.create(
            name=fake.name(),
            image =f'brands/{images[random.randint(0,17)]}'
        ) 

    print(f'Seed {n} Brands Successfully')       



create_Brand(5)
