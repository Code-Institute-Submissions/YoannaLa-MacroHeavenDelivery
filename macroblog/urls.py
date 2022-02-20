from . import views
from django.urls import path


urlpatterns = [
    path('macroblog', views.PostList.as_view(), name='macroblog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostDetail.as_view(), name='post_like'),
  
]
