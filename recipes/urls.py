from django.urls import path

from .views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_create_view,
    recipe_update_view,

)

app_name='recipes' #this will prevent urls name conflicte
# with this we can make use of recipe:lisr  as a revers call
urlpatterns = [
    path("list/", recipe_list_view, name='list'),
    path("create/", recipe_create_view, name='create'),
    path("<int:id>/edit/", recipe_update_view, name='update'),
    path("<int:id>/", recipe_detail_view, name='detail')
]