from django.contrib import admin

# Register your models here.
from posts.models import Post

#więcej na stronie: https://docs.djangoproject.com/en/1.9/ref/contrib/admin/
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ["timestamp", "updated"]
    list_filter = ["timestamp", "updated"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)