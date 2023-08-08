import uuid
from django.db import models


class Core(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class GeneralProductCategory(Core):
    created_at, updated_at = None, None


class ProductCategory(Core):
    created_at, updated_at = None, None
    general = models.ForeignKey(GeneralProductCategory, on_delete=models.CASCADE)


class ProductImage(Core):
    product_id = models.ForeignKey('Product', models.CASCADE, 'product_image')
    is_general = models.BooleanField(default=False)
    image = models.ImageField(upload_to='shop/')


class Detailed(models.Model):
    class SizeChoices(models.TextChoices):
        S = 'S', 'Small'
        M = 'M', 'Medium'
        L = 'L', 'Large'
        XL = 'XL', 'Extra large'

    class ProductColor(models.TextChoices):
        BlUE = 'Blue', 'Blue'
        WHITE = 'White', 'White'
        RED = 'Red', 'Red'
        BLACK = 'Black', 'Black'
        PINK = 'Pink', 'Pink'
        PURPLE = 'Purple', 'Purple'

    product_id = models.ForeignKey('Product', models.CASCADE, 'product_detailed')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    detail = models.CharField(max_length=100)
    color = models.CharField(choices=ProductColor.choices, null=True)
    size = models.CharField(choices=SizeChoices.choices, null=True)


class Company(Core):
    created_at, updated_at = None, None
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug company')


class Product(Core):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug product')
    description = models.TextField()
    company = models.ForeignKey(Company, models.CASCADE, 'company')
    category = models.ForeignKey(ProductCategory, models.CASCADE, 'category')
