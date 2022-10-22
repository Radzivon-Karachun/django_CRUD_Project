from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Blog


def home(request):
    blogs = Blog.objects.order_by('-create_date')
    context = {
        'blogs': blogs,
    }
    return render(request, 'crud/home.html', context)


class CreateBlog_page(generic.CreateView):
    model = Blog
    fields = ['title', 'body']
    template_name = 'crud/create_page.html'
    success_url = reverse_lazy('home')


class DetailBlog_page(generic.DetailView):
    model = Blog
    template_name = 'crud/detail_page.html'


class UpdateBlog_page(generic.UpdateView):
    model = Blog
    template_name = 'crud/update_page.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')


class DeleteBlog_page(generic.DeleteView):
    model = Blog
    template_name = 'crud/delete_page.html'
    success_url = reverse_lazy('home')
