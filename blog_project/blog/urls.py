from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from blog.views import *


    

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/delete', views.post_delete, name="post_delete"),
    path('create-post', views.post_create, name='create'),
    path('post/<int:pk>/edit', views.post_edit, name='edit'),
    path('admin/', admin.site.urls),
    path('login-page/', views.login_page, name='login'),
    path('register-page/', views.register_page, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    
]

