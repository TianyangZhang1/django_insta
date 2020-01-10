from django.contrib import admin

# Register your models here.
from Insta.models import Post, InstaUser, like, Userconnections


admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(like)
admin.site.register(Userconnections)

