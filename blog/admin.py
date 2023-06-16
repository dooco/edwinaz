from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """ Admin for Post """
    list_display = (
        'user',
        'title',
        'content',
        'excerpt',
        'image',
        'date_added',
    )

    ordering = ('date_added',)


admin.site.register(Post, PostAdmin)