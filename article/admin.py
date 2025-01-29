from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import article

user = get_user_model()

# admin.site.unregister(user)

class articleInline(admin.StackedInline):
    model = article
    extra = 0

class useradmin(admin.ModelAdmin):
    inlines = [articleInline]
    # field = ['title', 'content', 'publish']

# admin.site.register(user, useradmin)

# Register your models here.


class articleadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'updated', 'slug']
    search_fields = ['title', 'content']
    raw_id_fields = ['user']
admin.site.register(article, articleadmin)

