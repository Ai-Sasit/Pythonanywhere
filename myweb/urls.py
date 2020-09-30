from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('login', views.login_Web),
    path('loginX', views.log_in),

    path('indexR', views.reg_success),
    path('register', views.register),

    path('logoutX', views.log_out),

    path('Editpro', views.Editpro),
    path('EditProcess', views.Edit_Process),

    path('AuthorEdit', views.AuthorEdit),
    path('AuthorX',views.AuthorX),

    path('Writing', views.Writing),
    path('WritingX', views.WritingX),

]