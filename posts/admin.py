from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'username', 'created_datetime', 'updated_datetime']
    list_filter = ['created_datetime', 'username']
    search_fields = ['title', 'username', 'content']
    readonly_fields = ['created_datetime', 'updated_datetime']
    date_hierarchy = 'created_datetime'