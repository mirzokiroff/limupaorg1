from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    postcode = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])
    # country = models.CharField(max_length=255, blank=True, null=True)
    # company_name = models.CharField(max_length=255, blank=True, null=True)


class OurTeam(models.Model):
    image = models.ImageField(upload_to='customers/')
    name = models.CharField(max_length=222)
    job = models.CharField(max_length=222)
    email = models.EmailField(max_length=222, unique=True, null=True, blank=True)
    facebook = models.URLField(max_length=222, null=True, blank=True)
    twitter = models.URLField(max_length=222, null=True, blank=True)
    linkedin = models.URLField(max_length=222, null=True, blank=True)
    instagram = models.URLField(max_length=222, null=True, blank=True)

    def __str__(self):
        return self.name
