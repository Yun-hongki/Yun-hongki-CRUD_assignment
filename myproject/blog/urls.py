from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:blog_id>', views.detail, name='detail'),
    path('blog/new', views.new, name='new'),
    path('blog/create', views.create, name='create'),
    path('blog/<int:blog_id>/edit', views.edit, name='edit'),
    path('blog/<int:blog_id>/update', views.update, name='update'),
    path('blog/<int:blog_id>/delete', views.delete, name='delete'),
    
]
