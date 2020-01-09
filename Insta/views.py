from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from  django.views.generic.edit import CreateView, UpdateView, DeleteView
from  Insta.models import Post
from  django.urls import  reverse_lazy

class HelloDjango(TemplateView):
    template_name = 'home.html'

# Create your views here.

class Postview(ListView):
    model = Post
    template_name = 'post.html'

class postdetailview(DetailView):
    model = Post
    template_name = 'show_detail.html'

class createV(CreateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'

class updatetitleview(UpdateView):
    model =  Post
    template_name = 'edit.html'
    fields = ['title']

class delview(DeleteView):
    model = Post
    template_name = 'del.html'
    success_url = reverse_lazy('b')

