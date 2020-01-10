from django.db import models
from imagekit.models import ProcessedImageField
from  django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class InstaUser(AbstractUser):
    pic = ProcessedImageField(
        upload_to='static/images/personal',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

    def get_connections(self):
        connections = Userconnections.objects.filter(creator = self)
        return connections

    def get_follower(self):
        followers = Userconnections.objects.filter(following= self)
        return  followers

    def is_followed_by(self, user):
        followers =  Userconnections.objects.filter(following = self)
        return  followers.filter(creator=user).exists()


class Userconnections(models.Model):

   # created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name='friendship_creator_set')
    following = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name='friend_set')

    def __str__(self):
        return self.creator.username + " follows " + self.following.username


class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
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
        # use the related name
        return self.reallylikes.count()

class like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reallylikes')
    user = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name='reallylikes')

    class Meta:
        unique_together = ("post", 'user')

    def __str__(self):
        return 'Like:' + self.user.username + ' likes ' + self.post.title



class comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(InstaUser, on_delete= models.CASCADE, related_name='comments')
    commentpart = models.CharField(max_length=100)
    post_on = models.DateTimeField(auto_now_add=True, editable=False)
