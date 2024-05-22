from django.contrib import admin
from .models import Post,Author,Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","excerpt","author","content","date","image","slug")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name","email")


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
