from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    context = {}
    if request.user.is_authenticated:
        blogs = Blog.objects.order_by('-create_date')
        context = {
            'blogs': blogs,
        }
    else:
        context['userStatus'] = 'not logged in'

    return render(request, 'crud/home.html', context)



class CreateBlog_page(LoginRequiredMixin, generic.CreateView):
    model = Blog
    fields = ['title', 'body']
    template_name = 'crud/create_page.html'
    success_url = reverse_lazy('home')


class DetailBlog_page(generic.DetailView):
    model = Blog
    template_name = 'crud/detail_page.html'


class UpdateBlog_page(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    template_name = 'crud/update_page.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')


class DeleteBlog_page(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = 'crud/delete_page.html'
    success_url = reverse_lazy('home')
