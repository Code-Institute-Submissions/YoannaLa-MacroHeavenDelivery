from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Product)

