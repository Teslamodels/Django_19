from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class Home(ListView):
    model = Post
    template_name = 'home.html'

class Page(DetailView):
    model = Post
    template_name = 'detail.html'
