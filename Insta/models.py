from django.db import models
from imagekit.models import ProcessedImageField
from  django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pic = ProcessedImageField(
        upload_to='static/images/personal',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_posts',
        blank=True,
        null=True
    )
    title = models.TextField(blank=True, null=True)
    images = ProcessedImageField(
        upload_to='static/images',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null= True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def get_like(self):
        return self.likes.count()

class like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ("post", 'user')

    def __str__(self):
        return 'Like:' + self.user.username + ' likes ' + self.post.title

class comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comments')
    commentpart = models.CharField(max_length=100)
    post_on = models.DateTimeField(auto_now_add=True, editable=False)
