import random
from django.core.management.base import BaseCommand
from limupa.shop.models import Product, Detailed, ProductImage, ProductCategory, Company
from random import choice
from django.utils.text import slugify
from faker import Faker
from time import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        start_time = time()
        for i in range(1, 100):
            title = fake.text(100)
            p = Product.objects.create(
                title=title,
                slug=slugify(title),
                description=fake.text(15),
                category=ProductCategory.objects.all().order_by('?').first(),
                company=Company.objects.all().order_by('?').first()
            )
            image = ProductImage.objects.create(
                product_id=p,
                image='shop/laptop.jpg',
                is_general=True
            )

            print(f'post {i} has been created')
        end_time = time()
        print('Finished!!!')
        milliseconds = end_time - start_time
        print(f'Time elapsed: {milliseconds} milliseconds')


# class Command(BaseCommand):
#     faker = Faker()
#
#     def handle(self, *args, **options):
#         product_all = Product.objects.all()
#         for _ in range(1000):
#             title = self.faker.sentence(6)
#
#             product = Product.objects.create(
#                 title=title,
#                 slug=slugify(title),
#                 description=self.faker.text(),
#                 category=ProductCategory.objects.all().order_by('?').first(),
#                 company=Company.objects.all().first()
#             )
#             details = Detailed.objects.create(
#                 price=random.randint(200, 10000),
#                 quantity=random.randint(1, 1000),
#                 detail=random.shuffle([15.3, 14.0, 12.0, 16.0]),
#                 color=random.shuffle(Detailed.ProductColor.values),
#                 size=random.shuffle(Detailed.SizeChoices.values)
#             )
#             product_image = ProductImage.objects.create(
#                 is_general=True,
#                 image='zbad5tfbbe5newoz03dw.jpeg'
#             )
#             for i in range(3):
#                 product_image = ProductImage.objects.create(
#                     image='2-laptop-and-monitor.jpg'
#                 )