from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Blog


def home(request):
    return render(request, 'crud/home.html')


class CreateBlog_page(generic.CreateView):
    model = Blog
    fields = ['title', 'body']
    template_name = 'crud/create_page.html'
    success_url = reverse_lazy('home')


class DetailBlog_page(generic.DetailView):
    model = Blog
    template_name = 'crud/detail_page.html'
