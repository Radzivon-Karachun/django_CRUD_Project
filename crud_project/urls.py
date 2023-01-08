from django.urls import path
from crud_project.views import home, CreateBlog_page, DetailBlog_page, UpdateBlog_page, DeleteBlog_page
from auth_system.views import signup_page, login_page, logout_page, public_page, private_page, PrivateClass_page


urlpatterns = [
    path('', home, name='home'),

    path('create/', CreateBlog_page.as_view(),
         name='create_blog_page'),
    path('<int:pk>/', DetailBlog_page.as_view(),
         name='detail_blog_page'),
    path('<int:pk>/update/', UpdateBlog_page.as_view(),
         name='update_blog_page'),
    path('<int:pk>/delete/', DeleteBlog_page.as_view(),
         name='delete_blog_page'),

    path('signup', signup_page,
         name='signup_page'),
    path('login', login_page,
         name='login_page'),
    path('logout', logout_page,
         name='logout_page'),

    path('publicpage', public_page,
         name='public_page'),
    path('privatepage', private_page,
         name='private_page'),
    path('privateclasspage', PrivateClass_page.as_view(),
         name='privateclass_page'),
]
