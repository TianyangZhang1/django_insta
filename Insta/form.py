from django.contrib.auth.forms import UserCreationForm
from  Insta.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'pic')
