from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Colonnes affichées
    list_filter = ('author', 'created_at')  # Filtres
    search_fields = ('title', 'content', 'author')  # Recherche
    date_hierarchy = 'created_at'  # Navigation par date