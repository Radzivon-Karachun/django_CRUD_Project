from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('create/', views.CreateBlog_page.as_view(),
         name='create_blog_page'),
]
