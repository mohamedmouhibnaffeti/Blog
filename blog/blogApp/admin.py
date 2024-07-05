from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'status')
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'content', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author', 'content')

# Register your models with custom admin classes
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
