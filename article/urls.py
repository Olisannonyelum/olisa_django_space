
from django.urls import path


from article import views


app_name = 'article'
urlpatterns = [
    path('', views.article_search_view, name='search'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail_view, name='detail'),#in this <int:id> 
    # path('articles/', views.article_search_view, name='search'),
    # path('articles/create', views.article_create, name='create'),
    # path('articles/<slug:slug>/', views.article_detail_view, name='detail'),#in this <int:id> 
    
]
   