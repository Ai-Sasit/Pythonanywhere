from django.urls import path

from . import views

urlpatterns = [
    # ex: /myweb/
    path('', views.index, name='index'),
    # ex: /myweb/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /myweb/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('register', views.register, name='register'),
    path('login', views.login_Web, name='login'),
    path('indexR', views.reg_success, name='indexR'),
    path('loginX', views.log_in, name='loginX'),
    
    path('logoutX', views.log_out, name='logoutX'),

]