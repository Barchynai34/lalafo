from django.contrib import admin

from apps.posts.models import Post

@admin.register(Post)
class PosrAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'image', 'created')
