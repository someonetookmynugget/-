from django.contrib import admin
from django.urls import path
from . import views
from .views import next
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    # path('next/', next.as_view(), name="next"),
    path('next/', views.next, name="next"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)