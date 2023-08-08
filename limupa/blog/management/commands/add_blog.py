import random
from django.core.management.base import BaseCommand
from limupa.blog.models import Post
from random import choice
from django.utils.text import slugify
from faker import Faker


class Command(BaseCommand):
    faker = Faker()

