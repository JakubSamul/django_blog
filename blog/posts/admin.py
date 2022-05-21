from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "active", "pub_date")
    list_filter = ('active', 'author')
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
