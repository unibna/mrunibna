from typing import cast
from django.core import paginator
from django.db import models
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic import ListView

from apps.post.models import Category, Post


def HomeView(request):
    template_name = 'home/home.html'
    
    # get context
    category_list = Category.objects.all()

    post_list = Post.objects.order_by('created')

    if post_list.count() > 2:
        highlight_post = post_list[0]
        latest_post = post_list[1]

        post_list = post_list[2:]
    else:
        highlight_post = None
        latest_post = None

    context = {
        'category_list': category_list,
        'post_list': post_list,
        'highlight_post': highlight_post,
        'latest_post': latest_post,
    }

    return render(request, template_name, context)


def Handle404View(request, exception):
    template_name = 'home/404.html'
    return render(request, template_name)


def Handle500View(request):
    template_name = 'home/500.html'
    return render(request, template_name)