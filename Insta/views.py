from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from  django.views.generic.edit import CreateView, UpdateView, DeleteView
from  Insta.models import Post
from  django.urls import  reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from Insta.form import CustomUserCreationForm
from Insta.models import like, InstaUser,Userconnections
from annoying.decorators import ajax_request


class HelloDjango(TemplateView):
    template_name = 'home.html'

# Create your views here.

class Postview(ListView):
    model = Post
    template_name = 'post.html'
    def get_queryset(self):
        currect_user = self.request.user
        following = set()
        for conn in Userconnections.objects.filter(creator = currect_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(author__in=following)


class postdetailview(DetailView):
    model = Post
    template_name = 'show_detail.html'

class createV(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'
    login_url = 'login'

class updatetitleview(UpdateView):
    model =  Post
    template_name = 'edit.html'
    fields = ['title']

class delview(DeleteView):
    model = Post
    template_name = 'del.html'
    success_url = reverse_lazy('b')

class signupview(CreateView):
    form_class = CustomUserCreationForm  #UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserDetail(DetailView):
    model = InstaUser
    template_name = 'user_detail.html'




@ajax_request
def addlike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        likeit = like(post=post, user = request.user)
        likeit.save()
        result = 1
    except Exception as e:
        likeit = like.objects.get(post=post, user=request.user)
        likeit.delete()
        result = 0

    return {"result":result,"post_pk":post_pk }