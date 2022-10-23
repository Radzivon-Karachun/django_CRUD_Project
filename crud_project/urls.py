from django.urls import path
from crud_project import views


urlpatterns = [
    path('', views.home, name='home'),

    path('create/', views.CreateBlog_page.as_view(),
         name='create_blog_page'),
    path('<int:pk>/', views.DetailBlog_page.as_view(),
         name='detail_blog_page'),
    path('<int:pk>/update/', views.UpdateBlog_page.as_view(),
         name='update_blog_page'),
    path('<int:pk>/delete/', views.DeleteBlog_page.as_view(),
         name='delete_blog_page'),
]
