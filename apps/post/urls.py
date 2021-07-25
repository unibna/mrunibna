from django.urls import path

from .views import CategoryList, CategoryDetail
from .views import PostList, PostDetail, PostCreate

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<slug:slug>', CategoryDetail.as_view(), name='category_detail'),

    path('post-create', PostCreate.as_view(), name='post_create'),
    path('post/<slug:slug>', PostDetail.as_view(), name='post_detail'),
]
