from django.urls import path
from Insta.views import HelloDjango, Postview, postdetailview, createV, updatetitleview, delview

urlpatterns = [
    path('hello', HelloDjango.as_view(), name='helloworld'),
    path('post/', Postview.as_view(), name = 'b'),
    path('post/<int:pk>/', postdetailview.as_view(), name='detail'),
    path('post/new/',createV.as_view(), name='create'),
    path('post/edit/<int:pk>/', updatetitleview.as_view(), name= 'edit'),
    path('post/del/<int:pk>/', delview.as_view(), name = 'del'),
]

