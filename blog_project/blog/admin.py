from django.contrib import admin
from blog.models import PostModel

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(PostModel, PostModelAdmin)

