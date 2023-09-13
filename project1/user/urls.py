from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /home/
    path("", views.profile, name="profile"),
    path("update/", views.user_update, name="user_update"),
    path("password/", views.change_password, name="change_password"),
    path("comments/", views.comments, name="comments"),
    path("deletecomments/<int:id>", views.deletecomments, name="deletecomments"),
    # ex: /home/5/
    #path("<int:question_id>/", views.detail, name="detail"),
]



