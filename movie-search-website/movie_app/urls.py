from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('category/<str:category>/', views.category, name='category'),
]    