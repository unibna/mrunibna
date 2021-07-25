from django.db import models
from django.forms import forms
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from .models import Category, Post
from .forms import PostCreationForm

class PostList(ListView):
    model = Post
    template_name = "post/post/post_list.html"
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        category_list = Category.objects.all()
        context['category_list'] = category_list

        return context

class PostDetail(DetailView):
    model = Post
    template_name = "post/post/post_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        category_list = Category.objects.all()
        context['category_list'] = category_list

        return context

class PostCreate(CreateView):
    model = Post 
    form_class = PostCreationForm
    template_name = "post/post/post_create.html"
    success_url = reverse_lazy('post_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        user_post_list = Post.objects.filter(author=self.request.user)
        context['user_post_list'] = user_post_list

        return context


class CategoryList(ListView):
    model = Category
    template_name = "post/category/category_list.html"


class CategoryDetail(DetailView):
    model = Category
    template_name = "post/category/category_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        category_list = Category.objects.all()
        context['category_list'] = category_list

        return context