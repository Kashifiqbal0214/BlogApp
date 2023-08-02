from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.main, name= 'main'),
    path( 'Blog/', views.Blog, name = 'Blog' ),
    path('Blog/details/<int:id>', views.details, name= 'details'),
    path( 'testBlog/', views.testBlog, name = 'testBlog' ),
    path('testing/', views.testing, name='testing'),
]