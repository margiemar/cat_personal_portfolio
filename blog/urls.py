from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.all_blogs, name='alias_all_blogs'),
    path("<int:blog_id>", views.detail, name='detail'),
]
