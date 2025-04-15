from django.contrib import admin
from .models import BlogPost, Comment



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at', 'is_admin', 'parent')
    list_filter = ('is_admin', 'created_at')
    search_fields = ('name', 'email', 'body', 'post__title')  # <-- required for autocomplete_fields
    autocomplete_fields = ('post', 'parent')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('post', 'parent', 'name', 'email', 'website', 'body', 'is_admin')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )


