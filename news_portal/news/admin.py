from django.contrib import admin
from .models import *


admin.site.register(News)


@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):

    def get_text(self, obj):
        return obj.text[:30]

    list_display = ['id', 'get_text', 'owner', 'news', 'level', 'created_at']
    list_display_links = ('id', 'get_text',)
