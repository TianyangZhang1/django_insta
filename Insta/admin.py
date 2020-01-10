from django.contrib import admin

# Register your models here.
from Insta.models import Post, User, like


admin.site.register(Post)
admin.site.register(User)
admin.site.register(like)
