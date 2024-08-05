from django.urls import path
from .views import HomeView, PostCreateView, PostDetailView, like_post
from .views_search import UserSearchView
app_name = 'webapp'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('search/', UserSearchView.as_view(), name='user_search'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('like/', like_post, name='like_post'),
]

