from django.contrib import admin
from .models import Setting,ContactFormMessage
# Register your models here.

class ContactForAdmin(admin.ModelAdmin):
    list_display = ["name","email","subject","message","note","status"]
    list_filter = ["status"]

admin.site.register(Setting)
admin.site.register(ContactFormMessage,ContactForAdmin)