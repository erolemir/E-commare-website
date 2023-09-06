from django.contrib import admin
from .models import Category,Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    list_filter = ["status"]
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","category","price", "status"]
    list_filter = ["category","status"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)