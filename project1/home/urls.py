from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # ex: /home/
    path("", views.index, name="index"),
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
    path("referances/", views.referances, name="referances"),
    path("iletisim/", views.iletisim, name="iletisim"),
    path("urunler/", views.urunler, name="urunler"),
    path("urunler/<int:id>", views.urun_detay, name="urun_detay"),
    # ex: /home/5/
    #path("<int:question_id>/", views.detail, name="detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
