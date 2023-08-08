from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import GeneralProductCategory, ProductCategory, Product, Company, Detailed


@admin.register(GeneralProductCategory)
class GeneralProductForm(ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductCategory)
class ProductCategoryForm(ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductForm(ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Company)
class CompanyForm(ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register((Detailed))
