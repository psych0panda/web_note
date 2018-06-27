from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('create_category', views.create_category, name='create_category'),
    path('latest_article', views.latest_article, name='latest_article'),
    path('create_article/', views.create_article, name='create_article'),
    path('<str:article_title>/',
         views.read_article, name='read_article'),
    path('update/<str:article_title>/',
         views.update_article, name='update_article'),
    path('delete/<str:article_title>/',
         views.delete_article, name='delete_article'),
    path('articles/', views.home, name='articles'),
    path('/about/', views.about, name='about'),
    path('/contact/', views.contact, name='contact'),
]
