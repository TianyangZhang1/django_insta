from django.urls import path
from Insta.views import HelloDjango

urlpatterns = [
    path('', HelloDjango.as_view(), name='helloworld')
]

