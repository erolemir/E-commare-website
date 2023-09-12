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
    list_display = ["title","category","price", "status","image_tag"]
    list_filter = ["category","status"]
    readonly_fields = ("image_tag",)
    prepopulated_fields = {'slug': ('title',)}
    def image_tag(self,obj):
        return obj.image_tag()

   
    image_tag.short_description = "Image"
    
    
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["title","product"]
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ["subject","comment","user", "status"]
    list_filter = ["status"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)