from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "is_active"]
    list_filter = ["product"]


admin.site.register(Comment, CommentAdmin)
