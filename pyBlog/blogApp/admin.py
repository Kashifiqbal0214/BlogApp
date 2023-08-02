from django.contrib import admin
from .models import BlogTable

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "post_date",)

admin.site.register(BlogTable, AuthorAdmin)