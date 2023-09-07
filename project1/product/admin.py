from django.contrib import admin
from .models import Category,Product,Images

# Register your models here.

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    list_filter = ["status"]
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","category","price", "status"]
    list_filter = ["category","status"]
    inlines = [ImagesInline]
    
    
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["title","product"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)