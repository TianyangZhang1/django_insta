from Insta.models import like
from django import template

register = template.Library()

@register.simple_tag
def if_user_like(post, user):
    try:
        like_it = like.objects.get(post=post, user=user)
        return 'fa-heart'
    except:
        return 'fa-heart-o'


@register.simple_tag
def is_following(current_user, background_user):
    return background_user.get_follower().filter(creator=current_user).exists()
