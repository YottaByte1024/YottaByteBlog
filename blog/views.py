from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import RegisterUserForm, LoginUserForm, AddPostForm
from .models import Post, ColPost


class ColPostsListView(ListView):
    model = ColPost
    queryset = ColPost.objects.filter(is_published=True).order_by('priority')
    template_name = 'blog/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogListView(ListView):
    paginate_by = 5
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-id')
    template_name = 'blog/post_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostView(DetailView):
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-id')
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class AddPostView(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpost.html'
    success_url = reverse_lazy('blog_list')

    def get_success_url(self):
        return reverse_lazy('blog_list')


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/updatepost.html'
    slug_url_kwarg = 'post_slug'
    form_class = AddPostForm
    # fields = ('title', 'slug', 'abstract', 'body', 'is_published')


