from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post


def create(request):
    return render(request, 'post/create.html', {})


class DetailPost(DetailView):
    model = Post
    template_name = 'post/detail.html'


class ListPost(ListView):
    model = Post
