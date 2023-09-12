from django.contrib import admin
from .models import Setting,ContactFormMessage,UserProfile,UserProfileForm
# Register your models here.

class ContactForAdmin(admin.ModelAdmin):
    list_display = ["name","email","subject","message","note","status"]
    list_filter = ["status"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user_name","phone","address","city","country","image_tag"]
    list_filter = ["city","country"]
    readonly_fields = ("image_tag",)

    def user_name(self,obj):
        return obj.user.username

    def image_tag(self,obj):
        return obj.image_tag()

    user_name.short_description = "User"
    image_tag.short_description = "Image"

admin.site.register(Setting)
admin.site.register(ContactFormMessage,ContactForAdmin)
admin.site.register(UserProfile,UserProfileAdmin)