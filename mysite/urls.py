from django.contrib import admin
from django.urls import include, path
from myweb import views

urlpatterns = [
    path('', views.index),
    path('myweb/', include('myweb.urls')),
    path('polls/', include('polls.urls')),
    path('Reading/<int:index>', views.Reading),
    path('admin/', admin.site.urls),
]
