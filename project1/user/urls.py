from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /home/
    path("", views.profile, name="profile"),
    # ex: /home/5/
    #path("<int:question_id>/", views.detail, name="detail"),
]



