from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'update_time', 'score')
    list_filter = ('category', 'update_time')
    search_fields = ('title', 'description')
    ordering = ('-update_time',)

admin.site.register(Movie, MovieAdmin)    