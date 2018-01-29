from django.contrib import admin
from .models import Post, LikeDislike, Vote


admin.site.register(Post)
admin.site.register(LikeDislike)
admin.site.register(Vote)