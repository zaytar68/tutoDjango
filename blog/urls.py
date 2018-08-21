from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'$', views.post_list, name='post-list'),
    path('', views.post_list, name='post-list'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    ]
