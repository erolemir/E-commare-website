from django.contrib import admin
from .models import Category,Product,Images,Comment

# Register your models here.

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    list_filter = ["status"]
    prepopulated_fields = {'slug': ('title',)}
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","category","price", "status"]
    list_filter = ["category","status"]
    inlines = [ImagesInline]
    prepopulated_fields = {'slug': ('title',)}
    
    
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["title","product"]
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ["subject","comment","user", "status"]
    list_filter = ["status"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)