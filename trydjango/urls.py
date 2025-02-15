"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
''' 
    i dont know what the include dose for now, am leaving this note here for later rememberas
'''

from article import views

from .view import home, article_home
from accounts.views import login_view, logout_view, register_veiw


"""
    the recipes.urls is the path where the urls.py is located as in here it say's
    it is located in the recipes folder
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pantry/recipes/', include('recipes.urls')), # i never know watin this shit the do 
    # path('blog/', include('article.urls')),
    path('articles/', include('article.urls')),
    # path('articles/', views.article_search_view),
    # path('articles/create', views.article_create, name='article-create'),
    # path('articles/<slug:slug>/', views.article_detail_view, name='article-detail'),#in this <int:id> 
    path('olisa/', home), 
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_veiw)
]
   