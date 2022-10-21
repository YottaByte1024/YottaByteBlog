from django.contrib import admin
from .models import Post, ColPost


class ColPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'priority', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['priority', 'is_published']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(ColPost, ColPostAdmin)

