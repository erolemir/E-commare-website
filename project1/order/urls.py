from django.urls import path
from . import views


urlpatterns = [
    path("", views.order, name="order"),
    path("addtocard/<int:id>", views.addtocard, name="addtocard"),
    path("shopcart/", views.shopcart, name="shopcart"),
    path("deleteformcart/<int:id>", views.deleteformcart, name="deleteformcart"),
    path("orderproduct/", views.orderproduct, name="shopcart"),
    
]