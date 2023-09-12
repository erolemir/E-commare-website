from django.contrib import admin

# Register your models here.

from .models import ShopCard,Order,OrderProduct

class ShopCardAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','price','amount']
    list_filter = ['user']
    
class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','product','price','quantity','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address', 'city', 'country', 'status']  # address ekledik
    list_filter = ['status']
    readonly_fields = ('user', 'phone', 'address', 'city', 'country', 'ip', 'total')
    can_delete = False
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','price','amount','status']
    list_filter = ['user']

admin.site.register(ShopCard,ShopCardAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)