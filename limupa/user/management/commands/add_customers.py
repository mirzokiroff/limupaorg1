import random
from django.core.management.base import BaseCommand
from user.models import OurTeam
from random import choice
from django.utils.text import slugify
from faker import Faker
from time import time



