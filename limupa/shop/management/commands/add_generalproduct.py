import random
from django.core.management.base import BaseCommand
from limupa.shop.models import Product, Detailed, ProductImage, ProductCategory, Company, GeneralProductCategory
from random import choice
from django.utils.text import slugify
from faker import Faker
from time import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        start_time = time()
        for i in range(1, 100):
            title = fake.text(7)
            GeneralProductCategory.objects.create(
                title=title,
                slug=slugify(title)
            )
            print(f'post {i} has been created')
        end_time = time()
        print('Finished!!!')
        milliseconds = end_time - start_time
        print(f'Time elapsed: {milliseconds} milliseconds')