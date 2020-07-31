from django.contrib import admin
from django.urls import include, path
from myweb import views

urlpatterns = [
    path('', views.index),
    path('newtheme' , views.newtheme),
    path('myweb/', include('myweb.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
